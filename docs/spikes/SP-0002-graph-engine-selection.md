---
id: SP-0002
type: spike
title: Graph engine selection for the Cross-Reference Graph Index
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-06
owner: eng-lead
created: 2026-07-06
timebox: 5d
links:
  derives-from: [EP-0004]
  satisfies: [BG-0001]
  relates-to: [SP-0001]
cites: [DEC-0061, DEC-0062, DEC-0059, DEC-0060, DEC-0064]
---

# SP-0002: Graph Engine Selection

## Question

Which graph engine should back the Cross-Reference Graph Index, given the
contract it must serve: main + per-branch overlays
([DEC-0059](../decisions/DEC-0059-main-plus-branch-overlays.md)),
session-synchronous overlay writes
([DEC-0060](../decisions/DEC-0060-session-sync-global-async.md)), the
three-tier query API with **read-only guarded openCypher as a hard
requirement** ([DEC-0062](../decisions/DEC-0062-tiered-query-api.md)),
fast deterministic rebuilds
([DEC-0064](../decisions/DEC-0064-scheduled-rebuild-diff.md)), and
self-hosted enterprise operations
([DEC-0050](../decisions/DEC-0050-bitbucket-datacenter-v1.md))?

## Why It Blocks

EP-0004 stories that touch engine specifics (overlay implementation,
executor guards, rebuild pipeline) cannot be written until the engine is
chosen; the contract tiers are engine-neutral and proceed in parallel.

## Method

1. Build a thin prototype of the named-traversal set plus the openCypher
   executor against three candidates:
   - **KuzuDB** (embedded, Cypher-native) — zero ops footprint; probe the
     multi-node/shared-state story;
   - **Postgres + Apache AGE** (openCypher extension) — likely already in
     the stack for app state; probe overlay ergonomics and AGE maturity;
   - **Neo4j (Community/Enterprise)** — reference openCypher; probe on-prem
     ops burden and licensing.
2. Load the real bootstrap graph (this repository) plus synthetic graphs at
   10x/100x scale with realistic branch-overlay counts.
3. Measure: overlay/view implementation fit, traversal ergonomics and
   latency, rebuild time at scale, guard enforcement (depth/time/result),
   multi-node deployment story, operational burden (backup, upgrade,
   monitoring) in a self-hosted enterprise.
4. Recommend an engine and record the choice, its runner-up, and any
   contract adjustments as Decisions per
   [DEC-0023](../decisions/DEC-0023-spike-findings-become-decisions.md).

## Findings

Pending — filled at completion.

## Resulting Decisions

Pending — at minimum: the engine choice and the overlay implementation
approach.
