---
id: DEC-0057
type: decision
title: Sessions stay open across pauses and auto-close on inactivity with partial distillation
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0006 @ T4-T5"
links:
  derives-from: [SES-0006]
---

# DEC-0057: Session lifecycle — open across pauses, inactivity auto-close

## Context

Stakeholders engage asynchronously — answer three questions, disappear for
days, return. The pause/resume/close model had to reconcile that with
SPEC-session's closed-is-immutable rule.

## Decision

Sessions stay open across pauses by default; resuming re-orients the
participant (what's settled, what's open). After a configurable inactivity
window the session auto-closes with **partial distillation**: confirmed
decisions commit as accepted, unconfirmed material is marked `proposed`,
and the record notes incompleteness. A later return opens a *new* session
that loads the prior one as context.

## Rationale

One sitting-spanning session keeps turn-span citations coherent for a
continuous line of inquiry, while auto-close prevents abandoned sessions
from accumulating as permanently open provenance.

## Alternatives Considered

- **Close on every exit**: one goal scatters across five fragmented
  records.
- **Never auto-close**: unconfirmed decisions sit in limbo indefinitely.

## Implications

The inactivity window is per-deployment (possibly per-pack) configuration;
re-orientation behavior is pack-defined; auto-close is a mechanical write
(DEC-0033).
