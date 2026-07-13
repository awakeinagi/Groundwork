---
id: DEC-0443
type: decision
title: "Rechartered BG-0002's anticipated derived-work roster: thirteen epic topics"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-12
source-span: "SES-0085 T7, T9, T11"
overview: >-
  The rechartered BG-0002 lists thirteen anticipated derived-work
  topics — Engine core, Agents, Skills (two audiences), Artifact
  model, Modality parity, Adoption-greenfield, Adoption-brownfield,
  Self-governance, Export/packaging, Runtime portability,
  Collaboration and concurrency, Human browsing surface, and EP-0009
  continuing as-is. Corpus-format versioning folds under
  export/packaging or the artifact model; team governance
  configuration folds under collaboration and concurrency. The
  roster is anticipation, not derivation — each epic derives only
  through its own refinement session after the recharter gate,
  subject to the epic-slicing coupling check.
links:
  derives-from: [SES-0085]
  relates-to: [EP-0009, IDEA-0060, IDEA-0010, IDEA-0013, BG-0002]
---

# DEC-0443: Rechartered BG-0002's anticipated derived-work roster: thirteen epic topics

## Context

Round 1's charter-object answer (SES-0085 T7) asked for topic-specific epics beyond the base recharter: agents, skills for two audiences, usage with/without the app, and the artifacts the Engine operates on, plus separate greenfield/brownfield adoption epics. The facilitator consolidated an eight-item roster (T8), and round 2 (T9) added runtime portability, collaboration and concurrency, and the human browsing surface, confirmed the BG-0001/app boundary, and confirmed two adoption epics rather than one. Round 3 (T10-T11) added Engine core itself, since EP-0009 covers only the interaction surface and no topic named the Engine's own internal mechanics.

## Decision

The rechartered BG-0002 lists thirteen anticipated derived-work topics: Engine core (the paradigm mechanics themselves); Agents; Skills for two audiences (skills consumed by Groundwork-owned agents, and skills for users entering a bare agent runtime); Artifact model (the artifacts the Engine operates on, their scoping and design); Modality parity (usage with and without the Application); Adoption-greenfield and Adoption-brownfield as two separate epics; Self-governance; Export and packaging; Runtime portability; Collaboration and concurrency; the Human browsing surface; and EP-0009 (Artifact Interaction Surface) continuing as-is.

## Rationale

The roster is anticipation, not derivation: each epic derives only through its own refinement session after the recharter gate, where the epic-slicing coupling check applies.

## Alternatives Considered

Corpus-format versioning and team governance configuration were considered as standalone roster topics and folded instead: corpus-format versioning under export/packaging or the artifact model rather than standing alone, and team governance configuration under collaboration and concurrency. Adding Engine core was itself a live round-3 question ("Add Engine core (recommended yes)") rather than an assumed inclusion — the stakeholder confirmed it explicitly (T11: "Yes — list it (Recommended)").

## Implications

Each of the thirteen topics derives only through its own refinement session after the recharter gate, subject to the epic-slicing coupling check; the roster itself creates no epic and re-scopes no existing one, including EP-0009, which continues as-is.
