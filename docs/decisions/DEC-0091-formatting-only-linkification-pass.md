---
id: DEC-0091
type: decision
title: Formatting-only linkification of immutable artifacts is sanctioned
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
overview: >-
  A mechanical pass converts bare cross-references to markdown links across
  the entire corpus, including closed sessions and accepted decisions, as a
  formatting-only exception to immutability. This edit class—reference
  formatting changing no words, meaning, or structure—is sanctioned for the
  initial pass and future link-integrity repairs. Meaning-touching edits
  remain forbidden. Git history preserves pre-pass text for audit integrity.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0014 @ T2-T3"
links:
  derives-from: [SES-0014]
  relates-to: [DEC-0090]
---

# DEC-0091: Formatting-only linkification of immutable artifacts is sanctioned

## Context

DEC-0090 makes bare body
cross-references integrity violations, but much of the existing corpus —
including closed sessions (append-only) and accepted decisions (immutable)
— predates the rule. Strict immutability would leave the corpus permanently
red under the new checker rule or force the rule to exempt old artifacts.

## Decision

A mechanical pass converts bare cross-references to markdown links across
the **entire** existing corpus, including closed sessions and accepted
decisions. This class of edit — reference formatting that changes no words,
meaning, or structure, verified by diff review — is sanctioned as an
exception to session/decision immutability, both for the initial pass and
for future fixes required by the same integrity rule (e.g. repairing a
link after a slug rename). Any edit that touches meaning remains forbidden:
that path is still a new session or a superseding decision.

## Rationale

The participant weighed a permanently mixed-style corpus against a
narrowly-scoped immutability exception and chose corpus-wide consistency:
immutability protects *what was said and decided*, and wrapping an ID in a
link changes neither. Git history preserves the pre-pass text, so the
audit trail survives intact.

## Alternatives Considered

- **Linkify editable artifacts only** (facilitator's recommendation):
  strictest reading of immutability, but leaves closed sessions and
  accepted decisions — the bulk of the corpus — permanently exempt and
  inconsistent.
- **Forward-only rule, no retrofit**: same inconsistency, plus the checker
  rule would need per-artifact grandfathering.

## Implications

One-time linkification pass over all of `docs/` (except `docs/specs/`,
which already complies); the commit performing it cites this decision.
Reference-formatting edits to immutable artifacts no longer require
supersession. Immutability of content is otherwise unchanged.
