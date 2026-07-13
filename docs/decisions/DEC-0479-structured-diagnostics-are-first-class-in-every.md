---
id: DEC-0479
type: decision
title: "Structured diagnostics are first-class in every Engine operation contract"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-13
source-span: "SES-0091 @ T12-T13"
overview: >-
  Operation errors and checker findings could be contracted
  structures or informal prose. This decision makes structured
  diagnostics first-class: every kernel operation contracts typed,
  enumerated failure/finding output (rule ID, artifact, location,
  severity, fix hint for findings; enumerated error kinds for
  failures) as part of the public operation catalog, letting agents
  self-correct without prose parsing.
links:
  relates-to: [DEC-0478]
  derives-from: [SES-0091]
---

# DEC-0479: Structured diagnostics are first-class in every Engine operation contract

## Context

Operation errors and checker findings could be contracted structures or informal prose left to each adapter.

## Decision

Every kernel operation contracts its failure and finding output as typed, enumerated structures — rule ID, artifact, location, severity, and fix hint for checker findings, and enumerated error kinds for operation failures. The structure is part of the public operation catalog.

## Rationale

A contract that only describes success is half a contract. Agents self-correct from typed findings without prose parsing, and observability and adoption reporting consume the same shape.

## Alternatives Considered

Informal prose diagnostics were rejected because every consumer would re-parse text and diagnostics would drift per adapter.

## Implications

The diagnostics schema becomes a declared value contract in the Engine's component docs; the CLI renders it but never defines it.
