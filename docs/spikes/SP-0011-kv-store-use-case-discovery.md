---
id: SP-0011
type: spike
title: KV-store additional use-case discovery
status: deferred
release: backlog
owner: eng-lead
created: 2026-07-08
timebox: 2d
links:
  derives-from: [EP-0008]
  satisfies: [BG-0001]
  relates-to: []
cites: [DEC-0203]
---

# SP-0011: KV-Store Additional Use-Case Discovery

> Deferred to `backlog` at creation (per
> [DEC-0203](../decisions/DEC-0203-queue-kv-ports-added.md), the
> deferral citation per
> [DEC-0100](../decisions/DEC-0100-scope-moves-cite-decisions.md)). Not
> trigger-subscribed — revived manually when a concrete candidate use
> case is proposed, not by a scale condition.

## Question

What additional KV-store use cases — beyond the two already scoped
(ephemeral coordination state as the baseline, general-purpose caching
as a supported extension, per
[DEC-0203](../decisions/DEC-0203-queue-kv-ports-added.md)) — does
Groundwork need, and does the current Port contract (get / set / delete,
with TTL) accommodate them without modification?

## Why It Blocks

Nothing today. When a new candidate use case is proposed, it blocks
confidently reusing the KV-store Port contract as-is: without this
spike, a new use might silently assume undocumented KV semantics (atomic
increment, compare-and-swap, pub/sub) the current contract doesn't
guarantee.

## Method

1. Track candidate use cases as they're proposed in future epics or
   stories.
2. For each candidate, check it against the existing get/set/delete/TTL
   contract.
3. Where a candidate doesn't fit, evaluate extending the KV-store Port
   contract vs. routing the use case to a different Port (or a new one).
4. Record contract extensions — or explicit confirmation that none are
   needed — as Decisions, per
   [DEC-0023](../decisions/DEC-0023-spike-findings-become-decisions.md).

## Findings

Pending — recorded at spike completion (or at each revival, if reused
across multiple candidate use cases).

## Resulting Decisions

Pending — at minimum: whether the KV-store Port contract needs
extension for the use case(s) that triggered revival.
