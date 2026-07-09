---
id: DEC-0042
type: decision
title: The gate engine emits governance events and metrics; the UI renders dashboards
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
overview: >-
  The gate engine (EP-0003) owns the governance event log capturing gate
  transitions, staleness sweeps, and conflict lifecycle, and exposes a
  language-neutral metrics and query API. The web UI epic (EP-0006) owns
  dashboards rendered over that API. This seam pattern allows alternative
  front ends to consume the metrics contract without backend changes, giving
  governance observability its own ownership boundary and making approval
  latency, stale counts, conflict aging, and gate throughput visible while
  trust in the new system is being established.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0004 @ T4-T5"
links:
  derives-from: [SES-0004]
---

# DEC-0042: Governance reporting — EP-0003 emits, EP-0006 renders

## Context

Governance observability (approval latency, stale counts, conflict aging,
gate throughput) needed an owner, especially because staleness sweeps and
conflict blocking must be visible while trust in the new system is being
established.

## Decision

The gate engine owns the governance event log (gate transitions, staleness
sweeps, conflict lifecycle) and exposes a language-neutral metrics/query
API. The web UI epic owns dashboards rendered over that API.

## Rationale

Same seam pattern as every other boundary in the system; an alternative
front end can consume the metrics contract without backend changes.

## Alternatives Considered

- **Dashboards inside EP-0003**: a backend epic owning UI surface muddies
  the EP-0006 boundary.
- **Defer reporting**: invisible sweeps and blocking exactly when the
  system is new.

## Implications

The metrics/query API joins EP-0003's contract list; EP-0006's scope gains
governance dashboards.
