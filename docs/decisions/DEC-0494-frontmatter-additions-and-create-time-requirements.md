---
id: DEC-0494
type: decision
title: "Frontmatter additions and create-time requirements"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi
decided-on: 2026-07-13
source-span: "SES-0092"
overview: >-
  Research frontmatter adds commissioned-by, a person identifier;
  source-mode, an enum of provided, seeded, and agent-sourced per
  DEC-0451; and the inspired reciprocal link list. links.derives-
  from must name the intake session per DEC-0449. commissioned-by,
  source-mode, and derives-from are demanded at creation under the
  DEC-0417 pattern. No loop state is mirrored into frontmatter: the
  latest round's Goals Assessment is the loop's authoritative state.
links:
  derives-from: [SES-0092]
  relates-to: [DEC-0417, DEC-0449, DEC-0451]
---

# DEC-0494: Frontmatter additions and create-time requirements

## Context

Research needs frontmatter fields distinct from every other type —
who commissioned it, how its sources are gathered, and which session
it traces to — and those fields need to be enforced at creation
rather than left to drift in afterward.

## Decision

Research frontmatter adds commissioned-by, a person identifier;
source-mode, an enum of provided, seeded, and agent-sourced per
DEC-0451; and the inspired reciprocal link list. links.derives-from
must name the intake session per DEC-0449. commissioned-by,
source-mode, and derives-from are demanded at creation under the
DEC-0417 pattern. No loop state is mirrored into frontmatter: the
latest round's Goals Assessment is the loop's authoritative state.

## Rationale

Demanding these fields at create time (rather than allowing a
commissioned-by-less or session-less Research artifact to exist
transiently) closes the same provenance gap DEC-0417 already closed
for sessions; keeping loop state out of frontmatter avoids a second,
driftable copy of information the round sections already carry
authoritatively.

## Alternatives Considered

Making commissioned-by and source-mode optional-but-recommended was
considered and rejected: it would let provenance-bare Research
artifacts exist, undermining the same accountability guarantee
DEC-0417 established. Mirroring the current loop state into
frontmatter (e.g. a "goals-remaining" field) was considered and
rejected as a drift surface with no independent value over reading
the latest round.

## Implications

`create --type research` refuses without --field values for
commissioned-by, source-mode, and links.derives-from, per the
REQUIRED_AT_CREATE table's established pattern.
