---
id: DEC-0401
type: decision
title: "Batch apply gains truthful failure accounting; rollback stays deferred"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0077 @ T8-T9"
overview: >-
  During SES-0077's own T4/T5 write, a timed-out batch left three of
  four operations applied with no accounting (IDEA-0034). The apply
  loop now emits a flushed per-op result line as each operation
  lands, plus a terminal applied-N-of-M summary; an apply-time
  failure stops and prints a manifest of applied, failed, and not-
  attempted operations. An interrupted process leaves the flushed
  lines as a truthful partial record, and a missing summary line
  documents an unfinished batch. Transactional rollback stays out of
  scope pending the DEC-0391 and DEC-0394 concurrency machinery.
  Decided at SES-0077, paired with the whole-batch pre-validation
  decision.
links:
  derives-from: [SES-0077]
  relates-to: [DEC-0391, DEC-0394, IDEA-0034, DEC-0400, DEC-0412]
---
# DEC-0401: Batch apply gains truthful failure accounting; rollback stays deferred

## Context

During SES-0077's own T4/T5 write, a timed-out batch left three of four operations applied with no accounting of what had landed (the process exited 143).

## Decision

The apply loop now emits a flushed per-op result line as each operation lands, plus a terminal applied-N-of-M summary. An apply-time failure stops the batch and prints a manifest of applied, failed, and not-attempted operations. An interrupted process leaves the flushed lines as a truthful partial record, and a missing summary line documents an unfinished batch.

## Rationale

Not separately recorded at distillation; the rationale is carried by the Context and Decision above and by the source session's transcript at the recorded source span (skeleton restored at SES-0077).

## Alternatives Considered

No alternatives were separately recorded at distillation (skeleton restored at SES-0077).

## Implications

Transactional rollback is explicitly out of scope for this decision, pending the DEC-0391 concurrency machinery.
