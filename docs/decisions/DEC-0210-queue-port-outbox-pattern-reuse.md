---
id: DEC-0210
type: decision
title: Queue Port's durable adapter reuses the App Database Port's outbox retry/dead-letter/stale-lease pattern
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Queue Port's failure contract mirrors App Database Port's outbox
  pattern: bounded retry count per job, stale-lease typed errors on
  ack/nack of expired or unknown lease (job remains/becomes claimable
  again), dead-letter parking after configurable maximum failed
  deliveries visible through bookkeeping surface. Delivery
  at-least-once; consumers idempotent by contract. Reuses already-proven
  pattern from same codebase for same underlying problem. Constrains
  ST-0060's Acceptance Criteria and Component Doc. Status accepted.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0039 @ T3-T4"
links:
  derives-from: [SES-0039]
  relates-to: [DEC-0139, DEC-0203, DEC-0204]
  supersedes: []
---

# DEC-0210: Queue Port Reuses the Outbox Failure Pattern

## Context

The Queue Port's v1 durable adapter
(DEC-0204)
needs a concrete retry/failure contract before
ST-0060's Acceptance Criteria can be
testable. CMP-0003's
outbox already defines exactly this shape for at-least-once delivery
(DEC-0139).

## Decision

The Queue Port's failure contract mirrors the App Database Port's
outbox pattern: bounded retry count per job, `stale-lease` typed errors
on ack/nack of an expired or unknown lease (job remains/becomes
claimable again), and dead-letter parking after a configurable maximum
of failed deliveries — visible through the port's own bookkeeping
surface, never silently dropped. Delivery is at-least-once; consumers
(the background runtime, ST-0061)
are idempotent by contract.

## Rationale

This is an already-proven pattern in this exact codebase
(DEC-0139),
for the same underlying problem (durable, at-least-once, retryable work
items behind a Port). Reusing it means one failure-semantics vocabulary
project-wide instead of two competing ones for superficially different
Ports.

## Alternatives Considered

- **Unlimited retries with exponential backoff, no dead-letter**:
  rejected — a job that can never terminally fail has no path to
  operator visibility when something is systematically broken; contradicts
  this project's "never silently dropped" stance already established for
  the outbox.

## Implications

ST-0060's Acceptance Criteria and,
later, its Component Doc's failure contract cite
DEC-0139
directly rather than re-deriving the same guarantees independently.
