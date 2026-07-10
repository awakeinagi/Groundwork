---
id: DEC-0318
type: decision
title: Project-local .claude/skills is the canonical, git-tracked skill home; .agents/skills is retired
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0057 @ T13-T15"
overview: >-
  The project's skills (groundwork-design-session, artifact-interact,
  system-architecture-bp, and any future ones) live canonically in
  the repo's project-local .claude/skills/ directory, which Claude
  Code loads natively and git tracks — the versioned record and the
  loadable copy become the same thing. The .agents/skills vendored
  mirror is retired and deleted; its only purpose was versioning,
  which .claude/skills now serves. The user-level ~/.claude/skills
  installation is demoted to a personal convenience copy installed
  FROM the repo (per-skill install scripts, DEC-0319). Ends the
  standing rsync-sync obligation between the live skill and the
  vendored copy — canonical edits happen in-repo and are committed
  like any other change.
links:
  derives-from: [SES-0057]
  relates-to: [DEC-0319, DEC-0320]
---

# DEC-0318: .claude/skills Is the Canonical Skill Home

## Context

Skills lived in `~/.claude/skills` (loadable, unversioned) with a
vendored copy in `.agents/skills` (versioned, not loadable) and a
standing manual sync obligation between them. The stakeholder
directed at T13 that skills be copied into project-local
`.claude/skills` for git tracking; T14-T15 settled which copy is
canonical.

## Decision

Project-local `.claude/skills/` is the canonical, git-tracked home of
the project's skills. `.agents/skills` is retired and deleted.
`~/.claude/skills` becomes a personal convenience install synced from
the repo via the install scripts (DEC-0319).

## Rationale

Claude Code loads project-local skills natively, so the versioned
record and the loadable copy collapse into one location — the sync
obligation (and its observed drift risk) disappears.

## Alternatives Considered

- **Keep .agents/skills as a second mirror** for non-Claude runners —
  two sync obligations for a hypothetical consumer; rejected.
- **~/.claude/skills stays canonical** with the repo copy synced from
  it — preserves today's discipline, new location; rejected.

## Implications

Executed at the DEC-0320 cutover: copy skills into
`.claude/skills/`, delete `.agents/skills`, update every reference.
The facilitator memory rule about syncing the vendored copy becomes
obsolete and is updated then.
