---
id: EP-0016
type: epic
title: "Observability"
status: draft
owner: awakeinagi@gmail.com
created: 2026-07-13
overview: >-
  Observability frames visibility into the paradigm's operation —
  audit trails, agent-interaction telemetry, gate/checker metrics,
  session analytics (DEC-0446's four pillars) — as a coherent cross-
  cutting framework rather than ad-hoc per-epic instrumentation,
  serving BG-0002 outcome 4's verification needs (DEC-0442). In
  scope: the observability framework and contracts — what events,
  metrics, and traces are emitted, in what format, to where, with
  what retention; the four DEC-0446 pillars; consumer definitions
  for the browsing surface, governance compliance checks, and
  dogfooding analysis. Out of scope: instrumentation points inside
  other epics' own surfaces (each owning epic implements this epic's
  contracts) and Application-side dashboards. This epic has no
  outgoing impact edges among current siblings; it is impacted-by
  Engine Core & Artifact Model (Engine operations are the primary
  instrumented surface) and Self-Governance & Dogfooding (governance
  obligations define much of what must be captured). Open risk:
  framework design depends on Engine Core & Artifact Model's Engine
  API and Agent & Skill Surfaces' contracts stabilizing first, so
  this epic's refinement should sequence after theirs; the audit
  trail sits closer to core than typical observability, as part of
  the provenance guarantee. Derives from BG-0002; draft status.
links:
  impacted-by: [EP-0010, EP-0014]
  derives-from: [BG-0002]
cites: [DEC-0462, DEC-0446, DEC-0442]
---

# EP-0016: Observability

## Summary

Visibility into the paradigm's operation — audit trails,
agent-interaction telemetry, gate/checker metrics, and session
analytics (DEC-0446's four pillars) — as a coherent cross-cutting
framework rather than ad-hoc per-epic instrumentation.

## Why (Goal Alignment)

Serves BG-0002 outcome 4's verification needs (DEC-0442): governance
obligations can only be checked mechanically if the right events,
metrics, and traces are actually captured. DEC-0446 named the four
pillars this epic frames as one framework rather than letting each
epic invent its own instrumentation.

## Scope

**In:**
- The observability framework and contracts: what events, metrics,
  and traces are emitted, in what format, to where, with what
  retention.
- The four DEC-0446 pillars: audit trails, agent-interaction
  telemetry, gate/checker metrics, session analytics.
- Consumer definitions: the browsing surface, governance compliance
  checks, and dogfooding analysis.

**Out:**
- Instrumentation points inside other epics' surfaces — each owning
  epic implements this epic's contracts, it does not define them.
- Application-side dashboards (BG-0001).

## Domain Context

Bounded context: **Groundwork observability** (per DEC-0462,
DEC-0446, DEC-0442). Consumes Engine Core & Artifact Model's
operations as its primary instrumented surface (the EP-0010→EP-0016 impact
edge) and Self-Governance & Dogfooding's compliance obligations (the
EP-0014→EP-0016 impact edge); has no outgoing impact edges among current
siblings.

## Interfaces & Contracts to Define

- The event/metric/trace emission contract: format, transport,
  retention.
- The four-pillar contract: audit trail, agent-interaction telemetry,
  gate/checker metrics, session analytics, each specified separately.
- Consumer contracts for the browsing surface, governance compliance
  checks, and dogfooding analysis.

## Risks & Open Questions

- Framework design depends on Engine Core & Artifact Model's Engine
  API and Agent & Skill Surfaces' contracts stabilizing first —
  sequence this epic's refinement after theirs.
- The audit trail is part of the provenance guarantee, so it sits
  closer to core than typical observability concerns — worth noting
  explicitly so it isn't deprioritized as a nice-to-have.

## Derived Work

None yet; this epic derives stories and spikes at its own refinement
session.
