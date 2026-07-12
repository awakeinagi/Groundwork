---
id: DEC-0392
type: decision
title: "Order-dependent writes are one batch or explicitly sequenced; batch keys do not cross tasks"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-12
source-span: "SES-0076 @ T22, T27-T28"
overview: >-
  Writes that reference each other's newly created artifacts belong
  in one batch, or the facilitator sequences the dependent task
  after the prerequisite completes, since batch keys resolve only
  within their own batch. Session transcripts are inherently serial:
  at most one in-flight turn-appending task per session artifact,
  dispatched in conversation order; appends to different sessions
  parallelize freely. Decided at SES-0076 alongside DEC-0391, the
  shared/exclusive lock design.
links:
  derives-from: [SES-0076]
  relates-to: [DEC-0391]
---
# DEC-0392: Order-dependent writes are one batch or explicitly sequenced; batch keys do not cross tasks

## Context

With write applies serializing at the apply moment per DEC-0391, the ordering of dependent writes across tasks remained to be defined (skeleton restored at SES-0077).

## Decision

Writes that reference each other's newly created artifacts belong in one batch, or the facilitator sequences the dependent task after the prerequisite completes — batch keys resolve only within their own batch.

Session transcripts are inherently serial: at most one in-flight turn-appending task per session artifact, dispatched in conversation order; appends to different sessions parallelize freely.

## Rationale

Not separately recorded at distillation; the rationale is carried by the Context and Decision above and by the source session's transcript at the recorded source span (skeleton restored at SES-0077).

## Alternatives Considered

No alternatives were separately recorded at distillation (skeleton restored at SES-0077).

## Implications

No separate implications were recorded at distillation; the operative consequences are stated in the Decision (skeleton restored at SES-0077).
