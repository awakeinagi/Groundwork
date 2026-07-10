---
id: DEC-0333
type: decision
title: Git stays with the caller — the librarian validates but never commits
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0058 @ T10-T11"
overview: >-
  The artifact-librarian's task surface ends at the working tree: it
  performs typed writes, runs per-operation validation, and runs the
  full check_links.py suite when a task asks for pre-commit
  assurance — but it never stages, commits, or otherwise touches git.
  Commit discipline (checker-then-commit, at least once per session,
  descriptive messages) stays with the caller — normally the
  facilitator, who owns session boundaries and knows what a commit
  means. Rationale doubles as safety: whole-tree git operations in
  subagents are exactly what the project's parallel-agent discipline
  forbids, and a committing librarian would make parallel read
  fan-outs (DEC-0332) hazardous. Chosen over commit-on-request, which
  saves the caller one step while reintroducing that hazard class.
links:
  derives-from: [SES-0058]
  relates-to: [DEC-0324, DEC-0315, DEC-0332]
---

# DEC-0333: The Caller Commits

## Context

Sessions end with checker-then-commit. With writes delegated, does
the commit delegate too?

## Decision

No. The librarian's surface ends at the working tree — typed writes,
per-op validation (DEC-0315), and the full checker on request. Git
operations (stage, commit, anything else) belong to the caller.

## Rationale

Commits mark session and approval boundaries the caller owns, and
subagents performing whole-tree git operations is the exact hazard
the project's parallel-agent discipline exists to prevent —
especially alongside DEC-0332's parallel read fan-outs.

## Alternatives Considered

- **Commit-on-request** — one step saved, hazard class
  reintroduced; rejected.

## Implications

Librarian task results include a "ready to commit" signal (checker
outcome) so the caller can commit immediately without re-validating.
