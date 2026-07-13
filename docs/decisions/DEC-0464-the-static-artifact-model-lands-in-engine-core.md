---
id: DEC-0464
type: decision
title: "The static artifact model lands in Engine Core"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0089 @ T4, T13"
overview: >-
  DEC-0445 broadened EP-0009 to the dynamic artifact domain but
  explicitly excluded the static design of artifact types and
  scoping, leaving its epic placement open. SES-0089's derivation
  resolves this: the static artifact model (types, schemas,
  frontmatter, link semantics) merges into the Engine Core &
  Artifact Model epic rather than standing alone or living inside
  EP-0009. The Engine's validation, integrity checking, and parsing
  mechanics are defined in terms of the artifact model, so the two
  share a common closure that a standalone epic would only bisect.
  This cleanly separates Engine Core (what an artifact is) from
  EP-0009 (what is done with it) along the dynamic-versus-static
  seam DEC-0445 named.
links:
  derives-from: [SES-0089]
  relates-to: [DEC-0445, DEC-0462]
---

# DEC-0464: The static artifact model lands in Engine Core

## Context

DEC-0445 broadened EP-0009 to the dynamic artifact domain and left the
static design of artifact types and their scoping with the anticipated
Artifact model topic; the placement was open.

## Decision

The static artifact model — types, schemas, frontmatter, link
semantics — merges into the Engine Core & Artifact Model epic rather
than standing alone.

## Rationale

The Engine's mechanics are defined in terms of the artifact model:
validation, integrity checking, and parsing change whenever types
change (common closure). A standalone epic would be a seam neither
side can change across independently.

## Alternatives Considered

A standalone Artifact Model epic (no independent shippability);
placement inside EP-0009 (DEC-0445 explicitly excluded static design
from it).

## Implications

Engine Core defines what an artifact is; EP-0009 defines what is done
with it — the dynamic-versus-static seam DEC-0445 named.
