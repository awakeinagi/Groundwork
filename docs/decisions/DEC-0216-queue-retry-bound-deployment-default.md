---
id: DEC-0216
type: decision
title: Queue Port retry bound is a single deployment-wide default, not a per-job override
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0040 @ T1-T2"
links:
  derives-from: [SES-0040]
  relates-to: [DEC-0210, DEC-0139, DEC-0206]
  supersedes: []
---

# DEC-0216: Queue Retry Bound Is a Single Deployment-Wide Default

## Context

[DEC-0210](DEC-0210-queue-port-outbox-pattern-reuse.md) established
"bounded retries per job" but left open whether the bound is one
deployment-wide configured value or overridable per job at enqueue
time.

## Decision

v1 defines a single deployment-wide max-retry value, set via the
Composition Root's deployment configuration
([DEC-0206](DEC-0206-composition-root-yaml-config.md)); `enqueue()`
carries no per-job retry-bound parameter.

## Rationale

Matches the App Database Port precedent
([CMP-0003](../components/CMP-0003-app-database-port.md)), which
exposes no per-operation retry override either — retry policy is
adapter/deployment configuration, not a per-call parameter. No cited
Acceptance Criterion in
[ST-0060](../stories/ST-0060-queue-port.md) or
[ST-0061](../stories/ST-0061-background-job-execution-runtime.md)
calls for per-job tuning; a single default keeps the contract simplest
and can be extended later if a real job type needs a different bound.
