#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["ladybug<1.0", "pyyaml"]
# ///
"""Local queryable graph index for a Groundwork artifact tree (LadybugDB).

Run via uv, which installs dependencies into a temporary managed venv:

    uv run <skill>/scripts/groundwork_graph.py <command> [args] [options]

The graph is a DERIVED view of docs/ frontmatter (plus Design Element
headings in component docs). The markdown is always the source of truth:
never treat graph edits as design changes — edit the docs, then `sync`
or `build`. The database file (default `<root>/.groundwork-graph`) is
disposable and should be gitignored.

Commands:
  build                Rebuild the whole graph from docs/ (drop + recreate).
  sync PATH|ID ...     Incrementally re-index changed/deleted artifacts.
  query CYPHER         Run raw openCypher against the graph.
  impact ID            Downstream blast radius: derives/satisfies
                       descendants (would go stale), citers, impact-edge
                       neighbors, dependents.
  trace ID             Upstream provenance: ancestor chain to business
                       goal(s) + cited decisions with source-spans.
  gaps                 Cross-reference audit: unresolved refs, citations
                       of superseded decisions, uncited accepted
                       decisions, approved artifacts with nothing
                       derived, sessions producing no decisions,
                       approved stories no element implements.
  order [TYPE]         Impact-ranked refinement order among unapproved
                       artifacts of TYPE (default: epic).
  elements [ETYPE]     Design-element inventory across components, with
                       implemented stories and completeness.
  progress             Design percent-complete rollup: story -> epic ->
                       business goal, over Implements edges (DEC-0095).
  stats                Node/edge counts and most-connected artifacts.

Options:
  --root PATH   Project root containing docs/ (default: cwd).
  --db PATH     Database file (default: <root>/.groundwork-graph).
  --json        Emit rows as JSON instead of aligned text.

Schema:
  (:Artifact {id, type, title, status, owner, created, path, context,
              component_type, source_span})
  (:Element {key, name, etype, component, complete})
  Artifact-[:DERIVES {ltype}]->Artifact     derives-from | satisfies
  Artifact-[:IMPACTS]->Artifact             impacts (impacted-by = inverse)
  Artifact-[:DEPENDS_ON]->Artifact
  Artifact-[:CONFLICTS_WITH]->Artifact
  Artifact-[:SUPERSEDES]->Artifact
  Artifact-[:RELATES_TO]->Artifact
  Artifact-[:CITES]->Artifact
  Artifact-[:HAS_ELEMENT]->Element
  Element-[:IMPLEMENTS]->Artifact           element's Implements: stories
  Artifact-[:MENTIONS]->Artifact            bare-ID reference in body prose
                                            (DEC-0251; code spans excluded)

Element.complete is a heuristic for "design-complete" (DEC-0095): the
element's block contains at least one of its own contract items
(<Name>.<B|A|D>-<n>) and no "Pending" marker. The tier-2 suite is the
real judge; this powers the progress estimate.

Unresolved link/cite targets become placeholder nodes with
type = status = 'missing' so gaps stay queryable.
"""

import argparse
import json
import re
import sys
import textwrap
from pathlib import Path

import ladybug
import yaml

SKIP_DIRS = {"specs"}
ID_RE = re.compile(r"^(BG|EP|ST|SP|CMP|SES|DEC|CFL|CON|CP|IDEA)-\d{4}$")
ELEMENT_HEADING_RE = re.compile(r"^###\s+(\S+)\s+\(([^)]*)\)\s*$", re.MULTILINE)
DESIGN_ELEMENTS_RE = re.compile(r"^## Design Elements\s*$(.*?)(?=^## |\Z)",
                                re.MULTILINE | re.DOTALL)
LINK_TO_REL = {
    "derives-from": ("DERIVES", "derives-from"),
    "satisfies": ("DERIVES", "satisfies"),
    "impacts": ("IMPACTS", None),
    "depends-on": ("DEPENDS_ON", None),
    "conflicts-with": ("CONFLICTS_WITH", None),
    "supersedes": ("SUPERSEDES", None),
    "relates-to": ("RELATES_TO", None),
    # impacted-by is the inverse of impacts; stored once in impacts direction
}
REL_TABLES = ["DERIVES", "IMPACTS", "DEPENDS_ON", "CONFLICTS_WITH",
              "SUPERSEDES", "RELATES_TO", "CITES", "MENTIONS"]
