---
id: SP-0002
type: spike
title: Postgres + pgvector graduation evaluation
status: deferred
release: backlog
owner: eng-lead
created: 2026-07-06
timebox: 7d
links:
  derives-from: [EP-0004]
  satisfies: [BG-0001]
  relates-to: [SP-0001, EP-0007]
cites: [DEC-0061, DEC-0062, DEC-0059, DEC-0060, DEC-0064, DEC-0070,
        DEC-0102, DEC-0105]
---

# SP-0002: Postgres + pgvector Graduation Evaluation

> Re-scoped by [DEC-0105](../decisions/DEC-0105-sp-0002-rescoped-deferred.md)
> (the deferral citation per
> [DEC-0100](../decisions/DEC-0100-scope-moves-cite-decisions.md)).
> Originally "Graph Engine Selection", approved 2026-07-06 — the v1
> engine question was answered by
> [DEC-0102](../decisions/DEC-0102-v1-embedded-stack.md): embedded
> LadybugDB (graph) + DuckDB (app database + vector search). Deferred to
> `backlog`; revived when any of `TRG-0001`–`TRG-0004` in the
> [trigger registry](../TRIGGERS.md) fires.

## Question

When a graduation trigger fires, how should Groundwork move from the
embedded v1 stack (LadybugDB graph, DuckDB app database +
vector/semantic search, per
[DEC-0102](../decisions/DEC-0102-v1-embedded-stack.md)) to Postgres +
pgvector (or equivalent server-grade infrastructure) — while preserving
the contracts it must serve: main + per-branch overlays
([DEC-0059](../decisions/DEC-0059-main-plus-branch-overlays.md)),
session-synchronous overlay writes
([DEC-0060](../decisions/DEC-0060-session-sync-global-async.md)), the
three-tier query API with **read-only guarded openCypher as a hard
requirement** ([DEC-0062](../decisions/DEC-0062-tiered-query-api.md)),
fast deterministic rebuilds
([DEC-0064](../decisions/DEC-0064-scheduled-rebuild-diff.md)), and
self-hosted enterprise operations
([DEC-0050](../decisions/DEC-0050-bitbucket-datacenter-v1.md))?

## Why It Blocks

Nothing, currently — this spike is deferred and blocks no sibling work.
When a trigger fires: multi-node deployment stories and any
scale-dependent contract adjustments block on its findings.

## Method

1. Establish which trigger fired and what it demands (HA? concurrent
   writers? scale? policy?) — the answer shapes the target: Postgres +
   pgvector alone vs. Postgres plus a graph answer (Apache AGE,
   recursive CTEs, or retaining LadybugDB behind the Graph Index's
   derived-view boundary — the index is rebuildable, so graph and app
   storage may graduate independently).
2. Prototype the openCypher tier
   ([DEC-0062](../decisions/DEC-0062-tiered-query-api.md)) and overlay
   semantics ([DEC-0059](../decisions/DEC-0059-main-plus-branch-overlays.md))
   on the candidate target; measure against the embedded baseline on the
   real corpus at current scale plus the projected scale that fired the
   trigger.
3. Evaluate pgvector + Postgres full-text against the DuckDB search
   baseline for the retrieval contract
   ([DEC-0067](../decisions/DEC-0067-retrieval-owns-search.md)),
   including re-embed cost at scale for embedding-model swaps.
4. Define the migration path: dual-write vs. rebuild-and-cutover (the
   Graph Index rebuilds from canon by design, per
   [DEC-0064](../decisions/DEC-0064-scheduled-rebuild-diff.md); the app
   database and outbox
   ([DEC-0103](../decisions/DEC-0103-outbox-in-app-database.md)) need a
   real plan), the rollback story, and operational runbook deltas.
5. Record the graduation choice, migration plan, and any contract
   adjustments as Decisions per
   [DEC-0023](../decisions/DEC-0023-spike-findings-become-decisions.md).

## Findings

Pending — filled at completion.

## Resulting Decisions

Pending — at minimum: the graduation target and the migration approach.
