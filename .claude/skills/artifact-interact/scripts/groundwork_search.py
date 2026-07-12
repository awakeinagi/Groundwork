# /// script
# requires-python = ">=3.10"
# dependencies = ["duckdb", "model2vec", "numpy", "pyyaml"]
# ///
"""Groundwork semantic search + decision-recall audit.

Hybrid semantic search over the artifact corpus (DEC-0111, DEC-0116),
model2vec potion-base-8M static embeddings (DEC-0112), section- and
turn-level chunking (DEC-0113), brute-force similarity — no persisted
HNSW (DEC-0114), per-file hash freshness reconciled on every query
(DEC-0117), cite-ready two-tier output (DEC-0118), hybrid retrieval
semantics: superseded redirect, one-hop graph boost, subtree scoping,
metadata pre-filters, boilerplate dedupe (DEC-0119).

Commands:
  search "query" [--k N] [--type T] [--status S] [--current] [--turns]
                 [--within ID] [--no-boost]
  similar <ID> [--k N]
  audit <artifact-file-or-ID> [--k N]   decision-recall audit: accepted
                                        decisions relevant to the artifact
                                        but absent from its considered set
                                        (frontmatter cites + inline refs);
                                        emits a judge context packet
  build                                 force full index rebuild

Index lives in .groundwork-search (DuckDB) at the project root:
derived, disposable, gitignored — never a source of truth.
"""

import argparse
import contextlib
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

import duckdb
import numpy as np
import yaml
from model2vec import StaticModel

from groundwork_audit_packet import build_packet, rank_candidates

DIM = 256
DEC_RE = re.compile(r"DEC-\d{4}")
HEADING_RE = re.compile(r"^(#{1,4})\s+(.*)$", re.MULTILINE)
TURN_RE = re.compile(r"^\*\*T(\d+)[^.]*\.\*\*", re.MULTILINE)
ITEM_RE = re.compile(r"^(?:\d+\.|-)\s", re.MULTILINE)
LINK_KINDS = ("cites", "derives-from", "relates-to", "impacts", "impacted-by")


def parse_doc(path: Path):
    text = path.read_text()
    fm, body = {}, text
    if text.startswith("---"):
        try:
            end = text.index("\n---", 3)
            fm = yaml.safe_load(text[3:end]) or {}
            body = text[end + 4:]
        except (ValueError, yaml.YAMLError):
            pass
    return fm, body


def _split_items(name, chunk, out):
    header, text = chunk.split("\n", 1) if "\n" in chunk else (chunk, "")
    items = [m.start() for m in ITEM_RE.finditer(text)]
    if len(items) >= 2:
        out.append((name, None, chunk))
        bounds = items + [len(text)]
        for i in range(len(items)):
            item = text[bounds[i]:bounds[i + 1]].strip()
            if len(item) > 40:
                out.append((name, None, f"{header}\n{item}"))
    elif len(chunk) <= 1600:
        out.append((name, None, chunk))
    else:
        buf = ""
        for p in chunk.split("\n\n"):
            if len(buf) + len(p) > 1200 and buf:
                out.append((name, None, buf))
                buf = p
            else:
                buf = f"{buf}\n\n{p}" if buf else p
        if buf:
            out.append((name, None, buf))


def chunk_doc(fm, body):
    """-> [(section, turn, text)] ; sessions get per-turn chunks (DEC-0113)."""
    title = f"{fm.get('id', '')}: {fm.get('title', '')}".strip(": ")
    out = []
    heads = list(HEADING_RE.finditer(body))
    for i, m in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(body)
        sect_name, sect = m.group(2).strip(), body[m.end():end].strip()
        if not sect:
            continue
        if fm.get("type") == "session" and sect_name.lower() == "transcript":
            turns = list(TURN_RE.finditer(sect))
            for j, t in enumerate(turns):
                tend = turns[j + 1].start() if j + 1 < len(turns) else len(sect)
                out.append((sect_name, int(t.group(1)),
                            f"{title} — T{t.group(1)}\n{sect[t.start():tend].strip()}"))
            continue
        _split_items(sect_name, f"{title} — {sect_name}\n{sect}", out)
    if not heads and body.strip():
        out.append(("(body)", None, f"{title}\n{body.strip()}"))
    return out


def iter_docs(root: Path):
    for f in sorted((root / "docs").rglob("*.md")):
        fm, body = parse_doc(f)
        if fm.get("id"):
            yield f, fm, body


