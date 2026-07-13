---
id: DEC-0452
type: decision
title: "Source provenance inside findings"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0086"
overview: >-
  Every Research artifact carries a source register listing each
  source's title, reference or URL, source type, and date accessed,
  and every finding cites its source or sources from that register.
  A structured register with per-finding citation makes findings
  independently verifiable and durable even as the underlying source
  (a web page, for instance) changes or disappears, matching the
  rigor Decisions already apply to their own source spans.
links:
  derives-from: [SES-0086]
---

# DEC-0452: Source provenance inside findings

## Context

Grilling round 2 (T7) asked about source-provenance rigor; the stakeholder (T8) accepted the recommendation for a source register with per-finding citations.

## Decision

Every Research artifact carries a source register listing each source's title, reference or URL, source type, and date accessed, and every finding cites its source or sources from that register.

## Rationale

A structured register with per-finding citation makes findings independently verifiable and durable even as the source itself (a web page, for instance) changes or disappears.

## Alternatives Considered

Informal inline citation without a structured register was rejected as insufficiently rigorous for evidence meant to justify new or amended Business Goals.

## Implications

The checker can validate that every finding references at least one register entry, similar in spirit to how Decisions cite their source span.
