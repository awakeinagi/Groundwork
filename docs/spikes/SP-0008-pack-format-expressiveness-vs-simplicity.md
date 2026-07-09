---
id: SP-0008
type: spike
title: Pack format expressiveness vs. simplicity
status: approved
owner: ds-lead
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
created: 2026-07-08
timebox: 3d
links:
  derives-from: [EP-0002]
  satisfies: [BG-0001]
  relates-to: [ST-0033]
cites: [DEC-0056, DEC-0181]
---

# SP-0008: Pack Format Expressiveness vs. Simplicity

## Question

Can a declarative `pack.yaml` schema (phases, stopping criteria,
escalation triggers, guardrail policy, context recipe) express real
strategy-pack variation, or does authoring real packs require escalating
to a general scripting/templating layer?

## Why It Blocks

ST-0033's
schema is drafted but not final — a declarative-only schema that can't
express real branching or conditional behavior would force a rework of
the format itself, not just individual packs, and every other story in
this epic (guardrails, context assembly, glossary maintenance, eval
harness) builds on packs conforming to that format
(per DEC-0181).

## Method

1. Draft the `pack.yaml` schema per
   DEC-0053 and
   ST-0033,
   including the context-recipe field
   (per DEC-0056)
   that scenario 2 and 3 below will exercise for expressiveness.
2. Design three concrete pack scenarios chosen for maximum shape
   diversity: a linear grilling flow (goal-refinement), a mediation flow
   with escalation branching (conflict-mediation), and a classification
   flow (CP-triage).
3. For each scenario, check whether its real behavior (stopping
   conditions, branch points, escalation triggers) is expressible in the
   declarative schema without an escape hatch.
4. Where a scenario can't be expressed declaratively, record the
   specific gap (what construct was needed) rather than a pass/fail
   verdict alone.

## Findings

Pending — filled at completion.

## Resulting Decisions

Pending — completion requires ≥1 DEC deriving from this spike.
