---
id: DEC-0476
type: decision
title: "EP-0010 owns the Engine port contracts; the Engine ships embedded default adapters; consumers may diverge on implementation, never on feature support"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-13
source-span: "SES-0091 @ T4-T5"
overview: >-
  DEC-0121 assigned graph/vector-store ports to BG-0001 epics while
  EP-0010 also claims graph sync and semantic search, an
  unreconciled overlap. This decision gives EP-0010 sole ownership
  of the Engine's port contract definitions (graph store, vector
  store, embedding provider, corpus filesystem), has the Engine ship
  embedded zero-hosting default adapters so skill-mode never
  requires self-hosted infrastructure, and allows consuming surfaces
  like the Groundwork Application to diverge on adapter
  implementation while all adapters must support the same features.
links:
  derives-from: [SES-0091]
  relates-to: [DEC-0121, DEC-0102, DEC-0441, DEC-0444, DEC-0477, DEC-0486, DEC-0135]
---

# DEC-0476: EP-0010 owns the Engine port contracts; the Engine ships embedded default adapters; consumers may diverge on implementation, never on feature support

## Context

DEC-0121 assigned the graph-store port to EP-0004 and the vector-store/embedding ports to EP-0007 on the BG-0001 track, while EP-0010 claims graph sync and the semantic-search substrate — an overlap nothing reconciled, carried explicitly to this session.

## Decision

EP-0010 owns the definitions of the Engine's port contracts: graph store, vector store, embedding provider, and corpus filesystem. The Engine ships embedded, zero-hosting default adapters for each, so installing the paradigm's agent skills never requires self-hosted infrastructure. Consuming surfaces, notably the Groundwork Application, may diverge on adapter implementation — their own databases and embedding providers — but never on feature support: every adapter satisfies the same port contracts.

## Rationale

The advisor debate reconciled on a single interface owner to avoid co-ownership coupling, and on in-Engine defaults to avoid a dangling dependency on BG-0001 epics whose reframing DEC-0441 defers. The stakeholder added the divergence-under-consensus rule to guarantee skill-mode's zero-hosting property, giving the example that shipped agent skills must never require users to host their own Neo4j database.

## Alternatives Considered

Absorbing the ports outright and superseding the BG-0001 assignments was rejected as reaching across a goal boundary and pre-empting a deferred rechartering. Leaving adapter ownership with EP-0004/EP-0007 was rejected as a dangling cross-track dependency.

## Implications

DEC-0121's port assignments are narrowed on the BG-0002 side — they now describe BG-0001 adapter work, not port definitions — and DEC-0121's ratified citers need consistency review. Skill-mode's substrate stays self-contained per DEC-0444.
