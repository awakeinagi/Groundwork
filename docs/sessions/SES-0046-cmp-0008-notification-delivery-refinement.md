---
id: SES-0046
type: session
title: "CMP-0008 Notification Delivery refinement"
status: closed
owner: eng-lead
created: 2026-07-08
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
[CMP-0008](../components/CMP-0008-notification-delivery.md) from a
draft stub to a contract-complete component doc, fed by approved story
[ST-0024](../stories/ST-0024-notifier-connector-email-adapter.md) and
its cited decisions.

## Pre-session state

[CMP-0008](../components/CMP-0008-notification-delivery.md) was a stub
with `Pending` sections. Its feeding story
([ST-0024](../stories/ST-0024-notifier-connector-email-adapter.md))
was approved, covering the notifier connector contract, the v1 email
adapter, per-user channel preference resolution, delivery feedback, and
adapter credential handling. The related notification center story
([ST-0048](../stories/ST-0048-notification-center.md), under
[EP-0006](../epics/EP-0006-refinement-web-ui.md)) was also approved,
establishing that the center owns preference storage, routing, the
preferences panel, and read/unread state — with notifier connector
implementations explicitly out of scope.

## Transcript

### T1 — Facilitator

Recapped settled decisions
([DEC-0075](../decisions/DEC-0075-notification-center-connectors.md),
[DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md),
[DEC-0149](../decisions/DEC-0149-notifier-story-under-ep-0005.md),
[DEC-0152](../decisions/DEC-0152-secrets-encrypted-in-app-database.md),
[DEC-0156](../decisions/DEC-0156-future-connector-families-deferred.md),
[ST-0048](../stories/ST-0048-notification-center.md)'s boundary).
Presented four structural boundary questions, each with a recommended
answer:

1. **Protocol graduation**: keep in
   [CMP-0008](../components/CMP-0008-notification-delivery.md)
   (recommended) or graduate to a standalone protocol-type CMP. Reasoning: one future direct
   consumer (notification center,
   [EP-0006](../epics/EP-0006-refinement-web-ui.md), no CMP yet);
   [CMP-0004](../components/CMP-0004-governance-gate-engine.md) goes
   through the center, not directly.
2. **Delivery shape**: resolved channel address (recommended) or
   person-id delivery. Reasoning: matches code-host connector pattern;
   [ST-0048](../stories/ST-0048-notification-center.md) owns
   preferences.
3. **Digest/batch composition**: center composes (recommended) or
   connector batches internally. Reasoning: routing and timing are the
   center's.
4. **Conformance**: yes, formal expectations with a test-double adapter
   (recommended), following
   [DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md)'s
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
   [DEC-0167](../decisions/DEC-0167-connector-typed-error-idempotency-convention.md)'s
   convention. Safe for durable job retries
   ([DEC-0204](../decisions/DEC-0204-v1-default-adapters-deferred-alternates.md)).
3. **Channel address shape**: opaque string, adapter interprets
   (recommended) or typed per-channel union. Reasoning: new channel
   types add an adapter, never a protocol type change.

### T4 — Stakeholder

Accepted all three recommendations without amendment.

### T5 — Facilitator

Decision confirmation. Proposed two decisions:

- [DEC-0240](../decisions/DEC-0240-notifier-protocol-stays-in-cmp-0008.md):
  graduation review — protocol stays in
  [CMP-0008](../components/CMP-0008-notification-delivery.md); one
  future consumer doesn't trigger
  [DEC-0136](../decisions/DEC-0136-graduation-review-required.md).
- [DEC-0241](../decisions/DEC-0241-notifier-delivery-boundary.md):
  delivery boundary — resolved-address, pre-rendered, center-resolved.

Proposed three-element decomposition: NotifierConnector (protocol),
NotifierCapabilityManifest (value), EmailNotifier (service).
Dependencies: [CMP-0015](../components/CMP-0015-secret-store.md).

### T6 — Stakeholder

Confirmed both decisions and the element decomposition.

## Decisions Produced

- [DEC-0240](../decisions/DEC-0240-notifier-protocol-stays-in-cmp-0008.md) —
  NotifierConnector protocol stays in
  [CMP-0008](../components/CMP-0008-notification-delivery.md)
- [DEC-0241](../decisions/DEC-0241-notifier-delivery-boundary.md) —
  delivery boundary: resolved-address, pre-rendered, center-resolved
