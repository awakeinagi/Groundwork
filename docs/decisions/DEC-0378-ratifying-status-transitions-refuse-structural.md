---
id: DEC-0378
type: decision
title: "Ratifying status transitions refuse structural defects: duplicate sibling headings and placeholder text"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0072 @ T11-T14"
overview: >-
  A set-status transition to approved, accepted, or closed refuses while the body
  (outside code) contains duplicate same-level headings under one
  parent or placeholder lines — standalone TBD/TODO/FIXME (with
  optional punctuation) or an unallocated ID placeholder like SES-
  XXXX. Backtick-quoting exempts legitimate mentions. Applies to all
  ratifying transitions, not session close alone: SP-0015 would have
  been caught at its own approval gate.
links:
  relates-to: [DEC-0315, DEC-0379]
  derives-from: [SES-0072]
---

# DEC-0378: Ratifying status transitions refuse structural defects: duplicate sibling headings and placeholder text

## Context

SP-0015 shipped approved with a duplicate heading and SES-0070 closed with TBD text; nothing gated ratification on body structure.

## Decision

Gate every ratifying transition on the structural scan (duplicate sibling headings, placeholder lines; TBD/TODO/FIXME token list plus PREFIX-XXXX).

## Rationale

The transition is the moment that matters — the pre-commit checker runs later than the act that created the defect; the small token list catches the real cases with near-zero false positives.

## Alternatives Considered

Session-close-only gating (approvals stay unguarded); broader placeholder pattern sets (false-positive risk on legitimate prose); checker-only (after the fact).

## Implications

Sessions and spikes must be placeholder-free before ratification; legitimate placeholder mentions must be code-quoted.
