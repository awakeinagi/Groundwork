---
id: DEC-0471
type: decision
title: "The artifact model is evolving; migration is first-class Engine Core scope"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0089 @ T10, T11"
overview: >-
  Engine Core's charter needs a posture on artifact-model stability.
  Recent record shows repeated model change: the RSCH type
  (SES-0086/SES-0087), EP-0009's recharter (DEC-0445), the overview-
  field retrofit. SES-0089 decides the artifact model is treated as
  evolving rather than frozen: schema versioning, a migration
  mechanism, and backward compatibility for existing corpora become
  first-class Engine Core scope, rather than freezing the model at
  Engine Core's gate (which would make every later change a breaking
  event Adoption inherits the fallout of) or deferring to a model-
  change inventory during refinement (recent history already
  demonstrates the drift). Adoption's corpus-compatibility promises
  will depend on this migration mechanism.
links:
  derives-from: [SES-0089]
  relates-to: [DEC-0445, DEC-0462]
---

# DEC-0471: The artifact model is evolving; migration is first-class Engine Core scope

## Context

Engine Core's charter needs a posture on artifact-model stability. The
recent record shows repeated model change: the RSCH type
(SES-0086/SES-0087), EP-0009's recharter (DEC-0445), the overview-field
retrofit.

## Decision

The artifact model is treated as evolving: schema versioning, a
migration mechanism, and backward compatibility for existing corpora
are first-class Engine Core scope.

## Rationale

Assuming stability and being wrong breaks every adopted corpus on each
model change; assuming evolution and being wrong costs only a
rarely-exercised mechanism.

## Alternatives Considered

Freezing the model at Engine Core's gate (every later change becomes a
breaking event whose fallout Adoption inherits); deferring to a
model-change inventory during refinement (recent history already
demonstrates the drift).

## Implications

The migration mechanism is in-scope for Engine Core; Adoption's
corpus-compatibility promises depend on it.
