---
id: DEC-0355
type: decision
title: "The ActiveGraph spike program is exploratory with no kill-bar success thresholds"
status: proposed
owner: awakeinagi@gmail.com
created: 2026-07-10
decided-by: awakeinagi
decided-on: 2026-07-10
source-span: "SES-0064 @ T8-T9"
overview: >-
  The five-spike ActiveGraph program (DEC-0354) is exploratory: no
  spike carries a pass/fail kill-bar threshold. Each spike states
  explicit evaluation criteria -- what it measures and catalogs --
  and its data-source assumptions, per EP-0009's reviewer-debate
  residual (grounding through contracts, DEC-0336), but sets no
  adoption bar. Adoption thresholds are set only after this evidence
  exists, at the DEC-0337 option-survey/DEC-0335 design-intake stage
  that follows the spikes' report. Confirmed in SES-0064 (T9) via
  stakeholder option selection.
links:
  derives-from: [SES-0064]
  relates-to: [DEC-0354, DEC-0336, DEC-0345]
---

## Context

At T8 the facilitator proposed the five-spike set with a recommended success bar per spike. The stakeholder's T9 option selections confirmed the spikes but explicitly declined to set kill-bar thresholds at design time, asking instead for each spike to state what it measures.

## Decision

The spike program is exploratory: no spike carries a pass/fail kill-bar threshold. Each of the five SP artifacts states an explicit "Evaluation Criteria" section (what it measures and catalogs) and a "Data-Source Assumptions" section, but sets no adoption bar. Adoption thresholds are set only after the spikes' evidence exists, at the DEC-0337 option-survey / DEC-0335 design-intake stage.

## Rationale

The program's purpose is to gather evidence about an unfamiliar, alpha-stage tool against the real corpus, not to pre-commit to an adoption bar before that evidence exists -- premature thresholds would bias what gets measured. Requiring explicit evaluation criteria (rather than a vague "see what happens") keeps the spikes grounded and contract-bearing per DEC-0336, without collapsing into a false kill/no-kill verdict the exploratory framing does not support.

## Alternatives Considered

- **Set a numeric kill-bar per spike (e.g. SP-A's coverage recommendation from T8)** -- rejected by the stakeholder at T9; premature given the tool's alpha maturity and the unknowns the spikes exist to surface.
- **No evaluation criteria at all, purely narrative findings** -- rejected; EP-0009's reviewer-debate residual and DEC-0336's grounding-through-contracts priority require each spike to state what it measures before it runs.

## Implications

Every SP-0013..SP-0017 body carries "Evaluation Criteria" (explicitly no pass/fail threshold) and "Data-Source Assumptions" sections. The DEC-0337 survey, not this decision or any spike's findings alone, sets adoption thresholds once the evidence exists.
