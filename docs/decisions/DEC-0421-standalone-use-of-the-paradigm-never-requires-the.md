---
id: DEC-0421
type: decision
title: "Standalone use of the paradigm never requires the application"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-12
source-span: "SES-0082 T2, T10, T21, T31"
accepted-in: SES-0082
overview: >-
  Using the Groundwork Paradigm never requires the Groundwork
  Application: agent skills and gw tooling are a permanent, first-
  class delivery mode. This narrows DEC-0001 without superseding it
  — DEC-0001's application-as-primary-form-factor choice stands, but
  its skills-first rejection is confined to that form-factor
  question and does not preclude additive standalone skill-mode
  delivery.
links:
  derives-from: [SES-0082]
  relates-to: [DEC-0001, BG-0002]
---

# DEC-0421: Standalone use of the paradigm never requires the application

## Context

Once DEC-0001 (this decision's own precursor) is read literally, it could be misread as requiring the hosted application for any real use of Groundwork. SES-0082 needed to confirm whether skill-mode delivery is a permanent, independently viable way to use the paradigm, or merely a stopgap until the application exists.

## Decision

Using the Groundwork Paradigm never requires hosting or running the Groundwork Application: the agent skills and gw tooling are a permanent, first-class delivery mode.

## Rationale

This narrows DEC-0001 without superseding it: DEC-0001's choice of a standalone application as the product's primary form factor and its rationale — business stakeholders need a UI, not a terminal — stand unchanged; its rejection of a skills-first approach is confined to that product form-factor question and does not preclude standalone skill-mode delivery, which is additive.

## Alternatives Considered

Superseding DEC-0001 outright was considered and rejected as disproportionate: DEC-0001's core finding (the application is the right primary form factor for business stakeholders) remains correct and unchanged. Treating skill-mode as a temporary bridge until the application ships was also rejected — it would undercut DEC-0326's standing-instruction skill delivery model and the corpus's own use of Groundwork today, which is skill-mode only.

## Implications

DEC-0001 is not amended or marked stale; a relates-to link records the narrowing relationship for anyone reading either decision. Skill-mode delivery can be relied on as permanent by any project that adopts the paradigm without ever standing up the application.
