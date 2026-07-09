---
id: DEC-0019
type: decision
title: Groundwork is specified using its own process and formats
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-05
overview: >-
  Groundwork specifies itself using its own artifact formats and pipeline; SES-0001
  is the inception session, producing DEC records and component docs in production
  format authored manually until tooling self-hosts; validates doc format before
  application code exists and directly satisfies language-agnostic rebuild requirement.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-05
source-span: "SES-0001 @ T10-T11"
links:
  derives-from: [SES-0001]
---

# DEC-0019: Full dogfood — Groundwork specs itself with its own formats

## Context

Groundwork's artifact formats and pipeline could be validated only after the
application exists, or exercised immediately by using them to specify the
system itself.

## Decision

Full dogfood. The inception grilling session is SES-0001; its distilled
decisions are the first DEC records; Groundwork's own business goal is
BG-0001; its components get contract-complete Component Docs in exactly the
format the system will produce — authored manually (with agent assistance)
until the tool can host itself.

## Rationale

The doc format gets validated before a line of application code exists, and
the resulting specs directly satisfy the rebuild-in-any-language requirement
(DEC-0018).

## Alternatives Considered

- **Conventional spec first**: faster start; format untested until late.
- **Hybrid** (formats yes, pipeline ceremony no): loses the gate/session
  discipline that needs validating too.

## Implications

This repository is simultaneously Groundwork's first Canonical Store and its
specification. Friction encountered while dogfooding is design feedback.
