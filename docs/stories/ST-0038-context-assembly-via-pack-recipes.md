---
id: ST-0038
type: story
title: Context assembly via pack recipes
status: approved
owner: ds-lead
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
created: 2026-07-08
overview: >-
  Declarative retrieval boundary between session and Graph Index /
  Consolidation layer: each strategy pack states what context it needs—
  required graph paths, preferred consolidations, fallback crawls, token
  budget with truncation priority, on-demand tool enablement. Default
  exclusion rule keeps synthesized shared draft prose from anchoring fresh
  1:1 sessions; only structured facts flow in unless pack explicitly opts in.
links:
  derives-from: [EP-0002]
  satisfies: [BG-0001]
  depends-on: [ST-0033]
  impacts: []
  impacted-by: [ST-0033]
cites: [DEC-0056, DEC-0068, DEC-0180]
---

# ST-0038: Context Assembly via Pack Recipes

## Summary

The declarative retrieval boundary between a session and the Graph Index
/ Consolidation layer: each strategy pack states what context it needs —
required graph paths, preferred consolidations, fallback crawls, a token
budget with truncation priority, and whether on-demand graph tools are
enabled — resolved at session start and on demand, with a default
exclusion rule that keeps the synthesized shared draft from anchoring
fresh 1:1 sessions.

## Acceptance Criteria

1. Each strategy pack declares a context recipe: required graph paths,
   preferred consolidations, fallback crawls, a token budget with
   priority order for truncation, and whether on-demand graph-query
   tools are enabled mid-session
   (per DEC-0056).
2. The retrieval layer resolves a pack's recipe via a `resolve(recipe,
   task) → bundle` operation against
   EP-0004's Graph Index and
   EP-0007's
   Consolidation layer at session start, and again on demand mid-session
   when the recipe enables on-demand tools; resolution is deterministic
   for a given (recipe, task, repo-ref, index-state) and every returned
   bundle element carries source refs and freshness metadata
   (per DEC-0056,
   DEC-0068).
3. By default, a resolved context recipe excludes the incremental
   synthesis shared draft's prose from a fresh 1:1 session's context;
   only structured facts (settled, accepted decisions reachable via the
   graph) flow in — never the draft's framing or phrasing — unless a
   pack explicitly opts in for a documented reason
   (per DEC-0180).
4. When a token budget is exceeded, required paths are fetched, fresh
   consolidations substitute where they cover a path, search fills
   remaining content gaps, and everything is ranked and truncated to the
   budget by the recipe's declared priority order — never an
   undocumented heuristic
   (per DEC-0068).
5. Recipe resolution degrades gracefully when a preferred consolidation
   is stale or missing, falling back to the declared crawl rather than
   failing the session open
   (per DEC-0068).

## Component Impact

None yet — a Component Doc for this epic's bounded context is stubbed once the first story here refines toward it.

## Out of Scope

The Graph Index and Consolidation layer's own query/build mechanics
(EP-0004,
EP-0007 — this story
consumes their contracts); the pack schema fields the recipe lives inside
(ST-0033); what
produces the shared draft being excluded by default
(ST-0037).

## Notes for Implementers

The default-exclusion rule (criterion 3) is the resolution of a
named epic-level risk — treat it as load-bearing, not a nice-to-have;
a pack that opts in must document why in its `pack.yaml`.
