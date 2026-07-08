---
id: CMP-0014
type: component
title: KV-Store Port
status: draft
owner: eng-lead
created: 2026-07-08
context: platform
component-type: protocol
links:
  derives-from: [EP-0008]
  satisfies: [BG-0001]
  depends-on: [CMP-0003, CMP-0013]
---

# CMP-0014: KV-Store Port

> Standalone `protocol`-type component, mirroring
> [CMP-0003](CMP-0003-app-database-port.md)'s pattern and extending the
> Port family per
> [DEC-0203](../decisions/DEC-0203-queue-kv-ports-added.md).

## Purpose

The infrastructure seam for ephemeral coordination state and
general-purpose caching: the contract any KV-store Adapter must
satisfy — `get`/`set`/`delete` with TTL — plus the conformance suite
that defines Adapter validity. v1 ships a default Adapter reusing the
App Database Port's DuckDB engine instance
([ST-0062](../stories/ST-0062-kv-store-port.md)).

## Pending — Ubiquitous Language

## Pending — Design Elements

Element decomposition mirrors
[CMP-0003](CMP-0003-app-database-port.md)'s `AppDatabasePort`
element: a `KvStorePort` protocol element with get/set/delete + TTL
operations and lazy-plus-swept expiry semantics
([DEC-0211](../decisions/DEC-0211-kv-store-lazy-expiry-plus-sweep.md)).

## Pending — Component Invariants

## Pending — Implementation Guidance

## Pending — Dependencies

The v1 default Adapter reuses
[CMP-0003](CMP-0003-app-database-port.md)'s DuckDB engine instance
(own table, no shared operations); the periodic expiry sweep runs on
[CMP-0013](CMP-0013-background-job-execution-runtime.md); exact
consumed sections declared at contract time.

## Pending — Acceptance & Test Expectations

Conformance to this port's own suite, mirroring
[CMP-0003](CMP-0003-app-database-port.md)'s Acceptance & Test
Expectations pattern, is the headline expectation.

## Pending — Out of Scope
