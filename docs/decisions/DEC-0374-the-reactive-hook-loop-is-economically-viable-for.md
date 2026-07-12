---
id: DEC-0374
type: decision
title: "The reactive hook-loop is economically viable for Groundwork's checker (SP-0016)"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-11
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-11
source-span: "SES-0071"
overview: >-
  The edit -> project-delta -> fire-rulebase -> inject-findings loop
  pays for itself in context economy at current corpus scale.
  Evidence from SP-0016 (throwaway build): the batch projection +
  24-rule rulebase costs ~0.5s cold per edit over the 588-artifact
  corpus; only edit-introduced findings are injected (delta versus a
  clean baseline), DEC-0118 two-tier cite-ready packaged, at ~35
  tokens for a clean edit and ~64 tokens for one actionable
  violation; a live Sonnet design-editing agent caught and corrected
  a seeded superseded-cite violation (cited superseded DEC-0289,
  corrected to successor DEC-0316) using ONLY the injected finding,
  with no best-practice or decision source texts in its context
  (verified: the successor DEC appeared only in the injection; the
  agent read no decision files; 3 tool uses total). This confirms
  the T3 context-window force-multiplier premise behind DEC-0354.
  Descriptive result, no kill bar (DEC-0355). Scope: SP-0016's build
  is strictly throwaway (DEC-0351); adoption of reactive checking
  happens only through the ordinary DEC-0337 option survey +
  DEC-0335 design intake.
links:
  relates-to: [DEC-0354, DEC-0355, DEC-0351, DEC-0118, DEC-0315, DEC-0375, DEC-0368]
  derives-from: [SES-0071]
---

# The reactive hook-loop is economically viable for Groundwork's checker (SP-0016)

## Context

SP-0016 tested the stakeholder's original T3 framing (context-window force-multiplier, DEC-0354): does an edit -> project-delta -> fire-rulebase -> inject-findings loop pay for itself in context economy? The build is throwaway per DEC-0351 and reused SP-0014's projector and 24-rule rulebase.

## Decision

The reactive hook-loop pays for itself in context economy at current corpus scale (588 artifacts). The batch projection plus 24-rule rulebase costs ~0.5s cold per edit; only edit-introduced findings are injected (delta versus a clean baseline), packaged per DEC-0118's two-tier cite-ready format, at ~35 tokens for a clean edit and ~64 tokens for one actionable violation. A live Sonnet design-editing agent caught and corrected a seeded superseded-cite violation -- an edit citing superseded DEC-0289 was corrected to successor DEC-0316 -- using ONLY the injected finding, with no best-practice or decision source texts in its context.

## Rationale

SES-0071 base tests: T-a (benign edit) confirmed the hook fires end-to-end and injects "no new structural findings" at ~35 tokens, 0.69s latency. T-c (seeded R8 superseded-cite) confirmed the hook injects exactly one finding at ~64 tokens (0.4992s), and the agent corrected DEC-0289 to DEC-0316 from that finding alone; a second hook fire then confirmed "no new structural findings" (0.4721s, ~35 tokens). Independence of the correction from any source text was verified three ways: DEC-0316 appears nowhere in the mirror file or task prompt except the injected finding; the agent made 3 tool uses total (Read, Edit, Edit) and read no decision/source files; the correction occurred with zero intervening tool calls. This confirms the T3 context-window force-multiplier premise behind DEC-0354.

## Alternatives Considered

Treating the result as a pass/fail gate was rejected -- SP-0016 is evaluated descriptively only, with no kill bar (DEC-0355); the finding is a measurement, not a threshold verdict.

## Implications

SP-0016's build remains strictly throwaway (DEC-0351); this decision records a descriptive result, not an adoption. Any adoption of reactive checking for Groundwork's own checker proceeds only through the ordinary DEC-0337 option survey followed by DEC-0335 design intake -- never by this spike's findings alone.
