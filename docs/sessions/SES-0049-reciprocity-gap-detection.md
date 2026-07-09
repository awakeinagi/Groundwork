---
id: SES-0049
type: session
title: Reciprocity gap detection — derived-work completeness, dead cites, mention edges
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-08
participant: awakeinagi@gmail.com
participant-role: eng-lead
facilitator: Claude Code (claude-fable-5)
transcript-fidelity: reconstructed
links:
  relates-to: [BG-0001, EP-0008, DEC-0242]
---

# SES-0049: Reciprocity Gap Detection

Method-level session, following the SES-0035 precedent (fix the method,
then the instance). Trigger: the stakeholder noticed EP-0008 is absent
from BG-0001's Derived Work section and asked why `tools/check_links.py`
did not flag it.

## Transcript

### T1 — Stakeholder

"I've just noticed that our EP-0008 is not mentioned in BG-0001. Our
link checking script should have picked that up."

### T2 — Facilitator

Investigated and confirmed, with root cause:

- BG-0001's Derived Work section lists EP-0001..EP-0007 and SP-0001; it
  omits EP-0008 — and also SP-0006 and SP-0007, all of which carry
  `derives-from: [BG-0001]`.
- The checker passes because derivation is recorded one-directionally in
  the child's frontmatter. No rule requires the parent's body to mention
  its children; the Derived Work section is unchecked prose. Reciprocity
  is enforced only for `impacts`/`impacted-by` (rule 6) and component
  elements ↔ stories (rule 9).
- Process root cause: EP-0008 was derived late (SES-0038, the
  gap-closure retrospective) after BG-0001's Derived Work list was
  written. The derivation playbooks have no "update the parent's Derived
  Work section" step, so late-derived children silently miss the list.

### T3 — Stakeholder

Asked to generalize: use the graph to find cases like this — the items
say they derive from BG-0001 but BG-0001's Derived Work doesn't list
them. What other connections indicate documentation gaps?

### T4 — Facilitator

Ran an empirical reciprocity sweep over all 2,078 frontmatter edges:
for each edge A→B, does A's body prose mention B, and does B's body
prose mention A (bare-ID matching per DEC-0242, code spans excluded)?
Patterns ≥70% consistent are treated as real conventions whose
exceptions are gaps. Findings, by strength:

1. **Parent doesn't list derived children.** Epic→goal 7/8 (BG-0001
   misses EP-0008; SP-0006/SP-0007 also missing at goal level);
   story→epic 59/64 (EP-0006 misses ST-0051..ST-0055 — all late-derived
   deferred release-2 stories). Same root cause as T2.
2. **Dead cites.** ~66 instances of a frontmatter `cites:` DEC never
   referenced in body prose (24 epics, 19 components, 9 stories, 3 in
   BG-0001: DEC-0192..0194). Since contract lines carry `(per DEC)`
   citations in prose, a dead cite is frontmatter cruft or missing
   provenance in the text.
3. **Component-refinement sessions not mentioning their epic.**
   SES-0040..SES-0044 `relates-to` EP-0008 but never say so in the
   body (pattern 76% consistent). Sessions are append-only once
   closed — retroactive fixes are off the table.
4. **Epic impact edges unexplained in prose.** 64–71% consistent,
   8 gaps per direction. Weakest convention.

Negative result: `satisfies` for stories/components/spikes is 0%
mentioned in prose in either direction — pure frontmatter traceability
by design. Blanket "every edge appears in prose" would be wrong; rules
must be per edge-type.

Tooling observation: the graph index carries frontmatter edges only;
body bare-ID mentions are not indexed, which is exactly why none of
this was queryable. A `MENTIONS` edge would make each asymmetry a
two-line Cypher query.

### T5 — Stakeholder

"Great finds. Missing provenance is a first-class problem for
Groundwork so we must surface and handle those types of problems."
Directed a proper design session.

### T6 — Facilitator

Grilling round 1, enforcement level per gap class (recommendations
first): (1) derived-children completeness — blocking checker rule /
warning / graph-only; (2) dead cites — blocking after in-session
remediation / warning-first / warning-only; (3) reverse direction,
body-mentioned DECs absent from `cites:` — blocking (measure first) /
warning / no; (4) session-side rules given append-only closed sessions —
warning + playbook step (recommended) / blocking for new sessions only /
leave sessions out.

### T7 — Stakeholder

(1) Blocking. (2) Blocking, after remediation. (3) Yes, blocking too.
(4) Pushed back on the recommendation: sessions should be **blocking**
as well — "Is editing cross-references in a closed document really a
violation? As long as we're not changing the content, I see it more as
data enrichment." (Facilitator note: this aligns with DEC-0091's
sanction of formatting-only edits to immutable artifacts, under which
DEC-0243 de-linkified the corpus.)

### T8 — Facilitator

Measured the reverse-cites backlog: 110 body-mentioned DECs absent from
`cites:` across 54 artifacts — on top of ~66 dead cites (~176 items
total, ~70 artifacts). Noted the structural-provenance edge case:
BG-0001 cites DEC-0192..0194 (goal-template redesign) which govern the
artifact's *structure*, not any single line — dropping those cites
would lose real provenance; disposition rules must allow a one-line
provenance note. Grilling round 2: (1) shape of the enrichment
sanction extending DEC-0091 — transcript-protected (recommended) /
including transcripts / frontmatter-only; (2) impact-edge prose —
warning for epics, silent for stories (recommended) / blocking /
graph-only; (3) remediation execution — full sweep this session
(recommended) / staged / disposition-table review first; (4) graph
MENTIONS edge + gaps audit extension — yes (recommended) / index only /
skip.

### T9 — Stakeholder

