---
id: BG-0002
type: business-goal
title: Groundwork Core Technology — Engine & Delivery of the Paradigm
status: approved
approved-on: 2026-07-12
approved-by: awakeinagi
owner: awakeinagi@gmail.com
created: 2026-07-09
overview: >-
  BG-0002 tracks the Groundwork Engine as the core technology and
  full delivery of the paradigm around it — skill-mode first-class,
  adoptable, portable, exportable, self-governing — rechartered
  because the Application is mostly a presentation layer atop the
  Engine (per DEC-0423) and the prior charter had drifted three
  times without naming what the track actually is (per IDEA-0058,
  DEC-0441). The Application's UI remains BG-0001's object; its own
  reframing toward a presentation-and-team layer is a separate
  future step (per DEC-0441, IDEA-0058). Outcomes: single-sourced
  paradigm mechanics, no surface reimplementing paradigm logic;
  skill-mode first-class and permanent, no Application required (per
  DEC-0421, DEC-0433, DEC-0444); adoptable by greenfield and
  brownfield projects; self-governing — every deployed execution
  surface documented, contracted, and gated, condensing DEC-0338's
  prior five outcomes (per DEC-0442); portable across the major
  agent-chat runtimes; deliverable/exportable to third parties (per
  DEC-0441). Scope in: the Engine's mechanics and paradigm delivery
  without the Application. Out: the Application itself, re-deciding
  ratified architecture, and BG-0001's reframing. Constraints: no-
  arbitrary-builds, contract-grounded documentation, right-sized
  research, test plans in presented designs, the librarian write
  path, and DEC-0423's single-sourcing/extraction-trigger constraint
  (per DEC-0335, DEC-0336, DEC-0337, DEC-0345, DEC-0388). Solo
  governance (per DEC-0263). Derived work: EP-0009 continues; seven
  further epics (Engine Core & Artifact Model, Agent & Skill
  Surfaces, Runtime Portability & Modality Parity, Adoption, Self-
  Governance & Dogfooding, Collaboration/Concurrency/Browsing,
  Observability) derived at SES-0089 per DEC-0462; Export/Packaging
  remains anticipated and underived, triggered by the first third-
  party consumer (per DEC-0467). Status: approved.
links:
  relates-to: [SES-0059, BG-0001, DEC-0346, DEC-0441, DEC-0442, DEC-0443, DEC-0444]
cites: [DEC-0335, DEC-0336, DEC-0337, DEC-0338, DEC-0340, DEC-0341, DEC-0344, DEC-0345, DEC-0263, DEC-0388, DEC-0421, DEC-0422, DEC-0423, DEC-0433, DEC-0446, DEC-0445, DEC-0462, DEC-0467]
---

# BG-0002: Groundwork Core Technology — Engine & Delivery of the Paradigm

## Problem

The dogfooding exercise proved the value of the paradigm lives in agents and skills working with the methodology — and that the application-first framing jumped the gun: the Application is mostly a presentation layer around the Groundwork Engine (per DEC-0423). This goal's charter had drifted three times away from its original framing — sacrificial method-tooling governance (per DEC-0338), pattern permanence (per DEC-0346), permanent skill-mode delivery (per DEC-0421, DEC-0422) — until the charter no longer named what the track actually is: the home of the core technology (per IDEA-0058, DEC-0441).

## Intent

BG-0002 tracks the development and refinement of the Groundwork Engine itself as the core technology, and full delivery of the paradigm around it: skill-mode first-class, adoptable by new and pre-existing projects, portable across agent runtimes, exportable to third parties, and governed by its own pipeline (per DEC-0441). The Application's UI has merit but is a layer atop the Engine, owned by BG-0001, whose own reframing is a separate future step (per DEC-0441, IDEA-0058). Stated as intent only — how any of it is achieved belongs to the derived layers.

## Outcomes & Success Criteria

1. Single-sourced paradigm — all paradigm mechanics exist in exactly one Groundwork Engine; no surface reimplements paradigm logic (per DEC-0423, DEC-0441).
2. Skill-mode first-class and permanent — an agent-chat runtime plus the Groundwork skills delivers the complete core paradigm, no Application required (per DEC-0421, DEC-0433, DEC-0444).
3. Adoptable — greenfield bootstrap and brownfield fold-in of pre-existing projects both produce compliant, checker-passing corpora (per DEC-0441, DEC-0443).
4. Self-governing — every deployed execution surface is documented, contracted, and gated by the pipeline it implements: gated contracts citing decisions, no ungoverned capability (mechanically checked), human gates before deployment, nothing ratified invisibly unbuilt, no build without intake (per DEC-0442, condensing the prior charter's five outcomes; underlying DEC-0335, DEC-0340, DEC-0341, DEC-0344, DEC-0345).
5. Portable — skill-mode functions across the major agent-chat runtimes with runtime-specific surface kept thin (per DEC-0441).
6. Deliverable to others — the paradigm can be packaged and exported for third-party adoption (per DEC-0441).

## Scope

**In:** The Engine's mechanics and everything that delivers the paradigm without the Application (per DEC-0441).

**Out (non-goals):** The Application itself — UI, team-facing features, hosting, native reimplementations (BG-0001's object, per DEC-0441); re-deciding ratified architecture (DEC-0423's single-sourcing and extraction trigger are constraints here, not open questions); BG-0001's reframing (separate future step, per DEC-0441).

## Constraints

- No-arbitrary-builds (per DEC-0335).
- Grounding through contracts (per DEC-0336).
- Research sized to the decision (per DEC-0337).
- Test plans inside presented designs (per DEC-0345).
- Librarian write path with chartered direct reads (per DEC-0388).
- Library extraction only at the first non-CLI consumer (per DEC-0423).

## Stakeholders & Roles

Solo governance (per DEC-0263): the operator holds sponsor, approver, and arbiter roles.

## Conflicts & Tensions

- Two descriptions of artifact handling coexist until an implementation is natively rebuilt (per DEC-0346, DEC-0422).
- The goal is deliberately broad — the pressure valve is that the derived-work roster is anticipated, not chartered, and each epic gates on its own merits (per DEC-0443).
- The human browsing surface sits near the BG-0001 presentation line — kept here because it serves skill-mode users without the app (per DEC-0443).

## Derived Work

- EP-0009 (Artifact Lifecycle & Interaction, renamed per DEC-0445)
  continues under the rechartered goal.
- Seven epics derived at SES-0089's epic derivation, condensing the
  fifteen anticipated topics named at DEC-0443/DEC-0446 along real
  bounded-context seams (per DEC-0462): EP-0010 (Engine Core &
  Artifact Model — the single-sourced paradigm mechanics and static
  artifact model); EP-0011 (Agent & Skill Surfaces — the canonical
  agent definitions and skills delivering the paradigm); EP-0012
  (Runtime Portability & Modality Parity — cross-runtime translations
  and the paradigm's parity contract); EP-0013 (Adoption — greenfield
  bootstrap and brownfield fold-in as one epic); EP-0014
  (Self-Governance & Dogfooding — the governance-rule obligations
  merged with the dogfooding practice loop); EP-0015 (Collaboration,
  Concurrency & Browsing — the multi-actor concurrency model and the
  human browsing surface); EP-0016 (Observability — the audit-trail,
  telemetry, checker-metrics, and session-analytics framework).
- Remaining anticipated: Export/Packaging stays an anticipated topic,
  underived, its trigger being the first third-party consumer (per
  DEC-0467).

