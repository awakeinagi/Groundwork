---
id: SES-0092
type: session
title: "RSCH spec and template design — method-level detail while EP-0010 gates"
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-13
participant: operator, Claude
participant-role: stakeholder, facilitator
facilitator: Claude
transcript-fidelity: verbatim
kind: full
intake: {origin: user, proposed-by: operator}
overview: >-
  Continuing the Research (RSCH) artifact-type refinement, the
  stakeholder asked the facilitator to place the remaining work
  among BG-0002's now-larger sibling epic set. RSCH's static-design
  home, EP-0010, was found mid-refinement and gate-locked in the
  concurrently open SES-0091, so the facilitator proposed grilling
  RSCH at method level instead: SPEC-research content, template,
  frontmatter schema, subfile and round-section conventions, and
  checker rule specifics, as accepted decisions the future EP-0010
  stories can cite once gated. Three grilling rounds produced eleven
  accepted decisions (DEC-0488 through DEC-0498): the main-file
  required-section skeleton, the Method section and its loop stop
  conditions, the round-section convention with a conditional Next
  Round Plan, numbered research goals, the Source Register and per-
  finding identifier formats, create-time frontmatter requirements,
  the exclusion of release scoping and TRIGGERS, the Idea-pattern
  two-tier validation split, the concluded gate, and same-change
  SPEC-artifact-common fold-back with a pinned verbatim template.
  Three ideas were captured (IDEA-0066 through IDEA-0068). Close-out
  ran a consistency sweep (four informational, non-contradictory
  citer hits) and a clean terms check, plus a recall audit against
  the parallel SES-0091 Engine decisions: a Sonnet 5 judge found one
  gap, since resolved — DEC-0496's tier-1 items and DEC-0497's
  concluded gate both fall inside DEC-0475's write-time self-trust
  categories (schema validity, link referential integrity, gate-
  state legality), while RSCH's completeness rules run check-time,
  so DEC-0496 and DEC-0497 now carry relates-to links to DEC-0475.
  The session is closed.
links:
  relates-to: [EP-0010, DEC-0464, DEC-0456, BG-0002, SES-0091, DEC-0488, DEC-0489, DEC-0490, DEC-0491, DEC-0492, DEC-0493, DEC-0494, DEC-0495, DEC-0496, DEC-0497, DEC-0498, IDEA-0066, IDEA-0067, IDEA-0068]
---

# SES-0092: RSCH spec and template design — method-level detail while EP-0010 gates

## Purpose

Continue refining the Research (RSCH) artifact type. With new epics
now standing under BG-0002, the session first locates where RSCH's
remaining static-design work belongs among them, then — finding its
natural home (EP-0010) mid-refinement and gate-locked — proceeds to
grill the method-level detail that stands on its own regardless of
gate timing: the SPEC-research content, the RSCH template, the
frontmatter schema, subfile and round-section conventions, and
checker rule specifics.

## Transcript

### T1

**Stakeholder** (verbatim, three consecutive messages): "Let's
continue refining this new Research artifact. There are new Epics
under BG-0002; see where this fits best and let's start." Then, after
the facilitator's placement analysis: "Can you work under EP-0010
while it's in-refinement?" Then: "OK let's start grilling while we
wait".

### T2

**Facilitator** (restatement and classification): The facilitator
located the BG-0002 sibling epic set and identified EP-0010 (Engine
Core & Artifact Model, draft) as RSCH's static-design home per
DEC-0464 and DEC-0456, with EP-0009 keeping the dynamic side. It
reported that EP-0010 is mid-refinement in the concurrently open
SES-0091 (thirteen decisions confirmed, recording and close pending),
and that the gate invariant bars deriving RSCH build stories from a
draft epic with no waiver. It recommended the legal high-value
alternative: continue refining RSCH at method level — the
SPEC-research content, template, frontmatter schema, subfile and
round-section conventions, and checker rule specifics — as accepted
decisions the future EP-0010 stories will cite, making post-gate
story derivation nearly mechanical. It committed not to touch the
open SES-0091.

### T3

**Stakeholder** (alignment): Confirmed the method-level path: start
grilling while EP-0010's gate is pending.

### T4

**Facilitator** (SPEC-precedent briefing): Reported the SPEC-precedent
briefing: SPEC-artifact-common's identity/frontmatter/status/integrity
structure; SPEC-idea's tier-1 versus tier-2 validation split
(DEC-0269); SPEC-session's close-gate and create-required fields
(DEC-0417 pattern); and the checker's rule map, which now runs through
rule 26 against SPEC-artifact-common's own enumerated rules 1 through
11 — a documented drift. It noted that RSCH currently exists only in
decision records: no prefix-table entry, FIELD_SCHEMA row,
REQUIRED_AT_CREATE row, skeleton entry, or template.

### T5

**Facilitator** (grilling round 1): Asked the required body sections,
the frontmatter additions and create-time requirements, the
round-section convention, and subfile naming and indexing.

### T6

**Stakeholder** (round 1 decisions): Accepted all four
recommendations: per-round nesting (Inspiration, Research Goals,
Source Register, dated Round sections each closing with Findings and
Business-Goal Applicability, a conditional Subtopic Files index); lean
frontmatter with commissioned-by, source-mode, and derives-from
required at create; dated H2 rounds with gapless numbering and ordered
dates; and slug-named subfiles with a both-ways directory-to-index
check.

### T7

**Facilitator** (round 2): Asked the Source Register format, the
tier-1/tier-2 rule split, status-transition gates, and
release/TRIGGERS scoping plus the SPEC-common fold-back.

### T8

