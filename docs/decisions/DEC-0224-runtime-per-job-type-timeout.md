---
id: DEC-0224
type: decision
title: Background Job Execution Runtime enforces a configurable per-job-type execution timeout
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Each registered handler declares or defaults to a runtime-wide fallback
  maximum execution duration; the runtime cancels handlers exceeding it and
  calls QueuePort.nack as if the handler had raised an exception. A concurrency
  bound eroded by hung jobs isn't a real bound. Timeout-triggered nack reuses
  the existing failure-handling path rather than inventing a second mechanism.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0042 @ T1-T2"
links:
  derives-from: [SES-0042]
  relates-to: [DEC-0223, DEC-0225]
  supersedes: []
---

# DEC-0224: Runtime Enforces a Per-Job-Type Execution Timeout

## Context

ST-0061 AC6
requires the runtime to execute a bounded number of jobs concurrently,
never unbounded fan-out. Without a per-execution timeout, a single
handler that hangs (e.g. a stuck network call) occupies a concurrency
slot indefinitely, degrading the bound to "the pool minus however many
jobs happen to be stuck."

## Decision

Each registered handler declares (or defaults to a runtime-wide
fallback) a maximum execution duration; the runtime cancels a handler
that exceeds it and calls `QueuePort.nack` as if the handler had
raised, per
DEC-0223's exception
path.

## Rationale

A concurrency bound that can be silently eroded by hung jobs isn't
really a bound. Timeout-triggered nack reuses the exact same
failure-handling path exceptions already take
(DEC-0223) rather than
inventing a second one — a timeout is simply another way execution
fails to complete cleanly.

## Alternatives Considered

T1 posed the timeout question as a configurable per-job-type timeout with auto-nack on expiry versus no runtime-enforced timeout at all; the no-timeout alternative was weighed and rejected because it would let a single hung handler erode the bounded-concurrency guarantee ST-0061 AC6 requires, degrading the pool to "however many jobs happen to be stuck." The stakeholder confirmed the enforced-timeout recommendation as given (T2). (skeleton restored at SES-0078)

## Implications

A handler that exceeds its declared (or runtime-wide fallback) maximum execution duration is cancelled by the runtime and treated exactly as if it had raised, routing through the same nack path DEC-0223 established. This preserves the concurrency bound against silent erosion by hung jobs without introducing a second, separate failure-handling mechanism. (skeleton restored at SES-0078)
