---
id: DEC-0315
type: decision
title: Per-operation invariant validation with targeted re-checks; the full checker stays the pre-commit gate
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0057 @ T10-T11"
overview: >-
  Each write operation enforces its own preconditions — immutability
  (accepted DECs, closed sessions), status-transition legality, link
  reciprocity, SPEC shape of what it writes — and after writing
  re-validates only the artifacts it touched. The full
  check_links.py integrity suite remains the pre-commit gate, not a
  per-write cost. Chosen over running the whole checker on every
  write (slow on a 476-artifact corpus; surfaces pre-existing
  warnings on unrelated writes) and over preconditions-only with no
  post-write re-validation (misses composition effects on the touched
  artifacts). Errors are precise and name the sanctioned alternative
  where one exists.
links:
  derives-from: [SES-0057]
  relates-to: [DEC-0312, DEC-0313, DEC-0130]
---

# DEC-0315: Per-Operation Invariants with Targeted Re-Checks

## Context

Guardrail depth had to be fixed: how much validation does each write
operation run, given the checker already gates every commit?

## Decision

Operations enforce their own preconditions and re-validate only the
artifacts they touched; `check_links.py` in full remains the
pre-commit gate. Errors are precise, naming the violated invariant
and the sanctioned alternative where one exists.

## Rationale

Fast writes with precise errors; the expensive corpus-wide
composition check runs once per commit where it already lives, not
once per operation.

## Alternatives Considered

- **Full checker on every write** — strongest but slow and noisy;
  rejected.
- **Preconditions only** — misses post-write composition effects on
  touched artifacts; rejected.

## Implications

The write scripts share validation logic with check_links.py's rules
(single implementation in the parsing core, not a re-implementation)
— a build constraint for DEC-0322. Prior art: DEC-0130 established
the same discipline product-side — typed operations and their
validator consume one shared allowlist/rules asset so writer and
checker cannot fork; the build follows that shape.
