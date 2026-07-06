---
id: DEC-0048
type: decision
title: Jira projections are created on approval; field ownership is split
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0005 @ T4-T5"
links:
  derives-from: [SES-0005]
---

# DEC-0048: Project on approval; split field ownership

## Context

Projection timing (when does an epic get its Jira issue?) and field
ownership once implementation teams start moving tickets across sprint
boards needed definition — total canonical ownership would kill normal
sprint workflow.

## Decision

Projections are created when the artifact first merges to main (approved);
drafts never appear in Jira. Field ownership is split: **content fields**
(title, summary, description, doc link, doc-id) are canonical-owned — edits
there are drift ([DEC-0044](DEC-0044-drift-revert-capture-proposal.md)).
**Workflow fields** (status column, sprint, assignee, estimates) are
Jira-owned — teams work normally, and the connector syncs workflow state
into the doc store as implementation telemetry via mechanical writes
([DEC-0033](DEC-0033-typed-mechanical-writes.md)), not drift.

## Rationale

Jira-dwellers only ever see ratified content, and sprint mechanics stay
untouched; the doc store still learns implementation progress for
traceability reporting.

## Alternatives Considered

- **Project drafts too**: unratified content in Jira; doubled drift surface.
- **Everything canonical-owned**: sprint boards die.

## Implications

Artifact frontmatter gains a synced `jira-status` field (schema addition at
story level); the field-ownership map is part of the Jira connector
contract.
