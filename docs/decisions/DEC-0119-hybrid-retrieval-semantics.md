---
id: DEC-0119
type: decision
title: Hybrid retrieval — always-on superseded redirect, graph boost, subtree scoping, metadata pre-filters
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
overview: >-
  Search integrates the graph (read-only) with six semantics: current-truth
  redirect (superseded hits annotated with successors), graph-boosted artifact
  ranking (one-hop decay 0.25 over CITES/DERIVES/RELATES_TO/IMPACTS),
  subtree scoping (--within <ID>), metadata pre-filters (--type, --status,
  --current, --turns; WHERE clauses before ranking), similar <ID> neighbors,
  boilerplate deduplication at index time. Default is include-everything +
  annotate + redirect; pre-filters opt-in. Superseded text often best-matches;
  history questions legitimate.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0019 @ T8-T15"
links:
  derives-from: [SES-0019]
  relates-to: [DEC-0111, DEC-0113, DEC-0114, DEC-0118]
---

# DEC-0119: Hybrid Retrieval Semantics

## Context

POC 1 proved pure semantic search actively misleads on this corpus:
superseded decisions are immutable and stay forever, and for "which
database engine stores the graph and handles vector search" the top
hit was superseded DEC-0070
while current DEC-0102 sat at rank 10.
The graph knows what the vectors cannot: current truth, structure, and
scope.

## Decision

The search tool integrates the graph (read-only) with these semantics:

1. **Current-truth redirect, always on** — every hit on a `superseded`
   decision is annotated with its accepted successor via `SUPERSEDES`
   edges.
2. **Graph-boosted artifact ranking** — each artifact's best chunk
   score propagates one hop over `CITES`/`DERIVES`/`RELATES_TO`/
   `IMPACTS` edges with 0.25 decay; the boosted artifact tier heads the
   output (disable with `--no-boost`).
3. **Subtree scoping** — `--within <ID>` restricts hits to the graph's
   `DERIVES*` descendants of an artifact.
4. **Metadata pre-filters** — `--type` and `--status` flags, plus
   `--current` excluding `superseded`/`stale` rows; applied in DuckDB
   as `WHERE` clauses *before* similarity ranking (exact, and measured
   faster than unfiltered). A `--turns` filter searches transcript
   turns only (prior-art recall).
5. **`similar <ID>`** — semantic neighbors of an artifact, as an
   advisory supplement to graph impact analysis.
6. **Boilerplate dedupe at index time** — identical section bodies
   recurring across artifacts are indexed once.
7. **Provenance delegation** — hits stay lean; deep why-does-this-exist
   traversal belongs to the graph tool's `trace`.

Default retrieval is **include-everything + annotate + redirect**;
pre-filters are opt-in.

## Rationale

All POC-measured on the real corpus: the redirect fixed the misleading
query; boosting promoted the correct artifact set
(EP-0004,
SES-0017,
SP-0002,
DEC-0102) and demoted the four
identical "Derived Work — None yet" boilerplate hits that fooled cosine
similarity; `--current` brought
DEC-0102 from rank 10 into the top-8;
pre-filtering is exact
and free precisely because DEC-0114
chose brute force (vss's HNSW index is silently bypassed by `WHERE`
clauses). Include-all remains the default because superseded text is
often the best-matching text and history questions ("why did we
abandon Postgres?") are legitimate — the redirect makes stale hits
safe instead of hiding them.

## Alternatives Considered

- **Pure semantic search, no graph**: demonstrated misleading (rank-1
  superseded hit).
- **Filter superseded/stale out by default**: hides the best-matching
  trail and breaks history queries; kept opt-in as `--current`.
- **Inline provenance expansion per hit**: duplicated `trace`, noisily.

## Implications

The script depends on `ladybug<1.0` read-only
(DEC-0116) and warns
when the graph is stale (DEC-0117).
Boost weight (0.25, one hop) is a starting point, tunable with use.
