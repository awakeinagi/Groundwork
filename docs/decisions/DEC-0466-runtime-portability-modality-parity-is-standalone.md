---
id: DEC-0466
type: decision
title: "Runtime Portability & Modality Parity is standalone, with a strict consumer boundary"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0089 @ T7, T8, T9, T11, T12, T13"
overview: >-
  The system-architect consultation's one documented disagreement —
  folding runtime portability into Agent & Skill Surfaces versus
  standing it alone — was arbitrated by the stakeholder, who needs
  sponsor-level tracking of support for different agent-chat
  interfaces (Claude Code, GitHub Copilot, Codex, OpenCode, and
  similar non-app runtimes). This decision makes Runtime Portability
  & Modality Parity a standalone epic under a strict boundary: it
  consumes canonical agent/skill definitions from Agent & Skill
  Surfaces and owns only translations, adapters, the parity
  contract, and the modality-parity proof — it never redefines skill
  expression. A runtime-abstraction-cost spike is its first derived
  work and doubles as a fold-back trigger if adapters prove
  trivially thin. A permanent one-way impacts edge runs from Agent &
  Skill Surfaces into this epic; parity gaps are documented
  degradation, following the DEC-0460/DEC-0461 precedent, never
  silent.
links:
  derives-from: [SES-0089]
  relates-to: [DEC-0444, DEC-0441, DEC-0462]
---

# DEC-0466: Runtime Portability & Modality Parity is standalone, with a strict consumer boundary

## Context

The consultation's one documented disagreement — portability standalone
versus folded into Agent & Skill Surfaces as a quality attribute — was
arbitrated by the stakeholder, who stated the need for an epic to track
support for the different agent-chat interfaces (non-app use): Claude
Code, GitHub Copilot, Codex, OpenCode, and similar.

## Decision

Runtime Portability & Modality Parity is a standalone epic with a
strict boundary: it consumes the canonical agent and skill definitions
owned by Agent & Skill Surfaces and owns the runtime translations and
adapters, the parity contract, and the modality-parity proof; it never
redefines how skills are expressed. Its first derived work is the
runtime-abstraction-cost spike, which doubles as the fold-back trigger:
if the spike shows the adapters are trivially thin, the epic merges
back into Agent & Skill Surfaces.

## Rationale

BG-0002 outcome 5 is a distinct success criterion with an external
change driver (runtime API churn) and its own delivery rhythm — adding
support for a runtime is a trackable body of work — and the stakeholder
requires sponsor-level visibility of it. Translating a Claude Code
agent config to another harness's format is this epic's chartered
work; single-sourcing (outcome 1) requires translations be generated
from or drift-checked against the canonical definitions, never
hand-maintained forks.

## Alternatives Considered

Folding into Agent & Skill Surfaces with the spike as a split trigger
(the facilitator's initial recommendation; declined by the stakeholder
for the tracking need and distinct rhythm); an equal-peers
lowest-common-denominator parity design (the reference-runtime-versus-
equal-peers question is explicitly deferred to the epic's refinement,
after the spike reports).

## Implications

A permanent one-way impacts edge runs from Agent & Skill Surfaces to
this epic. Parity gaps are documented degradation, never silent —
precedent: the DEC-0460/DEC-0461 affordance fallbacks.
