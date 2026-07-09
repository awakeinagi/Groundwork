---
id: DEC-0111
type: decision
title: The skill gains a semantic search tool on DuckDB + vss, pip-bundled, dogfooding DEC-0102
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0019 @ T1-T3, T16"
links:
  derives-from: [SES-0019]
  relates-to: [DEC-0102]
---

# DEC-0111: The Skill Gains a Semantic Search Tool on DuckDB + vss

## Context

The facilitation skill's local tooling had a queryable graph view
(LadybugDB) but no meaning-based retrieval over the artifact corpus.
DEC-0102 had already committed
Groundwork's v1 to embedded DuckDB for the app database and
vector/semantic search, with the skill's graph tool cited as dogfooding
evidence for the embedded graph half — the search half had no
equivalent.

## Decision

The skill's tooling gains semantic search built on **DuckDB with the
vss extension**, packaged via pip so it works offline: dependencies
`duckdb`, `duckdb-extensions`, and `duckdb-extension-vss`;
`import_extension("vss")` followed by `LOAD vss`, never a network
`INSTALL vss`. This dogfoods
DEC-0102's vector-search commitment
the same way the graph tool dogfoods embedded LadybugDB.

## Rationale

Same stack as the system being designed means every skill-tool session
generates evidence about the v1 storage decisions (it already surfaced
the `WHERE`-bypasses-HNSW behavior and extension-packaging facts). The
pip-bundled extension keeps the tool runnable offline in uv-managed
ephemeral venvs. Packaging was verified empirically in-session: bare
`LOAD vss` fails without the `duckdb-extensions` base package's
`import_extension()` copying the bundled binary into DuckDB's extension
directory — three packages, not the two originally proposed.

## Alternatives Considered

- **Runtime `INSTALL vss` from DuckDB's extension repo**: needs network
  at first run per DuckDB version; the participant explicitly directed
  the pip route
  (SES-0019 T2).
- **A non-DuckDB vector store (e.g., sqlite-vec, FAISS, chromadb)**:
  loses the dogfood alignment with
  DEC-0102 for no capability gain at
  this scale.

## Implications

The skill ships `scripts/groundwork_search.py`
(DEC-0116) with hybrid
graph integration (DEC-0119);
skill docs gain usage guidance and cookbook recipes
(DEC-0118).
