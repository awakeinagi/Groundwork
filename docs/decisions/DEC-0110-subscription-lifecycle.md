---
id: DEC-0110
type: decision
title: Subscription lifecycle — revival unsubscribes everywhere; emptied armed triggers auto-retire
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0018 @ T1-T3"
links:
  derives-from: [SES-0018]
  relates-to: [DEC-0109, DEC-0107, DEC-0100]
---

# DEC-0110: Subscription Lifecycle Invariants

## Context

With multi-subscriber triggers
(DEC-0109) and multi-trigger items
(the graduation spike sits under four conditions), revival must clean up
the subscription graph: a revived item cannot be revived again.

## Decision

Three invariants, the first two checker-enforced:

1. **Armed triggers subscribe only deferred artifacts, at least one.**
   A subscriber line on an armed trigger whose target is not `deferred`
   is an integrity violation — this is what makes the unsubscribe rule
   mechanical and forgettable-proof.
2. **Revival unsubscribes the item everywhere.** When an item leaves
   `deferred` (whichever trigger fired, or a direct decision-cited
   revival), its subscriber lines are removed from **all other armed
   triggers** as part of the same change, covered by the same reviving
   decision — no separate ceremony.
3. **An armed trigger emptied by unsubscription auto-retires**, citing
   the same reviving decision in its `**Retired:**` line. A watched
   condition with no watchers is context noise; if the condition
   matters again, a new TRG entry is armed — IDs are never reused.

## Rationale

Invariant 1 turns "we need to make sure it's unsubscribed" from a
process promise into a checkable property: forgetting the cleanup fails
the build. Auto-retirement keeps the armed set — the only entries loaded
into agent context — exactly the set of live conditions someone is
waiting on.

## Alternatives Considered

- **Keep emptied triggers armed for future subscribers**: sits in every
  agent context doing nothing, indistinguishable from forgotten cleanup.
- **Unsubscription as its own decision**: double ceremony; the reviving
  decision already carries the intent.

## Implications

The checker validates armed-subscriber status and non-empty armed
triggers; [SPEC-triggers](../specs/SPEC-triggers.md) records the
lifecycle. When a trigger fires and revives all its subscribers
(DEC-0109), each revived item's
other subscriptions are removed and any trigger thereby emptied retires
— one decision, one commit, whole-graph consistency.
