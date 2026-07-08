---
id: DEC-0214
type: decision
title: Queue Port job-type is an open string namespace, not a closed enum
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0040 @ T1-T2"
links:
  derives-from: [SES-0040]
  relates-to: [DEC-0128, DEC-0203, DEC-0210]
  supersedes: []
---

# DEC-0214: Queue Job-Type Is an Open String Namespace

## Context

[CMP-0012](../components/CMP-0012-queue-port.md) (Queue Port) needed a
job-type shape decided before its `enqueue`/`claim` operations could be
specified. [CMP-0002](../components/CMP-0002-change-event.md)'s
`ChangeEvent.kind` precedent uses a closed enum with gated extension
([DEC-0128](DEC-0128-change-event-closed-schema.md)); the Queue Port
needed its own explicit call rather than inheriting that shape by
default.

## Decision

`job-type` is an open string namespace: any value is a valid job-type
at the port level, and new job types are added by registering a
handler on the background job execution runtime
([ST-0061](../stories/ST-0061-background-job-execution-runtime.md)),
never by a contract change to this port.

## Rationale

`ChangeEvent.kind` is closed because its consumers (Graph Index,
governance sweeps) branch on the enum directly and a silent new value
would break them ([DEC-0128](DEC-0128-change-event-closed-schema.md)).
Jobs have the opposite consumption pattern: the port never interprets
`job-type` itself, only the runtime's registered handler does
([ST-0061](../stories/ST-0061-background-job-execution-runtime.md)'s
Notes for Implementers already anticipates future jobs — notifier
retries, staleness sweeps — registering against a generic dispatch
loop). Gating every future job type through this CMP would add
ceremony with no consumer that needs the closed guarantee.
