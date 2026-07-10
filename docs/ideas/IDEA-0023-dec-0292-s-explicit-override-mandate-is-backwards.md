---
id: IDEA-0023
type: idea
title: "DEC-0292's explicit-override mandate is backwards: frontmatter alone preserves model and effort"
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-10
proposed-by: awakeinagi
overview: >-
  Three live diagnostic spawns of system-architect contradict
  DEC-0292's premise that "the frontmatter pin alone has been
  observed not to take effect." No-override (frontmatter model
  claude-opus-4-6, effort high) yielded effort 99/100; DEC-0292's
  mandated explicit model="fable" override yielded effort "low" then
  40/100 on repeat — the frontmatter-only path DEC-0292 says doesn't
  work actually delivers correct model AND effort, while the
  mandated override silently drops effort. Cause: the Agent tool has
  a model parameter but no effort parameter; only Workflow's agent()
  supports explicit effort, so DEC-0292's practice cannot currently
  pass "explicit model + high effort" together. Separately, claude-
  opus-4-6 is not a real Anthropic model identifier per official
  docs (current lineup: claude-fable-5, claude-opus-4-8, claude-
  sonnet-5, claude-haiku-4-5-20251001), yet it still resolved and
  ran at full effort, suggesting frontmatter model is treated as
  opaque label text. A future session should supersede DEC-0292 with
  this corrected finding, choose a fix (drop the explicit-override
  mandate; route high-effort needs through Workflow's agent(); or
  another reconciliation), and correct the frontmatter's model
  string to a real identifier.
links:
  derives-from: [SES-0062]
  relates-to: [DEC-0292, DEC-0329, IDEA-0016]
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

Pending — awaiting take-up. A future session should: verify the
effort-drop finding is not a fluke (ideally with a larger sample or by
inspecting harness-level docs/behavior if available), supersede
DEC-0292 (never edit an accepted decision — supersede only) with the
corrected empirical picture, decide the fix for guaranteeing high
effort at system-architect spawn time, and correct the frontmatter
model string to a real current identifier.

