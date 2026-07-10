---
id: DEC-0316
type: decision
title: One unified artifact CLI with subcommand families and a JSON mode
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0057 @ T11-T13"
overview: >-
  The artifact-interact surface is one unified CLI: a single entry
  point with subcommand families — read, write, search, graph, check
  — under uniform --root and --json conventions, the shared parsing
  core underneath, compact output by default and JSON for
  programmatic use. The read side is redesigned in the move rather
  than transplanted: this supersedes DEC-0289 (the eight-affordance
  stdlib read tool homed in groundwork-design-session). The
  affordance intent of DEC-0289 carries forward — ID-addressed
  concise reads (overview, outline, section, element, item, turns,
  term, citers) remain the read family's basis, and the SES-0053
  division of labor (search answers "what's relevant", graph "how is
  it connected", reads "what does it say, cheaply") survives as the
  family split inside one tool. Exact affordance set and flags are
  fixed in the DEC-0322 build under its eval loop. Also narrows
  DEC-0116's separate-script framing; the search index remains its
  own gitignored artifact.
links:
  derives-from: [SES-0057]
  supersedes: [DEC-0289]
  relates-to: [DEC-0116, DEC-0310, DEC-0314, DEC-0317, DEC-0322]
---

# DEC-0316: One Unified Artifact CLI

## Context

With all artifact tooling moving to one skill (DEC-0310) and the
stakeholder electing to redesign the read side during the move
(SES-0057 T11), the shape of the consolidated surface had to be
fixed: unified CLI, harmonized separate scripts, or a usage-mined
fresh design.

## Decision

One unified CLI: a single entry point with read / write / search /
graph / check subcommand families, uniform `--root`/`--json`
conventions, compact-by-default output, the shared parsing core
underneath. Supersedes DEC-0289's framing (eight-affordance script
homed in the design-session skill); the concise-read affordances and
the SES-0053 division of labor carry forward as the read family's
basis. Affordance-level and flag-level design lands in the DEC-0322
build.

## Rationale

One tool to learn, one convention set, one parsing core — the
context-bloat and agent-efficiency goals of the proposal argue for a
single coherent surface over four scripts with drifting conventions.

## Alternatives Considered

- **Separate scripts, harmonized conventions** — smaller refactor,
  familiar entry points, but perpetuates surface fragmentation;
  rejected.
- **Usage-driven fresh design first** — mine sessions for read/write
  patterns before fixing the shape; rejected as a pre-step (the eval
  loop in the build covers this iteratively).

## Implications

DEC-0289 is superseded (its citers — DEC-0290, SES-0053 — reviewed
under the consistency sweep; DEC-0290's overview-inclusion rule
transfers to the unified CLI's search/graph families). DEC-0116 is
narrowed: own gitignored index survives, separate-script homing does
not. All command examples in design-session references and AGENTS.md
change at the DEC-0320 cutover.
