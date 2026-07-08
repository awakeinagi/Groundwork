---
id: ST-0029
type: story
title: Additional notifier adapters — Slack, Teams, and beyond
status: deferred
release: backlog
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0005]
  satisfies: [BG-0001]
  depends-on: [ST-0024]
cites: [DEC-0075, DEC-0156]
---

# ST-0029: Additional Notifier Adapters

> Deferred to `backlog` at creation (per
> [DEC-0156](../decisions/DEC-0156-future-connector-families-deferred.md),
> the deferral citation per
> [DEC-0100](../decisions/DEC-0100-scope-moves-cite-decisions.md)).
> Subscribed to trigger TRG-0008 — a deployment requiring a
> notification channel beyond email revives it.

## Summary

Delivery channels beyond the v1 email adapter — Slack, Teams, and
whatever a deployment demands — each a new adapter under the notifier
connector contract.

## Acceptance Criteria

Indicative until revival re-refines this story (deferred stories cannot
pass a gate):

1. Each new adapter implements the notifier contract from
   [ST-0024](ST-0024-notifier-connector-email-adapter.md) and passes
   its conformance expectations
   (per [DEC-0075](../decisions/DEC-0075-notification-center-connectors.md)).
2. Channel selection stays a per-user preference; the in-app
   notification center remains the source of truth regardless of
   channel (per [DEC-0075](../decisions/DEC-0075-notification-center-connectors.md)).

## Component Impact

None yet — adapters land in or alongside
[CMP-0008](../components/CMP-0008-notification-delivery.md) at revival.

## Out of Scope

The notifier contract and email adapter
([ST-0024](ST-0024-notifier-connector-email-adapter.md)); notification
routing rules ([EP-0006](../epics/EP-0006-refinement-web-ui.md)).
