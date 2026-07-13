---
id: EP-0014
type: epic
title: "Self-Governance & Dogfooding"
status: approved
approved-on: 2026-07-13
approved-by: awakeinagi@gmail.com
owner: awakeinagi@gmail.com
created: 2026-07-13
overview: >-
  Self-Governance & Dogfooding tracks BG-0002's outcome that every
  deployed execution surface is documented, contracted, and gated by
  the pipeline it implements (DEC-0442), merged with the dogfooding
  practice loop that discovers and validates those obligations
  (DEC-0463). Quality goals, in priority order: auditability
  (DEC-0446, DEC-0442); correctness biased toward false positives
  over false negatives (DEC-0513, DEC-0509); coverage completeness
  (DEC-0442); modifiability (DEC-0511, DEC-0484). In scope:
  definitions and policies of the governance rules — which rules
  exist, what they check, gate policy — running as check-time rule
  families on Engine Core & Artifact Model's checker machinery per
  DEC-0469 and DEC-0475, artifact-type-agnostic across whatever
  types the Engine's model defines; DEC-0442's five subsumed
  obligations; the dogfooding loop, formalized as the existing
  change-intake path with no dedicated capture machinery (DEC-0508).
  Refined this session (SES-0094): the bootstrap-circularity
  transition principle is settled — pre-change rules govern a method
  change (DEC-0504) — mechanism formalized by draft-ahead spike
  SP-0021 (DEC-0505); the EP-0015→EP-0014 impact edge closes the
  governance-configuration seam's bookkeeping gap (DEC-0506); the
  rule-family authoring contract is consumed from EP-0010,
  sequencing governance-rule stories after it — an execution risk if
  that contract shifts (DEC-0507); the governance/ files carry a
  three-way ownership split among EP-0014/EP-0015/EP-0010
  (DEC-0510); derived work splits into two independent lanes plus
  the spike, mitigating that risk (DEC-0512). Out of scope: checker
  machinery itself and other projects' use of Groundwork. Impacted
  by EP-0010 and EP-0015; impacts Observability. Open, deferred to
  story level: continuous enforcement beyond the check-time posture
  (DEC-0509). Derives from BG-0002; approved 2026-07-13.
links:
  impacts: [EP-0016]
  impacted-by: [EP-0010, EP-0015]
  derives-from: [BG-0002]
cites: [DEC-0462, DEC-0463, DEC-0469, DEC-0442, DEC-0446, DEC-0019, DEC-0263, DEC-0443, DEC-0504, DEC-0505, DEC-0506, DEC-0507, DEC-0508, DEC-0509, DEC-0510, DEC-0511, DEC-0512, DEC-0475, DEC-0484, DEC-0486, DEC-0335, DEC-0037, DEC-0154, DEC-0513]
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

Driving quality goals, in priority order: (1) auditability —
governance checks produce a record of what was evaluated, under which
rule-set version, with what result; this is the substance of the
EP-0016 consumption contract (DEC-0446, DEC-0442); (2) correctness
with an explicit bias — when uncertain, rules report rather than stay
silent, preferring false positives over false negatives (DEC-0513,
DEC-0509); (3) coverage completeness — every governed artifact type is
checked, leaving no ungoverned capability (DEC-0442); (4)
modifiability — new rules and policy changes land without Engine
changes (DEC-0511, DEC-0484).

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
  process and formats. Its mechanism is the existing intake path:
  observations from the project's own use of the paradigm enter
  change intake like any other proposal, captured as IDEA-* items
  when not acted on immediately (DEC-0508); a derived story
  formalizes this contract, and no dedicated capture machinery is
  built (DEC-0335).
- A governance variant this epic's design must preserve for
  skill-only projects: DEC-0263 established that skill-only projects
  reuse the governance-as-code files, seeded with solo-god-mode at
  bootstrap.
- Enforcement posture: governance rules run as check-time rule
  families per DEC-0475 — they report at gate prep and explicit
  check runs and never block writes (DEC-0509); whether they
  additionally run continuously (CI or pre-commit) is a story-level
  decision, deferred.
