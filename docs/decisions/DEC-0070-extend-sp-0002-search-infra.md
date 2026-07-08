---
id: DEC-0070
type: decision
title: SP-0002 is extended to evaluate search/vector infrastructure alongside the graph engine
status: superseded
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0008 @ T4-T5"
links:
  derives-from: [SES-0008]
---

# DEC-0070: Extend [SP-0002](../spikes/SP-0002-postgres-pgvector-graduation.md) with the search workload

## Context

Search needs an engine (embeddings + full-text,
[DEC-0067](DEC-0067-retrieval-owns-search.md)); the candidates overlap
[SP-0002](../spikes/SP-0002-postgres-pgvector-graduation.md)'s almost entirely — pgvector + FTS rides the same Postgres being
evaluated with Apache AGE, embedded vector indexes pair with the embedded
graph option, and dedicated stores share the same on-prem ops criteria.

## Decision

[SP-0002](../spikes/SP-0002-postgres-pgvector-graduation.md) is extended to
evaluate the retrieval workload: pgvector + Postgres full-text vs. an
embedded vector index vs. a dedicated vector store, measured on the same
corpus and criteria as the graph candidates. The spike returns one
coherent infrastructure recommendation covering graph and search.

## Rationale

Two spikes would prototype the same Postgres instance twice; graph and
search infrastructure choices interact (shared engine vs. two systems) and
should be judged together.

## Alternatives Considered

- **Separate `SP-0003`**: near-total overlap in candidates and criteria.
- **Pick pgvector now**: "probably right" is what spikes exist to test.

## Implications

[SP-0002](../spikes/SP-0002-postgres-pgvector-graduation.md)'s timebox extends (5d → 7d); embedding-model versioning and
re-embed mechanics are contract-level regardless of the engine outcome.
