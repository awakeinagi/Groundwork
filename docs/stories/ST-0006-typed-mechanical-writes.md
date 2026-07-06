---
id: ST-0006
type: story
title: Typed mechanical write operations and credential separation
status: gated
owner: eng-lead
created: 2026-07-06
links:
  derives-from: [EP-0001]
  satisfies: [BG-0001]
  depends-on: [ST-0002]
  impacted-by: [ST-0002]
cites: [DEC-0033, DEC-0035, DEC-0038, DEC-0047, DEC-0048]
---

# ST-0006: Typed Mechanical Write Operations

## Summary

The mechanical-write surface: the closed set of typed operations through
which system facts (transcript turns, stale marks, Jira telemetry, CPs,
counters) reach the repository, with credential separation making design
changes inexpressible through this path.

## Acceptance Criteria

1. The mechanical operation set is closed and explicit — at minimum
   `append-turn`, `close-session`, `mark-stale`, `clear-stale`,
   `set-jira-key`, `set-jira-status`, `create-change-proposal`,
   `set-cp-triage` — each constructing its commit entirely from typed
   parameters (per DEC-0033, DEC-0035, DEC-0038, DEC-0047, DEC-0048).
2. No mechanical operation can modify artifact body content or non-
   allowlisted frontmatter fields; attempts are rejected structurally, not
   by policy check (per DEC-0033).
3. Agent processes hold no git credentials; only the storage service's
   identity can construct commits (verified by deployment test)
   (per DEC-0033).
4. Where upstream branch protection forbids direct pushes, mechanical
   writes flow through auto-PRs approved by the program user, gated by the
   mechanical-diff validator as a required check (per DEC-0033).
5. Direct-commit vs. auto-PR mode is per-deployment configuration with no
   code change (per DEC-0033).

## Component Impact

[CMP-0001](../components/CMP-0001-artifact-store-service.md) — supplies
the mechanical-write allowlist in its API and Behavior Contracts.

## Out of Scope

The mechanical-diff validator implementation (ST-0007); who *invokes*
mark-stale (Governance engine, EP-0003).

## Notes for Implementers

The allowlist is part of the published API contract — extending it is a
contract change that goes through a gate, never a quiet addition.
