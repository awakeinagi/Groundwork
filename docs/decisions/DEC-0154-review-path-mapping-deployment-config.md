---
id: DEC-0154
type: decision
title: The role-to-review-path mapping lives in deployment configuration, not governance files
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0026 @ T4-T5"
links:
  derives-from: [SES-0026]
  relates-to: [DEC-0043, DEC-0037]
---

# DEC-0154: Review-Path Mapping in Deployment Configuration

## Context

[DEC-0043](DEC-0043-oauth-reviews-program-user-fallback.md) made which
roles review via OAuth versus the program user "per-deployment
configuration" without locating that configuration — governance file
(PR-gated) or deployment settings.

## Decision

The role→review-path mapping lives in **deployment configuration**,
taking [DEC-0043](DEC-0043-oauth-reviews-program-user-fallback.md) at
its word. It is not a `governance/` file.

## Rationale

The mapping reflects seat procurement — an operational fact about the
deployment, not an approval rule. The audit trail of who approved what
is already carried by the signed attribution block
([DEC-0153](DEC-0153-service-signed-attribution-block.md)) and the
host review record, so PR-gating the mapping adds ceremony without
adding assurance.

## Alternatives Considered

- **Extend `governance/gate-policies.yaml`**: Arbiter-gated and
  repo-audited, but touches the approved
  [ST-0012](../stories/ST-0012-governance-config-schemas.md) schema set
  and gates an ops fact behind design governance.

## Implications

No governance schema change; the connector reads the mapping at review
time; changing a role's path is an operational change, not a gated one.
