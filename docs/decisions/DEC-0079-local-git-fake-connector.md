---
id: DEC-0079
type: decision
title: A local-git fake connector implements the code-host contract for development and CI
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0011 @ T2-T3"
links:
  derives-from: [SES-0011]
---

# DEC-0079: Local-git fake connector

## Context

ST-0003's branch/PR orchestration consumes the code-host connector
contract, but the real Bitbucket Data Center connector ships with EP-0005
— and requiring a BBDC instance in every dev/CI loop would couple store
development to external infrastructure.

## Decision

Build a fake connector implementing the full code-host contract —
capability manifest included — against a local bare repository: branches
are real git; PRs, reviews, and required checks are simulated in local
metadata. The store pipeline (and later the gate engine) develops and
CI-tests hermetically against it. The fake is a permanent test double, not
throwaway scaffolding.

## Rationale

Hermetic CI from day one, contract-first design pressure (the contract is
exercised as a whole before any host exists), and the BBDC connector's
later swap-in becomes the first real validation of connector pluggability
([DEC-0045](DEC-0045-capability-declaring-connectors.md)).

## Alternatives Considered

- **BBDC connector first**: couples all development to a BBDC instance;
  one host's quirks drive the contract.
- **Ad-hoc per-test stubs**: the contract is never exercised whole until
  the worst possible moment.

## Implications

The fake connector is a deliverable within ST-0003's scope; its simulated
review/check semantics must track the contract spec, not any particular
host.
