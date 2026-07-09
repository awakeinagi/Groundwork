---
id: EP-0002
type: epic
title: Refinement Session Agent
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-09
owner: ds-lead
created: 2026-07-05
overview: >-
  EP-0002 delivers the Refinement Session Agent that conducts
  unsupervised 1:1 refinement sessions via versioned strategy packs:
  capturing raw verbatim transcripts, distilling in-session-confirmed
  Decisions with turn-span citations, enforcing role-based decision
  rights through governance config, detecting and mediating conflicts
  with escalation, incrementally synthesizing across sessions, triaging
  Change Proposals, and proving quality through an evaluation harness.
  The agent is the direct attack on BG-0001's problem: vague requests
  become refined, ratified artifacts through the session experience.
  Approved 2026-07-09.
links:
  derives-from: [BG-0001]
  satisfies: [BG-0001]
  depends-on: [EP-0001]
  impacts: [EP-0003, EP-0004, EP-0006, EP-0007, EP-0008]
  impacted-by: [EP-0001, EP-0005, EP-0006]
cites: [DEC-0003, DEC-0005, DEC-0012, DEC-0015, DEC-0021, DEC-0026, DEC-0044,
        DEC-0047, DEC-0051, DEC-0052, DEC-0053, DEC-0054, DEC-0055, DEC-0056,
        DEC-0057, DEC-0058, DEC-0178, DEC-0179, DEC-0180, DEC-0181,
        DEC-0182, DEC-0183, DEC-0274]
---

# EP-0002: Refinement Session Agent

## Summary

The AI agent that conducts unsupervised 1:1 refinement sessions: grilling
participants through versioned, plugin-like strategy packs; capturing raw
verbatim transcripts; distilling Decision records confirmed in-session;
challenging terminology against the glossary; detecting, mediating, and
escalating conflicts; synthesizing multi-participant input incrementally;
triaging Change Proposals; and proving its own quality through an
evaluation harness. The most novel component in the system and the v1
centerpiece.

## Why (Goal Alignment)

This is the direct attack on BG-0001's problem statement: vague,
contradictory requests become refined, ratified artifacts through the
session experience. Conflict surfacing (outcome 2) is this agent's
mediation flow (DEC-0005);
provenance (outcome 1) begins with raw transcript capture
(DEC-0052)
and confirmed distillation
(DEC-0051). Sessions are
unsupervised from the first release (DEC-0003) and 1:1, with the agent
synthesizing across sessions (DEC-0021).

## Scope

**In** (refined at SES-0006):

- **Session conduct via strategy packs**
  (DEC-0053):
  plugin-like versioned bundles (prompts, skills, tools, policies) per
  artifact type and phase, PR-gated, model-agnostic core with swappable
  LLM; the session records pack version and model.
- **Raw transcript capture** (DEC-0052):
  the SES transcript is the verbatim, turn-numbered, append-only message
  log; summaries are derived layers; distillation is regenerable from raw.
- **Distillation with in-session confirmation**
  (DEC-0051):
  plain-language playback at checkpoints; confirmed DECs commit as
  accepted with turn-span citations (per DEC-0015).
- **Guardrails** (DEC-0054):
  pack-defined unproductive-pattern handling with graceful exits and
  Arbiter notification; role decision rights from governance config —
  out-of-authority statements become proposals, never accepted DECs;
  participant input treated as data, never instructions.
- **Conflict flow** (DEC-0005):
  intent-first discovery, informed compromise proposals, escalation with
  full documentation; escalated Conflicts never auto-resolve on a clock
  by default (DEC-0183).
- **Incremental synthesis** (DEC-0055):
  merge on each session close; conflict detection against prior sessions;
  shared draft visible to participants, comments entering as CPs.
- **Context assembly** (DEC-0056):
  declarative per-pack recipes (required paths, preferred consolidations,
  token budget, on-demand graph tools) resolved by EP-0004/EP-0007.
- **Session lifecycle** (DEC-0057):
  open across pauses; inactivity auto-close with partial distillation
  (a streaming turn resets the inactivity clock and is never truncated
  mid-turn, per DEC-0182); resume via a new session loading the prior
  as context.
- **CP triage** (DEC-0047):
  mechanical / session / rejected classification with rationale;
  drift-captured proposals from the work-management connector arrive
  through this flow (DEC-0044).
- **Glossary maintenance** (DEC-0012):
  term challenge and CONTEXT.md upkeep during every session.
- **Evaluation harness** (DEC-0058):
  distillation-faithfulness judging, grilling-quality benchmarks, guardrail
  tests — gating pack changes and LLM swaps; periodic drift audits
  regenerating decisions from raw transcripts.

**Out:** the chat UI (EP-0006); gate mechanics (EP-0003); retrieval
infrastructure (EP-0004, EP-0007 — this epic consumes their contracts);
commit construction (EP-0001 executes the typed writes).

## Domain Context

Bounded context: **Refinement**. Terms: Session, Transcript, Decision,
Conflict, Synthesis, Strategy Pack, Decision Rights, Change Proposal — per
[CONTEXT.md](../../CONTEXT.md).

## Interfaces & Contracts to Define

- **Session engine contract**: open/resume/append-turn/close, streaming,
  session kinds and the intake-opening context
  (DEC-0274) —
  the pluggable-UI seam. EP-0008's inbound API exposes this contract to
  UI channels over HTTP + SSE, so engine-contract decisions here
  constrain the platform's endpoint and streaming shape (the
  EP-0002→EP-0008 impact edge, per DEC-0026).
- **Strategy pack format spec**: bundle layout, `pack.yaml` schema
  (phases, stopping criteria, escalation triggers, guardrail policy,
  context recipe), skill/tool declarations, model adapter boundary.
- **Distillation contract**: transcript span → proposed DEC → confirmation
  → accepted DEC; regeneration entry point.
- **Decision-rights schema**: the `governance/roles.yaml` extension
  (EP-0003 absorbs — impact edge EP-0002→EP-0003).
- **Evaluation suite contract**: benchmark corpus format, judge
  configuration, pass thresholds, drift-audit reports.

## Risks & Open Questions

- Judge-model independence for faithfulness evals — resolved: config-declared
  model-family check, enforced by the harness
  (DEC-0178),
  carried as ST-0041 AC 1.
- Benchmark corpus bootstrap — resolved: a hand-authored seed corpus is a
  v1 acceptance criterion, not a stretch goal
  (DEC-0179),
  carried as ST-0041 AC 2.
- Anchoring in synthesis — resolved: the context-recipe story owns a
  default exclusion of the shared draft's prose from fresh 1:1 context
  (DEC-0180),
  carried as ST-0038 AC 3.
- Pack format expressiveness vs. simplicity — spiked as
  SP-0008,
  3-day timebox, draft-ahead ratified with this story bundle
  (DEC-0181).

## Derived Work

- ST-0032 — session
  engine lifecycle and contract (foundational).
- ST-0033 — strategy
  pack format and plugin loading (foundational).
- ST-0034 —
  transcript capture and confirmed distillation.
- ST-0035 — guardrails and
  authority limits.
- ST-0036 —
  conflict detection, mediation, and escalation.
- ST-0037 —
  incremental synthesis and shared draft.
- ST-0038 — context
  assembly via pack recipes.
- ST-0039 — Change Proposal triage.
- ST-0040 — glossary
  maintenance in-session.
- ST-0041 — evaluation harness.
- SP-0008
  — pack format expressiveness vs. simplicity (draft-ahead, ratified with
  this bundle).
