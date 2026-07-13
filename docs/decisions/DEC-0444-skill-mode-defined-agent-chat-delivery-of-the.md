---
id: DEC-0444
type: decision
title: "skill-mode defined: agent-chat delivery of the paradigm, no Application"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-12
source-span: "SES-0085 T7, T9"
overview: >-
  skill-mode is defined as the delivery mode where a user interfaces
  with the Groundwork paradigm entirely through an agent-chat
  runtime (Claude Code, GitHub Copilot, Codex, OpenCode, and
  similar) via the Groundwork skills, with no Application or UI
  involved. The gw CLI is the substrate the skills drive, not the
  mode itself — raw CLI or script use is direct Engine access, not a
  named delivery mode. skill-mode is the paradigm's core subset per
  DEC-0433, and enters CONTEXT.md as a glossary term.
links:
  derives-from: [SES-0085]
  relates-to: [DEC-0421, DEC-0422, DEC-0433]
---

# DEC-0444: skill-mode defined: agent-chat delivery of the paradigm, no Application

## Context

The locate-first sweep (T4) flagged that "skill-mode" had no glossary entry despite being load-bearing in DEC-0421, DEC-0422, and DEC-0433. Round 1 card 3 asked whether to define it now; the stakeholder gave a starting definition (T7: "when a user interfaces with the Groundwork paradigm via an agent chat only... like Claude Code, Github Copilot, Codex, OpenCode, etc., no app/UI"). Round 2 card 4 then posed the CLI edge case: does raw gw CLI or script use, with no agent involved, count as skill-mode?

## Decision

skill-mode is the delivery mode in which a user interfaces with the Groundwork paradigm entirely through an agent-chat runtime — Claude Code, GitHub Copilot, Codex, OpenCode, and similar — via the Groundwork skills, with no Application or UI involved.

## Rationale

The gw CLI is the substrate the skills drive, not the mode itself: raw CLI or script use is direct Engine access, not a named delivery mode.

## Alternatives Considered

Round 2 offered three readings of the CLI edge: agent-chat defines it and the CLI is merely the substrate (recommended); any non-app use counts as skill-mode; or keep grilling before deciding. The stakeholder confirmed the recommended reading — "Agent-chat defines it (Recommended)" (SES-0085 T9).

## Implications

skill-mode is the paradigm's core subset per DEC-0433, and the definition enters CONTEXT.md as a glossary term.
