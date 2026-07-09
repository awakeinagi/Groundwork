---
id: DEC-0287
type: decision
title: The checker enforces overview presence and the 250-word cap on every artifact
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0053 @ T8-T9"
overview: >-
  A new integrity rule in tools/check_links.py: every artifact's
  frontmatter must contain a non-empty overview: field of at most 250
  words. Both checks are mechanical and cheap. Faithfulness of the
  overview to the body is explicitly not checker territory — it is kept
  by the same-edit rule and gate checklist (DEC-0288). The rule lands in
  the same commit as the full corpus retrofit so the corpus is never
  half-covered.
links:
  derives-from: [SES-0053]
  relates-to: [DEC-0284, DEC-0286, DEC-0242]
---

# DEC-0287: The Checker Enforces Overview Presence and the Word Cap

## Context

Tooling and reading habits can only rely on overviews if presence is
guaranteed, and batch reads are only budgetable if the cap holds.
Advisory conventions predictably decay to partial coverage.

## Decision

`tools/check_links.py` gains a new integrity rule: **every artifact's
frontmatter contains a non-empty `overview:` field of at most 250
words, and every bare artifact ID inside it resolves to an existing
artifact** — DEC-0242's resolution guarantee extended to the overview
surface, which body-prose scanning (its rule) does not cover.
Violations block commits like any other integrity failure.
Faithfulness to the body is out of the checker's scope — it is a
process obligation (DEC-0288).

## Rationale

Presence and length are the two properties that are mechanically
checkable and whose failure silently breaks the feature: a missing
overview forces a full-file read; a bloated one *is* a full-file read.
Faithfulness requires judgment and stays human-checked. Enabling the
rule only once the retrofit (DEC-0291) covers the whole corpus — same
commit — avoids a window where the checker is red or the rule is
disabled.

## Alternatives Considered

- **Presence only** — simpler; rejected: nothing stops overviews from
  bloating into the very full-reads being eliminated.
- **Advisory (no rule)** — rejected: decays to partial coverage;
  tooling cannot rely on the field.

## Implications

`check_links.py` (project copy and skill master) gains the rule; the
integrity-rules list in the skill's system reference and
[SPEC-artifact-common](../specs/SPEC-artifact-common.md) document it.
New-artifact authoring must write the overview at creation time — the
checker makes omission impossible to commit.
