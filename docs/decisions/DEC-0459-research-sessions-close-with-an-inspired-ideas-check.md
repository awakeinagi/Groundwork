---
id: DEC-0459
type: decision
title: "Research sessions close with an inspired-ideas check"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: SES-0087
overview: >-
  The research-session workflow defined by DEC-0450 gains a closing
  step after compile, present, and write: the facilitator asks
  whether the investigation inspired any ideas, and each captured
  idea is recorded as an IDEA artifact carrying inspired-by naming
  the RSCH — within the type list DEC-0454 permits — joining the
  work queue per DEC-0261. This mirrors the inspired-ideas check
  DEC-0261 runs at design-session close.
links:
  derives-from: [SES-0087]
  relates-to: [DEC-0450, DEC-0454, DEC-0261, DEC-0281]
---

# DEC-0459: Research sessions close with an inspired-ideas check

## Context

While SES-0086's close-out batch was running, the stakeholder relayed an addition through a message to a running recall-audit judge agent: research (RSCH) workflows may generate IDEAs, and the research-session workflow defined by DEC-0450 should ask about them at workflow end. The facilitator surfaced the relayed message for verification rather than acting on it, and the stakeholder confirmed it as their own input, choosing to have it recorded as part of the design. Because SES-0086 had already closed, the addition was captured back-to-back as its own expedited session, SES-0087.

## Decision

The research-session workflow defined by DEC-0450 gains a closing step after compile, present, and write: the facilitator asks whether the investigation inspired any ideas, and each captured idea is recorded as an IDEA artifact carrying inspired-by naming the RSCH — within the type list DEC-0454 permits — joining the work queue per DEC-0261.

## Rationale

This mirrors the inspired-ideas check DEC-0261 runs at design-session close, keeping the same backlog-capture pattern consistent across both session kinds rather than inventing a separate mechanism for research sessions.

## Alternatives Considered

Leaving research sessions without a closing inspired-ideas check was rejected — DEC-0450's workflow stages already end at write, and omitting the check would silently drop IDEA-worthy tangents that surface during deep investigation, the same problem DEC-0261 addresses for design sessions.

## Implications

Research-session facilitation guidance gains this closing step; captured ideas from a research session use the DEC-0454 inspired-by/inspired link pair naming the RSCH, and follow the DEC-0261 work-queue path from there.
