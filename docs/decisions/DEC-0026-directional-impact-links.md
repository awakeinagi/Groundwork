---
id: DEC-0026
type: decision
title: Same-level impact is modeled as reciprocal directional links
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-05
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-05
source-span: "SES-0002 @ T1-T2"
links:
  derives-from: [SES-0002]
---

# DEC-0026: Same-level impact modeled as reciprocal directional links

## Context

Refinement of one artifact often shapes the decisions available to its
siblings (e.g., one epic's contract choices constraining another's), and
this influence exists at every level — goals, epics, stories, spikes. The
existing link vocabulary had no way to express it: `derives-from` is
cross-level, `depends-on` is consumption of contracts, not decision
influence.

## Decision

Two new typed links, `impacts` and `impacted-by`, are added to the closed
vocabulary. Semantics: "X impacts Y" means decisions recorded while refining
X are expected to constrain, shape, or invalidate decisions in Y. Impact
links connect same-type artifacts only. Both directions are stored — X lists
`impacts: [Y]` and Y lists `impacted-by: [X]` — and reciprocity plus the
same-type restriction are enforced mechanically by the link checker.

## Rationale

Directional edges are the minimum structure a refinement-ordering algorithm
needs (DEC-0027). Storing both
directions keeps each artifact self-describing when read in isolation
(important for agents holding a single doc); the consistency risk of
redundant storage is eliminated by checker-enforced reciprocity rather than
by convention.

## Alternatives Considered

- **Store `impacts` only, derive the inverse in the Graph Index**: no
  redundancy, but a doc no longer reveals what impacts it when read alone.
- **Reuse `relates-to`**: untyped and undirected — too weak to rank on.

## Implications

[SPEC-artifact-common](../specs/SPEC-artifact-common.md) vocabulary and
integrity rules updated; `tools/check_links.py` enforces reciprocity.
Impact edges are proposals until ratified at the artifact's gate, like any
other frontmatter content.
