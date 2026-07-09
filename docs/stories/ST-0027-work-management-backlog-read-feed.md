---
id: ST-0027
type: story
title: Work-management backlog read feed for agent context
status: deferred
release: "2"
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0005]
  satisfies: [BG-0001]
  depends-on: [ST-0025]
  impacted-by: [ST-0025]
cites: [DEC-0016, DEC-0100, DEC-0148, DEC-0155]
---

# ST-0027: Work-Management Backlog Read Feed

> Deferred to release `2` at creation (per
> DEC-0148,
> the deferral citation per
> DEC-0100).
> No trigger subscription — revival is release-2 planning.

## Summary

The agent's second context feed: read-only access to the
work-management backlog so refinement can detect overlap and conflict
against items that never went through Groundwork.

## Acceptance Criteria

Indicative until revival re-refines this story (deferred stories cannot
pass a gate):

1. The work-management contract's backlog read operations expose issue
   summaries, status, and links sufficient for overlap/conflict
   detection against in-flight items
   (per DEC-0016,
   DEC-0155).
2. Read access is read-only and scoped; no backlog write operation is
   expressible through the feed
   (per DEC-0016).

## Component Impact

None yet — lands in the work-management connector component stubbed at
revival (see ST-0025).

## Out of Scope

What the agent does with the feed — overlap detection lives with the
session agent (EP-0002);
projection sync (ST-0025,
deferred).
