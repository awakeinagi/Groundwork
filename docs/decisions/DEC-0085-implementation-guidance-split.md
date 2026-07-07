---
id: DEC-0085
type: decision
title: Implementation Guidance section — normative cited Constraints + advisory Notes
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0012 @ T6-T7"
links:
  derives-from: [SES-0012]
---

# DEC-0085: Implementation Guidance Split

## Context

The sponsor wanted an implementation notes/details section in CMP docs.
[DEC-0018](DEC-0018-python-backend-language-agnostic-specs.md) requires
language-agnostic contracts and
[DEC-0011](DEC-0011-contract-complete-component-docs.md) requires
contracts buildable stand-alone — yet stack commitments made through
refinement (e.g. a spike choosing the graph store) need a binding home.

## Decision

CMP docs gain an **Implementation Guidance** section with two
subsections. **Constraints** (`IG-<n>` items): normative for the
reference implementation, decision-cited, gate-checked. **Notes**:
advisory, may be stack-specific, never gate-checked and never
load-bearing — the contract sections must remain sufficient without
them.

## Rationale

The split preserves [DEC-0018](DEC-0018-python-backend-language-agnostic-specs.md): a rebuild in another language ignores the
notes and renegotiates the constraints, while spike-driven stack
decisions still surface in the doc an implementer actually holds instead
of living only in DEC records.

## Alternatives Considered

- **Advisory-only section**: simplest, but binding stack decisions would
  have no home in the CMP and the Handoff Manifest could not surface
  them as requirements.
- **Fully normative section**: strongest binding, but bakes stack
  choices into the contract itself, against [DEC-0018](DEC-0018-python-backend-language-agnostic-specs.md).

## Implications

Section rules in [SPEC-component](../specs/SPEC-component.md); [ST-0007](../stories/ST-0007-tier2-check-suite.md)
checks that Constraints items cite decisions and exempts Notes. [SP-0002](../spikes/SP-0002-graph-engine-selection.md)'s
graph-store outcome lands as an `IG-` constraint in the Graph Index CMP.
