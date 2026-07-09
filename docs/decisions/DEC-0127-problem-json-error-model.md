---
id: DEC-0127
type: decision
title: The storage API error model is RFC 9457 problem+json with typed problem URIs
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
overview: >-
  Every non-2xx response across the storage API surface is application/
  problem+json per RFC 9457, with a stable machine-readable type URI
  per failure class (at minimum: tier1-validation-failed, id-conflict,
  not-found, branch-diverged, append-only-violation, mechanical-op-rejected,
  port-unavailable). Tier-1 field-level errors ride in errors[] extension
  member. The problem-type vocabulary is part of the published contract;
  adding a type is a contract change.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0022 @ T3-T4"
links:
  derives-from: [SES-0022]
  relates-to: [DEC-0018, DEC-0034]
---

# DEC-0127: RFC 9457 problem+json Error Model

## Context

Every API item across CMP-0001's
services needs one error shape; the OpenAPI contract is the deliverable
of record (DEC-0018)
and tier-1 failures must carry field-level errors
(DEC-0034).

## Decision

Every non-2xx response across the storage API surface is an
`application/problem+json` body per **RFC 9457**, with a stable,
machine-readable `type` URI per failure class (at minimum:
`tier1-validation-failed`, `id-conflict`, `not-found`,
`branch-diverged`, `append-only-violation`, `mechanical-op-rejected`,
`port-unavailable`). Tier-1 field-level errors ride in an `errors[]`
extension member (field, rule, message). The problem-type vocabulary is
part of the published contract; adding a type is a contract change.

## Rationale

RFC 9457 standardizes what a bespoke envelope would re-document; generic
client tooling understands it; the conformance suite can assert on
`type` alone.

## Alternatives Considered

- **Custom `{code, message, details[]}` envelope** — marginally simpler
  to read, reinvents the standard, opaque to generic tooling.
