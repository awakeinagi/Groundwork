---
id: SES-0039
type: session
title: Backend Application Platform story derivation
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Sliced EP-0008 into eight stories covering Composition Root, Inbound
  API (REST and SSE), Queue Port and runtime, KV-store Port, and async
  runtime execution. Resolved config format (YAML deployment file),
  API split (REST/artifact vs. SSE session), Queue/KV layering (sibling
  adapters on co-located engine), and operational specifics (Queue
  outbox pattern with retries, KV TTL mechanism, RFC 9457 error envelope,
  SSE reconnect/resume). Decision-recall audit addressed seven genuine
  gaps and one layering ambiguity across stories. No mutual coupling
  found. Produced ST-0057-ST-0064 and DEC-0206-DEC-0213.
participant: awakeinagi@gmail.com
participant-role: stakeholder
facilitator: Claude Sonnet 5 (claude-sonnet-5) via Claude Code CLI
transcript-fidelity: reconstructed
links:
  relates-to: [EP-0008, DEC-0206, DEC-0207, DEC-0208, DEC-0209, DEC-0210, DEC-0211, DEC-0212, DEC-0213]
---

# SES-0039: Backend Application Platform Story Derivation

## Purpose

Slice the approved EP-0008
(Backend Application Platform) into implementable stories per
[story-slicing-seams.md](../../CONTEXT.md), resolving the one explicitly
open point from the epic (Composition Root config schema format) plus
the operational specifics needed for testable Acceptance Criteria.

## Transcript

**T1 — Facilitator.** Recapped the epic's settled scope (Composition
Root, Inbound API, Queue Port, KV-store Port, async runtime) and its one
flagged open question (config schema format). Proposed applying the
Operations/Data-seam precedent this project already used at
ST-0010/ST-0008
(port contract+adapter separate from the consumer that rides it) to the
new Queue Port, and the Data Seam's channel variant to the Inbound API
(REST vs. SSE). Asked a Round 1 question set: config schema format, API
story split, Queue Port/runtime split, and Composition Root's
story-level build-order dependency on the two new ports.

**T2 — Stakeholder.** Confirmed all four recommendations: a structured
YAML deployment-config file (env vars reserved for secrets/overrides);
splitting the Inbound API into a REST/artifact+gate story and a separate
SSE session-streaming story; splitting the Queue Port contract+adapter
from the async runtime that consumes it; and Composition Root
depends-on both new Port stories in addition to
ST-0010.

**T3 — Facilitator.** With the story boundaries settled, asked a Round 2
question set covering the operational specifics each story's Acceptance
Criteria needs to be concrete and testable: Queue Port retry/dead-letter
semantics, KV-store TTL/expiry mechanism, the Inbound API's
error-response contract (flagging that
DEC-0127 already
establishes RFC 9457 problem+json for the storage API surface, so the
question was whether the Inbound API reuses it), and whether the SSE
story defines reconnect/resume now or defers it to Component Doc stage.

**T4 — Stakeholder.** Confirmed all four recommendations: the Queue
Port's durable adapter mirrors CMP-0003's
outbox pattern (bounded retries, stale-lease safety, dead-letter after
max attempts); KV-store uses lazy-on-read expiry plus a best-effort
periodic sweep (itself a job on the new async runtime); the Inbound API
reuses DEC-0127's
RFC 9457 problem+json model rather than inventing a new envelope; and
the SSE story defines reconnect-with-backoff/resume-from-last-event-id
now, as a testable Acceptance Criterion.

**T5 — Facilitator.** Distilled eight decisions
(DEC-0206–DEC-0213)
and drafted the eight stories
(ST-0057–ST-0064),
ST-0063 and
ST-0064
entering directly as `deferred`/`backlog` per
DEC-0204's
implication that the alternate adapters be captured as linked deferred
stories. Added reciprocal impact-edge bookkeeping to the existing
stories these new ones influence
(ST-0010,
ST-0022,
ST-0032,
ST-0043,
ST-0044,
ST-0045,
ST-0046,
ST-0047,
ST-0048) and to
EP-0008's Derived
Work section.

**T6 — Facilitator.** Ran the cross-story coupling check
(`groundwork_epic_coupling.py check --type story`) over the eight new
siblings: no mutual pairs found, one-way fan-out from
ST-0057 (Composition Root, the
aggregator) reported as informational only, consistent with the
project's own foundational-epic precedent. Ran the consistency
sweep/terms check over
DEC-0206–DEC-0213:
no contradictions found against
DEC-0121/DEC-0122/DEC-0127's
existing citers, aside from one unlinked but intentional
`stale-lease`-vocabulary co-occurrence between
DEC-0210
and CMP-0003 (deliberate
pattern reuse, already body-linked; no action needed).

Ran the decision-recall audit per story (two Sonnet 5 judges, four
stories each). Genuine gaps surfaced and were fixed in-story: `ST-0057`
was missing DEC-0152
(its env-var AC read as endorsing a second, competing secrets path);
`ST-0058` was missing
DEC-0163
(its metrics-exposure AC didn't preserve the fixed-endpoint contract)
and DEC-0042;
`ST-0059` was missing both
DEC-0182
(reconnect's interaction with the session inactivity clock was
unaddressed) and its own already-referenced
DEC-0212
from its `cites` list; `ST-0060` was missing
DEC-0129 and
DEC-0135, plus a
contract gap (job payloads must never embed secrets — closed by adding
an Acceptance Criterion citing
DEC-0152);
`ST-0061` was missing
DEC-0131 and
had no stated concurrency model (closed by adding a bounded-concurrency
Acceptance Criterion); `ST-0062` had a genuine layering ambiguity
(whether its adapter routes through `AppDatabasePort`'s `bookkeeping`
family or is a sibling adapter on the same co-located DuckDB engine —
resolved as the latter, matching the vector-store/app-database
precedent, per
DEC-0129);
`ST-0064` needed clarification that a library's native TTL/eviction may
substitute for the default adapter's sweep mechanism provided the
observable contract holds. `ST-0063` returned "nothing to add" — its
nearest near-miss (`DEC-0210`) was judged already structurally implied
by its conformance-suite requirement.

## Decisions Produced

DEC-0206,
DEC-0207,
DEC-0208,
DEC-0209,
DEC-0210,
DEC-0211,
DEC-0212,
DEC-0213

## Conflicts Raised

None.
