---
id: DEC-0151
type: decision
title: Workflow telemetry stays projection-side; the jira-key linkage is the only canonical write
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  The stable jira-key linkage (written once via set-jira-key mechanical
  write when projection is created) is the only canonical write the
  work-management connector makes. Volatile workflow state (status,
  sprint, assignee, estimates) is read by connector, stored app-side,
  and joined at query time. No jira-status frontmatter field exists.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0026 @ T4-T5, clarified @ T9-T10"
links:
  derives-from: [SES-0026]
  relates-to: [DEC-0048, DEC-0095, DEC-0033]
---

# DEC-0151: Workflow Telemetry Projection-Side Only

## Context

DEC-0048's
implication had the connector syncing Jira workflow state into
frontmatter (a planned `jira-status` field via mechanical writes), but
the later DEC-0095 explicitly
rejected mechanical writes of implementation status into canon —
implementation % joins the Graph Index against the projection at query
time. The decision-recall audit surfaced the tension at story
derivation.

## Decision

The stable `jira-key` linkage — the issue key written once into artifact
frontmatter via the `set-jira-key` typed mechanical write
(DEC-0033) when the projection
is created — is the **only** canonical write the work-management
connector ever makes. Volatile workflow state (status column, sprint,
assignee, estimates) is read by the connector, stored app-side, and
joined at query time per
DEC-0095. No `jira-status`
frontmatter field ever exists.

## Rationale

The linkage is a set-once durable fact — exactly what the mechanical
path exists for; workflow state is high-churn build state that
DEC-0095 was accepted to keep
out of design markdown. DEC-0048's
core — project on approval, split field ownership, workflow edits are
telemetry not drift — stands unchanged; only the telemetry destination
is narrowed.

## Alternatives Considered

- **Keep the `jira-status` frontmatter plan**: would need to supersede
  DEC-0095 and reintroduces
  churn in canon.
- **Drop workflow telemetry**: leaves implementation % without its v1
  data source.

## Implications

The work-management connector's telemetry store rides the app database
port (DEC-0121); the planned
schema addition from
DEC-0048's
implication is cancelled.
