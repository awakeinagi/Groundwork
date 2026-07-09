---
id: DEC-0253
type: decision
title: A crisply defined mechanical floor exempts zero-semantic-content fixes from sessions
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
overview: >-
  Changes with zero semantic content—typo/spelling fixes, formatting,
  broken-link or reference repair—are mechanical fixes: they skip the
  session requirement and are committed directly with descriptive
  messages; git history is their audit trail. Alters no meaning, touches
  no contract line, decision text, status, approval field, or frontmatter
  link semantics. When in doubt it is semantic and requires a session.
  Keeps mandatory-session rule credible without trivial process burden.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0050 @ T10-T11"
links:
  derives-from: [SES-0050]
---

# DEC-0253: The mechanical-fix floor

## Context

If every instructed change requires a session (DEC-0252), does a typo
fix? A floor was needed that keeps the mandatory-session rule credible
without taxing trivia.

## Decision

Changes with zero semantic content — typo/spelling fixes, formatting,
broken-link or reference repair — are **mechanical fixes**: they skip
the session requirement and are committed directly with a descriptive
message; git history is their audit trail. Definition: a mechanical
fix alters no meaning and touches no contract line, decision text,
status, approval field, or frontmatter link semantics. The tiebreak is
categorical: **when in doubt, it is semantic** and requires a session.

## Rationale

Process pain is how paradigms get abandoned; a session record per typo
trains users to resent — then bypass — the method. The existing
sanctioned edits (reference-formatting, cross-reference enrichment per
DEC-0248) already establish that meaning-preserving edits are a safe
category.

## Alternatives Considered

- **Mechanical fixes get a CP (triage: mechanical), no session**:
  stronger audit trail, but a CP artifact per typo is ceremony without
  provenance value beyond the commit message.
- **No floor**: maximally consistent, practically corrosive.

## Implications

AGENTS.md's "mechanical, non-design edits" wording is subsumed by this
sharper definition. CP triage's `mechanical` outcome remains for
out-of-band-sourced fixes (the CP is the capture, the fix is the
disposition) — the floor here covers live instruction.
