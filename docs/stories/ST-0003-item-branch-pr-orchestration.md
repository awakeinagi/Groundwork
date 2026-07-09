---
id: ST-0003
type: story
title: Item-branch and gate-PR lifecycle orchestration
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-07
owner: eng-lead
created: 2026-07-06
overview: >-
  Implements the fork-pull mechanics: creating an artifact opens its
  dedicated item branch on the fork and a gate PR against upstream main,
  carrying the artifact and its sessions/decisions as they accrue.
  Refinement commits accumulate on the branch; PR merge transitions the
  artifact to approved, recording approver identities from reviews.
  Post-merge edits reuse the branch and open a new PR; artifact returns to
  in-refinement. Frontmatter status and branch/PR state stay synchronized
  throughout via atomic updates or reconciliation on next event. All host
  interactions go through the code-host connector contract; v1 is GitHub
  cloud. Full orchestration test suite passes hermetically against the
  local-git fake connector.
links:
  derives-from: [EP-0001]
  satisfies: [BG-0001]
  depends-on: [ST-0002]
  impacts: [ST-0004]
  impacted-by: [ST-0002]
cites: [DEC-0028, DEC-0032, DEC-0043, DEC-0045, DEC-0079, DEC-0172]
---

# ST-0003: Item-Branch and Gate-PR Lifecycle Orchestration

## Summary

The fork-pull mechanics: creating an artifact opens its item branch and
gate PR; refinement commits accumulate on the branch; merge is approval;
post-merge changes reuse the branch with a new PR; frontmatter `status`
stays synchronized with branch/PR state throughout.

## Acceptance Criteria

1. Creating an artifact opens a dedicated item branch on the fork and a PR
   against upstream main, carrying the artifact and its associated
   sessions/decisions as they accrue (per DEC-0028).
2. PR merge transitions the artifact to `approved`, recording approver
   identities resolved from the PR's reviews (per DEC-0028, DEC-0032,
   DEC-0043).
3. Post-merge edits to the same item reuse its branch and open a new PR;
   the artifact returns to `in-refinement`/`gated` accordingly
   (per DEC-0028).
4. Frontmatter `status` and branch/PR state can never disagree at rest:
   every lifecycle transition updates both atomically or reconciles on
   next event (per DEC-0028).
5. All host interactions go through the code-host connector contract and
   respect its capability manifest; v1 target is GitHub (cloud)
   (per DEC-0045, DEC-0172).
6. The full orchestration test suite passes hermetically against the
   local-git fake connector, which implements the complete contract
   including its capability manifest and ships as part of this story
   (per DEC-0079).

## Component Impact

CMP-0001 — supplies
the branch/PR sections of its Behavior and API Contracts.

## Out of Scope

Gate *policy* evaluation (Governance engine's `gate-policy` check); the
review UI (EP-0006); the GitHub connector implementation itself (EP-0005).

## Notes for Implementers

The fake connector is a permanent test double — its simulated review/check
semantics track the contract spec, never any particular host's quirks
(per DEC-0079).

ST-0004's per-session worktrees sit on top of the item branch this
story manages: worktrees are cut from the item branch and their
sole-version changes merge back to it, so the branch creation, reuse,
and PR-lifecycle semantics defined here bound what worktree isolation
can assume.