**Stakeholder** (round 2, partial): Accepted the S-numbered register
table with [Sn] finding citations and the concluded-gate with all
other transitions free. Asked for elaboration on the tier split and on
scoping before answering those two questions.

### T9

**Facilitator** (elaboration): Elaborated in plain language: tier 1
refuses a write instantly on facts the payload alone shows and must
never be wrong even mid-work; tier 2 tolerates work-in-flight and
checks cross-file and cross-artifact completeness at commit; pushing
completeness rules into tier 1 would refuse legitimate mid-round
saves. On scoping: release labels and TRIGGERS serve shipping
deliverables, which research is not; the fold-back obligation prevents
SPEC-artifact-common from repeating its rules-1-through-11 drift for
the new type.

### T10

**Stakeholder** (tier split and card format): Chose the Idea-pattern
tier split. Asked for grilling cards to be re-presented with detail on
the options and previews reserved for examples; the facilitator then
discovered empirically, via a stakeholder screenshot, that Claude
Code's preview layout hides option descriptions entirely, corrected
its approach to putting full analysis in chat before each card, and
noted the DEC-0472 through DEC-0474 guidance needs a method-level
revisit, queued as an idea.

### T11

**Stakeholder** (scoping decision): Chose banning both release scoping
and TRIGGERS at tier 1, and instructed that an idea be captured to
sync SPEC-artifact-common with the checker's actual rule set.

### T12

**Facilitator** (fold-back options): Elaborated the fold-back options
with concrete diffs and timelines: same-change keeps the master spec
born-in-sync for the three RSCH spots while the sync idea covers
historical drift; batching everything into the sync idea leaves a
window where SPEC-artifact-common denies RSCH exists.

### T13

**Stakeholder** (fold-back choice): Chose same-change fold-back for
the RSCH entries.

### T14

**Facilitator** (round 3): Asked whether per-finding identifiers are
required structure and whether the template should be pinned by
decision now; both recommendations were accepted, and the stakeholder
asked the facilitator to propose any further sections before
finalizing.

### T15

**Facilitator** (further-sections proposal): Proposed five candidates
with analysis: Method (search strategy, source-admission bar,
goals-met criteria); a per-round Goals Assessment; Derived Work as a
body mirror of the inspired list; an optional per-round Open
Questions; and a cumulative Key Takeaways section it recommended
against as duplicating the overview field.

### T16

**Stakeholder** (sections chosen): Adopted Method, Goals Assessment,
Derived Work, and Open Questions exactly as recommended, skipped Key
Takeaways, and asked for further loop-friendly structure, stating a
desire to incorporate more agent loops into Groundwork.

### T17

**Facilitator** (loop-structure proposal): Proposed three loop
structures — numbered goals G1, G2, and so on; a conditional Next
Round Plan subsection as the loop's resumable state; and required stop
conditions in Method — and recommended against mirroring loop state
into frontmatter as a drift surface.

### T18

**Stakeholder** (loop structure chosen): Adopted all three and
declined the frontmatter mirror.

### T19

**Facilitator** (closing summary): Presented the closing summary, the
fully assembled pinned template, and the inspired-ideas check listing
three ideas.

### T20

**Stakeholder** (confirmation): Confirmed the summary, the template,
and all three ideas, with nothing further to add.

### T21

**Facilitator**: Reported the close-out machinery. The consistency sweep over DEC-0488 through DEC-0498 returned four informational citer hits (SP-0019 via DEC-0447 and DEC-0488; CMP-0001, ST-0001, and ST-0065 via DEC-0269 and DEC-0496), none contradictory, needing no edits; the terms check was clean. The recall audit examined the parallel SES-0091 Engine decision set alongside general candidates; a Sonnet 5 judge found one gap — DEC-0475's rule that write-time enforcement covers only self-trust invariants was never reconciled against DEC-0496's tier-1 list. The facilitator's disposition, recorded here: every RSCH tier-1 item falls inside DEC-0475's write-time categories — the create-required trio and enum validity are schema validity, derives-from naming a real session is link referential integrity, the DEC-0497 concluded gate is gate-state transition legality, and the create-time skeleton is emitted by the create operation itself rather than refused from a payload — while all RSCH completeness and cross-file rules run as check-time rule families, so DEC-0496 and DEC-0497 conform to DEC-0475's boundary test and now carry relates-to pointers to it. All other candidates (DEC-0482, DEC-0483, DEC-0479, DEC-0484, DEC-0476, DEC-0478, DEC-0480, DEC-0098) were judged not-a-gap: mechanism, deployment, or output-format constraints the implementing stories inherit without contradiction.

### T22

**Facilitator**: Closed the session under the stakeholder's standing authorization from the distillation confirmation.

## Decisions Produced

Eleven decisions were produced by this method-level grilling round:

- DEC-0488 — RSCH main-file required sections
- DEC-0489 — The Method section and its stop conditions
- DEC-0490 — Round-section convention
- DEC-0491 — Numbered research goals
- DEC-0492 — Source Register format and citation
- DEC-0493 — Per-finding identifiers
- DEC-0494 — Frontmatter additions and create-time requirements
- DEC-0495 — No release scoping or trigger subscriptions
- DEC-0496 — Two-tier validation split
- DEC-0497 — The concluded gate
- DEC-0498 — Fold-back and the pinned template

Three ideas were captured alongside these decisions: IDEA-0066 (sync
SPEC-artifact-common's rule documentation with the checker's actual
rule set), IDEA-0067 (revise grilling-card guidance for the
empirically mapped preview-layout mechanics), and IDEA-0068
(generalize Research's loop-friendly structure to other artifact
types).

## Conflicts Raised

None yet.
