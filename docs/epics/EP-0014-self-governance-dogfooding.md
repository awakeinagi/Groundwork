---
id: EP-0014
type: epic
title: "Self-Governance & Dogfooding"
status: draft
owner: awakeinagi@gmail.com
created: 2026-07-13
overview: >-
  Self-Governance & Dogfooding tracks BG-0002's outcome that every
  deployed execution surface is documented, contracted, and gated by
  the pipeline it implements (DEC-0442), merged with the dogfooding
  practice loop that discovers and validates those obligations
  (DEC-0463). In scope: definitions and policies of the governance
  rules — which rules exist, what they check, gate policy — running
  as rule families on Engine Core & Artifact Model's checker
  machinery per DEC-0469; DEC-0442's five subsumed obligations
  (gated contracts citing decisions; no ungoverned capability,
  mechanically checked; human gates before deployment; nothing
  ratified invisibly unbuilt; no build without intake); the
  dogfooding loop, the Groundwork project's own use of the paradigm
  to develop the Engine, surfacing refinements. Out of scope: the
  checker machinery itself (Engine Core & Artifact Model's domain)
  and other projects' use of Groundwork (Adoption's domain, per
  DEC-0463's distinction from DEC-0446). This epic impacts
  Observability: governance obligations define much of what
  observability must capture, including audit trails and
  gate/checker metrics serving compliance verification. Open risk:
  the bootstrap-circularity transition rule needs formalizing at
  this epic's refinement. Derives from BG-0002; draft status.
links:
  impacts: [EP-0016]
  impacted-by: [EP-0010]
  derives-from: [BG-0002]
cites: [DEC-0462, DEC-0463, DEC-0469, DEC-0442, DEC-0446, DEC-0019, DEC-0263, DEC-0443]
---

# EP-0014: Self-Governance & Dogfooding

## Summary

BG-0002's outcome that every deployed execution surface is
documented, contracted, and gated by the pipeline it implements
(DEC-0442), merged with the dogfooding practice loop that discovers
and validates those obligations (DEC-0463).

## Why (Goal Alignment)

BG-0002 condenses five prior outcomes into one self-governance
obligation (DEC-0442): no ungoverned capability, mechanically
checked; human gates before deployment; nothing ratified invisibly
unbuilt; no build without intake; gated contracts citing decisions.
DEC-0463 merged the dogfooding practice loop into this same epic since
dogfooding is how the Groundwork project discovers whether those
obligations actually hold.

## Scope

**In:**
- Definitions and policies of the governance rules — which rules
  exist, what they check, gate policy — running as rule families on
  Engine Core & Artifact Model's checker machinery, per DEC-0469 (the
  EP-0010→EP-0014 impact edge landing here).
- The five subsumed obligations of DEC-0442: gated contracts citing
  decisions; no ungoverned capability, mechanically checked; human
  gates before deployment; nothing ratified invisibly unbuilt; no
  build without intake.
- The dogfooding loop — the Groundwork project's own use of the
  paradigm to develop the Engine, surfacing refinements, founded on
  DEC-0019's precedent that Groundwork is specified using its own
  process and formats.
- A governance variant this epic's design must preserve for
  skill-only projects: DEC-0263 established that skill-only projects
  reuse the governance-as-code files, seeded with solo-god-mode at
  bootstrap.

**Out:**
- The checker machinery itself — Engine Core & Artifact Model's
  domain, per DEC-0469.
- Other projects' use of Groundwork — Adoption's domain, per
  DEC-0463's distinction from DEC-0446.

## Domain Context

Bounded context: **Groundwork self-governance & dogfooding** (per
DEC-0462, DEC-0463, DEC-0442). Consumes the checker machinery Engine
Core & Artifact Model hosts; feeds Observability's compliance-
verification consumer.

## Interfaces & Contracts to Define

- The governance-rule-family contract: rule definitions, gate policy,
  and how they run on the Engine's shared checker.
- The dogfooding-loop contract: how the Groundwork project's own use
  of the paradigm surfaces refinements back into the corpus.
- The Observability consumption contract for audit trails and
  gate/checker metrics that serve compliance verification (the
  EP-0014→EP-0016 impact edge: governance obligations define much of what
  observability must capture).
- The governance-configuration seam with EP-0015: this epic owns the
  evaluation of team governance configuration as rule families on the
  Engine-hosted checker (DEC-0469), while EP-0015 owns the
  governance-configuration schema itself — roles, domains,
  gate-policies, and people (DEC-0443).

## Risks & Open Questions

- The bootstrap-circularity transition rule — when a method change
  alters how the method documents itself, the old method governs
  until the new one is approved under it — needs formalizing at this
  epic's refinement.

## Derived Work

None yet; this epic derives stories and spikes at its own refinement
session.
