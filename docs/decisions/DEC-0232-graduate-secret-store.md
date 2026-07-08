---
id: DEC-0232
type: decision
title: The encrypted secret store graduates to a standalone service-type CMP
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0045 @ T1-T2"
links:
  derives-from: [SES-0045]
  relates-to: [DEC-0152, DEC-0136, DEC-0080]
---

# DEC-0232: Graduate the Secret Store

## Context

[DEC-0152](DEC-0152-secrets-encrypted-in-app-database.md) placed
connector secrets envelope-encrypted in the app database, drafted as a
[CMP-0007](../components/CMP-0007-identity-and-access.md) concern. But the approved
[CMP-0009](../components/CMP-0009-github-connector.md) `IG-5` already
stores its per-installation webhook signing secrets in that facility,
and [CMP-0010](../components/CMP-0010-composition-root.md) hands it
the master key — a contract-certain second consumer, which is exactly
the graduation rule's trigger
([DEC-0136](DEC-0136-graduation-review-required.md),
[DEC-0080](DEC-0080-hybrid-component-granularity.md)).

## Decision

The encrypted secret store graduates to its own standalone
service-type component,
[CMP-0015](../components/CMP-0015-secret-store.md), consumed by
[CMP-0007](../components/CMP-0007-identity-and-access.md) (OAuth
tokens, the attribution signing key) and
[CMP-0009](../components/CMP-0009-github-connector.md) (webhook
signing secrets).

## Rationale

Two consumers before the element was even drafted; the same pattern
that graduated the App Database Port
([DEC-0135](DEC-0135-graduate-app-database-port.md)). Its conformance
(envelope encryption, master-key handling) versions independently of
identity concerns.

## Alternatives Considered

- **Keep in [CMP-0007](../components/CMP-0007-identity-and-access.md)**: fewer docs, but contradicts the graduation
  rule and buries a cross-component facility inside identity.
- **Defer to gate-time review**: risks restructuring the doc and the
  [CMP-0009](../components/CMP-0009-github-connector.md)/[CMP-0010](../components/CMP-0010-composition-root.md) cross-references late.

## Implications

[CMP-0009](../components/CMP-0009-github-connector.md) and
[CMP-0010](../components/CMP-0010-composition-root.md) get pointer
amendments (the facility is [CMP-0015](../components/CMP-0015-secret-store.md), not [CMP-0007](../components/CMP-0007-identity-and-access.md)) and
re-affirmation; [ST-0021](../stories/ST-0021-delegated-reviews-and-attribution.md)
and [ST-0022](../stories/ST-0022-identity-auth-and-person-resolution.md)
add [CMP-0015](../components/CMP-0015-secret-store.md) to Component Impact.
