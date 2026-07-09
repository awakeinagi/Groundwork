---
id: DEC-0123
type: decision
title: Embedding model identity and dimensionality are stamped on the vector index; mismatch refuses service and forces re-embed
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
overview: >-
  The embedding port contract exposes the adapter's model identity and
  vector dimensionality. The vector store stamps both onto every index.
  On mismatch between configured embedding adapter and index stamp, the
  system refuses to serve results from the stale index and requires full
  re-embed before semantic search resumes. This converts silent corruption
  of incomparable vectors into a loud, actionable state. Stamping identity
  matters because two models can share a dimension and still be incomparable.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0020 @ T4-T5, T6-T7"
links:
  derives-from: [SES-0020]
  relates-to: [DEC-0067, DEC-0121, DEC-0122]
---

# DEC-0123: Embedding Identity Stamping and Forced Re-embed on Mismatch

## Context

A pluggable embedding port (DEC-0121)
creates a silent failure mode: vectors from different models are
incomparable (and often differently dimensioned), so a config-time model
swap (DEC-0122) against an
existing index would return garbage similarity scores with no error.
DEC-0067 already pinned the
embedding-model version with "swap = re-embed batch"; the port contract
must make that enforceable.

## Decision

The embedding port contract must expose the adapter's **model identity
and vector dimensionality**. The vector store stamps both onto every
index it builds. On mismatch between the configured embedding adapter
and the index stamp, the system **refuses to serve** results from the
stale index and requires a **full re-embed** before semantic search
resumes. Whether the rebuild runs automatically or waits for operator
confirmation is story-level detail.

## Rationale

The failure is invisible without contract machinery — search keeps
returning plausible-looking, meaningless rankings. Refusing service
converts silent corruption into a loud, actionable state. Stamping
identity (not just dimensionality) matters because two models can share
a dimension and still be incomparable.

## Alternatives Considered

- **Leave it to adapter documentation** — trusts operators to remember
  the re-index rule; rejected because the failure mode gives no signal
  when they forget.
