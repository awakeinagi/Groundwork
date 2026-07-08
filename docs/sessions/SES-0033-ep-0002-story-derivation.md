---
id: SES-0033
type: session
title: EP-0002 story derivation — session engine, packs, guardrails, synthesis, eval harness
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-08
participant: awakeinagi@gmail.com
participant-role: stakeholder
facilitator: Claude Sonnet 5 (claude-sonnet-5) via Claude Code CLI
transcript-fidelity: reconstructed
links:
  relates-to: [EP-0002]
---

# SES-0033: [EP-0002](../epics/EP-0002-refinement-session-agent.md) Story Derivation

## Purpose

Slice the approved [EP-0002](../epics/EP-0002-refinement-session-agent.md)
(Refinement Session Agent) into implementable stories, resolving the
epic's four recorded open questions (judge-model independence, benchmark
corpus bootstrap, synthesis anchoring, pack format expressiveness) plus
build order and a candidate spike.

## Transcript

**T1 — Sponsor.** Continue with creating stories for [EP-0002](../epics/EP-0002-refinement-session-agent.md).

**T2 — Agent.** Prep: confirmed [EP-0002](../epics/EP-0002-refinement-session-agent.md) is the design frontier
(approved, no derived work), read its full scope (11 bullets: session
conduct via packs, transcript capture, distillation with confirmation,
guardrails, conflict flow, incremental synthesis, context assembly,
session lifecycle, CP triage, glossary maintenance, evaluation harness)
and cited decisions, and confirmed
[EP-0004](../epics/EP-0004-graph-index.md)/[EP-0007](../epics/EP-0007-consolidation-memory-layer.md)
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
[DEC-0178](../decisions/DEC-0178-eval-harness-judge-model-family-independence.md)–[DEC-0181](../decisions/DEC-0181-sp-0008-pack-format-expressiveness-spike.md);
drafted [ST-0032](../stories/ST-0032-session-engine-lifecycle-and-contract.md)–[ST-0041](../stories/ST-0041-evaluation-harness.md)
(all current, `draft`) with `depends-on` build-order edges and
reciprocal `impacts`/`impacted-by` edges per T6's dependency shape, and
[SP-0008](../spikes/SP-0008-pack-format-expressiveness-vs-simplicity.md)
(3-day timebox, draft-ahead ratified with this bundle); amended
[EP-0002](../epics/EP-0002-refinement-session-agent.md) (Risks →
resolutions citing the new decisions, Derived Work, `cites`; set
`stale` pending re-affirmation in this gate bundle). No CMP stub drafted
per the sponsor's amendment at T7.

**T9 — Agent (consistency checks,
[DEC-0157](../decisions/DEC-0157-relates-to-sweep-at-distillation.md)/[DEC-0158](../decisions/DEC-0158-identifier-cooccurrence-audit.md)).**
Ran `sweep`/`terms` on
[DEC-0178](../decisions/DEC-0178-eval-harness-judge-model-family-independence.md)–[DEC-0181](../decisions/DEC-0181-sp-0008-pack-format-expressiveness-spike.md).
`sweep`: no accepted decisions in any new DEC's `relates-to`/
`supersedes` — nothing to walk. `terms`: `pack.yaml` co-occurs, unlinked,
between [DEC-0181](../decisions/DEC-0181-sp-0008-pack-format-expressiveness-spike.md)
and the accepted [DEC-0053](../decisions/DEC-0053-strategy-packs-as-plugins.md)
— genuine relation, not a conflict; added `relates-to: [DEC-0053]` on
[DEC-0181](../decisions/DEC-0181-sp-0008-pack-format-expressiveness-spike.md).

