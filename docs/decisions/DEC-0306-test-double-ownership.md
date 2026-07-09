---
id: DEC-0306
type: decision
title: Test doubles are design elements of the component owning the contract they fake
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0056 @ T8-T9"
overview: >-
  A test double (fake, fixture, reference stub) is a design element of
  the component that owns the contract it fakes — e.g. the local-git
  fake connector becomes an element of CMP-0005 beside the conformance
  suite. Promotion from non-normative Notes (DEC-0085) happens through
  normal component amendment when the double is first referenced by a
  (test)-typed Uses: edge (DEC-0299). One fake, many consumers,
  specified where the contract semantics live. Forced by adopting
  three edge types: a (test) edge must target an owned, specified
  node.
links:
  derives-from: [SES-0056]
  relates-to: [DEC-0299, DEC-0085, CMP-0005]
---

# DEC-0306: Test-Double Ownership

## Context

Adopting the `(test)` edge type (DEC-0299) means fixture dependencies
must resolve to owned nodes; today fakes live only in non-normative
Notes (DEC-0085).

## Decision

A test double is a **design element of the component that owns the
contract it fakes**, promoted from Notes via normal component
amendment when first referenced by a `(test)`-typed `Uses:` edge.

## Rationale

The double's fidelity obligations are the contract's semantics; the
conformance suite it must pass lives in the same doc. One fake serves
many consumers without re-specification.

## Alternatives Considered

- **Consumer's integration package owns its fakes** — N consumers
  re-specify the same fake; rejected.
- **Central test-infrastructure component** — splits fakes from the
  contracts they mirror; rejected.

## Implications

Lazy promotion: no bulk retrofit; CMP-0005's local-git fake is the
expected first promotion when Uses: retrofit reaches its consumers.
