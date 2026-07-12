---
id: DEC-0411
type: decision
title: "Lock primitive and chokepoint for gw concurrent writes"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0079 @ T3-T6"
overview: >-
  Defines the fcntl.flock-based read_lock/write_lock context
  managers and the exclusive-lock's apply-span scope, per the
  SES-0079 design gate.
links:
  derives-from: [SES-0079]
  relates-to: [DEC-0391, DEC-0317]
---

# DEC-0411: Lock primitive and chokepoint for gw concurrent writes

## Context

DEC-0391 mandates a shared/exclusive lock guarding the gw write path, but the four corpus readers (read, search, graph, check) and the writer currently share no access layer at all — code reconnaissance during this session's design gate (SES-0079 T3) confirmed no locking exists anywhere in the scripts.

## Decision

A new stdlib-only module `gw_lock.py` in the artifact-interact scripts directory provides `read_lock(root)` and `write_lock(root)` context managers over `fcntl.flock` on a single gitignored lockfile `<root>/.groundwork-lock`. Acquisition is non-blocking with retry to a deadline (10s for reads, 60s for writes, overridable via `GW_LOCK_TIMEOUT`), after which it refuses cleanly, naming the holder PID. Release is explicit at context-manager exit; kernel release-on-process-death is the crash fallback only, not the primary release path. The exclusive lock wraps the apply span exactly — corpus scan, ID allocation, edits, reciprocity bookkeeping, recheck, and graph sync — not whole-command execution; this scoping was a stakeholder amendment made at SES-0079 T4/T5.

## Rationale

A context-manager-scoped lock releases the instant the protected work finishes rather than waiting on OS cleanup after process exit, which the stakeholder specifically raised (SES-0079 T4) as the difference between a lock that frees promptly under normal operation and one that only frees via crash-fallback semantics. Scoping the exclusive hold to the read-modify-write unit — not just the bytes-on-disk writes — is required because ID allocation itself reads the corpus scan; a narrower lock would let the allocation race that DEC-0391 exists to close reopen.

## Alternatives Considered

Locking only around the bare per-file write calls was rejected: it leaves the corpus-scan-then-allocate step unprotected, so two writers could still observe the same "next ID" and collide — this is exactly the SES-0078/SES-0079 H1 collision recon turned up as a live instance the same day. Locking the whole command process (parse through output) was also rejected as unnecessarily coarse; argument parsing and output formatting carry no shared-state risk and don't need to wait on the lock.

## Implications

Every read family (read, search, graph, check) must acquire the shared lock before scanning live files so a read can never observe a torn mid-apply state; concurrent reads never block each other. `write_lock` becomes the sole entry point the apply span uses, replacing DEC-0394's interim single-write-librarian rule once the build ships and verifies (see the sibling verification-gate decision).
