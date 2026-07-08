---
id: DEC-0204
type: decision
title: V1 default adapters for Queue and KV-store; alternates deferred
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0038 @ T2-T3"
links:
  derives-from: [SES-0038]
  relates-to: [DEC-0203, DEC-0102, DEC-0200]
  supersedes: []
---

# DEC-0204: V1 Default Adapters for Queue and KV-Store; Alternates Deferred

## Context

With Queue and KV-store established as Ports
([DEC-0203](DEC-0203-queue-kv-ports-added.md)), each needs a v1 default
adapter. Every existing Port in this project follows one pattern — one
v1 default adapter, alternates deferred behind a trigger
([DEC-0102](DEC-0102-v1-embedded-stack.md)'s embedded stack, with
Postgres+pgvector, Bitbucket Data Center, and external secrets all
deferred via
[SP-0002](../spikes/SP-0002-postgres-pgvector-graduation.md)/[SP-0004](../spikes/SP-0004-bbdc-required-check-surface.md)/[SP-0005](../spikes/SP-0005-external-secret-store-adapter.md)) —
and this decision keeps that pattern rather than breaking it.

## Decision

**Queue Port v1 default**: a durable, app-database-backed queue table
(DuckDB) — jobs survive a process restart, and no new storage
technology is added for v1. The ephemeral in-memory adapter
(`asyncio.Queue`) is a real, useful alternative but is **deferred/
backlog**, not built in v1.

**KV-store Port v1 default**: reuses the app-database Port — a KV table
on the same DuckDB instance, zero new deployment surface. A dedicated
embedded KV library (e.g. diskcache) is a real alternative but is also
**deferred/backlog**, not built in v1.

Neither deferred alternate is trigger-subscribed to
`TRG-0001`/`TRG-0002` — those triggers govern graduation to *external*
adapters ([DEC-0205](DEC-0205-graduation-trigger-reuse-and-spikes.md)),
not the choice between two embedded options. The deferred alternates are
revived manually if a concrete need (e.g. a testing/dev-environment
preference) surfaces.

## Rationale

Keeping v1 scoped to one default adapter per Port, matching
[BG-0001](../goals/BG-0001-groundwork.md)'s "goal refinement end-to-end"
v1 slice, avoids building parallel implementations of the same seam
before any story demands it — the exact anti-pattern
`story-slicing-seams.md`'s no-fixed-count guidance warns against
("avoid inventing unnecessary splits without stakeholder demand," the
same principle applied to adapters instead of stories). A durable
default for Queue specifically (rather than ephemeral) matters because
jobs like notifier retries and work-management reconciliation sweeps
([DEC-0169](DEC-0169-connector-push-webhook-delivery.md)) shouldn't
silently vanish on a crash or restart.

## Alternatives Considered

- **Build both adapters per Port in v1**: considered, since it was the
  stakeholder's initial direction — reconsidered against the
  established one-default-per-Port pattern and the v1 scope framing;
  the deferred/backlog path keeps the alternates available without
  paying their conformance-testing cost before anything needs them.
- **Ephemeral in-memory as the Queue default**: rejected — simplest to
  build, but loses queued jobs on crash, which is a worse default for a
  system already committed to durable, auditable state everywhere else
  (per [DEC-0008](DEC-0008-git-backed-markdown-store.md)'s canonical
  git-backed store ethos).

## Implications

[EP-0008](../epics/EP-0008-backend-application-platform.md)'s Scope
explicitly lists both deferred alternates under Out; story derivation
will draft them as `deferred`/`backlog` stories, no gate needed.
