---
id: DEC-0484
type: decision
title: "Rule hosting: Engine-owned rule code with declarative policy config, substrate-neutral pending the ActiveGraph consolidation"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-13
source-span: "SES-0091 @ T6-T11"
overview: >-
  Rule authoring needed a contract shape between Engine-provided
  machinery and rule-author-supplied content. This decision makes
  rule logic Engine-owned code with declarative committed
  configuration for tunable tables (approvers, thresholds, gate
  policies), ships no rule DSL or extension point, and keeps the
  hosting contract substrate-neutral — hand-written checker code or
  compiled ActiveGraph behaviors — pending the ActiveGraph spike
  program's consolidation.
links:
  derives-from: [SES-0091]
  relates-to: [DEC-0469, DEC-0470, DEC-0263, DEC-0354, DEC-0387, DEC-0475]
---

# DEC-0484: Rule hosting: Engine-owned rule code with declarative policy config, substrate-neutral pending the ActiveGraph consolidation

## Context

When a paradigm rule is added or changed, what its author writes and what the Engine provides needed a contract shape.

## Decision

Rule logic is Engine-owned code, and the tunable tables rules consult — approvers, thresholds, gate policies — are declarative committed configuration, continuing the governance-as-code pattern. No rule DSL or published extension point ships. The hosting contract is substrate-neutral: whether rule families execute as hand-written checker code or as compiled ActiveGraph behaviors over a typed projection is an implementation choice, decided after the ActiveGraph spike program's consolidation, and the contract must not preclude either substrate.

## Rationale

This matches the working governance configuration pattern of DEC-0263, while a rule language rich enough for the corpus's structural rules would grow into a programming language and constitute the extension point DEC-0470 declined. The stakeholder's substrate-awareness condition is grounded in DEC-0354's spike program, the SP-0014 and SP-0016 findings including DEC-0387, and the proposed DEC-0370 and DEC-0373 awaiting the consolidation session.

## Alternatives Considered

Fully declarative rules were rejected for DSL strain and extension-point tension. Baking policy into code was rejected because every governance tweak would become an Engine release, retiring governance-as-code.

## Implications

EP-0014 authors configuration and commissions rule logic; the rule-family hosting contract describes obligations without naming an execution substrate; the ActiveGraph consolidation session later selects the substrate.
