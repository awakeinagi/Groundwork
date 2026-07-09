---
id: DEC-0064
type: decision
title: Index correctness is verified by scheduled rebuild-and-diff
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
overview: >-
  On a schedule (nightly by default) the service rebuilds the index from the
  repository at current refs and diffs against the live index. Any divergence
  raises an alarm, and the rebuilt index atomically replaces the live one. The
  same verification runs on demand after incidents. Rebuild output is the
  correctness definition (DEC-0060); incremental-update bugs produce invisible
  graph drift that misleads impact analysis or manifests. This detects graph
  drift—exactly the wrongness nobody notices—within hours and self-heals with
  atomic replacement.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0007 @ T4-T5"
links:
  derives-from: [SES-0007]
---

# DEC-0064: Scheduled rebuild-and-diff verification

## Context

Rebuild output is the correctness definition
(DEC-0060); incremental-update
bugs produce graph drift that is invisible until a wrong traversal
misleads an impact analysis or manifest.

## Decision

On a schedule (nightly by default) the service rebuilds the index from the
repository at current refs and diffs against the live index. Any
divergence raises an alarm, and the rebuilt index atomically replaces the
live one. The same verification runs on demand after incidents.

## Rationale

Graph drift is exactly the kind of wrongness nobody notices; hours-bounded
detection with self-healing replacement turns a silent corruption class
into an alerting metric.

## Alternatives Considered

- **Rebuild on failure only**: drift isn't visible as failure.
- **Rebuild on every merge**: merge latency scales with corpus size.

## Implications

Rebuild time budget becomes a monitored metric (and an SP-0002 criterion);
divergence alarms flow into the governance/ops observability surface.
