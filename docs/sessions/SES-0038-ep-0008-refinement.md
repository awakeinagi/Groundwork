---
id: SES-0038
type: session
title: Backend Application Platform epic refinement
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-08
participant: awakeinagi@gmail.com
participant-role: stakeholder
facilitator: Claude Sonnet 5 (claude-sonnet-5) via Claude Code CLI
transcript-fidelity: reconstructed
links:
  relates-to: [SES-0035]
---

# SES-0038: Backend Application Platform Epic Refinement

## Purpose

Grill the epic identified as missing in
[SES-0035](SES-0035-goal-template-redesign.md)'s retrospective, using
the process built since then: `epic-slicing-seams.md`'s Protocol Seam
for boundary-setting, [BG-0001](../goals/BG-0001-groundwork.md)'s System
Context for already-settled ground, and the deliverable-coverage/
cross-epic-coupling checks before gating.

## Transcript

**T1 — Facilitator.** Recapped settled context (standalone application,
single-process/single-writer v1 posture per
[DEC-0001](../decisions/DEC-0001-standalone-application.md) and
[BG-0001](../goals/BG-0001-groundwork.md)'s System Context; SSE as
default transport per
[DEC-0187](../decisions/DEC-0187-sse-default-pluggable-websocket.md);
the four existing Ports per
[DEC-0121](../decisions/DEC-0121-infrastructure-ports.md)). Classified
the epic under the Protocol Seam (Core Platform Engine & API Foundation,
distinct from [EP-0006](../epics/EP-0006-refinement-web-ui.md)'s
channel). Proposed the Composition Root split — this epic wires Port
contracts to Adapters at startup; the engine epics keep owning the
contracts. Proposed impact edges (`impacted-by` on
[EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md)..[EP-0005](../epics/EP-0005-connectors-and-identity.md),
[EP-0007](../epics/EP-0007-consolidation-memory-layer.md); reciprocal
`impacts`/`impacted-by` with
[EP-0006](../epics/EP-0006-refinement-web-ui.md)) and a Round 1
structured question set: composition scope, API framework, async
execution model, build-order dependency.

**T2 — Stakeholder.** Confirmed the Composition Root split and FastAPI.
Amended the async-model recommendation: build support for both an
in-process and an external execution path, with dedicated Queue and
KV-store Ports so each is swappable — not a single either/or choice.
Confirmed build-order dependency scoped to
[EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md) only.

**T3 — Facilitator.** Flagged that adding two Ports narrows/extends
[DEC-0121](../decisions/DEC-0121-infrastructure-ports.md) ("four
infrastructure ports") without superseding it — the exact
[DEC-0157](../decisions/DEC-0157-relates-to-sweep-at-distillation.md)
relates-to-sweep case — and asked a second round: KV-store's purpose,
the Queue Port's v1 default adapter (durable vs. ephemeral), the
KV-store Port's v1 default adapter (reuse app-database vs. dedicated
library), and when Queue/KV-store graduate to external adapters.

**T4 — Stakeholder.** KV-store: ephemeral coordination state as the
baseline, general-purpose caching also supported, a deferred spike
tracking further future uses. Queue: build stories for both the durable
and ephemeral adapters, durable as default. KV-store: build stories for
both adapter options. Graduation: reuse `TRG-0001`/`TRG-0002`.

**T5 — Stakeholder (interjection).** Add a spike for using AWS SQS.

**T6 — Facilitator.** Opened
[SP-0009](../spikes/SP-0009-aws-sqs-queue-adapter-evaluation.md) (AWS
SQS, named specifically per the request, mirroring
[SP-0002](../spikes/SP-0002-postgres-pgvector-graduation.md)'s
one-spike-per-adapter-question pattern), deferred/backlog, subscribed to
`TRG-0001`/`TRG-0002`. Read back the round so far and flagged two
things before finalizing: which KV-store adapter is the unstated
default, and a tension against this project's established one-default-
adapter-per-Port pattern (every existing Port ships one v1 default and
defers alternates behind a trigger — Postgres+pgvector via
[SP-0002](../spikes/SP-0002-postgres-pgvector-graduation.md), Bitbucket
Data Center via
[SP-0004](../spikes/SP-0004-bbdc-required-check-surface.md), external
secrets via
[SP-0005](../spikes/SP-0005-external-secret-store-adapter.md)) — asked
whether Queue/KV-store's secondary adapters should follow that same
deferred pattern instead of being built in v1 alongside the default.

