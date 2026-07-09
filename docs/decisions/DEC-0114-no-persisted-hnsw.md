---
id: DEC-0114
type: decision
title: Search is exact brute-force; no persisted HNSW index; the experimental persistence flag is never set
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
overview: >-
  Search uses exact brute-force cosine similarity over persistent DuckDB
  embeddings with no HNSW index; the experimental persistence flag is never
  set. Measured on ~922 chunks: ~35 ms per query; pre-filtered queries ~32 ms
  (faster because filtering is exact, bypassing any index). Brute force is
  exact, zero corruption risk, and removes experimental features. HNSW adoption
  is deferred to SP-0003 under TRG-0003 at corpus scale.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0019 @ T3-T4, T9, T15"
links:
  derives-from: [SES-0019]
  relates-to: [DEC-0111, DEC-0115]
---

# DEC-0114: Exact Brute-Force Search, No Persisted HNSW

## Context

The reference blog post builds an HNSW index via the vss extension and
documents two sharp edges: HNSW **persistence is experimental**
(`hnsw_enable_experimental_persistence`, with WAL-corruption risk on
unclean shutdown), and the index is only used inside a `top_k` CTE —
plain `WHERE` clauses silently bypass it. The corpus is ~10³ chunks.

## Decision

The search tool stores embeddings in a persistent DuckDB file and
queries with **exact brute-force cosine similarity**
(`array_cosine_similarity`, full scan). No HNSW index is created; the
experimental persistence flag is never set. The vss extension stays
loaded (dogfood, distance functions, future readiness).

## Rationale

Measured on the real corpus: ~35 ms per query over 922 chunks, and
pre-filtered queries are *faster* (32 ms) because a scan has no index
to bypass — filtering is exact and free, which the HNSW path cannot
offer (its `WHERE`-bypass caveat). Brute force is exact, has zero
corruption risk, and removes the one experimental feature in the
stack. An approximate index earns nothing until the corpus grows by
orders of magnitude — which is precisely the condition `TRG-0003`
already watches.

## Alternatives Considered

- **Persisted HNSW per the blog**: exercises vss hardest, but adopts a
  documented corruption risk for a speedup unmeasurable at ~10³ rows.
- **HNSW rebuilt in-memory per query**: avoids the flag but pays index
  build on every search for no benefit at this scale.

## Implications

HNSW adoption is deferred to
SP-0003 under `TRG-0003`
(DEC-0115). Result quality is
exact by construction — no recall/accuracy trade-off to tune today.
