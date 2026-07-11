---
id: SP-0014
type: spike
title: "Structural design-rule precision over the projected corpus"
status: draft
owner: awakeinagi@gmail.com
created: 2026-07-10
timebox: 1 session
overview: >-
  Question: do compiled structural rules fire true findings on the
  real design? Method: hand-compile ~12 structural rules -- about
  half from the system-architecture-bp corpus (dependency cycles,
  stability direction, orphaned interfaces), half from Groundwork's
  own rule-type DECs (citation integrity, mandatory-contract-kind
  completeness, Uses-typing/build-order) -- as ActiveGraph
  behaviors; fire against SP-0013's projected graph; stakeholder
  disposes every finding. Depends on SP-0013 (impacted-by).
  Evaluation criteria: complete findings catalog with stakeholder
  dispositions (real / noise / change-worthy); per-rule precision
  notes; explicitly no kill bar (DEC-0355). Data-source assumptions:
  SP-0013's projection is faithful (its coverage stats gate what
  rules can see); compiled rules derive only from already-curated
  sources (ratified corpus content and accepted DECs). Deliverable:
  findings catalog.
links:
  impacts: [SP-0016, SP-0017]
  impacted-by: [SP-0013]
  derives-from: [EP-0009]
  relates-to: [SP-0013]
cites: [DEC-0354, DEC-0351, DEC-0355, DEC-0335, DEC-0337, DEC-0345, DEC-0336]
---

> Guardrails (DEC-0351): this spike's outputs are strictly throwaway and are never deployed as part of the artifact interaction surface. Adoption of anything it surfaces happens only through the ordinary path -- a DEC-0337 option survey followed by DEC-0335 design intake -- never by this spike's findings alone.

## Question

Do compiled structural rules fire true findings on the real design? Concretely: when ~12 structural rules -- drawn half from the system-architecture-bp corpus (dependency cycles, stability direction, orphaned interfaces) and half from Groundwork's own rule-type decisions (citation integrity, mandatory-contract-kind completeness, Uses-typing/build-order) -- are compiled as ActiveGraph behaviors and fired against SP-0013's projected graph, are the findings real, noise, or change-worthy?

## Why It Blocks

Blocks nothing today. It is the load-bearing evidence for the executable-design-knowledge idea (DEC-0354): if compiled structural rules mostly fire noise, the approach's central premise weakens regardless of ActiveGraph as substrate. SP-0016 (SP-D) and SP-0017 (SP-E) both depend on this spike's rulebase.

## Method

Hand-compile approximately 12 structural rules as ActiveGraph behaviors: roughly six from the system-architecture-bp corpus (dependency cycles, stability direction, orphaned interfaces) and roughly six from Groundwork's own rule-type DECs (citation integrity, mandatory-contract-kind completeness, Uses-typing/build-order). Fire the rulebase against the graph SP-0013 projected. The stakeholder disposes every finding the rules produce -- real, noise, or change-worthy.

This spike builds a throwaway executable; per DEC-0345, its validation approach (the checks described above) is part of the reviewed spike design, not chosen ad hoc after the fact, and is sized minimally per DEC-0336's throwaway-scope yardstick.

## Evaluation Criteria
Descriptive measures, no pass/fail threshold (DEC-0355): a complete findings catalog with the stakeholder's disposition on each (real / noise / change-worthy); per-rule precision notes (which rules fired only real findings, which fired noise, and why).

## Data-Source Assumptions
SP-0013's projection is faithful enough to build on -- its coverage stats (fraction of contract items and typed edges projected cleanly) gate what these rules can see and thus what findings are even possible. Compiled rules derive only from already-curated sources: ratified system-architecture-bp content and accepted Groundwork DECs, never invented heuristics.

## Findings

Pending — recorded at spike completion.


## Resulting Decisions

Pending — a completed spike produces at least one decision, even "assumption confirmed, no change."
