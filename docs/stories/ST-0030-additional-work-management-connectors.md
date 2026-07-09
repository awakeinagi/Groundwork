---
id: ST-0030
type: story
title: Additional work-management connectors — monday.com, OpenProject, Jira Cloud
status: deferred
release: backlog
owner: eng-lead
created: 2026-07-08
overview: >-
  Deferred to backlog (trigger TRG-0009: deployment requiring work-management
  system other than Jira Data Center). Adapters for monday.com, OpenProject,
  Jira Cloud validating host-agnostic contract. Each new adapter implements
  full contract (projection lifecycle, field-ownership, drift events, backlog
  read) and declares capability manifest. Swapping systems is config plus
  conformant adapter.
links:
  derives-from: [EP-0005]
  satisfies: [BG-0001]
  depends-on: [ST-0025]
cites: [DEC-0100, DEC-0155, DEC-0156]
---

# ST-0030: Additional Work-Management Connectors

> Deferred to `backlog` at creation (per
> DEC-0156,
> the deferral citation per
> DEC-0100).
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
   ST-0025 —
   projection lifecycle, field-ownership map, drift events, backlog
   read — and declares its capability manifest
   (per DEC-0155).
2. Swapping systems is deployment configuration plus a conformant
   adapter; no core change
   (per DEC-0155).

## Component Impact

None yet — one component per adapter, stubbed at revival against the
work-management contract component (itself stubbed when
ST-0025 revives).

## Out of Scope

The contract and Jira DC reference adapter
(ST-0025, deferred).
