---
id: DEC-0483
type: decision
title: "The artifact-model schema version is a corpus-level SemVer marker; migrations move whole corpora atomically"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-13
source-span: "SES-0091 @ T6-T9"
overview: >-
  The schema version needed a declaration locus and numbering
  scheme. This decision declares exactly one artifact-model schema
  version per corpus, in a corpus-level marker numbered with
  Semantic Versioning, with migrations moving the entire corpus
  atomically so mixed-version corpora are impossible by construction
  — ruling out lazy per-artifact migration.
links:
  derives-from: [SES-0091]
  relates-to: [DEC-0471, DEC-0480, DEC-0482, DEC-0487]
---

# DEC-0483: The artifact-model schema version is a corpus-level SemVer marker; migrations move whole corpora atomically

## Context

The schema version needed a declaration locus and a numbering scheme.

## Decision

Each corpus declares exactly one artifact-model schema version in a corpus-level marker, numbered with Semantic Versioning. Migrations move the entire corpus atomically from one version to the next; mixed-version corpora are impossible by construction.

## Rationale

Per-artifact stamps would make every read version-branching and the checker permanently mixed-version-aware, a standing cost for a rare event. The stakeholder set Semantic Versioning explicitly, aligning with the release-labeling conventions already in use.

## Alternatives Considered

Per-artifact version stamps enable lazy migration but were rejected for their permanent read-path and checker complexity.

## Implications

Lazy per-artifact migration is off the table, and the migration-mechanism spike evaluates in-place rewrite versus side-by-side migration under this shape.
