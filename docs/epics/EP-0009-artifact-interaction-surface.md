---
id: EP-0009
type: epic
title: "Artifact Interaction Surface"
status: approved
approved-on: 2026-07-12
approved-by: awakeinagi
owner: awakeinagi@gmail.com
created: 2026-07-10
overview: >-
  The single method epic governing the artifact-librarian agent and
  the artifact-interact skill as gated, contracted deliverables
  under BG-0002: two Component Docs, one per artifact (different
  consumer sets per DEC-0339), each carrying a mandatory runtime-
  policy contract section (DEC-0340) with a frontmatter-pinned model
  per DEC-0348 (no spawn-time model param mandated), plus
  guardrailed exploratory evaluation of candidate interaction-
  surface tooling whose executable spikes carry a test plan per
  DEC-0345, sized by DEC-0336. The skill's CMP consolidates the
  DEC-0310 premise that artifact-interact is the single home of all
  artifact-touching tooling; the conformance check (DEC-0341) is
  operationally constrained by DEC-0347's agent-definition startup-
  caching. Interfaces to define include the absorption-trigger
  conditions (DEC-0109/DEC-0338/DEC-0346) and a shared gate
  criterion: neither CMP gates until consumer expectations —
  currently distributed across DEC-0388, DEC-0327, DEC-0330,
  DEC-0331, DEC-0340, DEC-0342, and the SES-0076 concurrency set
  (DEC-0391, DEC-0392, DEC-0393) — are captured. Backfill of the
  already-built surface (DEC-0342's protocol, DEC-0340's SPEC
  amendment, DEC-0341's conformance check, TRIGGERS.md absorption-
  trigger arming) is in scope but its execution is deferred by
  sequencing, not superseded (DEC-0350) — the epic's first derived
  work is the exploratory spike program, which now includes SP-0018
  (the multi-session worktree write model); the spikes are safe
  under this sequencing because their outputs are throwaway
  (DEC-0351) and any adoption still routes through
  DEC-0337/DEC-0335. The epic completes in phases and gates per
  story/spike, not as a release train. Open questions carried
  through the gate: install-script contract scope (deferred a third
  time) and the defect-tracking artifact shape (travels with the
  backfill).
links:
  derives-from: [BG-0002]
  satisfies: [BG-0002]
  relates-to: [DEC-0339, IDEA-0015]
cites: [DEC-0339, DEC-0340, DEC-0341, DEC-0342, DEC-0344, DEC-0346, DEC-0325, DEC-0334, DEC-0311, DEC-0350, DEC-0351, DEC-0352, DEC-0353, DEC-0322, DEC-0324, DEC-0327, DEC-0330, DEC-0331, DEC-0335, DEC-0337, DEC-0338, DEC-0310, DEC-0345, DEC-0336, DEC-0347, DEC-0348, DEC-0109, DEC-0329, DEC-0354, DEC-0388, DEC-0389, DEC-0391, DEC-0392, DEC-0393]
---

## Summary

The single method epic governing the artifact-librarian agent and the
artifact-interact skill as gated, contracted deliverables: two
Component Docs, one per artifact — different consumer sets per
DEC-0339 (the skill answers to the librarian and DEC-0327-chartered
agents; the librarian answers to all agents for writes and synthesis
reads per DEC-0388, with targeted reads chartered directly per
DEC-0388/DEC-0389) — each carrying a mandatory runtime-policy contract
section (DEC-0340). Also scopes guardrailed exploratory evaluation of
candidate tooling for this surface (DEC-0351). Backfill of the
already-built surface is in scope but its execution is deferred
(DEC-0350); the first work this epic actually derives is the
exploratory spike program.

## Why (Goal Alignment)

