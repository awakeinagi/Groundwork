---
id: DEC-0422
type: decision
title: "Absorption triggers retire implementations, never skill-mode delivery"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-12
source-span: "SES-0082 T10, T21, T31"
accepted-in: SES-0082
overview: >-
  Extends DEC-0346's narrowing of DEC-0338: an absorption trigger
  retires a specific implementation surface (e.g. a Claude-Code
  subagent) for a native application equivalent, never skill-mode
  delivery of the paradigm itself. The engine and CLI adapter
  persist permanently. TRIGGERS.md needs review/repair to carry this
  distinction.
links:
  derives-from: [SES-0082]
  relates-to: [DEC-0338, DEC-0346, BG-0002]
---

# DEC-0422: Absorption triggers retire implementations, never skill-mode delivery

## Context

DEC-0346 already narrowed DEC-0338 to say the method track's pattern is permanent and only its implementation may be swapped. SES-0082 needed to extend that clarification specifically to the absorption-trigger mechanism in TRIGGERS.md, given the new paradigm/application delineation: what exactly does an absorption trigger retire when it fires?

## Decision

The method track's absorption clauses are clarified beyond DEC-0346's narrowing of DEC-0338: an absorption trigger firing retires a specific implementation surface (for example a Claude-Code subagent) in favor of a native application equivalent; it never retires skill-mode delivery of the paradigm itself. The engine and its CLI adapter persist permanently to serve standalone use. The trigger language in TRIGGERS.md is to be reviewed and repaired to carry this distinction.

## Rationale

Without this clarification, an absorption trigger could be misread as license to eventually retire skill-mode entirely once the application matures, which directly conflicts with DEC-0001-B's standing that skill-mode is permanent. Scoping absorption to "implementation surface" rather than "capability" keeps the trigger mechanism useful (it still lets a Claude-Code-specific subagent be replaced by a native equivalent) without threatening the paradigm's standalone availability.

## Alternatives Considered

Leaving TRIGGERS.md's existing language unclarified was rejected — it currently reads ambiguously enough to support the capability-retirement misreading. Rewriting the trigger mechanism from scratch was considered and rejected as unnecessary; the existing absorption-trigger design is sound, it only needed this scope clarification.

## Implications

TRIGGERS.md requires a follow-up review and repair pass to make every absorption trigger's language consistent with "retires an implementation surface, never skill-mode delivery." The gw CLI and its engine are confirmed as permanent standalone-serving components regardless of any future application-side absorption.
