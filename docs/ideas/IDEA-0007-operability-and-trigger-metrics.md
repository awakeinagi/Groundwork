---
id: IDEA-0007
type: idea
title: EP-0008 operability story cluster and trigger threshold metrics
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-09
proposed-by: awakeinagi@gmail.com
overview: >-
  Captured from SES-0055 findings 2 and 3 (both MAJOR, ratified at
  T7). Finding 2: non-rebuildable runtime state (ID counters DEC-0031,
  outbox DEC-0103, queue/KV DEC-0203/DEC-0204, secrets CMP-0015) has
  no backup/restore, health-endpoint, or baseline-telemetry owner —
  add an operability story cluster under EP-0008. Finding 3: armed
  triggers TRG-0001..TRG-0004 lack fitness-function-grade measurement
  (no SLO defines "degrades"/"bottleneck"), so the embedded→server
  re-architecture triggers can never fire — add a threshold-metrics
  story (EP-0008 runtime metrics, or EP-0004 graph probes);
  strengthens DEC-0105. Take-up grilling resumes at the two open
  parameters (SES-0055 T8 recommendations on record): app-db recovery
  objectives (recommended RPO 24h / RTO 4h via daily +
  upgrade-time snapshots) and provisional trigger thresholds
  (recommended app-emitted, operator-reviewed: p95 interactive read
  > 500ms sustained, graph rebuild > 60s, recurring writer-lock
  contention). Independent of the SES-0055 T9 atom-model proposal.
links:
  derives-from: [SES-0055]
  relates-to: [EP-0008, EP-0004, DEC-0031, DEC-0103, DEC-0203, DEC-0204,
               DEC-0105, CMP-0015]
---

# IDEA-0007: Operability & Trigger Metrics

## The Idea

Execute SES-0055 findings 2 and 3 (ratified accepts): derive an
operability story cluster under EP-0008 (backup/restore for
non-rebuildable app-db state, health endpoints, baseline telemetry)
and a threshold-metrics story making TRG-0001..TRG-0004 measurable.

## Spark Context

Surfaced by the SES-0055 dual-architect review (record-grounded
instance findings 2 and 6; independent instance adopted both).
Grilling on RPO/RTO and threshold numbers began at SES-0055 T8 and was
paused by the T9 atom-model proposal; both parameters are
proposal-independent and resume as-is at take-up.

## Disposition

Pending.