(1) Transcript-protected enrichment accepted, with a refinement
proposal: append a metadata section to the bottom of the Transcript
section, without editing the internal record. (2) Stronger than
recommended: **blocking** for epics, stories, and components on the
**impactor** side (the node carrying `impacts`) — "having a proper
explanation of how one system item impacts another is vital"; silent
on the impactee side; missing/one-sided impact edges in a known
impactor→impactee relationship also block (reciprocity, existing rule
6, affirmed). (3) Full sweep this session. (4) Yes — index + gaps
audit.

### T10 — Facilitator

Presented six drafted decisions for plain-language confirmation:
DEC-0246 (derived-work completeness blocking), DEC-0247 (cites↔prose
synchronization, both directions blocking, with per-instance
remediation dispositions), DEC-0248 (cross-reference enrichment
sanction extending DEC-0091, transcript-protected via an appended
Post-Close Enrichment subsection), DEC-0249 (impactor-side impact
prose blocking for epics/stories/components, impactee silent),
DEC-0250 (session relates-to targets must appear in the body),
DEC-0251 (graph MENTIONS edges + reciprocity gaps audits). Stated
sweep scope: 8 derived-work entries, ~176 cite-sync items, 5 session
enrichments, ~38 impact explanations; diff and disposition summary to
be reviewed before commit.

### T11 — Stakeholder

"Approved. Please continue."

### T12 — Facilitator (distillation checks & recall audit)

**Consistency checks (per DEC-0157, DEC-0158)** ran over
DEC-0246..DEC-0251 immediately after recording. `sweep`: 13 ratified
citers flagged for review — ST-0045 (cites DEC-0242; its provenance
drill-down view is unaffected and may later consume MENTIONS data —
informational), and DEC-0026's citers CMP-0001, EP-0001..EP-0007,
ST-0007, ST-0045 (DEC-0249 adds a prose obligation without changing
DEC-0026's edge semantics; the affected epics are remediated in this
session's sweep). Disposition: no contradictions, no staleness.
`terms`: `impacted-by` overlap with DEC-0196/DEC-0199 (coupling
checks — complementary mechanisms, no link needed) and
`groundwork_graph.py` overlap with DEC-0116/DEC-0244 (shared tooling
noun, no contradiction). Disposition: reviewed, clear.

**Decision-recall audit** on this session (15 candidates, one Sonnet 5
judge). Findings and resolutions:

- DEC-0157/DEC-0158 flagged as unevidenced — the checks had run but
  were unrecorded; resolved by this turn's record.
- DEC-0063 (product graph index carries frontmatter metadata only,
  bodies stay in the store) unreconciled with MENTIONS: resolved by
  amending DEC-0251 (relates-to + boundary paragraph — a MENTIONS
  edge records that a reference exists, never body content, the shape
  DEC-0092's IMPLEMENTS edges already exercise).
- DEC-0092/DEC-0094 precedent narrated but uncited in DEC-0246:
  resolved by amending DEC-0246's relates-to and Rationale.
- Contract gap: DEC-0247's dispositions didn't cover a dead cite on a
  *superseded* DEC (SP-0002 cites DEC-0061/DEC-0070, superseded by
  DEC-0102): resolved by adding a fifth disposition — prose notes the
  supersession; re-pointing happens only via re-affirmation.

**Tooling find:** while implementing DEC-0251, discovered the graph's
Implements-line parser still expected DEC-0090-era markdown links, so
after DEC-0243's de-linkification the graph carried **zero**
IMPLEMENTS edges — silently degrading `gaps`, `elements`, and
`progress`. Fixed to bare-ID parsing (a missed implication of
DEC-0242's "tooling must accept the bare form").

### T13 — Facilitator (execution record)

Implemented and remediated in-session:

- **Checker**: rules 15–18 added to `tools/check_links.py` and the
  skill's bundled copy (DEC-0246, DEC-0247, DEC-0249, DEC-0250).
  Initial run: 243 violations (18 / 167 / 40 / 18 by rule).
- **Graph**: MENTIONS edges + five reciprocity audits in `gaps`
  (DEC-0251); schema and cookbook docs updated. The IMPLEMENTS parser
  bug from T12 fixed — 65 IMPLEMENTS and 3,380 MENTIONS edges now
  indexed (5,826 edges total, up from 2,078).
- **Method docs**: derivation playbooks gained the update-the-parent
  and impactor-prose steps; the session protocol and template gained
  the relates-to mention obligation and the Post-Close Enrichment
  form; integrity rules 12–15 and the enrichment carve-out documented;
  AGENTS.md (project + skill asset) updated; two stale
  markdown-link-era wordings fixed alongside.
- **Remediation**: all 243 items fixed across 92 artifacts — BG-0001
  by the facilitator (Derived Work entries for EP-0008/SP-0006/
  SP-0007; six cites added; DEC-0192..0194 structural-provenance
  note); five parallel batches for epics (67), stories (71),
  components (47, plus one code-span citation de-backticked per
  DEC-0242), spikes (27, incl. the SP-0002 superseded-cite
  disposition), sessions (16 files, Post-Close Enrichment per
  DEC-0248). No cite was dropped as cruft anywhere — every dead cite
  anchored to genuine governed content. All 38 impact-edge
  explanations grounded in the deriving sessions.
- **Verification**: `check_links.py` → OK, 400 artifacts, 0
  violations (18 pre-existing coverage-gap warnings untouched); all
  five graph reciprocity audits empty; diff audited — no artifact ID
  lost from any file, no contract item renumbered, no status/approval
  field touched.

## Decisions Produced

DEC-0246, DEC-0247, DEC-0248, DEC-0249, DEC-0250, DEC-0251

## Conflicts Raised

None.
