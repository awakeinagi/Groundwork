---
id: DEC-0097
type: decision
title: deferred joins the artifact status lifecycle for stories and epics
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0016 @ T1-T5"
links:
  derives-from: [SES-0016]
  relates-to: [DEC-0006, DEC-0098, DEC-0100]
---

# DEC-0097: `deferred` Joins the Artifact Status Lifecycle for Stories and Epics

## Context

During design sessions, nice-to-have stories surface that don't belong
in the current release. They must be captured as real artifacts without
pretending they're current work — and the existing lifecycle has no
state for "captured, parked, intentionally not proceeding."

## Decision

A new lifecycle status `deferred` is added to the standard artifact
lifecycle, valid for stories and epics only. Entry: from any active
status (`draft`, `in-refinement`, `gated`, `approved`). While deferred:
the artifact cannot pass a gate, and nothing may derive from it. Exit
(revival): always to `draft` — body content, citations, and links are
retained, but the artifact re-earns its gate in the current context.

## Rationale

The participant's framing: it isn't sensible to approve a story before
it is in scope — gates ratify work that feeds the next stage
([DEC-0006](DEC-0006-gate-every-stage.md)). Reviving to `draft` rather
than restoring the pre-deferral status is the same principle applied at
the exit: the world moved on while the story was parked, and silent
re-approval is what staleness machinery exists to prevent. Allowing
deferral *from* `approved` keeps the common real-world event — a
release-cut meeting descoping ratified work — a single honest transition
instead of a supersede dance.

## Alternatives Considered

- **Orthogonal scope-only field with no status change** (facilitator's
  original recommendation): rejected — lets out-of-scope stories hold
  approvals.
- **Defer only from `draft`/`in-refinement`**: rejected — makes
  descoping approved work heavyweight (supersede + new story).
- **Revive to remembered prior status**: rejected — re-approves in a
  stale context.
- **Release-roster artifact type / bucket epic**: rejected in the
  mechanism round — heavy machinery, and the bucket epic corrupts the
  derivation tree.

## Implications

The lifecycle diagram in
[SPEC-artifact-common](../specs/SPEC-artifact-common.md) gains the
state; the "nothing derives from an unapproved parent" rule covers
deferred epics with no new machinery. A deferred artifact carries a
`release:` label per [DEC-0098](DEC-0098-semver-release-labels.md) and
cites its deferral decision per
[DEC-0100](DEC-0100-scope-moves-cite-decisions.md). Skill references
sync.
