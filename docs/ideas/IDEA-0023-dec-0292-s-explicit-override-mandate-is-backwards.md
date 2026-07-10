---
id: IDEA-0023
type: idea
title: "DEC-0292's explicit-override mandate is backwards: frontmatter alone preserves model and effort"
status: taken-up
owner: awakeinagi@gmail.com
created: 2026-07-10
proposed-by: awakeinagi
overview: >-
  Three live diagnostic spawns of system-architect (SES-0062)
  appeared to contradict DEC-0292's premise that a frontmatter model
  pin alone doesn't take effect, suggesting the mandated explicit-
  override practice silently dropped effort while frontmatter alone
  preserved it. SES-0063 took this idea up and re-verified it at a
  larger sample (24 spawns, 8 arms): the headline finding is REFUTED
  — frontmatter effort in fact survives explicit spawn-time model
  overrides, both same-family and cross-family. The apparent
  contradiction traced to a different mechanism entirely: agent
  definition files are read once at Claude Code startup (DEC-0347),
  so mid-session frontmatter edits were silently served stale,
  producing the earlier "doesn't take effect" illusion. The
  corrected practice — frontmatter-only pinning, no mandated
  explicit spawn-time model param — is recorded in DEC-0348, which
  narrows (via relates-to, not full supersession) DEC-0292 and
  DEC-0329's explicit-override clauses while leaving their surviving
  content (the agents' existence, consultation moments, and model-
  tier choices) unchanged. The system-architect's `claude-opus-4-6`
  frontmatter string, also flagged by this idea as undocumented, is
  retained on the stakeholder's empirical ratification (DEC-0349).
  Status: taken-up.
links:
  derives-from: [SES-0062]
  relates-to: [DEC-0292, DEC-0329, IDEA-0016, SES-0063, DEC-0347, DEC-0348, DEC-0349]
---

# IDEA-0023: DEC-0292's explicit-override mandate is backwards: frontmatter alone preserves model and effort

## The Idea

Verbatim: "DEC-0292 requires passing an explicit `model` override at
every system-architect spawn because 'the frontmatter pin alone has
been observed not to take effect.' Three live diagnostic spawns
contradict this: (1) no explicit model param, relying on frontmatter's
`model: claude-opus-4-6` alone → agent self-reported running as
claude-opus-4-6 at reasoning effort 99/100 (matching frontmatter's
effort: high). (2) explicit `model: fable` override (DEC-0292's
mandated practice) → agent self-reported running as claude-fable-5 at
effort 'low'. (3) repeat of (2) → claude-fable-5 at effort 40/100. So
the frontmatter-only path (which DEC-0292 says doesn't work) actually
delivers both the correct model AND the correct high effort; the
explicit-override path DEC-0292 mandates instead silently drops effort
to ~40/100 regardless of frontmatter's effort: high. Structural cause:
the Agent tool used for spawning agents has a `model` parameter but no
`effort` parameter at all — only the separate Workflow tool's
`agent()` function supports an explicit effort override — so there is
currently no way to pass 'explicit model + high effort' together
through the Agent tool that DEC-0292 was written against. Also
separately confirmed via docs.anthropic.com (models overview +
model-deprecations pages): `claude-opus-4-6` is not a real current or
deprecated Anthropic model identifier at all — current lineup is
claude-fable-5 (most capable), claude-opus-4-8, claude-sonnet-5,
claude-haiku-4-5-20251001 — yet the frontmatter pin using this
nonexistent string still resolved successfully and ran at full effort
in the diagnostic, suggesting the harness treats this frontmatter
field as opaque label text rather than a validated model ID. A future
session should supersede DEC-0292 with the corrected empirical
finding, and decide the actual fix: candidates include (a) stop
mandating an explicit model override for system-architect spawns via
the Agent tool, relying on frontmatter alone since it demonstrably
preserves both model and effort; (b) route system-architect
consultations that need guaranteed high effort through Workflow's
agent() with an explicit effort option instead of the plain Agent
tool; (c) some other reconciliation. Also correct the frontmatter's
`model: claude-opus-4-6` string itself, since it is not a real/current
Anthropic model identifier per official docs even though it appears to
resolve to *something* functional in practice — replace with a real
current identifier or alias (e.g. claude-fable-5 / the 'fable' alias)
once the effort question is settled."

## Spark Context

Raised during a change-intake session opened to work IDEA-0016
(2026-07-10). The session's path-pick evolved: original ask ("switch
to claude-opus-4-6") → discovered claude-opus-4-6 isn't a real model
per official Anthropic docs → user asked to empirically verify via
live test spawns rather than assume → three diagnostic Agent-tool
spawns of system-architect (Test A: no override; Test B: explicit
model="fable"; Test C: repeat of B) produced the findings above. This
idea captures that finding as its own item so the current session can
close/continue without resolving it now. Relates to IDEA-0016, the
idea whose take-up prompted this diagnostic investigation.

## Disposition

Taken up in SES-0063 (2026-07-10). The headline finding — "DEC-0292's
explicit-override mandate silently drops effort, frontmatter alone
preserves both model and effort" — is REFUTED by a larger sample (24
probe spawns across 8 arms): frontmatter effort survives explicit
spawn-time model overrides, both same-family and cross-family. The
real root cause of every historical "frontmatter pin alone doesn't
take effect" observation was startup caching of agent definitions
(DEC-0347: `.claude/agents/*.md` is read once at Claude Code startup;
mid-session edits are silently ignored until restart) — not a genuine
limitation of the frontmatter mechanism. The corrected practice —
project agents are pinned via frontmatter alone, with explicit
spawn-time model params reserved for deliberate one-off deviations —
is recorded in DEC-0348. The frontmatter `model: claude-opus-4-6`
string on system-architect is retained, ratified by the stakeholder on
empirical grounds, per DEC-0349. See SES-0063 for the full
verification transcript.

