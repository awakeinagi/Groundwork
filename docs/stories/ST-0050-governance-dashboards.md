---
id: ST-0050
type: story
title: Governance dashboards
status: deferred
release: "2"
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0006]
  satisfies: [BG-0001]
  depends-on: [ST-0045]
cites: [DEC-0042, DEC-0073, DEC-0100, DEC-0133, DEC-0163]
---

# ST-0050: Governance Dashboards

> Deferred to release `2` at creation (per
> [DEC-0073](../decisions/DEC-0073-v1-ui-surfaces.md), the v1 surface
> subset; the deferral citation per
> [DEC-0100](../decisions/DEC-0100-scope-moves-cite-decisions.md)/[DEC-0133](../decisions/DEC-0133-out-of-scope-differentiated-rule.md)). No
> trigger subscription — revival is release-2 planning.

## Summary

Dashboards surfacing the governance-reporting split's metrics (per
[DEC-0042](../decisions/DEC-0042-governance-reporting-split.md)) —
design velocity, gate throughput, staleness backlog — for owners who
need a program-level view rather than one artifact at a time.

## Acceptance Criteria

Indicative until revival re-refines this story (deferred stories cannot
pass a gate):

1. Renders the governance metrics API's named endpoints (`get-approval-latency`,
   `get-stale-counts`, `get-conflict-aging`, `get-gate-throughput`,
   `search-events`) as charts/tables scoped by goal, epic, or the whole
   design (per [DEC-0042](../decisions/DEC-0042-governance-reporting-split.md),
   [DEC-0163](../decisions/DEC-0163-governance-metrics-api-named-endpoints.md)).
2. Reuses [ST-0045](ST-0045-goal-artifact-view.md)'s provenance
   drill-down so a metric can be traced back to the artifacts behind it.

## Component Impact

None — deferred.

## Out of Scope

The metrics API itself ([EP-0003](../epics/EP-0003-governance-and-gate-engine.md)).

## Notes for Implementers

Revisit against whatever metrics the governance/gate engine has actually
shipped by release 2 — this story's ACs are a placeholder, not a locked
contract.
