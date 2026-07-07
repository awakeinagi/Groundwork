---
id: DEC-0089
type: decision
title: API-item request/response schemas must resolve — inline or to declared elements
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0013 @ T1-T3"
links:
  derives-from: [SES-0013]
---

# DEC-0089: API Schema-Resolution Rule

## Context

The sponsor asked whether service elements should be obligated to define
data contracts for their inputs and outputs. A mandatory D-kind on
services would misfire: services are stateless and own no data, and the
A-kind already mandates request/response schemas per operation. The real
failure mode is an API item that *names* a payload type nobody defines.

## Decision

Gate rule for all API contract items (any element type): every request
and response schema is either defined inline (language-neutral form) or
resolves to a declared value or event element in the same doc or a
depends-on component's contract. Dangling type references are
gate-blockers.

## Rationale

Closes the sponsor's coverage concern at the precise point of failure
without empty-or-duplicated Data Contract sections on stateless
services — and nudges shared payloads into first-class value/event
elements with their own citable data-contract items.

## Alternatives Considered

- **Mandatory D-kind on services**: explicit slot for I/O schemas, but
  duplicates what A-items already mandate and contradicts "stateless —
  owns no data"; payload schemas belong to value/event elements.

## Implications

Rule recorded in [SPEC-design-elements](../specs/SPEC-design-elements.md);
enforced by the tier-2 suite ([ST-0007](../stories/ST-0007-tier2-check-suite.md)) as part of element validation.
