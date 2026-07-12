---
id: SES-0053
type: session
title: Per-artifact progressive disclosure — overview field and concise-read tooling
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-09
participant: awakeinagi@gmail.com
participant-role: stakeholder
facilitator: Claude Code (claude-fable-5)
transcript-fidelity: reconstructed
overview: >-
  Method-level session adopting per-artifact progressive disclosure to cut
  agent token spend when exploring the corpus: every artifact gains a
  derived, non-normative frontmatter overview (max 250 words,
  checker-enforced), a new stdlib read tool serves concise reads
  (overviews, outlines, sections, elements, contract items, turn spans,
  glossary terms, citers), and search/graph outputs include overviews by
  default. Existing artifacts are bulk-retrofitted by a Haiku-pinned
  overview-writer agent. Produced DEC-0284..DEC-0291 and captured
  IDEA-0003 (system-architect agent) and IDEA-0004 (ux-explorer agent).
  Distinct concern from EP-0007, which may later consume these outputs.
links:
  relates-to: [EP-0007, DEC-0017, DEC-0068, DEC-0248, IDEA-0003, IDEA-0004, DEC-0284, DEC-0285, DEC-0286, DEC-0287, DEC-0288, DEC-0289, DEC-0290, DEC-0291]
---

# SES-0053: Per-Artifact Progressive Disclosure

## Purpose

Intake and full grilling of a stakeholder proposal to minimize agent
token spend when exploring the docs corpus, via "progressive
disclosure" in the agent-skills sense: read a small overview first,
open the full file only when needed, and serve common
small-information needs without whole-file reads. Prior art
distinguished in-session: EP-0007's Consolidation Memory Layer
(DEC-0017, DEC-0068) covers the *application's* retrieval design and
is explicitly a separate concern (T3) — this session changes the
*method now* (frontmatter schema, checker, skill tooling, corpus
retrofit). The non-normativity ruling leans on the immutability
carve-out precedent of DEC-0248. Captured IDEA-0003 and IDEA-0004 at
the close. Facilitated under the change-intake protocol (DEC-0255,
DEC-0256, DEC-0266).

## Transcript

### T1 — Stakeholder

"I've noticed that you have to burn a lot of tokens reading these
documents. I would like to minimize your token spend when exploring
the docs and use something like 'progressive disclosure' from agent
skills. What if we added an overview field [to] the frontmatter of our
docs so an agent could first read that (maybe add a script to the
groundwork agent skill) and then decide if it needs to read more of
the file. We could also [add] more options for concise reading of doc
files related to common use cases; anything we can do for the agent
not to have to read the entire file just to discover a relatively
small piece of information."

### T2 — Facilitator

Intake steps run: todo list (DEC-0256), locate pass (DEC-0266) via
semantic search. Restated the intention as three parts — (1) an
`overview:` frontmatter field on every artifact, (2) skill tooling to
read overviews first and bodies selectively, (3) concise-read
affordances for common use cases. Surfaced prior art: EP-0007 /
DEC-0017 / DEC-0068 cover this concern for the *product*; today's
partial method-level coverage is search snippets, the graph tool, and
the unused CON type. Named the affected set (SPEC-artifact-common,
checker, skill references/templates/scripts, both AGENTS.md files,
~438-artifact retrofit) and the drift tension (an overview duplicates
meaning). Recommended a full grilling session.

### T3 — Stakeholder

Confirmed alignment, with a clarification for the record: this is a
separate concern from the Consolidation Memory Layer (EP-0007), though
what is built here could serve its goals — the layer could consume the
overviews and concise-read outputs.

### T4 — Facilitator

Round 1 (foundations), four questions with recommendations: placement
(frontmatter field vs first body section vs sidecar index; recommended
frontmatter — machine-extractable via cheap YAML parse); coverage (all
artifact types vs pipeline-only vs size-triggered; recommended all);
normativity (derived/non-normative like consolidations — never citable
as provenance, body wins, regenerable, which legalizes retrofitting
closed sessions and accepted decisions in the spirit of DEC-0248 — vs
normative ratified content; recommended derived); enforcement (checker
presence rule + same-edit accuracy rule + gate checklist vs presence
only vs advisory; recommended the first).

### T5 — Stakeholder

Accepted all four recommendations: frontmatter field, all types,
derived/non-normative, checker + same-edit rule.

### T6 — Facilitator

Round 2 (tooling, content, retrofit): tooling shape (new stdlib
read-tool script vs extending search/graph vs both from day one;
recommended the new script, with search-output enrichment deferrable);
v1 affordances (multi-select: batch overviews, named-section read, CMP
element read, session turn-range read); retrofit strategy (bulk
generation now via parallel subagents vs big-types-first vs
incremental; recommended bulk now, checker rule landing in the same
commit); content standard (recommended self-sufficient 2–4 sentences
≈80 words, per-type guidance in templates).

