---
id: DEC-0167
type: decision
title: The code-host connector protocol adopts typed error conditions and natural-key idempotency per operation
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Every CMP-0005 operation enumerates typed error conditions (not-found,
  permission-denied, conflict, capability-unsupported, rate-limited)
  that adapters map host-native errors onto; no host-specific exception
  crosses the seam. Creation operations with natural key (fork, branch,
  PR) are idempotent on that key: retrying succeeds returns existing
  resource rather than erroring or duplicating.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0030 @ T1"
links:
  derives-from: [SES-0030]
  relates-to: [DEC-0129, DEC-0139, DEC-0045]
---

# DEC-0167: Connector Typed Errors and Idempotency Convention

## Context

CMP-0003 (App Database
Port) established a precedent for infrastructure/integration seams:
every operation enumerates typed error conditions in the contract
rather than leaking engine-specific exceptions
(DEC-0129,
DEC-0139).
CMP-0005
needed the same question answered for host-facing operations, plus a
retry story: orchestration calls (fork/branch/PR creation) can be
retried after an ambiguous network failure, and the contract must say
what a conforming adapter does.

## Decision

Every CMP-0005
operation enumerates a closed set of typed error conditions drawn from
a shared vocabulary — `not-found`, `permission-denied`, `conflict`,
`capability-unsupported`, `rate-limited` — that adapters map their
host-native errors onto; no host-specific exception type crosses the
seam. Creation operations with a natural key (fork provisioning, branch
create, PR open) are idempotent on that key: retrying a call that
already succeeded returns the existing resource rather than erroring or
duplicating.

## Rationale

Extends CMP-0003's
proven pattern to the connector seam rather than inventing a second
convention; `capability-unsupported` additionally gives the
capability-manifest mechanism
(DEC-0045)
a concrete failure mode when a caller invokes an above-minimum
operation the manifest didn't declare. Natural-key idempotency is
necessary because host orchestration calls are the one place in the
system where a caller cannot simply consult the Canonical Store to
learn whether an ambiguous prior attempt succeeded.

## Alternatives Considered

- **Adapter-discretion error handling** — faster to draft, but leaves
  every consumer (CMP-0001,
  CMP-0004) guessing
  per-adapter failure shapes, exactly what the port precedent exists to
  prevent.
- **At-most-once semantics via client-generated request IDs** — stronger
  guarantee, but requires host APIs to accept idempotency keys, which
  BBDC's REST APIs do not uniformly support; natural-key idempotency
  achieves the same practical outcome without that requirement.

## Implications

`CodeHostConnector`'s operation items each list their error conditions;
the conformance suite exercises the closed vocabulary and idempotent
retry behavior (per DEC-0079).
