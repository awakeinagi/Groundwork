---
id: SES-0018
type: session
title: Trigger subscriptions — multi-subscriber triggers and revival unsubscription
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-07
participant: awakeinagi@gmail.com
participant-role: eng-lead
facilitator: Claude Code (claude-fable-5)
transcript-fidelity: reconstructed
links:
  relates-to: [SP-0002, DEC-0105, DEC-0106, DEC-0107]
---

# SES-0018: Trigger Subscriptions

## Purpose

The participant identified two gaps in the trigger registry as designed
in [SES-0017](SES-0017-v1-storage-stack-and-triggers.md)
([DEC-0106](../decisions/DEC-0106-trigger-registry.md)): an item
subscribed to several triggers (like
[SP-0002](../spikes/SP-0002-postgres-pgvector-graduation.md) under
`TRG-0001`–`TRG-0004`) must be unsubscribed from the others when one
fires — a revived item cannot be re-revived; and one trigger should be
subscribable by multiple items so the same condition is never duplicated.

## Transcript

**T1 — awakeinagi.** If you look at the current triggers, `SP-0002` (the
graduation spike) has multiple triggers tied to it. When one of those
triggers fires and the spike is activated (no longer deferred status),
we need to make sure it is unsubscribed from the other triggers; it
can't be reactivated again. We should also make triggers subscribable by
more than one item so we don't have to create duplicate triggers for the
same condition.

**T2 — facilitator.** Reframed entries as condition + subscriber list
and asked three design details, recommendations first: fire scope
(recommended: a firing revives all subscribers — the condition holding
is a fact about the world, not about one item; each revival cites the
one firing decision), empty-trigger handling (recommended: an armed
trigger whose last subscriber is unsubscribed auto-retires, citing the
same reviving decision; a needed-again condition gets a new TRG entry),
and subscriber format (recommended: a `**Subscribers:**` block with one
action-verb line per subscription, replacing the single
`**Consequence:**` field).

**T3 — awakeinagi.** Accepted fire-all-subscribers and auto-retire as
recommended. On format, amended: "we also have Cites links for each
subscriber. E.g. `DEC-0109` creates the trigger and its first subscriber
`SP-0002`. Another `SP-0012` is later added to the same trigger by
`DEC-0121`.
We need to be able to tie each subscription to the decision (and
session) that created it." — each subscriber line carries its own
`(per DEC-nnnn)` citation; the entry-level `**Cites:**` remains the
arming decision.

## Decisions Produced

- [DEC-0109](../decisions/DEC-0109-trigger-subscriptions.md) — trigger
  entries hold a subscriber list; each subscription is individually
  decision-cited; a firing revives all subscribers
- [DEC-0110](../decisions/DEC-0110-subscription-lifecycle.md) —
  subscription lifecycle invariants: armed triggers subscribe only
  deferred artifacts (≥1); revival unsubscribes the item everywhere
  else; an emptied armed trigger auto-retires

## Conflicts Raised

None.
