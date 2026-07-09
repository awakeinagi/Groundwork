---
id: DEC-0063
type: decision
title: The index carries frontmatter metadata only; bodies stay in the store
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
overview: >-
  Nodes carry frontmatter-derived attributes (id, type, status, title, owner,
  refs); edges carry link type and provenance. Bodies stay in the store: queries
  return IDs plus metadata, and callers fetch documents through the storage API.
  Full-text and semantic search over bodies is a separate retrieval concern in
  EP-0007's neighborhood, not this index. This keeps rebuild fast and the index
  small, and avoids duplicating body storage that the consolidation and retrieval
  layer will need to own anyway.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0007 @ T4-T5"
links:
  derives-from: [SES-0007]
---

# DEC-0063: Metadata-only graph

## Context

The index could carry anything from bare link topology to full document
bodies; content depth determines rebuild speed, index size, and who owns
text search.

## Decision

Nodes carry frontmatter-derived attributes (id, type, status, title,
owner, refs); edges carry link type and provenance. Bodies stay in the
store: queries return IDs plus metadata, and callers fetch documents
through the storage API. Full-text/semantic search over bodies is a
separate retrieval concern in EP-0007's neighborhood — not this index.

## Rationale

Keeps rebuild fast and the index small, and avoids duplicating body
storage that the consolidation/retrieval layer will need to own anyway.

## Alternatives Considered

- **Full-text sidecar in the index**: doubles the index's job, slows
  rebuilds.
- **Bodies as node properties**: two copies of every document to keep
  consistent.

## Implications

Text/semantic search lands as an EP-0007 refinement question (impact edge
EP-0004→EP-0007 already present); UI and agents compose graph queries with
store fetches.
