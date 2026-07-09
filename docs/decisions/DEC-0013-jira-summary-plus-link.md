---
id: DEC-0013
type: decision
title: Jira issues carry summary plus link back; component docs get no Jira issue
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-05
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-05
source-span: "SES-0001 @ T6-T7"
links:
  derives-from: [SES-0001]
---

# DEC-0013: Jira carries summary + link back; no Jira issues for components

## Context

Epics, Stories, and Spikes map naturally to Jira issue types. The question
was how much content each Jira issue carries versus the canonical doc, and
whether Component Docs get Jira representation at all.

## Decision

Jira issues carry title, a generated summary, status, and a prominent link to
the canonical doc, with the doc ID in a custom field. Full detail lives only
in the doc store. Component Docs get no Jira issue; the stories that build
them are the trackable units.

## Rationale

Minimizes the drift surface (DEC-0002):
the less content mirrored into Jira, the less can diverge, and Jira
formatting would mangle full doc bodies anyway.

## Alternatives Considered

- **Full mirror**: convenient for Jira-dwellers, maximum drift/noise.
- **Components as Jira items**: adds a tracking surface for artifacts that
  are specifications, not work items.

## Implications

The Jira connector contract is small: create/update projection, detect
drift, redirect editors to the UI.
