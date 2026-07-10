---
id: DEC-0328
type: decision
title: Existing specialized agents are rechartered under the escape hatch
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0058 @ T8-T9"
overview: >-
  Applies DEC-0327's agent-definition clause to the two existing
  project agents, which touch docs/ directly and cannot delegate
  (subagents cannot spawn subagents). overview-writer is rechartered
  to explicitly load the artifact-interact skill and perform its
  writes through the typed update-overview operation instead of raw
  Edit — its definition load counts as manual, and its write surface
  narrows to exactly the one operation its purpose requires.
  system-architect keeps its corpus access as an explicit read-only
  charter stated in its definition (Read/Grep/Glob over docs/; it
  advises, never edits — unchanged behavior, now explicitly
  sanctioned). Recall-audit judge subagents continue to receive
  facilitator-prepared packets and need no charter. The
  agent-definition charter is the standing sanctioning mechanism:
  any future specialized agent wanting direct artifact access gets it
  the same way — an explicit, ratified charter in its versioned
  definition, never ambient access.
links:
  derives-from: [SES-0058]
  relates-to: [DEC-0327, DEC-0291, DEC-0292, DEC-0313]
---

# DEC-0328: Recharter the Existing Specialized Agents

## Context

Under everything-mandatory delegation (DEC-0325), overview-writer
(raw Edit on overview fields, DEC-0291) and system-architect
(Read/Grep/Glob over the corpus, DEC-0292) would be standing
violations — and neither can delegate, since subagents cannot spawn
subagents.

## Decision

- **overview-writer**: definition explicitly loads artifact-interact;
  all writes go through the typed `update-overview` operation
  (DEC-0313) instead of raw Edit. Read access for context remains.
- **system-architect**: definition gains an explicit read-only
  corpus charter (Read/Grep/Glob over docs/; never edits). Behavior
  unchanged; sanction made explicit.
- **Recall-audit judges**: no charter — they consume
  facilitator-prepared packets, as today.
- **Standing mechanism**: future specialized agents obtain direct
  artifact access only via an explicit charter in their ratified
  agent definition.

## Rationale

The charter route keeps both agents working without packet rework
while ending ambient, unsanctioned access. Narrowing overview-writer
to the typed operation also closes the last raw-write path a project
agent held, completing DEC-0312's guardrail story.

## Alternatives Considered

- **Facilitator pre-packages everything** — purest mandate; reworks
  two working agents and bloats packets; rejected.
- **Reads free for all subagents** — per-operation boundary,
  weakens the uniform rule; rejected.

## Implications

Both agent definitions are edited in the SES-0058 build. The
overview-writer recharter lands with the artifact-interact build
(DEC-0334) since the update-overview operation must exist first.
