---
id: SP-0003
type: spike
title: HNSW index adoption for DuckDB vector search at scale
status: deferred
release: backlog
owner: eng-lead
created: 2026-07-07
timebox: 3d
links:
  derives-from: [EP-0007]
  satisfies: [BG-0001]
  relates-to: [SP-0002]
cites: [DEC-0114, DEC-0115, DEC-0119]
---

# SP-0003: HNSW Index Adoption for DuckDB Vector Search at Scale

> Deferred to `backlog` at creation (per
> [DEC-0115](../decisions/DEC-0115-sp-0003-hnsw-deferred.md), the
> deferral citation per
> [DEC-0100](../decisions/DEC-0100-scope-moves-cite-decisions.md)).
> Revived when `TRG-0003` in the [trigger registry](../TRIGGERS.md)
> fires — alongside co-subscriber
> [SP-0002](SP-0002-postgres-pgvector-graduation.md), which evaluates
> the competing answer (graduate off embedded storage entirely).

## Question

At what corpus/query scale does the DuckDB vector search (skill tooling
today, the system's search per
[DEC-0102](../decisions/DEC-0102-v1-embedded-stack.md) tomorrow)
outgrow exact brute-force scanning
([DEC-0114](../decisions/DEC-0114-no-persisted-hnsw.md)) — and if HNSW
via the vss extension is the answer, how are its two documented hazards
handled: experimental index persistence (WAL-corruption risk on unclean
shutdown) and the `top_k`-CTE-only query pattern that plain `WHERE`
clauses silently bypass, which today gives us exact, free pre-filtering
([DEC-0119](../decisions/DEC-0119-hybrid-retrieval-semantics.md))?

## Why It Blocks

Nothing, currently — deferred; brute force is measured at ~35 ms over
922 chunks (2026-07-07 baseline,
[SES-0019](../sessions/SES-0019-semantic-search-hybrid-tooling.md)
POC). When `TRG-0003` fires:
search-latency-sensitive work blocks on choosing between in-place HNSW
(this spike) and infrastructure graduation
([SP-0002](SP-0002-postgres-pgvector-graduation.md)).

## Method

1. Reproduce the firing condition: measure brute-force latency at the
   actual corpus size that triggered, and at 10× that.
2. Benchmark HNSW (vss) against it: build time, query latency, recall
   loss, and behavior under the filtered-query patterns the hybrid
   semantics depend on (`--current`, `--type`, `--within` — the
   `WHERE`-bypass problem may force query restructuring into `top_k`
   CTEs plus post-filtering, with recall consequences).
3. Evaluate persistence strategies: experimental persisted index vs
   rebuild-in-memory-on-open (index build cost amortized per session)
   vs accepting rebuild-from-embeddings on corruption (the index file
   is derived and disposable by design).
4. Compare outcomes against
   [SP-0002](SP-0002-postgres-pgvector-graduation.md)'s pgvector
   evaluation on the same corpus — one decision should choose between
   in-place indexing and graduation.
5. Record findings as Decisions per
   [DEC-0023](../decisions/DEC-0023-spike-findings-become-decisions.md).

## Findings

Pending — filled at completion.

## Resulting Decisions

Pending — at minimum: index-or-graduate, and the persistence strategy
if indexing.
