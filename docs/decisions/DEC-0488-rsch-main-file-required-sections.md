---
id: DEC-0488
type: decision
title: "RSCH main-file required sections"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi
decided-on: 2026-07-13
source-span: "SES-0092"
overview: >-
  The Research main file carries these required sections in order:
  Inspiration, holding the investigation's trigger context from the
  intake session; Research Goals as a numbered list; Method; Source
  Register; one Round section per research round; Derived Work,
  present from creation with "None yet." as legal content; and
  Subtopic Files, required exactly when the artifact's subfile
  directory exists. Sections may be brief but must exist, per SPEC-
  artifact-common's body conventions. This fixes a single stable
  shape for every Research artifact so create-time skeleton guards
  and the checker can enforce structural completeness the same way
  they do for every other Groundwork type.
links:
  derives-from: [SES-0092]
  relates-to: [DEC-0447, DEC-0453]
---

# DEC-0488: RSCH main-file required sections

## Context

SPEC-research needs a definitive, checkable list of the Research main
file's required body sections, in order, so a create-time skeleton
guard and the checker can enforce structural completeness the same
way they do for every other artifact type.

## Decision

The Research main file carries these required sections in order:
Inspiration, holding the investigation's trigger context from the
intake session; Research Goals as a numbered list; Method; Source
Register; one Round section per research round; Derived Work, present
from creation with "None yet." as legal content; and Subtopic Files,
required exactly when the artifact's subfile directory exists.
Sections may be brief but must exist, per SPEC-artifact-common's body
conventions.

## Rationale

Each section carries a distinct, non-overlapping duty in the
investigation's lifecycle — trigger context, targets, procedure,
evidence, per-pass record, downstream consequence, and optional
elaboration — and fixing their order and presence lets both the
create-time skeleton guard and downstream tooling (templates, the
design-session skill, the checker) rely on a single stable shape
across every Research artifact.

## Alternatives Considered

A looser, author's-choice section set was considered and rejected: it
would make the checker's completeness rules unenforceable and would
leave agents guessing where new content belongs, defeating the
progressive-disclosure benefit fixed structure gives every other
Groundwork type.

## Implications

The create-time skeleton guard (DEC-0407's pattern) must recognize
this exact section list for type=research. Derived Work's
"None yet." default and Subtopic Files' conditional requirement are
both testable preconditions the checker can verify mechanically.
