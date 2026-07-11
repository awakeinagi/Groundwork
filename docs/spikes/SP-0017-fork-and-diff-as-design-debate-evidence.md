---
id: SP-0017
type: spike
title: "Fork-and-diff as design-debate evidence"
status: draft
owner: awakeinagi@gmail.com
created: 2026-07-10
timebox: 1 session
overview: >-
  Question: does forking a design run and diffing rule findings
  across two alternative designs produce decision-grade evidence?
  Method: encode two alternative designs for a question the corpus
  has already decided; run both through SP-0014 (SP-B)'s rulebase
  via ActiveGraph fork-and-diff; compare the structural findings-
  diff against what the recorded architect debate actually surfaced.
  Depends on SP-0014 (impacted-by); explicitly queued last.
  Evaluation criteria: findings-diff vs. historical-debate
  comparison -- what the diff surfaced that the debate missed and
  vice versa -- explicitly no kill bar (DEC-0355). Data-source
  assumptions: at least one decided design question with a recorded
  dual-instance debate exists in the corpus (several do); SP-0014's
  rulebase. Deliverable: comparison report.
links:
  impacted-by: [SP-0014]
  derives-from: [EP-0009]
  relates-to: [SP-0014]
cites: [DEC-0354, DEC-0351, DEC-0335, DEC-0337, DEC-0355, DEC-0345, DEC-0336]
---

> Guardrails (DEC-0351): this spike's outputs are strictly throwaway and are never deployed as part of the artifact interaction surface. Adoption of anything it surfaces happens only through the ordinary path -- a DEC-0337 option survey followed by DEC-0335 design intake -- never by this spike's findings alone.

## Question

Does forking a design run and diffing rule findings across two alternative designs produce decision-grade evidence? Concretely: for a question the corpus has already decided through a recorded dual-instance architect debate, does an ActiveGraph fork-and-diff of the two alternatives' structural findings surface anything the debate missed, or miss anything the debate surfaced?

## Why It Blocks

Blocks nothing today; explicitly queued last since it depends on SP-0014's rulebase. It is the test of the T4 fork-and-diff idea as empirical evidence in design debates within the DEC-0354 executable-design-knowledge program -- if the diff mostly reproduces or misses what human/agent debate already surfaces, the case for fork-and-diff as a distinct value-add weakens.

## Method

Encode two alternative designs for a question the corpus has already decided (a question with a recorded dual-instance architect debate). Run both alternatives through SP-0014's rulebase via ActiveGraph's fork-and-diff mechanism. Compare the resulting structural findings-diff against what the recorded debate actually surfaced.

This spike builds a throwaway executable; per DEC-0345, its validation approach (the checks described above) is part of the reviewed spike design, not chosen ad hoc after the fact, and is sized minimally per DEC-0336's throwaway-scope yardstick.

## Evaluation Criteria
Descriptive measures, no pass/fail threshold (DEC-0355): the findings-diff compared against the historical-debate record -- what the diff surfaced that the debate missed, and what the debate surfaced that the diff missed.

## Data-Source Assumptions
At least one decided design question with a recorded dual-instance debate exists in the corpus (several do). SP-0014's rulebase exists and is reusable for this spike's two alternative-design encodings.

## Findings

Pending — recorded at spike completion.


## Resulting Decisions

Pending — a completed spike produces at least one decision, even "assumption confirmed, no change."
