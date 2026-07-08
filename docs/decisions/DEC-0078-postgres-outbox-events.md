---
id: DEC-0078
type: decision
title: The change-event stream is a transactional outbox in the service's Postgres
status: superseded
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0011 @ T2-T3"
links:
  derives-from: [SES-0011]
---

# DEC-0078: Postgres transactional outbox for events

## Context

The change-event stream ([ST-0008](../stories/ST-0008-change-event-stream.md)) needed a transport delivering
at-least-once with per-artifact ordering to the Graph Index, governance,
and consolidation consumers ([DEC-0060](DEC-0060-session-sync-global-async.md)).

## Decision

Each canonical write records its event in an outbox table in the service's
Postgres, atomically with the write's bookkeeping; a dispatcher delivers
to consumers with retries. Replay-from-git remains the recovery path and
correctness anchor if the outbox is lost.

## Rationale

Boring, debuggable, at-least-once by construction, and no new
infrastructure for a self-hosted enterprise deployment
([DEC-0050](DEC-0050-bitbucket-datacenter-v1.md) ops-burden logic) serving
a handful of internal consumers.

## Alternatives Considered

- **LISTEN/NOTIFY**: fire-and-forget; the outbox gets built anyway as
  catch-up.
- **Message broker**: right at large scale, heavy for on-prem v1.

## Implications

Postgres is now definitively in the reference stack (also a data point for
[SP-0002](../spikes/SP-0002-postgres-pgvector-graduation.md)'s Postgres+AGE candidate); dispatcher lag is the bounded-lag knob
of [DEC-0060](DEC-0060-session-sync-global-async.md).
