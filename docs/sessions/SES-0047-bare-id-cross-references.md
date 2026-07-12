---
id: SES-0047
type: session
title: Bare-ID cross-references and the doc viewer
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Method-level session addressing token overhead of markdown links
  (~264 KB / 65k tokens corpus-wide, 25-30% of component docs). Converted
  body prose from inline markdown artifact links to bare IDs (IDs
  derivable from <ID>-<slug>.md pattern). Full-corpus migration, bare
  IDs everywhere with non-artifact links remaining markdown. Inverted
  checker to enforce bare IDs, flag inline artifact links. Built
  single-page vanilla-JavaScript viewer (human_docs.html) with Tailwind
  CSS, Mermaid rendering, full-text search, backlinks panel, graph and
  semantic-search API endpoints from skill scripts. Produced
  DEC-0242-DEC-0244.
participant: awakeinagi@gmail.com
participant-role: eng-lead
facilitator: Claude Code (claude-fable-5)
transcript-fidelity: reconstructed
links:
  relates-to: [DEC-0009, DEC-0090, DEC-0091, DEC-0242, DEC-0243, DEC-0244]
---

# SES-0047: Bare-ID Cross-References and the Doc Viewer

Method-level session, following SES-0014's precedent (which produced
the convention this session reverses). Focus: the token cost of the
documentation corpus in agent context, especially Component Docs.

## Purpose

Method-level session to address the token overhead of inline markdown cross-references corpus-wide and establish the human browsing surface for bare-ID navigation. (skeleton restored at SES-0078)

## Transcript

### T1 — Facilitator

Presented a measured analysis of where tokens go, prompted by the
stakeholder's observation that the docs — CMPs especially — consume too
much agent context. Findings: inline markdown link paths are pure
redundancy (every artifact file is `<ID>-<slug>.md` in a
type-determined directory, so the path is fully derivable from the
ID). Measured overhead: components 29%, epics 30%, sessions 25%,
stories 23%, decisions 12% — ~264 KB / ~65k tokens corpus-wide. A
CMP-0004 read costs ~8.5k tokens of which ~2.5k is repeated paths.
Ranked levers: (1) bare-ID prose references, (2) derived handoff
views, (3) prose trimming. Recommended (1) as a convention change run
through a proper session.

### T2 — Stakeholder

Chose to run it as a proper design session.

### T3 — Facilitator

Round 1, four questions with recommendations: adopt bare IDs in prose
(recommended: everywhere, non-artifact links stay markdown); migration
scope (recommended: living artifacts only, conservative on
immutability); checker enforcement (recommended: full inversion —
bare IDs must resolve, inline artifact links become violations);
navigation mitigation (recommended: small linkify script).

### T4 — Stakeholder

Bare IDs everywhere — "The docs are for the agent first and
foremost," with interest in exploring the linkify option further.
**Full corpus** migration, beyond the facilitator's conservative
living-artifacts recommendation. Full checker inversion as
recommended. Navigation amended beyond the recommendation: a
single-page webapp — one .html file, vanilla JavaScript — for humans
to browse the docs with clean rendering and clickable links.

### T5 — Facilitator

Verified the migration surface: zero anchored artifact links, four
links with descriptive (non-ID) text to reword manually. Stated one
owned design call: at 387 files / 1.3 MB the viewer eager-loads the
whole corpus, making search and backlinks free. Round 2, three viewer
questions: file discovery (recommended: parse `python3 -m
http.server` directory listings — zero derived state; alternative: a
checker-emitted manifest enabling GitHub Pages); markdown rendering
(recommended: hand-rolled subset renderer for the checker-constrained
dialect; alternative: embedded minified library); features
(recommended: full-text search, backlinks panel, frontmatter chips;
Mermaid rendering listed as heavy).

### T6 — Stakeholder

