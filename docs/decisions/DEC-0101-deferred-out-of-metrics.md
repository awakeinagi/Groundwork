---
id: DEC-0101
type: decision
title: Deferred items leave metric denominators and gain a dedicated discovery view
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0016 @ T4-T5"
links:
  derives-from: [SES-0016]
  relates-to: [DEC-0093, DEC-0095, DEC-0097, DEC-0098]
---

# DEC-0101: Deferred Items Leave Metric Denominators and Gain a Dedicated Discovery View

## Context

The design percent-complete rollups
([DEC-0095](DEC-0095-percent-complete-metrics.md)) and story-coverage
warnings ([DEC-0093](DEC-0093-story-design-coverage-check.md)) assume
every story counts. Deferred stories
([DEC-0097](DEC-0097-deferred-status.md)) would read as false gaps and
artificially deflate current-release progress.

## Decision

Clarifying — not superseding —
[DEC-0093](DEC-0093-story-design-coverage-check.md) and
[DEC-0095](DEC-0095-percent-complete-metrics.md): their denominators are
**in-scope stories only**. `deferred` stories leave the design-%
rollups and the uncovered-story warnings. New audit warning: a
component design element whose `Implements:` line references *only*
deferred stories (in-scope contract content motivated by nothing in
scope). Discovery surface: the status report gains a **Deferred**
section grouped by release label and sorted by SemVer precedence with
`backlog` last (per [DEC-0098](DEC-0098-semver-release-labels.md)), and
the graph tooling a backlog view/filter.

## Rationale

The design-% metric's job is answering "is this release's design done?"
— including backlog items breaks that permanently (a goal could never
reach 100%). A dedicated listing serves the actual discovery need
directly instead of polluting the completion metrics.

## Alternatives Considered

- **Include deferred items in rollups, annotated**: rejected — the
  metric stops answering its question.
- **Per-release rollups everywhere** (v1: 80%, v2: 10%): acknowledged as
  the natural future enhancement, rejected now — triples the reporting
  surface ahead of demonstrated need. This decision is the extension
  point when it's wanted.

## Implications

`tools/check_links.py` and the skill's status/graph tooling need
updates; the deferred-only-Implements warning extends the audit family
of [DEC-0093](DEC-0093-story-design-coverage-check.md).
