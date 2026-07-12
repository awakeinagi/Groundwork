---
id: SES-0042
type: session
title: Background Job Execution Runtime contract refinement
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Refined CMP-0013 (Background Job Execution Runtime) toward
  contract-completeness, consuming the approved CMP-0012 (Queue Port).
  Settled handler registration API owned by this CMP (not centralized
  in Composition Root), auto-nack on uncaught exceptions, per-job
  execution timeout with auto-nack on expiry, and single global
  concurrency cap. Decision-recall audit found no missing decisions;
  nearest near-misses already carried transitively through depends-on
  relationship to CMP-0012. No graduation indicated. Produced
  DEC-0222-DEC-0225.
participant: awakeinagi@gmail.com
participant-role: stakeholder
facilitator: Claude Sonnet 5 (claude-sonnet-5) via Claude Code CLI
transcript-fidelity: reconstructed
links:
  relates-to: [EP-0008, ST-0061, CMP-0013, DEC-0222, DEC-0223, DEC-0224, DEC-0225]
---

# SES-0042: Background Job Execution Runtime Contract Refinement

## Purpose

Refine the stubbed
CMP-0013
(Background Job Execution Runtime) toward contract-completeness,
consuming the now-approved
CMP-0012 (Queue Port). This
session resolves the design points ST-0061
left open at story grain: the job-handler registration surface, how
uncaught handler exceptions are treated, whether the runtime enforces a
per-job execution timeout, and the shape of the bounded-concurrency
limit.

## Transcript

**T1 — Facilitator.** Asked a Round 1 question set, each with a
recommended answer:
1. Handler registration — a `register(job-type, handler)` API this CMP
   owns, called by each producer at its own startup, vs. the
   Composition Root centrally registering every handler. Recommended:
   this CMP owns `register()`; each producer (e.g. the KV-store
   Adapter registering its sweep) calls it directly, keeping
   registration co-located with the job's owner rather than
   centralized in the Composition Root — closing the "forward-declared"
   open point flagged in
   CMP-0014's Notes.
2. Uncaught handler exceptions — auto-nack (retry per the Queue Port's
   bound, eventually dead-letter) vs. propagate/crash. Recommended:
   auto-nack, so one broken job never takes down the runtime.
3. Per-job execution timeout — a configurable per-job-type timeout with
   auto-nack on expiry, vs. no runtime-enforced timeout. Recommended:
   enforce one, as the minimal safeguard against a hung handler
   starving the bounded concurrency pool
   (ST-0061
   AC6).
4. Concurrency scope — a single global cap vs. per-job-type caps.
   Recommended: single global cap, simplest for v1 with only one
   concrete job type.

**T2 — Stakeholder.** Confirmed all four recommendations as given.

**T3 — Facilitator.** Decision-recall audit on the drafted
CMP-0013:
nothing missing. Closest near-misses were `DEC-0217` (Queue Port's Job
envelope schema) and `DEC-0152` (secrets encrypted in the app
database) — both already properly carried transitively through the
`depends-on` relationship to
CMP-0012 rather than needing
independent citation here, the same pattern
CMP-0001 already
uses for its own dependencies. Everything else in the candidate set
(vector-store graduation spikes, BBDC connector decisions, workflow
telemetry, an unrelated "Approver/Arbiter queue" UI concept sharing
only the word "queue") was noise from generic term overlap.

**T4 — Facilitator.** Graduation review: checked `JobRuntime` via the
graph tool's `elements` command. Consumed only within `CMP-0013`
today; no graduation indicated.

### Post-Close Enrichment

- 2026-07-08 — Cross-reference enrichment (per DEC-0248, DEC-0250):
  this session refined CMP-0013, a component of the Backend
  Application Platform epic EP-0008.

## Decisions Produced

DEC-0222,
DEC-0223,
DEC-0224,
DEC-0225

## Conflicts Raised

None.
