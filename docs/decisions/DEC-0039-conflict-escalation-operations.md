---
id: DEC-0039
type: decision
title: Escalated conflicts queue with the Arbiter and block merges; timeout resolution electable per artifact
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0004 @ T3"
links:
  derives-from: [SES-0004]
---

# DEC-0039: Conflict escalation operations

## Context

DEC-0005 defined the
mediation-then-escalation flow; the operational mechanics — where escalated
conflicts land, what they block, and whether they expire — needed
definition.

## Decision

Default behavior: escalated Conflicts enter an Arbiter work queue in the UI
(with notifications via configured channels); the artifacts in tension
carry a failing `conflicts-open` status check so their PRs cannot merge. No
automatic timeout — a conflict resolves only by a ratified Decision or
explicit withdrawal; aging conflicts escalate in visibility (reminders,
dashboards), not in state. **Exception, electable per artifact**: an
artifact may opt into timeout-to-default — after a configured period, the
conflict auto-resolves per a configured default rule, recorded as a system
Decision citing the election.

## Rationale

Deciding-by-not-deciding shouldn't be the system default, but some
artifacts (time-boxed initiatives, low-stakes tensions) legitimately prefer
motion over deliberation — making that a per-artifact election keeps the
choice explicit and auditable rather than institutional.

## Alternatives Considered

- **Global timeout-to-default**: institutionalizes non-decision.
- **Arbiter panel with SLA**: heavy for initial deployment scale.

## Implications

The timeout election is artifact frontmatter (schema addition at story
level); auto-resolutions produce system Decisions that cite both the
election and the default rule, keeping provenance intact.
