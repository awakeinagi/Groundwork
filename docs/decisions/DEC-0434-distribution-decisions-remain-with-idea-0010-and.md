---
id: DEC-0434
type: decision
title: "Distribution decisions remain with IDEA-0010 and IDEA-0013 take-up, framed by this delineation"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-12
source-span: "SES-0082 T10, T11, T21, T31"
accepted-in: SES-0082
overview: >-
  Skill and plugin distribution decisions remain with IDEA-0010's
  and IDEA-0013's take-up, framed by this session's delineation: the
  distribution unit targets the portable skill specification with
  explicit versioning, consumer projects track rather than fork, and
  the application does not distribute the paradigm.
links:
  derives-from: [SES-0082]
  relates-to: [IDEA-0010, IDEA-0013, DEC-0319]
---

# DEC-0434: Distribution decisions remain with IDEA-0010 and IDEA-0013 take-up, framed by this delineation

## Context

Both a plugin-packaging idea (IDEA-0010) and a paradigm-export-mechanism idea (IDEA-0013) were already captured before this session, addressing how the skills and paradigm get distributed to adopters. SES-0082 needed to say how the paradigm/application delineation this session settled bears on those still-uncaptured decisions, without prematurely deciding distribution mechanics that belong to their own future take-up sessions.

## Decision

Skill and plugin distribution decisions remain with the take-up of IDEA-0010 and IDEA-0013 and are made within this session's delineation framing: the distribution unit targets the portable skill specification with explicit versioning, consumer projects track rather than fork, and the application does not distribute the paradigm.

## Rationale

Distribution mechanics are a separate design question from delineation (what the two deliverables are) and from single-sourcing (DEC-D) — deciding them here would pre-empt the dedicated take-up sessions those ideas already exist to run. Stating the framing now (skill spec as the distribution unit, tracking over forking, application not being a distribution channel for the paradigm) gives those future sessions a consistent starting boundary consistent with everything else this session settled, without foreclosing their own design work.

## Alternatives Considered

Deciding distribution mechanics fully within SES-0082 was rejected — it would exceed this session's scope and duplicate the purpose IDEA-0010 and IDEA-0013 already exist to serve. Leaving no framing at all for those future sessions was rejected — it would risk their take-up work drifting from the delineation this session just ratified (e.g. accidentally treating the application as a paradigm-distribution channel).

## Implications

IDEA-0010 and IDEA-0013 remain captured, not yet taken up; this decision does not advance their status. Their eventual take-up sessions inherit the stated framing as a starting constraint rather than an open question.
