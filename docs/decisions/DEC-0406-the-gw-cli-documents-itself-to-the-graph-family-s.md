---
id: DEC-0406
type: decision
title: "The gw CLI documents itself to the graph family's standard"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0077 @ T10-T11"
overview: >-
  The stakeholder directed that agents must be able to learn correct
  usage from --help alone; reconnaissance found the search and read
  families nearly undocumented and gw_write lacking short help,
  while the graph family was fully documented. The read, search,
  write, consistency, and coupling families adopt the graph family's
  standard: top-level description, short help and long description
  per subcommand, help on every argument, and an epilog with worked
  examples. The gw dispatcher keeps its hand-rolled exec design and
  its help text gains the complete family and subcommand map;
  check_links.py and status_report.py keep their current interfaces.
  The audit runs after the other items so it documents the post-
  change surface. Decided at SES-0077.
links:
  derives-from: [SES-0077]
  relates-to: [DEC-0316, DEC-0388]
---
# DEC-0406: The gw CLI documents itself to the graph family's standard

## Context

The stakeholder directed that agents must be able to learn correct usage from `--help` alone. Reconnaissance found the search and read families nearly undocumented, and `gw_write` lacking short help, while the graph family was already fully documented.

## Decision

The read, search, write, consistency, and coupling families adopt the graph family's standard: a top-level description, short help and a long description per subcommand, help on every argument, and an epilog with worked examples. The gw dispatcher keeps its hand-rolled exec design, but its own help text gains the complete family and subcommand map. `check_links.py` and `status_report.py` keep their current interfaces. This audit runs after every other item in the package, so it documents the post-change surface rather than a moving target.

## Rationale

Not separately recorded at distillation; the rationale is carried by the Context and Decision above and by the source session's transcript at the recorded source span (skeleton restored at SES-0077).

## Alternatives Considered

No alternatives were separately recorded at distillation (skeleton restored at SES-0077).

## Implications

No separate implications were recorded at distillation; the operative consequences are stated in the Decision (skeleton restored at SES-0077).
