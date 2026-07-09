---
id: DEC-0242
type: decision
title: Body cross-references are bare artifact IDs; the checker validates resolution
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Artifact body cross-references become bare IDs (DEC-0152, CMP-0009)
  instead of inline markdown links, saving ~30% of read time on high-reread
  documents with zero information loss. Non-artifact links stay markdown.
  Replaces DEC-0090's linked form. tools/check_links.py inverts: bare
  artifact IDs must resolve; artifact markdown links become violations.
  Human navigability moves to the doc viewer (DEC-0244).
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0047 @ T1-T4, T7-T8"
links:
  derives-from: [SES-0047]
  supersedes: [DEC-0090]
  relates-to: [DEC-0009, DEC-0091]
---

# DEC-0242: Body Cross-References Are Bare Artifact IDs

## Context

DEC-0090 made every body cross-reference an inline markdown link
`[<ID>](relative/path.md)` for human navigability. Measurement shows
the link paths are pure redundancy — every artifact file is
`<ID>-<slug>.md` in a directory determined by its type, so the path
is fully derivable from the ID — costing ~65k tokens (~20%)
corpus-wide and ~30% of every Component Doc read. The corpus's
primary reader has shifted: agents consume these docs in context far
more often than humans click through them.

## Decision

In artifact **bodies**, cross-references to other artifacts are bare
IDs (`DEC-0152`, `CMP-0009`). Citation clauses take the form
`(per DEC-0152, DEC-0239)`. References to non-artifact files
(CONTEXT.md, specs, code paths) and external URLs remain markdown
links. Frontmatter semantics are unchanged (bare IDs per DEC-0009).
Item-level citation granularity is unchanged — every contract line
still cites its decisions; only the notation compresses.

`tools/check_links.py` inverts its enforcement: every bare artifact
ID in body prose must resolve to an existing artifact (typo
protection); an inline markdown link targeting an artifact file is a
violation; remaining non-artifact relative links must still resolve.
Human navigability moves to the doc viewer (DEC-0244).

## Rationale

The docs are for the agent first and foremost — the stakeholder's
framing. Bare IDs cut ~30% off the highest-re-read documents at zero
information loss, and they are *more* rot-proof than links: a slug
rename breaks every stored path but never an ID, since resolution
happens at check time against the live tree. DEC-0090's readability
benefit is preserved by the viewer, which linkifies at render time
instead of storage time.

## Alternatives Considered

- **Keep inline links** (DEC-0090's rule): full click-through in raw
  GitHub/IDE rendering, but the token overhead persists and grows
  with the corpus.
- **Bare IDs in citation clauses only**: roughly half the savings,
  two styles in one document, drift-prone rule surface.
- **Derived stripped views only, canon unchanged**: no convention
  churn, but design-time context — where refinement actually reads
  canon — saves nothing.

## Implications

SPEC-artifact-common's body conventions and integrity rules are
rewritten citing this decision; `tools/check_links.py` and the
skill's bundled copy invert Rule 8 and re-express Rules 9 and 14
(Implements lines and trigger-registry subscriber lines use bare
IDs); the skill's templates and installed AGENTS.md show the bare
form; the vendored `.agents` skill copy is synced. The existing
corpus is brought into compliance by DEC-0243. Tooling that parses
`(per DEC-nnnn)` citations must accept the bare form.
