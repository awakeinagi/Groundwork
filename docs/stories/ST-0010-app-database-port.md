---
id: ST-0010
type: story
title: App database port — protocol contract, conformance suite, DuckDB adapter
status: gated
owner: eng-lead
created: 2026-07-07
links:
  derives-from: [EP-0001]
  satisfies: [BG-0001]
  impacts: [ST-0008]
cites: [DEC-0018, DEC-0077, DEC-0102, DEC-0103, DEC-0121, DEC-0122, DEC-0124,
        DEC-0125]
---

# ST-0010: App Database Port

## Summary

The Canonical Store's infrastructure seam for its transactional
workload: the app database port defined as a Protocol design element,
the shared conformance test suite that defines adapter validity, and
the v1 DuckDB adapter — so the outbox and operational bookkeeping ride
a config-swappable contract instead of an engine API.

## Acceptance Criteria

1. The app database port is defined as a Protocol design element in the
   Artifact Store Service's contract, covering the Canonical Store's
   relational/transactional workload: outbox storage and dispatch
   bookkeeping, and operational bookkeeping counters (retry counts,
   session-inactivity tracking, and similar) (per [DEC-0121](../decisions/DEC-0121-infrastructure-ports.md),
   [DEC-0103](../decisions/DEC-0103-outbox-in-app-database.md)).
2. Consumers program against the port contract only; no consumer code
   references an engine API directly (per [DEC-0121](../decisions/DEC-0121-infrastructure-ports.md)).
3. The concrete adapter is selected by deployment configuration:
   swapping engines is a config change plus an adapter implementation,
   never a change to consumer code (per [DEC-0122](../decisions/DEC-0122-config-selected-adapters.md)).
4. A shared conformance test suite ships with the port; passing it is
   the definition of a valid adapter, for bundled and future adapters
   alike (per [DEC-0122](../decisions/DEC-0122-config-selected-adapters.md)).
5. v1 ships the DuckDB adapter only, and it passes the conformance
   suite (per [DEC-0124](../decisions/DEC-0124-v1-adapter-set.md), [DEC-0102](../decisions/DEC-0102-v1-embedded-stack.md)).
6. Artifact-ID allocation state is not stored behind the port and the
   port contract exposes no ID-counter surface; rescan-on-boot remains
   the sole ID-counter mechanism (per [DEC-0125](../decisions/DEC-0125-port-counters-exclude-id-allocation.md), [DEC-0077](../decisions/DEC-0077-id-rescan-on-boot.md)).

## Component Impact

[CMP-0001](../components/CMP-0001-artifact-store-service.md) — supplies
the app-database-port Protocol element, its conformance expectations,
and the DuckDB-adapter Constraint in Implementation Guidance.

## Out of Scope

The vector store and embedding ports ([EP-0007](../epics/EP-0007-consolidation-memory-layer.md))
and the graph store port ([EP-0004](../epics/EP-0004-graph-index.md));
second storage adapters — they arrive with the
[SP-0002](../spikes/SP-0002-postgres-pgvector-graduation.md) graduation
evaluation (per [DEC-0105](../decisions/DEC-0105-sp-0002-rescoped-deferred.md));
the outbox's event schema and delivery semantics
([ST-0008](ST-0008-change-event-stream.md)).

## Notes for Implementers

The conformance suite is the executable form of the port contract, in
the same spirit as the storage API's contract-first testing (per
[DEC-0018](../decisions/DEC-0018-python-backend-language-agnostic-specs.md));
write the suite against the contract, then make the DuckDB adapter pass
it.
