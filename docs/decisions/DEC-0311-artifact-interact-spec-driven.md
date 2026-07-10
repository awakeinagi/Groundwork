---
id: DEC-0311
type: decision
title: artifact-interact is Groundwork-specific and SPEC-driven
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0057 @ T6-T7"
overview: >-
  The artifact-interact skill is Groundwork-specific: its API is
  defined by and validated against the corpus SPEC documents
  (docs/specs/SPEC-*.md) — the skill is the executable form of the
  SPECs. No generic structured-markdown engine, no profile/schema
  layer for other artifact systems. Chosen over a "generic core +
  Groundwork profile" design to keep guardrails tight and avoid
  speculative generality; a generic engine would weaken the
  guarantees (looser validation) while enlarging the design surface.
  Consequence: SPEC changes and skill behavior must stay in lockstep
  — a SPEC amendment implies a skill update, and the skill's
  validation rules cite the SPECs as their normative basis.
links:
  derives-from: [SES-0057]
  relates-to: [DEC-0310]
---

# DEC-0311: artifact-interact Is Groundwork-Specific and SPEC-Driven

## Context

A guardrailed artifact API could be built as a generic
structured-markdown toolkit (frontmatter + typed links + sections)
with Groundwork's rules as one loadable profile, or as a
Groundwork-only tool grounded directly in the corpus SPECs.

## Decision

artifact-interact is Groundwork-specific. Its read/write/validation
behavior is defined by and validated against `docs/specs/SPEC-*.md`;
the skill is the executable form of the SPECs.

## Rationale

Tight guardrails need a fixed normative basis. Generality multiplies
design surface and weakens guarantees for zero current consumers.

## Alternatives Considered

- **Generic core + Groundwork profile** — reusable beyond Groundwork
  but more design surface and weaker validation; rejected.

## Implications

SPEC amendments imply skill updates (and vice versa: behavior the
skill needs that the SPECs don't state is a SPEC gap to fix through
sessions). TRG-0005 (first post-launch SPEC change) gains a second
consumer to keep in sync.
