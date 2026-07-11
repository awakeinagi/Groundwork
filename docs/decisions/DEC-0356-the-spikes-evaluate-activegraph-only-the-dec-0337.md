---
id: DEC-0356
type: decision
title: "The spikes evaluate ActiveGraph only; the DEC-0337 option survey is deferred until after the spikes report"
status: proposed
owner: awakeinagi@gmail.com
created: 2026-07-10
decided-by: awakeinagi
decided-on: 2026-07-10
source-span: "SES-0064 @ T9"
overview: >-
  The five-spike program evaluates ActiveGraph only. The DEC-0337
  option survey -- comparing at minimum the current judge-agent-
  with-checklist baseline and a thin owned implementation of the
  same rule concepts -- is deliberately deferred until after the
  spikes report, and must run before any adoption decision, followed
  by DEC-0335 design intake. This is consistent with DEC-0351's
  adoption routing (spike findings never self-authorize deployment).
  Confirmed in SES-0064 (T9) via stakeholder option selection.
links:
  derives-from: [SES-0064]
  relates-to: [DEC-0337, DEC-0351, DEC-0354, DEC-0336]
---

## Context

T9's option selections confirmed ActiveGraph-only scope for the spikes themselves, raising the question of when the DEC-0337 option survey (which must compare ActiveGraph against alternatives before any adoption) happens relative to the spike program.

## Decision

The spikes evaluate ActiveGraph only. The DEC-0337 option survey -- comparing at minimum the current judge-agent-with-checklist baseline and a thin owned implementation of the same rule concepts -- is deliberately deferred until after the spikes report, and must run before any adoption decision, followed by DEC-0335 design intake. This is consistent with DEC-0351's adoption routing.

## Rationale

Running a full option survey before the spikes exist would compare alternatives against a hypothesis, not evidence -- the spikes exist precisely to generate the evidence the survey needs about what ActiveGraph's approach actually buys. Deferring the survey (not skipping it) keeps DEC-0337's research-before-build guarantee intact for the eventual adoption decision while letting the exploratory work proceed focused.

## Alternatives Considered

- **Run the DEC-0337 survey before any spike starts** -- rejected; there is nothing yet to compare the baseline and thin-owned-implementation options against beyond the T4 elaboration.
- **Skip the option survey altogether and adopt on spike findings alone** -- rejected; violates DEC-0351's explicit adoption-routing guardrail and DEC-0337's option-survey requirement.

## Implications

No adoption decision may be made until the DEC-0337 survey (baseline vs. thin owned implementation vs. ActiveGraph) runs and DEC-0335 design intake follows. The spikes' findings feed that survey as evidence, not as a substitute for it.
