---
id: DEC-0156
type: decision
title: Future connector families are deferred backlog stories, each behind a demand trigger
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0026 @ T6-T8"
links:
  derives-from: [SES-0026]
  relates-to: [DEC-0133, DEC-0100, DEC-0050, DEC-0075, DEC-0155]
---

# DEC-0156: Future Connector Families Behind Demand Triggers

## Context

The new stories' Out of Scope sections name future work — GitHub /
Bitbucket Cloud / GitLab hosts
(DEC-0050), Slack/Teams
notifiers (DEC-0075),
and, after DEC-0155,
non-Jira work-management systems — which
DEC-0133 requires to
exist as deferred artifacts, not prose.

## Decision

Three deferred `backlog` stories capture the families — additional
code-host connectors
(ST-0028),
additional notifier adapters
(ST-0029),
additional work-management connectors
(ST-0030)
— each subscribed to its own armed demand trigger: a deployment
requiring a host other than Bitbucket Data Center (TRG-0007), a
channel beyond email (TRG-0008), or a work-management system other
than Jira Data Center (TRG-0009).

## Rationale

One story per family keeps distinct contracts and demand signals
separate; condition-driven revival beats someone remembering at release
planning. Each family's revival demand is observable and
human-testable.

## Alternatives Considered

- **Backlog stories without triggers**: less machinery; revival depends
  on memory.
- **One combined "additional adapters" story**: conflates three
  contracts and three demand signals.

## Implications

Out of Scope entries across the new stories link these three; the
trigger registry gains TRG-0007..TRG-0009 citing this decision;
deferrals cite this decision per
DEC-0100.
