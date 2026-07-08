---
id: ST-0002
type: story
title: Storage service core and OpenAPI contract
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-07
owner: eng-lead
created: 2026-07-06
links:
  derives-from: [EP-0001]
  satisfies: [BG-0001]
  depends-on: [ST-0001]
  impacts: [ST-0003, ST-0004, ST-0005, ST-0006, ST-0008]
  impacted-by: [ST-0001]
cites: [DEC-0018, DEC-0029, DEC-0034, DEC-0035]
---

# ST-0002: Storage Service Core and OpenAPI Contract

## Summary

The storage service's core read/write surface over the application-owned
fork, defined as a language-neutral OpenAPI contract: artifact reads with
ref information, writes routed through tier-1 validation onto the correct
branch, and type-aware write rules.

## Acceptance Criteria

1. Reads return the artifact plus the ref (commit sha) it was read at, and
   accept an optional ref/branch parameter for pinned reads (per [DEC-0029](../decisions/DEC-0029-api-writes-git-reads.md)).
2. Every write path runs tier-1 validation before any commit is
   constructed; failures return the validation library's field-level
   errors (per [DEC-0034](../decisions/DEC-0034-two-tier-validation.md)).
3. The service is the only holder of repository write credentials; no
   other identity can push (verified by host-side permission test)
   (per [DEC-0029](../decisions/DEC-0029-api-writes-git-reads.md), [DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md)).
4. Session artifacts expose only `append-turn` and `close` mutation
   operations; edit/delete of existing turns is unrepresentable in the API
   (per [DEC-0035](../decisions/DEC-0035-store-enforced-append-only-transcripts.md)).
5. The full surface is defined in OpenAPI and published with the spec set;
   a conformance test suite runs against the contract, not the
   implementation (per [DEC-0018](../decisions/DEC-0018-python-backend-language-agnostic-specs.md)).

## Component Impact

[CMP-0001](../components/CMP-0001-artifact-store-service.md) — supplies
its API Contract core.

## Out of Scope

Branch/PR orchestration ([ST-0003](ST-0003-item-branch-pr-orchestration.md)); worktrees ([ST-0004](ST-0004-session-worktree-management.md)); mechanical
operations beyond session append/close ([ST-0006](ST-0006-typed-mechanical-writes.md)); events ([ST-0008](ST-0008-change-event-stream.md)).

## Notes for Implementers

Python reference implementation per [DEC-0018](../decisions/DEC-0018-python-backend-language-agnostic-specs.md), but the OpenAPI contract is
the deliverable of record — write it first.
