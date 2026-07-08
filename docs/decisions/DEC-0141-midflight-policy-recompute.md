---
id: DEC-0141
type: decision
title: Governance changes recompute all open PRs' checks under the new policy; host reviews stand as facts
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0025 @ T2-T3"
links:
  derives-from: [SES-0025]
  relates-to: [DEC-0036, DEC-0037]
---

# DEC-0141: Mid-Flight Policy Recomputation

## Context

[EP-0003](../epics/EP-0003-governance-and-gate-engine.md) deferred the
recomputation semantics of mid-flight governance changes to story
level: when `roles.yaml` or `gate-policies.yaml` changes while gate PRs
are open, what happens to their checks?

## Decision

Merging a governance change triggers recomputation of the
`gate-policy` check on every open PR under the new policy. Existing
host reviews stand as facts; the check re-evaluates whether those facts
satisfy the new policy — results may flip in either direction. No PR
merges under a policy the organization has already rejected.

## Rationale

A rights revocation must bite immediately — the window between policy
change and PR re-open is exactly what such changes exist to close.
Keeping reviews as facts avoids punishing every open PR with restarted
approvals after unrelated policy edits.

## Alternatives Considered

- **Grandfather open PRs** under their open-time policy: predictable
  for authors, but revocations don't take effect where they matter
  most.
- **Recompute and dismiss reviews**: strictest, but multiplies approver
  load after every governance edit regardless of relevance.

## Implications

Bulk recomputation is one trigger class of the event-driven check
engine ([DEC-0145](DEC-0145-event-driven-check-recomputation.md));
criterion in [ST-0014](../stories/ST-0014-gate-policy-check.md).
