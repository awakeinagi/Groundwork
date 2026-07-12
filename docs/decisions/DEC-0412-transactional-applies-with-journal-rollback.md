---
id: DEC-0412
type: decision
title: "Transactional applies with journal rollback"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0079 @ T3-T6"
overview: >-
  Defines atomic per-file writes and journal-based rollback/crash
  recovery for gw_write apply, closing the rollback gap DEC-0401
  left deferred.
links:
  derives-from: [SES-0079]
  relates-to: [DEC-0391, DEC-0401]
---

# DEC-0412: Transactional applies with journal rollback

## Context

Recon at SES-0079 T3 found batch apply pre-validates its ops but leaves partial writes on disk when a mid-batch failure occurs; the op_apply failure path even carries a code comment explicitly deferring rollback to the DEC-0391 machinery. DEC-0401 (SES-0077) shipped truthful failure accounting — a manifest of applied/failed/not-attempted ops — but explicitly left transactional rollback itself out of scope pending this decision.

## Decision

Per-file writes become atomic via tempfile-plus-`os.replace`. Before an op or batch's first mutation, the original bytes of every file about to be touched, plus the list of any newly created files, are journaled under `<root>/.groundwork-journal/`. The journal is deleted on success. A recheck failure or any exception during the apply restores every journaled file's original bytes and removes any created files, spanning reciprocal-edge secondary files (e.g. the mirrored side of an `add-link`) as well as the primary target. The next process to acquire the lock rolls back any leftover journal before proceeding, covering crash recovery when a process dies mid-apply.

## Rationale

Truthful accounting (DEC-0401) tells a caller what happened; it does not undo a half-applied batch. Journaling original bytes rather than diffing forward is simple to reason about, cheap for the artifact sizes this corpus deals in, and makes rollback and crash recovery the same code path — the lock acquirer that finds a stale journal on startup performs the identical restore that a live process would perform on its own recheck failure.

## Alternatives Considered

Git-based rollback (relying on the working tree's version control) was rejected: DEC-0333 puts git entirely outside the tool's authority, and a git-backed rollback would require staging/commit operations the librarian is chartered never to perform. An in-memory-only transaction (buffer all writes, flush once at the end) was rejected because it doesn't cover the crash-recovery case — a process that dies before the final flush leaves nothing recorded to roll back from on the next run.

## Implications

Every write op's disk-touching step routes through the same atomic-replace-plus-journal path, not just `apply`'s batch loop — a single-op `write` call gets the same crash safety. The `.groundwork-journal/` directory must be gitignored alongside the lockfile. This decision directly retires DEC-0401's "rollback stays deferred" carve-out once implemented.
