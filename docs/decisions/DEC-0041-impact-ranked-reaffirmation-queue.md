---
id: DEC-0041
type: decision
title: Re-affirmation queues are ordered by impact rank
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0004 @ T4-T5"
links:
  derives-from: [SES-0004]
---

# DEC-0041: Impact-ranked re-affirmation queue

## Context

A staleness sweep ([DEC-0038](DEC-0038-subtree-staleness-reaffirmation.md))
can put dozens of re-affirmations in front of approvers at once; the order
they clear in determines how fast the critical path unblocks.

## Decision

Each approver gets a work queue in the Groundwork UI ordered by impact
rank: the same algorithm that orders refinement
([DEC-0027](DEC-0027-impact-ranked-refinement-order.md) / SP-0001) also
orders re-affirmation — items whose decisions constrain the most siblings
and descendants clear first. Human judgment over raw impact edges serves
until the spike lands. Notifications are batched via configured channels.

## Rationale

One prioritization brain for the whole system; clearing high-impact items
first unblocks the most downstream work per approval.

## Alternatives Considered

- **Dependency-order only**: ignores same-level impact edges.
- **Approver self-triage**: critical path delayed invisibly.

## Implications

SP-0001's algorithm gains a second consumer — its objective function should
account for re-affirmation clearing as well as initial refinement ordering
(noted as spike input).
