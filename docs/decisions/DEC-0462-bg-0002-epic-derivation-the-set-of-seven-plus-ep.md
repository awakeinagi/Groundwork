---
id: DEC-0462
type: decision
title: "BG-0002 epic derivation: the set of seven plus EP-0009"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0089 @ T4, T13"
overview: >-
  SES-0089 ran BG-0002's epic derivation via dual-instance system-
  architect consultation. This decision records the resulting set:
  seven new epics (Engine Core & Artifact Model; Agent & Skill
  Surfaces; Runtime Portability & Modality Parity; Adoption; Self-
  Governance & Dogfooding; Collaboration, Concurrency & Browsing;
  Observability) plus EP-0009 continuing as the eighth sibling. It
  compresses BG-0002's fifteen DEC-0443/DEC-0446 anticipated topics
  along real bounded-context seams rather than deriving one epic per
  topic. Names are working titles; real IDs are allocated at each
  epic's own creation. The decision is the anchor for nine sibling
  derivation decisions made in the same session (merges, placements,
  and boundary calls).
links:
  derives-from: [SES-0089]
  relates-to: [DEC-0443, DEC-0446, DEC-0463, DEC-0464, DEC-0465, DEC-0466, DEC-0467, DEC-0468]
---

# DEC-0462: BG-0002 epic derivation — the set of seven plus EP-0009

## Context

BG-0002's recharter (DEC-0441) carried fifteen anticipated derived-work
topics (DEC-0443, DEC-0446), explicitly anticipation rather than
derivation. SES-0089 ran the derivation with the required dual-instance
system-architect consultation.

## Decision

BG-0002 derives seven epics — Engine Core & Artifact Model; Agent &
Skill Surfaces; Runtime Portability & Modality Parity; Adoption;
Self-Governance & Dogfooding; Collaboration, Concurrency & Browsing;
Observability — with EP-0009 (Artifact Lifecycle & Interaction)
continuing as the eighth member of the sibling set. Names are working
titles; IDs are allocated at creation.

## Rationale

The fifteen topics compress along real bounded-context seams; both
consultation instances converged on this shape after two rebuttal
rounds, and over-fragmentation adds gate overhead without unlocking
parallelism for a solo operator.

## Alternatives Considered

Fifteen one-topic epics (gate rent without parallelism); a six-epic
variant folding portability into the skills epic (rejected by
stakeholder arbitration — see the portability decision); a four-epic
minimal variant folding browsing and observability into Engine Core
(loses real boundaries).

## Implications

Each epic refines through its own session in impact order, Engine Core
first. BG-0002's Derived Work section lists all eight members.
