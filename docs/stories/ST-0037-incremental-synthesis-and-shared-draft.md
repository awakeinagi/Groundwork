---
id: ST-0037
type: story
title: Incremental synthesis and shared draft
status: gated
owner: ds-lead
created: 2026-07-08
links:
  derives-from: [EP-0002]
  satisfies: [BG-0001]
  depends-on: [ST-0034, ST-0036]
  impacts: [ST-0039]
  impacted-by: [ST-0032, ST-0034, ST-0036]
cites: [DEC-0021, DEC-0030, DEC-0055]
---

# ST-0037: Incremental Synthesis and Shared Draft

## Summary

The merge step that turns per-participant 1:1 sessions into one coherent
item draft: runs on every session close, detects conflicts against prior
sessions' decisions, and keeps an evolving synthesized draft visible to
all participants for async comment — with the anchoring risk of that
visibility mitigated at the context-assembly boundary
([ST-0038](ST-0038-context-assembly-via-pack-recipes.md)), not here.

## Acceptance Criteria

1. On each session close, the agent merges new material into the target
   item's draft on its item branch: the closing session's worktree
   merges into the generic item branch when it holds the only version,
   or a user-suffixed branch when multiple versions or a conflict exist,
   until reconciled
   (per [DEC-0055](../decisions/DEC-0055-incremental-synthesis-shared-draft.md),
   [DEC-0021](../decisions/DEC-0021-one-on-one-sessions.md),
   [DEC-0030](../decisions/DEC-0030-session-worktrees-branch-merge.md)).
2. Synthesis runs conflict detection against prior sessions' accepted
   decisions on every merge; on divergence it opens the mediation flow
   with the affected participants
   (per [DEC-0055](../decisions/DEC-0055-incremental-synthesis-shared-draft.md)).
3. The evolving synthesized draft is visible to all participants for
   async comment
   (per [DEC-0055](../decisions/DEC-0055-incremental-synthesis-shared-draft.md)).
4. Participant comments on the shared draft enter the system as Change
   Proposals, never as direct draft edits
   (per [DEC-0055](../decisions/DEC-0055-incremental-synthesis-shared-draft.md)).
5. The item's PR gate sees one coherent draft plus full multi-session
   provenance (which sessions and decisions contributed which content) —
   the draft is never presented for gating without that provenance trail
   (per [DEC-0055](../decisions/DEC-0055-incremental-synthesis-shared-draft.md)).

## Component Impact

None yet — a Component Doc for this epic's bounded context is stubbed once the first story here refines toward it.

## Out of Scope

Preventing the shared draft from biasing later 1:1 sessions' framing —
owned by the context-assembly story's default exclusion rule
(per [DEC-0180](../decisions/DEC-0180-context-recipe-owns-anchoring-mitigation.md),
[ST-0038](ST-0038-context-assembly-via-pack-recipes.md)); CP triage of
draft comments once captured
([ST-0039](ST-0039-change-proposal-triage.md)); the mediation mechanics
themselves ([ST-0036](ST-0036-conflict-detection-mediation-and-escalation.md)).

## Notes for Implementers

Synthesis is the producer of the anchoring risk (it makes the draft
visible); [ST-0038](ST-0038-context-assembly-via-pack-recipes.md) is the
consumer-side control (per [DEC-0180](../decisions/DEC-0180-context-recipe-owns-anchoring-mitigation.md)).
Do not duplicate the exclusion rule here.
