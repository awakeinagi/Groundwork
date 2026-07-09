---
id: DEC-0206
type: decision
title: Composition Root v1 config format is a structured YAML deployment-config file; env vars reserved for secrets/overrides
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  v1 Composition Root reads a single structured YAML deployment config
  file naming the Adapter for each of six Ports plus each Adapter's
  configuration block. Environment variables reserved for secrets and
  environment-specific overrides, never primary mechanism for adapter
  selection. Matches project's established pattern for deployment-scoped
  settings; one reviewable file for whole topology easier to audit than
  scattered environment variables. Constrains ST-0057's Acceptance
  Criteria and Composition Root Component Doc contract. Status accepted.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0039 @ T1-T2"
links:
  derives-from: [SES-0039]
  relates-to: [DEC-0121, DEC-0122, DEC-0154]
  supersedes: []
---

# DEC-0206: Composition Root v1 Config Format — Structured YAML File

## Context

EP-0008 explicitly
left the Composition Root's config schema format (structured file,
environment variables, or both) open, to resolve at story derivation
(SES-0038).

## Decision

The v1 Composition Root reads a single structured **YAML** deployment
config file naming the Adapter selected for each of the six Ports
(DEC-0121,
DEC-0203), plus each
Adapter's own configuration block. Environment variables are reserved
for secrets and environment-specific overrides (e.g. an API key or a
per-deployment path) layered on top of the file, never the primary
mechanism for adapter selection.

## Rationale

Matches this project's own established pattern for deployment-scoped
settings — "deployment configuration" already names a place, not a
mechanism (DEC-0154),
and structured YAML is the format the project already uses for
comparable config-as-data surfaces (governance-as-code's
`gate-policies.yaml`, per
DEC-0037). One
reviewable file for the whole topology (which Adapter binds which
Port) is easier to audit than scattered environment variables.

## Alternatives Considered

- **Environment variables only**: 12-factor-idiomatic, but six Ports'
  worth of adapter selection plus per-adapter settings in flat env vars
  is hard to review as one coherent topology.
- **No v1 default, implementer's choice**: leaves the contract
  underspecified — the exact gap this decision exists to close.

## Implications

ST-0057's Acceptance Criteria
require the YAML schema and env-override precedence rules; the schema
itself is part of the Composition Root's Component Doc contract once
drafted.
