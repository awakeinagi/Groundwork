---
id: DEC-0246
type: decision
title: Derived-work completeness is a blocking checker rule
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Every artifact whose derives-from names a business goal or epic must
  reference each child by bare ID in that parent's body. This is a
  blocking rule in tools/check_links.py, failing pre-commit like broken
  links. Derivation playbooks gain an explicit step: deriving a child
  updates the parent's Derived Work section in the same edit. Matches
  the 92–100% existing convention across the corpus; enforcement is
  mechanical per DEC-0242's notation.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0049 @ T1-T2, T6-T7, T10-T11"
links:
  derives-from: [SES-0049]
  relates-to: [DEC-0092, DEC-0094, DEC-0242]
---

# DEC-0246: Derived-Work Completeness Is a Blocking Checker Rule

## Context

EP-0008, SP-0006, and SP-0007 all carry `derives-from: [BG-0001]`, yet
BG-0001's Derived Work section listed none of them; EP-0006 likewise
omitted its late-derived stories ST-0051..ST-0055. Derivation is
recorded one-directionally in the child's frontmatter, and no checker
rule required the parent's body to acknowledge its children — the
Derived Work section was unchecked prose. Every gap instance traces to
late derivation: the child was created after the parent's Derived Work
list was written, and no playbook step said to go back.

## Decision

Every artifact whose `derives-from` names a business goal or an epic
must be referenced by bare ID in that parent's body. This is a
blocking rule in `tools/check_links.py` (and the skill's bundled
copy), failing the pre-commit check exactly like a broken link. The
derivation playbooks gain an explicit step: deriving a child updates
the parent's Derived Work section in the same edit.

## Rationale

The convention already held at 92–100% across the corpus — its
exceptions were documentation gaps, not style variance. The check is
purely mechanical (bare-ID presence per DEC-0242's notation), and it
is symmetric with the existing element↔story reciprocity rule
(DEC-0092's Implements lines, DEC-0094's reciprocity check): both
enforce that a parent-side inventory acknowledges child-side claims.

## Alternatives Considered

- **Non-blocking warning**: gaps stay visible but accumulate; the
  EP-0006 case shows five accumulated in one epic already.
- **Graph audit only**: caught only when someone runs the periodic
  audit — exactly the failure mode that let EP-0008 go unnoticed.

## Implications

BG-0001 and EP-0006 are enriched with the missing entries (sanctioned
by DEC-0248, no re-gating). `check_links.py` gains the rule in both
copies; refinement-process.md derivation playbooks gain the update
step; the graph's `gaps` audit mirrors the query (DEC-0251).
