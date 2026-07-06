---
id: ST-0008
type: story
title: Branch-aware change-event stream
status: draft
owner: eng-lead
created: 2026-07-06
links:
  derives-from: [EP-0001]
  satisfies: [BG-0001]
  depends-on: [ST-0002]
  impacted-by: [ST-0002]
cites: [DEC-0038, DEC-0059, DEC-0060, DEC-0066]
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

## Component Impact

[CMP-0001](../components/CMP-0001-artifact-store-service.md) — supplies
the event schema and delivery guarantees in its API Contract.

## Out of Scope

Consumers' internal processing (EP-0003/0004/0007); notification-center
events (EP-0006 — user-facing notifications derive from governance events,
not raw store events).

## Notes for Implementers

Transport choice (outbox, LISTEN/NOTIFY, broker) is an open refinement
point for this story's session; replayability-from-git is the invariant
that must survive whatever is chosen.
