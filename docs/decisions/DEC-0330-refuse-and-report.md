---
id: DEC-0330
type: decision
title: On write-API refusals the librarian refuses and reports — it never adapts
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0058 @ T8-T9"
overview: >-
  When a caller's task asks for something the artifact-interact write
  API refuses — editing an accepted decision, an illegal status
  transition, a reciprocity-breaking link — the artifact-librarian
  performs nothing and returns the refusal to the caller, including
  the sanctioned alternative the API names (per DEC-0315's error
  contract, e.g. "accepted decisions are immutable — supersede
  instead"). The librarian never substitutes the sanctioned
  alternative on its own: choosing to supersede a decision is a
  process-level act the stakeholder (via the facilitator) must
  ratify, and a subagent silently making it would relocate authority
  the process deliberately places at the session table. Chosen over
  autonomous adaptation and over a caller-granted "adapt as needed"
  latitude mode (two behaviors, more contract surface, same authority
  leak when used). Cost accepted: an extra round-trip on refusals.
links:
  derives-from: [SES-0058]
  relates-to: [DEC-0324, DEC-0312, DEC-0315]
---

# DEC-0330: Refuse and Report

## Context

The write API refuses invariant-violating operations with errors
naming the sanctioned alternative (DEC-0312, DEC-0315). With a
librarian between caller and API, the question: may the librarian act
on that alternative itself?

## Decision

No. On any API refusal the librarian performs nothing and returns the
refusal verbatim — including the named sanctioned alternative — to
the caller, who decides.

## Rationale

The refused-then-sanctioned path is usually a process-level choice
(supersede vs abandon; new session vs enrichment) that belongs to the
facilitator and stakeholder, not a toolbelt subagent. Refusals are
rare enough that the extra round-trip is cheap; silent adaptation
would be an authority leak precisely where the guardrails are
supposed to be strongest.

## Alternatives Considered

- **Adapt within sanctioned ops** — fewer round-trips, silent
  process decisions; rejected.
- **Caller-granted latitude flag** — two behaviors; the flag would
  invite routine use and the same leak; rejected.

## Implications

The librarian's definition states the rule; its result contract
(DEC-0324) includes a refusal-report shape. Callers mid-session
surface refusals to the stakeholder like any other tension.
