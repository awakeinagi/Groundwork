---
id: DEC-0067
type: decision
title: The retrieval layer owns full-text and semantic search over artifact bodies
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0008 @ T2-T3"
links:
  derives-from: [SES-0008]
---

# DEC-0067: Retrieval layer owns search

## Context

DEC-0063 kept text search out of the
Graph Index and deferred ownership here. Cross-goal conflict detection
("does a similar goal already exist?") needs semantic similarity — a core
EP-0002 requirement, not an optimization.

## Decision

EP-0007's retrieval layer owns full-text and embedding-based semantic
search over artifact bodies, built as a derived, rebuildable index (the
same pattern as the Graph Index): rebuilt from the store at any ref, with
the embedding-model version pinned — a model swap is a re-embed batch job,
never a silent mix.

## Rationale

Graph answers structure, search answers content, consolidations answer
efficiency — one retrieval layer composes all three for the recipe
resolver. Bolting search onto the store would muddy its
write-authority contract.

## Alternatives Considered

- **No search in v1**: conflict detection degrades to link-following
  exactly when the corpus is too small to have links.
- **Store-owned search**: wrong layer; the store is deliberately thin.

## Implications

Search infrastructure is evaluated in the extended SP-0002
(DEC-0070); search results in
bundles carry the same source-ref citations as everything else.
