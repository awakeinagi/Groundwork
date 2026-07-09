---
id: DEC-0103
type: decision
title: The change-event outbox lives in the app database (DuckDB in v1)
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
overview: >-
  The transactional-outbox pattern for change events is hosted in the app
  database (DuckDB in v1) instead of a separate Postgres instance. Each
  canonical write records its event in an outbox table atomically with the
  write's bookkeeping; a dispatcher delivers to consumers with retries;
  replay-from-git remains the recovery path. The pattern's guarantees
  (at-least-once, per-artifact ordering, durability) are host-agnostic.
  Supersedes DEC-0078.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0017 @ T2-T3"
links:
  derives-from: [SES-0017]
  supersedes: [DEC-0078]
  relates-to: [DEC-0102, DEC-0060]
---

# DEC-0103: Change-Event Outbox in the App Database

## Context

DEC-0078 put the change-event
outbox in the service's Postgres; with the v1 stack change
(DEC-0102) that host database no longer
exists in v1.

## Decision

The transactional-outbox design is retained unchanged, hosted in the
**app database — DuckDB in v1**: each canonical write records its event
in an outbox table atomically with the write's bookkeeping; a dispatcher
delivers to consumers with retries; replay-from-git remains the recovery
path and correctness anchor. If graduation ever moves the app database
to Postgres, the pattern ports as-is.

## Rationale

The pattern's guarantees (at-least-once, per-artifact ordering per
DEC-0060, durable across
restarts) are host-agnostic; only the host changed. Same
zero-new-infrastructure logic as the original decision, now stronger:
the outbox rides the embedded database that's already there.

## Alternatives Considered

- **In-process event dispatch for single-process v1**: less machinery,
  but weaker durability across crashes/restarts and a real redesign of
  ST-0008 instead of a host
  swap.
- **Message broker**: still heavy for v1, unchanged from the original
  analysis.

## Implications

ST-0008 (gated) re-points
its criteria and citations here;
CMP-0001's Pending
notes update. Dispatcher lag remains the bounded-lag knob of
DEC-0060.
