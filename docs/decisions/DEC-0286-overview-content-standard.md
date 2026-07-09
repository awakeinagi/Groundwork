---
id: DEC-0286
type: decision
title: Overview content standard — self-sufficient plain prose, max 250 words
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0053 @ T6-T7"
overview: >-
  Overviews are self-sufficient plain prose of at most 250 words:
  readable without the body, stating what the artifact is, its core
  content or outcome, and its current disposition. Bare artifact IDs are
  allowed; markdown formatting is not. Per-type guidance lives in the
  skill's templates (a decision's overview states the decision in one
  breath; a session's states what was refined and produced; a
  component's states what its contract covers). The stakeholder raised
  the cap from the recommended ~80 words to 250.
links:
  derives-from: [SES-0053]
  relates-to: [DEC-0242]
---

# DEC-0286: Overview Content Standard

## Context

Batch overview reads are only budgetable if overview density is
predictable; free-form summaries decay into either one-line vagueness
or full-section duplication. The facilitator recommended a 2–4
sentence / ~80-word shape (SES-0053 @ T6); the stakeholder kept the
shape but raised the ceiling (T7).

## Decision

An overview is **self-sufficient plain prose, at most 250 words**:
readable without the body, stating what the artifact is, its core
content or outcome, and its current disposition (e.g. "deferred behind
TRG-0010"). Bare artifact IDs are allowed and must resolve, extending
DEC-0242's bare-ID convention into the overview field
(resolution checked by DEC-0287's rule); markdown
formatting is not used. Per-type one-line guidance
lives in the skill's templates — e.g. a decision's overview states the
decision in one breath; a session's states what was refined and what
it produced; a component's states what it is and what its contract
covers.

## Rationale

Self-sufficiency is the point of progressive disclosure: an overview
that requires the body to make sense saves nothing. The 250-word cap
is generous enough for dense artifacts (session transcripts, component
contracts) while keeping a filtered batch of dozens of overviews
cheaper than a handful of full files. Plain prose keeps extraction and
downstream embedding trivial.

## Alternatives Considered

- **One-sentence strict** — cheapest to scan; rejected: uselessly
  vague or run-on for sessions and CMPs.
- **Free-form per author** — zero friction; rejected: unpredictable
  density defeats batch budgeting.
- **~80-word cap (as recommended)** — amended by the stakeholder to
  250 words.

## Implications

The cap is checker-enforced alongside presence (DEC-0287). Templates
in the skill (and the vendored copy) gain the per-type guidance. The
overview-writer agent (DEC-0291) bakes the standard into its prompt.
