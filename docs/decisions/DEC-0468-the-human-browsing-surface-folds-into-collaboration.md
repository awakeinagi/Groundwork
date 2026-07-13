---
id: DEC-0468
type: decision
title: "The human browsing surface folds into Collaboration & Concurrency"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0089 @ T4, T13"
overview: >-
  The human browsing surface (human_docs.html, serve_docs.py), a
  separate DEC-0443 roster topic near the BG-0001 presentation line,
  folds into the Collaboration, Concurrency & Browsing epic rather
  than standing alone. It fails the standalone-outcome test: it is
  the human-readable face of what concurrent sessions produce, and
  alone it would be a one-story epic paying full gate rent. Folding
  into Engine Core was an acceptable fallback but declined in favor
  of aligning with the collaboration change driver. The epic now
  owns rendered browsing, cross-reference navigation, and the human
  search surface alongside the concurrency model.
links:
  derives-from: [SES-0089]
  relates-to: [DEC-0443, DEC-0462]
---

# DEC-0468: The human browsing surface folds into Collaboration & Concurrency

## Context

The human browsing surface (human_docs.html, serve_docs.py) was its own
roster topic; BG-0002 notes it sits near the BG-0001 presentation line
and stays because it serves skill-mode users without the Application.

## Decision

The human browsing surface folds into the Collaboration, Concurrency &
Browsing epic rather than standing alone.

## Rationale

It fails the standalone-outcome test: it is the human-readable face of
what concurrent sessions produce, and standalone it would be a
one-story epic paying full gate rent.

## Alternatives Considered

A standalone channel epic (too thin); folding into Engine Core (an
acceptable fallback, declined in favor of the collaboration
change-driver alignment).

## Implications

The epic owns rendered browsing, cross-reference navigation, and the
human search surface alongside the concurrency model.
