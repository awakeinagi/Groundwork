---
id: DEC-0104
type: decision
title: Deferred status and release scoping extend to spikes
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0017 @ T3"
links:
  derives-from: [SES-0017]
  supersedes: [DEC-0097]
  relates-to: [DEC-0098, DEC-0100, DEC-0105]
---

# DEC-0104: Deferred Status and Release Scoping Extend to Spikes

## Context

[DEC-0097](DEC-0097-deferred-status.md) limited `deferred` to stories
and epics. Re-scoping
[SP-0002](../spikes/SP-0002-postgres-pgvector-graduation.md) to a future
evaluation exposed the gap: a research question can be real, captured,
and intentionally not current — exactly what deferral expresses — with
no way to park it honestly.

## Decision

Supersedes [DEC-0097](DEC-0097-deferred-status.md), restating its scope:
the `deferred` lifecycle status and the `release:` field
([DEC-0098](DEC-0098-semver-release-labels.md)) are valid for
**stories, epics, and spikes**. All other semantics are unchanged —
entry from any active status; no gates and no derivation while deferred;
revival to `draft`; deferral and revival each cite a decision
([DEC-0100](DEC-0100-scope-moves-cite-decisions.md)); a spike inherits
its release default from its parent epic (a cross-cutting spike deriving
from a Business Goal carries its own label).

## Rationale

A deferred spike is the honest state for "this question matters later":
the alternative — leaving it approved-but-dormant or archiving and
re-creating it — either pollutes the active pipeline or throws away the
question's history. Spikes already share the standard lifecycle;
excluding them from deferral was an artifact of the original session's
focus on stories, not a considered boundary.

## Alternatives Considered

- **Keep stories/epics only; archive dormant spikes**: loses continuity
  of the question and its accumulated context.
- **Extend to all pipeline types including components/goals**: still
  incoherent for goals (they define releases) and derivable for
  components (they serve whichever stories are in scope) — unchanged
  from the original analysis.

## Implications

[SPEC-artifact-common](../specs/SPEC-artifact-common.md),
[SPEC-spike](../specs/SPEC-spike.md), the checker's release-scoped type
set, status tooling, and the glossary's Deferred entry all widen to
include spikes. Artifacts citing
[DEC-0097](DEC-0097-deferred-status.md) are walked for staleness (none
cite it in frontmatter at supersession time).
