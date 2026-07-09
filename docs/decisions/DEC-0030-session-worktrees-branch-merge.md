---
id: DEC-0030
type: decision
title: Worktree per user session; merge to item branch or fork user branches
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
overview: >-
  Each user session gets its own git worktree; if worktree is only version of
  item, changes merge to generic item branch; if multiple versions or conflict
  exist, user-suffixed branches used until reconciled; sessions isolated by
  construction and divergence represented explicitly as branches for agent synthesis.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0003 @ T3"
links:
  derives-from: [SES-0003]
---

# DEC-0030: Session worktrees; item-branch merge or user branches on conflict

## Context

Concurrent edits to the same item — e.g., an agent distilling decisions
while a human edits, or two stakeholders refining in parallel sessions —
need a concurrency contract.

## Decision

Each user session gets its own git worktree. If the session's worktree holds
the only version of the item, its changes merge into the generic item branch
(e.g. `EP-0010-epic_desc`). If multiple versions or a conflict exist,
user-suffixed branches are used (e.g. `EP-0010-epic_desc-user1`,
`EP-0010-epic_desc-user2`) until reconciled.

## Rationale

Sessions are isolated by construction (no locks to leak, no mid-session
interference), and divergence is represented explicitly as branches — which
is also where the agent's cross-session synthesis
(DEC-0021) naturally operates:
reconciling user branches into the item branch before the PR is approved.

## Alternatives Considered

- **Optimistic versioning** (agent's recommendation): lighter, but pushes
  merge burden onto every client mid-session.
- **Session-scoped leases**: blocks the agent/human collaboration the system
  wants.

## Implications

The store manages worktree lifecycle per session; unreconciled user branches
are a visible pre-gate state the UI must surface; conflicting user branches
that reflect *design* disagreement (not just text conflict) should surface
through the Conflict artifact flow
(DEC-0005).
