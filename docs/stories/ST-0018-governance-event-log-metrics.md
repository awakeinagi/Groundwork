---
id: ST-0018
type: story
title: Governance event log and metrics API
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
overview: >-
  Observability spine of governance: the two-grade event log (provenance
  and telemetry) the engine emits for gate transitions, staleness sweeps,
  re-affirmation outcomes, conflicts, checks, and System-Decision
  auto-resolutions, plus a language-neutral metrics/query API for
  dashboards. Persists behind App Database Port.
links:
  derives-from: [EP-0003]
  satisfies: [BG-0001]
  depends-on: [ST-0008, ST-0010]
  impacted-by: [ST-0014, ST-0015, ST-0016, ST-0017]
cites: [DEC-0018, DEC-0042, DEC-0075, DEC-0102, DEC-0121, DEC-0144, DEC-0146]
---

# ST-0018: Governance Event Log and Metrics API

## Summary

The observability spine of governance: the two-grade event log the
engine emits and the language-neutral metrics/query API the dashboards
consume.

## Acceptance Criteria

1. The engine emits governance events covering, at minimum: gate
   transitions, staleness sweeps and clears (with their impact reports
   stored telemetry-grade), re-affirmation outcomes, conflict
   lifecycle, check registrations and recomputations, and
   System-Decision auto-resolutions
   (per DEC-0042,
   DEC-0146).
2. Every event type declares its truth grade: provenance-grade events
   mirror facts already landed in git or host history and reconverge on
   rebuild; telemetry-grade events are dashboard-authoritative, lossy
   on rebuild, and never citable as provenance
   (per DEC-0144).
3. The log persists behind the App Database Port; no consumer or engine
   code touches a database engine API directly
   (per DEC-0121,
   DEC-0102).
4. A language-neutral metrics/query API exposes the log for
   EP-0006 dashboards
   (approval latency, stale counts, conflict aging, gate throughput),
   with provenance queries answering only from provenance-grade events
   (per DEC-0042,
   DEC-0144,
   DEC-0018).

## Component Impact

CMP-0004 — supplies
its event-log and metrics-API contract sections.

## Out of Scope

Rendering dashboards (EP-0006,
per DEC-0042);
delivering notifications — the event→notification routing belongs to
the notification center (EP-0006)
and its notifier connectors
(EP-0005, per
DEC-0075);
the ChangeEvent stream itself
(CMP-0002, which this log
consumes but does not produce).
