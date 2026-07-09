---
id: DEC-0034
type: decision
title: "Two-tier validation: schema on every write, completeness at the gate"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
overview: >-
  Two-tier validation: tier 1 structural on every API write (frontmatter parses,
  schema satisfied, links resolve in branch view), tier 2 completeness as required
  PR checks (required sections present, items cite decisions, links reciprocal, no
  open conflicts); main always fully valid while branches structurally valid but
  incomplete.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0003 @ T4-T5"
links:
  derives-from: [SES-0003]
---

# DEC-0034: Two-tier validation — schema always, completeness at the gate

## Context

Draft artifacts mid-refinement are legitimately incomplete (a story whose
acceptance criteria don't cite decisions *yet*), but a malformed artifact on
main poisons the graph every consumer relies on.

## Decision

Validation runs in two tiers. **Tier 1 — structural**, on every API write to
any branch: frontmatter must parse and satisfy the type's schema; links must
resolve within the branch's view. Rejected writes never land, even for
drafts. **Tier 2 — completeness**, as required checks on the PR blocking
merge: required sections present, contract items cite decisions, impact
links reciprocal, no open conflicts. Main is always fully valid; branches
are structurally valid but may be incomplete.

## Rationale

Matches enforcement strictness to what each consumer needs: mid-session
reads need parseable artifacts, not finished ones; main's consumers (swarm,
projections, index) need everything.

## Alternatives Considered

- **Strict everywhere**: the agent couldn't save work-in-progress, forcing
  state outside the store.
- **Validate only at merge**: branch reads consume unvalidated garbage.

## Implications

`tools/check_links.py` evolves into the tier-2 check suite run as a required
PR check (DEC-0033 adds the
mechanical-diff validator alongside it); tier-1 schemas are the
machine-readable JSON Schema versions of the SPECs (EP-0001 contract).
