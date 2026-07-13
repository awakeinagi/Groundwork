---
id: DEC-0511
type: decision
title: "Governance rules are artifact-type-agnostic; no direct edges to EP-0011 or EP-0013"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-13
source-span: "SES-0094 @ T6–T7, T10–T11"
overview: >-
  DEC-0442's no-ungoverned-capability obligation touches every
  epic's artifact types, raising whether EP-0014 needs direct impact
  edges to EP-0011 or EP-0013. This decision states governance rules
  are artifact-type-agnostic — they run over whatever artifact types
  the Engine's model defines (DEC-0469, DEC-0484) — and draws no
  direct edge to either epic, since an edge to every governed epic
  would create a star topology that belongs to EP-0010's hub-and-
  spoke shape, not governance's; SES-0089's coupling check found no
  such coupling.
links:
  derives-from: [SES-0094]
  relates-to: [DEC-0469, DEC-0484, DEC-0263, DEC-0486]
---

# DEC-0511: Governance rules are artifact-type-agnostic; no direct edges to EP-0011 or EP-0013

## Context

DEC-0442's no-ungoverned-capability obligation touches every epic's artifact types — agent and skill definitions, bootstrap seeding, and future types — raising the question of whether EP-0014 needs direct impact edges to EP-0011 or EP-0013.

## Decision

Governance rules are artifact-type-agnostic: they run over whatever artifact types the Engine's model defines (DEC-0469, DEC-0484), and EP-0014 draws no direct impact edge to EP-0011 or EP-0013. Gating agent or skill definitions is general rules applied to those artifact types, and EP-0013's bootstrap seeding of governance/ files (DEC-0263) is story-level consumption mediated by EP-0010's compliance definition (DEC-0486).

## Rationale

An edge to every epic whose artifact types get governed would create a star topology, and that hub-and-spoke shape is the Engine's topology (EP-0010's), not governance's; SES-0089's coupling check found no such coupling.

## Alternatives Considered

An EP-0014→EP-0011 edge was rejected as starting the star topology. An EP-0014→EP-0013 edge was rejected as overstating a file-seeding dependency already mediated by EP-0010's compliance definition.

## Implications

EP-0014's body carries the agnosticism note, and future artifact types are governed without changes to EP-0014.
