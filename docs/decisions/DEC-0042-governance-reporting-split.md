---
id: DEC-0042
type: decision
title: The gate engine emits governance events and metrics; the UI renders dashboards
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0004 @ T4-T5"
links:
  derives-from: [SES-0004]
---

# DEC-0042: Governance reporting — [EP-0003](../epics/EP-0003-governance-and-gate-engine.md) emits, [EP-0006](../epics/EP-0006-refinement-web-ui.md) renders

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

- **Dashboards inside [EP-0003](../epics/EP-0003-governance-and-gate-engine.md)**: a backend epic owning UI surface muddies
  the [EP-0006](../epics/EP-0006-refinement-web-ui.md) boundary.
- **Defer reporting**: invisible sweeps and blocking exactly when the
  system is new.

## Implications

The metrics/query API joins [EP-0003](../epics/EP-0003-governance-and-gate-engine.md)'s contract list; [EP-0006](../epics/EP-0006-refinement-web-ui.md)'s scope gains
governance dashboards.
