---
id: DEC-0200
type: decision
title: No fixed story count; INVEST-grounded split-vs-merge heuristics adopted
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0037 @ T2, T4, T6"
links:
  derives-from: [SES-0037]
  relates-to: [DEC-0197, DEC-0198, DEC-0199]
  supersedes: []
---

# DEC-0200: No Fixed Story Count; INVEST-Grounded Split-vs-Merge Heuristics Adopted

## Context

[DEC-0197](DEC-0197-no-fixed-epic-count.md) established the same
principle for epics. A six-seam story catalog
([DEC-0198](DEC-0198-story-slicing-seam-catalog.md)) risks the same
over-fragmentation failure mode at story grain — applying every seam to
every epic regardless of size — and a supplementary source fetched
during this session
(<https://socadk.github.io/design-practice-repository/activities/DPR-StorySplitting.html>)
independently confirmed the same anti-pattern by name: "avoid inventing
unnecessary splits without stakeholder demand."

## Decision

`story-slicing-seams.md` states explicitly there is no fixed or required
number of stories per epic; splitting exists to satisfy INVEST
(Independent, Negotiable, Valuable, Estimable, Small, Testable), not as
an end in itself. Concrete signals are given for when to split (Acceptance
Criteria ballooning past one coherent testable set; a story bundling more
than one seam; the [coupling check](DEC-0199-story-coupling-check-generalization.md)
showing low coupling between proposed halves) versus when to keep merged
(splitting would leave a half with no independently observable value;
persistent mutual coupling per the same check). Splitting's benefit
beyond scheduling is also stated: it surfaces candidate Component Doc
boundaries before Component derivation, since a story's Component
Impact field is where slicing decisions become CMP/Design Element shape.

## Rationale

An authoritative external source independently naming the same
anti-pattern this session was already guarding against (per
[DEC-0197](DEC-0197-no-fixed-epic-count.md)'s reasoning) strengthens the
case for stating it explicitly rather than leaving it as an assumed
judgment call.

## Alternatives Considered

- **Derive new story-specific split/merge language from scratch**:
  rejected — INVEST is the standard, already-authoritative vocabulary
  for story quality; reusing it keeps the guidance grounded rather than
  inventing parallel terminology for the same concept.

## Implications

`refinement-process.md`'s Story playbook references this guidance
alongside the seam catalog and the coupling check.
