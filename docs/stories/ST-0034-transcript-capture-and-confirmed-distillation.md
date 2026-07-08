---
id: ST-0034
type: story
title: Transcript capture and confirmed distillation
status: gated
owner: ds-lead
created: 2026-07-08
links:
  derives-from: [EP-0002]
  satisfies: [BG-0001]
  depends-on: [ST-0032]
  impacts: [ST-0036, ST-0037, ST-0039, ST-0041]
  impacted-by: [ST-0032]
cites: [DEC-0015, DEC-0051, DEC-0052]
---

# ST-0034: Transcript Capture and Confirmed Distillation

## Summary

The verbatim record every Decision traces back to, and the confirmation
loop that turns it into ratified provenance: raw, turn-numbered,
append-only transcript capture, plain-language playback of proposed
decisions at checkpoints, and re-runnable distillation from raw text
when drift or hallucination is suspected.

## Acceptance Criteria

1. The transcript stored in the SES artifact is the raw message log —
   verbatim, turn-numbered, append-only — never an agent summary; any
   condensed view is a derived layer that does not replace it
   (per [DEC-0052](../decisions/DEC-0052-raw-transcripts-regenerable-distillation.md)).
2. At natural checkpoints (topic close, session end) the agent plays back
   proposed Decisions in plain language; the participant confirms or
   corrects while present, and the confirmation exchange itself lands in
   the transcript
   (per [DEC-0051](../decisions/DEC-0051-in-session-decision-confirmation.md)).
3. Only confirmed decisions commit to the item branch as `accepted`, with
   `source-span` citing the turns that support them; the item's PR gate
   remains final ratification
   (per [DEC-0051](../decisions/DEC-0051-in-session-decision-confirmation.md)).
4. Distillation is a re-runnable function of the raw transcript: given a
   SES artifact, re-running it reproduces the same proposed decisions
   deterministically enough to diff against what was accepted
   (per [DEC-0052](../decisions/DEC-0052-raw-transcripts-regenerable-distillation.md),
   [DEC-0015](../decisions/DEC-0015-transcript-decision-citation-chain.md)).
5. Contracts, requirements, and acceptance criteria produced anywhere in
   the system cite Decision IDs, not raw transcript spans directly —
   implementation agents crawl to Decisions and rarely need raw
   transcripts
   (per [DEC-0015](../decisions/DEC-0015-transcript-decision-citation-chain.md)).

## Component Impact

None yet — a Component Doc for this epic's bounded context is stubbed once the first story here refines toward it.

## Out of Scope

The eval harness's faithfulness judging and drift-audit re-runs of this
machinery ([ST-0041](ST-0041-evaluation-harness.md)); how conflicting
distillations feed the mediation flow
([ST-0036](ST-0036-conflict-detection-mediation-and-escalation.md)); pack
selection of which questions produce which transcript content
([ST-0033](ST-0033-strategy-pack-format-and-plugin-loading.md)).

## Notes for Implementers

Distillation re-runs must be deterministic enough to diff, not
byte-identical — the eval harness's drift audits
([ST-0041](ST-0041-evaluation-harness.md)) depend on a meaningful diff
signal, not exact reproduction.