class Store:
    def __init__(self, root: Path):
        self.root = root
        self.model = None
        self.db = duckdb.connect(str(root / ".groundwork-search"))
        self.db.execute(f"""
            CREATE TABLE IF NOT EXISTS files(file TEXT PRIMARY KEY, hash TEXT);
            CREATE TABLE IF NOT EXISTS chunks(
                file TEXT, artifact TEXT, atype TEXT, status TEXT,
                section TEXT, turn INT, text TEXT, thash TEXT,
                emb FLOAT[{DIM}]);
            CREATE TABLE IF NOT EXISTS meta(
                artifact TEXT PRIMARY KEY, atype TEXT, status TEXT,
                title TEXT, file TEXT, links JSON);
        """)

    def _model(self):
        if self.model is None:
            # Third-party loaders (huggingface hub, tqdm) may chatter on
            # stdout; the audit packet owns stdout (IDEA-0027), so route
            # any load-time output to stderr.
            with contextlib.redirect_stdout(sys.stderr):
                self.model = StaticModel.from_pretrained(
                    "minishlab/potion-base-8M")
        return self.model

    def encode(self, texts):
        v = self._model().encode(texts)
        return v / (np.linalg.norm(v, axis=1, keepdims=True) + 1e-9)

    def refresh(self, force=False):
        """Per-file hash reconciliation on every invocation (DEC-0117)."""
        if force:
            self.db.execute("DELETE FROM files; DELETE FROM chunks; DELETE FROM meta")
        seen, stale = set(), []
        self.newest_doc_mtime = 0.0
        old = dict(self.db.execute("SELECT file, hash FROM files").fetchall())
        # Live docs/ scan under the shared corpus lock (DEC-0391,
        # DEC-0415): the index never snapshots a torn mid-apply state.
        # Embedding and DB writes below run on the in-memory copy,
        # after release.
        from gw_lock import read_lock
        with read_lock(self.root):
            for f, fm, body in iter_docs(self.root):
                rel = str(f.relative_to(self.root))
                seen.add(rel)
                self.newest_doc_mtime = max(self.newest_doc_mtime,
                                            f.stat().st_mtime)
                h = hashlib.sha1(f.read_bytes()).hexdigest()
                if old.get(rel) != h:
                    stale.append((rel, h, fm, body))
        gone = set(old) - seen
        for rel in gone:
            self.db.execute("DELETE FROM chunks WHERE file=?", [rel])
            self.db.execute("DELETE FROM files WHERE file=?", [rel])
            self.db.execute("DELETE FROM meta WHERE file=?", [rel])
        if not stale:
            return 0
        for rel, _h, _fm, _body in stale:
            self.db.execute("DELETE FROM chunks WHERE file=?", [rel])
        rows, texts, dedupe = [], [], set(
            r[0] for r in self.db.execute("SELECT DISTINCT thash FROM chunks").fetchall())
        for rel, h, fm, body in stale:
            self.db.execute(
                "INSERT OR REPLACE INTO meta VALUES (?,?,?,?,?,?)",
                [fm.get("id"), fm.get("type"), fm.get("status"),
                 fm.get("title", ""), rel,
                 json.dumps({k: (fm.get("links") or {}).get(k) or []
                             for k in LINK_KINDS}
                            | {"supersedes": (fm.get("links") or {}).get("supersedes") or []})])
            for sect, turn, text in chunk_doc(fm, body):
                th = hashlib.sha1(text.split("\n", 1)[-1].encode()).hexdigest()
                if th in dedupe:      # boilerplate dedupe (DEC-0119.6)
                    continue
                dedupe.add(th)
                rows.append([rel, fm.get("id"), fm.get("type"), fm.get("status"),
                             sect, turn, text, th])
                texts.append(text)
            self.db.execute("INSERT OR REPLACE INTO files VALUES (?,?)", [rel, h])
        if rows:
            vecs = self.encode(texts)
            self.db.executemany(
                "INSERT INTO chunks VALUES (?,?,?,?,?,?,?,?,?)",
                [r + [v.tolist()] for r, v in zip(rows, vecs)])
        return len(rows)

    # -- graph-ish helpers computed from frontmatter links ----------------
    def links(self):
        out = {}
        for a, lj in self.db.execute("SELECT artifact, links FROM meta").fetchall():
            out[a] = json.loads(lj)
        return out

    def redirect_map(self):
        red = {}
        for a, l in self.links().items():
            for old in l.get("supersedes", []):
                red[old] = a
        for old in list(red):
            tgt = red[old]
            while tgt in red:
                tgt = red[tgt]
            red[old] = tgt
        return red

    def descendants(self, rootid):
        kids = {}
        for a, l in self.links().items():
            for p in l.get("derives-from", []):
                kids.setdefault(p, set()).add(a)
        out, todo = set(), [rootid]
        while todo:
            n = todo.pop()
            for c in kids.get(n, ()):
                if c not in out:
                    out.add(c)
                    todo.append(c)
        return out | {rootid}

    def warn_graph_staleness(self):
        g = self.root / ".groundwork-graph"
        # Reuse the mtime high-water mark refresh() just computed rather
        # than re-parsing the whole corpus a second time (IDEA-0027).
        newest = getattr(self, "newest_doc_mtime", None)
        if newest is None:
            newest = max((f.stat().st_mtime
                          for f, _, _ in iter_docs(self.root)), default=0)
        if not g.exists() or g.stat().st_mtime < newest:
            print("WARNING: .groundwork-graph is stale or missing — provenance "
                  "features degrade; rebuild: uv run groundwork_graph.py "
                  "--root . build", file=sys.stderr)

    def matrix(self, where="1=1", params=()):
        rows = self.db.execute(
            f"SELECT artifact, atype, status, section, turn, text, emb "
            f"FROM chunks WHERE {where}", list(params)).fetchall()
        if not rows:
            return rows, np.zeros((0, DIM))
        return rows, np.array([r[6] for r in rows], dtype=np.float32)


