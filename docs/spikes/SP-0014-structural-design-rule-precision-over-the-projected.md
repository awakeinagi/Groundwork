---
id: SP-0014
type: spike
title: "Structural design-rule precision over the projected corpus"
status: in-refinement
owner: awakeinagi@gmail.com
created: 2026-07-10
timebox: 1 session
overview: >-
  Question: do compiled structural rules fire true findings on the
  real design? Method: hand-compile structural rules as ActiveGraph
  behaviors and fire them against SP-0013's projected graph;
  stakeholder disposes every finding. At take-up (SES-0069), the
  stakeholder directed expansion beyond the planned ~12 rules to
  every structural rule the two curated sources worthily ground: the
  executed rulebase is 24 rules -- 14 discovery rules (system-
  architecture-bp structural smells plus Groundwork's rule-type
  DECs, including schema resolution per DEC-0089, test-double
  promotion-candidate detection per DEC-0306, staleness propagation
  per DEC-0096, and bundle closure per DEC-0303), 5 calibration
  rules with recorded expected outputs, 3 rules vacuous against
  current Uses: data, and 2 weak/proxy-grounding probes retained as
  noise-rate tests. Depends on SP-0013 (impacted-by). Evaluation
  criteria: complete findings catalog with stakeholder dispositions
  (real / noise / change-worthy); per-rule precision notes;
  explicitly no kill bar (DEC-0355). Data-source assumptions:
  SP-0013's projection is faithful (its coverage stats gate what
  rules can see); compiled rules derive only from already-curated
  sources (ratified corpus content and accepted DECs). Grounding-
  strength tags record how firmly each rule derives from its source,
  since the best-practice corpus grounds rules via practitioner
  sources rather than named design-principle citations. Deliverable:
  findings catalog.
links:
  impacts: [SP-0016, SP-0017]
  impacted-by: [SP-0013]
  derives-from: [EP-0009]
  relates-to: [SP-0013]
cites: [DEC-0354, DEC-0351, DEC-0355, DEC-0335, DEC-0337, DEC-0345, DEC-0336, DEC-0315, DEC-0309, DEC-0299, DEC-0086, DEC-0358, DEC-0365, DEC-0359, DEC-0360, DEC-0088, DEC-0089, DEC-0092, DEC-0094, DEC-0096, DEC-0303, DEC-0306]
---

> Guardrails (DEC-0351): this spike's outputs are strictly throwaway and are never deployed as part of the artifact interaction surface. Adoption of anything it surfaces happens only through the ordinary path -- a DEC-0337 option survey followed by DEC-0335 design intake -- never by this spike's findings alone.

## Question

Do compiled structural rules fire true findings on the real design? Concretely: when ~12 structural rules -- drawn half from the system-architecture-bp corpus (dependency cycles, stability direction, orphaned interfaces) and half from Groundwork's own rule-type decisions (citation integrity, mandatory-contract-kind completeness, Uses-typing/build-order) -- are compiled as ActiveGraph behaviors and fired against SP-0013's projected graph, are the findings real, noise, or change-worthy?

## Why It Blocks

Blocks nothing today. It is the load-bearing evidence for the executable-design-knowledge idea (DEC-0354): if compiled structural rules mostly fire noise, the approach's central premise weakens regardless of ActiveGraph as substrate. SP-0016 (SP-D) and SP-0017 (SP-E) both depend on this spike's rulebase.

## Method

Hand-compile approximately 12 structural rules as ActiveGraph behaviors: roughly six from the system-architecture-bp corpus (dependency cycles, stability direction, orphaned interfaces) and roughly six from Groundwork's own rule-type DECs (citation integrity, mandatory-contract-kind completeness, Uses-typing/build-order). Fire the rulebase against the graph SP-0013 projected. The stakeholder disposes every finding the rules produce -- real, noise, or change-worthy.

This spike builds a throwaway executable; per DEC-0345, its validation approach (the checks described above) is part of the reviewed spike design, not chosen ad hoc after the fact, and is sized minimally per DEC-0336's throwaway-scope yardstick.

The rulebase must position itself against DEC-0315's per-operation-checks-vs-full-checker-gate architecture: these rules are exploratory firing over a projection, not a replacement for the pre-commit gate. The structural contracts it validates are the ones SP-0013 projects -- DEC-0309's Uses-edges source-of-truth/depends-on projection and DEC-0299's typed Uses vocabulary (interface/implementation/test) -- and element-taxonomy/obligation checks defer to DEC-0086, which gives SPEC-design-elements ownership of that taxonomy.

### Expanded rulebase (SES-0069)

At take-up, the stakeholder directed expansion beyond the planned ~12 rules to every structural rule the two curated sources worthily ground (SES-0069 T9): the executed rulebase is 24 rules -- 14 discovery rules (including schema resolution per DEC-0089, test-double ownership and promotion-candidate detection per DEC-0306, staleness propagation per DEC-0096, seam-graduation candidates, bundle closure per DEC-0303, and best-practice rules for data reach-in, pass-through services, and happy-path-only contracts), 5 calibration rules with recorded expected outputs (item-citation completeness: SP-0013's 10 provenance edge cases; DEC-0309 projection equality: zero; bundle closure: the IDEA-0026 range dispute; fake-promotion candidates: DEC-0359's three; uncovered approved stories: the 19 known checker coverage warnings), 3 rules vacuous against current data (per DEC-0365's acknowledgment), and 2 weak/proxy-grounding probes retained deliberately as noise-rate tests. Contract-kind completeness checks follow DEC-0088's obligation matrix; Implements-coverage checks follow DEC-0092 and DEC-0094. Grounding-strength tags are recorded per rule; the best-practice corpus grounds its rules via practitioner sources, not Martin's named package principles.

## Evaluation Criteria
Descriptive measures, no pass/fail threshold (DEC-0355): a complete findings catalog with the stakeholder's disposition on each (real / noise / change-worthy); per-rule precision notes (which rules fired only real findings, which fired noise, and why).

## Data-Source Assumptions

**Execution precondition (DEC-0358).** SP-0013's findings show zero typed `Uses:` lines exist anywhere in the corpus, so the dependency-cycle, stability-direction, and build-order rules in this spike's planned rulebase have no edge data to fire against today. Per DEC-0358, this spike's execution is deferred until the corpus-wide `Uses:` backfill is taken up and completed; it does not proceed with a reduced rulebase in the interim.

**Precondition met (DEC-0365).** SES-0066 executed the corpus-wide `Uses:` backfill (DEC-0359) and armed checker enforcement (DEC-0360): 71 typed edges now exist across the 15 conforming CMPs' 53 elements. DEC-0358's precondition is satisfied; SP-0014 is unblocked and may execute in its own future session. Note the qualifier distribution is 100% `(interface)`, zero `(implementation)` -- SP-0014's build-order/serialization rules will be vacuously satisfied against this data (an acknowledged, not blocking, consequence).

## Findings

Pending — recorded at spike completion.


## Resulting Decisions

Pending — a completed spike produces at least one decision, even "assumption confirmed, no change."