- Governance rules are artifact-type-agnostic: they run over
  whatever artifact types the Engine's model defines (DEC-0469,
  DEC-0484, DEC-0511), so gating agent or skill definitions is
  general rules applied to those types, and no direct impact edge to
  EP-0011 or EP-0013 exists.

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

The governance/ configuration files (roles.yaml, domains.yaml,
gate-policies.yaml, people.yaml) carry a three-way ownership split
(DEC-0510): their schema and format belong to EP-0015 (DEC-0443);
their committed policy content — the values the rule families
consult — belongs to this epic (DEC-0484's tunable tables); the
evaluation machinery belongs to EP-0010 (DEC-0469). The files remain
project-committed configuration the Engine reads, never
Engine-defined schema (DEC-0037's foundational placement of
governance configuration as versioned files in the canonical repo).
A related boundary sits outside these files entirely: the
role-to-review-path mapping — which roles review via OAuth versus
the program-user path — lives in deployment configuration, not the
governance/ files, since it reflects seat procurement rather than an
approval rule this epic's policy content governs (DEC-0154).
EP-0013 seeds these files at project bootstrap (DEC-0263); that is
story-level consumption of this epic's policy content, arriving via
EP-0010's compliance definition rather than through a direct
epic-level dependency (DEC-0486, DEC-0511).

## Interfaces & Contracts to Define

- The governance-rule-family contract: rule definitions, gate policy,
  and how they run on the Engine's shared checker. Provided by this
  epic — the rule definitions and gate policy — to run on EP-0010's
  Engine-hosted checker (DEC-0469); check results are consumed by
  EP-0016 for compliance verification.
- Consumed: the rule-family authoring contract — the shape,
  registration mechanism, and policy-configuration schema of a rule
  family — from EP-0010's rule-hosting component doc (DEC-0507);
  governance-rule stories sequence after that doc reaches draft
  completeness.
- The dogfooding-loop contract: how the Groundwork project's own use
  of the paradigm surfaces refinements back into the corpus. Produced
  by this project's own use of the paradigm; consumed by change
  intake, per DEC-0508.
- The Observability consumption contract for audit trails and
  gate/checker metrics that serve compliance verification (the
  EP-0014→EP-0016 impact edge: governance obligations define much of what
  observability must capture). This consumption contract is defined
  at story level once EP-0016's framework stabilizes — EP-0016's own
  noted dependency.
- The governance-configuration seam with EP-0015: this epic owns the
  evaluation of team governance configuration as rule families on the
  Engine-hosted checker (DEC-0469), while EP-0015 owns the
  governance-configuration schema itself — roles, domains,
  gate-policies, and people (DEC-0443). This seam carries the
  one-directional EP-0015→EP-0014 impact edge (DEC-0506).

## Risks & Open Questions

- Resolved at this refinement: the transition principle — a change to
  the method or its governance rules is gated by the rules accepted
  before the change, and new rules take effect only after approval
  under the old ones (DEC-0504). The mechanism (transition-window
  protocol, re-validation policy, genesis documentation, meta-tier
  placement, test plan) is formalized by SP-0021 (DEC-0505).
- Open, deferred to story level: whether governance rule families
  additionally run continuously (CI or pre-commit) beyond the
  check-time posture (DEC-0509).
- Execution risk: governance-rule stories depend on EP-0010's
  rule-family authoring contract shape stabilizing (DEC-0507); if
  that contract shifts after stories derive, rework follows.
  Mitigated by the two-lane structure (DEC-0512): the dogfooding lane
  and SP-0021 proceed regardless.

## Derived Work

SP-0021 — Bootstrap-circularity transition mechanism: drafted in this
session as draft-ahead work, ratified by this epic's approval; runs
as the next refinement target after approval, before story derivation
(DEC-0505). Stories derive after approval in two lanes (DEC-0512):
governance-rule stories, sequenced after EP-0010's rule-hosting
component doc reaches draft (DEC-0507), and dogfooding-loop stories,
unblocked — including the story formalizing the dogfooding-loop
contract (DEC-0508).

