---
id: DEC-0060
type: decision
title: "Index freshness: synchronous for the writing branch, async globally, rebuild as truth"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
overview: >-
  Writes update the writer's branch overlay synchronously—a session always reads
  its own writes. Propagation to other views (main on merge, other overlays) rides
  the change-event stream asynchronously with bounded lag. Full rebuild from the
  repository is both the recovery path and the correctness definition: an index
  state is correct iff it equals rebuild output at that ref. This gives mid-session
  agents the read-your-writes consistency they need without paying strict synchrony
  across all views, which would stall writes on every large merge.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0007 @ T2-T3"
links:
  derives-from: [SES-0007]
---

# DEC-0060: Session-sync, global-async freshness

## Context

An agent creates a link mid-session and immediately queries the graph in
the same session; the consistency contract determines whether it sees its
own write.

## Decision

Writes update the writer's branch overlay synchronously — a session always
reads its own writes. Propagation to other views (main on merge, other
overlays) rides the change-event stream asynchronously with bounded lag.
Full rebuild from the repository is both the recovery path and the
correctness definition: an index state is correct iff it equals rebuild
output at that ref.

## Rationale

Read-your-writes is the only consistency a mid-session agent actually
needs; paying strict synchrony across all views would stall writes on
every large merge.

## Alternatives Considered

- **Strictly synchronous everywhere**: merge re-indexing stalls the system.
- **Eventual everywhere**: the agent gets yesterday's answer about its own
  edit.

## Implications

Bounded-lag targets are deployment configuration; the rebuild-equals-truth
definition is operationally enforced by
DEC-0064.
