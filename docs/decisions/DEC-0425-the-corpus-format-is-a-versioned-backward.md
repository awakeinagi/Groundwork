---
id: DEC-0425
type: decision
title: "The corpus format is a versioned, backward-compatible contract"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-12
source-span: "SES-0082 T10, T11, T21, T31"
accepted-in: SES-0082
overview: >-
  The corpus format is the versioned contract between all operating
  modes and consumers of a Groundwork corpus: a format-version
  marker is mandatory, evolution is additive-only, and a breaking
  change requires a migration tool plus its own decision record.
links:
  derives-from: [SES-0082]
  relates-to: [DEC-0263]
---

# DEC-0425: The corpus format is a versioned, backward-compatible contract

## Context

With multiple operating modes (solo, skill-only multi-user, application-hosted) all reading and writing the same markdown tree, SES-0082 needed to decide how the corpus's own file format evolves without breaking whichever mode isn't yet upgraded.

## Decision

The corpus format is the versioned contract between all operating modes and all consumers of a Groundwork corpus. A format-version marker is mandatory, evolution is additive-only, and a breaking change requires a migration tool and its own decision record.

## Rationale

Treating the corpus format as a contract rather than an implementation detail is what lets solo, skill-only, and application modes coexist and interoperate on the same repository even when they're running different tooling versions — each consumer can check the version marker and know what it's dealing with. Additive-only evolution keeps that contract cheap to honor; breaking changes are rare enough to warrant their own gated decision and migration tooling rather than ad hoc handling.

## Alternatives Considered

Leaving the format implicitly versioned (inferred from tooling version rather than stamped in the corpus) was rejected — it makes cross-mode compatibility unverifiable without running the tooling itself. Allowing breaking changes without a dedicated migration path was rejected as incompatible with DEC-0263's immutability invariants and with develop-branch release promotion (DEC-L), both of which depend on being able to trust a stamped format version.

## Implications

A format-version marker must be added to the corpus (or confirmed already present) and checked by the integrity checker. Any future breaking change to the artifact schema requires its own decision record plus a migration tool before it can ship.
