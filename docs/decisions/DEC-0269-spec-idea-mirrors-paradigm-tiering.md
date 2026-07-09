---
id: DEC-0269
type: decision
title: SPEC-idea mirrors the paradigm's Idea semantics — tier-1 validates shape, cross-artifact rules are tier-2
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
overview: >-
  DEC-0269 constrains SPEC-idea to mirror the paradigm's Idea semantics
  exactly: tier-1 validation at store write time covers schema-expressible
  shape (prefix, directory, statuses, required fields, rejection of
  release/gate), while tier-2 validation at PR time covers cross-artifact
  rules (spawning session cross-references, take-up derivation, decline
  rationale). Divergence is a conformance bug; the paradigm's semantics
  are already accepted.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0051 @ T6-T7"
links:
  derives-from: [SES-0051]
  relates-to: [DEC-0258, DEC-0259, DEC-0261]
---

# DEC-0269: The SPEC-idea contract and its validation tiers

## Context

The application needs a normative spec for the Idea artifact
(SPEC-idea.md) and a decision on which of its rules the store enforces
at write time (tier-1) versus at PR time (tier-2).

## Decision

SPEC-idea mirrors the paradigm's semantics exactly (DEC-0258,
DEC-0259, DEC-0261): prefix `IDEA`, directory `docs/ideas/`, statuses
`captured → taken-up | declined`, required `proposed-by`,
`derives-from` naming the spawning session when there is one, and
`release:`/gate fields rejected outright. Schema-expressible shape is
**tier-1** (a nonconforming write never reaches the repo).
Cross-artifact rules — the spawning session cross-references the Idea,
the take-up session derives from it, decline requires rationale in the
Disposition section — are **tier-2/PR checks**.

## Rationale

Divergence between the skill's checker and the application's validator
is a conformance bug by definition — the paradigm's semantics are
already accepted, so the app inherits rather than re-decides them. The
tiering follows the established logic: cross-artifact obligations may
be satisfied by a later edit in the same branch, exactly why
reciprocity and release cross-file validity are tier-2 today.

## Alternatives Considered

- **Tier-1 shape only, no tier-2 rules**: the app would accept corpora
  the paradigm's checker rejects.
- **Everything tier-1**: rejected for the same-branch-later-edit
  reason that keeps reciprocity out of tier-1.

## Implications

SPEC-artifact-common's prefix list and type enum gain IDEA; the
tier-2 rule catalog (ST-0007's family) gains the Idea cross-artifact
rules when next amended — noted, not executed here.
