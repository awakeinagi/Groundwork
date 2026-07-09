---
id: DEC-0285
type: decision
title: Overviews are derived, non-normative content — never citable, body wins, regenerable
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0053 @ T4-T5"
overview: >-
  The overview: field is derived convenience in the same class as
  consolidations: never citable as provenance, the body always wins on
  conflict, and it is freely regenerable. Because adding or correcting
  an overview adds no ratified meaning, closed sessions and accepted
  decisions may receive one without violating immutability — the same
  principle as DEC-0248's cross-reference enrichment carve-out. This is
  what makes the whole-corpus retrofit (DEC-0291) legal without
  per-artifact re-gating.
links:
  derives-from: [SES-0053]
  relates-to: [DEC-0248, DEC-0017]
---

# DEC-0285: Overviews Are Derived, Non-Normative Content

## Context

An overview is a second copy of an artifact's meaning. If it were
ratified content, every overview edit to an approved artifact would be
a semantic change requiring a session, and closed sessions and
accepted decisions — immutable — could never receive one
retroactively, blocking any retrofit.

## Decision

Overviews are **derived, non-normative** content, in the same class as
consolidations (DEC-0017): never citable as provenance, the body
always wins on any conflict, freely regenerable. Adding or correcting
an overview alters no recorded meaning; it is therefore legal on
closed sessions and accepted decisions, does not trigger staleness or
re-gating, and needs no supersession machinery.

## Rationale

This is the same principle behind DEC-0248's cross-reference
enrichment carve-out: additions that surface or summarize
already-ratified content without altering it are not semantic changes.
Making overviews normative would buy stronger guarantees for agents
acting on overviews alone, at the cost of making the field effectively
unretrofittable and every future touch heavyweight — the wrong trade
for a token-efficiency device whose failure mode (a stale overview) is
recoverable by opening the body.

## Alternatives Considered

- **Normative, gate-checked summary** — stronger read-alone
  guarantees; rejected: freezes immutable artifacts out of coverage
  and turns every overview tweak into a session.

## Implications

The retrofit (DEC-0291) proceeds by generation without per-artifact
ratification. Overviews are excluded from provenance rules — a
contract line citing an overview is invalid. Accuracy is kept by
process, not ratification (DEC-0288). Unlike consolidations, overviews
carry no source-pinning; drift is a bug, not corruption.
