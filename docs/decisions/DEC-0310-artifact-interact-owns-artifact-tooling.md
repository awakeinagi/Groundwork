---
id: DEC-0310
type: decision
title: artifact-interact owns all artifact-touching tooling; groundwork-design-session becomes pure method
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0057 @ T11-T13"
overview: >-
  A new standalone skill, artifact-interact, becomes the single home
  of every artifact-touching ability: concise reads, the new typed
  write API, the shared frontmatter/structure parsing core, semantic
  search, the graph index, consistency checks, epic/story coupling
  checks, the status report, and ownership of the check_links.py and
  serve_docs.py sources that bootstrap installs into projects. The
  groundwork-design-session skill keeps zero scripts and becomes pure
  method: process references, question banks, templates. Scope grew
  during grilling from the initial "read tool + parsing core" split
  to the full toolbelt — the stakeholder's T11 amendment "all
  artifact related abilities will now live on this skill" governs.
  Narrows DEC-0116 (search remains its own gitignored index, but no
  longer a design-session script). Consumption relationship is set by
  DEC-0321 (mandatory Step-0 load).
links:
  derives-from: [SES-0057]
  relates-to: [DEC-0116, DEC-0289, DEC-0321]
---

# DEC-0310: artifact-interact Owns All Artifact-Touching Tooling

## Context

The stakeholder proposed breaking artifact parsing/reading abilities
out of groundwork-design-session into a standalone skill (SES-0057
T1). Grilling opened with a narrower split (read tool + parsing core
move; search/graph/analysis stay) which the stakeholder amended at
T11: all artifact-related abilities live on the new skill.

## Decision

`artifact-interact` is a new standalone skill owning every
artifact-touching ability: concise reads, the typed write API
(DEC-0312..DEC-0314), the shared parsing core, semantic search, the
graph index, consistency checks, the epic/story coupling checks, the
status report, and the sources of `check_links.py` and
`serve_docs.py` that bootstrap installs into projects.
`groundwork-design-session` retains zero scripts — it becomes pure
method (process references, question banks, templates) and consumes
artifact-interact per DEC-0321.

## Rationale

One home for artifact interaction gives a single parsing core (ending
per-script re-implementation), a single surface for agents to learn,
and a clean method/mechanism boundary: the design-session skill says
*what the process is*, artifact-interact says *how artifacts are
touched*.

## Alternatives Considered

- **Read tool + parsing core only move** (round-1 recommendation) —
  leaves search/graph/analysis split across skills; rejected by the
  T11 amendment.
- **Read + write only, no parsing consolidation** — persists the
  duplication that motivated the extraction; rejected.
- **Decide per script during build** — defers the boundary; rejected
  in favor of a complete roster now.

## Implications

DEC-0116's separate-script framing is narrowed (own index survives;
design-session homing does not). DEC-0289's homing is superseded via
DEC-0316. The design-session SKILL.md, its references, the AGENTS.md
asset, and installed project copies all require the DEC-0320 cutover.
The build runs under DEC-0322.
