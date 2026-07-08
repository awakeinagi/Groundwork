---
id: ST-0055
type: story
title: Change proposal triage views
status: deferred
release: "2"
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0006]
  satisfies: [BG-0001]
  depends-on: [ST-0045]
cites: [DEC-0047, DEC-0073, DEC-0100, DEC-0133]
---

# ST-0055: Change Proposal Triage Views

> Deferred to release `2` at creation (per
> [DEC-0073](../decisions/DEC-0073-v1-ui-surfaces.md), the v1 surface
> subset; the deferral citation per
> [DEC-0100](../decisions/DEC-0100-scope-moves-cite-decisions.md)/[DEC-0133](../decisions/DEC-0133-out-of-scope-differentiated-rule.md)). No
> trigger subscription — revival is release-2 planning.

## Summary

A UI over Change Proposal triage (per
[DEC-0047](../decisions/DEC-0047-change-proposal-artifact.md)) — list,
filter, and act on `CP-` artifacts (the backend triage operations exist
in [ST-0039](ST-0039-change-proposal-triage.md); this story is their UI).

## Acceptance Criteria

Indicative until revival re-refines this story (deferred stories cannot
pass a gate):

1. Lists CPs filterable by triage status and target artifact.
2. Triage actions call the typed `create-change-proposal`/`set-cp-triage`
   operations ([ST-0039](ST-0039-change-proposal-triage.md)) rather than
   a parallel write path.

## Component Impact

None — deferred.

## Out of Scope

CP triage semantics and storage
([EP-0002](../epics/EP-0002-refinement-session-agent.md)).

## Notes for Implementers

This is a thin UI over [ST-0039](ST-0039-change-proposal-triage.md)'s
already-approved backend contract — no new triage logic belongs here.
