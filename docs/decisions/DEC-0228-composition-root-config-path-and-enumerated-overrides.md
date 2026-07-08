---
id: DEC-0228
type: decision
title: The config-file path comes from one env var with a default; env overrides are limited to an enumerated set, never arbitrary dotted-path
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0043 @ T3"
links:
  derives-from: [SES-0043]
  relates-to: [DEC-0206, DEC-0122, DEC-0152]
  supersedes: []
---

# DEC-0228: Config Path from One Env Var; Enumerated Overrides Only

## Context

[DEC-0206](../decisions/DEC-0206-composition-root-yaml-config.md) fixed
the v1 config as a single reviewable YAML file, with env vars reserved
for secrets and environment-specific overrides "layered on top." It did
not fix *how the YAML path is located* nor *the scope of what env vars
may override* — which [CMP-0010](../components/CMP-0010-composition-root.md)
must pin down.

## Decision

The YAML config path is resolved from a **single environment variable**
(e.g. `GROUNDWORK_CONFIG`) with a **documented default path**.
Environment variables may override only a **documented, enumerated set**
of values: the master secret-decryption key
([DEC-0152](../decisions/DEC-0152-secrets-encrypted-in-app-database.md))
plus a small set of per-deployment values (e.g. resource paths and
endpoints). **Arbitrary dotted-path / deep-key env overrides are not
supported**, and **Adapter selection is never driven by an env var** —
it lives only in the YAML.

## Rationale

Preserves [DEC-0206](../decisions/DEC-0206-composition-root-yaml-config.md)'s
load-bearing rationale: the one YAML file remains the single reviewable
source of the deployment topology (which Adapter binds which Port).
Arbitrary deep overrides would re-open exactly that — the true topology
would no longer be readable from the file, and adapter selection could
silently drift into env space. An enumerated override set gives the
genuine 12-factor needs (secrets, per-host paths) a home without
sacrificing auditability.

## Alternatives Considered

- **Arbitrary dotted-path env overrides** (`GW__QUEUE__ADAPTER=…`):
  rejected — maximally flexible but reintroduces the scattered,
  hard-to-audit topology
  [DEC-0206](../decisions/DEC-0206-composition-root-yaml-config.md)
  explicitly rejected, and lets adapter selection escape the YAML.

## Implications

[CMP-0010](../components/CMP-0010-composition-root.md)'s config-loading
contract documents the path env var + default and the closed override
set; an override key outside the enumerated set is not silently
honored. Consistent with
[DEC-0122](../decisions/DEC-0122-config-selected-adapters.md)'s
"selection is deployment configuration, never code."
