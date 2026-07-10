---
id: DEC-0327
type: decision
title: The manual-load escape hatch — explicit skill load sanctions direct use; agent definitions count
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0058 @ T7-T9"
overview: >-
  The single exception to mandatory librarian delegation (DEC-0325):
  direct use of the artifact-interact tooling is sanctioned when the
  skill has been manually loaded. "Manual" means an explicit load —
  by the human operator in the conversation, or by an agent
  definition that explicitly loads the skill (or explicitly charters
  a narrow raw-access surface). An agent-definition load counts as
  manual because the definition is versioned, reviewed, and
  stakeholder-ratified — the charter IS the sanction (DEC-0328
  applies this to the existing agents). What never sanctions direct
  use: description-based auto-triggering, which DEC-0326 disables
  anyway. This hatch is what lets the librarian itself work (its
  definition loads the skill), lets specialized subagents function
  despite being unable to spawn sub-subagents, and preserves an
  operator override for debugging and tooling work.
links:
  derives-from: [SES-0058]
  relates-to: [DEC-0325, DEC-0326, DEC-0328]
---

# DEC-0327: The Manual-Load Escape Hatch

## Context

Everything-mandatory delegation (DEC-0325) collides with two facts:
subagents cannot spawn subagents (so specialized agents like
overview-writer cannot delegate), and the librarian itself must use
the tooling directly. The stakeholder's T7 enforcement wording
carried the exception: "...unless the artifact-interact skill has
been manually loaded."

## Decision

Direct use of artifact-interact tooling is sanctioned if and only if
the skill was explicitly loaded:

- by the human operator in the live conversation, or
- by an agent definition that explicitly loads the skill or
  explicitly charters a narrow raw-access surface (confirmed at T9:
  a definition-level load counts as manual).

Auto-triggering from context never sanctions direct use — and is
disabled regardless (DEC-0326).

## Rationale

Agent definitions are versioned, reviewed artifacts the stakeholder
ratifies — an explicit load there is a deliberate human act, exactly
what "manual" is meant to capture. Without the definition clause, the
librarian itself and every chartered specialist would be standing
violations.

## Alternatives Considered

- **Operator-only manual load** — purest, but forces packet-rework of
  working agents (overview-writer, system-architect); rejected at T9.
- **Reads free, writes chartered** — per-operation boundary weakens
  the uniform rule; rejected.

## Implications

DEC-0328 recharters the existing agents under this rule. New
specialized agents wanting direct artifact access must have it
chartered in their definitions and ratified like any method change.
