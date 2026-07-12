---
id: DEC-0380
type: decision
title: "Session close requires complete identity frontmatter"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0072 @ T20-T21"
overview: >-
  The set-status closed transition refuses while participant,
  participant-role, facilitator, or transcript-fidelity is missing —
  the SES-0070 close-out gap (all four missing on a committed closed
  session) cannot recur. Documented in SPEC-session's lifecycle
  section.
links:
  derives-from: [SES-0072]
---

# DEC-0380: Session close requires complete identity frontmatter

## Context

SES-0070 was closed and committed with all four identity fields absent; the closed-session immutability gate then correctly blocked ordinary repair.

## Decision

The four identity fields are close preconditions.

## Rationale

A session record without participant/facilitator identity fails its provenance purpose, and post-close repair requires sanctioned direct edits.

## Alternatives Considered

Checker-only enforcement (after the fact); larger required-field sets (kind/intake vary legitimately by session weight).

## Implications

SPEC-session lifecycle documents the gate; close tasks must carry the fields.
