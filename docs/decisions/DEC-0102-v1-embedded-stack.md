---
id: DEC-0102
type: decision
title: v1 storage stack — embedded LadybugDB for graph, DuckDB for app database and vector search
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0017 @ T1-T3"
links:
  derives-from: [SES-0017]
  supersedes: [DEC-0061, DEC-0070]
  relates-to: [DEC-0062, DEC-0050, DEC-0105]
---

# DEC-0102: v1 Storage Stack — Embedded LadybugDB + DuckDB

## Context

Engine selection for the Graph Index was assigned to a prototype spike
([DEC-0061](DEC-0061-engine-via-spike.md)), extended to cover the
search/vector workload ([DEC-0070](DEC-0070-extend-sp-0002-search-infra.md)).
The sponsor has since committed the v1 stack directly, informed by real
usage rather than a prototype matrix.

## Decision

v1 uses embedded engines only:

- **Graph Index**: embedded **LadybugDB** (openCypher-native, satisfying
  the hard language requirement of
  [DEC-0062](DEC-0062-tiered-query-api.md)).
- **App database + vector/semantic search**: embedded **DuckDB**,
  serving the retrieval layer's search contract
  ([DEC-0067](DEC-0067-retrieval-owns-search.md)).

Postgres + pgvector are not in v1; their evaluation is deferred to the
re-scoped [SP-0002](../spikes/SP-0002-postgres-pgvector-graduation.md)
([DEC-0105](DEC-0105-sp-0002-rescoped-deferred.md)), revived when a
graduation trigger fires.

## Rationale

The embedded LadybugDB choice is evidence-backed: the design skill's own
graph tool has been running LadybugDB with openCypher over this
repository's artifact graph — the real bootstrap corpus named in the
original spike method. Embedded engines are the strongest answer to the
first-class ops-burden criterion
([DEC-0050](DEC-0050-bitbucket-datacenter-v1.md)): zero external
infrastructure for a self-hosted deployment. The consequence, recorded
openly: **v1 is single-process/single-writer** — the boundary the
graduation triggers watch.

## Alternatives Considered

- **Run [SP-0002](../spikes/SP-0002-postgres-pgvector-graduation.md)'s original prototype matrix as planned**: highest rigor, but
  the dogfood evidence already covers the openCypher fit, and the
  matrix's server-side candidates answer a question v1 no longer asks.
- **Postgres + AGE + pgvector now**: one engine for everything, but
  external infrastructure from day one and AGE maturity unverified.

## Implications

[DEC-0061](DEC-0061-engine-via-spike.md) and
[DEC-0070](DEC-0070-extend-sp-0002-search-infra.md) are superseded;
[EP-0004](../epics/EP-0004-graph-index.md) and
[EP-0007](../epics/EP-0007-consolidation-memory-layer.md) are amended
and go stale for re-affirmation. Engine-specific epic stories can now be
written against LadybugDB/DuckDB. Stack commitments land in Component
Doc Implementation Guidance → Constraints, decision-cited, per
[DEC-0085](DEC-0085-implementation-guidance-split.md). The change-event
outbox moves host per
[DEC-0103](DEC-0103-outbox-in-app-database.md).
