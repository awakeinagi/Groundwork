---
id: DEC-0150
type: decision
title: A timeboxed spike validates BBDC's required-check surface before the connector story gates
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0026 @ T2-T3"
links:
  derives-from: [SES-0026]
  relates-to: [DEC-0050, DEC-0036, DEC-0142]
---

# DEC-0150: BBDC Required-Check Surface Spike

## Context

[EP-0005](../epics/EP-0005-connectors-and-identity.md) recorded a
candidate spike: Bitbucket Data Center has no native path-scoped
reviewer requirements, so the `gate-policy` check carries more
enforcement weight ([DEC-0050](DEC-0050-bitbucket-datacenter-v1.md)) —
and the whole gate design
([DEC-0036](DEC-0036-host-base-plus-service-gate-check.md),
[DEC-0142](DEC-0142-gate-engine-owns-check-registration.md)) assumes
BBDC merge checks / Code Insights can host the registered required
checks.

## Decision

[SP-0004](../spikes/SP-0004-bbdc-required-check-surface.md) — a
timeboxed spike against a real Bitbucket Data Center instance —
validates that merge checks / Code Insights suffice as the
required-check surface (per-PR blocking, re-reporting on recomputation,
program-user visibility) **before**
[ST-0020](../stories/ST-0020-bitbucket-data-center-connector.md) gates.
Findings land as decisions.

## Rationale

A failed assumption here reworks the gate design; discovering that
mid-implementation is the expensive path. The unknown is real (API
capability, not code we control), which is what spikes are for.

## Alternatives Considered

- **Fold into the connector story as a criterion**: cheaper, but the
  assumption fails at implementation time instead of before contract
  sign-off.
- **Accept the risk on documented APIs**: fastest; leaves the epic's
  recorded risk unaddressed.

## Implications

[ST-0020](../stories/ST-0020-bitbucket-data-center-connector.md)
depends on the spike; the spike is drafted in this derivation bundle
and ratified with it.
