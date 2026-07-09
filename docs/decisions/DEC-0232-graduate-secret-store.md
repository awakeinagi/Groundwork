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

DEC-0152 placed
connector secrets envelope-encrypted in the app database, drafted as a
CMP-0007 concern. But the approved
CMP-0009 `IG-5` already
stores its per-installation webhook signing secrets in that facility,
and CMP-0010 hands it
the master key — a contract-certain second consumer, which is exactly
the graduation rule's trigger
(DEC-0136,
DEC-0080).

## Decision

The encrypted secret store graduates to its own standalone
service-type component,
CMP-0015, consumed by
CMP-0007 (OAuth
tokens, the attribution signing key) and
CMP-0009 (webhook
signing secrets).

## Rationale

Two consumers before the element was even drafted; the same pattern
that graduated the App Database Port
(DEC-0135). Its conformance
(envelope encryption, master-key handling) versions independently of
identity concerns.

## Alternatives Considered

- **Keep in CMP-0007**: fewer docs, but contradicts the graduation
  rule and buries a cross-component facility inside identity.
- **Defer to gate-time review**: risks restructuring the doc and the
  CMP-0009/CMP-0010 cross-references late.

## Implications

CMP-0009 and
CMP-0010 get pointer
amendments (the facility is CMP-0015, not CMP-0007) and
re-affirmation; ST-0021
and ST-0022
add CMP-0015 to Component Impact.
