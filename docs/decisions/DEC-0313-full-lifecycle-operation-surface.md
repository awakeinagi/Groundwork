---
id: DEC-0313
type: decision
title: The v1 write surface is the full lifecycle operation set
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0057 @ T10-T11"
overview: >-
  artifact-interact v1 ships the complete set of typed write
  operations a refinement session actually performs: create (any
  artifact type, template-seeded, ID-allocating, slug-generating),
  append-turn (sessions, including post-close enrichment placement),
  edit-section (body section replacement on mutable artifacts),
  set-status (transition-validated, gate stamping of
  approved-by/approved-on), add-link and add-cite
  (reciprocity-enforced, cross-reference-enrichment aware), supersede
  (new DEC + superseded-by backlink + stale-walk hook), and
  update-overview. Chosen over a minimal core that grows on demand
  and over a pre-build lifecycle audit: the sole-sanctioned-path
  stance (DEC-0312) is only honest if the operation set covers what
  sessions do — gaps would force freehand violations. The exact
  flag-level shape of each operation is build territory under
  DEC-0322's eval loop; the operation list itself is fixed here.
links:
  derives-from: [SES-0057]
  relates-to: [DEC-0312, DEC-0314, DEC-0322]
---

# DEC-0313: Full Lifecycle Operation Set in v1

## Context

With the write API mandated as the sole write path (DEC-0312), the
v1 operation surface had to be sized: minimal-and-grow, audited from
observed session writes, or complete lifecycle coverage up front.

## Decision

v1 ships the full lifecycle set: `create` (template-seeded,
ID-allocating), `append-turn`, `edit-section`, `set-status`
(transition-validated, gate stamping), `add-link`/`add-cite`
(reciprocity-enforced), `supersede` (with stale-walk hook), and
`update-overview`.

## Rationale

A sole sanctioned path with coverage gaps forces the violations it
exists to prevent. The set enumerates what sessions demonstrably do —
every operation has current freehand precedent.

## Alternatives Considered

- **Minimal core (create, append-turn, edit-section, set-status),
  grow on demand** — ships sooner but the sole-path stance arrives
  only gradually; rejected.
- **Pre-build lifecycle audit to derive the set** — most rigorous but
  adds a work stage for a set the process reference already
  enumerates; rejected.

## Implications

Flag-level operation design happens in the DEC-0322 build. Operations
embed the invariants they guard (DEC-0315). Batch composition of
operations rides DEC-0314's `apply`.
