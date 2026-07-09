---
id: DEC-0281
type: decision
title: The Idea take-up flow ships in release 1 as an ST-0065 amendment
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
overview: >-
  DEC-0281 constrains the Idea take-up flow to release 1 as an ST-0065
  amendment: the captured-Ideas list gains a take-up action opening an
  intake-opened session with the Idea's verbatim text as the proposal
  (origin: idea), setting the Idea taken-up and its Disposition naming
  the session. This completes DEC-0261's work-queue semantics in the same
  release capturing Ideas.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0052 @ T8-T9"
links:
  derives-from: [SES-0052]
  relates-to: [DEC-0261, DEC-0271]
---

# DEC-0281: Take-up ships in release 1

## Context

DEC-0271 reserved the take-up flow — selecting a captured Idea and
opening an intake session from it — as a hand-off point for
IDEA-0001's session. That session (SES-0052) is now deciding where and
when it lands.

## Decision

Release 1, as an amendment to ST-0065: the captured-Ideas list gains a
**take-up action** that opens an intake-opened session with the Idea's
verbatim text as the proposal (`origin: idea`) and sets the Idea
`taken-up`, its Disposition naming the session. This completes
DEC-0261's work-queue semantics in the same release that captures
Ideas.

## Rationale

Everything take-up needs — the session UX and the intake-opening
contract — is release-1. Deferring to release 2 would ship a work
queue with no dequeue: Ideas captured that cannot be acted on for a
whole release. The change is one list action plus one open-session
call against contracts other stories own — amendment-sized, not
story-sized.

## Alternatives Considered

- **Release 2, joining ST-0055**: the reserved hand-off point sits
  empty a whole release.
- **A new release-1 story**: ceremony for one AC's worth of scope.

## Implications

ST-0065's Out of Scope reservation is fulfilled and replaced by the
new acceptance criterion; DEC-0271's reservation is discharged, not
superseded — it deferred exactly this decision to exactly this
session.
