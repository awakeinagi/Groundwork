---
id: SP-0009
type: spike
title: AWS SQS adapter evaluation for the Queue Port
status: deferred
release: backlog
owner: eng-lead
created: 2026-07-08
timebox: 3d
links:
  derives-from: [EP-0008]
  satisfies: [BG-0001]
  relates-to: [SP-0010]
cites: [DEC-0205]
---

# SP-0009: AWS SQS Adapter Evaluation for the Queue Port

> Deferred to `backlog` at creation (per
> [DEC-0205](../decisions/DEC-0205-graduation-trigger-reuse-and-spikes.md),
> the deferral citation per
> [DEC-0100](../decisions/DEC-0100-scope-moves-cite-decisions.md)).
> Subscribed to triggers `TRG-0001` and `TRG-0002` — either firing
> revives it.

## Question

When `TRG-0001` or `TRG-0002` fires, does AWS SQS serve as the Queue
Port's external adapter — and what does migration from the embedded,
durable app-database-backed queue
([DEC-0204](../decisions/DEC-0204-v1-default-adapters-deferred-alternates.md))
look like without losing in-flight jobs?

## Why It Blocks

Nothing today — that is why it is deferred. On a trigger firing, it
blocks any multi-node deployment story and any background-job story that
depends on cross-instance queue delivery (notifier retries, work-
management sync polling, once more than one app instance is serving).

## Method

1. Establish which trigger fired and what it demands (high availability?
   concurrent writers/instances? scale?) — the answer shapes urgency and
   the acceptable migration window.
2. Prototype the Queue Port contract (enqueue / consume / ack / retry)
   against AWS SQS: standard vs. FIFO queues, visibility timeout as the
   ack mechanism, dead-letter queue for retry exhaustion.
3. Evaluate operational overhead and cost against self-hosted
   alternatives (Celery/RQ + Redis), given Groundwork's self-hosted-first
   posture for enterprise deployments.
4. Define the migration path from the embedded DB-backed queue —
   drain-and-cutover vs. dual-write — and the rollback story.
5. Record the adapter choice and migration plan as Decisions, per
   [DEC-0023](../decisions/DEC-0023-spike-findings-become-decisions.md).

## Findings

Pending — recorded at spike completion.

## Resulting Decisions

Pending — at minimum: the adapter choice and the migration approach.
