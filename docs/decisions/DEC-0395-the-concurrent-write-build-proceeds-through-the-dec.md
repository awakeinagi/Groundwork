---
id: DEC-0395
type: decision
title: "The concurrent-write build proceeds through the DEC-0335 design gate; the SES-0076 mechanism comparison stands as its DEC-0337 option survey"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-12
source-span: "SES-0076 @ T14-T23"
overview: >-
  Nothing is built until a written design with its test plan is
  presented and approved, per DEC-0335. The design must cover the
  shared/exclusive lock, transactional rollback, version-token
  preconditions, guarded turn appends, and graph-sync-under-lock.
  The mechanism comparison recorded across SES-0076's queue-design
  turns (held FIFO, queue agent, batch-and-flush, spool-and-drainer,
  daemon, lock-in-write-path, worktrees) constitutes the DEC-0337
  option survey for the DEC-0391 build. Decided at SES-0076.
links:
  derives-from: [SES-0076]
  relates-to: [DEC-0335, DEC-0337, DEC-0391, DEC-0396]
---
# DEC-0395: The concurrent-write build proceeds through the design gate; the SES-0076 mechanism comparison stands as its option survey

## Context

The DEC-0391 lock build required its DEC-0335 design gate and DEC-0337 option survey to be arranged (skeleton restored at SES-0077).

## Decision

Nothing is built until a written design with its test plan is presented and approved. The design must cover the shared/exclusive lock, transactional rollback, version-token preconditions, guarded turn appends, and graph-sync-under-lock.

The mechanism comparison recorded across the session's queue-design turns — held FIFO, queue agent, batch-and-flush, spool-and-drainer, daemon, lock-in-write-path, and worktrees — constitutes this decision's option survey.

## Rationale

Not separately recorded at distillation; the rationale is carried by the Context and Decision above and by the source session's transcript at the recorded source span (skeleton restored at SES-0077).

## Alternatives Considered

No alternatives were separately recorded at distillation (skeleton restored at SES-0077).

## Implications

No separate implications were recorded at distillation; the operative consequences are stated in the Decision (skeleton restored at SES-0077).
