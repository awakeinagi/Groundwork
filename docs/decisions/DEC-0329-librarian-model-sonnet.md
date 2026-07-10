---
id: DEC-0329
type: decision
title: The artifact-librarian runs on a Sonnet-class model, pinned and passed explicitly
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0058 @ T6-T7"
overview: >-
  The artifact-librarian runs on a Sonnet-class model (currently
  Sonnet 5). The choice follows the project's per-agent model-fitting
  precedents: overview-writer runs Haiku for mechanical single-field
  writes (DEC-0291), system-architect runs the strongest available
  model for judgment-heavy advising (DEC-0292); the librarian sits
  between — task-level intents require multi-step tool planning,
  invariant-respecting writes, and faithful distillation (more than
  Haiku reliably delivers), while toolbelt execution would waste the
  strongest tier, and per-interaction spawns make cost per spawn
  matter. Per the DEC-0292 pattern and standing facilitator practice,
  the model is pinned in the agent definition's frontmatter AND
  passed explicitly as the Agent tool's model parameter at every
  spawn — the frontmatter pin alone has been observed not to take
  effect. Callers inheriting their own model into the librarian is
  explicitly rejected (unpredictable cost; violates the
  explicit-pinning practice).
links:
  derives-from: [SES-0058]
  relates-to: [DEC-0324, DEC-0291, DEC-0292]
---

# DEC-0329: Sonnet-Class Model, Doubly Pinned

## Context

Each project agent fixes its model deliberately: Haiku for
overview-writer's mechanical writes (DEC-0291), strongest-available
for system-architect's judgment (DEC-0292). The librarian spawns on
every artifact interaction, so the cost/capability point matters.

## Decision

The artifact-librarian runs on a Sonnet-class model, recorded in the
agent definition's frontmatter and passed explicitly as the Agent
tool's `model` parameter at every spawn.

## Rationale

Task-level intents involve planning several operations, respecting
write invariants, and distilling results a caller will trust without
re-reading — judgment beyond the mechanical, but squarely workhorse
territory. Sonnet is fast and cheap enough to spawn per interaction.
The double pin (frontmatter + explicit spawn parameter) exists
because the frontmatter pin alone has been observed not to take
effect.

## Alternatives Considered

- **Haiku** — cheapest per spawn, but distillation judgment risk on
  "find what matters" tasks; rejected.
- **Inherit the caller's model** — unpredictable cost, violates the
  explicit-pinning practice; rejected.

## Implications

Every documentation surface that tells agents to spawn the librarian
(AGENTS.md instruction, design-session references) states the
explicit `model: sonnet` parameter.
