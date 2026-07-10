---
id: IDEA-0012
type: idea
title: Skill-level contracts — skills' implicit capability surface
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-09
proposed-by: awakeinagi
overview: >-
  Captured at SES-0059's inspired-ideas check (facilitator-proposed,
  stakeholder-approved): agents got a mandatory runtime-policy
  contract (DEC-0340), but skills also carry implicit capability
  surprises — a skill's bundled scripts execute with whatever tools
  the loading agent holds, and skills have no equivalent contract
  shape beyond what individual CMPs cover. A future look at skill-
  level contracts may be warranted. Level unclear (SPEC extension,
  checker rule, or per-skill CMPs under BG-0002) — hence an Idea.
  Disposition pending.
links:
  derives-from: [SES-0059]
---

# IDEA-0012: Skill-Level Contracts — Skills' Implicit Capability Surface

## The Idea

Verbatim (facilitator proposal at the SES-0059 inspired-ideas check,
stakeholder disposition: "Yes, you can add that as an idea or a
spike."): the conversation exposed that *skills* can also carry
implicit capability surprises — a skill's scripts run with the loading
agent's permissions; a future look at skill-level contracts beyond the
agent checklist might be warranted.

## Spark Context

Raised at SES-0059's close, immediately after the session designed the
agent-contract profile (DEC-0340): agents got a mandatory
runtime-policy contract, but skills — which inject content and whose
bundled scripts execute with whatever tools the loading agent holds —
have no equivalent contract shape beyond what the artifact-interact
CMP will cover for that one skill. Level unclear (a SPEC extension?
a checker rule? per-skill CMPs under BG-0002?) — hence an Idea per the
DEC-0259 boundary.

## Disposition

Pending — awaiting take-up via the change-intake protocol as its own
session.
