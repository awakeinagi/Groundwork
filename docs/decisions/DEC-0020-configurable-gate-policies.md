---
id: DEC-0020
type: decision
title: Gate policies support fixed role-mapping and committee approval
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-05
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-05
source-span: "SES-0001 @ T10-T11"
links:
  derives-from: [SES-0001]
---

# DEC-0020: Gate policies — fixed role-mapping AND committee approval

## Context

Gates at every stage (DEC-0006) need a rule
for who approves what — the governance keystone given unsupervised sessions.

## Decision

The gate engine supports both policies, configurable per artifact type:
(1) fixed role→gate mapping — each artifact type has a default approver role
(Product Owner for goals/epics; Eng/DS Leads for stories, spikes, component
docs), with a specific person auto-assigned per domain/team mapping and
overridable by an Arbiter/Admin; (2) committee gates — a gate requiring
sign-off from multiple roles (e.g., PO + Eng Lead + DS Lead) for
high-stakes transitions.

## Rationale

Different stages carry different risk; goal approval and swarm handoff may
warrant committees while routine story gates flow through a single role.
Building both up front avoids wedging committee semantics into a
single-approver model later.

## Alternatives Considered

- **Per-artifact ad-hoc assignment**: invites approval-shopping and gaps.

## Implications

Roles: Stakeholder, Product Owner, Eng Lead, DS Lead, Arbiter (see
CONTEXT.md). Gate policy is configuration, not code.
