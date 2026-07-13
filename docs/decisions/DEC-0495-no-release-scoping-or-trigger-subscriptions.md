---
id: DEC-0495
type: decision
title: "No release scoping or trigger subscriptions"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi
decided-on: 2026-07-13
source-span: "SES-0092"
overview: >-
  Research artifacts never carry release scoping or TRIGGERS
  subscriptions: research informs and does not ship, and refresh is
  served by reopening with a new round or by a new inspired-by
  Research artifact rather than by trigger machinery. The write API
  rejects both at tier 1, mirroring the Idea precedent.
links:
  derives-from: [SES-0092]
  relates-to: [DEC-0448]
---

# DEC-0495: No release scoping or trigger subscriptions

## Context

Release labels and TRIGGERS subscriptions exist to scope and refresh
shippable deliverables; Research artifacts are investigative
evidence, not deliverables, and the question of whether that
machinery applies to them needed a definitive answer.

## Decision

Research artifacts never carry release scoping or TRIGGERS
subscriptions: research informs and does not ship, and refresh is
served by reopening with a new round or by a new inspired-by Research
artifact rather than by trigger machinery. The write API rejects both
at tier 1, mirroring the Idea precedent.

## Rationale

Release scoping and TRIGGERS both presuppose a deliverable that ships
and later needs re-triggering on external change; Research has no
such lifecycle — its own reopen-with-a-new-round mechanism already
serves the "this needs revisiting" need directly and more precisely
than a generic trigger subscription would.

## Alternatives Considered

Allowing optional release/TRIGGERS fields "for future use" was
considered and rejected: unused optional fields on a type that
structurally can't ship invite confusion and eventual misuse; a hard
tier-1 rejection is unambiguous.

## Implications

The write API's tier-1 validation rejects any release field or
TRIGGERS subscription supplied for type=research, matching the
existing Idea-type precedent exactly.
