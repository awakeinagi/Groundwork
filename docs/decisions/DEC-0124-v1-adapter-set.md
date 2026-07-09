---
id: DEC-0124
type: decision
title: v1 ships the embedded storage adapters plus two embedding adapters — local model and REST client
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0020 @ T4-T5, T6-T7"
links:
  derives-from: [SES-0020]
  relates-to: [DEC-0102, DEC-0105, DEC-0121, DEC-0122]
---

# DEC-0124: v1 Adapter Set

## Context

Ports without second adapters are theoretical
(DEC-0121,
DEC-0122), but shipping second
storage adapters in v1 would pull the deferred graduation work
(SP-0002) into
scope, contradicting the embedded-only v1 stance
(DEC-0102).

## Decision

v1 ships:

- **App database port**: DuckDB adapter only.
- **Vector store port**: DuckDB + vss adapter only.
- **Graph store port**: LadybugDB adapter only.
- **Embedding port**: **two adapters** — a local embedding model and a
  REST-API client for external embedding services.

Second adapters for the storage/graph ports arrive with the
SP-0002 graduation
evaluation (DEC-0105);
every v1 adapter passes its port's conformance suite
(DEC-0122).

## Rationale

The embedding port is the swap the participant explicitly named
(local vs. external via REST), the cheapest second adapter to build,
and having two real adapters proves the port pattern end-to-end —
including the identity-stamping machinery of
DEC-0123, which only a model
swap exercises. DEC-0102's
embedded-only v1 storage commitment is unchanged.

## Alternatives Considered

- **Embedded/local defaults only** — leanest, but every port's
  swappability stays theoretical until written under pressure.
- **A second adapter for every port** — maximum confidence; rejected as
  effectively pulling
  SP-0002 into v1.
