---
id: DEC-0347
type: decision
title: "Agent definition files are read once at Claude Code startup; changes require exit-and-restart"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-10
decided-by: awakeinagi
decided-on: 2026-07-10
source-span: "SES-0063 @ T6-T10"
overview: >-
  Empirical finding from SES-0063's 24-spawn, 8-arm verification:
  `.claude/agents/*.md` definitions (existence and frontmatter
  model/effort/tools) are read once at Claude Code startup and
  cached for the session. A newly created agent yields "Agent type
  not found"; a frontmatter edit silently keeps serving the old
  cached values until the operator exits and restarts. Evidence: a
  mid-session frontmatter model edit (haiku to claude-opus-4-6) kept
  spawning haiku; after restart the same definition ran opus-4-6.
  This caching is the root cause of the false premise corrected by
  DEC-0348. Operational rule: after any agent-definition
  create/edit, restart before spawning; multi-variant experiments
  define all variants up front so one restart covers the whole
  matrix.
links:
  derives-from: [SES-0063]
  relates-to: [DEC-0292, DEC-0329, DEC-0349]
cites: [DEC-0292, DEC-0329]
---

# DEC-0347: Agent Definition Files Are Read Once at Claude Code Startup; Changes Require Exit-and-Restart

## Context

SES-0063 set out to verify SES-0062's finding that DEC-0292's
explicit-override mandate silently drops effort. The verification
matrix hit a confusing result mid-session (T6): after editing the
probe agent's frontmatter from `claude-haiku-4-5` to `claude-opus-4-6`,
three fresh spawns of that same agent definition still ran as Haiku.
The stakeholder (T7) correctly diagnosed the cause before the
facilitator did: "I think the main problem with these tests is we have
to close and restart Claude Code for the model changes to take
effect." A restart-once matrix (T8) confirmed it: after exiting and
restarting Claude Code, the identical `claude-opus-4-6` frontmatter
now resolved and ran (T10, arm C′) at a self-reported reasoning effort
of 99/100.

## Decision

`.claude/agents/*.md` definitions — their existence and their
frontmatter (`model`, `effort`, `tools`) — are read once at Claude
Code startup and cached for the session. A newly created agent file
yields "Agent type not found" until restart; a frontmatter edit to an
existing agent silently keeps serving the old cached values, with no
error, until the operator exits and restarts Claude Code. This
caching behavior is the root cause of the false premise DEC A
(DEC-0348) corrects: prior observations that "the frontmatter pin
alone doesn't take effect" were mid-session edits being served from a
stale cache, not a genuine failure of frontmatter to carry model or
effort.

Operational rule: after any agent-definition create or edit, restart
Claude Code before spawning that agent; when running a multi-variant
agent experiment, define all variants up front (before the session's
first spawn of any of them) so a single restart covers the whole
matrix, rather than editing-and-restarting per variant.

## Rationale

The evidence is a direct before/after contrast on the identical
frontmatter string: same file, same content, pre-restart it served
the old model, post-restart it served the new one. No other variable
changed between arm C (pre-restart, T6) and arm C′ (post-restart,
T10). This is a strong causal signal, and it fully explains SES-0062's
and DEC-0292's/DEC-0329's shared premise: the historical
"doesn't take effect" observations were never inspecting a
freshly-started session against a freshly-edited definition.

## Alternatives Considered

- **Treat it as a one-off fluke of the probe setup** — rejected; the
  stakeholder's diagnosis (T7) predicted the fix before it was tested,
  and the subsequent restart-once matrix (T8-T10) confirmed it
  directly rather than by inference.
- **Investigate further for a hot-reload mechanism** — no such
  mechanism was found or hypothesized as available; restart is the
  simplest sanctioned workaround and is now the recorded operational
  rule rather than left as tribal knowledge.

## Implications

Recorded as the operational finding underlying DEC-0348 (the
frontmatter-only pinning decision) and DEC-0349 (the system-architect
model-string ratification), both of which depend on this caching
behavior to explain why the earlier "frontmatter alone doesn't work"
observations were mistaken. Future agent-definition experiments in
this project should define all variants before the session's first
relevant spawn, then restart once, per the practice this decision
records.
