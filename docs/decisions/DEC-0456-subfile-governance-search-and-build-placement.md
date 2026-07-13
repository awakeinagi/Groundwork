---
id: DEC-0456
type: decision
title: "Subfile governance, search, and build placement"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0086"
overview: >-
  Subtopic files live only under the Research artifact's own
  directory; every subfile must be referenced from the main file;
  the checker flags orphaned subfiles and dangling references in
  both directions, and bare-ID cross-references inside subfiles are
  validated like any body prose. Subfile content is semantically
  indexed with hits attributed to the parent RSCH; the graph and
  link machinery see only the main artifact. Build work splits along
  the DEC-0445 seam: static type design (the Research SPEC,
  template, glossary, and ID prefix) belongs to the anticipated
  Artifact-model epic named by DEC-0443, and dynamic tooling support
  (gw CLI type support, checker rules, search and graph indexing,
  viewer handling) belongs to EP-0009.
links:
  derives-from: [SES-0086]
  relates-to: [DEC-0443, DEC-0445, DEC-0423]
---

# DEC-0456: Subfile governance, search, and build placement

## Context

Grilling round 4 (T12) asked about the rules governing subtopic files and their visibility to semantic search. At T13 the stakeholder accepted owned/referenced/checked subfile governance and semantic indexing of subfiles attributed to the parent. At T11 the facilitator noted DEC-0445's dynamic-versus-static seam.

## Decision

Subtopic files live only under the Research artifact's own directory; every subfile must be referenced from the main file; the checker flags orphaned subfiles and dangling references in both directions, and bare-ID cross-references inside subfiles are validated like any body prose. Subfile content is semantically indexed with hits attributed to the parent RSCH; the graph and link machinery see only the main artifact. Build work splits along the DEC-0445 seam: static type design (the Research SPEC, template, glossary, and ID prefix) belongs to the anticipated Artifact-model epic named by DEC-0443, and dynamic tooling support (gw CLI type support, checker rules, search and graph indexing, viewer handling) belongs to EP-0009.

## Rationale

Ownership-and-reference governance keeps subfiles from drifting into orphaned or dangling content without forcing every one to carry an ID; attributing search hits to the parent keeps the RSCH discoverable as a unit even when the matching text lives in a subfile. The DEC-0445 seam split is a direct application of the boundary that decision already drew between static artifact-type design and dynamic tooling.

## Alternatives Considered

Excluding subfiles from semantic search entirely was rejected — it would hide substantive detail from discovery. Giving subfiles their own graph nodes was rejected as unnecessary weight for content with no independent lifecycle.

## Implications

Build work for RSCH therefore has two homes, not one: the anticipated Artifact-model epic and EP-0009, each responsible for its half of the type's realization.
