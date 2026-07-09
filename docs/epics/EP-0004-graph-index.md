---
id: EP-0004
type: epic
title: Cross-Reference Graph Index
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-07
owner: eng-lead
created: 2026-07-05
links:
  derives-from: [BG-0001]
  satisfies: [BG-0001]
  depends-on: [EP-0001]
  impacts: [EP-0007, EP-0008]
  impacted-by: [EP-0001, EP-0002, EP-0003]
cites: [DEC-0002, DEC-0009, DEC-0010, DEC-0026, DEC-0056, DEC-0059, DEC-0060,
        DEC-0102, DEC-0062, DEC-0063, DEC-0064, DEC-0105, DEC-0121, DEC-0122,
        DEC-0124]
---

# EP-0004: Cross-Reference Graph Index

## Summary

A queryable graph over the typed links and citations in artifact
frontmatter — strictly a derived, rebuildable projection of the canonical
store, maintained as a main base view plus a thin overlay per open item
branch. Serves three query tiers (named traversals, a bounded generic
primitive, and read-only guarded openCypher) to agents, the gate engine,
the UI, and manifest generation.

## Why (Goal Alignment)

The cross-reference system (typed links over stable IDs, DEC-0009) is
BG-0001's alignment backbone; the Graph Index
makes it efficiently navigable at scale
(DEC-0010) without
compromising single-source-of-truth
(DEC-0002) — including for
drafts mid-refinement under the fork-pull model
(DEC-0059).

## Scope

**In** (refined at SES-0007):

- **View model** (DEC-0059):
  main base + per-item-branch overlays; view-parameterized queries;
  ref/status tagging on every result; overlay lifecycle bound to item
  branches.
- **Freshness** (DEC-0060):
  synchronous writes to the writer's overlay (read-your-writes for
  sessions); async propagation elsewhere via the change-event stream;
  rebuild output as the correctness definition.
- **Query tiers** (DEC-0062):
  named traversals (trace-to-goal, subtree, impact-neighborhood, cited-by,
  conflict-neighborhood, build-order); bounded generic traversal primitive
  for agent tools (DEC-0056);
  read-only openCypher endpoint with depth/time/result guards. The
  impact-neighborhood traversal walks the directional impact links
  (DEC-0026).
- **Content depth** (DEC-0063):
  frontmatter metadata only; bodies fetched from the store; text/semantic
  search explicitly deferred to the retrieval layer (EP-0007).
- **Verification** (DEC-0064):
  scheduled rebuild-and-diff with alarming and atomic replacement;
  deterministic `rebuild(ref) → index`.
- **Path-usage telemetry**: consumer-tagged traversal statistics (edge
  heat, no participant content) feeding consolidation placement (EP-0007).

**Out:** engine internals beyond the committed embedded engine —
LadybugDB per DEC-0102;
graduation to server-grade infrastructure (deferred
SP-0002, revived by
the [trigger registry](../TRIGGERS.md)); what
callers do with results; canonical link data itself (EP-0001 owns and
validates it); text search (EP-0007's neighborhood).

## Domain Context

Bounded context: **Graph Index**. Terms: Graph Index, Branch Overlay,
Provenance Chain, typed link vocabulary — per [CONTEXT.md](../../CONTEXT.md)
and [SPEC-artifact-common](../specs/SPEC-artifact-common.md).

## Interfaces & Contracts to Define

- **Graph query API**: the three tiers, language-neutral (OpenAPI), view
  parameter mandatory; engine hidden behind the executor boundary.
- **Graph store port** (DEC-0121):
  the executor boundary formalized as a Protocol seam — an
  openCypher-capable engine contract
  (DEC-0062); adapters
  config-selected with a conformance suite
  (DEC-0122); v1
  ships the LadybugDB adapter only
  (DEC-0124). EP-0008's Composition Root binds this port to the v1
  adapter at startup — the contract decided here constrains that
  platform wiring (the EP-0004→EP-0008 impact edge).
- **Rebuild contract**: `rebuild(canonical-ref) → index`, deterministic;
  diff format for verification runs.
- **Overlay lifecycle contract**: create/update/drop tied to item-branch
  events from EP-0001's change stream.
- **Path-usage telemetry schema**: consumed by EP-0007.

## Risks & Open Questions

- Embedded-engine scale limits (overlay memory/cost at high concurrent
  session counts, rebuild time at corpus growth) — watched by the armed
  graduation triggers in the [trigger registry](../TRIGGERS.md); crossing
  them revives SP-0002
  (per DEC-0102,
  DEC-0105).
- Guard calibration for the openCypher tier (limits tight enough to
  protect, loose enough to be useful) — story-level tuning.

## Derived Work

- SP-0002 — Postgres +
  pgvector graduation evaluation (originally the engine-selection spike,
  drafted during this epic's refinement; re-scoped and deferred per
  DEC-0105).
