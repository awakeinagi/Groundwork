---
id: SP-0011
type: spike
title: KV-store additional use-case discovery
status: deferred
release: backlog
owner: eng-lead
created: 2026-07-08
overview: >-
  Question: what additional KV-store use cases beyond the two already
  scoped (ephemeral coordination state as baseline, general-purpose
  caching as extension per DEC-0203) does Groundwork need, and does the
  current Port contract (get/set/delete with TTL) accommodate them
  without modification? Blocks no current work; blocks confident Port
  reuse when a new use case is proposed (without this spike, a new use
  might assume undocumented semantics like atomic increment, compare-and-
  swap, or pub/sub that the current contract doesn't guarantee). Method
  tracks candidate uses as proposed, checks each against existing
  contract, evaluates extending Port vs. routing to different Port where
  use doesn't fit. Deferred to backlog; not trigger-subscribed, revived
  manually by concrete use-case proposal. Findings pending.
timebox: 2d
links:
  derives-from: [EP-0008]
  satisfies: [BG-0001]
  relates-to: []
cites: [DEC-0023, DEC-0100, DEC-0203]
---

# SP-0011: KV-Store Additional Use-Case Discovery

> Deferred to `backlog` at creation (per
> DEC-0203, the
> deferral citation per
> DEC-0100). Not
> trigger-subscribed — revived manually when a concrete candidate use
> case is proposed, not by a scale condition.

## Question

What additional KV-store use cases — beyond the two already scoped
(ephemeral coordination state as the baseline, general-purpose caching
as a supported extension, per
DEC-0203) — does
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
   DEC-0023.

## Findings

Pending — recorded at spike completion (or at each revival, if reused
across multiple candidate use cases).

## Resulting Decisions

Pending — at minimum: whether the KV-store Port contract needs
extension for the use case(s) that triggered revival.
