---
id: DEC-0414
type: decision
title: "Turn appends auto-number under the lock"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0079 @ T3-T6"
overview: >-
  Defines lock-protected auto-numbering of append-turn payloads plus
  an optional expected-first-turn precondition, per the SES-0079
  design gate.
links:
  derives-from: [SES-0079]
  relates-to: [DEC-0391, DEC-0376, DEC-0392]
---

# DEC-0414: Turn appends auto-number

## Context

Recon at SES-0079 T3 found turn numbers are caller-embedded with no precondition: an `append-turn` payload names its own "### T7 (...)" heading, so two concurrent appenders composing against the same last-seen turn number would both write "T7", producing a duplicate or out-of-order transcript — the mechanism behind the SES-0078/SES-0079 H1-style collision class recon surfaced.

## Decision

`append-turn` reads the live transcript's maximum turn number under the lock and renumbers the payload's turn heading(s) to continue from it, preserving the order the payload presented them in. An optional `--expect-first-turn N` precondition refuses cleanly (with a re-read instruction) when the transcript has advanced past what the caller expected, mirroring the section version-token refusal shape.

## Rationale

Auto-numbering removes the caller's need to predict the next turn number at all under normal operation — the lock-protected read-then-renumber happens atomically as part of the write itself, so there's no window between "caller computes next number" and "caller writes it" for another writer to land in. The optional precondition exists for callers who specifically need to detect that the transcript moved (e.g. a facilitator restating an exchange that assumes no interleaving occurred).

## Alternatives Considered

Requiring every append-turn caller to pass the expected next-turn number unconditionally (make the precondition mandatory, not optional) was rejected: it would break the common case of a caller who genuinely doesn't care what number lands, just that their content is appended in order, forcing an unnecessary read before every append.

## Implications

Callers should stop hand-writing turn numbers in payloads meant to land immediately after the current end of a transcript; the payload's heading number becomes advisory and gets overwritten. Batches that append multiple turns in one `write apply` call get sequential numbers assigned in payload order, computed once against the transcript's state at lock acquisition.
