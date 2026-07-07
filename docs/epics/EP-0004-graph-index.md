---
id: EP-0004
type: epic
title: Cross-Reference Graph Index
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-06
owner: eng-lead
created: 2026-07-05
links:
  derives-from: [BG-0001]
  satisfies: [BG-0001]
  depends-on: [EP-0001]
  impacts: [EP-0007]
  impacted-by: [EP-0001, EP-0002, EP-0003]
cites: [DEC-0009, DEC-0010, DEC-0026, DEC-0056, DEC-0059, DEC-0060, DEC-0061,
        DEC-0062, DEC-0063, DEC-0064]
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

The cross-reference system is [BG-0001](../goals/BG-0001-groundwork.md)'s alignment backbone; the Graph Index
makes it efficiently navigable at scale
([DEC-0010](../decisions/DEC-0010-graph-index-derived.md)) without
compromising single-source-of-truth
([DEC-0002](../decisions/DEC-0002-doc-store-canonical.md)) — including for
drafts mid-refinement under the fork-pull model
([DEC-0059](../decisions/DEC-0059-main-plus-branch-overlays.md)).

## Scope

**In** (refined at [SES-0007](../sessions/SES-0007-ep-0004-refinement.md)):

- **View model** ([DEC-0059](../decisions/DEC-0059-main-plus-branch-overlays.md)):
  main base + per-item-branch overlays; view-parameterized queries;
  ref/status tagging on every result; overlay lifecycle bound to item
  branches.
- **Freshness** ([DEC-0060](../decisions/DEC-0060-session-sync-global-async.md)):
  synchronous writes to the writer's overlay (read-your-writes for
  sessions); async propagation elsewhere via the change-event stream;
  rebuild output as the correctness definition.
- **Query tiers** ([DEC-0062](../decisions/DEC-0062-tiered-query-api.md)):
  named traversals (trace-to-goal, subtree, impact-neighborhood, cited-by,
  conflict-neighborhood, build-order); bounded generic traversal primitive
  for agent tools ([DEC-0056](../decisions/DEC-0056-context-recipes-in-packs.md));
  read-only openCypher endpoint with depth/time/result guards.
- **Content depth** ([DEC-0063](../decisions/DEC-0063-metadata-only-graph.md)):
  frontmatter metadata only; bodies fetched from the store; text/semantic
  search explicitly deferred to the retrieval layer ([EP-0007](EP-0007-consolidation-memory-layer.md)).
- **Verification** ([DEC-0064](../decisions/DEC-0064-scheduled-rebuild-diff.md)):
  scheduled rebuild-and-diff with alarming and atomic replacement;
  deterministic `rebuild(ref) → index`.
- **Path-usage telemetry**: consumer-tagged traversal statistics (edge
  heat, no participant content) feeding consolidation placement ([EP-0007](EP-0007-consolidation-memory-layer.md)).

**Out:** engine internals until [SP-0002](../spikes/SP-0002-graph-engine-selection.md)
concludes ([DEC-0061](../decisions/DEC-0061-engine-via-spike.md)); what
callers do with results; canonical link data itself ([EP-0001](EP-0001-artifact-store-and-format-engine.md) owns and
validates it); text search ([EP-0007](EP-0007-consolidation-memory-layer.md)'s neighborhood).

## Domain Context

Bounded context: **Graph Index**. Terms: Graph Index, Branch Overlay,
Provenance Chain, typed link vocabulary — per [CONTEXT.md](../../CONTEXT.md)
and [SPEC-artifact-common](../specs/SPEC-artifact-common.md).

## Interfaces & Contracts to Define

- **Graph query API**: the three tiers, language-neutral (OpenAPI), view
  parameter mandatory; engine hidden behind the executor boundary.
- **Rebuild contract**: `rebuild(canonical-ref) → index`, deterministic;
  diff format for verification runs.
- **Overlay lifecycle contract**: create/update/drop tied to item-branch
  events from [EP-0001](EP-0001-artifact-store-and-format-engine.md)'s change stream.
- **Path-usage telemetry schema**: consumed by [EP-0007](EP-0007-consolidation-memory-layer.md).

## Risks & Open Questions

- Engine selection — [SP-0002](../spikes/SP-0002-graph-engine-selection.md)
  (openCypher support, overlay fit, multi-node story, on-prem ops burden).
- Overlay memory/cost at high concurrent-session counts — measure in
  [SP-0002](../spikes/SP-0002-graph-engine-selection.md)'s synthetic-scale runs.
- Guard calibration for the openCypher tier (limits tight enough to
  protect, loose enough to be useful) — story-level tuning.

## Derived Work

- [SP-0002](../spikes/SP-0002-graph-engine-selection.md) — Graph engine
  selection (drafted during this epic's refinement; ratified with the
  epic's approval per the item-branch pattern).
