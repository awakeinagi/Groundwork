---
id: ST-0046
type: story
title: Goal gate surface
status: approved
owner: eng-lead
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
created: 2026-07-08
links:
  derives-from: [EP-0006]
  satisfies: [BG-0001]
  depends-on: [ST-0045]
  impacts: [ST-0058]
  impacted-by: [ST-0042, ST-0045]
cites: [DEC-0032, DEC-0043, DEC-0076, DEC-0146, DEC-0184, DEC-0186, DEC-0188]
---

# ST-0046: Goal Gate Surface

## Summary

The review surface a Product Owner uses to approve a Business Goal
without ever opening the host PR: a semantic section-level diff, an
agent-written change summary, an impact report, and provenance links,
with approve/request-changes actions driving the host PR through the
connector; the raw diff stays one click away
(per DEC-0076).

## Acceptance Criteria

1. The surface renders a section-level semantic diff of the gated
   artifact against its last approved version — added/changed/removed
   content grouped by document section, not a raw line diff
   (per DEC-0076).
2. An agent-written plain-language change summary and an impact report
   (what changed, which artifacts are affected) render above the diff,
   sourced from the same impact report that lives in the re-affirmation
   PR description and event log — never a repo-stored copy
   (per DEC-0076,
   DEC-0146).
3. The surface reuses ST-0045's
   provenance drill-down so an approver can trace any changed section to
   its citing decisions without leaving the gate.
4. A raw unified diff of the underlying file is available one click away
   for technical reviewers, not shown by default
   (per DEC-0076).
5. Approve and request-changes actions call the code-host connector to
   post a review as the participant's linked identity (or the
   program-user fallback), landing in the same PR record a technical
   reviewer would see
   (per DEC-0032,
   DEC-0043).
6. A participant with no linked identity and no available program-user
   role sees an actionable prompt to complete
   ST-0042's linking flow
   instead of a disabled button with no explanation.
7. The surface ships as a `'use client'` export of the npm package (per
   DEC-0184,
   DEC-0186).
8. The surface meets WCAG 2.1 AA (diff regions are screen-reader
   navigable by section, approve/request-changes are keyboard-operable)
   and reflows usably from `sm` up
   (per DEC-0188).

## Component Impact

None yet — a Component Doc for this epic's bounded context is stubbed
once the first story here refines toward it.

## Out of Scope

Committee/multi-approver gate policy mechanics
(EP-0003); the
semantic-diff computation itself (backend, EP-0001/EP-0003);
gate surfaces for artifact types other than Business Goal (the
generalization ST-0051
depends on, once this contract is proven).

## Notes for Implementers

This story's diff/summary/impact-report rendering pattern is meant to
generalize to epic, story, and component-doc gates later — keep the
artifact-type-specific parts isolated from the shared rendering shell.

The approve/request-changes actions this surface performs define
ST-0058's gate-action
routes — the Inbound API fronts this story's connector-driving actions
over HTTP.
