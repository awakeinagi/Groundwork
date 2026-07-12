---
id: DEC-0439
type: decision
title: "The corpus format version lives in a root manifest file"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: stakeholder
source-span: "SES-0082 @ T41-T42"
overview: >-
  DEC-0425 mandates a versioned corpus format but not where the
  version marker lives. This decision places it in a small root-
  level manifest file (groundwork.yaml), the designated home for
  corpus-level metadata generally, extensible for needs like the
  docs-repo identity IDEA-0056 anticipates for code-only
  repositories. Per-artifact and git-metadata alternatives were
  declined in favor of one authoritative, file-tooling-visible
  location. Accepted at SES-0082 T42, confirming the T41
  recommendation.
links:
  derives-from: [SES-0082]
  relates-to: [DEC-0425, IDEA-0056]
---

# DEC-0439: The corpus format version lives in a root manifest file

## Context

DEC-0425 mandates that the corpus format be a versioned, backward-compatible contract, but did not specify where the version marker itself lives. A location was needed that any tooling operating on a copy of the corpus tree — including file-level tools with no git or database access — can reliably find.

## Decision

The corpus format-version marker mandated by DEC-0425 lives in a small manifest file at the corpus root (groundwork.yaml). The manifest is the designated home for corpus-level metadata generally — beginning with the format version, and available for future needs such as the docs-repo identity that code-only repositories would reference under the multi-repo territory captured in IDEA-0056.

## Rationale

A single root-level manifest gives one authoritative location that is visible to file-level tooling and preserved by any copy of the tree, without requiring database access or git history inspection to determine corpus compatibility.

## Alternatives Considered

Per-artifact version stamping and git-metadata-based alternatives were considered and declined: the manifest gives one authoritative location visible to file-level tooling and preserved by any copy of the tree, whereas per-artifact stamps or git metadata would scatter or hide the marker.

## Implications

Tooling that needs to check corpus format compatibility reads groundwork.yaml at the corpus root. The manifest is also the natural extension point for future corpus-level metadata, including a docs-repo identity field for code-only repositories under the multi-repo scenario in IDEA-0056.
