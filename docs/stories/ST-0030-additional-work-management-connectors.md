---
id: ST-0030
type: story
title: Additional work-management connectors — monday.com, OpenProject, Jira Cloud
status: deferred
release: backlog
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0005]
  satisfies: [BG-0001]
  depends-on: [ST-0025]
cites: [DEC-0155, DEC-0156]
---

# ST-0030: Additional Work-Management Connectors

> Deferred to `backlog` at creation (per
> [DEC-0156](../decisions/DEC-0156-future-connector-families-deferred.md),
> the deferral citation per
> [DEC-0100](../decisions/DEC-0100-scope-moves-cite-decisions.md)).
> Subscribed to trigger TRG-0009 — a deployment requiring a
> work-management system other than Jira Data Center revives it.

## Summary

Adapters for work-management systems beyond the Jira Data Center
reference — monday.com, OpenProject, Jira Cloud — validating the
host-agnostic contract the sponsor's modularity amendment called for.

## Acceptance Criteria

Indicative until revival re-refines this story (deferred stories cannot
pass a gate):

1. Each new adapter implements the work-management contract from
   [ST-0025](ST-0025-work-management-projection-lifecycle.md) —
   projection lifecycle, field-ownership map, drift events, backlog
   read — and declares its capability manifest
   (per [DEC-0155](../decisions/DEC-0155-pluggable-work-management-connector.md)).
2. Swapping systems is deployment configuration plus a conformant
   adapter; no core change
   (per [DEC-0155](../decisions/DEC-0155-pluggable-work-management-connector.md)).

## Component Impact

None yet — one component per adapter, stubbed at revival against the
work-management contract component (itself stubbed when
[ST-0025](ST-0025-work-management-projection-lifecycle.md) revives).

## Out of Scope

The contract and Jira DC reference adapter
([ST-0025](ST-0025-work-management-projection-lifecycle.md), deferred).
