---
id: DEC-0099
type: decision
title: Release labels are declared in the Business Goal's Scope section
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
overview: >-
  Each Business Goal's Scope section declares named releases as a
  machine-parseable list (one item per release, value in code span, current
  release marked). The checker validates every release field value in stories
  and epics against declared releases plus reserved backlog. Matching is exact:
  a label must literally equal a declared value; no prefix-matching. Adding,
  renaming, or re-scoping a release is a goal amendment passing its gate.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0016 @ T4-T5, T10-T11"
links:
  derives-from: [SES-0016]
  relates-to: [DEC-0098, DEC-0022]
---

# DEC-0099: Release Labels Are Declared in the Business Goal's Scope Section

## Context

The controlled vocabulary of
DEC-0098 needs one canonical,
validated home; otherwise nothing stops an undeclared release label
appearing with no gated record of what it means.

## Decision

Each Business Goal's **Scope** section declares the named releases of
the work it roots, as a machine-parseable list — one item per release,
the value in a code span, the current release marked:

```markdown
**Releases:**
- `1` (current) — goal refinement end-to-end
- `2` — connectors-led expansion
```

The checker validates every `release:` value in stories and epics
against the union of declared release values plus reserved `backlog`.
Matching is **exact**: a label must literally equal a declared value —
declare `1.2` before using it; no prefix-matching. Adding, renaming, or
re-scoping a release is an amendment to the goal, passing its gate.

## Rationale

Releases are scope statements, and Scope belongs to the goal — this puts
release definitions behind the same human gate that ratifies scope
everywhere else. DEC-0022
already lives as exactly this kind of statement; the declaration
codifies it. Exact matching was the facilitator's call, flagged and
confirmed: prefix-matching (declared `1` covering a story marked `1.2`)
invites ambiguity about which declared release owns a story.

## Alternatives Considered

- **CONTEXT.md glossary**: rejected — the glossary is definitions-only
  by rule; release rosters are scope decisions, not vocabulary.
- **Format-only validation, no declaration**: rejected — nothing would
  stop an undeclared label, and there'd be no gated record of what each
  release means.
- **Prefix-matching against declarations**: rejected for ambiguity of
  ownership.

## Implications

[SPEC-business-goal](../specs/SPEC-business-goal.md) gains the
subsection and its format.
BG-0001 needs an amendment declaring
its releases before the first `release:` label can validate; `backlog`
is usable immediately without any declaration.
