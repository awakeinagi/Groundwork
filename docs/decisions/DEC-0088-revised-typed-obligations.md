---
id: DEC-0088
type: decision
title: Revised typed obligations — entity full behavior contract, conditional API
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
overview: >-
  The typed obligations table is revised, superseding DEC-0083: entity now
  requires full behavior contract + data contract with conditional API
  (required exactly when exposed at the component boundary); value requires
  data; service requires API + behavior; event requires schema + semantics;
  protocol requires API + conformance. Obligations remain gate-checkable
  per element. Entity behavior deserves full expression without forcing
  language signatures on internals.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0013 @ T1-T3"
links:
  derives-from: [SES-0013]
  supersedes: [DEC-0083]
---

# DEC-0088: Revised Typed Contract Obligations

## Context

The sponsor challenged DEC-0083:
shouldn't entities define behavior and API contracts (the public API of
the object)? The original table compressed entity behavior into
"identity & lifecycle invariants" and said nothing about when an entity
owes an API contract.

## Decision

The typed obligations table is revised (superseding DEC-0083):

- **entity** ⇒ **behavior contract** (identity semantics, lifecycle
  states, allowed transitions, domain-operation semantics) + **data
  contract**, mandatory; **API contract conditional** — required exactly
  when the entity's operations are exposed at the component boundary
  (e.g., a graduated standalone entity CMP).
- **value** ⇒ data contract (schema, equality/immutability invariants).
- **service** ⇒ API contract + behavior contract.
- **event** ⇒ schema + emission/ordering/delivery semantics.
- **protocol** ⇒ API contract implementations must satisfy + conformance
  expectations.

Obligations remain gate-checkable per element.

## Rationale

Entity behavior deserved full breadth: what an entity's public methods
must guarantee is contract material, expressible as behavior items
without prescribing method signatures. Mandating A-kind on every entity
would force language-shaped signatures onto internal classes,
constraining implementation shape against
DEC-0011's
observable-guarantee standard and
DEC-0018; the
conditional captures the one case where an entity genuinely fronts the
boundary.

## Alternatives Considered

- **B+A+D all mandatory for entities**: uniform, but most entity
  A-sections would restate their B-items in implementation-shaped form.
- **Keep DEC-0083 as-is**: leaves entity operation semantics without a
  clearly mandated home.

## Implications

Obligations table updated in
[SPEC-design-elements](../specs/SPEC-design-elements.md); ST-0007 and
CMP-0001 cites move from DEC-0083 to this decision. Service I/O coverage
is handled separately by
DEC-0089.
