---
id: DEC-0480
type: decision
title: "Engine API versioning: compatible extension with tolerant readers until the first non-CLI consumer; foreign corpora pin schema versions"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-13
source-span: "SES-0091 @ T4-T5"
overview: >-
  The Engine API and adoption-verified corpora both needed a
  versioning posture. This decision has the Engine API evolve by
  compatible extension with tolerant readers under explicit
  compatibility rules (new optional fields compatible;
  removal/rename/type-change breaking), defers formal versioning
  machinery to the first non-CLI consumer, and has foreign corpora
  on the adoption surface pin explicit schema versions.
links:
  derives-from: [SES-0091]
  relates-to: [DEC-0423, DEC-0483]
---

# DEC-0480: Engine API versioning: compatible extension with tolerant readers until the first non-CLI consumer; foreign corpora pin schema versions

## Context

The Engine API and the corpora the adoption surface verifies both needed a versioning posture.

## Decision

The Engine API evolves by compatible extension with tolerant readers, under explicitly written compatibility rules: new optional fields are compatible; removal, rename, or type change is breaking. Formal API versioning machinery is deferred to the first non-CLI consumer. Foreign corpora on the adoption surface pin explicit schema versions.

## Rationale

The Engine has a single internal consumer today per DEC-0423, so versioning machinery would serve nobody, while external corpora cannot be forced to upgrade synchronously.

## Alternatives Considered

Formal versioning now was rejected as machinery without a second consumer. Leaving compatibility rules unstated was rejected because drift would be adjudicated ad hoc.

## Implications

When a second consumer arrives, the versioning decision is made against a clean compatibility record, and the adoption contract carries version pinning from the start.
