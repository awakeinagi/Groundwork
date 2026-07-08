---
id: DEC-0121
type: decision
title: Four infrastructure ports — app database, vector store, embedding, graph store — as Protocol-element seams
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0020 @ T1-T3, T6-T7"
links:
  derives-from: [SES-0020]
  relates-to: [DEC-0102, DEC-0062, DEC-0067, DEC-0122]
---

# DEC-0121: Four Infrastructure Ports as Protocol-Element Seams

## Context

The participant made modularity a requirement: the embedding model
(local or external via REST APIs), the vector DB, and the app DB must
each be easily swappable/pluggable
([SES-0020](../sessions/SES-0020-pluggable-infrastructure-ports.md) T1).
The accepted v1 stack is embedded-only
([DEC-0102](../decisions/DEC-0102-v1-embedded-stack.md)) with
graduation deferred behind triggers
([SP-0002](../spikes/SP-0002-postgres-pgvector-graduation.md)) — a
graduation that is only cheap if the engines sit behind seams.

## Decision

Groundwork's architecture must expose **four infrastructure Ports**,
each defined as a Protocol design element in the owning component's
contract:

1. **App database port** — relational/transactional workload: outbox
   ([DEC-0103](DEC-0103-outbox-in-app-database.md)), bookkeeping,
   counters. Owned by the Canonical Store context
   ([EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md)).
2. **Vector store port** — embed/index/query over vectors. Owned by the
   retrieval layer
   ([EP-0007](../epics/EP-0007-consolidation-memory-layer.md), per
   [DEC-0067](DEC-0067-retrieval-owns-search.md)).
3. **Embedding port** — text → vector, satisfiable by a local model or
   an external model behind a REST API. Owned by the retrieval layer.
4. **Graph store port** — the openCypher-capable engine behind the
   Graph Index's executor boundary
   ([EP-0004](../epics/EP-0004-graph-index.md), language requirement per
   [DEC-0062](DEC-0062-tiered-query-api.md)).

Vector store and app database are **deliberately separate ports** even
though one DuckDB engine implements both in v1 — a future deployment
may split them without redesign. Consumers program against port
contracts only; no consumer touches an engine API directly.

**Scope**: this binds the Groundwork product. The facilitation skill's
local tooling (graph/search scripts,
[DEC-0111](DEC-0111-skill-semantic-search-duckdb-vss.md)–[DEC-0120](DEC-0120-v1-scope-and-backlog-capture.md))
stays hard-wired to its embedded stack — its value is being trivially
runnable.

## Rationale

The graph engine was added to the participant's list of three because
LadybugDB is the engine the graduation spike most explicitly targets;
excluding it would hard-wire the engine most likely to be swapped. The
port split mirrors how the workloads would actually diverge under
graduation (Postgres app DB + dedicated vector DB is a plausible
end-state). Protocol elements are the existing Groundwork mechanism for
capability seams — no new artifact machinery needed.

## Alternatives Considered

- **Only the three named capabilities** — leaves the graph engine a
  direct dependency; graduating it becomes a refactor.
- **One combined storage port** — simpler surface, but couples the swap
  decisions: vector search cannot move off DuckDB without moving the
  outbox too.
- **Binding the skill tooling as well** — more consistent dogfooding,
  rejected as configuration surface on tools whose value is zero-config.
