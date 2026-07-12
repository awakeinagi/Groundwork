---
id: SP-0018
type: spike
title: "Multi-session worktree write model: merge-time ID allocation and serialized merges"
status: draft
owner: awakeinagi@gmail.com
created: 2026-07-12
timebox: 1 session
overview: >-
  A spike prototyping the multi-session write architecture the
  stakeholder sketched at SES-0076: worktree-isolated write
  execution with placeholder keys extending batch-key semantics to
  worktree scope, and a serialized merge step that allocates real
  IDs, rewrites references across filenames, frontmatter, links, and
  prose, integrates, and runs the checker. Open questions: the
  placeholder scheme, rewrite correctness, textual-conflict policy
  on shared files, the checker-failure-at-a-distance repair-or-
  bounce protocol, the merge lock across sessions, and interaction
  with DEC-0333 (git stays with the caller). Commissioned by
  DEC-0396 at SES-0076; sits under the DEC-0391 lock as the
  worktree-scale counterpart to that single-session write model.
links:
  derives-from: [EP-0009]
  relates-to: [DEC-0391, SES-0076]
cites: [DEC-0396, DEC-0391, DEC-0333, DEC-0351, DEC-0345]
---

# SP-0018: Multi-session worktree write model: merge-time ID allocation and serialized merges

## Question

Can worktree-isolated write execution with placeholder keys — batch-key semantics extended to worktree scope — combined with a serialized merge step that allocates real IDs, rewrites references, integrates, and runs the checker, support safe parallel Groundwork sessions?

## Why It Blocks

DEC-0391's shared/exclusive lock serializes concurrent writes within one session, but does nothing for two sessions working in separate worktrees at once: neither the placeholder-key scheme nor the merge protocol exists yet, so multi-session parallelism is currently unsafe and undocumented. Any future decision to permit parallel Groundwork sessions hinges on this spike's answer.

## Method

Prototype worktree-isolated write execution against placeholder keys, then a serialized merge step: allocate real IDs, rewrite references across filenames, frontmatter, links, and prose, integrate the worktree's changes, and run the full checker. Exercise the open questions directly: the placeholder scheme; rewrite correctness across all reference surfaces; textual-conflict policy on files touched by more than one worktree; the repair-or-bounce protocol when the checker fails at a distance after merge; the merge lock across sessions; and how the model interacts with DEC-0333 (git itself stays with the caller, never the librarian). Per DEC-0345, the design this spike presents — including its findings and any resulting decisions bearing an executable implementation — carries a test plan alongside it, reviewed and approved together with the design rather than assembled ad hoc after approval.

## Evaluation Criteria

Whether placeholder-key allocation and reference rewrite reproduce the same corpus state as sequential single-session writes; whether the merge lock prevents torn merges the way DEC-0391's file lock prevents torn applies; whether conflict and checker-failure cases have a well-defined, safe resolution path rather than silent corruption.

## Data-Source Assumptions

Builds on DEC-0391's lock-serialized apply model and DEC-0396's commissioning sketch from SES-0076; throwaway build per the established spike convention (DEC-0351) unless stated otherwise at gate.

## Findings

Pending — spike not yet executed.

## Resulting Decisions

Pending — spike not yet executed.
