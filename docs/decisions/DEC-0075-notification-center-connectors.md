---
id: DEC-0075
type: decision
title: An in-app notification center is the source of truth; delivery via notifier connectors
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0010 @ T2-T3"
links:
  derives-from: [SES-0010]
---

# DEC-0075: Notification center + notifier connectors

## Context

Gate requests, conflict escalations, session invitations, and staleness
sweeps all need to reach people ([DEC-0039](DEC-0039-conflict-escalation-operations.md),
[DEC-0041](DEC-0041-impact-ranked-reaffirmation-queue.md) referenced
"configured channels" without defining them).

## Decision

An in-app notification center is the source of truth: every event lands
there with read state and links into the relevant surface. External
delivery goes through pluggable notifier connectors — email in v1;
Slack/Teams and others as future adapters under the same connector pattern
(EP-0005 owns the adapter contract). Per-user channel preferences live
with the account.

## Rationale

Queues and escalations need an authoritative, auditable home that isn't
someone's inbox; the connector pattern extends naturally to delivery
channels.

## Alternatives Considered

- **Email only**: gate state buried in unread mail.
- **Host/Jira notifications**: business approvers were deliberately
  shielded from those systems ([DEC-0032](DEC-0032-ui-wraps-pr-gate.md)).

## Implications

The notifier connector contract joins EP-0005's adapter family; event →
notification routing rules are configuration; digest/batching behavior
([DEC-0041](DEC-0041-impact-ranked-reaffirmation-queue.md)) is per-user
preference.
