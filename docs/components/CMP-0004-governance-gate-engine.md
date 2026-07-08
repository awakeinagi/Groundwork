---
id: CMP-0004
type: component
title: Governance & Gate Engine
status: draft
owner: eng-lead
created: 2026-07-08
context: governance
links:
  derives-from: [EP-0003]
  satisfies: [BG-0001]
  depends-on: [CMP-0001, CMP-0002, CMP-0003]
---

# CMP-0004: Governance & Gate Engine

## Purpose

The rules layer of Groundwork: compiles governance-as-code onto host
branch protection, computes the `gate-policy` and `conflicts-open`
required checks, runs staleness sweeps with re-affirmation flows,
operates the Arbiter conflict queue, and emits the governance event log
with its metrics/query API — the component
[EP-0003](../epics/EP-0003-governance-and-gate-engine.md)'s stories
build.

## Pending — Ubiquitous Language

Resolved as contracts are drafted from the approved stories.

## Pending — Design Elements

Element decomposition follows story approval
([ST-0012](../stories/ST-0012-governance-config-schemas.md)–[ST-0018](../stories/ST-0018-governance-event-log-metrics.md)).

## Pending — Component Invariants

## Pending — Implementation Guidance

## Pending — Dependencies

Consumes [CMP-0001](CMP-0001-artifact-store-service.md) (mechanical
writes, auto-PRs), [CMP-0002](CMP-0002-change-event.md) (recomputation
and sweep triggers), [CMP-0003](CMP-0003-app-database-port.md) (event
log persistence); exact consumed sections declared at contract time.

## Pending — Acceptance & Test Expectations

## Pending — Out of Scope
