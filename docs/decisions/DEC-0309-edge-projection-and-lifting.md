---
id: DEC-0309
type: decision
title: Edge projection and lifting — element Uses. edges are the source of truth; component depends-on is their exact typed projection
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0056 @ T16-T17"
overview: >-
  Element Uses: edges (DEC-0299) are the fine-grained source of truth
  for structural dependencies. A component's depends-on must equal the
  exact projection of its members' cross-component Uses: targets —
  checker-enforced in both directions (cross-component element edge
  with no matching depends-on entry: error; depends-on entry no
  element edge supports: error). Lifted component edges are typed
  strongest-member-wins (implementation > interface > test);
  integration work packages sequence on lifted implementation edges
  only. At epic boundaries, lifting is reported, never enforced: epic
  impact edges keep their DEC-0026 decision-influence semantics, and
  the graph's gaps command flags cross-epic structural edges lacking
  a corresponding impact edge, for session review. Enforcement:
  tools/check_links.py now (self-hosting corpus), product tier-2
  checks (CMP-0001 SchemaValidator/CheckSuite) via follow-on
  amendment. "Lifted edge" enters CONTEXT.md.
links:
  derives-from: [SES-0056]
  relates-to: [DEC-0299, DEC-0026, DEC-0301, DEC-0303]
---

# DEC-0309: Edge Projection and Lifting

## Context

Raised by the stakeholder during the DEC-0299 review: if element A
(component X) uses element B (component Y), then X-depends-on-Y must
hold — the two levels need a consistency rule, and lifted edges need
type semantics.

## Decision

- **Exact projection**: a component's `depends-on` equals the exact
  projection of its members' cross-component `Uses:` targets;
  checker errors in both directions. `depends-on` stays written in
  frontmatter (gate-visible) but is checker-locked to the projection.
- **Type lifting**: the lifted component edge carries
  `max(member edge types)` with `implementation > interface > test`.
  Integration work packages sequence on lifted `implementation`
  edges only; interface-only couplings never serialize assembly.
- **Epic boundary**: report, don't enforce. Epic `impacts` edges keep
  DEC-0026 decision-influence semantics; the graph `gaps` command
  flags cross-epic structural edges lacking a corresponding impact
  edge, prompting session review.
- **Enforcement**: `tools/check_links.py` now (self-hosting corpus);
  product tier-2 checks via follow-on CMP-0001 amendment.

## Rationale

One source of truth with a mechanically enforced projection prevents
the two levels drifting; typed lifting preserves the
non-serialization guarantee of interface edges at assembly grain;
stopping hard enforcement at epics avoids corrupting
decision-influence lists with runtime facts.

## Alternatives Considered

- **One-way check** (extra depends-on entries allowed) — permits
  unexplained edges; rejected.
- **Full derivation** (drop authored depends-on) — gates lose an
  explicit ratified declaration; rejected.
- **Untyped component edges** — scheduling consequence re-derived
  from raw element edges every time; rejected.
- **Hard enforcement to epic level** — conflates runtime dependency
  with decision influence; rejected.

## Implications

check_links gains the projection check when Uses: lines appear
(retrofit queued); graph gains lifted-edge derivation and the
cross-epic report; CMP-0001 amendment queued for product-side
enforcement.
