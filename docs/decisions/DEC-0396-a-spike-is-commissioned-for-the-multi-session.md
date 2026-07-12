---
id: DEC-0396
type: decision
title: "A spike is commissioned for the multi-session worktree write model"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-12
source-span: "SES-0076 @ T15-T17, T19, T21"
overview: >-
  A spike will prototype the multi-session write architecture the
  stakeholder sketched at SES-0076: worktree-isolated execution,
  placeholder keys extending batch-key semantics to worktree scope,
  and serialized merges that allocate real IDs, rewrite references,
  integrate, and run the checker, with conflict policy and merge
  locking as its open questions. Worktrees suit parallel sessions;
  the DEC-0391 lock suits parallel writes within one session.
  Decided at SES-0076.
links:
  derives-from: [SES-0076]
  relates-to: [DEC-0391]
---
# DEC-0396: A spike is commissioned for the multi-session worktree write model

## Context

During SES-0076 the stakeholder sketched a multi-session write architecture too large to settle in-session (skeleton restored at SES-0077).

## Decision

A spike will prototype the multi-session write architecture the stakeholder sketched during the session: worktree-isolated execution, placeholder keys extending batch-key semantics to worktree scope, and serialized merges that allocate real IDs, rewrite references, integrate, and run the checker — with conflict policy and merge locking as its open questions.

## Rationale

Worktrees suit parallel sessions; the shared/exclusive lock suits parallel writes within one session.

## Alternatives Considered

No alternatives were separately recorded at distillation (skeleton restored at SES-0077).

## Implications

No separate implications were recorded at distillation; the operative consequences are stated in the Decision (skeleton restored at SES-0077).
