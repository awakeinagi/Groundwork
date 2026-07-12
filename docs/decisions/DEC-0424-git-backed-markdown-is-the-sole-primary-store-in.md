---
id: DEC-0424
type: decision
title: "Git-backed markdown is the sole primary store in every mode"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-12
source-span: "SES-0082 T10, T11, T12, T21, T31"
accepted-in: SES-0082
overview: >-
  The markdown artifact tree in git is the sole primary store in
  every operating mode; any application database is a derived, read-
  optimized projection rebuilt from the file tree, with application
  writes going through the shared engine under the DEC-0391 lock
  model. The engine defines a corpus-access port now, keeping
  storage reversible if scale triggers fire.
links:
  derives-from: [SES-0082]
  relates-to: [BG-0001, DEC-0391, DEC-0263, DEC-0416]
---

# DEC-0424: Git-backed markdown is the sole primary store in every mode

## Context

The architects' converged decomposition assumed git-primary storage, but SES-0082 needed to settle explicitly whether an application-mode database is ever the source of truth, and how that storage decision stays reversible if usage scale later demands otherwise.

## Decision

The markdown artifact tree in git is the sole primary store for Groundwork corpora in every operating mode. Any application database is a derived, read-optimized projection rebuilt from the canonical file tree, and application writes go through the shared engine to the files under the DEC-0391 lock model. The engine defines a corpus-access port even while the git-filesystem adapter is its only implementation, keeping the storage decision reversible if the armed scale triggers fire.

## Rationale

Git-backed markdown is what makes solo god-mode, skill-only multi-user mode, and the application all interoperate on the same corpus without a synchronization layer between competing sources of truth — any of them can read the files directly. A corpus-access port costs little to define now and preserves the option to swap in a different storage backend later without an application-wide rewrite, should TRG-scale triggers ever fire.

## Alternatives Considered

Making the application's database the primary store (with git as an export target) was rejected — it would break standalone skill-mode use, which depends on the files being authoritative, and would violate DEC-B's standing that the paradigm never requires the application. Skipping the corpus-access port and hard-coding filesystem access throughout the engine was rejected as a needless foreclosure of a reversible-by-design decision.

## Implications

Application-side caching or indexing layers must be built as projections with a defined rebuild path, never as an alternate write target. The corpus-access port is a concrete interface the engine (DEC-D) must expose from day one, even with a single git-filesystem implementation.
