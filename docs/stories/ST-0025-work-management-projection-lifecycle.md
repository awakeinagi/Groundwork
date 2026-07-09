---
id: ST-0025
type: story
title: Work-management connector — projection lifecycle and field ownership
status: deferred
release: "2"
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0005]
  satisfies: [BG-0001]
  impacts: [ST-0026, ST-0027]
  impacted-by: [ST-0019]
cites: [DEC-0013, DEC-0033, DEC-0045, DEC-0048, DEC-0100, DEC-0148, DEC-0151,
        DEC-0155]
---

# ST-0025: Work-Management Projection Lifecycle and Field Ownership

> Deferred to release `2` at creation (per
> DEC-0148,
> the deferral citation per
> DEC-0100).
> No trigger subscription — revival is release-2 planning. Jira Data
> Center webhook/event capability validation happens at revival (per
> DEC-0155).

## Summary

The work-management connector contract — host-agnostic and
capability-declaring, with Jira Data Center as the reference adapter —
and its projection lifecycle: issues created on first merge to main,
content canonical-owned, workflow Jira-owned and read as
projection-side telemetry.

## Acceptance Criteria

Indicative until revival re-refines this story (deferred stories cannot
pass a gate):

1. The work-management contract defines projection operations
   (create/update), the field-ownership map, backlog read, and drift
   events, with a capability manifest per adapter; Jira Data Center is
   the reference adapter
   (per DEC-0155,
   DEC-0045).
2. A projection is created when an artifact first merges to main —
   drafts never appear in the work-management system
   (per DEC-0048).
3. Projections carry title, generated summary, status, a prominent
   link to the canonical doc, and the doc ID in a custom field; full
   detail lives only in the doc store, and Component Docs get no
   projection (per DEC-0013).
4. On projection creation the issue key is written once into artifact
   frontmatter via the `set-jira-key` typed mechanical write — the
   connector's only canonical write
   (per DEC-0151,
   DEC-0033).
5. Workflow fields (status column, sprint, assignee, estimates) are
   host-owned: the connector reads them into app-side telemetry joined
   at query time, and no workflow state is ever committed to canon
   (per DEC-0048,
   DEC-0151).

## Component Impact

None yet — the work-management connector component is stubbed at
revival; the contract will follow the
CMP-0005
pattern (per DEC-0155).

## Out of Scope

Drift handling (ST-0026,
deferred); the backlog read feed
(ST-0027, deferred);
non-Jira adapters
(ST-0030,
deferred).
