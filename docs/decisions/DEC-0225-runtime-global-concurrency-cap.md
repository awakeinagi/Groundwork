---
id: DEC-0225
type: decision
title: Background Job Execution Runtime's concurrency bound is a single global cap, not per-job-type
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  The Background Job Execution Runtime's concurrency bound is a single
  deployment-wide configured cap (via Composition Root), applying across all
  job-types combined. No per-job-type override exists. v1 has one concrete job
  (KV-store expiry sweep); a per-type cap would be speculative. A single global
  cap satisfies the "never unbounded fan-out" requirement and can be extended
  later if a real starvation scenario surfaces between job types.
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

ST-0061 AC6
requires a configurable, small-by-default concurrency limit but left
open whether it applies globally across all job-types or per-type.

## Decision

v1 defines a single deployment-wide configured concurrency cap, set via
the Composition Root's deployment configuration
(DEC-0206), applying
across all job-types combined. No per-job-type override exists.

## Rationale

v1 has exactly one concrete job (the KV-store expiry sweep); a
per-job-type cap would be speculative configuration surface with no
current consumer to validate it against. A single global cap is the
simplest mechanism that satisfies the "never unbounded fan-out"
requirement and can be extended to per-type caps later if a real
starvation scenario surfaces between job types.

## Alternatives Considered

T1 posed the concurrency-scope question as a single global cap versus per-job-type caps; the per-job-type alternative was weighed and set aside for v1 because it would be speculative configuration surface with no current consumer to validate it against, given the runtime has exactly one concrete job (the KV-store expiry sweep). The stakeholder confirmed the single-global-cap recommendation as given (T2). (skeleton restored at SES-0078)

## Implications

v1 ships with one deployment-wide concurrency cap, configured via the Composition Root's deployment configuration (DEC-0206), applying uniformly across all job types combined with no per-type override. If a real starvation scenario between job types surfaces later, the mechanism can be extended to per-job-type caps at that point rather than being built speculatively now. (skeleton restored at SES-0078)
