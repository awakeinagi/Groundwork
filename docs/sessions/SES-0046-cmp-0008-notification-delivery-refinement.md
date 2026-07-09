---
id: SES-0046
type: session
title: "CMP-0008 Notification Delivery refinement"
status: closed
owner: eng-lead
created: 2026-07-08
overview: >-
  Refined CMP-0008 from draft stub to contract-complete, fed by approved
  ST-0024 and ST-0048. Settled protocol stays in CMP-0008 (one future
  consumer insufficient to trigger graduation). Resolved delivery
  boundary as resolved channel address (not person-id), pre-rendered
  content, center-composed routing and batching. Settled idempotency on
  notification_id per DEC-0167, opaque channel-address strings per
  adapter interpretation. Decomposed into three elements:
  NotifierConnector protocol, NotifierCapabilityManifest value,
  EmailNotifier service (v1 default). Produced DEC-0240-DEC-0241.
transcript-type: reconstructed
participants:
  facilitator: claude
  stakeholder: awakeinagi@gmail.com
artifact-focus: CMP-0008
links:
  derives-from: [EP-0005]
  relates-to: [ST-0024, ST-0048, CMP-0005, CMP-0007]
---

# SES-0046: Notification Delivery Refinement

Grilling session to refine
CMP-0008 from a
draft stub to a contract-complete component doc, fed by approved story
ST-0024 and
its cited decisions.

## Pre-session state

CMP-0008 was a stub
with `Pending` sections. Its feeding story
(ST-0024)
was approved, covering the notifier connector contract, the v1 email
adapter, per-user channel preference resolution, delivery feedback, and
adapter credential handling. The related notification center story
(ST-0048, under
EP-0006) was also approved,
establishing that the center owns preference storage, routing, the
preferences panel, and read/unread state — with notifier connector
implementations explicitly out of scope.

## Transcript

### T1 — Facilitator

Recapped settled decisions
(DEC-0075,
DEC-0045,
DEC-0149,
DEC-0152,
DEC-0156,
ST-0048's boundary).
Presented four structural boundary questions, each with a recommended
answer:

1. **Protocol graduation**: keep in
   CMP-0008
   (recommended) or graduate to a standalone protocol-type CMP. Reasoning: one future direct
   consumer (notification center,
   EP-0006, no CMP yet);
   CMP-0004 goes
   through the center, not directly.
2. **Delivery shape**: resolved channel address (recommended) or
   person-id delivery. Reasoning: matches code-host connector pattern;
   ST-0048 owns
   preferences.
3. **Digest/batch composition**: center composes (recommended) or
   connector batches internally. Reasoning: routing and timing are the
   center's.
4. **Conformance**: yes, formal expectations with a test-double adapter
   (recommended), following
   DEC-0045's
   pattern.

### T2 — Stakeholder

Accepted all four recommendations without amendment.

### T3 — Facilitator

Three contract-level detail questions for the `deliver()` operation:

1. **Payload rendering**: pre-rendered content — subject + body_text +
   optional body_html (recommended) or structured data that adapters
   render. Reasoning: adapters transport, never render; no second
   template surface.
2. **Idempotency**: idempotent on `notification_id` (recommended),
   following
   DEC-0167's
   convention. Safe for durable job retries
   (DEC-0204).
3. **Channel address shape**: opaque string, adapter interprets
   (recommended) or typed per-channel union. Reasoning: new channel
   types add an adapter, never a protocol type change.

### T4 — Stakeholder

Accepted all three recommendations without amendment.

### T5 — Facilitator

Decision confirmation. Proposed two decisions:

- DEC-0240:
  graduation review — protocol stays in
  CMP-0008; one
  future consumer doesn't trigger
  DEC-0136.
- DEC-0241:
  delivery boundary — resolved-address, pre-rendered, center-resolved.

Proposed three-element decomposition: NotifierConnector (protocol),
NotifierCapabilityManifest (value), EmailNotifier (service).
Dependencies: CMP-0015.

### T6 — Stakeholder

Confirmed both decisions and the element decomposition.

### Post-Close Enrichment

- 2026-07-08 — Cross-reference enrichment (per DEC-0248, DEC-0250):
  the connector boundary settled here follows the pattern of CMP-0005
  (Code-Host Connector Protocol) — resolved inputs, capability
  manifest, conformance suite — and the rejected person-id delivery
  alternative would have pulled person-id resolution, owned by
  CMP-0007 (Identity & Access), into the connector.

## Decisions Produced

- DEC-0240 —
  NotifierConnector protocol stays in
  CMP-0008
- DEC-0241 —
  delivery boundary: resolved-address, pre-rendered, center-resolved
