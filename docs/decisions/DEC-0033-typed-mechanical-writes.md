---
id: DEC-0033
type: decision
title: Mechanical writes are typed service operations; agents hold no git credentials
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0003 @ T5-T6"
links:
  derives-from: [SES-0003]
---

# DEC-0033: Typed mechanical writes; credential separation; verified fallback

## Context

Mechanical mutations (stale marks, jira-key backfill, transcript turn
appends, counters) record system facts, not design decisions — routing them
through human PR approval would create approval spam. But direct commits
raise two concerns (SES-0003 @ T5): enterprise rules may forbid direct
commits to upstream main, and safeguards must guarantee the agent commits
*only* metadata/append-only mutations, never bypassing the approval process.

## Decision

Three-part safeguard:

1. **Credential separation**: the LLM agent holds no git credentials. Only
   the storage service can write to the repository.
2. **Typed operations**: mechanical writes are expressible only as typed
   service operations (`append-turn`, `mark-stale`, `set-jira-key`, …). The
   service constructs the commit from the operation's parameters; an
   arbitrary diff is *inexpressible* through the mechanical path. Content
   changes have exactly one route: the item-branch → PR path
   (DEC-0028).
3. **Verified fallback for protected mains**: where enterprise branch
   protection forbids direct pushes, the service opens auto-PRs approved by
   a dedicated program user — gated by a deterministic mechanical-diff CI
   check verifying the diff touches only allowlisted fields/append regions.
   Machine verification replaces human approval spam. Direct-commit vs.
   auto-PR is per-deployment configuration.

## Rationale

The bypass risk is eliminated structurally (the API cannot express a design
change as a mechanical write) rather than by trusting agent behavior; the
program-user + diff-check fallback satisfies enterprise policy without
flooding humans with unrejectable approvals.

## Alternatives Considered

- **Everything through human PRs**: guarantees no bypass but spams approvers
  with facts nobody can reject, and a live session cannot PR per turn.
- **Metadata in the service DB**: breaks repo self-sufficiency.

## Implications

The mechanical-operation allowlist is part of the storage API contract
(EP-0001); the mechanical-diff validator is a required CI check the gate
engine provisions (EP-0003/EP-0005).
