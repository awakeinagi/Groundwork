---
id: DEC-0413
type: decision
title: "Per-section version tokens for gw reads and writes"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0079 @ T3-T6"
overview: >-
  Defines derived sha256-based section version tokens and the --if-
  match precondition on content-mutating write ops, per the SES-0079
  design gate.
links:
  derives-from: [SES-0079]
  relates-to: [DEC-0391]
---

# DEC-0413: Per-section version tokens

## Context

Recon at SES-0079 T3 found reads emit no version information at all: a caller who reads a section, composes an edit, and applies it has no way to detect that the section changed underneath them between the read and the write — a torn-write risk DEC-0391 names but does not itself specify a mechanism for.

## Decision

Reads of sections, outlines, and overviews emit a derived token (`v:` plus the first 12 hex characters of the sha256 of the normalized section text); nothing is stored in the artifact files themselves — the token is computed on demand from live content. Section-content-mutating write ops (`edit-section`, `update-overview`, and their batch forms) require an `--if-match` token and refuse on mismatch with a re-read instruction. `create` takes no token, since it has no prior content to race against. Link, status, and cite ops rely on the lock plus the post-write recheck rather than a token, since they mutate frontmatter/metadata rather than section prose a concurrent editor might also be composing against.

## Rationale

A derived, unstored token keeps the mechanism stateless and side-effect-free on read — no new frontmatter field, no write-on-read. Scoping the requirement to content-mutating ops (not every write) matches where a stale-composition race actually causes silent data loss: overwriting someone else's just-landed section edit with a payload composed against an older version.

## Alternatives Considered

A corpus-wide single version counter was rejected as unnecessarily coarse — it would invalidate every in-flight edit whenever any unrelated artifact changed, not just the one being composed against. Storing the token in frontmatter (persisted rather than derived) was rejected because it adds a file-format field purely for concurrency bookkeeping with no meaning to a human reader, and it would itself need locking to update consistently.

## Implications

Callers composing an edit must pass through the token from their most recent read; a caller that reads once and issues several edits across a task must re-read (and get a fresh token) between them. `write apply` batches referencing the same section twice need the second op to use the token the first op's result reports, not the original read's token.
