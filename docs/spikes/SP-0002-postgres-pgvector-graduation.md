---
id: SP-0002
type: spike
title: Postgres + pgvector graduation evaluation
status: deferred
release: backlog
owner: eng-lead
created: 2026-07-06
overview: >-
  Question: when a graduation trigger fires, how should Groundwork move
  from embedded v1 stack (LadybugDB graph, DuckDB app database plus
  vector search) to Postgres plus pgvector while preserving read-only
  guarded openCypher, main/branch overlays, session-synchronous writes,
  deterministic rebuilds, and self-hosted operations? Blocks no current
  work; multi-node deployment and scale-dependent stories block on its
  answer when a trigger fires. Method evaluates target choice (Postgres
  alone vs. Postgres plus graph answer), prototypes openCypher tier and
  overlays, evaluates pgvector/full-text retrieval, defines migration
  and rollback. Deferred to backlog; revived by TRG-0001..TRG-0004.
  Findings pending.
timebox: 7d
links:
  derives-from: [EP-0004]
  satisfies: [BG-0001]
  relates-to: [SP-0001, EP-0007]
cites: [DEC-0061, DEC-0062, DEC-0059, DEC-0060, DEC-0064, DEC-0070,
        DEC-0102, DEC-0105, DEC-0023, DEC-0050, DEC-0067, DEC-0100,
        DEC-0103]
---

# SP-0002: Postgres + pgvector Graduation Evaluation

> Re-scoped by DEC-0105
> (the deferral citation per
> DEC-0100).
> Originally "Graph Engine Selection", approved 2026-07-06 — the v1
> engine question was answered by
> DEC-0102: embedded
> LadybugDB (graph) + DuckDB (app database + vector search). The
> original charter derived from DEC-0061 (engine selection via this
> spike) as extended by DEC-0070 (search/vector infrastructure folded
> into the same evaluation) — both since superseded by DEC-0102.
> Deferred to
> `backlog`; revived when any of `TRG-0001`–`TRG-0004` in the
> [trigger registry](../TRIGGERS.md) fires.

## Question

When a graduation trigger fires, how should Groundwork move from the
embedded v1 stack (LadybugDB graph, DuckDB app database +
vector/semantic search, per
DEC-0102) to Postgres +
pgvector (or equivalent server-grade infrastructure) — while preserving
the contracts it must serve: main + per-branch overlays
(DEC-0059),
session-synchronous overlay writes
(DEC-0060), the
three-tier query API with **read-only guarded openCypher as a hard
requirement** (DEC-0062),
fast deterministic rebuilds
(DEC-0064), and
self-hosted enterprise operations
(DEC-0050)?

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
   (DEC-0062) and overlay
   semantics (DEC-0059)
   on the candidate target; measure against the embedded baseline on the
   real corpus at current scale plus the projected scale that fired the
   trigger.
3. Evaluate pgvector + Postgres full-text against the DuckDB search
   baseline for the retrieval contract
   (DEC-0067),
   including re-embed cost at scale for embedding-model swaps.
4. Define the migration path: dual-write vs. rebuild-and-cutover (the
   Graph Index rebuilds from canon by design, per
   DEC-0064; the app
   database and outbox
   (DEC-0103) need a
   real plan), the rollback story, and operational runbook deltas.
5. Record the graduation choice, migration plan, and any contract
   adjustments as Decisions per
   DEC-0023.

## Findings

Pending — filled at completion.

## Resulting Decisions

Pending — at minimum: the graduation target and the migration approach.
