---
id: DEC-0304
type: decision
title: Empty context means empty conversational context — pinned-corpus crawl stays sanctioned (extends DEC-0011)
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0056 @ T5-T7"
overview: >-
  "Empty context" means empty conversational context: an implementing
  agent receives only its work-package bundle plus the Shared
  Preamble, with no session history. Crawling the corpus pinned at
  canonical-ref remains sanctioned — DEC-0011's crawlable-provenance
  fallback survives, now scoped per element bundle. Extension of
  DEC-0011, not supersession; missing information reachable neither
  in the bundle nor by crawl remains a documentation defect
  (SPEC-handoff-manifest rule 4 in spirit). A strict no-crawl reading
  was rejected: it would sharply raise documentation burden before
  evidence warrants, against DEC-0011's explicit iterative-tightening
  mandate.
links:
  derives-from: [SES-0056]
  relates-to: [DEC-0011, DEC-0300, DEC-0297]
---

# DEC-0304: Empty-Context Semantics

## Context

The SES-0056 T1 proposal's "initially empty context" phrase has two
readings; the strict one (bundle only, no crawl) would silently
supersede DEC-0011's sanctioned fallback.

## Decision

**Empty context = empty conversational context.** The implementing
agent starts with its work-package bundle + the Shared Preamble and
no session history. Crawling the corpus pinned at `canonical-ref`
remains sanctioned (DEC-0011's fallback, now scoped per element
bundle). Information reachable neither in the bundle nor by crawl is
a documentation defect.

## Rationale

The bundle makes the common case self-sufficient; the crawl keeps
the rare missing detail from becoming a wrong guess — DEC-0011's
quality-first ordering, unchanged.

## Alternatives Considered

- **Strict no-crawl self-containment** — raises authoring burden
  sharply before defect evidence warrants; rejected.

## Implications

Bundle-closure (DEC-0303) targets zero *required* crawls; crawl
frequency is a natural fitness metric for tightening over time.
