---
id: ST-0052
type: story
title: Participant profile viewer/editor with consent management
status: deferred
release: "2"
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0006]
  satisfies: [BG-0001]
  depends-on: [ST-0042]
cites: [DEC-0071, DEC-0073, DEC-0100, DEC-0133]
---

# ST-0052: Participant Profile Viewer/Editor with Consent Management

> Deferred to release `2` at creation (per
> DEC-0073, the v1 surface
> subset; the deferral citation per
> DEC-0100/DEC-0133). No
> trigger subscription — revival is release-2 planning.

## Summary

A profile surface where a participant views/edits their opt-in profile
and manages consent (per
DEC-0071) — what
the consolidation/memory layer is allowed to remember about them.

## Acceptance Criteria

Indicative until revival re-refines this story (deferred stories cannot
pass a gate):

1. Renders the participant's current profile content and lets them edit
   or delete individual entries.
2. Consent toggles are explicit per data category, off by default,
   consistent with DEC-0071's
   opt-in model.

## Component Impact

None — deferred.

## Out of Scope

Profile storage and the consolidation layer that populates it
(EP-0007).

## Notes for Implementers

Depends on ST-0042 for
the authenticated participant context this surface edits against.