Directory-listing discovery as recommended. Hand-rolled renderer
**plus Tailwind CSS** (amendment). Features: search, backlinks,
frontmatter chips as recommended, **plus Mermaid rendering** and a
further amendment — the Python server should plug into the vendored
`.agents` skill scripts to expose the graph and semantic search as
advanced-search endpoints for the viewer.

### T7 — Facilitator

Pre-distillation provenance check surfaced that the existing
convention is decision-backed: DEC-0090 (body cross-references must
be resolvable markdown links, from SES-0014) — so the new convention
supersedes it rather than merely amending tooling. And DEC-0091
already sanctions exactly the needed edit class on immutable
artifacts ("reference formatting that changes no words, meaning, or
structure"), for the initial linkification pass *and future fixes of
the same class* — the full-corpus de-linkification is the same class,
inverse direction, so no fresh immutability exception is required.
Read back three decisions: DEC-0242 (bare-ID convention, supersedes
DEC-0090; frontmatter semantics unchanged per DEC-0009; item-level
citation granularity unchanged), DEC-0243 (full-corpus pass under
DEC-0091's sanction), DEC-0244 (viewer + API server as the
human-navigability home; Tailwind/Mermaid load from CDN at view time,
flagged as an internet-at-view-time constraint affecting humans
only). Method-level propagation included: SPEC-artifact-common, repo
AGENTS.md, the skill's templates and bundled checker, and the
vendored `.agents` copy.

### T8 — Stakeholder

Confirmed all three decisions.

## Consistency Checks

`sweep DEC-0242 DEC-0243 DEC-0244` and `terms` (per DEC-0157,
DEC-0158), plus a direct walk of DEC-0090's citers on supersession:

- **ST-0045** — AC2 contractually relied on DEC-0090's linked form
  ("relies on every body cross-reference already being a resolvable
  markdown link"). Amended: the view resolves bare IDs at render time
  (per DEC-0242); cite swapped DEC-0090 → DEC-0242; re-affirmed by the
  approver in this session.
- **DEC-0092** — mandates the `Implements:` line, notation clause says
  "as resolvable markdown links (per DEC-0090)". Substance (mandatory,
  enforced line) untouched; notation partially superseded, covered by
  DEC-0242's Rule 9 re-expression. Disposition: recorded, decision
  immutable, no edit.
- **DEC-0009's other citers** (CMP-0001, EP-0001, EP-0004, ST-0001,
  ST-0005, ST-0007) — cite it for frontmatter/graph semantics, which
  DEC-0242 explicitly leaves unchanged. Consistent.
- **terms**: DEC-0244's mentions of the skill scripts co-occur with
  DEC-0111/DEC-0116/DEC-0120 (the tools' origin decisions) — DEC-0244
  reuses that tooling, contradicts nothing; DEC-0138 is the operative
  link and is already in `relates-to`. No link added.
- **SES-0014/SES-0015/SES-0034** — historical records mentioning
  DEC-0090; sessions are append-only, no action.

## Decision-Recall Audit

Run on DEC-0242 post-migration (doubling as verification that the
audit tooling reads the bare-ID corpus correctly — it does; the
considered set picked up bare inline references). Judge verdict:
**Nothing to add** — twelve candidates, each either noise (disjoint
checker rules, search-tooling internals), already in frontmatter
(DEC-0091), or already dispositioned in this session's Consistency
Checks (DEC-0092, the closest near-miss). Judge observation: DEC-0091
surfaced as a candidate despite being in `relates-to` because the
graph index was stale during the run — the tool's documented
degradation, cleared by rebuilding the index.

## Decisions Produced

- DEC-0242 — body cross-references are bare artifact IDs (supersedes
  DEC-0090)
- DEC-0243 — full-corpus de-linkification pass under DEC-0091's
  sanction
- DEC-0244 — single-file doc viewer plus API server backed by the
  skill's search and graph tooling

## Conflicts Raised

None raised during this session. (skeleton restored at SES-0078)
