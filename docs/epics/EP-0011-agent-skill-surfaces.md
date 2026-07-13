---
id: EP-0011
type: epic
title: "Agent & Skill Surfaces"
status: draft
owner: awakeinagi@gmail.com
created: 2026-07-13
overview: >-
  Agent & Skill Surfaces owns BG-0002's outcome that an agent-chat
  runtime plus the Groundwork skills delivers the complete core
  paradigm (DEC-0444, DEC-0433), and holds the canonical, single-
  source form of every agent definition and skill (DEC-0462). In
  scope: agent definitions and their contracts; skills for both
  audiences, agent-consumed and bare-user-facing (DEC-0443's dual-
  audience topic); the canonical single-source form of every
  definition; orchestration-level delivery of the refinement-session
  protocol. Out of scope: runtime translations, adapters, and cross-
  runtime parity proof, which belong to Runtime Portability &
  Modality Parity per DEC-0466's strict consumer boundary; Engine
  mechanics, owned by Engine Core & Artifact Model; EP-0009's own
  contracted deliverables (the artifact-librarian agent and
  artifact-interact skill). This epic impacts Runtime Portability &
  Modality Parity (canonical definitions shape every translation)
  and Adoption (adopters install and use these skills; adoption
  bootstraps this surface). Open risk: which interview-flow and UX
  rules remain skill-convention versus graduate to Engine
  enforcement, a boundary shared with Engine Core & Artifact Model.
  Derives from BG-0002; draft status pending its own refinement
  session.
links:
  impacts: [EP-0012, EP-0013]
  impacted-by: [EP-0010, EP-0009]
  derives-from: [BG-0002]
cites: [DEC-0462, DEC-0466, DEC-0444, DEC-0433, DEC-0421, DEC-0443, DEC-0340]
---

# EP-0011: Agent & Skill Surfaces

## Summary

BG-0002's outcome that an agent-chat runtime plus the Groundwork
skills delivers the complete core paradigm (DEC-0444, DEC-0433). This
epic owns the canonical agent definitions and skills as the delivery
surface for that outcome (per DEC-0462).

## Why (Goal Alignment)

BG-0002 requires skill-mode to be first-class and permanent, with no
Application required (DEC-0421, DEC-0433, DEC-0444). This epic is
where that promise is kept concrete: the agent definitions and skills
themselves, authored once, canonically, and consumed everywhere.

## Scope

**In:**
- Agent definitions and their contracts, following the gate-enforced
  agent-contract profile DEC-0340 established as precedent (tool
  grants with rationale, model pin, memory policy, refusal semantics,
  spawn contract).
- Skills for both audiences — agent-consumed and bare-user-facing
  (DEC-0443's dual-audience topic).
- The canonical, single-source form of every definition (BG-0002
  outcome 1).
- Orchestration-level delivery of the refinement-session protocol.

**Out:**
- Runtime translations, adapters, and parity proof — the sibling
  epic's domain, per DEC-0466 (the EP-0011→EP-0012 impact edge: canonical
  definitions shape every translation, and DEC-0466's boundary means
  this epic never proves cross-runtime equivalence).
- Engine mechanics — EP-0011's (Engine Core & Artifact Model) domain.
- EP-0009's contracted deliverables — the artifact-librarian agent
  and the artifact-interact skill remain EP-0009's.

## Domain Context

Bounded context: **Groundwork agent & skill delivery surface** (per
DEC-0462, DEC-0444, DEC-0433). Consumes the Engine API defined by
Engine Core & Artifact Model; is itself consumed by Runtime
Portability & Modality Parity's translations and by Adoption's
onboarding flows.

## Interfaces & Contracts to Define

- The agent-definition contract: frontmatter, tool grants, model pin,
  memory policy, spawn contract.
- The dual-audience skill contract — what an agent-consumed skill and
  a bare-user-facing skill each must provide.
- The canonical-definition contract that Runtime Portability consumes
  or drift-checks against (the EP-0011→EP-0012 impact edge).
- The adoption-facing install/onboarding contract for these surfaces
  (the EP-0011→EP-0013 impact edge: adopters install and use these skills;
  adoption flows bootstrap this surface).

## Risks & Open Questions

- Which interview-flow and UX rules remain skill-convention versus
  graduate to Engine enforcement — a boundary question shared with
  Engine Core & Artifact Model's rule-line item, to be settled in
  coordination at refinement.

## Derived Work

None yet; this epic derives stories and spikes at its own refinement
session.
