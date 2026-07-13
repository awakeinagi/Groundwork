---
id: DEC-0447
type: decision
title: "New artifact type: Research (RSCH)"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0086"
overview: >-
  A new Groundwork artifact type, Research (RSCH-*), captures the
  learnings of a free-standing deep investigation into a topic drawn
  from any source class — web search, books, videos, or others.
  Research artifacts live in docs/research/. Each Research artifact
  consists of one canonical main file carrying the frontmatter,
  overview, status, links, research goals, compiled findings, and
  Business-Goal applicability analysis; optional subtopic write-ups
  live as plain markdown files in the artifact's own directory
  (docs/research/RSCH-nnnn/), owned by and referenced from the main
  file, without IDs or frontmatter of their own. The type fills the
  gap identified between Ideas (raw capture) and Spikes (design-
  tree-scoped investigation), giving free-standing investigation its
  own citable home. Static type design belongs to the anticipated
  Artifact-model epic named by DEC-0443; dynamic tooling support
  belongs to EP-0009.
links:
  derives-from: [SES-0086]
  relates-to: [DEC-0443]
---

# DEC-0447: New artifact type: Research (RSCH)

## Context

The stakeholder proposed a new Groundwork artifact type for capturing learnings from deep investigations into a topic, drawn from any source class, and for tracing how those learnings apply to Business Goals and derived work. At T4 the locate-first sweep (DEC-0266) found no duplicate in the corpus; the nearest prior art, IDEA-0005, is adjacent tooling capture rather than the type itself. DEC-0443's anticipated derived-work roster names "Artifact model" as the home topic for artifact-type additions under the rechartered BG-0002.

## Decision

A new Groundwork artifact type, Research (RSCH-*), captures the learnings of a free-standing deep investigation into a topic drawn from any source class — web search, books, videos, or others. Research artifacts live in docs/research/. Each Research artifact consists of one canonical main file carrying the frontmatter, overview, status, links, research goals, compiled findings, and Business-Goal applicability analysis; optional subtopic write-ups live as plain markdown files in the artifact's own directory (docs/research/RSCH-nnnn/), owned by and referenced from the main file, without IDs or frontmatter of their own.

## Rationale

A dedicated type gives investigation output a stable, citable identity distinct from the design tree, while the single-main-file-plus-subfiles shape lets deep write-ups scale without minting IDs for content that never needs independent lifecycle or linking.

## Alternatives Considered

Folding research output into Ideas was rejected (DEC-0259: Ideas are raw pre-classification capture, not analyzed evidence). Giving every subtopic file its own artifact ID was rejected as unnecessary ID/frontmatter overhead for content that is always read in the context of its parent.

## Implications

Establishes docs/research/ as a new directory; the static type design (SPEC, template, glossary entry, ID prefix) is build work under the anticipated Artifact-model epic named by DEC-0443, and dynamic tooling support belongs to EP-0009 per DEC-0445.
