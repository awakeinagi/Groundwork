---
id: DEC-0291
type: decision
title: Bulk retrofit of all existing artifacts via a Haiku-pinned overview-writer agent
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0053 @ T6-T9"
overview: >-
  All existing artifacts (~438) receive generated overviews now, in one
  bulk pass, via a new versioned project agent .claude/agents/
  overview-writer pinned to Haiku 4.5 — the model choice lives in the
  agent definition's frontmatter so spawning logic can never forget the
  override. Generation is legal without per-artifact re-gating because
  overviews are derived and non-normative (DEC-0285). The stakeholder
  spot-checks a cross-type sample, and the checker rule (DEC-0287) lands
  in the same commit as the retrofit so coverage is never partial.
links:
  derives-from: [SES-0053]
  relates-to: [DEC-0285, DEC-0286, DEC-0287]
---

# DEC-0291: Bulk Retrofit via a Haiku-Pinned Overview-Writer Agent

## Context

The corpus holds ~438 artifacts predating the overview field. Tooling
can only rely on the field at full coverage (DEC-0287 ties the checker
rule to that moment). Generation at this volume wants a cheap model,
and prior incidents showed model choices made per-spawn get forgotten —
the stakeholder directed that the spawning logic always use the
appropriate model, suggesting a custom project agent (SES-0053 @ T7).

## Decision

All existing artifacts receive generated overviews **now, in one bulk
pass**, produced by parallel subagents running a new versioned project
agent definition, `.claude/agents/overview-writer.md`, with:

- **Haiku 4.5 pinned in the agent definition's frontmatter** — the
  model override is structural, not per-spawn;
- the DEC-0286 content standard and DEC-0285 non-normativity baked
  into its prompt;
- read/edit tools only, scoped to writing the `overview:` field.

The stakeholder spot-checks a cross-type sample of the output; the
checker rule (DEC-0287) and the retrofit land in the same commit.

## Rationale

Bulk-now is the only strategy under which the checker rule can enable
immediately — incremental coverage leaves tooling unable to rely on
the field for months. Generation without per-artifact re-gating is
legal precisely because overviews are derived and non-normative
(DEC-0285); the 250-word cap and human spot-check bound the quality
risk, making Haiku 4.5's cost profile the right fit. Pinning the model
in a versioned agent definition makes the choice durable and reusable
for future overview work (new artifacts, drift repair).

## Alternatives Considered

- **Big types first (sessions/CMPs), rest later** — spreads work but
  delays the checker rule until the tail lands.
- **Incremental on touch** — rejected: partial coverage indefinitely.
- **Sonnet 5 or split-by-type generation** — better transcript
  compression at 3–4× cost; rejected with spot-check as safety net.
- **Inline per-spawn model overrides, no custom agent** — rejected:
  the model discipline would live only in this session — a known
  process-gap pattern.

## Implications

`.claude/agents/overview-writer.md` joins the repo. Fan-out prompts
follow the parallel-subagent discipline (no whole-tree git operations
in agents sharing a tree; diff-audit after the fan-out). Future
artifacts get their overviews at authoring time (DEC-0287); the agent
remains available for regeneration and drift repair.
