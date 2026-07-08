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
(per [DEC-0076](../decisions/DEC-0076-semantic-gate-diff.md)).

## Acceptance Criteria

1. The surface renders a section-level semantic diff of the gated
   artifact against its last approved version — added/changed/removed
   content grouped by document section, not a raw line diff
   (per [DEC-0076](../decisions/DEC-0076-semantic-gate-diff.md)).
2. An agent-written plain-language change summary and an impact report
   (what changed, which artifacts are affected) render above the diff,
   sourced from the same impact report that lives in the re-affirmation
   PR description and event log — never a repo-stored copy
   (per [DEC-0076](../decisions/DEC-0076-semantic-gate-diff.md),
   [DEC-0146](../decisions/DEC-0146-impact-reports-pr-and-log.md)).
3. The surface reuses [ST-0045](ST-0045-goal-artifact-view.md)'s
   provenance drill-down so an approver can trace any changed section to
   its citing decisions without leaving the gate.
4. A raw unified diff of the underlying file is available one click away
   for technical reviewers, not shown by default
   (per [DEC-0076](../decisions/DEC-0076-semantic-gate-diff.md)).
5. Approve and request-changes actions call the code-host connector to
   post a review as the participant's linked identity (or the
   program-user fallback), landing in the same PR record a technical
   reviewer would see
   (per [DEC-0032](../decisions/DEC-0032-ui-wraps-pr-gate.md),
   [DEC-0043](../decisions/DEC-0043-oauth-reviews-program-user-fallback.md)).
6. A participant with no linked identity and no available program-user
   role sees an actionable prompt to complete
   [ST-0042](ST-0042-identity-login-and-oauth-linking.md)'s linking flow
   instead of a disabled button with no explanation.
7. The surface ships as a `'use client'` export of the npm package (per
   [DEC-0184](../decisions/DEC-0184-ui-ships-as-embeddable-npm-component-library.md),
   [DEC-0186](../decisions/DEC-0186-all-components-client-boundaries.md)).
8. The surface meets WCAG 2.1 AA (diff regions are screen-reader
   navigable by section, approve/request-changes are keyboard-operable)
   and reflows usably from `sm` up
   (per [DEC-0188](../decisions/DEC-0188-shared-accessibility-responsive-baseline.md)).

## Component Impact

None yet — a Component Doc for this epic's bounded context is stubbed
once the first story here refines toward it.

## Out of Scope

Committee/multi-approver gate policy mechanics
([EP-0003](../epics/EP-0003-governance-and-gate-engine.md)); the
semantic-diff computation itself (backend, [EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md)/[EP-0003](../epics/EP-0003-governance-and-gate-engine.md));
gate surfaces for artifact types other than Business Goal (the
generalization [ST-0051](ST-0051-reaffirmation-and-approval-queues.md)
depends on, once this contract is proven).

## Notes for Implementers

This story's diff/summary/impact-report rendering pattern is meant to
generalize to epic, story, and component-doc gates later — keep the
artifact-type-specific parts isolated from the shared rendering shell.
