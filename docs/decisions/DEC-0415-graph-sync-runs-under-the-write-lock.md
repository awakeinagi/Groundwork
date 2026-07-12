---
id: DEC-0415
type: decision
title: "Graph sync runs under the write lock"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0079 @ T3-T6"
overview: >-
  Defines best-effort graph sync inside the exclusive-lock apply
  span and shared-lock protection for out-of-band graph/search
  rebuilds.
links:
  derives-from: [SES-0079]
  relates-to: [DEC-0391, DEC-0317]
---

# DEC-0415: Graph sync under the lock

## Context

Recon at SES-0079 T3 found graph/search sync is fully out-of-band today — nothing coordinates it with the write path, so a reader querying the graph mid-write could see a stale or partially-synced index, and DEC-0317's layered-dependency design keeps the graph/search engines opt-in via `uv` rather than a hard stdlib dependency of the write path.

## Decision

After the post-write recheck passes and before the exclusive lock is released, `gw_write` runs graph sync as a best-effort subprocess, invoked only when `uv` and an existing graph store are both present. A sync failure is reported as a warning; it never fails the write itself. Out-of-band graph and search rebuild commands take the shared (read) lock during their live-file scans, so they cannot observe a torn mid-apply state either.

## Rationale

Running sync inside the exclusive-lock span, rather than after release, keeps the graph consistent with the corpus state a subsequent reader will see — no gap where the lock is free but the graph is still stale. Making it best-effort (warn, don't fail) preserves DEC-0317's layering: a write must succeed on the stdlib-only core even when `uv` or the graph store isn't available in a given environment, since graph/search are opt-in heavy families, not hard requirements.

## Alternatives Considered

Making graph sync a hard precondition of a successful write (fail the write if sync fails) was rejected as it would turn an opt-in heavy dependency into a de facto mandatory one, contradicting DEC-0317. Running sync entirely outside the lock (fire-and-forget after release) was rejected because it reopens the same torn-state window this decision closes — a reader could query the graph in the gap between lock release and sync completion and see pre-write state inconsistently mixed with a stale index.

## Implications

Environments without `uv` or without an initialized graph store get writes with no sync attempt and no warning noise; environments with both get synced graphs at the cost of a slightly longer exclusive-lock hold per write. Out-of-band rebuild tooling must be updated to take the shared lock, not skip locking on the assumption that rebuilds are read-only.