BG-0002's premise: no ungoverned capability; every deployed method
execution surface is documented, contracted, and gated by the same
pipeline it implements. The artifact-librarian/artifact-interact pair
is the mandatory path for all writes and synthesis reads by any agent
touching Groundwork corpora (DEC-0388) and is currently built,
dogfooded daily, and uncontracted — the exact gap BG-0002 exists to
close, and its named first derived work (BG-0002's overview). The pair
ships as one deliverable per DEC-0334, which is why this epic hosts
two Component Docs, not two epics. Method work living in the artifact
tree (per DEC-0344) is how this obligation surfaced at all — the
status report's frontier, not a separate tracking mechanism.

## Scope

**In:**
- The two Component Docs per DEC-0339: the librarian's CMP (task
  contract, refusal semantics per DEC-0330, frontmatter-pinned model
  (DEC-0348 — the frontmatter pin is authoritative and sufficient;
  explicit spawn-time model params are no longer mandated, correcting
  DEC-0329's mandate clause), deny-by-default tool grants with
  rationale, memory policy per DEC-0331, spawn contract — per
  DEC-0340's agent-contract profile) and the artifact-interact skill's
  CMP (CLI operation semantics in SPEC lockstep, per DEC-0311). The
  skill's premise — that artifact-interact is the single home of all
  artifact-touching tooling (DEC-0310) — is what the skill CMP exists
  to consolidate.
- Runtime/capability configuration as a mandatory, gate-enforced
  contract section inside each CMP — not a separate epic (DEC-0339,
  DEC-0340).
- The DEC-0340 SPEC-component agent-profile amendment (already
  accepted; this epic is the deliverable it amends against).
- The DEC-0341 deployed-vs-contracted conformance check, operationally
  constrained by DEC-0347: agent definition files are read once at
  Claude Code startup and cached, so a conformance change to an agent
  definition requires a restart before the check can observe it as
  deployed.
- Arming the absorption-clause triggers in docs/TRIGGERS.md (per
  DEC-0338/DEC-0346) — currently unmet: no armed trigger exists yet
  for this surface, an open BG-0002 obligation surfaced this session.
- Guardrailed exploratory spikes evaluating candidate interaction-
  surface tooling (DEC-0351): spike outputs are throwaway and never
  deployed as part of the surface; adoption of anything a spike
  surfaces happens only through a DEC-0337 option survey followed by
  DEC-0335 design intake. Any executable spike artifact's design
  includes a test plan (DEC-0345), sized by DEC-0336's yardstick.
- The backfill of the already-built surface (DEC-0342's protocol
  (sequencing revised by DEC-0350), above) — in scope, execution
  deferred per DEC-0350.

**Out:**
- Distribution/packaging (install.sh, the IDEA-0010 plugin) — derives
  only at IDEA-0010's own take-up, per DEC-0339. Whether install.sh is
  contracted *within this epic* is a deliberately deferred open
  question (DEC-0352), not a scope-out call made here.
- Product features — BG-0001's tree, not this method-track epic.
- Re-deciding ratified architecture (DEC-0339, DEC-0340, DEC-0341,
  DEC-0342 stand as accepted).
- DEC-0322's eval-loop territory — explicitly excluded per DEC-0342.

## Domain Context

Bounded context: **Method track**. Term "Artifact Interaction
Surface" (the mandatory delegation surface — artifact-librarian agent
plus artifact-interact skill — through which all agents interact with
Groundwork corpora, per DEC-0324/DEC-0388, superseding DEC-0325) is
not yet glossary-resolved in CONTEXT.md; adding it is carried as
backfill-adjacent follow-up, not performed by this epic record itself.

## Interfaces & Contracts to Define

- The librarian CMP's task contract (input/output shape, refusal
  reporting per DEC-0330, verbatim mode).
- The artifact-interact CMP's CLI operation contract, kept in SPEC
  lockstep (DEC-0311).
- The runtime-policy profile sections in each CMP (DEC-0340): every
  config field and value, deny-by-default tool surface with
  rationale, model pin, memory policy, refusal semantics, spawn
  contract, concurrency obligations, breaking-change list.
- The conformance-check contract (DEC-0341): deployed-vs-contracted
  diff shape and violation reporting.
- The absorption-trigger condition(s) for the librarian and skill
  implementations: condition language and subscriber list per
  SPEC-triggers/DEC-0109, with firing semantics per DEC-0338/DEC-0346
  — a fired trigger retires the implementation only, never the
  method-track pattern it instantiates.

All of the above are deferred to the backfill fold-in Idea's take-up
(DEC-0350) — this epic charters them, it does not draft them.

Gate criterion: neither CMP gates until its consumers' expectations
are captured. Consumer expectations for this surface are today
distributed across DEC-0388, DEC-0327, DEC-0330, DEC-0331, DEC-0340,
DEC-0342, and the SES-0076 concurrency set (DEC-0391, DEC-0392,
DEC-0393); the CMPs consolidate them rather than introduce new ones.

## Risks & Open Questions

- Install-script contract scope: deliberately deferred a third time,
  carried as an explicit open question through this gate, to be
  settled at the backfill fold-in Idea's take-up (DEC-0352).
- Defect-artifact shape (stakeholder sketch: severity plus a multi-
  state status workflow) travels with the backfill rather than being
  designed now — its sole named consumer is DEC-0342's fix-via-defect
  disposition path (DEC-0353).
- docs/TRIGGERS.md carries no armed absorption trigger for this
  surface yet — an unmet BG-0002 obligation until the backfill arms
  one.
- Spike work under this epic brushes against BG-0002's admission
  predicate (can runtime diverge from the record unedited?) —
  mitigated by DEC-0351's throwaway-output guardrail.
- Safety argument for contract-later sequencing: the spikes leave the
  surface unchanged — their outputs are throwaway per DEC-0351 — and
  evaluate a NEW capability whose data source is the corpus, not the
  surface's own contract. Adoption of anything a spike surfaces
  requires the DEC-0337 option survey followed by DEC-0335 design
  intake, so no uncontracted change can reach the surface through
  this epic's exploratory track.

## Derived Work

The activegraph exploratory spike program (DEC-0354): SP-0013
(projection), SP-0014 (structural rule precision, impacted-by
SP-0013), SP-0015 (prose-to-rule compilation fidelity, independent),
SP-0016 (reactive hook-loop economics, impacted-by SP-0014), SP-0017
(fork-and-diff design-debate evidence, impacted-by SP-0014, queued
last), and SP-0018 (multi-session worktree write model: merge-time ID
allocation and serialized merges, the worktree-scale counterpart under
this same epic).

Pending:
- Backfill stories and both CMPs — created at the fold-in Idea's
  take-up (DEC-0350).

The epic completes in phases: first the exploratory spike program
(SP-0013..SP-0018 above), then the backfill at IDEA-0024's take-up.
Each story or spike gates individually — the epic itself is a scope
container, not a release train, and does not gate as a single unit of
completion.

