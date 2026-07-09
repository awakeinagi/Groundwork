---
id: SES-0033
type: session
title: EP-0002 story derivation — session engine, packs, guardrails, synthesis, eval harness
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Sliced Refinement Session Agent epic into 10 stories covering session
  conduct, pack format, guardrails, transcript capture, distillation,
  conflicts, synthesis, context assembly, lifecycle, and evaluation
  harness. Resolved open questions on judge-model independence
  enforcement, authored seed benchmark corpus requirement, and synthesis
  anchoring via default shared-draft prose exclusion. Drafted SP-0008
  spike on pack-format expressiveness (3d timeboxed). Decision-recall
  audit surfaced two contract gaps on turn truncation and conflict
  timeout-to-default. Produced ST-0032-ST-0041, SP-0008, and
  DEC-0178-DEC-0183.
participant: awakeinagi@gmail.com
participant-role: stakeholder
facilitator: Claude Sonnet 5 (claude-sonnet-5) via Claude Code CLI
transcript-fidelity: reconstructed
links:
  relates-to: [EP-0002]
---

# SES-0033: EP-0002 Story Derivation

## Purpose

Slice the approved EP-0002
(Refinement Session Agent) into implementable stories, resolving the
epic's four recorded open questions (judge-model independence, benchmark
corpus bootstrap, synthesis anchoring, pack format expressiveness) plus
build order and a candidate spike.

## Transcript

**T1 — Sponsor.** Continue with creating stories for EP-0002.

**T2 — Agent.** Prep: confirmed EP-0002 is the design frontier
(approved, no derived work), read its full scope (11 bullets: session
conduct via packs, transcript capture, distillation with confirmation,
guardrails, conflict flow, incremental synthesis, context assembly,
session lifecycle, CP triage, glossary maintenance, evaluation harness)
and cited decisions, and confirmed
EP-0004/EP-0007
(context assembly's retrieval dependencies) are both approved — no
blocking upstream work. Proposed a 10-story slice, one per scope bullet
(session lifecycle folded into the session-engine story), plus
confirmed the epic's flagged pack-format-expressiveness risk as a
candidate spike now that stories exist to hang it on.

**T3 — Sponsor.** 10 stories, 1:1 with scope bullets, as recommended.
Yes, draft the spike now.

**T4 — Agent.** Round 2 with recommendations on the three remaining open
questions: (a) judge-model independence enforced via a config-declared
model-family check, refusing to run faithfulness evals on a match
(recommended) vs. a hardcoded fixed judge model or leaving enforcement
to implementer discretion; (b) an authored seed benchmark corpus as a
v1 acceptance criterion, gating the harness from day one (recommended)
vs. organic growth with no seed requirement or a separate corpus-design
spike; (c) the context-assembly story owns anchoring mitigation via a
default exclusion of the shared draft's prose from fresh 1:1 context
(recommended) vs. the synthesis story owning it, or leaving it as an
implementer note with no acceptance criterion.

**T5 — Sponsor.** All three (a), (b), (c) as recommended.

**T6 — Agent.** Round 3: (a) build order — strategy pack format and
session engine as the two foundational stories, with guardrails,
context assembly, and glossary maintenance depending on pack format,
and transcript/distillation, conflict, and synthesis depending on
session engine (recommended) vs. treating pack format as a peer-level
concern with no depends-on edges; (b) the pack-expressiveness spike
timeboxed at 3 days, testing declarative-schema expressiveness against
three shape-diverse pack scenarios — linear grilling,
mediation-with-branching, classification (recommended) vs. a narrower
1-day field-list check; (c) stub this epic's component doc now,
matching every other epic's story-derivation pattern, vs. deferring the
component stub until a story refines toward it.

**T7 — Sponsor.** (a), (b) as recommended. (c) **amended**: defer the
component-doc stub until a story actually refines toward it — no
epic-level component stub in this bundle.

**T8 — Agent (synthesis).** Recorded
DEC-0178–DEC-0181;
drafted ST-0032–ST-0041
(all current, `draft`) with `depends-on` build-order edges and
reciprocal `impacts`/`impacted-by` edges per T6's dependency shape, and
SP-0008
(3-day timebox, draft-ahead ratified with this bundle); amended
EP-0002 (Risks →
resolutions citing the new decisions, Derived Work, `cites`; set
`stale` pending re-affirmation in this gate bundle). No CMP stub drafted
per the sponsor's amendment at T7.

**T9 — Agent (consistency checks,
DEC-0157/DEC-0158).**
Ran `sweep`/`terms` on
DEC-0178–DEC-0181.
`sweep`: no accepted decisions in any new DEC's `relates-to`/
`supersedes` — nothing to walk. `terms`: `pack.yaml` co-occurs, unlinked,
between DEC-0181
and the accepted DEC-0053
— genuine relation, not a conflict; added `relates-to: [DEC-0053]` on
DEC-0181.

**T10 — Agent (decision-recall audits,
DEC-0137).** Ran
the audit on all twelve drafts/amendments
(EP-0002,
ST-0032–ST-0041,
SP-0008);
two Sonnet 5 judge batches of six. Findings applied:
DEC-0035
(storage API's `append-turn`/`close`-only contract) added to
ST-0032
AC1; DEC-0056 added
alongside DEC-0053
in SP-0008's
Method and to ST-0040
AC5; DEC-0039
(escalation queue/status-check mechanics) and
DEC-0021 added to
ST-0036
AC3–5; DEC-0030
(worktree merge mechanics) added to
ST-0037
AC1; DEC-0068 (the resolver
contract itself) added to
ST-0038 AC2,
4, 5; DEC-0130
(`create-change-proposal`/`set-cp-triage` typed operations) added to
ST-0039 AC1, 2, 5;
DEC-0052
(drift audits regenerate from the raw transcript) added to
ST-0041 AC5. "Nothing to
add" verdicts: EP-0002,
ST-0033,
ST-0034,
ST-0035. Two
genuine contract gaps surfaced (not missing-decision findings, resolved
below): whether a streaming turn can be truncated by
ST-0032's
inactivity auto-close, and whether escalated Conflicts opt into
DEC-0039's
timeout-to-default election.

**T11 — Agent.** Round 4 with recommendations on the two surfaced gaps:
(a) a turn actively streaming resets the inactivity clock — auto-close
never truncates mid-turn (recommended) vs. allowing auto-close to
truncate a partial turn; (b) Conflicts do not default into
DEC-0039's
timeout-to-default election — the general opt-in mechanism stays
available per-artifact, but no `CFL-` auto-resolves on a clock by
default (recommended) vs. defaulting Conflicts into the election.

**T12 — Sponsor.** Both (a) and (b) as recommended.

**T13 — Agent (synthesis).** Recorded
DEC-0182
and
DEC-0183;
added ST-0032
AC6 and
ST-0036
AC6 to carry them. Re-ran `python3 tools/check_links.py` — clean (280
existing artifacts plus this bundle's 17 new/amended, 3 pre-existing
unrelated coverage warnings only).

## Decisions Produced

DEC-0178,
DEC-0179,
DEC-0180,
DEC-0181,
DEC-0182,
DEC-0183

## Conflicts Raised

None.
