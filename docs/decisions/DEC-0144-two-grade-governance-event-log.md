---
id: DEC-0144
type: decision
title: The governance event log carries two truth grades — mirrored provenance facts and lossy telemetry
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Governance event log carries two truth grades. Provenance-grade facts
  (approvals, auto-resolutions, stale marks and clears) must land in git or
  host history first; log only mirrors them; rebuild from git plus host
  history reconverges on them. Telemetry-grade events (engine-internal
  operations) are authoritative for dashboards and metrics, lossy on rebuild,
  never citable as provenance. Extends rebuild-sufficiency spirit honestly
  instead of pretending notification history lives in git; nothing
  decision-shaped gains a second truth.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0025 @ T4-T5"
links:
  derives-from: [SES-0025]
  relates-to: [DEC-0042, DEC-0131, DEC-0121]
---

# DEC-0144: Two-Grade Governance Event Log

## Context

The governance event log (DEC-0042)
cannot fully meet the rebuild-sufficiency bar
(DEC-0131): gate
transitions and sweeps are reconstructible from git and host history,
but operational events — notification sends, check recomputations,
queue snapshots — exist nowhere else.

## Decision

The log carries two truth grades. **Provenance-grade** facts
(approvals, auto-resolutions, stale marks and clears) must land in git
or host history first; the log only mirrors them, and a rebuild from
git plus host history reconverges on them. **Telemetry-grade** events
(engine-internal operations) are authoritative for dashboards and
metrics, lossy on rebuild, and never citable as provenance.

## Rationale

Extends DEC-0131's spirit
honestly instead of pretending notification history lives in git:
nothing decision-shaped gains a second truth, while the observability
DEC-0042 exists for keeps its
data.

## Alternatives Considered

- **Strict rebuild-sufficiency** (log only what git+host can
  reconstruct): guts approval-latency and queue-aging metrics.
- **Log as its own source of truth**: the second truth
  DEC-0002 exists to prevent; a lost
  app database would lose governance history.

## Implications

Every event type declares its grade in the log schema; the metrics API
may expose both, but provenance queries answer only from
provenance-grade events. Criteria land in
ST-0018.
