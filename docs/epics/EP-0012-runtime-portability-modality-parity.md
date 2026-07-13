---
id: EP-0012
type: epic
title: "Runtime Portability & Modality Parity"
status: draft
owner: awakeinagi@gmail.com
created: 2026-07-13
overview: >-
  Runtime Portability & Modality Parity tracks BG-0002's outcome
  that skill-mode functions across the major agent-chat runtimes
  with runtime-specific surface kept thin, arbitrated as a
  standalone, sponsor-trackable epic by DEC-0466. In scope: per-
  runtime translations and adapters for Claude Code, GitHub Copilot,
  Codex, OpenCode and similar (DEC-0444's runtime list), generated
  from or drift-checked against Agent & Skill Surfaces' canonical
  definitions, never hand-maintained forks; the parity contract,
  with capability gaps as documented degradation, never silent
  (precedent: DEC-0460/DEC-0461's affordance fallbacks); modality
  parity, the paradigm identical with and without the Application,
  largely reducing to every consumer consuming the same Engine
  (DEC-0423); the runtime-abstraction-cost spike as first derived
  work and fold-back trigger (DEC-0466). Out of scope: redefining
  how skills are expressed (Agent & Skill Surfaces' strict boundary)
  and the Application's own modality (BG-0001). No outgoing impact
  edges among current siblings; impacted-by Engine Core & Artifact
  Model and Agent & Skill Surfaces. Open questions, deferred to this
  epic's own refinement: reference-runtime versus equal-peers for
  the parity contract (after the runtime-survey spike), and the
  harness-affordance-gaps inventory. Derives from BG-0002; draft
  status.
links:
  impacted-by: [EP-0010, EP-0011]
  derives-from: [BG-0002]
cites: [DEC-0462, DEC-0466, DEC-0444, DEC-0441, DEC-0423, DEC-0460, DEC-0461, DEC-0433]
---

# EP-0012: Runtime Portability & Modality Parity

## Summary

BG-0002's outcome that skill-mode functions across the major
agent-chat runtimes, with runtime-specific surface kept thin, tracked
here as a sponsor-trackable body of work per DEC-0466's arbitration.

## Why (Goal Alignment)

BG-0002 requires portability across the major agent-chat runtimes and
modality parity — the paradigm identical with and without the
Application. DEC-0466 arbitrated this as its own standalone epic
rather than folded into Agent & Skill Surfaces, since translation and
parity-proof work is a distinct, ongoing, sponsor-trackable track.
This epic is one of the seven derived under BG-0002's rechartering
(per DEC-0441), which named portability among the goal's outcomes.

## Scope

**In:**
- Per-runtime translations and adapters for Claude Code, GitHub
  Copilot, Codex, OpenCode, and similar (DEC-0444's runtime list) —
  generated from or drift-checked against Agent & Skill Surfaces'
  canonical definitions, never hand-maintained forks.
- The parity contract: what "the complete paradigm works here" means,
  with capability gaps as documented degradation, never silent
  (precedent: the DEC-0460/DEC-0461 affordance fallbacks).
- Modality parity: the paradigm identical with and without the
  Application, which largely reduces to every consumer consuming the
  same Engine (DEC-0423), built on DEC-0433's SES-0082 pairing with
  DEC-0423 — skill-mode as the paradigm's core subset with parity
  tracked in a maintained parity/asymmetry matrix.
- The runtime-abstraction-cost spike as the first derived work and
  fold-back trigger (DEC-0466).

**Out:**
- Redefining how skills are expressed — Agent & Skill Surfaces owns
  canonical definitions; DEC-0466 draws this as a strict boundary.
- The Application's own modality (BG-0001).

## Domain Context

Bounded context: **Groundwork runtime portability & modality parity**
(per DEC-0462, DEC-0466). Consumes Agent & Skill Surfaces' canonical
definitions and Engine Core & Artifact Model's runtime-agnostic
substrate; has no outgoing impact edges among current siblings.

## Interfaces & Contracts to Define

- The parity contract itself: reference-runtime vs. equal-peers, and
  how documented degradation is expressed and surfaced.
- The generation-or-drift-check mechanism against the canonical
  definitions it consumes.
- The runtime-abstraction-cost spike's scope and fold-back trigger
  conditions (DEC-0466).

## Risks & Open Questions

- Reference-runtime vs. equal-peers for the parity contract — the
  stakeholder explicitly deferred this to this epic's own refinement,
  after the runtime-survey spike reports (SES-0089 T11).
- The harness-affordance-gaps inventory (notes/preview-dependent
  affordances, structured-question support, subagent support) is
  spike input for the same refinement.

## Derived Work

None yet; this epic derives stories and spikes at its own refinement
session.
