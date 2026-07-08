---
id: ST-0053
type: story
title: Consolidation review and flagging
status: deferred
release: "2"
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0006]
  satisfies: [BG-0001]
  depends-on: [ST-0045]
cites: [DEC-0072, DEC-0073, DEC-0100, DEC-0133]
---

# ST-0053: Consolidation Review and Flagging

> Deferred to release `2` at creation (per
> [DEC-0073](../decisions/DEC-0073-v1-ui-surfaces.md), the v1 surface
> subset; the deferral citation per
> [DEC-0100](../decisions/DEC-0100-scope-moves-cite-decisions.md)/[DEC-0133](../decisions/DEC-0133-out-of-scope-differentiated-rule.md)). No
> trigger subscription — revival is release-2 planning.

## Summary

A review surface for consolidation-layer output (per
[DEC-0072](../decisions/DEC-0072-consolidation-review-flagging.md)) — a
human can inspect what got consolidated and flag a bad consolidation for
correction.

## Acceptance Criteria

Indicative until revival re-refines this story (deferred stories cannot
pass a gate):

1. Lists consolidation records with their source artifacts/spans and the
   consolidated output side by side.
2. A flag action records a dispute against a consolidation record (per
   [DEC-0072](../decisions/DEC-0072-consolidation-review-flagging.md)),
   visible to whoever owns consolidation quality.

## Component Impact

None — deferred.

## Out of Scope

The consolidation process itself
([EP-0007](../epics/EP-0007-consolidation-memory-layer.md)).

## Notes for Implementers

Reuses [ST-0045](ST-0045-goal-artifact-view.md)'s provenance rendering
for the source-artifact side of the comparison.
