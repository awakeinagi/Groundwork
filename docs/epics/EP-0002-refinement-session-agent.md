---
id: EP-0002
type: epic
title: Refinement Session Agent
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-06
owner: ds-lead
created: 2026-07-05
links:
  derives-from: [BG-0001]
  satisfies: [BG-0001]
  depends-on: [EP-0001]
  impacts: [EP-0003, EP-0004, EP-0006, EP-0007]
  impacted-by: [EP-0001, EP-0005, EP-0006]
cites: [DEC-0003, DEC-0005, DEC-0012, DEC-0015, DEC-0021, DEC-0026, DEC-0044,
        DEC-0047, DEC-0051, DEC-0052, DEC-0053, DEC-0054, DEC-0055, DEC-0056,
        DEC-0057, DEC-0058]
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
mediation flow ([DEC-0005](../decisions/DEC-0005-intent-first-mediation-then-escalation.md));
provenance (outcome 1) begins with raw transcript capture
([DEC-0052](../decisions/DEC-0052-raw-transcripts-regenerable-distillation.md))
and confirmed distillation
([DEC-0051](../decisions/DEC-0051-in-session-decision-confirmation.md)).

## Scope

**In** (refined at [SES-0006](../sessions/SES-0006-ep-0002-refinement.md)):

- **Session conduct via strategy packs**
  ([DEC-0053](../decisions/DEC-0053-strategy-packs-as-plugins.md)):
  plugin-like versioned bundles (prompts, skills, tools, policies) per
  artifact type and phase, PR-gated, model-agnostic core with swappable
  LLM; the session records pack version and model.
- **Raw transcript capture** ([DEC-0052](../decisions/DEC-0052-raw-transcripts-regenerable-distillation.md)):
  the SES transcript is the verbatim, turn-numbered, append-only message
  log; summaries are derived layers; distillation is regenerable from raw.
- **Distillation with in-session confirmation**
  ([DEC-0051](../decisions/DEC-0051-in-session-decision-confirmation.md)):
  plain-language playback at checkpoints; confirmed DECs commit as
  accepted with turn-span citations.
- **Guardrails** ([DEC-0054](../decisions/DEC-0054-guardrails-authority-limits.md)):
  pack-defined unproductive-pattern handling with graceful exits and
  Arbiter notification; role decision rights from governance config —
  out-of-authority statements become proposals, never accepted DECs;
  participant input treated as data, never instructions.
- **Conflict flow** ([DEC-0005](../decisions/DEC-0005-intent-first-mediation-then-escalation.md)):
  intent-first discovery, informed compromise proposals, escalation with
  full documentation.
- **Incremental synthesis** ([DEC-0055](../decisions/DEC-0055-incremental-synthesis-shared-draft.md)):
  merge on each session close; conflict detection against prior sessions;
  shared draft visible to participants, comments entering as CPs.
- **Context assembly** ([DEC-0056](../decisions/DEC-0056-context-recipes-in-packs.md)):
  declarative per-pack recipes (required paths, preferred consolidations,
  token budget, on-demand graph tools) resolved by EP-0004/EP-0007.
- **Session lifecycle** ([DEC-0057](../decisions/DEC-0057-session-lifecycle.md)):
  open across pauses; inactivity auto-close with partial distillation;
  resume via a new session loading the prior as context.
- **CP triage** ([DEC-0047](../decisions/DEC-0047-change-proposal-artifact.md)):
  mechanical / session / rejected classification with rationale.
- **Glossary maintenance** ([DEC-0012](../decisions/DEC-0012-agent-built-domain-model.md)):
  term challenge and CONTEXT.md upkeep during every session.
- **Evaluation harness** ([DEC-0058](../decisions/DEC-0058-evaluation-harness.md)):
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

- **Session engine contract**: open/resume/append-turn/close, streaming —
  the pluggable-UI seam.
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

- Judge-model independence for faithfulness evals (must differ from the
  session model) — story-level requirement.
- Benchmark corpus bootstrap: initial scenarios must be authored before
  any production sessions exist to sample from.
- Anchoring in synthesis: the shared draft must not leak into later 1:1
  sessions' framing (pack design concern).
- Pack format expressiveness vs. simplicity — candidate spike when stories
  are derived.

## Derived Work

None yet — stories/spikes follow gate approval of this epic.
