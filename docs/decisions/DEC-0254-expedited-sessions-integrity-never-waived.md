---
id: DEC-0254
type: decision
title: Expedited single-round sessions compress grilling but waive no integrity step
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
overview: >-
  An expedited session is a single-round session: proposal is restated,
  confirmed once, and recorded—done in minutes. Compresses grilling only.
  Every integrity step still runs with nothing waived: decisions
  distilled and confirmed, consistency sweep and terms checks,
  decision-recall audit, staleness cascade where approved artifacts are
  modified, link checker before commit. Makes DEC-0252's hard rule
  livable for small semantic changes; keeps compliance cheap.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0050 @ T10-T13"
links:
  derives-from: [SES-0050]
---

# DEC-0254: Expedited sessions — compressed grilling, full integrity

## Context

DEC-0252's hard rule needs a cheap compliance path for small semantic
changes, or it invites working around the paradigm. What may an
expedited session skip?

## Decision

An **expedited session** is a single-round session: the proposal is
restated, confirmed once, and recorded — done in minutes. It
compresses the *grilling* only. Every integrity step still runs, none
waived: decisions distilled and confirmed, consistency sweep and terms
checks, the decision-recall audit, the staleness cascade where an
approved artifact is modified (DEC-0267), the link checker before
commit.

## Rationale

The integrity machinery is cheap and mostly automated; waiving it is
how expedited becomes a provenance hole. A small change conflicting
with a forgotten decision is precisely the failure mode the recall
audit exists to catch — arguably more likely at expedited speed, not
less.

## Alternatives Considered

- **Waive the recall audit for small changes**: fastest, wrong-way
  risk asymmetry.
- **Scale steps by blast radius**: efficient but converts a mechanical
  guarantee into a judgment call.

## Implications

The intake protocol (DEC-0255) offers this path whenever a user wants
speed; DEC-0252's hard rule stays livable. Idea-capture micro-sessions
(DEC-0258) are the degenerate case: a session record with zero
decisions still gets the checker before commit.
