---
id: DEC-0058
type: decision
title: An evaluation harness gates strategy-pack changes and LLM swaps
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0006 @ T4-T5"
links:
  derives-from: [SES-0006]
---

# DEC-0058: Evaluation harness gating methodology changes

## Context

Distillation faithfulness and grilling quality are EP-0002's flagged
risks; pack changes and model swaps
(DEC-0053) need a quality gate,
and DEC-0052
requires a drift-detection mechanism.

## Decision

The evaluation harness is in EP-0002's scope. It covers: **distillation
faithfulness** (an independent judge verifies each Decision is supported by
its cited turn span), **grilling quality** (coverage, dependency ordering,
recommended-answer discipline on benchmark scenarios), and **guardrail
behavior** (DEC-0054).
Strategy-pack changes and LLM swaps cannot merge without passing evals —
the tier-2 pattern (DEC-0034) applied to
methodology. Additionally, periodic **drift audits** re-run distillation
from raw transcripts and diff against accepted Decisions.

## Rationale

Methodology regressions should be caught by a harness, not by annoyed
stakeholders — during exactly the period trust in the system is being
established.

## Alternatives Considered

- **Separate quality epic later**: LLM swaps land unmeasured at the worst
  time.
- **Human review only**: no defense against silent regression.

## Implications

Benchmark scenario corpus becomes a maintained asset; judge-model
independence (different model than the session agent) is a story-level
requirement; drift-audit cadence is deployment configuration.
