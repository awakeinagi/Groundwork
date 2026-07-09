---
id: DEC-0129
type: decision
title: The app database port exposes typed operation families; no SQL crosses the seam
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0022 @ T3-T4"
links:
  derives-from: [SES-0022]
  relates-to: [DEC-0103, DEC-0121, DEC-0122]
---

# DEC-0129: AppDatabasePort Typed Operation Families

## Context

"Consumers program against port contracts only"
(DEC-0121) leaves open whether the
port is a typed operation surface or a SQL pass-through.

## Decision

The `AppDatabasePort` contract defines **engine-neutral typed operation
families**: transactional unit-of-work (atomic commit/rollback), outbox
append within a unit of work plus dispatch claim/ack/nack leasing
(DEC-0103), and keyed
operational-bookkeeping records (namespace, key, document). **No SQL
crosses the seam.** The conformance suite
(DEC-0122) tests exactly these
semantics — notably atomicity of write-bookkeeping plus outbox-append.

## Rationale

A typed surface lets any engine with the right semantics adapt — a
KV store could back bookkeeping — while a SQL port restricts adapters
to SQL engines and leaks dialect drift through the seam, degenerating
the conformance suite into SQL-compatibility testing.

## Alternatives Considered

- **SQL-level port** ("execute SQL in a transaction") — maximum
  consumer flexibility, minimum seam integrity. Rejected.
