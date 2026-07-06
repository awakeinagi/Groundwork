---
id: DEC-0035
type: decision
title: Append-only transcripts enforced by the store; sessions ride the item branch
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0003 @ T4-T5"
links:
  derives-from: [SES-0003]
---

# DEC-0035: Store-enforced append-only transcripts, on the item branch

## Context

Transcripts are the root of the provenance chain
([DEC-0015](DEC-0015-transcript-decision-citation-chain.md)); their
append-only property needed an enforcement point, and session artifacts
needed a home within the fork-pull branching model.

## Decision

The storage API is type-aware: for session artifacts it exposes only
`append-turn` and `close` operations — no edit or delete of existing turns,
enforced server-side regardless of caller. Sessions and their distilled
decisions are committed to the item branch as refinement proceeds
([DEC-0028](DEC-0028-fork-pull-pr-gating.md)) and land on main with the
item's PR merge — approving the item also ratifies its provenance trail.

## Rationale

Enforcement at the store survives buggy or prompt-injected agents (a
convention does not), and bundling provenance with the item's PR means the
gate reviewer sees the *why* alongside the *what*.

## Alternatives Considered

- **Agent-enforced convention**: one compromised rewrite silently corrupts
  the provenance record.
- **Separate append-only log store**: strong immutability but splits
  canonical truth out of the repo.

## Implications

Session append operations are mechanical writes under
[DEC-0033](DEC-0033-typed-mechanical-writes.md); the tier-2 PR checks
([DEC-0034](DEC-0034-two-tier-validation.md)) verify transcript history was
never rewritten (append-only diff over session files).
