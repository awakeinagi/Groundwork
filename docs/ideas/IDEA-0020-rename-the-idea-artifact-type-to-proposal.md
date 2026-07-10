---
id: IDEA-0020
type: idea
title: "Rename the Idea artifact type to Proposal"
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-10
proposed-by: awakeinagi
overview: >-
  No prior discussion has raised this rename. A take-up session must
  resolve a naming collision: the existing Change Proposal (CP-)
  artifact type already uses "proposal" in a distinct sense (out-of-
  band/unauthorized-attempt capture), so renaming Idea to Proposal
  would create ambiguity between two different, already-established
  artifact types in ordinary conversation. The rename also touches a
  wide surface (the IDEA- prefix, every existing captured Idea,
  process references describing "idea capture" and "the work queue")
  that must be scoped explicitly before execution.
links:
  derives-from: [SES-0061]
---

# IDEA-0020: Rename the Idea Artifact Type to Proposal

## The Idea

Verbatim: "An Idea to change the name of the Idea artifact to
Proposal."

## Spark Context

Checked at capture time: no prior session or decision has raised this
rename. The Idea artifact type itself was established at the paradigm
level in SES-0050 and taken up in SES-0051 (DEC-0268..DEC-0272), with
its lifecycle fixed by DEC-0269 (`captured → taken-up | declined`).
A rename touches a wide surface if taken up: the `IDEA-` prefix itself
(SPEC-artifact-common's closed prefix list), every existing captured
Idea's type field and prose references to "Idea"/"Ideas" across the
corpus (this session alone produced seven), the skill and process
references that describe "the work queue" and "idea capture," and
critically the unrelated Change Proposal (`CP-`) artifact type, whose
name already uses "proposal" in a different sense (an out-of-band or
unauthorized-attempt capture) — a rename to "Proposal" would create a
naming collision in ordinary conversation between two distinct,
already-established artifact types (`IDEA-` renamed to Proposal, vs.
existing `CP-` Change Proposal) that a take-up session must resolve
explicitly, not gloss over.

## Disposition

Pending — awaiting take-up. The CP/Proposal naming collision above
should be surfaced explicitly and resolved (rename CP- too? pick a
different name than Proposal? keep IDEA- as the ID prefix while
changing only the display/type-label word?) before any rename
executes, given the corpus-wide reference surface a prefix or
type-label change would touch.