def two_tier(store, rows, sims, k, boost=True, redirect=None):
    redirect = redirect or store.redirect_map()
    best, hits = {}, {}
    for i, r in enumerate(rows):
        a, s = r[0], float(sims[i])
        if a not in best or s > best[a]:
            best[a], hits[a] = s, r
    boosted = dict(best)
    if boost:
        links = store.links()
        for a in best:
            nb = [best[n] for n in
                  sum((links.get(a, {}).get(k2) or [] for k2 in LINK_KINDS), [])
                  if n in best]
            if nb:
                boosted[a] = best[a] + 0.25 * max(nb)
    arts = sorted(boosted, key=lambda a: -boosted[a])[:k]
    out = []
    for a in arts:
        r = hits[a]
        entry = {"artifact": a, "score": round(best[a], 3),
                 "boosted": round(boosted[a], 3), "type": r[1], "status": r[2],
                 "section": r[3] if r[4] is None else f"T{r[4]}",
                 "snippet": " ".join(r[5].split())[:150]}
        if r[2] == "superseded" and a in redirect:
            entry["superseded_by"] = redirect[a]
        out.append(entry)
    return out


def attach_overviews(store, entries, key="artifact"):
    """Include each hit's overview (DEC-0290) — read from the file at
    emit time so the index stays overview-free and disposable."""
    for e in entries:
        row = store.db.execute("SELECT file FROM meta WHERE artifact=?",
                               [e[key]]).fetchone()
        if not row:
            continue
        fm, _ = parse_doc(store.root / row[0])
        ov = fm.get("overview")
        if ov:
            e["overview"] = " ".join(str(ov).split())


def considered_set(fm, body, redirect):
    ids = set(fm.get("cites") or []) | set(DEC_RE.findall(body))
    for i in list(ids):
        if i in redirect:
            ids.add(redirect[i])
    return ids


def cmd_audit(store, target, k, output=None):
    redirect = store.redirect_map()
    path = Path(target)
    if not path.exists():  # allow bare artifact ID
        row = store.db.execute("SELECT file FROM meta WHERE artifact=?",
                               [target]).fetchone()
        if not row:
            sys.exit(f"no such artifact: {target}")
        path = store.root / row[0]
    fm, body = parse_doc(path)
    considered = considered_set(fm, body, redirect)
    chunks = chunk_doc(fm, body)
    qv = store.encode([c[2] for c in chunks])
    rows, mat = store.matrix("atype='decision' AND status='accepted'")
    sims = qv @ mat.T
    best = {}
    for qi in range(sims.shape[0]):
        for ri in range(sims.shape[1]):
            did = rows[ri][0]
            if did in considered or did == fm.get("id"):
                continue
            s = float(sims[qi, ri])
            if did not in best or s > best[did][0]:
                best[did] = (s, chunks[qi][0], rows[ri][3])
    meta = {a: (t, st, ti) for a, t, st, ti in store.db.execute(
        "SELECT artifact, atype, status, title FROM meta").fetchall()}
    # The audited artifact travels IN the packet — judges never evaluate
    # blind (IDEA-0027); assembly is pure/model-free for testability.
    artifact = {
        "id": fm.get("id", str(path)),
        "title": str(fm.get("title", "")),
        "overview": " ".join(str(fm.get("overview") or "").split()),
        "body": body.strip(),
    }
    packet = build_packet(artifact, considered, rank_candidates(best, k),
                          meta)
    attach_overviews(store, packet["candidates"], key="id")
    text = json.dumps(packet, indent=2)
    if output:
        Path(output).write_text(text + "\n", encoding="utf-8")
        print(f"packet -> {output}")
    else:
        print(text)


