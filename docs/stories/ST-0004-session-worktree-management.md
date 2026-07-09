---
id: ST-0004
type: story
title: Session worktree management and divergence handling
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-07
owner: eng-lead
created: 2026-07-06
links:
  derives-from: [EP-0001]
  satisfies: [BG-0001]
  depends-on: [ST-0003]
  impacted-by: [ST-0002, ST-0003]
cites: [DEC-0030, DEC-0055, DEC-0057]
---

# ST-0004: Session Worktree Management and Divergence Handling

## Summary

Per-session isolation on top of the item branch: each user session gets a
git worktree; sole-version changes merge to the item branch; concurrent
divergent versions get user-suffixed branches surfaced for synthesis;
abandoned worktrees are cleaned up.

## Acceptance Criteria

1. Opening a session provisions a dedicated worktree off the item branch;
   all of that session's writes land there (per DEC-0030).
2. On session close, if the worktree holds the only live version of the
   item, its changes merge into the generic item branch (per DEC-0030).
3. If multiple sessions produced divergent versions, user-suffixed
   branches (e.g. `EP-0010-desc-user1`) are created and the divergence is
   surfaced to the synthesis flow rather than auto-merged (per DEC-0030,
   DEC-0055).
4. Worktrees of sessions auto-closed for inactivity are garbage-collected
   after their partial distillation commits (per DEC-0057).
5. Worktree state is reconstructible after service restart: no in-flight
   session is orphaned or double-provisioned.

## Component Impact

CMP-0001 — supplies
the concurrency sections of its Behavior Contract.

## Out of Scope

The synthesis logic itself (Session Agent, EP-0002); conflict-artifact
creation for design-level disagreement (agent's call, per DEC-0030
implications).

## Notes for Implementers

Reconciliation of user branches into the item branch is agent-driven; this
story only guarantees the branches exist, are visible, and merge cleanly
when told to.
