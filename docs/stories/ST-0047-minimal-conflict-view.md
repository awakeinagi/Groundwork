---
id: ST-0047
type: story
title: Minimal conflict view
status: approved
owner: eng-lead
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
created: 2026-07-08
overview: >-
  Read surface for open CFL- conflict: the tension, each party's intent,
  the mediation record sourced from session transcripts, and escalation
  status. Mediation itself happens in-session; this view is where anyone
  can see where a conflict stands, read-only in v1. Per DEC-0005,
  DEC-0039, DEC-0073, DEC-0165, DEC-0183, DEC-0184, DEC-0186, DEC-0188.
links:
  derives-from: [EP-0006]
  satisfies: [BG-0001]
  depends-on: [ST-0044, ST-0045]
  impacts: [ST-0058]
  impacted-by: [ST-0044, ST-0045]
cites: [DEC-0005, DEC-0039, DEC-0073, DEC-0165, DEC-0183, DEC-0184, DEC-0186, DEC-0188]
---

# ST-0047: Minimal Conflict View

## Summary

A read surface for an open `CFL-` conflict: the tension, each party's
intent, the mediation record, and escalation status. Mediation itself
happens in-session (ST-0044); this
view is where anyone — including a party not in that session — can see
where a conflict stands
(per DEC-0005).

## Acceptance Criteria

1. The view renders the conflict's tension statement and every party's
   stated intent (not just their position), sourced from the `CFL-`
   artifact's content
   (per DEC-0005).
2. The mediation record renders as a read-only excerpt reusing
   ST-0045's provenance drill-down to
   link back to the session transcript spans where mediation happened.
3. Escalation status (open, escalated, resolved) renders with the
   arbitrating party/role if escalated, and the resolving decision if
   resolved (per DEC-0039).
   The status reflects `ConflictGate`'s actual operation surface —
   escalate, resolve, override-approver — and, when escalated, that the
   conflict does not default into any general timeout-to-default
   election (per DEC-0165,
   DEC-0183).
4. The `conflicts-with` links to every artifact in tension render as
   navigable entries, each showing that artifact's current status (a
   blocked gate is visibly explained, not just absent).
5. The view is read-only in v1 — no in-view mediation or escalation
   actions; those remain session-driven
   (per DEC-0073).
6. The view ships as a `'use client'` export of the npm package (per
   DEC-0184,
   DEC-0186).
7. The view meets WCAG 2.1 AA and reflows usably from `sm` up
   (per DEC-0188).

## Component Impact

None yet — a Component Doc for this epic's bounded context is stubbed
once the first story here refines toward it.

## Out of Scope

Conducting mediation or triggering escalation
(ST-0044, backend conflict flow in
EP-0002); a conflict
triage/queue list view (candidate post-v1 work, not scoped here).

## Notes for Implementers

Keep this view genuinely minimal per the epic's naming — it is a status
read surface, not a mediation tool; resist scope creep toward in-view
actions until a session-derived need justifies a new story.

The `CFL-` content this view renders defines
ST-0058's conflict-read
routes — the Inbound API serves exactly the read surface this story
needs, and nothing more while the view stays read-only.