### T7 — Stakeholder

New read-tool script accepted. All four affordances selected, plus an
instruction to think of other common needs worth addressing. Retrofit:
bulk-generate with parallel subagents accepted, amended — generate
with a cheaper model such as Haiku or Opus; ensure the spawning logic
always uses the appropriate model; consider a custom agent for the
project in `.claude/agents/`. Content standard: option 1 shape, but
with the max raised to 250 words.

### T8 — Facilitator

Round 3: proposed three further affordances — outline read (headings +
CMP element inventory; the middle disclosure layer), contract-item
lookup (`item CMP-nnnn StorageService.B-3`), glossary term lookup —
plus optional citers lookup (overlaps the graph tool but stdlib-cheap).
Generation model (recommended Haiku 4.5 with the 250-word cap and
spot-check as safety net; alternatives Sonnet 5 or split-by-type).
Custom agent (recommended yes: versioned `.claude/agents/`
overview-writer with the model pinned in frontmatter). Checker scope
(recommended presence + 250-word cap; both mechanical).

### T9 — Stakeholder

All four extra affordances selected, including citers. Haiku 4.5
accepted. Custom agent: yes. Checker: presence + cap.

### T10 — Facilitator

Decision playback in plain language (field; non-normativity; 250-word
standard; checker + same-edit enforcement; read tool with eight
subcommands; Haiku retrofit via custom agent). Proposed parking
"search results include overviews" as an IDEA. Ran the inspired-ideas
check (DEC-0261).

### T11 — Stakeholder

(a) Search-output enrichment should be built now, not parked — and
graph-search outputs should include overviews too. (b) Two additional
subagents wanted: a `system-architect` agent to help plan system
design at each stage of the artifact hierarchy, its context preloaded
with best practices on system architecture and design; and a
`ux-explorer` agent to traverse component and design-element links to
find gaps in the design based on the stated goals / requirements /
needs addressed in higher-level docs (BG, EP, ST).

### T12 — Facilitator

Amended the tooling decision accordingly: search and graph outputs
include overviews by default with an opt-out flag (DEC-0290). Applied
the focus-artifact test (DEC-0260) to the two subagent proposals —
both require different artifacts than this session's focus — and
parked them as IDEA-0003 (system-architect) and IDEA-0004
(ux-explorer) for take-up under the intake protocol in their own
sessions (DEC-0261). Closed into recording: DEC-0284..DEC-0291,
consistency checks, recall audit, implementation, retrofit, checker,
commit.

### T13 — Facilitator (close machinery)

Consistency checks (DEC-0157, DEC-0158) run over DEC-0284..DEC-0291.
Sweep dispositions: EP-0007 and ST-0038 (flagged via DEC-0017,
DEC-0068) are consistent — the separate-concern boundary recorded at
T3 means overviews are a potential input to that layer, not a change
to it. Terms dispositions: DEC-0289's example item ID rides the
DEC-0081 element-scoped item-ID convention — relationship surfaced by
adding DEC-0081 to its relates-to; DEC-0290 directly preserves
DEC-0116's disposable-index stance — DEC-0116 added to its relates-to;
remaining hits (DEC-0111, DEC-0120, DEC-0138, DEC-0244, DEC-0251)
reviewed, consistent, no action.

### T14 — Facilitator (close machinery)

Decision-recall audit run (15 candidates, one Sonnet 5 judge). One
finding confirmed: DEC-0242 was relevant and missing — DEC-0286
asserted overview bare IDs "resolve like any body reference," but
DEC-0242's resolution machinery scans body prose only, so a mistyped
ID inside an overview would have passed the checker silently.
Disposition: DEC-0286 and DEC-0287 amended pre-ratification to cite
DEC-0242 and to extend the new integrity rule — it now checks
presence, the 250-word cap, and that every bare artifact ID inside an
overview resolves. Judge-dismissed candidates (DEC-0246 carried by
DEC-0288's citation; DEC-0007 covered via the DEC-0248 precedent;
DEC-0247 superficial; the rest off-topic) accepted as dismissed.

## Decisions Produced

- DEC-0284 — every artifact carries a frontmatter `overview:` field
- DEC-0285 — overviews are derived, non-normative content
- DEC-0286 — overview content standard: self-sufficient, max 250 words
- DEC-0287 — checker enforces overview presence and the word cap
- DEC-0288 — same-edit accuracy rule and gate-prep faithfulness check
- DEC-0289 — a stdlib read tool owns ID-addressed concise reads
- DEC-0290 — search and graph outputs include overviews by default
- DEC-0291 — bulk retrofit via a Haiku-pinned overview-writer agent

Ideas captured at close (work queue, not this session's scope):
IDEA-0003 (system-architect subagent), IDEA-0004 (ux-explorer
subagent).

## Conflicts Raised

None.
