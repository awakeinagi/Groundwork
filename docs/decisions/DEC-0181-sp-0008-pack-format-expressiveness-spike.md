---
id: DEC-0181
type: decision
title: A timeboxed spike validates pack schema expressiveness before the pack-format story locks in
status: accepted
owner: ds-lead
created: 2026-07-08
overview: >-
  Prescribes SP-0008, a 3-day spike validating whether a declarative
  pack.yaml schema can express real strategy-pack variation without
  needing a scripting layer. Method: draft against three concrete
  scenarios spanning phase diversity.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0033 @ T6-T7"
links:
  derives-from: [SES-0033]
  relates-to: [DEC-0053]
  supersedes: []
---

# DEC-0181: A Timeboxed Spike Validates Pack Schema Expressiveness Before the Pack-Format Story Locks In

## Context

EP-0002's Risks named
"pack format expressiveness vs. simplicity" as a candidate spike once
stories were derived — a genuine unknown blocking
ST-0033's
schema design: can a declarative `pack.yaml` express real strategy-pack
variation, or does it need to escalate to a scripting/templating layer?

## Decision

SP-0008
is timeboxed at 3 days. Question: can a declarative `pack.yaml` schema
(phases, stopping criteria, escalation triggers, guardrail policy,
context recipe — per DEC-0053)
express real pack variation without a general scripting layer? Method:
draft the schema against three concrete pack scenarios spanning the
phase list (goal-refinement, conflict-mediation, CP-triage) and check
whether each scenario's behavior is expressible declaratively.

## Rationale

Three scenarios chosen for maximum shape diversity (a linear grilling
flow, a mediation flow with escalation branching, a triage
classification flow) give the spike a real test of expressiveness in a
timebox short enough not to block
ST-0033's
refinement.

## Alternatives Considered

- **Narrower 1-day spike validating only the field list**: skips the
  actual expressiveness question (declarative vs. scripting), which is
  the risk that matters — a complete field list says nothing about
  whether the fields can express branching or conditional behavior.

## Implications

ST-0033
is drafted now but its schema section should not be treated as final
until SP-0008's
findings land.
