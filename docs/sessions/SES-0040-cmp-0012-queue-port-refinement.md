---
id: SES-0040
type: session
title: Queue Port contract refinement
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Refined CMP-0012 (Queue Port) toward contract-completeness from ST-0060
  and outbox-pattern precedent (DEC-0210). Settled job-type as open
  string namespace, dead-letter terminal in v1, single deployment-wide
  retry default, and fixed-envelope job payload (opaque document).
  Resolved layering ambiguity: Queue adapter is sibling on co-located
  engine, not routing through AppDatabasePort. Decision-recall audit
  flagged missing citations and deferral/split decisions; added to
  cites. No graduation indicated. Produced DEC-0214-DEC-0218.
participant: awakeinagi@gmail.com
participant-role: stakeholder
facilitator: Claude Sonnet 5 (claude-sonnet-5) via Claude Code CLI
transcript-fidelity: reconstructed
links:
  relates-to: [EP-0008, ST-0060, CMP-0012]
---

# SES-0040: Queue Port Contract Refinement

## Purpose

Refine the stubbed CMP-0012
(Queue Port) toward contract-completeness. Most of the contract is
already settled by ST-0060's
Acceptance Criteria and the outbox-pattern-reuse precedent
(DEC-0210);
this session resolves the remaining points not pinned down at story
grain: the job-type namespace shape, dead-letter recovery, retry-bound
configuration, and the job payload envelope.

## Transcript

**T1 — Facilitator.** Asked a Round 1 question set, each with a
recommended answer:
1. Job-type namespace — open string namespace (future job types
   register without a contract change) vs. a closed enum mirroring
   ChangeEvent's `kind` (gated extension). Recommended: open string
   namespace, citing ST-0061's
   Notes for Implementers ("future jobs register against it").
2. Dead-letter recovery — terminal in v1 (visible via the status
   surface, no redrive operation) vs. an explicit `requeue(job-id)`
   operation. Recommended: terminal in v1 — no Acceptance Criterion in
   ST-0060 calls for redrive.
3. Retry-bound configuration — a single deployment-wide default vs.
   per-job override at enqueue time. Recommended: single
   deployment-wide default, matching the App Database Port precedent's
   lack of a per-operation override.
4. Job payload shape — a fixed envelope (job-id, job-type, opaque
   payload document, attempt count, timestamps) with the payload
   uninterpreted by the port, vs. per-job-type typed payload schemas
   declared at the port. Recommended: fixed envelope, opaque payload —
   mirrors `AppDatabasePort.A-3`'s bookkeeping `document` treatment.

**T2 — Stakeholder.** Confirmed all four recommendations as given.

**T3 — Facilitator.** While drafting `QueuePort`'s Dependencies section,
surfaced a fifth open point: ST-0060
AC5 describes the v1 durable adapter as "a queue table riding the App
Database Port" — the identical layering ambiguity
SES-0039 already
resolved for the KV-store Port. Asked whether the Queue adapter
literally routes through `AppDatabasePort`'s outbox/bookkeeping
operations, or is a sibling adapter with its own table on the same
co-located DuckDB engine, consuming no `AppDatabasePort` operations.
Recommended the latter, for consistency with the KV-store precedent
just settled in the same thread.

**T4 — Stakeholder.** Confirmed the recommendation.

**T5 — Facilitator.** Decision-recall audit on the drafted
CMP-0012 surfaced two citation
gaps: `DEC-0135` (the port-graduation pattern the header blockquote
already invokes by name but the frontmatter `cites:` list omitted) and
`DEC-0205`/`DEC-0208` (the trigger-deferral and port/runtime-split
decisions backing two Out of Scope bullets that named the boundary but
not the decision). All three added to `cites:` and the relevant
prose. No other candidate in the audit packet (Constraints-section
noise from unrelated
CMP-0004/CMP-0005
decomposition decisions, embedding-adapter decisions, the storage
API's problem+json model)
was genuinely relevant — closest near-miss was `DEC-0152` (secrets
encrypted in the app database): plausible in the abstract, but no
Acceptance Criterion of ST-0060
motivates a secrets discussion beyond the payload-opacity guarantee
already in `Job.D-2`, which does cite it.

**T6 — Facilitator.** Graduation review: checked `QueuePort`, `Job`,
`JobStatus` against the graduation rule (consumed by more than one CMP,
or needing independently versioned conformance) via the graph tool's
`elements` command. None are consumed outside `CMP-0012` today; no
graduation indicated.

### Post-Close Enrichment

- 2026-07-08 — Cross-reference enrichment (per DEC-0248, DEC-0250):
  this session refined CMP-0012, a component of the Backend
  Application Platform epic EP-0008.

## Decisions Produced

DEC-0214,
DEC-0215,
DEC-0216,
DEC-0217,
DEC-0218

## Conflicts Raised

None.