def main():
    ap = argparse.ArgumentParser(
        description="Hybrid semantic search and decision-recall audit "
        "over a Groundwork corpus (DEC-0111..DEC-0119). The index "
        "(.groundwork-search, DuckDB) is derived and disposable; "
        "per-file hash freshness reconciles on every invocation.",
        epilog="examples:\n"
        "  groundwork_search.py --root . search 'write serialization' "
        "--k 8\n"
        "  groundwork_search.py --root . search 'gate policy' "
        "--type decision --current\n"
        "  groundwork_search.py --root . similar IDEA-0034\n"
        "  groundwork_search.py --root . audit SES-0077 "
        "--output packet.json\n"
        "run via the gw dispatcher: gw.py --root <root> search ...",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=".", type=Path,
                    help="project root containing docs/ (default: cwd)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser(
        "search", help="semantic search over corpus chunks",
        description="Rank artifacts by chunk similarity to the query; "
        "two-tier output with overviews (DEC-0290), superseded "
        "redirects, and one-hop graph boost (DEC-0119).")
    s.add_argument("query", help="natural-language query")
    s.add_argument("--k", type=int, default=8,
                   help="artifacts to return (default 8)")
    s.add_argument("--type", help="filter by artifact type")
    s.add_argument("--status", help="filter by status")
    s.add_argument("--current", action="store_true",
                   help="exclude superseded and stale artifacts")
    s.add_argument("--turns", action="store_true",
                   help="match session transcript turns only")
    s.add_argument("--within", metavar="ID",
                   help="limit to the derives-from subtree of ID")
    s.add_argument("--no-boost", action="store_true",
                   help="disable the one-hop graph neighbor boost")
    s.add_argument("--no-overviews", action="store_true",
                   help="omit hit overviews from the output")
    m = sub.add_parser(
        "similar", help="artifacts most similar to a given one",
        description="Rank artifacts by similarity to the mean "
        "embedding of the given artifact's chunks (duplicate hunting).")
    m.add_argument("id", help="artifact ID")
    m.add_argument("--k", type=int, default=8,
                   help="artifacts to return (default 8)")
    m.add_argument("--no-overviews", action="store_true",
                   help="omit hit overviews from the output")
    a = sub.add_parser(
        "audit", help="decision-recall audit judge packet",
        description="Rank accepted decisions relevant to the artifact "
        "but absent from its considered set (cites + inline refs, "
        "superseded-redirected) and emit the self-sufficient judge "
        "packet (DEC-0405): the artifact's own title/overview/body, "
        "candidate overviews and scores, deterministic ordering.")
    a.add_argument("artifact", help="artifact ID or file path")
    a.add_argument("--k", type=int, default=15,
                   help="candidates to rank (default 15)")
    a.add_argument("--output", metavar="PATH",
                   help="write the packet JSON to PATH instead of stdout "
                        "(defends the machine-parsed stream, IDEA-0027)")
    sub.add_parser(
        "build", help="force a full index rebuild",
        description="Delete and rebuild the whole index; normally "
        "unnecessary (per-file freshness reconciles every run).")
    args = ap.parse_args()

    store = Store(args.root)
    t0 = time.time()
    n = store.refresh(force=args.cmd == "build")
    store.warn_graph_staleness()
    if args.cmd == "build":
        print(f"indexed {n} chunks in {time.time()-t0:.2f}s")
        return
    if args.cmd == "audit":
        cmd_audit(store, args.artifact, args.k, args.output)
        return

    where, params = ["1=1"], []
    if args.cmd == "search":
        if args.type:
            where.append("atype=?"); params.append(args.type)
        if args.status:
            where.append("status=?"); params.append(args.status)
        if args.current:
            where.append("status NOT IN ('superseded','stale')")
        if args.turns:
            where.append("turn IS NOT NULL")
        rows, mat = store.matrix(" AND ".join(where), params)
        if args.within:
            allowed = store.descendants(args.within)
            keep = [i for i, r in enumerate(rows) if r[0] in allowed]
            rows, mat = [rows[i] for i in keep], mat[keep]
        qv = store.encode([args.query])
        sims = (qv @ mat.T)[0]
        out = two_tier(store, rows, sims, args.k, boost=not args.no_boost)
    else:  # similar
        rows, mat = store.matrix()
        own = [i for i, r in enumerate(rows) if r[0] == args.id]
        if not own:
            sys.exit(f"no chunks for {args.id}")
        qv = mat[own].mean(axis=0, keepdims=True)
        qv = qv / np.linalg.norm(qv)
        sims = (qv @ mat.T)[0]
        rows2 = [(i, r) for i, r in enumerate(rows) if r[0] != args.id]
        idxs = [i for i, _ in rows2]
        out = two_tier(store, [r for _, r in rows2], sims[idxs], args.k)
    if not args.no_overviews:
        attach_overviews(store, out)
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        # Downstream consumer (head, less) closed the pipe — not an
        # error (IDEA-0048). Re-point stdout so interpreter shutdown
        # doesn't re-raise, and exit clean.
        os.dup2(os.open(os.devnull, os.O_WRONLY), sys.stdout.fileno())
        sys.exit(0)
