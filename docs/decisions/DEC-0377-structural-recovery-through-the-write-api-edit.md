---
id: DEC-0377
type: decision
title: "Structural recovery through the write API: edit-section --occurrence N and a delete-section operation"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0072 @ T11-T12"
overview: >-
  The edit-section op gains --occurrence N (target the Nth heading matching
  the substring) and a new delete-section op removes a heading and
  its span, refusing to delete the last occurrence of a type-
  required section; both honor existing immutability preconditions
  (closed sessions, accepted decisions; --amend for approved/stale).
  Ends the "corrupted structure requires git or a freehand edit"
  hole; validated by repairing SP-0015, SP-0013, EP-0009,
  IDEA-0015/0016/0025 in this session.
links:
  relates-to: [DEC-0312, DEC-0376]
  derives-from: [SES-0072]
---

# DEC-0377: Structural recovery through the write API: edit-section --occurrence N and a delete-section operation

## Context

Once a phantom heading existed, no write-API path could reach past it; every prior repair needed operator-sanctioned out-of-band edits or git reverts.

## Decision

Add --occurrence N to edit-section and a delete-section op with required-template protection (duplicates deletable, the type's required section set is not).

## Rationale

Repairs belong inside the sanctioned write path; the ops are small and validated against real corpus damage in this session.

## Alternatives Considered

No recovery op (YAGNI — leaves the out-of-band hole open); occurrence flag only (deleting an empty orphan via replacement is clumsier).

## Implications

Librarian memory guidance telling agents to stop and refuse-and-report is superseded by "repair via delete-section/--occurrence".
