---
id: ST-0045
type: story
title: Goal artifact view with provenance drill-down
status: approved
owner: eng-lead
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
created: 2026-07-08
links:
  derives-from: [EP-0006]
  satisfies: [BG-0001]
  depends-on: [ST-0042]
  impacts: [ST-0046, ST-0047, ST-0058]
  impacted-by: []
cites: [DEC-0009, DEC-0015, DEC-0026, DEC-0090, DEC-0184, DEC-0186, DEC-0188]
---

# ST-0045: Goal Artifact View with Provenance Drill-Down

## Summary

A rendered Business Goal a stakeholder can read and trust: the goal's
content plus a drill-down path from the goal into the decisions that
shaped it and the transcript spans behind each decision
(per [DEC-0015](../decisions/DEC-0015-transcript-decision-citation-chain.md)),
with typed-link navigation to related artifacts.

## Acceptance Criteria

1. The view renders a Business Goal's full content (Summary, Why,
   Scope, Domain Context, etc.) from its stored frontmatter and body,
   never a hand-summarized paraphrase.
2. Every decision citation in the artifact body is clickable and opens
   that decision's own content inline or in a drill-down panel, which in
   turn links to the `source-span` transcript turns that support it —
   the full goal → decision → transcript chain is navigable without
   leaving the view. This relies on every body cross-reference already
   being a resolvable markdown link, not a bare ID
   (per [DEC-0015](../decisions/DEC-0015-transcript-decision-citation-chain.md),
   [DEC-0090](../decisions/DEC-0090-clickable-body-cross-references.md)).
   Where the same artifact is both a typed link (AC3) and an inline
   body citation, each renders once in its own list — the view never
   deduplicates across the two, since they answer different questions
   (structural relationship vs. in-prose citation).
3. Typed links — the closed vocabulary of `derives-from`, `satisfies`,
   `depends-on`, `conflicts-with`, `supersedes`, `relates-to`, and
   `cites` (per [DEC-0009](../decisions/DEC-0009-typed-links-stable-ids.md)),
   including the reciprocal `impacts`/`impacted-by` pair
   (per [DEC-0026](../decisions/DEC-0026-directional-impact-links.md))
   — render as a navigable, labeled list distinct from inline body
   citations, reflecting each link's direction and type.
4. The view works for any artifact status (`draft`, `gated`, `approved`,
   `stale`) and visibly labels the current status.
5. The view ships as a `'use client'` export of the npm package,
   parameterized by artifact ID so a host can deep-link to any goal
   (per [DEC-0184](../decisions/DEC-0184-ui-ships-as-embeddable-npm-component-library.md),
   [DEC-0186](../decisions/DEC-0186-all-components-client-boundaries.md)).
6. The view meets WCAG 2.1 AA (heading structure mirrors document
   structure, drill-down panels are keyboard-reachable and
   screen-reader-announced) and reflows usably from `sm` up
   (per [DEC-0188](../decisions/DEC-0188-shared-accessibility-responsive-baseline.md)).

## Component Impact

None yet — a Component Doc for this epic's bounded context is stubbed
once the first story here refines toward it.

## Out of Scope

Editing or approving the goal ([ST-0046](ST-0046-goal-gate-surface.md));
rendering epics/stories/spikes/components with this same view (a
generalization worth a future story once the goal-view contract is
proven, tracked in
[ST-0056](ST-0056-full-artifact-graph-browsing.md)); the graph query
API itself ([EP-0004](../epics/EP-0004-graph-index.md)).

## Notes for Implementers

This story's rendering primitives (body renderer, citation
drill-down, typed-link list) are the reusable core
[ST-0046](ST-0046-goal-gate-surface.md) and
[ST-0047](ST-0047-minimal-conflict-view.md) build on — design them for
reuse, not goal-specific one-offs.
