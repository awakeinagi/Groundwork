---
id: DEC-0190
type: decision
title: Business Goals gain a required System Context section (C4 Level 1/2 inspired)
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0035 @ T11-T12"
links:
  derives-from: [SES-0035]
  relates-to: [DEC-0189, DEC-0192, DEC-0194]
  supersedes: []
---

# DEC-0190: Business Goals Gain a Required "System Context" Section

## Context

DEC-0001 (goal-level, physical form
factor) named three deliverables — web UI, backend services, connector
integrations — but only two got their own epic. "Backend services" was
silently absorbed into the union of the domain epics derived from
SES-0001's synthesis. No
Business Goal section forced an explicit, complete boundary-level
description of what's being built.

## Decision

The Business Goal template gains a required **System Context** section,
positioned after Intent: what's being built (1-2 sentences, boundary
only), who uses it and how, where it lives, the trigger/output contract,
existing-vs-new for the system's own parts, existing systems needing
change, and external dependencies. Boundary-only by design — no internal
architecture, preserving (not violating) the "no solution language in
goals" rule. The full question set lives in
`references/goal-grilling-questions.md`.

## Rationale

This is the C4 model's Level 1 (System Context) and Level 2 (Container)
framing, cross-referenced against arc42's "System Scope and Context"
template section. C4 Level 2 specifically asks "what are the
separately-deployable/runnable units" — the question that would have
surfaced a backend/API container independent of the domain engines had it
been asked at BG-0001's inception. The section's answers directly feed the
epic-derivation deliverable-coverage pass
(DEC-0194).

## Alternatives Considered

- **Rely on epic derivation alone to catch gaps**, leaving physical
  form-factor decisions like DEC-0001
  as the only goal-level boundary statement: rejected — epic derivation
  happens after the goal is already
  gated and approved, too late to change the goal's own framing.
  Structured boundary-capture at goal time is cheaper and catches gaps
  before commitment.

## Implications

Feeds the mandatory Context Diagram at goal gate
(DEC-0192).
BG-0001 is backfilled with this section.
