---
id: DEC-0037
type: decision
title: Governance configuration lives as versioned files in the canonical repo
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0004 @ T2-T3"
links:
  derives-from: [SES-0004]
---

# DEC-0037: Governance-as-code in the canonical repo

## Context

Role assignments (PO / Eng Lead / DS Lead / Arbiter), domain→approver
mappings, and per-artifact-type gate policies need an authoritative,
auditable home.

## Decision

Governance configuration is versioned files in the canonical repository
(e.g. `governance/roles.yaml`, `governance/domains.yaml`,
`governance/gate-policies.yaml`), edited through the same PR flow as any
artifact — changing who can approve is itself a gated change, with the
Arbiter as the owner of `governance/`. The Admin UI is a friendly editor
over these files, not a separate store.

## Rationale

Approval-rights changes get the full audit trail; a clone rebuilds complete
system state (consistent with [DEC-0008](DEC-0008-git-backed-markdown-store.md));
no second source of truth to drift.

## Alternatives Considered

- **Service DB + admin UI**: real-time edits, but rights changes bypass the
  PR audit trail and break repo self-sufficiency.
- **Code-host teams as source**: host team admins (often IT) would control
  Groundwork governance; roles like Arbiter don't map cleanly.

## Implications

Governance files get their own schema (tier-1 validated like artifacts,
per [DEC-0034](DEC-0034-two-tier-validation.md)); the gate engine watches
them and recompiles branch protection on change
([DEC-0036](DEC-0036-host-base-plus-service-gate-check.md)); host teams
are a *projection* of `roles.yaml`, synced by the connector.
