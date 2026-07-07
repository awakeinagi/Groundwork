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
                       derived, sessions producing no decisions.
  order [TYPE]         Impact-ranked refinement order among unapproved
                       artifacts of TYPE (default: epic).
  elements [ETYPE]     Design-element inventory across components.
  stats                Node/edge counts and most-connected artifacts.

Options:
  --root PATH   Project root containing docs/ (default: cwd).
  --db PATH     Database file (default: <root>/.groundwork-graph).
  --json        Emit rows as JSON instead of aligned text.

Schema:
  (:Artifact {id, type, title, status, owner, created, path, context,
              component_type, source_span})
  (:Element {key, name, etype, component})
  Artifact-[:DERIVES {ltype}]->Artifact     derives-from | satisfies
  Artifact-[:IMPACTS]->Artifact             impacts (impacted-by = inverse)
  Artifact-[:DEPENDS_ON]->Artifact
  Artifact-[:CONFLICTS_WITH]->Artifact
  Artifact-[:SUPERSEDES]->Artifact
  Artifact-[:RELATES_TO]->Artifact
  Artifact-[:CITES]->Artifact
  Artifact-[:HAS_ELEMENT]->Element

Unresolved link/cite targets become placeholder nodes with
type = status = 'missing' so gaps stay queryable.
"""

import argparse
import json
import re
import sys
from pathlib import Path

import ladybug
import yaml

SKIP_DIRS = {"specs"}
ID_RE = re.compile(r"^(BG|EP|ST|SP|CMP|SES|DEC|CFL|CON|CP)-\d{4}$")
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
              "SUPERSEDES", "RELATES_TO", "CITES"]

DDL = [
    "CREATE NODE TABLE Artifact(id STRING PRIMARY KEY, type STRING, "
    "title STRING, status STRING, owner STRING, created STRING, "
    "path STRING, context STRING, component_type STRING, source_span STRING)",
    "CREATE NODE TABLE Element(key STRING PRIMARY KEY, name STRING, "
    "etype STRING, component STRING)",
    "CREATE REL TABLE DERIVES(FROM Artifact TO Artifact, ltype STRING)",
    "CREATE REL TABLE IMPACTS(FROM Artifact TO Artifact)",
    "CREATE REL TABLE DEPENDS_ON(FROM Artifact TO Artifact)",
    "CREATE REL TABLE CONFLICTS_WITH(FROM Artifact TO Artifact)",
    "CREATE REL TABLE SUPERSEDES(FROM Artifact TO Artifact)",
    "CREATE REL TABLE RELATES_TO(FROM Artifact TO Artifact)",
    "CREATE REL TABLE CITES(FROM Artifact TO Artifact)",
    "CREATE REL TABLE HAS_ELEMENT(FROM Artifact TO Element)",
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
            elements = ELEMENT_HEADING_RE.findall(section.group(1))
    return {
        "id": str(fm["id"]),
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
        for rel, ltype, target in pairs:
            self.ensure_placeholder(target)
            prop = " {ltype: $lt}" if ltype else ""
            self.conn.execute(
                f"MATCH (a:Artifact {{id: $a}}), (b:Artifact {{id: $b}}) "
                f"MERGE (a)-[r:{rel}{prop}]->(b)",
                {"a": aid, "b": target, **({"lt": ltype} if ltype else {})})
        for name, etype in art["elements"]:
            self.conn.execute(
                "MERGE (e:Element {key: $k}) SET e.name=$n, e.etype=$t, "
                "e.component=$c",
                {"k": f"{aid}/{name}", "n": name, "t": etype, "c": aid})
            self.conn.execute(
                "MATCH (a:Artifact {id: $a}), (e:Element {key: $k}) "
                "MERGE (a)-[:HAS_ELEMENT]->(e)", {"a": aid, "k": f"{aid}/{name}"})

    def delete_artifact(self, aid):
        self.drop_edges_and_elements(aid)
        self.conn.execute("MATCH (a:Artifact {id: $id}) DETACH DELETE a",
                          {"id": aid})


def emit(rows, as_json, empty="  (none)"):
    if as_json:
        print(json.dumps(rows, indent=2))
        return
    if not rows:
        print(empty)
        return
    cols = list(rows[0].keys())
    widths = {c: max(len(c), *(len(str(r.get(c, ""))) for r in rows))
              for c in cols}
    print("  " + "  ".join(c.ljust(widths[c]) for c in cols))
    for r in rows:
        print("  " + "  ".join(str(r.get(c, "")).ljust(widths[c])
                               for c in cols))


def cmd_build(g, root, args):
    arts = scan_docs(root)
    for art in arts.values():
        g.upsert_artifact(art)
    for art in arts.values():
        g.add_edges(art)
    n = g.rows("MATCH (a:Artifact) RETURN count(a) AS n")[0]["n"]
    e = sum(g.rows(f"MATCH ()-[r:{t}]->() RETURN count(r) AS n")[0]["n"]
            for t in REL_TABLES)
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
         + "RETURN e.component AS component, e.name AS element, "
           "e.etype AS type ORDER BY component, element")
    emit(g.rows(q, {"t": args.etype} if args.etype else {}), args.json)


def cmd_stats(g, root, args):
    print("Artifacts by type/status:")
    emit(g.rows(
        "MATCH (a:Artifact) WHERE a.type <> 'missing' "
        "RETURN a.type AS type, a.status AS status, count(a) AS n "
        "ORDER BY type, status"), args.json)
    edges = [{"rel": t,
              "n": g.rows(f"MATCH ()-[r:{t}]->() RETURN count(r) AS n")[0]["n"]}
             for t in REL_TABLES]
    print("\nEdges:")
    emit(edges, args.json)
    print("\nMost-connected artifacts (in+out degree, top 10):")
    emit(g.rows(
        "MATCH (a:Artifact)-[r]-() WHERE a.type <> 'missing' "
        "RETURN a.id AS id, a.type AS type, count(r) AS degree, "
        "a.title AS title ORDER BY degree DESC, id LIMIT 10"), args.json)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", default=".", help="project root (has docs/)")
    ap.add_argument("--db", default=None, help="database file path")
    ap.add_argument("--json", action="store_true", help="JSON output")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("build")
    p = sub.add_parser("sync")
    p.add_argument("targets", nargs="+", metavar="PATH|ID")
    p = sub.add_parser("query")
    p.add_argument("cypher")
    for name in ("impact", "trace"):
        p = sub.add_parser(name)
        p.add_argument("id")
    sub.add_parser("gaps")
    p = sub.add_parser("order")
    p.add_argument("type", nargs="?", default="epic")
    p = sub.add_parser("elements")
    p.add_argument("etype", nargs="?", default=None)
    sub.add_parser("stats")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    db_path = Path(args.db) if args.db else root / ".groundwork-graph"
    if args.cmd != "build" and not db_path.exists():
        sys.exit(f"No graph at {db_path} — run `build` first.")
    g = Graph(db_path, fresh=(args.cmd == "build"))
    {"build": cmd_build, "sync": cmd_sync, "query": cmd_query,
     "impact": cmd_impact, "trace": cmd_trace, "gaps": cmd_gaps,
     "order": cmd_order, "elements": cmd_elements,
     "stats": cmd_stats}[args.cmd](g, root, args)


if __name__ == "__main__":
    main()
