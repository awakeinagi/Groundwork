---
id: DEC-0477
type: decision
title: "The Engine kernel is pure: all I/O flows through ports"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-13
source-span: "SES-0091 @ T4-T5"
overview: >-
  The Engine's API surface needed a layering decision before any
  contract could be shaped. This decision adopts hexagonal layering:
  the kernel (artifact model, ID allocation, validation, gate state,
  rule machinery, parsing, graph-sync and search logic) performs no
  I/O itself; all I/O crosses port contracts implemented by adapters
  outside the kernel, making EP-0012's cross-runtime parity
  checkable and the kernel testable without live stores.
links:
  relates-to: [DEC-0476, DEC-0478]
  derives-from: [SES-0091]
---

# DEC-0477: The Engine kernel is pure: all I/O flows through ports

## Context

The Engine API surface and the runtime-agnostic substrate contract needed a layering decision before any contract surface could be shaped.

## Decision

The Engine follows hexagonal layering. The kernel — the artifact model, ID allocation, validation, gate state, rule machinery, format parsing, and the logic of graph sync and semantic search — performs no filesystem or network I/O itself; all I/O crosses port contracts implemented by adapters outside the kernel.

## Rationale

A pure kernel is what makes EP-0012's cross-runtime parity promise checkable and the kernel unit-testable without live stores; source-code dependencies point only inward.

## Alternatives Considered

A kernel with direct filesystem access is simpler today but binds the Engine to one runtime's I/O model and makes parity a per-runtime reimplementation question.

## Implications

EP-0012 binds parity against port and operation contracts, and the kernel is testable without infrastructure.
