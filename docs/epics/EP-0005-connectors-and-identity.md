---
id: EP-0005
type: epic
title: Connectors & Identity
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-05
links:
  derives-from: [BG-0001]
  satisfies: [BG-0001]
  depends-on: [EP-0001, EP-0003]
  impacts: [EP-0001, EP-0002, EP-0006, EP-0008]
  impacted-by: [EP-0001, EP-0003]
cites: [DEC-0002, DEC-0013, DEC-0016, DEC-0024, DEC-0026, DEC-0028, DEC-0032,
        DEC-0036, DEC-0043, DEC-0044, DEC-0045, DEC-0046, DEC-0047, DEC-0048,
        DEC-0049, DEC-0050, DEC-0075, DEC-0132, DEC-0142, DEC-0148, DEC-0149,
        DEC-0150, DEC-0151, DEC-0152, DEC-0153, DEC-0154, DEC-0155, DEC-0156,
        DEC-0172, DEC-0173]
---

# EP-0005: Connectors & Identity

## Summary

The pluggable boundary adapters: the code-host connector (fork/branch/PR
orchestration, delegated reviews, branch-protection and team
administration, read-only context access), the Jira connector (projection
sync, drift capture, workflow telemetry), and identity (auth providers,
the person registry, OAuth linkage). Each sits behind a capability-declaring
contract so implementations are swappable; v1 targets GitHub (cloud),
with Bitbucket Data Center deferred to backlog behind trigger
`TRG-0010`
(per DEC-0172,
supersedes DEC-0050).

## Why (Goal Alignment)

BG-0001 outcome 5 (sync without drift) is the Jira connector
(DEC-0002,
DEC-0044); the
PR gate itself now runs through the code-host connector
(DEC-0028,
DEC-0032); the agent's
existing-context awareness rides its read operations
(DEC-0016,
DEC-0049).

## Scope

**In** (refined at SES-0005):

- **Code-host connector** (DEC-0045):
  operations for fork/branch/worktree push, PR open/merge/review-state,
  review posting (per-user OAuth and program-user paths, per
  DEC-0043),
  branch-protection and team/required-check administration (consumed by
  EP-0003's policy compiler), read-only browse/search filtered by the
  `governance/repos.yaml` allowlist (DEC-0049),
  and a capability manifest with a documented minimum set. v1
  implementation: **GitHub (cloud)**; Bitbucket Data Center deferred to
  backlog
  (DEC-0172,
  supersedes DEC-0050).
- **Work-management connector** (generalized from "Jira connector" per
  DEC-0155;
  release-2 scoped per
  DEC-0148):
  host-agnostic contract with Jira Data Center as reference adapter;
  projection created on first merge to main; split
  field ownership — content canonical-owned, workflow Jira-owned read as
  projection-side telemetry (DEC-0048,
  DEC-0151);
  drift detection with before/after capture; revert + Change Proposal
  creation (DEC-0044,
  DEC-0047); editor
  redirection comments; the agent's backlog read feed
  (DEC-0016).
- **Notifier connector** (added per
  DEC-0075/DEC-0149,
  amendment re-affirmed with the story-derivation gate): the delivery
  contract under the in-app notification center, plus the v1 email
  adapter.
- **Identity**: pluggable auth providers
  (DEC-0024);
  `governance/people.yaml` person registry with stable person-ids
  (DEC-0046); per-user OAuth
  host-identity linkage (tokens in the service secret store, never the
  repo); role-claims resolution for the gate engine.

**Out:** gate policy logic (EP-0003 — this epic executes its compilation
requests); CP triage (EP-0002 — the agent triages what this epic captures);
what the agent does with read context (EP-0002); writing to codebases
(out entirely, per DEC-0014).

## Domain Context

Bounded context: **Integration**. Terms: Connector, Projection, Drift,
Change Proposal — per [CONTEXT.md](../../CONTEXT.md).

## Interfaces & Contracts to Define

- **Code-host connector contract** + capability manifest schema + the
  minimum capability set (CMP-level) — bound by
  CMP-0001's
  forward-declared consumption list
  (DEC-0132)
  and the gate engine's registration/administration operations
  (DEC-0142).
- **Work-management connector contract**: projection operations,
  field-ownership map, drift events with diffs, backlog read,
  projection-side telemetry
  (DEC-0155,
  DEC-0151).
- **Notifier connector contract**: delivery operations, capability
  manifest, channel preferences
  (DEC-0075).
- **Auth provider contract**: authenticate → auth subject; person-id
  resolution against the registry; role claims for EP-0003.
- **Person registry schema**: `governance/people.yaml` (tier-1 validated;
  schema owned by ST-0012).
- **Attribution block schema**: the service-signed program-user review
  attribution (DEC-0153).
- **CP creation operation**: the typed write connectors use to file
  proposals (DEC-0033).

## Risks & Open Questions

All four recorded risks were resolved at story derivation
(SES-0026):

- BBDC required-check surface → spike
  SP-0004
  (DEC-0150).
  Moot for v1 since SES-0031:
  GitHub, not BBDC, is v1
  (DEC-0172), and
  GitHub's documented Checks API/required-status-checks already support
  the semantics the spike would have validated
  (DEC-0173).
  ST-0020 and
  the spike are deferred together, reviving on trigger `TRG-0010`.
- Jira flavor → confirmed Data Center, generalized to a pluggable
  work-management contract
  (DEC-0155);
  DC webhook/event validation happens when the release-2 stories revive.
- Program-user attribution → service-signed attribution block
  (DEC-0153).
- Bootstrap identity migration → criterion 5 of
  ST-0022.

## Derived Work

Derived at SES-0026:

- Current release:
  ST-0019 (connector
  protocol & capability manifest),
  ST-0031 (GitHub connector,
  per SES-0031, took
  ST-0020's
  former slot),
  ST-0021
  (delegated reviews & attribution),
  ST-0022
  (identity & person resolution),
  ST-0023 (read-only
  context access),
  ST-0024
  (notifier contract & email adapter).
- Release 2 (deferred per
  DEC-0148):
  ST-0025,
  ST-0026,
  ST-0027.
- Backlog, trigger-subscribed (per
  DEC-0156,
  DEC-0152,
  DEC-0172):
  ST-0020 (BBDC
  connector, deferred from current release; trigger `TRG-0010`),
  ST-0028,
  ST-0029,
  ST-0030;
  spikes
  SP-0004 (trigger
  `TRG-0010`),
  SP-0005.
- Component stubs:
  CMP-0005,
  CMP-0006
  (BBDC, dormant alongside its deferred story),
  CMP-0009 (GitHub, v1),
  CMP-0007,
  CMP-0008.
