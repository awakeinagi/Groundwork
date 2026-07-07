---
id: DEC-0031
type: decision
title: ID allocation serialized by a lock on the API server
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0003 @ T3"
links:
  derives-from: [SES-0003]
---

# DEC-0031: ID allocation via a thread/process-safe API-server lock

## Context

IDs are sequential per prefix and never reused
([DEC-0009](DEC-0009-typed-links-stable-ids.md)); concurrent creations must
not mint the same ID — including creations on different item branches that
have not yet merged.

## Decision

The API server serializes ID allocation with a thread/process-safe lock.
Because all writes flow through the service ([DEC-0029](DEC-0029-api-writes-git-reads.md)),
service-side serialization is sufficient regardless of which branch a
creation lands on.

## Rationale

Simplest mechanism that is correct under the fork-pull model, where a
committed counter file on main would lag branches.

## Alternatives Considered

- **Committed counter file** (agent's recommendation): repo-self-sufficient,
  but under branch-per-item the main-branch counter doesn't see unmerged
  creations.
- **Scan-derived max+1**: racy without a lock anyway.

## Implications

Counter durability across service restarts must be specified at story level
(e.g., rescan all refs on boot, or a persisted allocation log); multi-node
API deployment upgrades "process-safe lock" to a distributed lock — noted
as an [EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md) story concern.
