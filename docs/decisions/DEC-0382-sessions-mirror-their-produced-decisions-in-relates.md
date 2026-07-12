---
id: DEC-0382
type: decision
title: "Sessions mirror their produced decisions in relates-to, enforced by checker rule 23, with full historical backfill"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0072 @ T15-T18"
overview: >-
  Every decision whose derives-from names a session must appear in
  that session's links.relates-to (SPEC-session semantics amended to
  "artifacts the session refined or produced"); decisions deriving
  from spikes keep the existing cites back-link convention, which
  rule 23 also enforces. The survey found no session in the corpus
  carried the edge (~373 missing links across 65 sessions); full
  backfill was chosen over a forward-only cutoff and executed as
  add-link batches under DEC-0248 cross-reference enrichment,
  keeping the rule stateless.
links:
  relates-to: [DEC-0383]
  derives-from: [SES-0072]
---

# DEC-0382: Sessions mirror their produced decisions in relates-to, enforced by checker rule 23, with full historical backfill

## Context

SES-0064's empty relates-to surfaced that the session→decision edge existed only on the decision side; the graph could not answer "what did this session produce" from the session.

## Decision

The relates-to list mirrors produced decisions; rule 23 enforces both the session path and the spike-cites path; history is backfilled in full.

## Rationale

The derives-from link already encodes "produced" precisely, so the session side needs only a generic mirror inside the closed link vocabulary; a grandfather cutoff would bake arbitrary state into the checker forever.

## Alternatives Considered

A dedicated produces/produced-by link pair (duplicates derives-from, touches every tool); forward-only enforcement.

## Implications

SPEC-session amended; ~65 closed sessions gained relates-to entries (and Post-Close Enrichment mentions where prose lacked them, per DEC-0248/DEC-0250).
