---
id: DEC-0268
type: decision
title: The Idea type enters the application via amendments to the schema-suite contracts, not a new store story
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
overview: >-
  DEC-0268 constrains the Idea type reflection in the application to
  amendments only to ST-0001 and CMP-0001: the artifact-type enumeration
  extends to include IDEA with acceptance criteria for Idea-specific
  validation, and the SchemaValidator type list matches. No new store
  story; adding a type is the schema suite's existing charter per
  ST-0001, and dual stories would split that responsibility.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0051 @ T6-T7"
links:
  derives-from: [SES-0051]
  relates-to: [DEC-0258]
---

# DEC-0268: Idea support is schema-suite amendment work

## Context

Reflecting the paradigm's Idea type (DEC-0258) in the application
requires the store to validate it. ST-0001 AC1 and CMP-0001
`SchemaValidator.D-1` hard-enumerate the artifact-type set — should
the reflection amend them, or land as a new story under EP-0001?

## Decision

Amendments only. ST-0001's AC1 enumeration extends to include IDEA and
the story gains an acceptance criterion for Idea-specific validation
(statuses, `proposed-by`, rejection of release/gate fields); CMP-0001's
`SchemaValidator.D-1` type list extends to match. No new store story:
"a schema for every artifact type" is ST-0001's existing charter, and
a parallel "Idea support" story would split ownership of the same
responsibility across two artifacts.

## Rationale

The seam holds: adding a type is the schema suite doing its job on one
more input, not new store behavior. The cost is honest — amending an
approved story stales CMP-0001 (element-scoped) — and the DEC-0267
machinery handles it inside this session.

## Alternatives Considered

- **New story under EP-0001 plus minimal amendments**: a cleaner
  citation home for the new decisions, but duplicates ST-0001's
  responsibility and leaves "who owns Idea validation" ambiguous.

## Implications

ST-0001 and CMP-0001 are amended and re-affirmed in-session
(DEC-0267). Pre-launch, no migration machinery is needed — ST-0011
(schema evolution, deferred backlog) and TRG-0005 are untouched.