IMPLEMENTS_RE = re.compile(r"^Implements:", re.MULTILINE)
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
BARE_ID_RE = re.compile(r"\b(?:BG|EP|ST|SP|CMP|SES|DEC|CFL|CON|CP|IDEA)-\d{4}\b")
FENCED_CODE_RE = re.compile(r"```.*?(?:```|\Z)", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")

DDL = [
    "CREATE NODE TABLE Artifact(id STRING PRIMARY KEY, type STRING, "
    "title STRING, status STRING, owner STRING, created STRING, "
    "path STRING, context STRING, component_type STRING, source_span STRING)",
    "CREATE NODE TABLE Element(key STRING PRIMARY KEY, name STRING, "
    "etype STRING, component STRING, complete BOOLEAN)",
    "CREATE REL TABLE DERIVES(FROM Artifact TO Artifact, ltype STRING)",
    "CREATE REL TABLE IMPACTS(FROM Artifact TO Artifact)",
    "CREATE REL TABLE DEPENDS_ON(FROM Artifact TO Artifact)",
    "CREATE REL TABLE CONFLICTS_WITH(FROM Artifact TO Artifact)",
    "CREATE REL TABLE SUPERSEDES(FROM Artifact TO Artifact)",
    "CREATE REL TABLE RELATES_TO(FROM Artifact TO Artifact)",
    "CREATE REL TABLE CITES(FROM Artifact TO Artifact)",
    "CREATE REL TABLE HAS_ELEMENT(FROM Artifact TO Element)",
    "CREATE REL TABLE IMPLEMENTS(FROM Element TO Artifact)",
    "CREATE REL TABLE MENTIONS(FROM Artifact TO Artifact)",
]


def parse_artifact(path, root):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return None
    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return None
    if not isinstance(fm, dict) or not ID_RE.match(str(fm.get("id", ""))):
        return None
    body = text[m.end():]
    elements = []
    if fm.get("type") == "component":
        section = DESIGN_ELEMENTS_RE.search(body)
        if section:
            sec = section.group(1)
            heads = list(ELEMENT_HEADING_RE.finditer(sec))
            for i, h in enumerate(heads):
                name, etype = h.group(1), h.group(2)
                end = heads[i + 1].start() if i + 1 < len(heads) else len(sec)
                block = sec[h.end():end]
                stories = []
                stripped = block.lstrip("\n")
                if stripped.startswith("Implements:"):
                    para = stripped.split("\n\n", 1)[0]
                    stories = [s for s in dict.fromkeys(
                        BARE_ID_RE.findall(para)) if s.startswith("ST-")]
                complete = ("Pending" not in block and
                            re.search(rf"{re.escape(name)}\.[BAD]-\d+",
                                      block) is not None)
                elements.append({"name": name, "etype": etype,
                                 "stories": stories, "complete": complete})
    prose = INLINE_CODE_RE.sub("", FENCED_CODE_RE.sub("", body))
    own = str(fm["id"])
    mentions = sorted(set(BARE_ID_RE.findall(MD_LINK_RE.sub("", prose)))
                      - {own})
    return {
        "id": own,
        "props": {
            "type": str(fm.get("type") or ""),
            "title": str(fm.get("title") or ""),
            "status": str(fm.get("status") or ""),
            "owner": str(fm.get("owner") or ""),
            "created": str(fm.get("created") or ""),
            "path": str(path.relative_to(root)),
            "context": str(fm.get("context") or ""),
            "component_type": str(fm.get("component-type") or ""),
            "source_span": str(fm.get("source-span") or ""),
        },
        "links": fm.get("links") or {},
        "cites": fm.get("cites") or [],
        "mentions": mentions,
        "elements": elements,
    }


def scan_docs(root):
    docs = root / "docs"
    if not docs.is_dir():
        sys.exit(f"No docs/ under {root} — not a Groundwork project?")
    out = {}
    for path in sorted(docs.rglob("*.md")):
        if path.parent.name in SKIP_DIRS:
            continue
        art = parse_artifact(path, root)
        if art:
            out[art["id"]] = art
    return out


def as_list(v):
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


class Graph:
    def __init__(self, db_path, fresh=False):
        if fresh and db_path.exists():
            db_path.unlink()
        existed = db_path.exists()
        self.conn = ladybug.Connection(ladybug.Database(str(db_path)))
        if not existed:
            for stmt in DDL:
                self.conn.execute(stmt)

    def rows(self, cypher, params=None):
        res = self.conn.execute(cypher, params or {})
        cols = res.get_column_names()
        out = []
        while res.has_next():
            out.append(dict(zip(cols, res.get_next())))
        return out

    def upsert_artifact(self, art):
        self.conn.execute(
            "MERGE (a:Artifact {id: $id}) SET a.type=$type, a.title=$title, "
            "a.status=$status, a.owner=$owner, a.created=$created, "
            "a.path=$path, a.context=$context, "
            "a.component_type=$component_type, a.source_span=$source_span",
            {"id": art["id"], **art["props"]})

    def ensure_placeholder(self, target):
        self.conn.execute(
            "MERGE (a:Artifact {id: $id}) "
            "ON CREATE SET a.type='missing', a.status='missing', a.title='', "
            "a.owner='', a.created='', a.path='', a.context='', "
            "a.component_type='', a.source_span=''",
            {"id": target})

    def drop_edges_and_elements(self, aid):
        for rel in REL_TABLES:
            self.conn.execute(
                f"MATCH (a:Artifact {{id: $id}})-[r:{rel}]->() DELETE r",
                {"id": aid})
        self.conn.execute(
            "MATCH (a:Artifact {id: $id})-[:HAS_ELEMENT]->(e:Element) "
            "DETACH DELETE e", {"id": aid})

    def add_edges(self, art):
        aid = art["id"]
        pairs = []
        for ltype, targets in art["links"].items():
            spec = LINK_TO_REL.get(ltype)
            if spec is None:
                continue  # impacted-by (inverse) and unknown types
            for t in as_list(targets):
                pairs.append((spec[0], spec[1], str(t)))
        for t in as_list(art["cites"]):
            pairs.append(("CITES", None, str(t)))
        for t in art.get("mentions", []):
            pairs.append(("MENTIONS", None, t))
        for rel, ltype, target in pairs:
            self.ensure_placeholder(target)
            prop = " {ltype: $lt}" if ltype else ""
            self.conn.execute(
                f"MATCH (a:Artifact {{id: $a}}), (b:Artifact {{id: $b}}) "
                f"MERGE (a)-[r:{rel}{prop}]->(b)",
                {"a": aid, "b": target, **({"lt": ltype} if ltype else {})})
        for el in art["elements"]:
            key = f"{aid}/{el['name']}"
            self.conn.execute(
                "MERGE (e:Element {key: $k}) SET e.name=$n, e.etype=$t, "
                "e.component=$c, e.complete=$done",
                {"k": key, "n": el["name"], "t": el["etype"], "c": aid,
                 "done": el["complete"]})
            self.conn.execute(
                "MATCH (a:Artifact {id: $a}), (e:Element {key: $k}) "
                "MERGE (a)-[:HAS_ELEMENT]->(e)", {"a": aid, "k": key})
            for sid in el["stories"]:
                self.ensure_placeholder(sid)
                self.conn.execute(
                    "MATCH (e:Element {key: $k}), (s:Artifact {id: $s}) "
                    "MERGE (e)-[:IMPLEMENTS]->(s)", {"k": key, "s": sid})

    def delete_artifact(self, aid):
        self.drop_edges_and_elements(aid)
        self.conn.execute("MATCH (a:Artifact {id: $id}) DETACH DELETE a",
                          {"id": aid})


OVERVIEWS = {}  # id -> overview text; filled in main() per DEC-0290


def load_overviews(root):
    """Read overviews from frontmatter at emit time (DEC-0290) — the
    graph DB stays overview-free and disposable."""
    ov = {}
    docs = root / "docs"
    if not docs.is_dir():
        return ov
    for path in sorted(docs.rglob("*.md")):
        if path.parent.name in SKIP_DIRS:
            continue
        try:
            text = path.read_text()
            end = text.index("\n---", 3)
            fm = yaml.safe_load(text[3:end]) or {}
        except (OSError, ValueError, yaml.YAMLError):
            continue
        if isinstance(fm, dict) and fm.get("id") and fm.get("overview"):
            ov[str(fm["id"])] = " ".join(str(fm["overview"]).split())
    return ov


def emit(rows, as_json, empty="  (none)"):
    if OVERVIEWS:
        for r in rows:
            key = r.get("id") or r.get("artifact")
            if key in OVERVIEWS and "overview" not in r:
                r["overview"] = OVERVIEWS[key]
    if as_json:
        print(json.dumps(rows, indent=2))
        return
    if not rows:
        print(empty)
        return
    cols = [c for c in rows[0].keys() if c != "overview"]
    widths = {c: max(len(c), *(len(str(r.get(c, ""))) for r in rows))
              for c in cols}
    print("  " + "  ".join(c.ljust(widths[c]) for c in cols))
    for r in rows:
        print("  " + "  ".join(str(r.get(c, "")).ljust(widths[c])
                               for c in cols))
        if r.get("overview"):
            print(textwrap.fill(r["overview"], width=78,
                                initial_indent="      ",
                                subsequent_indent="      "))


def cmd_build(g, root, args):
    arts = scan_docs(root)
    for art in arts.values():
        g.upsert_artifact(art)
    for art in arts.values():
        g.add_edges(art)
    n = g.rows("MATCH (a:Artifact) RETURN count(a) AS n")[0]["n"]
    e = sum(g.rows(f"MATCH ()-[r:{t}]->() RETURN count(r) AS n")[0]["n"]
            for t in REL_TABLES + ["IMPLEMENTS"])
    el = g.rows("MATCH (e:Element) RETURN count(e) AS n")[0]["n"]
    print(f"Built: {n} artifacts, {e} edges, {el} elements "
          f"({len(arts)} docs scanned)")


def cmd_sync(g, root, args):
    for ref in args.targets:
        path = (root / ref) if not ID_RE.match(ref) else None
        if path is None:  # bare ID: find its current file, if any
            hits = [p for p in (root / "docs").rglob(f"{ref}-*.md")
                    if p.parent.name not in SKIP_DIRS]
            path = hits[0] if hits else None
            aid = ref
        else:
            m = re.match(r"([A-Z]+-\d{4})-", Path(ref).name)
            aid = m.group(1) if m else None
        if path is None or not path.exists():
            if aid:
                g.delete_artifact(aid)
                print(f"deleted {aid} (no file)")
            else:
                print(f"skip {ref}: cannot determine artifact id")
            continue
        art = parse_artifact(path, root)
        if not art:
            print(f"skip {ref}: unparseable frontmatter")
            continue
        g.upsert_artifact(art)
        g.drop_edges_and_elements(art["id"])
        g.add_edges(art)
        print(f"synced {art['id']}")


def cmd_query(g, root, args):
    emit(g.rows(args.cypher), args.json)


def cmd_impact(g, root, args):
    aid = args.id
    print(f"Impact of a change to {aid}:")
    print("\nDerivation descendants (would be marked stale):")
    emit(g.rows(
        "MATCH (d:Artifact)-[:DERIVES*1..20]->(a:Artifact {id: $id}) "
        "RETURN DISTINCT d.id AS id, d.type AS type, d.status AS status, "
        "d.title AS title ORDER BY id", {"id": aid}), args.json)
    print("\nCiters (rest on its decisions/content):")
    emit(g.rows(
        "MATCH (c:Artifact)-[:CITES]->(a:Artifact {id: $id}) "
        "RETURN c.id AS id, c.type AS type, c.status AS status, "
        "c.title AS title ORDER BY id", {"id": aid}), args.json)
    print("\nImpact-edge neighbors (decisions here shape them):")
    emit(g.rows(
        "MATCH (a:Artifact {id: $id})-[:IMPACTS]->(s:Artifact) "
        "RETURN s.id AS id, s.status AS status, s.title AS title "
        "ORDER BY id", {"id": aid}), args.json)
    print("\nDependents (consume its contracts):")
    emit(g.rows(
        "MATCH (d:Artifact)-[:DEPENDS_ON]->(a:Artifact {id: $id}) "
        "RETURN d.id AS id, d.status AS status, d.title AS title "
        "ORDER BY id", {"id": aid}), args.json)


def cmd_trace(g, root, args):
    aid = args.id
    print(f"Provenance of {aid}:")
    print("\nAncestors (derives-from/satisfies closure):")
    emit(g.rows(
        "MATCH (a:Artifact {id: $id})-[:DERIVES*1..20]->(p:Artifact) "
        "RETURN DISTINCT p.id AS id, p.type AS type, p.status AS status, "
        "p.title AS title ORDER BY id", {"id": aid}), args.json)
    print("\nDecisions cited (with source spans):")
    emit(g.rows(
        "MATCH (a:Artifact {id: $id})-[:CITES]->(d:Artifact) "
        "OPTIONAL MATCH (d)-[:DERIVES]->(s:Artifact) "
        "RETURN d.id AS id, d.status AS status, d.source_span AS span, "
        "s.id AS from_session, d.title AS title ORDER BY id",
        {"id": aid}), args.json)


def cmd_gaps(g, root, args):
    print("Unresolved references (placeholder targets):")
    emit(g.rows(
        "MATCH (m:Artifact {type: 'missing'}) "
        "OPTIONAL MATCH (x:Artifact)-[]->(m) "
        "RETURN m.id AS missing_id, collect(DISTINCT x.id) AS referenced_by"),
        args.json)
    print("\nArtifacts citing superseded decisions:")
    emit(g.rows(
        "MATCH (x:Artifact)-[:CITES]->(d:Artifact {status: 'superseded'}) "
        "WHERE x.status <> 'superseded' "
        "OPTIONAL MATCH (n:Artifact)-[:SUPERSEDES]->(d) "
        "RETURN x.id AS artifact, x.status AS status, d.id AS cites, "
        "n.id AS superseded_by ORDER BY artifact"), args.json)
    print("\nAccepted decisions cited by nothing:")
    emit(g.rows(
        "MATCH (d:Artifact {type: 'decision', status: 'accepted'}) "
        "OPTIONAL MATCH (x:Artifact)-[:CITES]->(d) "
        "WITH d, count(x) AS c WHERE c = 0 "
        "RETURN d.id AS id, d.title AS title ORDER BY id"), args.json)
    print("\nApproved artifacts with nothing derived (frontier):")
    emit(g.rows(
        "MATCH (a:Artifact {status: 'approved'}) "
        "WHERE a.type IN ['business-goal', 'epic'] "
        "OPTIONAL MATCH (d:Artifact)-[:DERIVES]->(a) "
        "WITH a, count(d) AS c WHERE c = 0 "
        "RETURN a.id AS id, a.type AS type, a.title AS title ORDER BY id"),
        args.json)
    print("\nClosed sessions that produced no decisions:")
    emit(g.rows(
        "MATCH (s:Artifact {type: 'session'}) "
        "OPTIONAL MATCH (d:Artifact {type: 'decision'})-[:DERIVES]->(s) "
        "WITH s, count(d) AS c WHERE c = 0 "
        "RETURN s.id AS id, s.title AS title ORDER BY id"), args.json)
    print("\nApproved stories no design element implements (DEC-0093):")
    emit(g.rows(
        "MATCH (s:Artifact {type: 'story', status: 'approved'}) "
        "OPTIONAL MATCH (e:Element)-[:IMPLEMENTS]->(s) "
        "WITH s, count(e) AS c WHERE c = 0 "
        "RETURN s.id AS id, s.title AS title ORDER BY id"), args.json)
    print("\nDerived children unlisted in parent body (DEC-0246):")
    emit(g.rows(
        "MATCH (c:Artifact)-[r:DERIVES]->(p:Artifact) "
        "WHERE r.ltype = 'derives-from' "
        "AND p.type IN ['business-goal', 'epic'] "
        "OPTIONAL MATCH (p)-[m:MENTIONS]->(c) "
        "WITH p, c, count(m) AS n WHERE n = 0 "
        "RETURN p.id AS parent, c.id AS unlisted_child "
        "ORDER BY parent, unlisted_child"), args.json)
    print("\nDead cites — cited, never referenced in prose (DEC-0247):")
    emit(g.rows(
        "MATCH (a:Artifact)-[:CITES]->(d:Artifact) "
        "WHERE a.type IN ['business-goal', 'epic', 'story', 'spike', "
        "'component'] AND d.type <> 'missing' "
        "OPTIONAL MATCH (a)-[m:MENTIONS]->(d) "
        "WITH a, d, count(m) AS n WHERE n = 0 "
        "RETURN a.id AS artifact, d.id AS dead_cite "
        "ORDER BY artifact, dead_cite"), args.json)
    print("\nDecisions referenced in prose but uncited (DEC-0247):")
    emit(g.rows(
        "MATCH (a:Artifact)-[:MENTIONS]->(d:Artifact {type: 'decision'}) "
        "WHERE a.type IN ['business-goal', 'epic', 'story', 'spike', "
        "'component'] "
        "OPTIONAL MATCH (a)-[l:CITES|RELATES_TO|DERIVES|SUPERSEDES|"
        "IMPACTS|DEPENDS_ON|CONFLICTS_WITH]->(d) "
        "WITH a, d, count(l) AS n WHERE n = 0 "
        "RETURN a.id AS artifact, d.id AS uncited_mention "
        "ORDER BY artifact, uncited_mention"), args.json)
    print("\nImpact edges unexplained in the impactor's prose (DEC-0249):")
    emit(g.rows(
        "MATCH (a:Artifact)-[:IMPACTS]->(t:Artifact) "
        "OPTIONAL MATCH (a)-[m:MENTIONS]->(t) "
        "WITH a, t, count(m) AS n WHERE n = 0 "
        "RETURN a.id AS impactor, t.id AS unexplained_target "
        "ORDER BY impactor, unexplained_target"), args.json)
    print("\nSession relates-to targets unmentioned in body (DEC-0250):")
    emit(g.rows(
        "MATCH (s:Artifact {type: 'session'})-[:RELATES_TO]->(t:Artifact) "
        "OPTIONAL MATCH (s)-[m:MENTIONS]->(t) "
        "WITH s, t, count(m) AS n WHERE n = 0 "
        "RETURN s.id AS session, t.id AS unmentioned_target "
        "ORDER BY session, unmentioned_target"), args.json)


def cmd_order(g, root, args):
    t = args.type
    rows = g.rows(
        "MATCH (a:Artifact {type: $t}) "
        "WHERE NOT a.status IN ['approved', 'superseded', 'archived', "
        "'missing'] "
        "OPTIONAL MATCH (a)-[:IMPACTS]->(out:Artifact) "
        "OPTIONAL MATCH (inn:Artifact)-[:IMPACTS]->(a) "
        "WHERE inn.status <> 'approved' "
        "RETURN a.id AS id, a.status AS status, "
        "count(DISTINCT out) AS impact_fanout, "
        "collect(DISTINCT inn.id) AS unsettled_impactors, "
        "a.title AS title", {"t": t})
    for r in rows:
        r["unsettled_impactors"] = [x for x in r["unsettled_impactors"] or []
                                    if x]
        r["ready"] = "yes" if not r["unsettled_impactors"] else "no"
    rows.sort(key=lambda r: (r["ready"] != "yes", -r["impact_fanout"],
                             r["id"]))
    print(f"Refinement order among unapproved '{t}' artifacts "
          f"(ready = all impactors approved; rank by impact fan-out):")
    emit([{k: r[k] for k in
           ("id", "status", "ready", "impact_fanout",
            "unsettled_impactors", "title")} for r in rows], args.json)


def cmd_elements(g, root, args):
    q = ("MATCH (c:Artifact)-[:HAS_ELEMENT]->(e:Element) "
         + ("WHERE e.etype = $t " if args.etype else "")
         + "OPTIONAL MATCH (e)-[:IMPLEMENTS]->(s:Artifact) "
           "RETURN e.component AS component, e.name AS element, "
           "e.etype AS type, e.complete AS complete, "
           "collect(s.id) AS implements ORDER BY component, element")
    emit(g.rows(q, {"t": args.etype} if args.etype else {}), args.json)


def cmd_progress(g, root, args):
    live = "NOT %s.status IN ['superseded', 'archived', 'missing']"
    stories = g.rows(
        f"MATCH (s:Artifact {{type: 'story'}}) WHERE {live % 's'} "
        "OPTIONAL MATCH (e:Element)-[:IMPLEMENTS]->(s) "
        "RETURN s.id AS id, s.status AS status, s.title AS title, "
        "count(e) AS elements, "
        "sum(CASE WHEN e.complete THEN 1 ELSE 0 END) AS complete "
        "ORDER BY id")
    for r in stories:
        r["design_pct"] = round(100 * r["complete"] / r["elements"]) \
            if r["elements"] else 0
        if not r["elements"]:
            r["title"] += "  [uncovered]"
    print("Story design % (complete elements / referencing elements; "
          "uncovered = 0%):")
    emit([{k: r[k] for k in ("id", "status", "elements", "complete",
                             "design_pct", "title")} for r in stories],
         args.json)
    pct = {r["id"]: r["design_pct"] for r in stories}
    for child, parent, label in (("story", "epic", "Epic"),
                                 ("epic", "business-goal", "Business goal")):
        groups = g.rows(
            f"MATCH (c:Artifact {{type: '{child}'}})-[:DERIVES]->"
            f"(p:Artifact {{type: '{parent}'}}) "
            f"WHERE {live % 'c'} AND {live % 'p'} "
            "RETURN DISTINCT p.id AS parent, c.id AS child ORDER BY parent")
        agg = {}
        for row in groups:
            agg.setdefault(row["parent"], []).append(
                pct.get(row["child"], 0))
        rows = [{"id": p, "children": len(v),
                 "design_pct": round(sum(v) / len(v))}
                for p, v in sorted(agg.items())]
        for r in rows:
            pct[r["id"]] = r["design_pct"]
        print(f"\n{label} design % (equal-weighted over direct children):")
        emit(rows, args.json)


def cmd_stats(g, root, args):
    print("Artifacts by type/status:")
    emit(g.rows(
        "MATCH (a:Artifact) WHERE a.type <> 'missing' "
        "RETURN a.type AS type, a.status AS status, count(a) AS n "
        "ORDER BY type, status"), args.json)
    edges = [{"rel": t,
              "n": g.rows(f"MATCH ()-[r:{t}]->() RETURN count(r) AS n")[0]["n"]}
             for t in REL_TABLES + ["IMPLEMENTS"]]
    print("\nEdges:")
    emit(edges, args.json)
    print("\nMost-connected artifacts (in+out degree, top 10):")
    emit(g.rows(
        "MATCH (a:Artifact)-[r]-() WHERE a.type <> 'missing' "
        "RETURN a.id AS id, a.type AS type, count(r) AS degree, "
        "a.title AS title ORDER BY degree DESC, id LIMIT 10"), args.json)


EPILOG = """\
quick start:
  uv run groundwork_graph.py --root /path/to/project build
  uv run groundwork_graph.py --root /path/to/project gaps

examples:
  build                                  rebuild after many doc edits
  sync docs/epics/EP-0002-foo.md         re-index one edited file
  sync ST-0004 DEC-0091                  re-index by artifact ID
  impact DEC-0011                        who goes stale if this changes?
  trace CMP-0001                         why does this exist? which DECs?
  order story                            what should be refined next?
  elements protocol                      all protocol elements across CMPs
  progress                               design % per story/epic/goal
  query "MATCH (a:Artifact {status:'gated'}) RETURN a.id, a.title"
  --json query "..."                     machine-readable output

The graph is a DERIVED view: markdown under docs/ is always the source
of truth. Edit docs first, then `sync` (or `build` — it is cheap).
Full schema + a Cypher recipe cookbook: references/graph-queries.md
(next to this script's skill). Run `<command> --help` for details.
"""

COMMANDS = {
    "build": ("rebuild the whole graph from docs/",
              "Drop and recreate the database from every artifact's "
              "frontmatter, plus Design Element headings in component "
              "docs. Cheap (seconds); when in doubt, rebuild rather "
              "than sync. Unresolved link/cite targets become "
              "placeholder nodes (type='missing') so gaps stay "
              "queryable."),
    "sync": ("incrementally re-index changed or deleted artifacts",
             "Re-parse the given files (or artifact IDs) and replace "
             "their nodes, outgoing edges, and elements. If the file "
             "is gone, the node is deleted. Docs stay canonical: sync "
             "reflects doc edits into the graph, never the reverse. "
             "Note: placeholders created by OTHER artifacts are only "
             "cleaned up by a full `build`."),
    "query": ("run raw openCypher against the graph",
              "One positional argument: the Cypher string (quote it). "
              "Node tables: Artifact(id, type, title, status, owner, "
              "created, path, context, component_type, source_span), "
              "Element(key, name, etype, component). Rel tables: "
              "DERIVES{ltype} (child->parent: derives-from/satisfies), "
              "IMPACTS (X impacts Y), DEPENDS_ON, CONFLICTS_WITH, "
              "SUPERSEDES (new->old), RELATES_TO, CITES "
              "(artifact->decision), HAS_ELEMENT (component->element). "
              "Mutating queries are allowed but are for what-if "
              "exploration only — rebuild to reset."),
    "impact": ("downstream blast radius of changing an artifact",
               "Four views of what a change to ID touches: derivation "
               "descendants (the set that would be marked stale), "
               "citers (artifacts resting on it — key for decisions "
               "about to be superseded), impact-edge neighbors "
               "(siblings its refinement shapes), and dependents "
               "(components consuming its contracts). Run BEFORE "
               "superseding a decision or amending an approved "
               "artifact."),
    "trace": ("upstream provenance of an artifact",
              "Ancestor chain to the business goal(s) via "
              "derives-from/satisfies, plus every decision the "
              "artifact cites with its source-span and originating "
              "session. Answers: why does this exist, and who decided "
              "what, where?"),
    "gaps": ("audit the cross-reference graph for holes",
             "Six checks: unresolved references (missing targets), "
             "artifacts still citing superseded decisions, accepted "
             "decisions cited by nothing, approved goals/epics with "
             "nothing derived yet (the refinement frontier), closed "
             "sessions that produced no decisions, and approved "
             "stories no design element implements (DEC-0093 "
             "design-coverage gaps)."),
    "order": ("impact-ranked refinement order among siblings",
              "For unapproved artifacts of TYPE: ready = every "
              "artifact that impacts it is approved; ranked by how "
              "many siblings their own refinement will shape "
              "(impact fan-out). Refine ready items with the largest "
              "fan-out first."),
    "elements": ("design-element inventory across components",
                 "Every `### <Name> (<type>)` element declared in "
                 "component docs, optionally filtered to one type, "
                 "with the stories each element implements (DEC-0092) "
                 "and its design-complete heuristic. Useful for "
                 "spotting seam-graduation candidates and reviewing "
                 "the element model as a whole."),
    "progress": ("design percent-complete rollup over Implements edges",
                 "The DEC-0095 design metric: per story, the fraction "
                 "of referencing elements that are design-complete "
                 "(no Pending content, own contract items present); "
                 "uncovered stories read 0%. Epics and business goals "
                 "average their direct children equally. An estimate, "
                 "not project management; implementation % lives "
                 "projection-side (Jira join), outside this tool."),
    "stats": ("node/edge counts and most-connected artifacts",
              "Artifact counts by type and status, edge counts per "
              "relationship table, and the ten highest-degree "
              "artifacts (the load-bearing neighborhoods)."),
}


def main():
    ap = argparse.ArgumentParser(
        prog="groundwork_graph.py",
        description="Local queryable graph index for a Groundwork "
                    "artifact tree (LadybugDB / openCypher). Built from "
                    "docs/ frontmatter links + Design Element headings; "
                    "a derived, disposable view — docs are the source "
                    "of truth.",
        epilog=EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=".",
                    help="project root containing docs/ (default: cwd)")
    ap.add_argument("--db", default=None,
                    help="database file (default: <root>/.groundwork-graph;"
                         " keep it gitignored)")
    ap.add_argument("--json", action="store_true",
                    help="emit result rows as JSON instead of aligned text")
    ap.add_argument("--no-overviews", action="store_true",
                    help="suppress artifact overviews in listing output "
                         "(included by default per DEC-0290)")
    sub = ap.add_subparsers(dest="cmd", required=True,
                            metavar="COMMAND")
    ps = {name: sub.add_parser(name, help=h, description=f"{h}. {d}")
          for name, (h, d) in COMMANDS.items()}
    ps["sync"].add_argument(
        "targets", nargs="+", metavar="PATH|ID",
        help="artifact file path (relative to --root) or bare ID "
             "(e.g. EP-0002); a missing file deletes the node")
    ps["query"].add_argument(
        "cypher", help="openCypher statement (single quoted argument)")
    for name in ("impact", "trace"):
        ps[name].add_argument("id", help="artifact ID, e.g. DEC-0011")
    ps["order"].add_argument(
        "type", nargs="?", default="epic",
        help="artifact type: business-goal | epic | story | spike | "
             "component (default: epic)")
    ps["elements"].add_argument(
        "etype", nargs="?", default=None,
        help="filter to one element type: entity | value | service | "
             "event | protocol (default: all)")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    db_path = Path(args.db) if args.db else root / ".groundwork-graph"
    if args.cmd != "build" and not db_path.exists():
        sys.exit(f"No graph at {db_path} — run `build` first.")
    g = Graph(db_path, fresh=(args.cmd == "build"))
    if not args.no_overviews and args.cmd in (
            "impact", "trace", "order", "gaps", "elements"):
        OVERVIEWS.update(load_overviews(root))
    {"build": cmd_build, "sync": cmd_sync, "query": cmd_query,
     "impact": cmd_impact, "trace": cmd_trace, "gaps": cmd_gaps,
     "order": cmd_order, "elements": cmd_elements,
     "progress": cmd_progress, "stats": cmd_stats}[args.cmd](g, root, args)


if __name__ == "__main__":
    main()
