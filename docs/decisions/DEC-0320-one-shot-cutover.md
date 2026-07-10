---
id: DEC-0320
type: decision
title: One-shot cutover — all references to old script locations updated, no shims
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0057 @ T12-T13"
overview: >-
  The extraction lands as a one-shot cutover: scripts move to
  artifact-interact in one change, and the same effort updates every
  reference — the groundwork-design-session SKILL.md and its
  references/*.md, the AGENTS.md asset and this project's installed
  AGENTS.md, and facilitator memory. No deprecation shims or
  forwarder scripts remain at the old paths. The cutover also
  executes the DEC-0318 migration: copy the skills into project-local
  .claude/skills, retire .agents/skills. Chosen over a transition
  period with forwarders, which adds cleanup debt for a single-
  operator project where all consumers update in the same change.
links:
  derives-from: [SES-0057]
  relates-to: [DEC-0310, DEC-0318]
---

# DEC-0320: One-Shot Cutover

## Context

Existing references to bundled script paths live in the
design-session SKILL.md, its references, the AGENTS.md asset,
installed project copies, and facilitator memory; the migration
needed a compatibility stance.

## Decision

One-shot cutover: scripts move in one change; all references update
in the same effort; no shims. The DEC-0318 skill-home migration
executes as part of it.

## Rationale

A single operator and a known, enumerable reference set make a
transition period pure debt; forwarders rot.

## Alternatives Considered

- **Deprecation shims printing the new location** — safer for stale
  docs and muscle memory, adds cleanup debt; rejected.

## Implications

The DEC-0322 build's definition of done includes the reference sweep
(SKILL.md, references, AGENTS.md asset + installed copy, memory) and
the .claude/skills migration with .agents/skills deletion.
