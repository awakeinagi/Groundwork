---
id: DEC-0131
type: decision
title: Rebuild-sufficiency is a component invariant — all derived state reconstructible from the fork's refs
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0022 @ T5-T6"
links:
  derives-from: [SES-0022]
  relates-to: [DEC-0002, DEC-0077, DEC-0103]
---

# DEC-0131: Rebuild-Sufficiency Invariant

## Context

Rescan-on-boot (DEC-0077), the
outbox-is-plumbing rule (DEC-0103),
and event replayability (ST-0008)
each assert a piece of the same guarantee without a component-level
home.

## Decision

CMP-0001 guarantees
as a component invariant: **every piece of derived state — app
database contents, outbox, worktrees, ID counters, and any cache — is
reconstructible from the fork's git refs alone.** A deployment restored
from only the fork repository converges to correct service state.

## Rationale

This is the load-bearing generalization of canonical-store discipline
(DEC-0002): git is the single source
of truth, so anything not rebuildable from it would be a second truth.
Naming it once at component level keeps each element's design honest —
any proposed persistent state must answer "how is this rebuilt from
refs?"

## Alternatives Considered

- **Leave it implicit across element items** — each element already
  hints at it; without the component-level statement, a new element
  could quietly introduce unrebuildable state.
