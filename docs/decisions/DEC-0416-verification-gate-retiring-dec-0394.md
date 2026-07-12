---
id: DEC-0416
type: decision
title: "Verification gate retiring DEC-0394"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0079 @ T3-T6"
overview: >-
  Defines the concrete test-suite-plus-live-acceptance-run condition
  that must be met before DEC-0394's interim single-writer rule
  expires.
links:
  derives-from: [SES-0079]
  relates-to: [DEC-0391, DEC-0394]
---

# DEC-0416: Verification gate retiring DEC-0394

## Context

DEC-0394 keeps exactly one write-task librarian running at a time as an interim rule, expiring only "when the DEC-0391 implementation is verified" — a condition that decision left unspecified. This session's design gate needs to define what "verified" means concretely, so the retirement isn't a judgment call made informally at build time.

## Decision

DEC-0394's interim single-write-librarian rule expires only when both of the following hold: (1) the new test suite passes in full, covering the reproduced parallel-create race (the SES-0078/SES-0079 H1 collision), shared/exclusive lock semantics, rollback, crash recovery, the section version-token behavior, and the turn-append precondition, plus the existing guard-test regression suite continuing to pass; and (2) one live acceptance run of two genuinely parallel write-task librarians operating against the real corpus finishes with a clean full `check`.

## Rationale

A test-suite-only gate risks a design that passes in isolation but still collides under real concurrent librarian usage patterns the tests didn't anticipate; a live-run-only gate risks shipping without regression coverage for the specific race this whole build exists to close. Requiring both closes each gap the other leaves open, and gives a concrete, checkable stopping condition rather than leaving "verified" to be decided informally when the build feels done.

## Alternatives Considered

Retiring DEC-0394 as soon as the code merges (no explicit verification gate) was rejected — that was the exact ambiguity this decision exists to remove. Requiring only the live acceptance run (skip the reproduced-race regression test) was rejected because a single successful parallel run doesn't prove the race is actually closed, only that it didn't happen to occur that one time.

## Implications

DEC-0394 stays in force as the operative interim rule through this build's entire implementation and initial testing; only after both conditions are met does a follow-up `set-status superseded` (or equivalent) on DEC-0394 become appropriate, and that action belongs to whoever runs the verification, not to this design-gate decision itself.
