---
id: DEC-0418
type: decision
title: "Agent-registry reload semantics are incoming-turn-boundary refresh, not startup-only"
status: accepted
owner: awakeinagi
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0083 @ T3-T6"
overview: >-
  Controlled marker-probe tests on Claude Code v2.1.207 (Linux,
  2026-07-12, SES-0083, stakeholder-witnessed) establish that a
  session's agent registry refreshes at incoming-turn boundaries,
  not once at startup: a top-level user message and an incoming
  teammate SendMessage refresh it; background-task completion
  notifications and AskUserQuestion answers do not. New agent files
  register on the immediately following incoming turn reliably (four
  trials); edits race the file watcher (stale on the readiness-ping
  turn in one round, current in another under identical timing) but
  are always current by the next incoming turn. This supersedes
  DEC-0347's startup-cache/restart-required finding, which was
  accurate for its version but is now obsolete; reload semantics are
  version-dependent, so a marker probe should be re-run after any
  Claude Code upgrade. DEC-0348's frontmatter-pin ruling stands with
  only its rationale's caching mechanism corrected; DEC-0349's
  restart-before-respawn claim is corrected to a new-incoming-turn
  requirement; EP-0009's body is repaired to match in this session.
links:
  relates-to: [DEC-0348, DEC-0349, DEC-0419]
  derives-from: [SES-0083]
  supersedes: [DEC-0347]
---

# DEC-0418: Agent-registry reload semantics are incoming-turn-boundary refresh, not startup-only

## Context

A Claude Code session's agent registry is not read once at startup. Controlled marker-probe tests on Claude Code v2.1.207 (Linux, 2026-07-12, stakeholder-witnessed in SES-0083's originating conversation) established that the registry of spawnable agent definitions refreshes when a new incoming turn starts and never mid-turn.

## Decision

Events verified to refresh the registry: a top-level user message, and an incoming teammate SendMessage. Events verified NOT to refresh it: background-task completion notifications, and a user's answer to an interactive AskUserQuestion prompt. The rule covers both newly created agent files and edits to existing ones, in both the project .claude/agents and user ~/.claude/agents directories. New-agent registrations were served correctly on the immediately following incoming turn in all four trials. Edits race the file watcher: a spawn on the turn of an edit's readiness ping served the stale pre-edit definition in one round and the edited definition in another under identical protocol timing, while a spawn on any later incoming turn always served the edited definition.

## Rationale

This supersedes DEC-0347, whose restart-required finding recorded pre-watcher behavior accurately for its version but no longer holds. Reload semantics are version- and platform-dependent (the upstream changelog records no agent watcher through v2.1.207 and open upstream issues report agent files failing to load on other platforms), so after any Claude Code upgrade the semantics are re-verified with a marker probe: write a throwaway agent whose output carries a distinctive marker, spawn it across turn boundaries, and compare markers.

## Alternatives Considered

The historical startup-only-cache model (DEC-0347) was ruled out directly: it predicts every same-turn spawn fails, but the immediately-following-turn trials showed reliable success instead. A mid-turn-poll model was also ruled out: no trial observed a new or edited definition become visible before an incoming turn boundary. No third model fit the observed edit-race behavior (stale in one round, current in another under identical timing) except a watcher racing the turn boundary, which is the model this decision adopts.

## Implications

Consequences for citers: DEC-0348's ruling that frontmatter pins are authoritative and sufficient stands unchanged, with only the caching mechanism in its rationale updated; DEC-0349's operational claim that an edited agent requires a restart before its next spawn is corrected to requiring a new incoming turn plus watcher ingestion; EP-0009's body statement of the startup-cache constraint is repaired in this session.
