---
id: ST-0011
type: story
title: Schema evolution and migration machinery for artifact SPEC changes
status: deferred
release: backlog
owner: eng-lead
created: 2026-07-07
links:
  derives-from: [EP-0001]
  satisfies: [BG-0001]
  relates-to: [ST-0001]
cites: [DEC-0100, DEC-0133]
---

# ST-0011: Schema Evolution and Migration Machinery

> Deferred to `backlog` at creation (per
> DEC-0133,
> the scope-move citation per
> DEC-0100).
> Revival is subscribed to trigger `TRG-0005` in
> [TRIGGERS.md](../TRIGGERS.md) — the first post-launch change to an
> artifact SPEC. Captured out of
> ST-0001's Out of Scope section,
> where it previously lived as prose only.

## Summary

When a SPEC document changes after launch, existing artifacts validate
against the old schema while new writes need the new one. This story
covers the machinery that first event requires: schema versioning,
corpus migration (or grandfathering rules), and the tier-1/tier-2
behavior during a transition window.

## Acceptance Criteria

Sketch, to be refined at revival in current context (per
DEC-0097 revival-at-draft
rule):

1. Schema assets carry a version; the validation library knows which
   version governs a given artifact (per DEC-0034).
2. A SPEC change ships with either a mechanical corpus migration or an
   explicit grandfathering rule — never silent breakage of existing
   artifacts (per DEC-0034, DEC-0018).

## Component Impact

CMP-0001 — would
extend the SchemaValidator element and schema assets.

## Out of Scope

The SPEC-change governance process itself (a gated edit, already
covered); any speculative versioning built before the first real spec
change (per DEC-0133 — this story exists precisely so
that build waits for its trigger).

## Notes for Implementers

None yet — POC-free capture; design starts at revival.
