---
id: DEC-0163
type: decision
title: The governance metrics/query API exposes fixed named endpoints, not a generic query language
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0029 @ T5-T6"
links:
  derives-from: [SES-0029]
  relates-to: [DEC-0042, DEC-0144, DEC-0018, DEC-0162]
---

# DEC-0163: Governance Metrics API — Fixed Named Endpoints

## Context

ST-0018 requires
a "language-neutral metrics/query API" exposing at minimum approval
latency, stale counts, conflict aging, and gate throughput for
EP-0006 dashboards, plus
provenance queries answering
only from provenance-grade events
(DEC-0144). The API shape
— fixed endpoints versus a generic parametrized query — was undecided.

## Decision

`GovernanceEventLog` exposes one API item per named metric
(`get-approval-latency`, `get-stale-counts`, `get-conflict-aging`,
`get-gate-throughput`), each taking a time range, plus a
`search-events` item for ad hoc provenance-grade lookups. No generic
query language.

## Rationale

Matches the story's explicit "at minimum" list exactly, keeps the
contract simple and directly testable against
DEC-0018's
language-neutral OpenAPI deliverable, and avoids designing an
aggregation query language before any second consumer demands one.

## Alternatives Considered

A single generic `query(event-types[], group-by, range)` endpoint —
rejected as more flexible than the current requirement warrants; it
would push query-language design into this contract now for a benefit
(supporting hypothetical future metrics) that can instead be handled by
adding a new named endpoint when a real one is needed.

## Implications

`GovernanceEventLog`'s API contract carries these five items. Adding a
new dashboard metric later is a small, gated contract addition (a new
named endpoint), not a query-language extension.
