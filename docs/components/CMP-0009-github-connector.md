---
id: CMP-0009
type: component
title: GitHub Connector
status: draft
owner: eng-lead
created: 2026-07-08
context: integration
links:
  derives-from: [EP-0005]
  satisfies: [BG-0001]
  depends-on: [CMP-0005]
cites: [DEC-0045, DEC-0079, DEC-0172]
---

# CMP-0009: GitHub Connector

## Purpose

The v1 reference adapter of the
[code-host connector protocol](CMP-0005-code-host-connector-protocol.md):
GitHub (cloud) REST/GraphQL and webhook integration, an honest
capability manifest, the Checks API and required-status-checks as the
required-check surface, CODEOWNERS and org teams for reviewer/team
routing. Takes Bitbucket Data Center's former v1 slot
(per [DEC-0172](../decisions/DEC-0172-github-v1-bbdc-deferred.md); see
[CMP-0006](CMP-0006-bitbucket-data-center-connector.md), now deferred).

## Pending — Ubiquitous Language

## Pending — Design Elements

Element decomposition follows story approval
([ST-0031](../stories/ST-0031-github-connector.md),
[ST-0023](../stories/ST-0023-read-only-context-access.md)).

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
