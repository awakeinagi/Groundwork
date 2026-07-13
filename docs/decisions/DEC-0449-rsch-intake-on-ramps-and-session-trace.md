---
id: DEC-0449
type: decision
title: "RSCH intake on-ramps and session trace"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0086"
overview: >-
  A Research artifact enters the corpus through one of three on-
  ramps: a dedicated quick intake session, take-up of a captured
  IDEA, or a parked tangent from any running session. The artifact
  carries derives-from pointing at its intake session, and that
  session must record the inspiration context — what inspired the
  investigation and why. Post-hoc entries derive from the session
  that records the findings review and reconstructs the inspiration
  context. This mirrors DEC-0258's existing idea-intake provenance
  pattern, keeping every RSCH traceable to the moment and reason it
  was commissioned.
links:
  derives-from: [SES-0086]
  relates-to: [DEC-0258, DEC-0261]
---

# DEC-0449: RSCH intake on-ramps and session trace

## Context

Grilling round 1 (T5) asked how the trigger enters the corpus. At T6 the stakeholder confirmed all three proposed on-ramps and asked to grill the dedicated-session workflow; at T10 the stakeholder confirmed derives-from as the session trace.

## Decision

A Research artifact enters the corpus through one of three on-ramps: a dedicated quick intake session, take-up of a captured IDEA, or a parked tangent from any running session. The artifact carries derives-from pointing at its intake session, and that session must record the inspiration context — what inspired the investigation and why. Post-hoc entries derive from the session that records the findings review and reconstructs the inspiration context.

## Rationale

Matching the existing DEC-0258 idea-intake pattern keeps provenance uniform across artifact types: every RSCH traces to the session that explains why it exists, whether that session is a purpose-built intake or a captured moment inside other work.

## Alternatives Considered

Requiring every RSCH to originate from its own dedicated session was rejected as too heavyweight for tangential or IDEA-sourced investigations.

## Implications

The checker's session-produced-artifact rules (DEC-0250-style body-mention and relates-to checks) extend to RSCH the same way they already apply to Decisions and Ideas.
