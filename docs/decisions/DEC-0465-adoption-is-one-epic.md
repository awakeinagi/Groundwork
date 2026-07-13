---
id: DEC-0465
type: decision
title: "Adoption is one epic"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0089 @ T4, T13"
overview: >-
  DEC-0443 listed Adoption-greenfield and Adoption-brownfield as
  separate anticipated roster topics. SES-0089's derivation
  collapses them into a single Adoption epic, since both share the
  same adopter persona, the same success target (a compliant,
  checker-passing corpus per BG-0002 outcome 3), and the same
  dependency on the Engine's compliance definition — splitting them
  buys no parallelism because both paths block on that shared
  definition. The greenfield-versus-brownfield distinction is
  carried at story level within the one epic instead of as two
  separate lifecycle-variant epics, which would only add gate
  overhead without unlocking independent work.
links:
  derives-from: [SES-0089]
  relates-to: [DEC-0443, DEC-0462]
---

# DEC-0465: Adoption is one epic

## Context

DEC-0443 listed Adoption-greenfield and Adoption-brownfield as separate
anticipated topics.

## Decision

Adoption is a single epic covering greenfield bootstrap and brownfield
fold-in; the two paths differentiate at story level.

## Rationale

Same adopter persona, same success target (a compliant, checker-passing
corpus per BG-0002 outcome 3), same dependency on the Engine's
compliance definition; splitting buys no parallelism because both
halves block on that definition.

## Alternatives Considered

Two lifecycle-variant epics (gate overhead without autonomy).

## Implications

The epic's stories carry the greenfield/brownfield distinction.
