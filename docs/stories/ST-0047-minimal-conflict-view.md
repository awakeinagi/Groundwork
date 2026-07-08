---
id: ST-0047
type: story
title: Minimal conflict view
status: approved
owner: eng-lead
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
created: 2026-07-08
links:
  derives-from: [EP-0006]
  satisfies: [BG-0001]
  depends-on: [ST-0044, ST-0045]
  impacts: []
  impacted-by: [ST-0044, ST-0045]
cites: [DEC-0005, DEC-0039, DEC-0073, DEC-0165, DEC-0183, DEC-0184, DEC-0186, DEC-0188]
---

# ST-0047: Minimal Conflict View

## Summary

A read surface for an open `CFL-` conflict: the tension, each party's
intent, the mediation record, and escalation status. Mediation itself
happens in-session ([ST-0044](ST-0044-session-conversation-ux.md)); this
view is where anyone — including a party not in that session — can see
where a conflict stands
(per [DEC-0005](../decisions/DEC-0005-intent-first-mediation-then-escalation.md)).

## Acceptance Criteria

1. The view renders the conflict's tension statement and every party's
   stated intent (not just their position), sourced from the `CFL-`
   artifact's content
   (per [DEC-0005](../decisions/DEC-0005-intent-first-mediation-then-escalation.md)).
2. The mediation record renders as a read-only excerpt reusing
   [ST-0045](ST-0045-goal-artifact-view.md)'s provenance drill-down to
   link back to the session transcript spans where mediation happened.
3. Escalation status (open, escalated, resolved) renders with the
   arbitrating party/role if escalated, and the resolving decision if
   resolved (per [DEC-0039](../decisions/DEC-0039-conflict-escalation-operations.md)).
   The status reflects `ConflictGate`'s actual operation surface —
   escalate, resolve, override-approver — and, when escalated, that the
   conflict does not default into any general timeout-to-default
   election (per [DEC-0165](../decisions/DEC-0165-conflict-gate-operation-surface.md),
   [DEC-0183](../decisions/DEC-0183-conflicts-no-default-timeout-election.md)).
4. The `conflicts-with` links to every artifact in tension render as
   navigable entries, each showing that artifact's current status (a
   blocked gate is visibly explained, not just absent).
5. The view is read-only in v1 — no in-view mediation or escalation
   actions; those remain session-driven
   (per [DEC-0073](../decisions/DEC-0073-v1-ui-surfaces.md)).
6. The view ships as a `'use client'` export of the npm package (per
   [DEC-0184](../decisions/DEC-0184-ui-ships-as-embeddable-npm-component-library.md),
   [DEC-0186](../decisions/DEC-0186-all-components-client-boundaries.md)).
7. The view meets WCAG 2.1 AA and reflows usably from `sm` up
   (per [DEC-0188](../decisions/DEC-0188-shared-accessibility-responsive-baseline.md)).

## Component Impact

None yet — a Component Doc for this epic's bounded context is stubbed
once the first story here refines toward it.

## Out of Scope

Conducting mediation or triggering escalation
([ST-0044](ST-0044-session-conversation-ux.md), backend conflict flow in
[EP-0002](../epics/EP-0002-refinement-session-agent.md)); a conflict
triage/queue list view (candidate post-v1 work, not scoped here).

## Notes for Implementers

Keep this view genuinely minimal per the epic's naming — it is a status
read surface, not a mediation tool; resist scope creep toward in-view
actions until a session-derived need justifies a new story.
