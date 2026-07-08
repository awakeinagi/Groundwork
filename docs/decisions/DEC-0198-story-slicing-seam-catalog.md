---
id: DEC-0198
type: decision
title: A story-slicing seam catalog is adopted for story derivation
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0037 @ T1-T4"
links:
  derives-from: [SES-0037]
  relates-to: [DEC-0199, DEC-0200, DEC-0195, DEC-0188, DEC-0196]
  supersedes: []
---

# DEC-0198: A Story-Slicing Seam Catalog Is Adopted for Story Derivation

## Context

The Story and spike derivation playbook lacked concrete slicing
guidance the same way the Epic playbook did before
[DEC-0195](DEC-0195-vertical-slicing-seam-catalog.md). The stakeholder
proposed five vertical-slicing seams (Data, Chronological, Fidelity,
Logic, Operational), validated against Richard Lawrence's "Patterns for
Splitting User Stories," plus a sixth (Operations/CRUD) proposed during
review and confirmed by name ("Operations Completion") against a
supplementary source
(<https://socadk.github.io/design-practice-repository/activities/DPR-StorySplitting.html>).

## Decision

Adopt a six-seam catalog in `references/story-slicing-seams.md`: Data,
Chronological, Fidelity, Logic, Operational, and Operations (CRUD/
lifecycle), each with a Rule and Examples, grounded where possible in
Groundwork's own artifact lifecycle. A cross-reference note documents
that Lawrence's "Architectural Spike vs. Implementation" pattern is
already natively covered by Groundwork's `SP-` artifact type — a story
whose real content is an investigation should become a Spike, not an
undersized story — rather than adding it as a seventh seam. Mike Cohn's
SPIDR mnemonic is noted as a complementary cross-reference. The Fidelity
seam carries an explicit caveat, tying to
[DEC-0188](DEC-0188-shared-accessibility-responsive-baseline.md):
"basic" means unstyled, never sub-baseline — every story, including the
mechanics-first one, still owes the shared accessibility/responsive
conformance citation.

## Rationale

Grounding in Lawrence's canonical catalog (and independently confirming
it via the DPR source) establishes these are established patterns, not
ad hoc guesses. The Spike cross-reference avoids inventing a redundant
seam for something Groundwork's artifact model already solves
structurally. The
[DEC-0188](DEC-0188-shared-accessibility-responsive-baseline.md) caveat
forecloses a plausible
misreading — that "get it working with raw elements first" means the
mechanics-only story is exempt from baseline accessibility — before it
causes a real gap the way the missing backend-platform epic did.

## Alternatives Considered

- **Add "Architectural Spike vs. Implementation" as a seventh seam**:
  rejected — Groundwork's `SP-` artifact type already encodes this
  distinction structurally; documenting it as a cross-reference avoids
  duplicating a mechanism that already exists.
- **Leave the Fidelity seam's accessibility interaction unstated**:
  rejected — the near-miss with `DEC-0188` was close enough to be worth
  an explicit caveat rather than relying on facilitators to notice it
  independently each time.

## Implications

`references/story-slicing-seams.md` created; `refinement-process.md`'s
Story playbook and `SKILL.md`'s reference map point to it.
