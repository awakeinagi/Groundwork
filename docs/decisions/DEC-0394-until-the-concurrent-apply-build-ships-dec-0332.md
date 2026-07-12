---
id: DEC-0394
type: decision
title: "Until the concurrent-apply build ships, DEC-0332 remains the operative interim write rule"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-12
source-span: "SES-0076 @ T24, T29"
overview: >-
  DEC-0391 supersedes DEC-0332 as ratified policy, but its
  guarantees exist only once the lock build lands. In the interim,
  exactly one write-task librarian runs at a time, backgroundable
  per DEC-0393; this decision expires when the DEC-0391
  implementation is verified. Decided at SES-0076.
links:
  derives-from: [SES-0076]
  relates-to: [DEC-0391, DEC-0393, DEC-0416]
---
# DEC-0394: Until the concurrent-apply build ships, DEC-0332 remains the operative interim write rule

## Context

DEC-0391 supersedes DEC-0332 as ratified policy, but its guarantees exist only once the lock build lands.

## Decision

In the interim, exactly one write-task librarian runs at a time (backgroundable per the background-by-default decision). This decision expires when the DEC-0391 implementation is verified.

## Rationale

Not separately recorded at distillation; the rationale is carried by the Context and Decision above and by the source session's transcript at the recorded source span (skeleton restored at SES-0077).

## Alternatives Considered

No alternatives were separately recorded at distillation (skeleton restored at SES-0077).

## Implications

No separate implications were recorded at distillation; the operative consequences are stated in the Decision (skeleton restored at SES-0077).
