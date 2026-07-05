---
id: DEC-0018
type: decision
title: Python backend + TypeScript frontend; all specs language-agnostic
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-05
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-05
source-span: "SES-0001 @ T8-T9"
links:
  derives-from: [SES-0001]
---

# DEC-0018: Python backend + TS frontend; language-agnostic specs

## Context

The standalone application ([DEC-0001](DEC-0001-standalone-application.md))
needs a reference stack, and the organization's engineers and data scientists
live in Python.

## Decision

Reference implementation: Python backend (agent layer on the Claude Agent
SDK) with a TypeScript frontend. Additionally — and as a hard requirement —
Groundwork's own design specifications must be detailed and
language-agnostic, such that the backend, frontend, agents, and connectors
can be rebuilt in different languages and frameworks as needed.

## Rationale

Meet the org where it lives (Python) without coupling the system's identity
to a stack: the specs, contracts, and artifact formats are the durable
product; implementations are replaceable.

## Alternatives Considered

- **TypeScript full-stack** (agent's recommendation): one language across UI
  and contracts, but misaligned with the org's skills.

## Implications

Contracts are expressed in language-neutral forms (JSON Schema, OpenAPI);
this requirement is itself a test the dogfooded specs
([DEC-0019](DEC-0019-full-dogfood.md)) must pass.
