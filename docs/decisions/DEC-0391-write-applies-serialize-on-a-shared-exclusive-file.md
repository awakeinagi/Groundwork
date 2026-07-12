---
id: DEC-0391
type: decision
title: "Write applies serialize on a shared/exclusive file lock with transactional, precondition-guarded application"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-12
source-span: "SES-0076 @ T13-T16, T19-T23, T25-T28"
overview: >-
  The gw_write apply path takes an exclusive file lock for the
  duration of an apply: ID allocation via batch keys, file edits,
  reciprocity bookkeeping, graph sync, and the post-write recheck
  all occur under it. Reads take the same lock in shared mode, so a
  read can never observe a torn mid-apply state, and concurrent
  reads never block each other. Applies are transactional, all-or-
  nothing, with rollback on recheck failure. Read operations emit
  per-section version tokens; writes carry the token they composed
  against, and the apply refuses with a re-read instruction rather
  than overwriting unseen changes. Turn appends auto-number at apply
  time and accept an expected-first-turn precondition. Write-task
  librarians may now fan out in parallel: serialization moves from
  the task level to the apply moment. This design proceeds through a
  design gate per SES-0076, and the interim single-writer rule stays
  operative until the lock build ships and is verified. Decided at
  SES-0076.
links:
  relates-to: [DEC-0392, DEC-0393, DEC-0394, DEC-0395]
  derives-from: [SES-0076]
  supersedes: [DEC-0332]
---
# DEC-0391: Write applies serialize on a shared/exclusive file lock with transactional, precondition-guarded application

## Context

SES-0076 had to choose the mechanism that lets multiple write tasks proceed safely against one corpus (skeleton restored at SES-0077).

## Decision

The `gw_write` apply path takes an exclusive file lock for the duration of an apply: ID allocation via batch keys, file edits, reciprocity bookkeeping, graph sync, and the post-write recheck all occur under it. Read operations take the same lock in shared mode, so a read can never observe a torn mid-apply state; concurrent reads never block each other.

Applies are transactional — all-or-nothing, with rollback on recheck failure, so a failed batch leaves the corpus untouched. Read operations emit per-section version tokens; write operations carry the token they composed against, and the apply refuses with a re-read instruction rather than overwriting unseen changes. Turn appends auto-number at apply time and accept an expected-first-turn precondition, refusing cleanly if the transcript advanced.

## Rationale

Not separately recorded at distillation; the rationale is carried by the Context and Decision above and by the source session's transcript at the recorded source span (skeleton restored at SES-0077).

## Alternatives Considered

A facilitator-held FIFO with dispatch-on-completion; a long-lived queue agent, rejected for DEC-0331 tension and message-drop risk; a spool directory with an opportunistic drainer; a standing Python daemon, rejected for process-lifecycle fragility; worktree isolation with merge-time IDs, redirected to the multi-session spike.

## Implications

The consequence is that write-task librarians may fan out in parallel: serialization moves from the task level, which was DEC-0332's rule, to the apply moment.
