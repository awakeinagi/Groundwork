---
id: IDEA-0044
type: idea
title: "Type-aware frontmatter validation at create time and in the checker"
status: taken-up
owner: awakeinagi@gmail.com
created: 2026-07-12
proposed-by: awakeinagi
overview: >-
  Create currently accepts --field frontmatter values with no
  validation against the type's SPEC. Proposal: create validates
  known per-type fields against a small schema derived from the
  SPECs (enums such as transcript-fidelity verbatim|reconstructed,
  scalar-versus-list shapes such as the one-participant session
  model per DEC-0021), refusing invalid values at write time; a
  matching checker rule applies the same schema corpus-wide to catch
  already-shipped instances. Fields outside the schema stay open for
  extension via --field. Spark context: SES-0073 was created with an
  off-spec transcript-fidelity value and list-valued participant
  fields; the close gate checks presence only, so nothing caught it
  until a human read the spec directly. Disposition: pending.
links:
  relates-to: [IDEA-0045]
  derives-from: [SES-0075]
---

# IDEA-0044: Type-aware frontmatter validation at create time and in the checker

## The Idea

Create validates known per-type frontmatter fields against a small schema derived from the SPECs (enums such as transcript-fidelity verbatim|reconstructed, scalar-versus-list shapes such as the one-participant session model per DEC-0021), refusing invalid values at write time; a matching checker rule applies the same schema corpus-wide to catch shipped instances. Fields not in the schema stay open for extension via --field.

## Spark Context

SES-0073 was created with off-spec transcript-fidelity and list-valued participant fields; the close gate checks presence only, so nothing caught it until a human read the spec.

## Disposition

Taken up via SES-0077. DEC-0402 adds a `FIELD_SCHEMA` table validating typed frontmatter fields at create, in the recheck, and via a new corpus-wide checker rule.

