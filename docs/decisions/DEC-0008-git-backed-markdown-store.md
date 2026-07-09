---
id: DEC-0008
type: decision
title: Reference doc store is git-backed markdown
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-05
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-05
overview: >-
  Reference implementation of canonical store is markdown files with YAML
  frontmatter in git repository owned by application. UI reads and writes
  through storage API. Versioning, diffs, and branch-based review come
  free. Implementation agents consume docs same way they consume code.
  Consolidation freshness can pin git refs. Storage interface does not
  leak git specifics, so database or wiki backend remains swappable.
source-span: "SES-0001 @ T4-T5"
links:
  derives-from: [SES-0001]
---

# DEC-0008: Reference doc store is git-backed markdown

## Context

Storage is a pluggable boundary, but the reference implementation shapes
versioning, review, and how the implementation swarm consumes docs.

## Decision

The reference implementation of the canonical store is markdown files with
YAML frontmatter in a git repository owned by the application; the UI reads
and writes through the storage API.

## Rationale

Versioning, diffs, and branch-based review come free; implementation agents
consume docs the same way they consume code; Consolidation freshness can pin
git refs (DEC-0017).

## Alternatives Considered

- **Database-native**: better queryability and real-time collaboration —
  the queryability need is met instead by the derived Graph Index
  (DEC-0010).
- **Existing wiki (Confluence)**: adoption-friendly, but API-mediated
  versioning and cross-refs are clumsy and the swarm would need extraction.

## Implications

The storage interface must not leak git specifics, so a database or wiki
backend remains swappable (DEC-0018
extends the same spirit to the whole stack).
