---
id: ST-0061
type: story
title: Background job execution runtime (in-process asyncio)
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0008]
  satisfies: [BG-0001]
  depends-on: [ST-0060]
  impacts: []
  impacted-by: [ST-0060]
cites: [DEC-0102, DEC-0121, DEC-0131, DEC-0203, DEC-0204, DEC-0205, DEC-0208,
        DEC-0210, DEC-0211]
---

# ST-0061: Background Job Execution Runtime (In-Process Asyncio)

## Summary

The consumer that rides the Queue Port
(ST-0060): an in-process asyncio runtime that
claims, executes, and acks/retries background jobs — no external
broker or worker process in v1
(per DEC-0208).

## Acceptance Criteria

1. An in-process asyncio runtime consumes jobs from the Queue Port
   (claim → execute → ack/nack), with no external broker or separate
   worker process required in v1
   (per DEC-0203,
   DEC-0208,
   DEC-0121).
2. The runtime honors
   ST-0060's retry/dead-letter contract:
   failed jobs retry up to the configured bound, then dead-letter
   (per DEC-0210).
3. The KV-store Port's periodic expiry sweep
   (per DEC-0211)
   runs as a named job on this runtime — the first concrete consumer
   proving the runtime end-to-end.
4. A process crash or restart does not lose queued jobs — the runtime
   resumes claiming from the durable adapter's persisted state on
   restart, which is derived state rebuildable from what the durable
   adapter persisted, never itself a second source of truth
   (per DEC-0204,
   DEC-0131).
5. Job execution is observable: a job's current state (queued,
   running, retrying, dead-lettered) is queryable through the Queue
   Port's bookkeeping surface, not only inferable from logs.
6. The runtime executes a bounded number of jobs concurrently (a
   configurable limit, small by default) via asyncio tasks — never
   unbounded fan-out — consistent with the v1 single-process/
   single-writer posture
   (per DEC-0102).

## Component Impact

CMP-0013
— approved.
CMP-0012 — approved; the
job-status observability item (`QueuePort.A-3`, `JobStatus`) this
story's Acceptance Criteria require also implements this story.

## Out of Scope

- The Queue Port contract and adapter itself —
  ST-0060.
- Multi-node/external execution — deferred behind `TRG-0001`/`TRG-0002`
  (per DEC-0205).
- Any specific job's business logic beyond the KV-store sweep named
  above — each future job is scoped by the story that needs it.

## Notes for Implementers

Keep the runtime's job-dispatch loop generic (claim → execute a
registered handler → ack/nack) so future jobs (staleness sweeps,
notifier retries, etc.) register against it rather than each growing
its own scheduling loop.
