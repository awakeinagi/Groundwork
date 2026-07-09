---
id: ST-0010
type: story
title: App database port — protocol contract, conformance suite, DuckDB adapter
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-07
owner: eng-lead
created: 2026-07-07
overview: >-
  Defines the Artifact Store's infrastructure seam for transactional
  workload as a Protocol design element: the app database port covering
  outbox storage/dispatch bookkeeping and operational bookkeeping counters
  (retry counts, session-inactivity tracking). Consumers program against
  the port contract only; no consumer references an engine API directly.
  Concrete adapter selected by deployment configuration — swapping engines
  is config change plus adapter implementation, never consumer code change.
  Shared conformance test suite shipped with port; passing it defines valid
  adapter. v1 ships DuckDB adapter only. ID-allocation state not stored
  behind port; port contract exposes no ID-counter surface; rescan-on-boot
  remains sole ID-counter mechanism.
links:
  derives-from: [EP-0001]
  satisfies: [BG-0001]
  impacts: [ST-0008]
cites: [DEC-0018, DEC-0077, DEC-0102, DEC-0103, DEC-0105, DEC-0121, DEC-0122,
        DEC-0124, DEC-0125, DEC-0135]
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
   session-inactivity tracking, and similar) (per DEC-0121,
   DEC-0103).
2. Consumers program against the port contract only; no consumer code
   references an engine API directly (per DEC-0121).
3. The concrete adapter is selected by deployment configuration:
   swapping engines is a config change plus an adapter implementation,
   never a change to consumer code (per DEC-0122).
4. A shared conformance test suite ships with the port; passing it is
   the definition of a valid adapter, for bundled and future adapters
   alike (per DEC-0122).
5. v1 ships the DuckDB adapter only, and it passes the conformance
   suite (per DEC-0124, DEC-0102).
6. Artifact-ID allocation state is not stored behind the port and the
   port contract exposes no ID-counter surface; rescan-on-boot remains
   the sole ID-counter mechanism (per DEC-0125, DEC-0077).

## Component Impact

CMP-0003 — supplies the
port's Protocol element, conformance expectations, and DuckDB-adapter
Constraint (standalone protocol CMP per
DEC-0135);
CMP-0001 consumes
it via its Dependencies section.

## Out of Scope

The vector store and embedding ports (EP-0007)
and the graph store port (EP-0004);
second storage adapters — they arrive with the
SP-0002 graduation
evaluation (per DEC-0105);
the outbox's event schema and delivery semantics
(ST-0008).

## Notes for Implementers

The conformance suite is the executable form of the port contract, in
the same spirit as the storage API's contract-first testing (per
DEC-0018);
write the suite against the contract, then make the DuckDB adapter pass
it.
