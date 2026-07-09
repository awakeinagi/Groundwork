---
id: DEC-0272
type: decision
title: Idea creation and disposition are typed mechanical-write operations, mirroring the Change Proposal pair
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
overview: >-
  DEC-0272 constrains Idea creation and disposition to typed
  mechanical-write operations joining MechanicalWriteService's closed
  set, mirroring Change Proposals one-to-one: create-idea for gateless
  durable-write capture tier-1-validated against the Idea schema, and
  set-idea-disposition to fill Disposition and flip captured →
  taken-up | declined within allowlist append-regions. Both are
  allowlisted operations under the existing mechanical-write machinery;
  extending the allowlist is the gated contract change.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0051 @ T12-T13"
links:
  derives-from: [SES-0051]
  relates-to: [DEC-0033, DEC-0258]
---

# DEC-0272: The gateless write path for Ideas

## Context

The SES-0051 recall audit's judge flagged a contract gap: CMP-0001's
documented artifact-creation operation (`BranchOrchestrator.A-1`)
universally opens a gate PR and reaches durability on merge — but
Ideas are gateless by design (DEC-0258), and ST-0065 is built around
seconds-long capture. Nothing defined how an Idea write becomes
durable.

## Decision

Idea writes join `MechanicalWriteService`'s closed operation set,
mirroring the Change Proposal pair one-to-one:
`create-idea(idea-document)` is the gateless durable-write path for
capture, tier-1-validated against the Idea schema; and
`set-idea-disposition(idea-id, outcome, rationale)` fills the
Disposition section and flips `captured → taken-up | declined` within
the allowlist's append-regions. Both are allowlisted operations under
the existing mechanical-write machinery (DEC-0033 family); extending
the allowlist is the gated contract change this decision ratifies.

## Rationale

The precedent is exact: CPs are the other reduced-lifecycle artifact,
created gatelessly via `create-change-proposal` with `set-cp-triage`
filling a body section — the same shape Ideas need. Routing Ideas
through the gate-PR path would contradict DEC-0258's gateless
lifecycle; inventing a third write mechanism would duplicate one that
already exists for exactly this case.

## Alternatives Considered

- **Park the gap as a captured Idea for a later session**: leaves
  CMP-0001 approved with a knowingly incomplete contract — failing the
  gate test inside the very session that amended it.
- **Route Idea creation through the gate-PR path**: contradicts the
  accepted gateless lifecycle and destroys capture-in-seconds.

## Implications

CMP-0001's `MechanicalWriteService.A-1..A-10` and the allowlist asset
(`MechanicalWriteService.D-1`) carry the two new operations; ST-0065
AC3's "typed operations" now has a concrete referent. ST-0006's AC1
enumerates the closed operation set and is amended in the same change —
the consistency sweep on this decision surfaced that citer, exactly
the partial-supersession catch it exists for.
