---
id: DEC-0381
type: decision
title: "Zero-decision session close requires an explicit recorded acknowledgment (--no-decisions-ok)"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0072 @ T5, T11-T12"
overview: >-
  Closing a session from which no decision derives refuses with a
  warning explaining the assessment obligation unless the caller
  passes --no-decisions-ok "<reason>"; the flag is the recorded
  assessment, echoed in the op output. Idea-capture micro-sessions
  (DEC-0258) legitimately pass it. Stakeholder-originated scope
  (T5): the warning must trigger the calling agent to assess and fix
  with the librarian when zero is wrong.
links:
  derives-from: [SES-0072]
---

# DEC-0381: Zero-decision session close requires an explicit recorded acknowledgment (--no-decisions-ok)

## Context

Sessions could close with their Decisions Produced unrecorded (SES-0071 closed with TBD there); nothing distinguished "legitimately zero" from "forgot to distill".

## Decision

Refuse zero-decision closes without an explicit reason-carrying acknowledgment flag.

## Rationale

An unattended agent can scroll past a printed warning; a required flag forces the assessment and records it.

## Alternatives Considered

A pure advisory warning (ignorable); advisory plus checker backstop (two soft nudges, still skippable at the moment of close).

## Implications

Idea-capture close tasks include the flag with their DEC-0258 justification.
