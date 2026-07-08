---
id: DEC-0188
type: decision
title: A shared accessibility and responsive baseline is folded into every v1 story's acceptance criteria, not a standalone story
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0034 @ T2-T3"
links:
  derives-from: [SES-0034]
  supersedes: []
---

# DEC-0188: Shared Accessibility and Responsive Baseline

## Context

[EP-0006](../epics/EP-0006-refinement-web-ui.md)'s Risks flagged
"accessibility and responsive baseline" as needing a story-level
definition before v1 build, with no standard named yet.

## Decision

The standard is WCAG 2.1 AA plus Tailwind's default breakpoint set
(`sm`/`md`/`lg`/`xl`/`2xl`, per
[DEC-0185](DEC-0185-tailwind-styled-sharing-host-config.md)'s shared
Tailwind config). Every v1 story's Acceptance Criteria carries an item
citing this decision instead of a standalone "accessibility baseline"
story, since the standard has nothing to build on its own — it only has
meaning as a constraint on the surfaces that render.

## Rationale

A standalone story would produce a document with no independently
testable deliverable; folding the citation into each surface's own
acceptance criteria keeps the constraint testable exactly where it
applies (that surface's markup, focus order, and layout).

## Alternatives Considered

- **Separate "Accessibility and responsive baseline" story**: centralizes
  the standard in one place other stories `depends-on`, but produces no
  shippable artifact of its own and adds a dependency edge to every v1
  story for a constraint, not a capability.

## Implications

Every v1 story drafted in this bundle carries a WCAG 2.1 AA /
Tailwind-breakpoint acceptance criterion citing this decision. Component
docs for this bounded context must state the concrete conformance checks
(automated axe-core pass, keyboard-navigation and focus-order
requirements) as part of their contract.
