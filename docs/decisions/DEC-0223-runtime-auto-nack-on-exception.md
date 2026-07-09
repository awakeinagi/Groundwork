---
id: DEC-0223
type: decision
title: Background Job Execution Runtime auto-nacks a job on an uncaught handler exception
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  The runtime dispatch loop catches any handler exception and calls QueuePort.nack
  on the job's behalf, feeding the Queue Port's retry/dead-letter bound. No
  handler exception crashes the runtime or another in-flight job. This routes
  exceptions through the existing nack path rather than inventing a separate
  failure-handling mechanism, keeping exactly one failure path (retry →
  dead-letter).
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0042 @ T1-T2"
links:
  derives-from: [SES-0042]
  relates-to: [DEC-0210, DEC-0139]
  supersedes: []
---

# DEC-0223: Runtime Auto-Nacks on Uncaught Handler Exception

## Context

ST-0061's
generic "claim → execute a registered handler → ack/nack" dispatch loop
left open what happens when a handler raises an exception the handler
itself didn't catch: propagate (crashing the runtime or that dispatch
task) or treat it as an implicit nack.

## Decision

The dispatch loop catches any exception a handler raises during
execution and calls `QueuePort.nack` on the job's behalf, feeding the
Queue Port's existing retry/dead-letter bound
(DEC-0210). No handler
exception crashes the runtime or another in-flight job.

## Rationale

A background job runtime that can be taken down by one buggy handler
defeats its own purpose — the whole point of bounded concurrency and
per-job isolation
(ST-0061 AC6)
is that jobs don't interfere with each other. Routing exceptions
through the same nack path as an explicit failure keeps exactly one
failure-handling mechanism (retry → dead-letter,
DEC-0139) instead of
two.
