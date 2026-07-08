---
id: DEC-0116
type: decision
title: Search ships as a separate script with its own gitignored DuckDB index file
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0019 @ T5-T6, T9"
links:
  derives-from: [SES-0019]
  relates-to: [DEC-0111, DEC-0119]
---

# DEC-0116: Separate Search Script and Gitignored Index File

## Context

The skill already ships `scripts/groundwork_graph.py` (LadybugDB, uv
inline dependencies, disposable `.groundwork-graph` file). The search
capability needed a home: extend that script or stand alone?

## Decision

Search is a **separate script, `scripts/groundwork_search.py`**, with
its own uv inline metadata (`duckdb`, `duckdb-extensions`,
`duckdb-extension-vss`, `model2vec`, plus `ladybug<1.0` opened
**read-only** for the hybrid graph features, `pyyaml`, `numpy`,
`pyarrow`). Its index lives in a sibling **`.groundwork-search`**
DuckDB file in the project root: derived view, disposable, rebuildable,
gitignored — never a source of truth, same discipline as
`.groundwork-graph`.

## Rationale

Independent tools fail independently: a broken embedding model never
blocks a graph query, and each stays runnable alone. The original
"separate dependency stacks" rationale weakened once the POC showed the
hybrid features need ladybug too (read-only opens of the live graph
verified working, no copy, no lock contention) — but the
independent-failure and lean-graph-venv arguments stand. The two
derived stores cannot share a file in any case: one is a LadybugDB
database, the other DuckDB.

## Alternatives Considered

- **Subcommand of `groundwork_graph.py`**: one entry point, but merges
  two dependency stacks into one venv, slows cold start for pure graph
  queries, and couples two derived views' failure modes.

## Implications

Project `.gitignore` gains `.groundwork-search` (and its WAL). The
search script treats the graph file as read-only input; it never writes
graph state ([DEC-0117](DEC-0117-index-freshness.md) covers its
staleness warning).
