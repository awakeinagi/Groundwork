---
id: DEC-0388
type: decision
title: "Targeted artifact reads are de-mediated for every agent; librarian mediation remains mandatory for writes and synthesis reads"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-12
source-span: "SES-0076 @ T4-T5, T10-T11, T29"
overview: >-
  Any agent may directly invoke targeted, bounded-output read
  operations (overview, outline, section, citers, filtered listings,
  a single search, a single graph query) without spawning the
  librarian. Librarian delegation remains mandatory for every write
  and for open-ended synthesis reads: precedent hunts, surveys,
  recall audits, and any task requiring iterative exploration or
  cross-artifact distillation. The boundary is output-shape plus
  judgment rather than a hard call cap; an agent that catches itself
  chaining many calls delegates instead. Raw Read/Grep/Glob of docs/
  remains forbidden outside existing DEC-0328-style charters. This
  partially reverses DEC-0325's everything-mandatory rule, refining
  the original SES-0058 writes-mandatory/reads-discretionary
  recommendation with usage evidence: the SES-0067 wall-clock
  complaint and the finding that spawn overhead on bounded reads
  buys no isolation value. Decided at SES-0076.
links:
  relates-to: [DEC-0389, DEC-0390]
  derives-from: [SES-0076]
  supersedes: [DEC-0325]
---
# DEC-0388: Targeted artifact reads are de-mediated for every agent; librarian mediation remains mandatory for writes and synthesis reads

## Context

SES-0076 examined librarian-mediation efficiency: which artifact interactions require librarian mediation and which may go direct (skeleton restored at SES-0077).

## Decision

Any agent may directly invoke targeted, bounded-output read operations — overview, outline, section, citers, filtered listings, a single search, a single graph query — and consume the result as-is. Librarian delegation remains the sole sanctioned path for every write and for open-ended synthesis reads: precedent hunts, surveys, recall audits, and any task requiring iterative exploration or cross-artifact distillation. The boundary is output-shape plus judgment: no hard call cap, but an agent that catches itself chaining many calls delegates instead.

Raw Read/Grep/Glob of `docs/` remains forbidden outside existing DEC-0328-style charters.

## Rationale

The spawn overhead on bounded reads buys no isolation value, since the CLI's outputs are already context-shaped. The SES-0067 wall-clock complaint made the cost concrete. The original SES-0058 writes-mandatory/reads-discretionary recommendation is adopted here in refined form, with usage evidence behind it.

## Alternatives Considered

Retaining everything-mandatory delegation; making all reads discretionary with no boundary; an enumerated operation whitelist; a hard call-count cap.

## Implications

No separate implications were recorded at distillation; the operative consequences are stated in the Decision (skeleton restored at SES-0077).
