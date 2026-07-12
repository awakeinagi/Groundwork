---
id: DEC-0384
type: decision
title: "Body H1 identity: create stamps allocated IDs into placeholder H1s; recheck and checker rule 24 enforce own-ID H1s"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0072 @ T19-T21"
overview: >-
  Bodies are authored before their ID exists, so create replaces a
  leading "# PREFIX-XXXX:" H1 with the allocated ID; the per-op
  recheck and checker rule 24 refuse/flag a body H1 carrying an
  unallocated ID placeholder or leading with another artifact's ID.
  Motivated by SES-0072's own record shipping with "# SES-XXXX:" and
  no safe API path to fix an H1; the sweep also caught DEC-0368's
  H1.
links:
  derives-from: [SES-0072]
---

# DEC-0384: Body H1 identity: create stamps allocated IDs into placeholder H1s; recheck and checker rule 24 enforce own-ID H1s

## Context

No op reaches an H1, and nothing verified H1/ID consistency — the placeholder state was invisible and unrepairable in-API.

## Decision

Stamp at create; enforce identity at recheck and in the checker.

## Rationale

Prevention at the only moment the ID becomes known, plus a corpus-wide detection net.

## Alternatives Considered

An H1-rewrite op (new mutation surface for a display-only line); librarian pre-derives the next ID (racy, and the old memory guidance that caused this).

## Implications

The body authoring convention is "# PREFIX-XXXX: <title>"; librarian memory updated.
