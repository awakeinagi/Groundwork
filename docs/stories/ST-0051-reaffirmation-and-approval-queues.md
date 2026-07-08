---
id: ST-0051
type: story
title: Impact-ranked re-affirmation and approval queues
status: deferred
release: "2"
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0006]
  satisfies: [BG-0001]
  depends-on: [ST-0046]
cites: [DEC-0038, DEC-0041, DEC-0073, DEC-0100, DEC-0133, DEC-0147]
---

# ST-0051: Impact-Ranked Re-affirmation and Approval Queues

> Deferred to release `2` at creation (per
> [DEC-0073](../decisions/DEC-0073-v1-ui-surfaces.md), the v1 surface
> subset; the deferral citation per
> [DEC-0100](../decisions/DEC-0100-scope-moves-cite-decisions.md)/[DEC-0133](../decisions/DEC-0133-out-of-scope-differentiated-rule.md)). No
> trigger subscription — revival is release-2 planning.

## Summary

A queue view listing every artifact awaiting re-affirmation or approval,
ordered by impact rank (per
[DEC-0041](../decisions/DEC-0041-impact-ranked-reaffirmation-queue.md)),
so an approver clears the items that unblock the most downstream work
first instead of hunting through the artifact tree.

## Acceptance Criteria

Indicative until revival re-refines this story (deferred stories cannot
pass a gate):

1. Lists `stale` and `gated` artifacts in impact rank order (per
   [DEC-0041](../decisions/DEC-0041-impact-ranked-reaffirmation-queue.md)),
   with each entry linking to [ST-0046](ST-0046-goal-gate-surface.md)-style
   review surfaces generalized to that artifact's type. A `stale` entry
   clearing (re-affirmed back to `approved`) drops off the queue
   immediately (per [DEC-0038](../decisions/DEC-0038-subtree-staleness-reaffirmation.md)).
2. Re-affirmation entries show the upstream diff and impact report
   inline, not just a link out.
3. The queue is a derived, read-only view computed from artifact status
   and the impact graph — it persists no queue-membership state of its
   own, matching the backend queue architecture
   (per [DEC-0147](../decisions/DEC-0147-derived-queue-views.md)).

## Component Impact

None — deferred.

## Out of Scope

Generalizing the gate surface to non-goal artifact types (a prerequisite
this story depends on, tracked as a note on
[ST-0046](ST-0046-goal-gate-surface.md)).

## Notes for Implementers

Depends on [ST-0046](ST-0046-goal-gate-surface.md)'s gate-surface pattern
having already generalized past Business Goals by the time this is
revived.
