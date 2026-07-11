---
id: SP-0015
type: spike
title: "Prose-to-rule compilation fidelity"
status: draft
owner: awakeinagi@gmail.com
created: 2026-07-10
timebox: 1 session
overview: >-
  Question: can prose best-practice knowledge compile into checkable
  rules without corruption? Method: one bounded curated source (an
  arc42 section from system-architecture-bp, or a chapter extracted
  via a book-to-skill-style pipeline); an agent compiles it into
  candidate rules, each citing its source passage; stakeholder
  reviews rule-vs-passage side by side. Independent of
  SP-0013/SP-0014. Evaluation criteria: ratifiable-as-is rate;
  catalog of compilation failure modes (over-generalization, lost
  applicability conditions, invented specificity) -- explicitly no
  kill bar (DEC-0355). Data-source assumptions: source is
  curated/licensed content already in the corpus or explicitly
  provided; passage-level citations are resolvable. Deliverable:
  fidelity report.
links:
  derives-from: [EP-0009]
cites: [DEC-0354, DEC-0351, DEC-0335, DEC-0337, DEC-0355, DEC-0345, DEC-0336]
---

> Guardrails (DEC-0351): this spike's outputs are strictly throwaway and are never deployed as part of the artifact interaction surface. Adoption of anything it surfaces happens only through the ordinary path -- a DEC-0337 option survey followed by DEC-0335 design intake -- never by this spike's findings alone.

## Question

Can prose best-practice knowledge compile into checkable rules without corruption? Concretely: when an agent compiles one bounded curated source into candidate rules, each citing its source passage, how often is the result ratifiable as-is, and what does it get wrong?

## Why It Blocks

Blocks nothing today. It is independent evidence for the compilation half of the executable-design-knowledge idea (DEC-0354) -- separate from SP-0014's hand-compiled rules, this spike tests whether an agent can do the compilation step itself faithfully, which matters for the approach scaling beyond a handful of hand-written rules.

## Method

Select one bounded curated source: an arc42 section from system-architecture-bp, or a chapter extracted via a book-to-skill-style pipeline. An agent compiles it into candidate rules, each citing the specific source passage it was compiled from. The stakeholder reviews each candidate rule against its cited passage, side by side.

This spike builds a throwaway executable; per DEC-0345, its validation approach (the checks described above) is part of the reviewed spike design, not chosen ad hoc after the fact, and is sized minimally per DEC-0336's throwaway-scope yardstick.

## Evaluation Criteria
Descriptive measures, no pass/fail threshold (DEC-0355): the ratifiable-as-is rate (fraction of candidate rules the stakeholder accepts without edits); a catalog of compilation failure modes observed (over-generalization, lost applicability conditions, invented specificity not present in the source).

## Data-Source Assumptions
The source passage is curated/licensed content already present in the corpus (e.g. system-architecture-bp's vendored arc42 material) or explicitly provided for this spike; passage-level citations are resolvable back to a specific location in the source so the stakeholder's side-by-side review is possible.

## Findings

Pending — recorded at spike completion.


## Resulting Decisions

Pending — a completed spike produces at least one decision, even "assumption confirmed, no change."