**T7 — Stakeholder.** Confirmed app-database-Port reuse as the KV-store
default, and confirmed deferring the secondary adapters behind a
trigger, matching the established pattern.

**T8 — Facilitator.** Finalized the shape: durable DB-backed Queue
adapter and app-database-reuse KV-store adapter as v1 defaults; the
ephemeral in-memory Queue adapter and the dedicated embedded KV library
adapter deferred/backlog (not trigger-subscribed — revived manually on a
concrete need, since they aren't a scale-graduation question); opened
[SP-0010](../spikes/SP-0010-external-kv-store-adapter-evaluation.md)
(external KV-store adapter evaluation, mirroring `SP-0009`) and
[SP-0011](../spikes/SP-0011-kv-store-use-case-discovery.md) (KV-store
use-case discovery, not trigger-subscribed). Drafted
[EP-0008](../epics/EP-0008-backend-application-platform.md), updated
[CONTEXT.md](../../CONTEXT.md)'s Port entry to six Ports plus a new
Composition Root term, added reciprocal impact-edge bookkeeping to
[EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md)..[EP-0007](../epics/EP-0007-consolidation-memory-layer.md),
and updated `docs/TRIGGERS.md`'s `TRG-0001`/`TRG-0002` subscriber lists.

**T9 — Facilitator.** Ran the deliverable-coverage pass (all
[BG-0001](../goals/BG-0001-groundwork.md) deliverables now map to an
epic), the cross-epic coupling check (one new mutual pair,
[EP-0006](../epics/EP-0006-refinement-web-ui.md)↔[EP-0008](../epics/EP-0008-backend-application-platform.md),
confirmed intentional per `DEC-0187`), the consistency sweep/terms
against
[DEC-0121](../decisions/DEC-0121-infrastructure-ports.md)'s citers (37
reviewed, no contradictions — three additional genuine cross-links
found and added:
[DEC-0135](../decisions/DEC-0135-graduate-app-database-port.md)'s
CMP-graduation pattern,
[DEC-0200](../decisions/DEC-0200-no-fixed-story-count.md)'s no-fixed-
count principle,
[DEC-0109](../decisions/DEC-0109-trigger-subscriptions.md)'s
subscriber-citation mechanics), and the decision-recall audit. The audit
found two genuine gaps:
[DEC-0102](../decisions/DEC-0102-v1-embedded-stack.md) and
[DEC-0124](../decisions/DEC-0124-v1-adapter-set.md) — the Composition
Root bullet named the *mechanism* for wiring adapters but never named
*which* v1 adapters it wires for the four pre-existing ports — plus an
independent contract gap: Queue/KV-store Port contracts didn't
explicitly require a conformance test suite, breaking the pattern every
other Port follows
([DEC-0122](../decisions/DEC-0122-config-selected-adapters.md)). All
three addressed directly in
[EP-0008](../epics/EP-0008-backend-application-platform.md)'s Scope and
Interfaces & Contracts to Define.

## Decisions Produced

[DEC-0201](../decisions/DEC-0201-composition-root-split.md),
[DEC-0202](../decisions/DEC-0202-fastapi-selected.md),
[DEC-0203](../decisions/DEC-0203-queue-kv-ports-added.md),
[DEC-0204](../decisions/DEC-0204-v1-default-adapters-deferred-alternates.md),
[DEC-0205](../decisions/DEC-0205-graduation-trigger-reuse-and-spikes.md)

## Conflicts Raised

None.
