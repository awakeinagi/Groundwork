---
id: CMP-0012
type: component
title: Queue Port
status: draft
owner: eng-lead
created: 2026-07-08
context: platform
component-type: protocol
links:
  derives-from: [EP-0008]
  satisfies: [BG-0001]
  depends-on: [CMP-0003]
---

# CMP-0012: Queue Port

> Standalone `protocol`-type component, mirroring
> [CMP-0003](CMP-0003-app-database-port.md)'s pattern per
> [DEC-0135](../decisions/DEC-0135-graduate-app-database-port.md)
> and extending the Port family per
> [DEC-0203](../decisions/DEC-0203-queue-kv-ports-added.md).

## Purpose

The infrastructure seam for background/async job execution: the
contract any Queue Adapter must satisfy — enqueue / consume /
acknowledge / retry — plus the conformance suite that defines Adapter
validity. Consumers (the background job execution runtime,
[CMP-0013](CMP-0013-background-job-execution-runtime.md)) program
against this contract; adapters conform to it
([ST-0060](../stories/ST-0060-queue-port.md)).

## Pending — Ubiquitous Language

## Pending — Design Elements

Element decomposition mirrors
[CMP-0003](CMP-0003-app-database-port.md)'s `AppDatabasePort`
element: a `QueuePort` protocol element with enqueue/consume/ack/retry
operation families and the outbox-pattern failure semantics
([DEC-0210](../decisions/DEC-0210-queue-port-outbox-pattern-reuse.md)).

## Pending — Component Invariants

## Pending — Implementation Guidance

## Pending — Dependencies

The v1 durable Adapter rides [CMP-0003](CMP-0003-app-database-port.md)
(App Database Port); exact consumed sections declared at contract time.

## Pending — Acceptance & Test Expectations

Conformance to this port's own suite, mirroring
[CMP-0003](CMP-0003-app-database-port.md)'s Acceptance & Test
Expectations pattern, is the headline expectation.

## Pending — Out of Scope
