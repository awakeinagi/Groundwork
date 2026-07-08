---
id: ST-0041
type: story
title: Evaluation harness
status: approved
owner: ds-lead
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
created: 2026-07-08
links:
  derives-from: [EP-0002]
  satisfies: [BG-0001]
  depends-on: [ST-0034, ST-0035]
  impacts: []
  impacted-by: [ST-0033, ST-0034, ST-0035]
cites: [DEC-0052, DEC-0058, DEC-0178, DEC-0179]
---

# ST-0041: Evaluation Harness

## Summary

The quality gate that stands between the agent's methodology and
production use: distillation-faithfulness judging by an independent
model, grilling-quality benchmarks, guardrail behavior tests, and
periodic drift audits — gating every strategy-pack change and every LLM
swap before it can merge.

## Acceptance Criteria

1. Distillation faithfulness is judged by verifying each Decision is
   supported by its cited turn span, using a judge model whose declared
   model family differs from the session model's family; the harness
   refuses to run the faithfulness eval when the families match
   (per [DEC-0058](../decisions/DEC-0058-evaluation-harness.md),
   [DEC-0178](../decisions/DEC-0178-eval-harness-judge-model-family-independence.md)).
2. Grilling quality is scored against a hand-authored seed benchmark
   corpus covering every strategy-pack phase (goal-refinement,
   epic-refinement, story-refinement, conflict-mediation, CP-triage) —
   coverage, dependency ordering, and recommended-answer discipline; the
   corpus exists and is exercised before the harness gates anything
   (per [DEC-0058](../decisions/DEC-0058-evaluation-harness.md),
   [DEC-0179](../decisions/DEC-0179-eval-harness-seed-benchmark-corpus.md)).
3. Guardrail behavior tests exercise the unproductive-pattern detection
   and graceful-exit paths (reframe, park-and-continue, offer pause,
   partial-record end) against benchmark scenarios
   (per [DEC-0058](../decisions/DEC-0058-evaluation-harness.md),
   [DEC-0054](../decisions/DEC-0054-guardrails-authority-limits.md)).
4. A strategy-pack change or an LLM swap cannot merge without passing the
   full benchmark suite — the tier-2 validation pattern applied to
   methodology, not just code
   (per [DEC-0058](../decisions/DEC-0058-evaluation-harness.md)).
5. Periodic drift audits re-run distillation from raw transcripts of
   past sessions — the transcript being the verbatim, append-only source
   of truth distillation is always regenerable from — and diff the
   result against the accepted Decisions on record, surfacing any
   divergence for review
   (per [DEC-0058](../decisions/DEC-0058-evaluation-harness.md),
   [DEC-0052](../decisions/DEC-0052-raw-transcripts-regenerable-distillation.md)).

## Component Impact

None yet — a Component Doc for this epic's bounded context is stubbed once the first story here refines toward it.

## Out of Scope

The pack PR-gating mechanism itself as a check
([EP-0003](../epics/EP-0003-governance-and-gate-engine.md) owns gate
check machinery; this story defines what the check must verify);
authoring the seed corpus's actual scenario content (a deliverable of
this story's AC 2, but the scenario-writing work itself, not a design
contract); this project's own decision-recall audit tooling — a
different, meta-level evaluation of Groundwork's own refinement process,
not of the agent this story specifies.

## Notes for Implementers

Judge-model independence (AC 1) is a config-declared family check, not a
runtime capability probe — the harness trusts the declared family, it
does not attempt to fingerprint the model.
