---
id: DEC-0038
type: decision
title: Staleness marks the whole subtree, blocks gates, and clears by re-affirmation
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0004 @ T2-T3"
links:
  derives-from: [SES-0004]
---

# DEC-0038: Subtree staleness with re-affirmation clearing

## Context

[DEC-0007](DEC-0007-impact-analysis-stale-marks.md) established impact
analysis + stale marks; the spread, blocking effect, and clearing mechanism
needed definition.

## Decision

When an approved artifact changes, its entire derived subtree is marked
stale in one mechanical sweep ([DEC-0033](DEC-0033-typed-mechanical-writes.md))
with the impact report attached. Blocking: stale artifacts cannot have new
children derived, and any open PR whose artifact has a stale ancestor fails
the `gate-policy` check until the ancestor clears. Clearing: lightweight
re-affirmation — the approver reviews the upstream diff plus impact report
and re-approves via a small PR; full re-refinement sessions happen only
where the approver rejects re-affirmation.

## Rationale

A genuinely invalidating change must reach the leaves immediately, not
after several human round-trips — but most upstream changes are absorbable,
so clearing is sized to the change: cheap when cosmetic, thorough when not.

## Alternatives Considered

- **One level at a time**: invalidation reaches component docs too slowly.
- **Advisory-only staleness**: tolerates building on invalidated bases —
  the original alignment problem, reproduced.

## Implications

Re-affirmation is a first-class gate-engine flow with its own queue
([DEC-0041](DEC-0041-impact-ranked-reaffirmation-queue.md)); the
`gate-policy` check evaluates ancestor staleness, not just approver
composition ([DEC-0036](DEC-0036-host-base-plus-service-gate-check.md)).
