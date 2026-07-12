---
id: DEC-0349
type: decision
title: "system-architect frontmatter stays model: claude-opus-4-6 (stakeholder call)"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-10
decided-by: awakeinagi
decided-on: 2026-07-10
source-span: "SES-0063 @ T13"
overview: >-
  Although `claude-opus-4-6` is absent from official Anthropic model
  documentation (current lineup: claude-fable-5, claude-opus-4-8,
  claude-sonnet-5, claude-haiku-4-5-20251001), SES-0063's restart-
  once matrix (arm C', 2026-07-10) showed it demonstrably resolves
  and runs, self-reporting "Opus 4.6 with 1M context" at reasoning
  effort 99/100 under frontmatter effort: high - the highest effort
  of any probe arm in the session. At T13's ratification round the
  stakeholder chose to keep `model: claude-opus-4-6` in the system-
  architect frontmatter on these empirical grounds, against the
  claude-fable-5 recommendation (the documented strongest GA model)
  and the 'fable' alias. Revisit if the identifier stops resolving
  or is deprecated.
links:
  derives-from: [SES-0063]
  relates-to: [DEC-0292, DEC-0348, DEC-0347, DEC-0418]
cites: [DEC-0292, DEC-0348]
---

# DEC-0349: system-architect Frontmatter Stays `model: claude-opus-4-6` (Stakeholder Call)

## Context

IDEA-0016 and IDEA-0023 both flagged that `claude-opus-4-6`, the
model string in `.claude/agents/system-architect.md`'s frontmatter, is
absent from official Anthropic model documentation — the current
documented lineup is claude-fable-5, claude-opus-4-8, claude-sonnet-5,
and claude-haiku-4-5-20251001. SES-0063's restart-once matrix (T10,
arm C′) tested this exact string post-restart: three spawns of the
`effort-probe` agent (frontmatter `model: claude-opus-4-6`, `effort:
high`) all self-reported running as "claude-opus-4-6[1m] (Opus 4.6
with 1M context)" at a reasoning effort of 99/100, read from a
reasoning-effort tag — the highest effort observed across all eight
probe arms in this session.

## Decision

Despite not appearing in official documentation, `claude-opus-4-6`
demonstrably resolves and runs, at the highest effort of any tested
arm. At T13's ratification round, the stakeholder (awakeinagi) was
presented three options for the system-architect frontmatter model
string — keep `claude-opus-4-6`, switch to `claude-fable-5` (the
documented strongest GA model, the facilitator's recommendation), or
switch to the `fable` alias — and ratified keeping `model:
claude-opus-4-6`, against the recommendation, on the empirical
grounds recorded above. The frontmatter is left unchanged. This
decision should be revisited if the identifier stops resolving or is
formally deprecated.

## Rationale

The stakeholder's call rests on direct, repeated empirical evidence
from this project's own probe harness (three consistent spawns, arm
C′) rather than on what current published documentation lists — the
string resolves to a real, functioning, high-effort-capable model
regardless of its absence from the documented lineup. Changing it to a
documented-but-unverified-in-this-harness alternative would trade a
proven-working configuration for an unproven one on documentation
grounds alone.

## Alternatives Considered

- **claude-fable-5** (documented strongest GA model) — the
  facilitator's recommendation; rejected by the stakeholder in favor
  of the empirically-verified string already in place.
- **The `fable` alias** — rejected for the same reason; also carries
  the ambiguity noted in SES-0062/IDEA-0023 that alias strings and
  resolved snapshot IDs are not the same thing for audit purposes.
- **Leave the question open pending further docs research** — rejected
  as unnecessary; the empirical evidence from this session's own
  restart-once matrix is sufficient grounds for a stakeholder
  ratification now, with an explicit revisit trigger (deprecation or
  stopped resolution) rather than open-ended deferral.

## Implications

No file change to `.claude/agents/system-architect.md` is made or
required by this decision — it ratifies the existing string. Combined
with DEC-0348 (frontmatter-only pinning) and DEC-0347 (restart
requirement), the system-architect's spawn practice is now: frontmatter
pins `model: claude-opus-4-6` and `effort: high`; no explicit
spawn-time model param is passed; any future frontmatter edit to this
agent requires a Claude Code restart before its next spawn. Revisit
this decision if `claude-opus-4-6` stops resolving or is listed as
deprecated in official documentation.
