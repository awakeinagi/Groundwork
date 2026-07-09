---
id: CMP-0013
type: component
title: Background Job Execution Runtime
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
context: platform
links:
  derives-from: [EP-0008]
  satisfies: [BG-0001]
  depends-on: [CMP-0012]
cites: [DEC-0102, DEC-0121, DEC-0131, DEC-0139, DEC-0203, DEC-0205,
        DEC-0206, DEC-0208, DEC-0210, DEC-0211, DEC-0214, DEC-0222,
        DEC-0223, DEC-0224, DEC-0225]
---

# CMP-0013: Background Job Execution Runtime

## Purpose

The in-process asyncio runtime that consumes the Queue Port
(CMP-0012): claims, executes, and
acks/retries background jobs, with no external broker or separate
worker process in v1
(DEC-0208). The
KV-store Port's periodic expiry sweep
(CMP-0014) is its first concrete job
(ST-0061).

## Ubiquitous Language

Port, Adapter, Job, Lease — per
[CONTEXT.md](../../CONTEXT.md)/CMP-0012. New
term: **Handler** (the registered callable that executes one
`job-type`'s jobs).

## Design Elements

### JobRuntime (service)

Implements: ST-0061

- `JobRuntime.A-1` — `register(job-type, handler, [timeout])`. Attaches
  a handler callable to a `job-type` (open string namespace, per
  DEC-0214);
  any component needing background work calls this directly at its own
  initialization — the runtime maintains no central catalog of job
  owners (per
  DEC-0222).
  `timeout` is optional; unset falls back to the runtime-wide default
  (per
  DEC-0224).
- `JobRuntime.A-2` — `start()` / `stop()`. Process-lifecycle hooks: on
  `start()`, begins claiming against the Queue Port; on `stop()`,
  finishes in-flight jobs (up to a grace period) and stops claiming new
  ones. Wired by the Composition Root
  (CMP-0010, forward-declared per
  DEC-0132
  since that CMP is refined separately).
- `JobRuntime.B-1` — dispatch loop: `claim` → look up the registered
  handler for the claimed job's `job-type` → execute → `ack` on
  success, `nack` on failure — the one generic loop every job rides,
  never a per-job-type scheduling loop (per
  DEC-0210).
- `JobRuntime.B-2` — unregistered `job-type`: a claimed job whose
  `job-type` has no registered handler is `nack`ed without execution —
  never silently dropped, never crashes the runtime (per
  DEC-0223's
  same never-crash discipline).
- `JobRuntime.B-3` — retry/dead-letter: the runtime honors the Queue
  Port's bound entirely by delegation — it holds no independent retry
  counter or policy of its own (per
  DEC-0210).
- `JobRuntime.B-4` — exception handling: an uncaught exception from a
  handler is caught by the dispatch loop and results in `nack`, never a
  runtime crash or a dropped in-flight job elsewhere (per
  DEC-0223).
- `JobRuntime.B-5` — execution timeout: a handler exceeding its
  registered (or default) timeout is cancelled and `nack`ed, via the
  same path as `B-4` (per
  DEC-0224).
- `JobRuntime.B-6` — bounded concurrency: a single deployment-wide
  configured cap bounds jobs executing concurrently across all
  `job-type`s combined — never unbounded fan-out, consistent with the
  v1 single-process/single-writer posture (per
  DEC-0225,
  DEC-0102).
- `JobRuntime.B-7` — crash/restart resumption: on restart, the runtime
  resumes claiming purely from the Queue Port's durable Adapter state —
  it holds no independent record of queued or in-flight work; that
  state is derived and rebuildable, never a second source of truth
  (per
  DEC-0131,
  DEC-0204).

## Component Invariants

- `C-1` — rebuild-sufficiency: the runtime's own view of pending/
  in-flight work is always derived from the Queue Port at process
  start; no cache or counter of it survives independently of that Port
  (per
  DEC-0131).
- `C-2` — concurrency never exceeds the configured cap, including
  across a mix of job-types (per
  DEC-0225).
- `C-3` — no job failure — exception, timeout, or explicit `nack` —
  ever prevents another concurrently executing job from completing (per
  DEC-0223).

## Implementation Guidance

### Constraints

- `IG-1` — v1 is in-process asyncio only: no external broker, message
  queue, or separate worker process (per
  DEC-0208,
  DEC-0102).
- `IG-2` — the concurrency cap and the default execution timeout are
  Composition Root deployment configuration
  (DEC-0206),
  not compiled-in constants (per
  DEC-0225,
  DEC-0224).
- `IG-3` — multi-node or external worker execution is deferred behind
  `TRG-0001`/`TRG-0002` (per
  DEC-0205).

### Notes

- Claim/poll cadence (how often the loop calls `QueuePort.A-2.claim`
  when idle) is an implementation choice, not a contract item — the
  contract only requires that claimed work eventually executes.
- The KV-store Port's expiry-sweep Adapter is expected to call
  `JobRuntime.A-1` at its own startup to register the sweep handler
  (per ST-0061
  AC3); this component's contract does not special-case that job.

## Dependencies

- CMP-0012 — the Queue Port this runtime
  consumes exclusively for all durable state; consumed sections:
  `QueuePort.A-2` (claim/ack/nack), `QueuePort.B-4`/`B-5`/`B-6`
  (stale-lease, dead-letter, and delivery semantics the runtime relies
  on rather than reimplements).

## Acceptance & Test Expectations

1. End-to-end dispatch: a handler registered via `JobRuntime.A-1`
   executes for a job enqueued through
   CMP-0012, and the job is acked on success
   (per ST-0061
   AC1).
2. Crash/restart resumption: killing the process mid-claim and
   restarting resumes work from the Queue Port's persisted state with
   no job lost (per
   DEC-0131).
3. Concurrency conformance: enqueuing more jobs than the configured cap
   never results in more than the cap executing concurrently (per
   DEC-0225).
4. Failure-path conformance: a handler exception, an execution timeout,
   and an unregistered `job-type` each result in `nack` (retry, then
   eventual dead-letter) with the runtime and other in-flight jobs
   unaffected (per
   DEC-0223,
   DEC-0224).
5. The KV-store Port's periodic expiry sweep runs end-to-end as the
   first concrete job on this runtime (per
   ST-0061
   AC3,
   DEC-0211).

## Out of Scope

Boundary statements (per
DEC-0133):

- The Queue Port contract and Adapter themselves —
  CMP-0012, per the port/runtime story split
  (DEC-0208).
- Multi-node/external execution — deferred behind
  `TRG-0001`/`TRG-0002` (per
  DEC-0205).
- Any specific job's business logic beyond the KV-store sweep named
  above — each future job is scoped by the story that needs it, and
  registers via `JobRuntime.A-1` without a change to this contract.
- Central handler-registry ownership — no component (including the
  Composition Root) maintains a catalog of what job-types exist; that
  is emergent from which producers have called `register` (per
  DEC-0222).
