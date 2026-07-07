---
id: DEC-0077
type: decision
title: ID counters are derived by rescan-on-boot; no persistent counter store
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0011 @ T2-T3"
links:
  derives-from: [SES-0011]
---

# DEC-0077: Rescan-on-boot ID counters

## Context

[DEC-0031](DEC-0031-service-lock-id-allocation.md) serialized allocation
behind a service lock but left counter durability across restarts open.

## Decision

No persistent counter state exists. On startup the service scans every
ref — main and all item branches — for the maximum existing ID per prefix,
then allocates from memory behind the lock. Single-allocator deployment is
a documented constraint (which the lock already implied).

## Rationale

The repository remains the only state: a clone rebuilds everything, and
there is no counter store whose loss or stale restore could re-mint IDs
that exist on unmerged branches. Boot cost is a ref scan — trivial at
documentation scale.

## Alternatives Considered

- **Allocation log in service DB**: fast boot, but a backup restore can
  re-issue IDs newer than the backup.
- **Committed counter file on a meta branch**: repo-sufficient but doubles
  commit traffic and adds mechanical-write surface.

## Implications

[ST-0005](../stories/ST-0005-id-allocation.md)'s durability and multi-node criteria resolve to this design;
horizontal scaling of the allocator, if ever needed, is a future decision
that supersedes this one.
