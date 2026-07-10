---
id: DEC-0321
type: decision
title: groundwork-design-session declares artifact-interact a mandatory Step-0 load
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0057 @ T11-T13"
overview: >-
  The groundwork-design-session SKILL.md instructs the facilitator to
  load the artifact-interact skill at Step 0 of every invocation — a
  hard dependency with a clear error path when the skill is not
  installed. artifact-interact is the single source of truth for
  artifact tool documentation; design-session prose never duplicates
  command syntax (references describe process moments and name the
  operation to use, linking to artifact-interact for the how). Chosen
  over an inline cheat-sheet (two places to keep in sync) and over
  relying on artifact-interact's own description-based triggering
  (under-triggering risk for a dependency the process cannot run
  without, given DEC-0312 makes its write API the only sanctioned
  write path).
links:
  derives-from: [SES-0057]
  relates-to: [DEC-0310, DEC-0312]
---

# DEC-0321: Mandatory Step-0 Load of artifact-interact

## Context

With design-session stripped of scripts (DEC-0310) and artifact
writes flowing only through artifact-interact (DEC-0312), the
consumption mechanism needed fixing — the stakeholder's T11 wording:
design-session "should reference this skill in its SKILL.md as an
autoload."

## Decision

design-session's SKILL.md makes loading artifact-interact a mandatory
Step-0 action (hard dependency, explicit error guidance if absent).
Command documentation lives only in artifact-interact; design-session
references name operations, not syntax.

## Rationale

The process cannot run without the tooling, so its load must not
depend on probabilistic triggering; a single documentation home
prevents the drift that dual-maintained cheat-sheets accumulate.

## Alternatives Considered

- **Reference + inline cheat-sheet** — faster in-session but two
  sync-coupled documentation sites; rejected.
- **Trigger-based load via skill description** — loosest coupling,
  under-triggering risk on a hard dependency; rejected.

## Implications

design-session SKILL.md Step 0 gains the load instruction at the
DEC-0320 cutover; all command examples migrate out of its prose.
