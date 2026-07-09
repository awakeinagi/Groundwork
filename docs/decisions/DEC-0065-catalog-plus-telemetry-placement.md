---
id: DEC-0065
type: decision
title: Consolidation placement is a static catalog plus telemetry-driven additions
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
overview: >-
  A small always-on catalog ships with the system: per-goal neighborhood,
  per-epic bundle, glossary-per-context. On top, EP-0004's path-usage telemetry
  proposes new consolidations when uncatalogued paths cross heat thresholds, and
  retirement when heat decays. Humans can also request consolidations explicitly.
  At launch there is no traffic to measure; the catalog covers predictable paths
  from day one while telemetry discovers the long tail no one predicted. Neither
  approach alone survives both cold-start and scale.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0008 @ T2-T3"
links:
  derives-from: [SES-0008]
---

# DEC-0065: Static catalog + telemetry-driven placement

## Context

Consolidations were conceived for "frequently travelled paths"
(DEC-0017), but at launch there
is no traffic to measure — and sessions need curated context most in
exactly that period.

## Decision

A small always-on catalog ships with the system: per-goal neighborhood,
per-epic bundle, glossary-per-context. On top, EP-0004's path-usage
telemetry proposes new consolidations when uncatalogued paths cross heat
thresholds, and retirement when heat decays. Humans can also request a
consolidation explicitly.

## Rationale

The catalog covers the predictable paths from day one; telemetry discovers
the long tail no one predicted. Neither alone survives both cold-start and
scale.

## Alternatives Considered

- **Telemetry-only**: nothing to serve during the trust-building months.
- **Manual curation only**: burden grows with the graph; hot paths go
  unnoticed.

## Implications

The catalog definition is configuration in the canonical repo (same
governance-as-code pattern, DEC-0037);
threshold tuning is deployment configuration.
