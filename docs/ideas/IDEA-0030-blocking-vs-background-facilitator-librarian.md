---
id: IDEA-0030
type: idea
title: "Blocking vs background facilitator-librarian interaction"
status: taken-up
owner: awakeinagi@gmail.com
created: 2026-07-11
proposed-by: awakeinagi
overview: >-
  Investigates which artifact-librarian actions the facilitator
  genuinely must wait for synchronously versus which can be left
  running in the background while the facilitator continues other
  work. Motivated by the observation that a substantial share of
  facilitator wall-clock time is spent waiting for the librarian to
  finish, under the everything-mandatory delegation rule (former
  DEC-0325, superseded by DEC-0388) and the librarian's serialized-
  write / parallel-read concurrency model (DEC-0332). Raised
  verbatim by the stakeholder at SES-0066's closing inspired-ideas
  check; captured at SES-0067. Taken up at SES-0076 together with
  sibling IDEA-0031 and a third remedy family — targeted-read de-
  mediation — seeking one ratified efficiency solution across all
  three. Resolved at SES-0076 by DEC-0393: librarian tasks launch in
  the background by default, the facilitator blocks only where the
  next turn depends on the result, and no barrier machinery is
  needed because every task reports actually applied outcomes.
links:

  derives-from: [SES-0067]
  relates-to: [IDEA-0031, DEC-0325, DEC-0332, SES-0076]
---

# IDEA-0030: Blocking vs background facilitator-librarian interaction

## The Idea

TBD.

## Spark Context

TBD.

## Disposition

Taken up at SES-0076 together with its sibling and a third remedy family (targeted-read de-mediation) surfaced at take-up; the session seeks one ratified efficiency solution across all three.

Resolved at SES-0076 by DEC-0393 — librarian tasks launch in the background by default and the facilitator blocks only where the next turn depends on the result; no barrier machinery is required because every task reports actually applied outcomes.

