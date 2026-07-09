---
id: ST-0063
type: story
title: Ephemeral in-memory Queue adapter (deferred alternate)
status: deferred
release: "backlog"
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0008]
  satisfies: [BG-0001]
  depends-on: [ST-0060]
  impacts: []
  impacted-by: [ST-0060]
cites: [DEC-0204]
---

# ST-0063: Ephemeral In-Memory Queue Adapter (Deferred Alternate)

## Summary

An `asyncio.Queue`-backed alternate Adapter for the Queue Port
(ST-0060) — a real, useful option (e.g. tests,
local dev without persistence overhead) but not the v1 default, and not
built in v1
(per DEC-0204).

## Acceptance Criteria

1. Passes the Queue Port's conformance suite
   (ST-0060) like any other Adapter, when
   built.
2. Jobs do not survive a process restart — documented as the Adapter's
   defining trade-off against the durable default, never mistaken for
   it in deployment configuration.

## Component Impact

None — deferred; no Component Doc work occurs until revived.

## Out of Scope

The durable v1 default adapter — ST-0060.

## Notes for Implementers

Not subscribed to `TRG-0001`/`TRG-0002` — those triggers govern
graduation to *external* adapters, not the choice between two embedded
options. Revive manually if a concrete need (e.g. a testing/dev-
environment preference) surfaces
(per DEC-0204).
