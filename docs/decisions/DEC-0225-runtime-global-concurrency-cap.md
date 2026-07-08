---
id: DEC-0225
type: decision
title: Background Job Execution Runtime's concurrency bound is a single global cap, not per-job-type
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0042 @ T1-T2"
links:
  derives-from: [SES-0042]
  relates-to: [DEC-0206]
  supersedes: []
---

# DEC-0225: Runtime Concurrency Cap Is Global, Not Per-Job-Type

## Context

[ST-0061](../stories/ST-0061-background-job-execution-runtime.md) AC6
requires a configurable, small-by-default concurrency limit but left
open whether it applies globally across all job-types or per-type.

## Decision

v1 defines a single deployment-wide configured concurrency cap, set via
the Composition Root's deployment configuration
([DEC-0206](DEC-0206-composition-root-yaml-config.md)), applying
across all job-types combined. No per-job-type override exists.

## Rationale

v1 has exactly one concrete job (the KV-store expiry sweep); a
per-job-type cap would be speculative configuration surface with no
current consumer to validate it against. A single global cap is the
simplest mechanism that satisfies the "never unbounded fan-out"
requirement and can be extended to per-type caps later if a real
starvation scenario surfaces between job types.
