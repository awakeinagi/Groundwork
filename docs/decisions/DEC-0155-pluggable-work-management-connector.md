---
id: DEC-0155
type: decision
title: Work management is a pluggable connector family; Jira Data Center is the reference adapter
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Work management generalizes to a pluggable connector family with
  host-agnostic, capability-declaring contract (DEC-0045 pattern
  applied to work management) owning projection lifecycle, drift
  capture, and backlog read feed. Jira Data Center (confirmed deployed
  flavor) is the reference adapter. Future adapters (monday.com,
  OpenProject, Jira Cloud) validate against the same contract.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0026 @ T6-T7"
links:
  derives-from: [SES-0026]
  relates-to: [DEC-0050, DEC-0045, DEC-0013]
---

# DEC-0155: Pluggable Work-Management Connector; Jira DC Confirmed

## Context

EP-0005 recorded an open
assumption: Jira Data Center (self-hosted Atlassian stack, per
DEC-0050's rationale). Asked to
confirm, the sponsor confirmed the flavor **and** amended the framing:
the agile work-management system must not be a Jira-shaped foundation.

## Decision

The "Jira connector" generalizes to a **work-management connector**
family: a host-agnostic, capability-declaring contract (the
DEC-0045 pattern applied
to work management) owning projection lifecycle, drift capture, and the
backlog read feed. **Jira Data Center — confirmed as the deployed
flavor — is the reference adapter.** Future adapters (monday.com,
OpenProject, Jira Cloud) validate against the same contract.

## Rationale

The sponsor's modularity principle applied consistently: the code host
got a host-agnostic contract for exactly this reason, and the
work-management side deserves the same seam rather than Jira semantics
hard-coded into core.

## Alternatives Considered

- **Jira-specific connector** (the epic's original wording): simpler v1
  surface, but swapping work-management systems later would mean core
  changes, not a new adapter.

## Implications

The deferred release-2 stories are drafted against the generic contract
with Jira DC as reference; DC webhook/event capability validation
happens at their revival. Additional work-management adapters are
future work captured per
DEC-0156. The
glossary gains **Work-Management Connector**; prior "Jira connector"
phrasing in earlier artifacts reads as the Jira DC adapter of this
family.
