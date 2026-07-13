---
id: SP-0019
type: spike
title: "Schema-migration mechanism under the corpus-level SemVer marker"
status: approved
approved-on: 2026-07-13
approved-by: awakeinagi@gmail.com
owner: awakeinagi@gmail.com
created: 2026-07-13
timebox: 1d
overview: >-
  A one-day spike investigating the schema-migration mechanism owed
  under the corpus-level SemVer schema marker DEC-0483 establishes.
  It prototypes in-place rewrite against side-by-side migration by
  replaying the Research-type addition (DEC-0447 through DEC-0459)
  as a formal migration under each mechanism, measuring interrupted-
  migration recovery and full-checker verification, and records the
  Engine contract obligations for corpora it cannot migrate
  automatically. Commissioned by DEC-0487 at SES-0091 as EP-0010
  derived work under DEC-0471's first-class migration scope; drafted
  ahead of EP-0010's own gate and ratified by that gate's approval
  rather than gated individually.
links:
  derives-from: [EP-0010]
  satisfies: [BG-0002]
cites: [DEC-0487, DEC-0483, DEC-0471, DEC-0447, DEC-0459]
---

# SP-0019: Schema-migration mechanism under the corpus-level SemVer marker

## Question

Given a corpus-level SemVer schema marker (DEC-0483), what migration
mechanism moves an existing corpus from schema version X to Y safely,
and what does the Engine contract owe corpora it cannot migrate
automatically?

## Why It Blocks

DEC-0471 makes schema versioning and migration first-class EP-0010
scope, and migration stories cannot be written until the mechanism's
shape is known. The corpus-level marker (DEC-0483) already eliminates
lazy per-artifact migration; what remains — in-place rewrite (needing
interrupted-migration recovery) versus side-by-side migration (needing
double disk and a swap protocol) — carries sharply different contract
obligations. Open sub-questions include whether a migration runs
inside the transactional write path, how the frontmatter shape of
immutable artifacts (closed sessions, accepted decisions) is migrated
without violating immutability, and the compliance story for corpora
multiple versions behind. Commissioned by DEC-0487 at SES-0091; this
spike is drafted ahead within EP-0010's gate bundle and ratified by
the epic's own approval rather than gated individually.

## Method

Prototype both mechanisms against a copy of this project's corpus,
replaying a real historical schema change — the Research-type addition
(DEC-0447 through DEC-0459 introduced it) — as a formal migration
under each mechanism, measuring safety properties (interrupted-
migration recovery, verification via the full checker) and recording
the trade-offs. Timebox: one day.

The immutability sub-question may conclude as a constraint-finding —
a named constraint the chosen mechanism must satisfy — rather than a
fully designed solution within the timebox.

## Findings

Not started.

## Resulting Decisions

None yet; the spike must produce at least one decision at completion.
