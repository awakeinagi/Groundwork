---
id: ST-0054
type: story
title: Synthesis shared-draft commenting feeding change proposals
status: deferred
release: "2"
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0006]
  satisfies: [BG-0001]
  depends-on: [ST-0045]
cites: [DEC-0047, DEC-0055, DEC-0073, DEC-0100, DEC-0133]
---

# ST-0054: Synthesis Shared-Draft Commenting Feeding Change Proposals

> Deferred to release `2` at creation (per
> DEC-0073, the v1 surface
> subset; the deferral citation per
> DEC-0100/DEC-0133). No
> trigger subscription — revival is release-2 planning.

## Summary

A commenting surface on the incremental synthesis shared draft (per
DEC-0055)
letting stakeholders react to in-progress synthesis, with comments
feeding into Change Proposals rather than editing the draft directly.

## Acceptance Criteria

Indicative until revival re-refines this story (deferred stories cannot
pass a gate):

1. Renders the current shared draft with inline commenting, scoped to
   sections (per DEC-0055).
2. A "propose change" action on a comment creates a `CP-` artifact (per
   DEC-0047) citing
   the comment, rather than mutating the draft in place.

## Component Impact

None — deferred.

## Out of Scope

The synthesis process and shared-draft storage itself
(EP-0002).

## Notes for Implementers

Reuses ST-0045's section-scoped
rendering; do not build a second body renderer.
