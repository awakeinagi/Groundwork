---
id: DEC-0455
type: decision
title: "Boundary rules for RSCH"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0086"
overview: >-
  The boundary with Spikes is the direction of derivation: a Spike
  answers a question the design tree already asked and derives from
  an Epic, while a Research artifact is free-standing investigation
  that can spawn new design-tree work; an epic-scoped question
  raised by research becomes a Spike deriving from that epic and
  citing the RSCH. The boundary with Ideas is analytical state: an
  Idea is raw pre-classification capture, while a Research artifact
  is post-investigation, analyzed evidence with derived-work
  tracking. Direction of derivation is an objective, checkable
  distinction that composes cleanly with SPEC-spike's existing
  definition.
links:
  derives-from: [SES-0086]
  relates-to: [DEC-0259]
---

# DEC-0455: Boundary rules for RSCH

## Context

At T4 the facilitator identified RSCH-versus-Spike and RSCH-versus-Idea as the two boundaries doing most of the design work. Grilling round 1 (T5) asked about the Spike boundary; the stakeholder (T6) chose the direction-of-derivation boundary as recommended.

## Decision

The boundary with Spikes is the direction of derivation: a Spike answers a question the design tree already asked and derives from an Epic, while a Research artifact is free-standing investigation that can spawn new design-tree work; an epic-scoped question raised by research becomes a Spike deriving from that epic and citing the RSCH. The boundary with Ideas is analytical state: an Idea is raw pre-classification capture, while a Research artifact is post-investigation, analyzed evidence with derived-work tracking.

## Rationale

Direction of derivation is an objective, checkable distinction (what does the artifact derive from) rather than a subjective one (how deep is the investigation), and it composes cleanly with SPEC-spike's existing definition of a Spike as deriving from an Epic. The analytical-state boundary with Ideas mirrors DEC-0259's own framing of what an Idea is not.

## Alternatives Considered

A depth-or-rigor-based boundary with Spikes (e.g. "RSCH is deeper investigation") was rejected as unmeasurable and likely to blur in practice.

## Implications

The checker's boundary/classification guidance (where it exists for Idea-versus-other-types today) extends to cover RSCH-versus-Spike using the derives-from direction as the test.
