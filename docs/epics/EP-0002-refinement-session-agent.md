---
id: EP-0002
type: epic
title: Refinement Session Agent
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: ds-lead
created: 2026-07-05
links:
  derives-from: [BG-0001]
  satisfies: [BG-0001]
  depends-on: [EP-0001]
  impacts: [EP-0003, EP-0004, EP-0006, EP-0007, EP-0008]
  impacted-by: [EP-0001, EP-0005, EP-0006]
cites: [DEC-0003, DEC-0005, DEC-0012, DEC-0015, DEC-0021, DEC-0026, DEC-0044,
        DEC-0047, DEC-0051, DEC-0052, DEC-0053, DEC-0054, DEC-0055, DEC-0056,
        DEC-0057, DEC-0058, DEC-0178, DEC-0179, DEC-0180, DEC-0181,
        DEC-0182, DEC-0183]
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

This is the direct attack on [BG-0001](../goals/BG-0001-groundwork.md)'s problem statement: vague,
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
  token budget, on-demand graph tools) resolved by [EP-0004](EP-0004-graph-index.md)/[EP-0007](EP-0007-consolidation-memory-layer.md).
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

**Out:** the chat UI ([EP-0006](EP-0006-refinement-web-ui.md)); gate mechanics ([EP-0003](EP-0003-governance-and-gate-engine.md)); retrieval
infrastructure ([EP-0004](EP-0004-graph-index.md), [EP-0007](EP-0007-consolidation-memory-layer.md) — this epic consumes their contracts);
commit construction ([EP-0001](EP-0001-artifact-store-and-format-engine.md) executes the typed writes).

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
  ([EP-0003](EP-0003-governance-and-gate-engine.md) absorbs — impact edge EP-0002→[EP-0003](EP-0003-governance-and-gate-engine.md)).
- **Evaluation suite contract**: benchmark corpus format, judge
  configuration, pass thresholds, drift-audit reports.

## Risks & Open Questions

- Judge-model independence for faithfulness evals — resolved: config-declared
  model-family check, enforced by the harness
  ([DEC-0178](../decisions/DEC-0178-eval-harness-judge-model-family-independence.md)),
  carried as [ST-0041](../stories/ST-0041-evaluation-harness.md) AC 1.
- Benchmark corpus bootstrap — resolved: a hand-authored seed corpus is a
  v1 acceptance criterion, not a stretch goal
  ([DEC-0179](../decisions/DEC-0179-eval-harness-seed-benchmark-corpus.md)),
  carried as [ST-0041](../stories/ST-0041-evaluation-harness.md) AC 2.
- Anchoring in synthesis — resolved: the context-recipe story owns a
  default exclusion of the shared draft's prose from fresh 1:1 context
  ([DEC-0180](../decisions/DEC-0180-context-recipe-owns-anchoring-mitigation.md)),
  carried as [ST-0038](../stories/ST-0038-context-assembly-via-pack-recipes.md) AC 3.
- Pack format expressiveness vs. simplicity — spiked as
  [SP-0008](../spikes/SP-0008-pack-format-expressiveness-vs-simplicity.md),
  3-day timebox, draft-ahead ratified with this story bundle
  ([DEC-0181](../decisions/DEC-0181-sp-0008-pack-format-expressiveness-spike.md)).

## Derived Work

- [ST-0032](../stories/ST-0032-session-engine-lifecycle-and-contract.md) — session
  engine lifecycle and contract (foundational).
- [ST-0033](../stories/ST-0033-strategy-pack-format-and-plugin-loading.md) — strategy
  pack format and plugin loading (foundational).
- [ST-0034](../stories/ST-0034-transcript-capture-and-confirmed-distillation.md) —
  transcript capture and confirmed distillation.
- [ST-0035](../stories/ST-0035-guardrails-and-authority-limits.md) — guardrails and
  authority limits.
- [ST-0036](../stories/ST-0036-conflict-detection-mediation-and-escalation.md) —
  conflict detection, mediation, and escalation.
- [ST-0037](../stories/ST-0037-incremental-synthesis-and-shared-draft.md) —
  incremental synthesis and shared draft.
- [ST-0038](../stories/ST-0038-context-assembly-via-pack-recipes.md) — context
  assembly via pack recipes.
- [ST-0039](../stories/ST-0039-change-proposal-triage.md) — Change Proposal triage.
- [ST-0040](../stories/ST-0040-glossary-maintenance-in-session.md) — glossary
  maintenance in-session.
- [ST-0041](../stories/ST-0041-evaluation-harness.md) — evaluation harness.
- [SP-0008](../spikes/SP-0008-pack-format-expressiveness-vs-simplicity.md)
  — pack format expressiveness vs. simplicity (draft-ahead, ratified with
  this bundle).
