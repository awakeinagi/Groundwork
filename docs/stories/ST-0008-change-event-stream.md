---
id: ST-0008
type: story
title: Branch-aware change-event stream
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-07
owner: eng-lead
created: 2026-07-06
links:
  derives-from: [EP-0001]
  satisfies: [BG-0001]
  depends-on: [ST-0002, ST-0010]
  impacted-by: [ST-0002, ST-0010]
cites: [DEC-0038, DEC-0059, DEC-0060, DEC-0066, DEC-0103, DEC-0121, DEC-0122,
        DEC-0124, DEC-0134, DEC-0135]
---

# ST-0008: Branch-Aware Change-Event Stream

## Summary

The event stream every derived system rides: artifact-changed events
emitted for each canonical write, branch-aware, reliably delivered, and
replayable — feeding Graph Index overlays, governance impact analysis, and
consolidation freshness.

## Acceptance Criteria

1. Every write that lands in the repository — content, mechanical, merge —
   emits an event carrying artifact ID, type, branch/ref, change kind, and
   changed fields (per DEC-0059, DEC-0060).
2. Delivery is at-least-once with per-artifact ordering; consumers are
   idempotent by contract (per DEC-0060).
3. Merge events carry enough information for the Graph Index to promote
   overlay state to the main view and drop the overlay (per DEC-0059).
4. Named consumers are wired and tested: Graph Index incremental updates
   (per DEC-0060), staleness sweeps (per DEC-0038), consolidation
   invalidation (per DEC-0066).
5. The stream is replayable from git history for any ref range — a
   consumer rebuilt from scratch converges to the same state as one that
   consumed live (per DEC-0060).
6. Events are recorded in a transactional outbox behind the app
   database port (ST-0010), atomically
   with the write's bookkeeping, and delivered by a dispatcher with
   retries; the outbox uses the port contract only — never an engine
   API directly — with the adapter config-selected (DuckDB adapter in
   v1) (per DEC-0103, DEC-0121, DEC-0122, DEC-0124).

## Component Impact

CMP-0002 — supplies the event
schema and delivery guarantees (graduated seam per
DEC-0134);
CMP-0003 — supplies the
outbox operation family and atomicity guarantee. Emission wiring lives
in CMP-0001's
behavior contract.

## Out of Scope

Consumers' internal processing (EP-0003/0004/0007); notification-center
events (EP-0006 — user-facing notifications derive from governance events,
not raw store events).

## Notes for Implementers

Replayability-from-git is the invariant the outbox must never be allowed
to erode — the outbox is delivery plumbing, not truth (per DEC-0103).
