---
id: ST-0033
type: story
title: Strategy pack format and plugin loading
status: approved
owner: ds-lead
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
created: 2026-07-08
links:
  derives-from: [EP-0002]
  satisfies: [BG-0001]
  depends-on: []
  impacts: [ST-0035, ST-0038, ST-0040, ST-0041]
  impacted-by: []
cites: [DEC-0053, DEC-0181]
---

# ST-0033: Strategy Pack Format and Plugin Loading

## Summary

The versioned, plugin-like bundle format that defines how the agent
conducts one kind of session — prompts, skills, tools, policies, and
context recipe, per artifact type and phase. Every downstream in-session
capability (guardrails, context assembly, glossary maintenance, and the
eval harness that gates changes to any of it) is pack-defined and reads
this format.

## Acceptance Criteria

1. The bundle layout and `pack.yaml` schema cover phases, stopping
   criteria, escalation triggers, guardrail policy, and a context recipe
   declaration, one pack per artifact-type-and-phase (goal-refinement,
   epic-refinement, story-refinement, conflict-mediation, CP-triage)
   (per [DEC-0053](../decisions/DEC-0053-strategy-packs-as-plugins.md)).
2. Packs are stored in the canonical repo and PR-gated like governance
   config — a pack change cannot land without passing the eval harness's
   benchmark suite
   (per [DEC-0053](../decisions/DEC-0053-strategy-packs-as-plugins.md),
   [DEC-0058](../decisions/DEC-0058-evaluation-harness.md)).
3. The pack core is model-agnostic; the underlying LLM is swappable
   through a defined model-adapter boundary while pack behavior is
   maintained
   (per [DEC-0053](../decisions/DEC-0053-strategy-packs-as-plugins.md)).
4. Every session records which pack version and which model conducted
   it, in the session's frontmatter
   (per [DEC-0053](../decisions/DEC-0053-strategy-packs-as-plugins.md)).
5. Skill and tool declarations within a pack resolve to a closed,
   documented set of loadable capabilities — a pack cannot declare an
   undeclared or arbitrary code capability.

## Component Impact

None yet — a Component Doc for this epic's bounded context is stubbed once the first story here refines toward it.

## Out of Scope

The specific policy content of any one pack (guardrail rules, context
recipe values) — those are per-pack configuration, not this story's
schema; whether the schema is declarative-only or needs a scripting
escape hatch is not yet settled
(pending [SP-0008](../spikes/SP-0008-pack-format-expressiveness-vs-simplicity.md),
per [DEC-0181](../decisions/DEC-0181-sp-0008-pack-format-expressiveness-spike.md)).

## Notes for Implementers

Do not treat this story's schema as final before
[SP-0008](../spikes/SP-0008-pack-format-expressiveness-vs-simplicity.md)'s
findings land — if declarative fields can't express real pack
variation, the schema (not just individual packs) may need a scripting
or templating layer.
