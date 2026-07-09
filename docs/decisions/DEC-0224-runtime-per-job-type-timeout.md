---
id: DEC-0224
type: decision
title: Background Job Execution Runtime enforces a configurable per-job-type execution timeout
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
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
