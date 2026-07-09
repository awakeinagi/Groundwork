---
id: DEC-0028
type: decision
title: Fork-pull git model with branch-per-item; PR approval is the gate
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0003 @ T3"
links:
  derives-from: [SES-0003]
---

# DEC-0028: Fork-pull model, branch-per-item, PR approval as the gate

## Context

The store needed a mapping from artifact lifecycle states onto git. The
agent recommended trunk-only with app-enforced gates; the sponsor chose a
git-native alternative.

## Decision

The application/agent owns a local fork of the upstream doc repository. For
each item (Business Goal, Epic, Story, Spike, …) the agent opens a dedicated
item branch, committing refinement changes — including the item's sessions
and decisions — as they occur. Opening the item branch also opens a PR
against upstream main; **approving the PR is the human-in-the-loop sign-off**
for the associated designs. Post-merge changes to the same item reuse the
item branch with a new PR. Upstream main therefore contains only approved
artifact versions.

## Rationale

Ratification becomes a durable, host-native audit record (reviews, required
checks, merge history) rather than app-internal state, and drafts are
isolated from main by construction.

## Alternatives Considered

- **Trunk-only + status field** (agent's recommendation): simpler mental
  model, but approval audit lives only in the app.
- **Branch per goal subtree**: isolates initiatives but breaks cross-goal
  conflict detection.

## Implications

Gate mechanics (EP-0003) execute through the code-host connector (EP-0005) —
confirming the EP-0005↔EP-0001 impact edges. Approvers interact via the UI
(DEC-0032); the frontmatter `status` field
is kept synchronized with branch/PR state by the store. Graph reads over
in-refinement branches become an EP-0004 concern.
