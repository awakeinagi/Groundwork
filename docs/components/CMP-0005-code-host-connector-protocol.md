---
id: CMP-0005
type: component
title: Code-Host Connector Protocol
status: draft
owner: eng-lead
created: 2026-07-08
context: integration
component-type: protocol
links:
  derives-from: [EP-0005]
  satisfies: [BG-0001]
---

# CMP-0005: Code-Host Connector Protocol

## Purpose

The capability seam every host interaction crosses: operation contracts
for fork/branch/PR orchestration, reviews, check administration, team
administration, and allowlisted read access; the capability-manifest
schema with the documented minimum set; the normalized host-event
schema; and the conformance suite any adapter — the local-git fake
included — must pass. The standalone `protocol`-type CMP promised by
[DEC-0080](../decisions/DEC-0080-hybrid-component-granularity.md) and
bound by [CMP-0001](CMP-0001-artifact-store-service.md)'s
forward-declared consumption list
([DEC-0132](../decisions/DEC-0132-connector-consumption-forward-declared.md)).

## Pending — Ubiquitous Language

Resolved as contracts are drafted from the approved stories.

## Pending — Design Elements

Element decomposition follows story approval
([ST-0019](../stories/ST-0019-code-host-connector-protocol.md),
[ST-0023](../stories/ST-0023-read-only-context-access.md)).

## Pending — Component Invariants

## Pending — Implementation Guidance

## Pending — Dependencies

Consumers, not dependencies, dominate this seam:
[CMP-0001](CMP-0001-artifact-store-service.md) (branch/PR/result
posting, per [DEC-0132](../decisions/DEC-0132-connector-consumption-forward-declared.md))
and [CMP-0004](CMP-0004-governance-gate-engine.md) (registration,
protection, teams, per
[DEC-0142](../decisions/DEC-0142-gate-engine-owns-check-registration.md)).
Exact consumed sections declared at contract time.

## Pending — Acceptance & Test Expectations

## Pending — Out of Scope
