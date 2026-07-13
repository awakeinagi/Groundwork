---
id: DEC-0489
type: decision
title: "The Method section and its stop conditions"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi
decided-on: 2026-07-13
source-span: "SES-0092"
overview: >-
  The Method section records the investigation's search strategy,
  the quality bar for admitting a source to the register, and the
  criteria by which goal satisfaction is judged, and must state
  explicit stop conditions — a round cap, a timebox, or a
  diminishing-returns criterion — so the DEC-0450 goals-met loop is
  auditable and safe to run unattended. The conclude-versus-abandon
  choice is judged against the stated stop conditions. Method is
  written at commissioning and may be refined in later rounds.
links:
  derives-from: [SES-0092]
  relates-to: [DEC-0450]
---

# DEC-0489: The Method section and its stop conditions

## Context

An unattended or loop-driven research process needs an explicit,
auditable definition of when it should keep going, admit a source, or
judge a goal satisfied — otherwise a goals-met loop (DEC-0450) has no
safe termination signal.

## Decision

The Method section records the investigation's search strategy, the
quality bar for admitting a source to the register, and the criteria
by which goal satisfaction is judged, and must state explicit stop
conditions — a round cap, a timebox, or a diminishing-returns
criterion — so the DEC-0450 goals-met loop is auditable and safe to
run unattended. The conclude-versus-abandon choice is judged against
the stated stop conditions. Method is written at commissioning and may
be refined in later rounds.

## Rationale

Without a written stop condition, an agent-run research loop has no
principled way to decide it is done short of exhausting an arbitrary
budget; naming the condition up front lets both the agent and a
reviewing stakeholder judge conclusion or abandonment against a
pre-committed standard rather than after-the-fact rationalization.

## Alternatives Considered

Leaving stop conditions implicit (a per-round human judgment call
only) was considered and rejected: it works for stakeholder-supervised
research but blocks the unattended agent-loop use case the stakeholder
explicitly wants more of.

## Implications

The concluded-transition gate (see the decision on the concluded gate)
checks the final round's Goals Assessment against Method's stated stop
conditions. Method's presence is enforced by the main-file section
skeleton.
