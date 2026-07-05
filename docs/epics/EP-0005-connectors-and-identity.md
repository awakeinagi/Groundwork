---
id: EP-0005
type: epic
title: Connectors & Identity
status: draft
owner: eng-lead
created: 2026-07-05
links:
  derives-from: [BG-0001]
  satisfies: [BG-0001]
  depends-on: [EP-0001, EP-0003]
  impacts: [EP-0001, EP-0006]
  impacted-by: [EP-0001, EP-0003]
cites: [DEC-0002, DEC-0013, DEC-0016, DEC-0024, DEC-0026]
---

# EP-0005: Connectors & Identity

## Summary

The pluggable boundary adapters: the Jira connector (projection sync, drift
detection, editor redirection), read-only code-host connectors (Bitbucket,
GitHub) for agent context, and the auth provider interface. Each sits behind
a defined API contract so implementations are swappable.

## Why (Goal Alignment)

BG-0001 outcome 5 (sync without drift) is the Jira connector
([DEC-0002](../decisions/DEC-0002-doc-store-canonical.md),
[DEC-0013](../decisions/DEC-0013-jira-summary-plus-link.md)). The agent's
existing-context awareness ([DEC-0016](../decisions/DEC-0016-agent-context-feeds.md))
requires the code-host and Jira read feeds. Modularity/extensibility — an
explicit BG-0001 constraint — is realized here as contracts.

## Scope

**In:** Jira connector — create/update projections (title, summary, status,
doc link, ID custom field), detect drift (webhook and/or poll), reconcile
toward canon, redirect editors to the Groundwork UI; code-host connector
contract — read-only repo browsing/search for agent context, uniform across
Bitbucket and GitHub; auth provider contract — stable person identifiers for
attribution ([DEC-0024](../decisions/DEC-0024-pluggable-auth.md)), simple
email/OIDC reference implementation; connector registry/configuration.

**Out:** what the agent does with context (EP-0002); writing to codebases
(out entirely — implementation is the swarm's job, per
[DEC-0014](../decisions/DEC-0014-docs-are-the-product.md)).

## Domain Context

Bounded context: **Integration**. Terms: Connector, Projection, Drift — per
[CONTEXT.md](../../CONTEXT.md).

## Interfaces & Contracts to Define

- **Jira connector contract**: projection sync operations + drift events.
- **Code-host connector contract**: list/read/search, provider-neutral.
- **Auth provider contract**: authenticate, identify (stable ID), role
  claims handed to the Governance engine (EP-0003).

## Risks & Open Questions

- Jira deployment specifics (Cloud vs. Data Center, available webhooks,
  custom-field provisioning) — explicitly deferred at SES-0001 T14;
  candidate spike when this epic is refined.
- Drift reconciliation UX: how a Jira-side editor is redirected without
  losing their intended change.

## Derived Work

None yet — stories/spikes follow refinement and approval of this epic.
