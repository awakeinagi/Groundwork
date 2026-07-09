---
id: DEC-0002
type: decision
title: The doc store is canonical; Jira is a projection
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-05
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-05
source-span: "SES-0001 @ T2-T3"
links:
  derives-from: [SES-0001]
---

# DEC-0002: The doc store is canonical; Jira is a projection

## Context

Jira items must stay in sync with the centralized doc store. Sync requires a
source of truth and a conflict rule for when the two diverge (e.g., someone
edits an Epic directly in Jira).

## Decision

The centralized doc store is the single source of truth. Jira is a projection
of it. People interface with the documentation system via the Groundwork UI
and are redirected there as needed; direct Jira edits are drift, detected and
reconciled back toward the canonical docs.

## Rationale

The grounding chain (goal → epic → story → component) must be authoritative
in exactly one place, or alignment with business intent — the system's core
purpose — degrades silently.

## Alternatives Considered

- **Jira canonical**: where PMs live, but Jira edits would bypass the
  refinement and provenance process.
- **Bidirectional merge**: field-level merge rules; most complex and
  failure-prone.

## Implications

The Jira connector needs drift detection and a reconciliation flow, and the
UI must be good enough that people prefer it (see
DEC-0013 for what Jira carries).
