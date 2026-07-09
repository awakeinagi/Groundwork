---
id: DEC-0302
type: decision
title: Slices are first-class artifacts — owned vertical subsets of work packages with end-to-end acceptance criteria
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0056 @ T10-T13"
overview: >-
  A Slice is a new first-class artifact type (SL- prefix, SPEC-slice):
  a named, owned vertical subset of work packages forming one
  end-to-end behavior (e.g. "gate an artifact"), carrying its own
  acceptance-criteria block — the durable home of end-to-end test
  expectations — and the standard artifact lifecycle (draft → gated →
  approved, decision-cited like all contract content). The manifest
  references approved slices in ordered sequence, walking skeleton
  first; within a slice, build-order topo-sorts lifted implementation
  edges. Slices reference work packages across components; they never
  regroup components (DEC-0307). Adopted as the independent
  consultation instance's full position — the stakeholder chose the
  owned-artifact form over a manifest-section acceptance block,
  jointly with putting swarm orchestration on the v1 table
  (DEC-0308): the orchestrator is the slice's concrete consumer.
links:
  derives-from: [SES-0056]
  relates-to: [DEC-0300, DEC-0301, DEC-0307, DEC-0308]
---

# DEC-0302: Slice Artifact Type

## Context

End-to-end behaviors span 4–6 components regardless of grouping
(~4 real flows: run a session, gate an artifact, emit a manifest,
resolve a conflict). Without an owning artifact, nobody writes the
end-to-end test — the consultation's one divergence was where that
home lives.

## Decision

A **Slice** is a first-class artifact type (`SL-` prefix,
SPEC-slice):

- a named, owned vertical subset of work packages forming one
  end-to-end behavior;
- carries an **acceptance-criteria block** — the durable home of E2E
  test expectations, decision-cited like all contract content;
- standard lifecycle (draft → gated → approved);
- referenced by the manifest in ordered sequence, walking skeleton
  first; within a slice, build-order topo-sorts lifted
  `implementation` edges;
- slices reference work packages across components and never regroup
  components (DEC-0307).

## Rationale

E2E acceptance criteria are specification content — Groundwork's
product — and with the orchestrator in v1 scope (DEC-0308) slices
gain a concrete consumer that dispatches and verifies them.

## Alternatives Considered

- **Manifest-section acceptance blocks** (facilitator synthesis) —
  no independent lifecycle or gate; rejected by stakeholder.
- **Pure scheduling construct, acceptance out of scope**
  (record-grounded position, per DEC-0014) — mooted by DEC-0308;
  rejected.

## Implications

New directory docs/slices/, SPEC-slice, ID prefix SL-, checker and
graph support; slice derivation (which flows, which packages) is
follow-on design work feeding the walking-skeleton sequencing
ratified at SES-0055 F9.
