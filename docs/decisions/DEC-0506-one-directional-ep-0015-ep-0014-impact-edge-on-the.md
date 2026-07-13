---
id: DEC-0506
type: decision
title: "One-directional EP-0015→EP-0014 impact edge on the governance-configuration seam"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-13
source-span: "SES-0094 @ T4–T5, T10–T11"
overview: >-
  EP-0014 and EP-0015 both describe the governance-configuration
  seam in their Interfaces sections but neither carried the DEC-0249
  frontmatter impact edge — rated the SES-0094 consultation's one
  blocking-severity gap. This decision records a one-directional
  impact edge, EP-0015 impacts EP-0014, since EP-0015's schema
  shapes what EP-0014's rule families can evaluate while the reverse
  influence is consumer-driven input, not an architectural edge.
  SES-0089's coupling check found no mutual coupling, so a one-way
  edge is the accurate record without reopening DEC-0443's settled
  placement.
links:
  derives-from: [SES-0094]
  relates-to: [DEC-0443, DEC-0249, DEC-0469]
---

# DEC-0506: One-directional EP-0015→EP-0014 impact edge on the governance-configuration seam

## Context

EP-0014 and EP-0015 both describe the governance-configuration seam in their Interfaces sections — EP-0015 owns the schema per DEC-0443, EP-0014 owns evaluation per DEC-0469 — but neither carried a frontmatter impact edge: the seam prose was added during SES-0089's decision-recall audit after that session's coupling check ran, and the DEC-0249 edge bookkeeping was skipped. The record-grounded architect rated this the draft's one blocking-severity gap.

## Decision

The governance-configuration seam carries a one-directional impact edge — EP-0015 impacts EP-0014 — recorded as impacts: [EP-0014] on EP-0015 and impacted-by: [EP-0015] on EP-0014, with DEC-0249 prose in EP-0015's body explaining that the schema it defines shapes what the governance rule families can evaluate.

## Rationale

EP-0015's schema definition shapes EP-0014's rule evaluation; the reverse influence — evaluation requirements informing the schema — is consumer-driven input, not an architectural impact edge. SES-0089's coupling check found no mutual coupling in this sibling set, and mutual edges are the method's signal for a false seam; a one-way edge records the real dependency without reopening DEC-0443's settled placement.

## Alternatives Considered

Mutual edges were rejected as contradicting the coupling-check finding and reopening a settled seam. Prose-only with no edge was rejected because graph queries would stay blind to the dependency and DEC-0249 reciprocity would remain incomplete.

## Implications

Refinement-order, impact-walk, and coupling queries now see EP-0015→EP-0014. EP-0014's gate does not newly block on EP-0015 — the edge is design-shaping, not blocking. EP-0015's overview refreshes with the edge.
