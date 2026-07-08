---
id: ST-0018
type: story
title: Governance event log and metrics API
status: gated
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0003]
  satisfies: [BG-0001]
  depends-on: [ST-0008, ST-0010]
  impacted-by: [ST-0014, ST-0015, ST-0016, ST-0017]
cites: [DEC-0018, DEC-0042, DEC-0102, DEC-0121, DEC-0144, DEC-0146]
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
   (per [DEC-0042](../decisions/DEC-0042-governance-reporting-split.md),
   [DEC-0146](../decisions/DEC-0146-impact-reports-pr-and-log.md)).
2. Every event type declares its truth grade: provenance-grade events
   mirror facts already landed in git or host history and reconverge on
   rebuild; telemetry-grade events are dashboard-authoritative, lossy
   on rebuild, and never citable as provenance
   (per [DEC-0144](../decisions/DEC-0144-two-grade-governance-event-log.md)).
3. The log persists behind the App Database Port; no consumer or engine
   code touches a database engine API directly
   (per [DEC-0121](../decisions/DEC-0121-infrastructure-ports.md),
   [DEC-0102](../decisions/DEC-0102-v1-embedded-stack.md)).
4. A language-neutral metrics/query API exposes the log for
   [EP-0006](../epics/EP-0006-refinement-web-ui.md) dashboards
   (approval latency, stale counts, conflict aging, gate throughput),
   with provenance queries answering only from provenance-grade events
   (per [DEC-0042](../decisions/DEC-0042-governance-reporting-split.md),
   [DEC-0144](../decisions/DEC-0144-two-grade-governance-event-log.md),
   [DEC-0018](../decisions/DEC-0018-python-backend-language-agnostic-specs.md)).

## Component Impact

[CMP-0004](../components/CMP-0004-governance-gate-engine.md) — supplies
its event-log and metrics-API contract sections.

## Out of Scope

Rendering dashboards ([EP-0006](../epics/EP-0006-refinement-web-ui.md),
per [DEC-0042](../decisions/DEC-0042-governance-reporting-split.md));
delivering notifications — the event→notification routing belongs to
the notification center ([EP-0006](../epics/EP-0006-refinement-web-ui.md))
and its notifier connectors
([EP-0005](../epics/EP-0005-connectors-and-identity.md), per
[DEC-0075](../decisions/DEC-0075-notification-center-connectors.md));
the ChangeEvent stream itself
([CMP-0002](../components/CMP-0002-change-event.md), which this log
consumes but does not produce).
