---
id: DEC-0470
type: decision
title: "Customization posture: opinionated-and-fixed, re-openable on demand"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0089 @ T10, T11, T12, T13"
overview: >-
  Third-party adoption raises whether the paradigm is configurable
  (custom artifact types, gate criteria, checker rules) or fixed;
  the posture shapes Engine Core, Adoption, and the future
  Export/Packaging topic (DEC-0467). SES-0089 settles this: the
  paradigm is opinionated-and-fixed — every adopter gets the same
  artifact types, gates, and checker rules — with Engine Core and
  Adoption drawing explicit Out-of-Scope lines against extension
  points, schema registries, and plugin contracts, rather than
  building configurability speculatively ahead of proven demand. The
  posture is explicitly re-openable: an actual adopter or user
  request for flexibility triggers a new session that may supersede
  this decision with targeted extension points at the demanded
  spots, never a speculative general plugin architecture.
links:
  derives-from: [SES-0089]
  relates-to: [DEC-0462, DEC-0467]
---

# DEC-0470: Customization posture — opinionated-and-fixed, re-openable on demand

## Context

Third-party adoption raises whether the paradigm is configurable —
custom artifact types, gate criteria, checker rules — or fixed; the
posture shapes Engine Core, Adoption, and the future Export topic.

## Decision

The paradigm is opinionated-and-fixed: every adopter gets the same
artifact types, gates, and checker rules. Engine Core and Adoption draw
explicit Out-of-Scope lines against extension points, schema
registries, and plugin contracts. The posture is explicitly
re-openable: an actual adopter or user request for flexibility triggers
a new session that may supersede this decision with targeted extension
points at the demanded spots — never a speculative general plugin
architecture.

## Rationale

The methodology is the product; speculative configurability widens
Engine Core ahead of any proven demand.

## Alternatives Considered

Configurable from the start (speculative infrastructure); leaving the
posture genuinely undecided (soft Out-of-Scope lines in two charters).

## Implications

Firm Out-of-Scope entries in the Engine Core and Adoption charters; the
revisit trigger is recorded here.
