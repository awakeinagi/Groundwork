---
id: SES-0014
type: session
title: Clickable cross-references in artifact bodies
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-07
overview: >-
  Scoped and authorized updating specs to make cross-references
  clickable in artifact bodies. Settled: scope to body prose only
  (frontmatter remains bare IDs per DEC-0009 to preserve Graph Index
  semantics), new integrity rule requiring inline links resolve with
  link text starting with artifact ID pointing at that artifact, bare
  IDs in prose flagged. Authorized full mechanical retrofit pass over
  entire corpus including closed sessions and accepted decisions, under
  explicit formatting-only decision. Produced 2 decisions.
participant: awakeinagi@gmail.com
participant-role: eng-lead
facilitator: Claude Code (claude-fable-5)
transcript-fidelity: reconstructed
links:
  relates-to: [DEC-0009, DEC-0090, DEC-0091]
---

# SES-0014: Clickable cross-references in artifact bodies

## Purpose

The participant proposed updating the design-doc specs so cross-references
are clickable, and asked for concerns before committing to the change.
Already settled going in: DEC-0009
(frontmatter typed links over bare stable IDs as the machine-readable
backbone) and DEC-0010
(the Graph Index is derived from frontmatter only).

## Transcript

**T1 — awakeinagi.** Let's update the specs for design docs to make
cross-references clickable. Any concerns about that change?

**T2 — Facilitator.** Reported the current state first:
[SPEC-artifact-common](../specs/SPEC-artifact-common.md) already prescribes
inline references as `[<ID>](relative/path.md)`, but practice has diverged —
the 121-artifact corpus mixes markdown links with bare IDs in body prose
(e.g. ST-0001 wrote citations
as bare `per DEC-0034, DEC-0009` text). So the change is really about
scope and enforcement, with three concerns:

1. *Frontmatter must stay bare IDs.* DEC-0009
   makes frontmatter the machine-readable backbone; the Graph Index and
   `tools/check_links.py` parse those YAML values as plain IDs. Making them
   markdown links breaks both tools and would require superseding DEC-0009
   with a huge blast radius. Prose links are explicitly non-semantic
   "navigational sugar", so a prose-side mandate complements DEC-0009
   rather than conflicting with it. Recommended: scope to body prose only.
2. *Link rot is unpoliced.* IDs are immutable but slugs and directories are
   embedded in relative paths, and the checker validates only
   frontmatter/`cites` IDs — never inline link targets. Mandating clickable
   links without a checker rule institutionalizes silent rot. Recommended:
   new integrity rule — inline links must resolve, link text beginning with
   an artifact ID must point at that artifact's file, and bare artifact IDs
   in prose are flagged.
3. *Retrofit collides with immutability.* Closed sessions are append-only
   and accepted decisions immutable, yet much of the corpus uses bare IDs.
   Recommended: apply the rule to new and still-editable artifacts only,
   leaving immutable artifacts as-is.

**T3 — awakeinagi.** Accepted the prose-only scope and the checker
enforcement rule as recommended. On the retrofit, chose the stronger option
over the recommendation: run a full mechanical pass over the entire
existing corpus — including closed sessions and accepted decisions — under
an explicit decision sanctioning formatting-only edits (no semantic change,
verified by diff review).

## Decisions Produced

DEC-0090,
DEC-0091

## Conflicts Raised

None.
