---
id: DEC-0139
type: decision
title: App database port operations carry a full failure contract — stale leases, dead-lettering, crash atomicity, typed errors
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  App database port contract defines failure semantics: stale lease —
  ack/nack with expired or unknown lease fails with typed error, event
  remains claimable; retry exhaustion — after configurable max failed
  deliveries event parks in dead-letter state, visible and never silently
  dropped; crash atomicity — crash mid-UnitOfWork leaves no partially
  visible state, verified by conformance suite failure injection; typed
  error conditions per operation enumerate in contract. Guesses about failure
  paths differ per engine; conformance suite exists to prevent them.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0024 @ T4-T5"
links:
  derives-from: [SES-0024]
  relates-to: [DEC-0103, DEC-0129, DEC-0131]
---

# DEC-0139: Port Operation Failure Semantics

## Context

The SES-0024 audit
judge flagged that CMP-0003
defined no failure semantics for port operations — an adapter author
holding only the contract could not know what a conforming adapter does
on an expired lease, exhausted retries, or a crash mid-transaction.

## Decision

The app database port contract defines:

1. **Stale lease** — `ack`/`nack` with an expired or unknown lease
   fails with a typed error; the event remains (or becomes again)
   claimable. Safe under at-least-once delivery because consumers are
   idempotent by contract.
2. **Retry exhaustion** — after a configurable maximum of failed
   deliveries an event parks in a **dead-letter state**, visible
   through the bookkeeping surface and never silently dropped;
   replay-from-git remains the ultimate recovery path.
3. **Crash atomicity** — a crash mid-UnitOfWork leaves no partially
   visible state; verified by the conformance suite's failure
   injection.
4. **Typed error conditions per operation** — each port operation
   enumerates its error conditions in the contract as in-process typed
   errors (the HTTP problem+json model of
   DEC-0127 governs the API
   surface, not the port).

## Rationale

Every failure path above is otherwise an adapter-author guess, and the
guesses differ per engine — exactly what a conformance-suite-defined
port exists to prevent.

## Alternatives Considered

- **Document at-least-once implications only** — cheaper; rejected
  because it leaves conforming behavior undefined on the paths that
  distinguish adapters.

## Implications

An adapter author holding only the AppDatabasePort contract can now determine conforming behavior on an expired lease, exhausted retries, or a crash mid-transaction, rather than having to guess — the gap the SES-0024 audit judge flagged in CMP-0003. The conformance suite's failure injection verifies crash atomicity, and the dead-letter state added for retry exhaustion is visible through the bookkeeping surface, with replay-from-git remaining the ultimate recovery path. Because per-operation typed error conditions are enumerated in the contract, the HTTP problem+json model of DEC-0127 continues to govern only the API surface, not the port itself. (skeleton restored at SES-0078)
