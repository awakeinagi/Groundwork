---
id: DEC-0427
type: decision
title: "Collaboration protocol: branch-per-session with a pull request at session close"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-12
source-span: "SES-0082 T14, T19, T20, T21, T31"
accepted-in: SES-0082
overview: >-
  In team mode each session runs on its own branch, landing via a
  pull request at close. Shared append surfaces (CONTEXT.md,
  TRIGGERS.md, SPEC files) need a declared conflict-resolution
  strategy; CI runs the checker post-merge. Derivation binds to main
  only; rebase plus checker re-validation is mandatory at close;
  mid-session approvals become visible to others only at merge.
links:
  derives-from: [SES-0082]
  relates-to: [DEC-0252, DEC-0265, DEC-0416]
---

# DEC-0427: Collaboration protocol: branch-per-session with a pull request at session close

## Context

With canonical-remote topology settled (DEC-G), SES-0082 needed a concrete protocol for how multiple concurrent sessions on the same corpus reach consensus without corrupting each other's work, especially around shared append-only surfaces like CONTEXT.md and TRIGGERS.md.

## Decision

In team mode each session runs on its own branch and lands through a pull request opened at session close. Three constraints are part of the rule. Shared append surfaces such as CONTEXT.md, TRIGGERS.md, and the SPEC files require a declared conflict-resolution strategy, and the integrity checker runs in continuous integration on the post-merge result. Derivation binds to the main branch: only artifacts approved on main feed dependent work, and dependent sessions are sequenced or explicitly branch-chained. Rebase plus checker re-validation is a mandatory session-close step. Approvals made mid-session become visible to other sessions only at merge.

## Rationale

Branch-per-session isolates concurrent grilling sessions from each other the same way DEC-0391's file lock isolates concurrent writes within one process, extended to the multi-process/multi-clone team setting. Binding derivation to main (rather than to any branch) prevents a session from building on work that never lands, and the merge-time visibility rule keeps approval semantics unambiguous — there is exactly one place (main) where "approved" is durably true.

## Alternatives Considered

Allowing sessions to derive from each other's unmerged branches was rejected as DEC-0252-incompatible in practice — it would make "which artifacts exist" branch-dependent and ambiguous. A shared-lock-across-clones model (rather than branch-per-session) was rejected as requiring new distributed infrastructure the git-remote-as-consensus topology (DEC-G) was chosen specifically to avoid.

## Implications

Session-close tooling in team mode must add a rebase-plus-recheck step and a pull-request-open step beyond the solo-mode close sequence. CONTEXT.md, TRIGGERS.md, and the SPEC files need a documented conflict-resolution strategy before this protocol is exercised in earnest. Continuous integration must run the full checker on every merge to main.
