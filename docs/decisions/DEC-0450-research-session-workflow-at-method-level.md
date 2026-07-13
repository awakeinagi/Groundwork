---
id: DEC-0450
type: decision
title: "Research-session workflow at method level"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0086"
overview: >-
  A dedicated research session proceeds through defined stages:
  capture the stakeholder's intent (what is to be researched and
  why) and the research goals; choose the source mode; deep-dive
  into each source; assess whether the intent and goals have been
  met, looping to find more sources and repeat until they are;
  compile all findings; present them to the stakeholder; and write
  the research into the RSCH artifact. The executable research
  harness that automates these stages is derived build work under
  its own design gate per DEC-0335; IDEA-0005 relates to that future
  work. Defining the workflow at the method level first, before any
  harness is built, follows DEC-0335's no-arbitrary-builds guard.
links:
  derives-from: [SES-0086]
  relates-to: [DEC-0335, IDEA-0005]
---

# DEC-0450: Research-session workflow at method level

## Context

At T6 the stakeholder described the workflow of a dedicated research session in detail and asked for it to be grilled. Grilling round 3 (T9) asked where the build work lands and what happens to IDEA-0005. At T10 the stakeholder confirmed the new Artifact-model epic under BG-0002 as the build home.

## Decision

A dedicated research session proceeds through defined stages: capture the stakeholder's intent (what is to be researched and why) and the research goals; choose the source mode; deep-dive into each source; assess whether the intent and goals have been met, looping to find more sources and repeat until they are; compile all findings; present them to the stakeholder; and write the research into the RSCH artifact. The executable research harness that automates these stages is derived build work under its own design gate per DEC-0335; IDEA-0005 relates to that future work.

## Rationale

Defining the workflow at the method level first (per DEC-0335's no-arbitrary-builds guard) lets the shape of the investigation loop be agreed before any harness is built to automate it, and gives IDEA-0005's researcher-agent idea a concrete home to be taken up against.

## Alternatives Considered

Building the harness immediately alongside the type design was rejected — DEC-0335 requires a presented, approved design before any build, and the harness is substantial enough to warrant its own gate.

## Implications

IDEA-0005 stays captured pending take-up against this workflow; the eventual harness derives from the anticipated Artifact-model epic or EP-0009 depending on whether it is static type support or dynamic tooling.
