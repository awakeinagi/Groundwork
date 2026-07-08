---
id: CMP-0006
type: component
title: Bitbucket Data Center Connector
status: draft
owner: eng-lead
created: 2026-07-08
context: integration
links:
  derives-from: [EP-0005]
  satisfies: [BG-0001]
  depends-on: [CMP-0005]
---

# CMP-0006: Bitbucket Data Center Connector

## Purpose

The v1 reference adapter of the
[code-host connector protocol](CMP-0005-code-host-connector-protocol.md):
Bitbucket Data Center REST and webhook integration, an honest
capability manifest, merge checks / Code Insights as the
required-check surface, reviewer groups for team routing
([DEC-0050](../decisions/DEC-0050-bitbucket-datacenter-v1.md)).

## Pending — Ubiquitous Language

## Pending — Design Elements

Element decomposition follows story approval
([ST-0020](../stories/ST-0020-bitbucket-data-center-connector.md),
[ST-0023](../stories/ST-0023-read-only-context-access.md)) and
[SP-0004](../spikes/SP-0004-bbdc-required-check-surface.md) findings.

## Pending — Component Invariants

## Pending — Implementation Guidance

## Pending — Dependencies

Implements [CMP-0005](CMP-0005-code-host-connector-protocol.md); exact
consumed sections declared at contract time.

## Pending — Acceptance & Test Expectations

Conformance to [CMP-0005](CMP-0005-code-host-connector-protocol.md)'s
suite is the headline expectation
(per [DEC-0079](../decisions/DEC-0079-local-git-fake-connector.md),
[DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md)).

## Pending — Out of Scope
