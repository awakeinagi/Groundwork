---
id: DEC-0319
type: decision
title: Every skill ships an install script for project-local and global installs
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0057 @ T15"
overview: >-
  Each skill in the repo's canonical .claude/skills/ home (DEC-0318)
  carries an install script that installs the skill from the repo
  into either a target project's .claude/skills/ (project-local
  install) or the user's ~/.claude/skills/ (global install), with the
  option to install all of the repo's .claude/skills globally in one
  invocation. This replaces the retired vendoring pattern as the
  distribution mechanism: the repo is the source of truth; personal
  and other-project copies are installed from it, never edited in
  place as canonical.
links:
  derives-from: [SES-0057]
  relates-to: [DEC-0318]
---

# DEC-0319: Per-Skill Install Scripts

## Context

With `.claude/skills` canonical in-repo (DEC-0318), users still need
the skills available globally (`~/.claude/skills`) and in other
projects; a sanctioned distribution mechanism was needed to replace
ad-hoc copying.

## Decision

Every skill ships an install script supporting project-local
(`<target>/.claude/skills/`) and global (`~/.claude/skills/`)
installation from the repo copy, including an option to install all
of the repo's skills globally at once.

## Rationale

Installs-from-canonical keep one source of truth while restoring the
convenience of globally available skills; a scripted path beats
undocumented rsync incantations.

## Alternatives Considered

- **Manual copy/rsync guidance only** — works but unscripted and
  error-prone; rejected.
- **Symlinks from ~/.claude/skills into the repo** — considered
  implicitly; fragile across machines and not what the stakeholder
  asked for; not adopted.

## Implications

Built during DEC-0322 for artifact-interact and retrofitted to the
existing skills at the DEC-0320 cutover.