**T10 — Agent (decision-recall audits,
[DEC-0137](../decisions/DEC-0137-decision-recall-audit-step.md)).** Ran
the audit on all twelve drafts/amendments
([EP-0002](../epics/EP-0002-refinement-session-agent.md),
[ST-0032](../stories/ST-0032-session-engine-lifecycle-and-contract.md)–[ST-0041](../stories/ST-0041-evaluation-harness.md),
[SP-0008](../spikes/SP-0008-pack-format-expressiveness-vs-simplicity.md));
two Sonnet 5 judge batches of six. Findings applied:
[DEC-0035](../decisions/DEC-0035-store-enforced-append-only-transcripts.md)
(storage API's `append-turn`/`close`-only contract) added to
[ST-0032](../stories/ST-0032-session-engine-lifecycle-and-contract.md)
AC1; [DEC-0056](../decisions/DEC-0056-context-recipes-in-packs.md) added
alongside [DEC-0053](../decisions/DEC-0053-strategy-packs-as-plugins.md)
in [SP-0008](../spikes/SP-0008-pack-format-expressiveness-vs-simplicity.md)'s
Method and to [ST-0040](../stories/ST-0040-glossary-maintenance-in-session.md)
AC5; [DEC-0039](../decisions/DEC-0039-conflict-escalation-operations.md)
(escalation queue/status-check mechanics) and
[DEC-0021](../decisions/DEC-0021-one-on-one-sessions.md) added to
[ST-0036](../stories/ST-0036-conflict-detection-mediation-and-escalation.md)
AC3–5; [DEC-0030](../decisions/DEC-0030-session-worktrees-branch-merge.md)
(worktree merge mechanics) added to
[ST-0037](../stories/ST-0037-incremental-synthesis-and-shared-draft.md)
AC1; [DEC-0068](../decisions/DEC-0068-recipe-resolver.md) (the resolver
contract itself) added to
[ST-0038](../stories/ST-0038-context-assembly-via-pack-recipes.md) AC2,
4, 5; [DEC-0130](../decisions/DEC-0130-mechanical-ops-shared-allowlist.md)
(`create-change-proposal`/`set-cp-triage` typed operations) added to
[ST-0039](../stories/ST-0039-change-proposal-triage.md) AC1, 2, 5;
[DEC-0052](../decisions/DEC-0052-raw-transcripts-regenerable-distillation.md)
(drift audits regenerate from the raw transcript) added to
[ST-0041](../stories/ST-0041-evaluation-harness.md) AC5. "Nothing to
add" verdicts: [EP-0002](../epics/EP-0002-refinement-session-agent.md),
[ST-0033](../stories/ST-0033-strategy-pack-format-and-plugin-loading.md),
[ST-0034](../stories/ST-0034-transcript-capture-and-confirmed-distillation.md),
[ST-0035](../stories/ST-0035-guardrails-and-authority-limits.md). Two
genuine contract gaps surfaced (not missing-decision findings, resolved
below): whether a streaming turn can be truncated by
[ST-0032](../stories/ST-0032-session-engine-lifecycle-and-contract.md)'s
inactivity auto-close, and whether escalated Conflicts opt into
[DEC-0039](../decisions/DEC-0039-conflict-escalation-operations.md)'s
timeout-to-default election.

**T11 — Agent.** Round 4 with recommendations on the two surfaced gaps:
(a) a turn actively streaming resets the inactivity clock — auto-close
never truncates mid-turn (recommended) vs. allowing auto-close to
truncate a partial turn; (b) Conflicts do not default into
[DEC-0039](../decisions/DEC-0039-conflict-escalation-operations.md)'s
timeout-to-default election — the general opt-in mechanism stays
available per-artifact, but no `CFL-` auto-resolves on a clock by
default (recommended) vs. defaulting Conflicts into the election.

**T12 — Sponsor.** Both (a) and (b) as recommended.

**T13 — Agent (synthesis).** Recorded
[DEC-0182](../decisions/DEC-0182-streaming-turn-resets-inactivity-clock.md)
and
[DEC-0183](../decisions/DEC-0183-conflicts-no-default-timeout-election.md);
added [ST-0032](../stories/ST-0032-session-engine-lifecycle-and-contract.md)
AC6 and
[ST-0036](../stories/ST-0036-conflict-detection-mediation-and-escalation.md)
AC6 to carry them. Re-ran `python3 tools/check_links.py` — clean (280
existing artifacts plus this bundle's 17 new/amended, 3 pre-existing
unrelated coverage warnings only).

## Decisions Produced

[DEC-0178](../decisions/DEC-0178-eval-harness-judge-model-family-independence.md),
[DEC-0179](../decisions/DEC-0179-eval-harness-seed-benchmark-corpus.md),
[DEC-0180](../decisions/DEC-0180-context-recipe-owns-anchoring-mitigation.md),
[DEC-0181](../decisions/DEC-0181-sp-0008-pack-format-expressiveness-spike.md),
[DEC-0182](../decisions/DEC-0182-streaming-turn-resets-inactivity-clock.md),
[DEC-0183](../decisions/DEC-0183-conflicts-no-default-timeout-election.md)

## Conflicts Raised

None.
