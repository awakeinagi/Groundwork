---
id: DEC-0361
type: decision
title: "CMP-0001 depends on CMP-0005"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-10
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-10
source-span: "SES-0066 @ T16-T17"
overview: >-
  BranchOrchestrator.B-3 mandates all host interaction via the code-
  host connector contract; that contract exists as CMP-0005, so the
  element edge (BranchOrchestrator -> CodeHostConnector, interface)
  and the depends-on entry were added and CMP-0001's stale future-
  standalone-protocol-type-CMP Dependencies note corrected.
links:
  derives-from: [SES-0066]
  relates-to: [DEC-0080, DEC-0132]
---

## Context

During the Uses: backfill's extraction and classification pass (SES-0066 T16), the facilitator found that `BranchOrchestrator.B-3` mandates all host interaction via the code-host connector contract, which exists as CMP-0005 — but CMP-0001's Dependencies note still described the connector as a "future" standalone protocol-type CMP not yet a standing dependency, a stale characterization from before CMP-0005 was approved.

## Decision

CMP-0001 depends on CMP-0005. The element edge (`BranchOrchestrator` → `CodeHostConnector`, `(interface)`) and a `CMP-0005` entry in CMP-0001's `depends-on` frontmatter link were added, and CMP-0001's stale "future standalone protocol-type CMP" Dependencies-section note was corrected to describe CMP-0005 as a standing dependency.

## Rationale

CMP-0005 is approved and its protocol is exactly what `BranchOrchestrator.B-3` requires; recording it as a forward declaration once the dependency is real is misleading to any reader of CMP-0001's Dependencies section and understates the structural edge the corpus's own contract prose already asserts.

## Alternatives Considered

Leaving CMP-0001's Dependencies note as a forward declaration was rejected: CMP-0005 has been approved since EP-0005 refinement completed, and DEC-0132 itself anticipated this edge becoming a standing dependency once the connector CMP existed.

## Implications

CMP-0001's depends-on now includes CMP-0005; DEC-0309's both-directions projection check (enforced by rule 20, decision 2) requires this. No other artifacts needed correction as a consequence.
