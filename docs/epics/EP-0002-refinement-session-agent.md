---
id: EP-0002
type: epic
title: Refinement Session Agent
status: draft
owner: ds-lead
created: 2026-07-05
links:
  derives-from: [BG-0001]
  satisfies: [BG-0001]
  depends-on: [EP-0001]
  impacts: [EP-0004, EP-0006, EP-0007]
  impacted-by: [EP-0001, EP-0006]
cites: [DEC-0003, DEC-0005, DEC-0012, DEC-0015, DEC-0021, DEC-0026]
---

# EP-0002: Refinement Session Agent

## Summary

The AI agent that conducts unsupervised 1:1 refinement sessions: grilling
participants with dependency-ordered clarifying questions (recommended answer
per question), capturing verbatim transcripts, distilling Decision records,
challenging terminology against the glossary, detecting and mediating
conflicts, and synthesizing multiple participants' sessions into a single
artifact. The most novel component in the system and the v1 centerpiece.

## Why (Goal Alignment)

This is the direct attack on BG-0001's problem statement: vague,
contradictory requests become refined, ratified artifacts through the
session experience. Conflict surfacing (BG-0001 outcome 2) is this agent's
mediation flow ([DEC-0005](../decisions/DEC-0005-intent-first-mediation-then-escalation.md));
provenance (outcome 1) begins with its transcript capture and distillation
([DEC-0015](../decisions/DEC-0015-transcript-decision-citation-chain.md)).

## Scope

**In:** session conduct (grilling methodology per artifact type: goal
refinement first, epic/story refinement later); transcript capture
(append-only, turn-numbered); Decision distillation with turn-span citation;
glossary challenge and CONTEXT.md maintenance
([DEC-0012](../decisions/DEC-0012-agent-built-domain-model.md)); conflict
detection, intent-discovery, mediation, and escalation packaging; cross-
session synthesis ([DEC-0021](../decisions/DEC-0021-one-on-one-sessions.md));
artifact drafting from synthesized sessions.

**Out:** the chat UI itself (EP-0006); gate mechanics (EP-0003); context
retrieval infrastructure (EP-0004, EP-0007 — this epic consumes their
interfaces).

## Domain Context

Bounded context: **Refinement**. Terms: Session, Transcript, Decision,
Conflict, Synthesis, Refinement Session — per [CONTEXT.md](../../CONTEXT.md).

## Interfaces & Contracts to Define

- **Session engine contract**: start/resume/close sessions, stream turns —
  the boundary the pluggable Q&A UI talks to.
- **Distillation contract**: session → proposed DEC records (human-visible
  before acceptance).
- **Question-strategy definition**: the grilling methodology as inspectable,
  versioned prompt/policy assets, not buried in code.
- **Model-provider boundary**: agent logic portable across model versions.

## Risks & Open Questions

- Quality bar for unsupervised operation ([DEC-0003](../decisions/DEC-0003-unsupervised-sessions.md)):
  what does the agent do when a participant is confused, hostile, or gives
  unusable answers? Escalation and session-abandonment paths — candidate
  spike.
- Distillation faithfulness: guarding against decisions the transcript
  doesn't actually support — evaluation harness needed.

## Derived Work

None yet — stories/spikes follow refinement and approval of this epic.
