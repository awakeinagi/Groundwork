---
id: DEC-0433
type: decision
title: "Skill-mode is the paradigm's core subset; parity is tracked in a maintained matrix"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-12
source-span: "SES-0082 T10, T11, T18, T21, T31"
accepted-in: SES-0082
overview: >-
  Skill-mode capability is the paradigm's core subset; the
  application is a superset — anything achievable in skill-mode is
  achievable in the application with the same corpus outcome, and
  application-only features are additive, never altering corpus
  semantics. A parity/asymmetry matrix is a maintained markdown
  document reviewed at releases, not automation.
links:
  derives-from: [SES-0082]
  relates-to: [BG-0001, BG-0002, DEC-0310]
---

# DEC-0433: Skill-mode is the paradigm's core subset; parity is tracked in a maintained matrix

## Context

With the paradigm and application delineated (DEC-A) and skill-mode confirmed permanent (DEC-B), SES-0082 needed to state precisely how the two relate functionally — what a stakeholder or adopter can rely on being true of both — and how that relationship stays true as the application gains features over time.

## Decision

Skill-mode capability is the paradigm's core subset and the application is a superset: anything achievable in skill-mode is achievable in the application with the same corpus outcome, and application-only features are additive and never alter corpus semantics. The parity and asymmetry matrix is a maintained markdown document reviewed at releases, not automation.

## Rationale

Stating skill-mode as the core subset gives every corpus-semantics decision (gate rules, integrity checks, ID allocation) a single place to be defined once and inherited by the application, consistent with DEC-D's single-engine ruling. Keeping the parity matrix as a reviewed markdown document rather than an automated conformance suite matches the current scale of the project — automation here would be built ahead of any real drift problem to detect.

## Alternatives Considered

Allowing the application to define its own additional corpus semantics beyond what skill-mode supports was rejected — it would break the "same corpus outcome" guarantee this decision exists to make, and would let the application silently diverge from the paradigm DEC-B says it's built on. Automating parity verification (a conformance test suite run in CI) was considered and set aside for now as disproportionate to current need; it can be revisited once the application backend actually exists to test against.

## Implications

A parity-and-asymmetry matrix document needs to be created and reviewed at each release once the application exists. Application feature proposals must be checked against this decision — additive UI/workflow features are fine, features that change what's achievable or what a corpus outcome means are not.
