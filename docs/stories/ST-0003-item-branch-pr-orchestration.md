---
id: ST-0003
type: story
title: Item-branch and gate-PR lifecycle orchestration
status: draft
owner: eng-lead
created: 2026-07-06
links:
  derives-from: [EP-0001]
  satisfies: [BG-0001]
  depends-on: [ST-0002]
  impacts: [ST-0004]
  impacted-by: [ST-0002]
cites: [DEC-0028, DEC-0032, DEC-0043, DEC-0045, DEC-0050]
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
   respect its capability manifest; v1 target is Bitbucket Data Center
   (per DEC-0045, DEC-0050).

## Component Impact

[CMP-0001](../components/CMP-0001-artifact-store-service.md) — supplies
the branch/PR sections of its Behavior and API Contracts.

## Out of Scope

Gate *policy* evaluation (Governance engine's `gate-policy` check); the
review UI (EP-0006); the BBDC connector implementation itself (EP-0005).

## Notes for Implementers

Development-time host strategy (fake vs. real connector ordering) is an
open refinement point for this story's session.
