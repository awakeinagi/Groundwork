---
id: DEC-0240
type: decision
title: NotifierConnector protocol stays in CMP-0008; graduation revisited at EP-0006
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0046 @ T1-T2"
links:
  derives-from: [SES-0046]
  relates-to: [DEC-0136, DEC-0080, DEC-0075]
---

# DEC-0240: NotifierConnector Protocol Stays in the Notification Delivery Component

## Context

The [CMP-0008](../components/CMP-0008-notification-delivery.md) stub
flagged the notifier protocol element for graduation review: the
[DEC-0045](DEC-0045-capability-declaring-connectors.md) connector
pattern already produced a standalone protocol-type CMP for the
code-host connector
([CMP-0005](../components/CMP-0005-code-host-connector-protocol.md)),
and this pattern might repeat for the notifier connector.

## Decision

The NotifierConnector protocol stays inside
[CMP-0008](../components/CMP-0008-notification-delivery.md). The only
direct consumer is the future notification center component (under
[EP-0006](../epics/EP-0006-refinement-web-ui.md), no CMP yet).
[CMP-0004](../components/CMP-0004-governance-gate-engine.md) goes
through the center ("fires a notification through the notification
center"), not directly through the protocol. One future consumer does
not trigger the graduation rule
([DEC-0136](DEC-0136-graduation-review-required.md)).

Revisit when [EP-0006](../epics/EP-0006-refinement-web-ui.md)'s
component boundary crystallizes and a second direct consumer is
identified.

## Rationale

The code-host protocol graduated because two approved CMPs
([CMP-0001](../components/CMP-0001-artifact-store-service.md),
[CMP-0004](../components/CMP-0004-governance-gate-engine.md)) consume
it directly. Here the only direct consumer path (notification center)
is not yet a CMP, and
[CMP-0004](../components/CMP-0004-governance-gate-engine.md)'s
consumption is mediated through that center — an indirect dependency
that the graduation rule does not count.

## Alternatives Considered

- **Graduate now to a standalone protocol-type CMP**: anticipates the
  center as a contract-certain consumer, but creates two CMPs (protocol
  + adapter) for a protocol with one v1 adapter and no direct second
  consumer yet.

## Implications

[CMP-0008](../components/CMP-0008-notification-delivery.md) carries
both the NotifierConnector protocol element and the EmailNotifier
service element. If a second direct consumer emerges at
[EP-0006](../epics/EP-0006-refinement-web-ui.md) refinement, the
protocol graduates via a new decision superseding this one.
