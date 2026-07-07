---
id: DEC-0083
type: decision
title: Element types carry gate-checkable contract obligations
status: superseded
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0012 @ T4-T5"
links:
  derives-from: [SES-0012]
---

# DEC-0083: Typed Contract Obligations

## Context

If element types were only descriptive labels, "contract-complete" would
stay judged at whole-doc level and a typed element with a missing
contract kind could slip through the gate.

## Decision

Each element type mandates which contract kinds its elements must
define, checkable at the gate:

- **entity** ⇒ identity/lifecycle invariants + data contract
- **value** ⇒ data contract (schema, equality/immutability invariants)
- **service** ⇒ API contract + behavior contract
- **event** ⇒ schema + emission/ordering/delivery semantics
- **protocol** ⇒ API contract implementations must satisfy + conformance
  expectations

## Rationale

Obligations make the taxonomy load-bearing rather than decorative: the
type of an element *is* a claim about which contracts it owes, so
completeness per element becomes mechanically checkable
(strengthening [DEC-0011](DEC-0011-contract-complete-component-docs.md)).

## Alternatives Considered

- **Descriptive labels only**: lighter to author, nothing new to check,
  but per-element completeness gaps stay invisible until implementation.

## Implications

Obligation table lives in
[SPEC-design-elements](../specs/SPEC-design-elements.md); ST-0007
enforces presence of each element's mandated contract kinds at the gate.
