---
id: DEC-0178
type: decision
title: Eval harness enforces judge-model independence via config-declared model-family check
status: accepted
owner: ds-lead
created: 2026-07-08
overview: >-
  Enforces DEC-0058's judge-model independence requirement via
  config-declared model-family check: the harness refuses to run
  faithfulness evals when the judge and session model families match.
  Constrains evaluation harness configuration and gating behavior.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0033 @ T2-T3"
links:
  derives-from: [SES-0033]
  supersedes: []
---

# DEC-0178: Eval Harness Enforces Judge-Model Independence via Config-Declared Model-Family Check

## Context

DEC-0058 requires the distillation-faithfulness
judge to differ from the session model, but left the enforcement
mechanism open. Without a check, a deployment could silently point both
roles at the same model family and lose the independence guarantee.

## Decision

The evaluation harness config declares the judge model's family
separately from the session model's family; the harness refuses to run
faithfulness evals when the two match. This mirrors the project's own
decision-recall audit discipline (a fixed independent judge tier,
distinct from the facilitator).

## Rationale

A declarative, harness-enforced check is cheap, deployment-portable, and
fails loud (refuses to run) rather than silently degrading eval
trustworthiness — matching the stakes of a gate that blocks pack changes
and model swaps.

## Alternatives Considered

- **Fixed judge model, hardcoded**: couples the harness to one vendor/model
  indefinitely; brittle as models are deprecated.
- **Unenforced requirement, left to implementer discretion**: no
  guardrail against silent misconfiguration; defeats the purpose of the
  independence requirement.

## Implications

ST-0041's acceptance criteria
require the family-check enforcement as a testable behavior.
