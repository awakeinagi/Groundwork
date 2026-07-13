---
id: DEC-0482
type: decision
title: "EP-0010 owns both the artifact-type roster and the type machinery; roster changes ride schema migration"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-13
source-span: "SES-0091 @ T12-T13"
overview: >-
  The fixed artifact-type roster and the type system it plugs into
  could have one owner or two. This decision gives EP-0010 ownership
  of both the roster and the type machinery, with roster changes
  riding schema-version bumps through the model-evolution/migration
  path and no separate type-extension mechanism, closing the back
  door to an implicit type registry.
links:
  derives-from: [SES-0091]
  relates-to: [DEC-0464, DEC-0470, DEC-0471, DEC-0483]
---

# DEC-0482: EP-0010 owns both the artifact-type roster and the type machinery; roster changes ride schema migration

## Context

The fixed list of artifact types and the type system it plugs into could have one owner or two.

## Decision

EP-0010 owns both the artifact-type roster — the fixed list of artifact types and their schemas — and the type machinery. Roster changes are schema-version bumps that ride the model-evolution and migration path; no extension mechanism for types exists.

## Rationale

DEC-0464 places the static model in this epic and DEC-0470's opinionated-and-fixed posture removes any extension-point argument for separating the roster from the machinery; a split owner invites a type registry by the back door.

## Alternatives Considered

Machinery-only ownership with the roster elsewhere was rejected as creating a second owner for half the artifact model.

## Implications

Future type additions, like the Research type added via DEC-0447 through DEC-0459, land as versioned schema changes with migrations.
