---
id: DEC-0014
type: decision
title: Docs are the product; swarm orchestration is out of scope
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-05
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-05
source-span: "SES-0001 @ T8-T9"
links:
  derives-from: [SES-0001]
---

# DEC-0014: Docs are the product; swarm orchestration is out of scope

## Context

The pipeline ends with component docs implementable by a swarm of agents.
Groundwork could also dispatch that swarm, track its progress, and ingest
results — or stop at the docs.

## Decision

Groundwork's responsibility ends at approved, contract-complete Component
Docs plus a machine-readable Handoff Manifest (docs, contracts, dependency
order). Swarm orchestration is a separate concern; the manifest is designed
as its API.

## Rationale

Keeps v1 scope sane and the system's identity crisp: Groundwork produces
grounded specifications; other systems build from them.

## Alternatives Considered

- **Swarm orchestration in scope**: the full loop; much bigger build.
- **Feedback loop in scope, dispatch out**: attractive later — PR links and
  implementation learnings flowing back — but not v1.

## Implications

The Handoff Manifest is a formal interface
([SPEC-handoff-manifest](../specs/SPEC-handoff-manifest.md)). A future
feedback-ingestion epic can extend the boundary without moving it.
