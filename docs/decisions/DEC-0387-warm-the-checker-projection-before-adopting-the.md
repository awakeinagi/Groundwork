---
id: DEC-0387
type: decision
title: "Warm the checker projection before adopting the reactive substrate"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-12
accepted-in: SES-0073
source-span: "SES-0073 @ T3"
overview: >-
  SP-0016 post-close follow-up (SES-0073) measured the checker
  projection warm versus cold. Cold per-edit projection costs about
  836 milliseconds, dominated by re-parsing 368 decision files;
  holding the parse warm cuts this to 79-106 milliseconds (8-11x),
  byte-identical to cold; a graph-held incremental update that swaps
  only the edited artifact's nodes reaches about 38 milliseconds
  (22x). The advantage compounds with corpus size: about 6x at the
  current 368 decisions, 8.6x at twice that, 12.4x at four times
  that, where cold reaches an unusable 2.3 seconds per edit; memory
  footprint stays a few megabytes even at four times scale.
  Groundwork should warm its integrity-checker projection as the
  first ActiveGraph-adjacent step, sequenced before adopting the
  reactive substrate explored in SP-0016/DEC-0374/DEC-0375, since
  warming delivers most of the live-editing latency benefit without
  the reactive substrate's build cost or DEC-0375's version-0.7
  pattern-matcher limitation. Three implementation constraints
  govern a correct build: incremental removal must restore severed
  incoming cross-references, guarded by a standing warm-equals-cold
  findings test; packaging must be in-process per session or a
  sidecar daemon because the graph does not serialize; and relation
  removal must be indexed by node so mutation cost stays
  proportional to the edited artifact, not the whole graph.
  Complements rather than supersedes DEC-0375. Descriptive, no kill
  bar (DEC-0355); adoption gated on DEC-0337/DEC-0335; the spike
  build was throwaway per DEC-0351.
links:
  derives-from: [SES-0073]
  relates-to: [SP-0016, DEC-0374, DEC-0375, DEC-0368, DEC-0315, DEC-0351, DEC-0355]
---

# DEC-0387: Warm the checker projection before adopting the reactive substrate

## Context

A post-close follow-up to spike SP-0016 measured the warm and persistent projection that the reactive hook and the production integrity checker currently perform cold on every run.

## Decision

Groundwork should therefore warm its integrity-checker projection as the first ActiveGraph-adjacent step, sequenced before any adoption of the reactive substrate: warming delivers most of the live-editing latency benefit at current and near-term scale without the reactive substrate's build cost or the version 0.7 pattern-matcher limitation recorded in DEC-0375, and it makes per-operation checking affordable in the sense DEC-0315 distinguishes from the pre-commit gate.

## Rationale

Holding the corpus parse warm reduces per-edit projection latency from about 836 milliseconds cold to about 79 to 106 milliseconds, an eight to eleven times improvement, with byte-identical findings; a graph-held incremental update that swaps only the edited artifact's nodes reaches about 38 milliseconds, a twenty-two times improvement. The advantage compounds as the corpus grows, from roughly six times at the current size to about twelve times at four times the corpus, where the cold path reaches an unusable 2.3 seconds per edit, and the in-memory footprint is negligible at a few megabytes.

## Alternatives Considered

This decision complements DEC-0375 rather than superseding it.

## Implications

A correct and scalable implementation must satisfy three constraints established by the measurements: incremental removal must restore the incoming cross-references it severs, guarded by a standing warm-equals-cold findings test, or it silently diverges from a cold rebuild; packaging must be in-process per session or a sidecar daemon because the graph does not serialize; and relation removal must be indexed by node so that mutation cost stays proportional to the edited artifact rather than the whole graph. Adoption remains gated on the ordinary DEC-0337 option survey and DEC-0335 design intake, the spike build was strictly throwaway per DEC-0351, and the result is descriptive with no kill bar per DEC-0355.
