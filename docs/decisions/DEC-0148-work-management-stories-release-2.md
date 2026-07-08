---
id: DEC-0148
type: decision
title: Work-management connector stories are born deferred at release 2
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0026 @ T2-T3"
links:
  derives-from: [SES-0026]
  relates-to: [DEC-0022, DEC-0099, DEC-0100]
---

# DEC-0148: Work-Management Stories Are Release-2 Deferred

## Context

[EP-0005](../epics/EP-0005-connectors-and-identity.md) carries no
`release:` label (current release), but
[BG-0001](../goals/BG-0001-groundwork.md) declares release `2` as
"connectors, full Graph Index, consolidations" and
[DEC-0022](DEC-0022-v1-goal-refinement-slice.md) excludes Jira sync
from the v1 slice. Story derivation had to reconcile the epic's default
with the goal's release plan — including the agent's Jira backlog read
feed, which [DEC-0016](DEC-0016-agent-context-feeds.md) associated with
v1 context work.

## Decision

The work-management connector stories — projection lifecycle, drift
capture, and the backlog read feed — are drafted in full now and born
`deferred` with `release: "2"`. The code-host connector, identity, and
notifier stories stay in the current release: the PR gate and the
agent's codebase context need them in v1.

## Rationale

Deferral captures the design without widening the v1 slice; the read
feed rides with the rest of the work-management plumbing because goal
refinement can proceed without backlog overlap detection, and read
access alone would still drag in the connector substrate.

## Alternatives Considered

- **Keep Jira work in the current release**: contradicts
  [DEC-0022](DEC-0022-v1-goal-refinement-slice.md)'s sequencing without
  superseding it.
- **A thin v1 read-only backlog feed**: honors
  [DEC-0016](DEC-0016-agent-context-feeds.md)'s implication literally,
  but ships connector plumbing for a feed the v1 slice doesn't need.
- **`backlog` label**: understates a commitment the goal already names
  as release 2.

## Implications

Three deferred stories carry `release: "2"` citing this decision; they
leave v1 denominators and revive at release-2 planning, re-entering at
`draft`.
