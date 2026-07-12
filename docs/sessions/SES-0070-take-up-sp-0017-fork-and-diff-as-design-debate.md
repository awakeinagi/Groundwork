---
id: SES-0070
type: session
title: "Take up SP-0017: fork-and-diff as design-debate evidence"
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-11
participant: awakeinagi@gmail.com
participant-role: operator/stakeholder
facilitator: Claude (Fable 5) via Claude Code
transcript-fidelity: reconstructed
overview: >-
  This session takes up SP-0017 (fork-and-diff as design-debate
  evidence): forking two alternative designs for an already-decided
  design question, running both through SP-0014's surviving
  ActiveGraph rulebase via fork-and-diff, and comparing the
  resulting structural findings-diff against a recorded dual-
  instance architect debate (DEC-0293 protocol) that actually
  decided that question -- descriptive, no kill bar (DEC-0355).
  SES-0056/DEC-0307 (the component grouping principle) is the
  leading benchmark candidate: a decided design question with a
  citable dual-instance debate record to diff against. Executes in
  parallel with the concurrent SP-0016 session, per stakeholder
  sanction. SP-0017 was previously queued last pending SP-0014's
  rulebase; SP-0014 completed and was approved at SES-0069
  (2026-07-11), clearing that dependency. The session ran the four-
  round fork-and-diff plus ActiveGraph capability assessment,
  producing five proposed decisions (DEC-0369..0373); full adoption
  was deferred to the DEC-0337 cross-spike survey, and the session
  closed with SP-0017 approved.
links:
  relates-to: [SP-0017, DEC-0369, DEC-0370, DEC-0371, DEC-0372, DEC-0373]
---

# SES-0070: Take up SP-0017: fork-and-diff as design-debate evidence

## Purpose

Take up and execute spike SP-0017: determine whether running two alternative designs for an already-decided design question through SP-0014's ActiveGraph rulebase, via fork-and-diff, produces decision-grade evidence when compared against the recorded human dual-instance system-architect debate (DEC-0293 protocol) that actually decided that question. Leading benchmark: SES-0056 turns 11-13 -> DEC-0307 (component grouping principle, bounded-context vs vertical-slice), the cleanest single-question instance with a stakeholder-adjudicated divergence between the two architect instances. Reuse SP-0014's surviving throwaway rulebase as input; all build artifacts stay in scratchpad and are never committed (DEC-0351). Deliverable: findings on the correspondence between the automated findings-diff and the human debate, plus any resulting decisions about whether/how fork-and-diff can serve as design-debate evidence in Groundwork.

## Transcript

Turn 1 -- Facilitator (restate & align): "Taking up SP-0017 as its own spike session (Mode 3). The spike asks whether running two alternative designs for an already-decided design question through SP-0014's rulebase, via ActiveGraph fork-and-diff, produces decision-grade evidence when measured against the human dual-instance system-architect debate (DEC-0293 protocol) that actually decided that question. Timebox: 1 session. Reuses SP-0014's surviving throwaway rulebase as input. No kill bar -- evaluation is a diff-vs-debate comparison."

Turn 2 -- Facilitator (dependency disposition): "SP-0017's 'Why It Blocks' section states it was 'explicitly queued last since it depends on SP-0014's rulebase.' That rationale is now satisfied: SP-0014 completed and was approved at SES-0069 (2026-07-11). The stakeholder has sanctioned parallel execution of this session alongside the concurrent SP-0016 session. Recording this disposition explicitly at take-up: the queued-last blocker is cleared; SP-0017 proceeds now."

Turn 3 -- Stakeholder (operator, awakeinagi@gmail.com): "[Belongs at record opening -- appended out of order per append-only rule, DEC-0255.] Stakeholder's verbatim engagement to take up SP-0017: 'Let's begin.' This was the operator's direct assent, given in response to the facilitator's readiness summary that framed the take-up of SP-0017 (fork-and-diff as design-debate evidence). The substantive take-up mandate -- proceed with SP-0017 as its own spike session, in parallel with the concurrent SP-0016 session -- was relayed to the facilitator through its spawning charter as the stakeholder's standing sanction; this turn records the operator's own words authorizing the session to begin."

Turn 4 -- Facilitator (Round 1 grilling): "Posed four Round-1 questions: (1) confirm benchmark SES-0056 T11-13 / DEC-0307; (2) adopt the definition of 'decision-grade evidence' as a graded verdict (strong/partial/weak) against which the findings-diff is scored; (3) run the required system-architect consultation or grant a session-specific waiver; (4) confirm the experiment unit is two forked alternatives to the one decided question."

Turn 5 -- Stakeholder: "(1) DEC-0307 confirmed as the starting benchmark; expand later toward mapping ActiveGraph's full capability range if the first run succeeds. (2) Graded-verdict definition adopted as a start; reassess after the first run. (3) No system-architect consultation for this session. (4) Confirmed: start with two forked alternatives to the one decided question, consider something broader only if this succeeds."

Turn 6 -- Facilitator (governance -- architect-consultation waiver): "Recording the stakeholder's T5(3) instruction as this session's explicit, session-specific waiver of the required system-architect consultation at spike sessions. This is distinct from and does not rely on the one-off waiver granted at SES-0069; it is SP-0017's own waiver."

Turn 7 -- Facilitator (benchmark correction): "Correcting an earlier mischaracterization: DEC-0307's component-grouping question was NOT a stakeholder-adjudicated divergence -- both architect instances at SES-0056 T12 CONVERGED and unanimously rejected vertical-slice regrouping (no rebuttal round needed). The genuine inter-instance divergence at SES-0056 was a separate question -- where end-to-end acceptance criteria live -- resolved in DEC-0302 (slices as first-class artifacts), which is an artifact-type choice the SP-0014 structural rulebase cannot see. DEC-0307 remains the benchmark, reframed as a decided question with two concrete rival STRUCTURAL alternatives (bounded-context vs vertical-slice) and an explicit recorded rejection rationale. The spike's sharpened question: what fraction of a human design-rejection rationale can an automated structural fork-and-diff independently surface? Of the five recorded human grounds for rejecting vertical-slice, only two are structural and visible to the rulebase -- seam duplication/blurred seam governance (rules R16/R21/R4) and 'flows span 4-6 components regardless of grouping' (R4/R11/R12/R22); the other three (common-closure violation, bounded-context cohesion, re-gating cost) are semantic/economic and invisible. Honest expected outcome: partial correspondence."

Turn 8 -- Facilitator (design + test plan presented): "Presented the method and test plan for approval. Method: adapt SP-0014's throwaway projector to emit the element-grain graph (elements, contract items, element-to-element USES edges, stories, decisions) as events into a SQLite-backed ActiveGraph runtime (the shared substrate); fork at the post-substrate event via Runtime.fork into fork-BC (grouping = the current 16-component inventory) and fork-VS (grouping = a vertical-slice cut faithful to the rejected alternative, duplicating shared seams); fire SP-0014's 24-rule behavior in each fork; compute the findings set-difference (and capture Runtime.diff's event-level view); map each diff entry to the five human rationale threads and grade correspondence. Test plan (validates the method itself, DEC-0345): T1 substrate parity (both forks start from identical element-grain state); T2 anchor to SP-0014 (fork-BC reproduces SP-0014's recorded findings for the boundary-sensitive rules); T3 fork isolation (mutating fork-VS leaves fork-BC unchanged); T4 diff confinement (findings-diff lands only in boundary-sensitive rules R4/R10/R11/R12/R16/R21/R22; any grouping-insensitive rule differing signals a state-leak bug); T5 determinism (each fork reproducible); T6 non-triviality (diff non-empty, distinguishing 'no structural signal found' from 'harness broken'). Two scope options offered: (A) single-flow vertical slice using the 'gate an artifact' flow (recommended, tractable, low-bias); (B) whole-corpus regroup. Build is throwaway, scratchpad-only, never committed (DEC-0351)."

Turn 9 -- Stakeholder: "(1) Scope A -- start with the single-flow slice. (2) Method and test plan approved; proceed to build."

Turn 10 -- Facilitator (governance constraints noted): "Two operator constraints registered for this and future sessions: (a) any Claude Code agent/subagent frontmatter hooks must be confined to a dedicated test agent, never added to shared/production agents; (b) creating a new agent definition requires a Claude Code restart before it is usable. Neither affects SP-0017: the build creates no new agent definition, and the only subagents used (artifact-librarian; a Sonnet decision-recall judge spawned via model override on an existing agent type) require no restart."

Turn 11 -- Stakeholder + Facilitator (disposition): "Facilitator presented the fork-and-diff results against the DEC-0307 benchmark: all six method-tests pass; findings-diff (BC vs a 'gate an artifact' vertical slice) surfaced R1 dependency cycles, R21 mutual coupling, R16 seam-graduation shifts, and R10 story-traceability breaks -- mapping to three of five human rejection grounds plus introduced cycles, blind to the two semantic grounds; verdict 'strong on direction, partial on rationale.' Stakeholder disposition: record the three findings as PRELIMINARY (proposed) decisions [the three DECs above], and EXTEND the spike beyond its original single-benchmark 1-session timebox into a broader assessment of ActiveGraph's full capability range in Groundwork -- subsequent test rounds to follow. This extension is stakeholder-directed and recorded here as a deliberate scope expansion of SP-0017."

Turn 12 -- Facilitator (mechanical repair, IDEA-0041): "The earlier sharpening edit-section batch introduced duplicate empty phantom headings in DEC-0369/0370/0371 (the gw-write edit-section phantom-heading defect). The stakeholder explicitly sanctioned a one-off content-preserving mechanical dedup (files untracked, so no git-checkout baseline; a clean single-pass body rewrite was used, not the buggy span path). Headings collapsed to one each, content preserved, and the two previously-stopped DEC-0355 Implications lines (DEC-0369, DEC-0371) added. These three are new instances of IDEA-0041 (now: SP-0015 shipped with it, SP-0016 caught-and-redone, DEC-0369/0370/0371 caught pre-commit) -- folded into IDEA-0041's evidence; the tooling fix is routed to the dedicated IDEA-0041 fix session."

Turn 13 -- Facilitator (findings): "SP-0017 executed four rounds (fork-and-diff on DEC-0307 grouping and DEC-0134/0135 graduation; provenance + deterministic replay; packs/schema/gates). Results recorded in SP-0017 Findings; five preliminary decisions DEC-0369..0373 produced. Verdict: ActiveGraph is a strong analysis/provenance substrate, a viable design-evaluation aid, and a partial write/gate substrate."

Turn 14 -- Facilitator (consistency sweep dispositions, DEC-0157/0158): "The distillation sweep flagged four ratified citers for review — CMP-0004/CMP-0008/CMP-0015 (via DEC-0373 relates-to DEC-0136) and BG-0002 (via DEC-0373 relates-to DEC-0312). Disposition: DEC-0373 references DEC-0136 and DEC-0312 comparatively (a capability finding measured against those Groundwork mechanisms), neither narrowing nor superseding them; the citers are unaffected. No action."

Turn 15 -- Facilitator (decision-recall audit dispositions): "A Sonnet-5 recall-audit judge returned findings on all five decisions. Facilitator accepted the link additions (with reciprocals): DEC-0135 + SP-0014 + DEC-0354 to DEC-0369; DEC-0345 + SP-0014 + DEC-0354 to DEC-0370; DEC-0307 + SP-0014 + DEC-0136 + DEC-0354 to DEC-0371; DEC-0138 + DEC-0117 + DEC-0146 + DEC-0354 to DEC-0372; DEC-0033 + DEC-0029 + DEC-0315 + DEC-0354 to DEC-0373 — plus Implications framing addenda (DEC-0355 no-kill-bar on DEC-0369/0371; DEC-0368 caveat on DEC-0372; DEC-0351 routing on DEC-0373). Rejected DEC-0036 as a near-miss (redundant with DEC-0315). All applied in this write window."

Turn 16 -- Stakeholder (dispositions + spike gate): "Stakeholder confirmed: keep all five decisions proposed; keep the rounds-3-4 capability-assessment findings within SP-0017; defer the full-adoption decision to a post-SP-0016 cross-spike DEC-0337 adoption survey (per SP-0015's precedent of ratifying findings while deferring adoption, reinforced by SP-0016's DEC-0374/0375 convergence). The system-architect consultation waived for this spike (T6) is required at that adoption survey. Stakeholder approved the SP-0017 spike gate and this session close; SP-0017 set approved."

Turn 17 -- Facilitator (close): "SES-0070 closed. SP-0017 approved with five proposed resulting decisions; full adoption deferred; all build code throwaway and archived off-corpus (DEC-0351). Follow-ups noted: the DEC-0337 cross-spike adoption survey; the IDEA-0041 edit-section heading-bug fix (three instances now: SP-0015 shipped, SP-0016 and DEC-0369/0370/0371 caught pre-commit) and repair of the shipped SP-0015 instance."

Turn 18 -- Facilitator (post-close enrichment, DEC-0248, 2026-07-12): "Operator-sanctioned repair of an incomplete close-out record, applied by direct edit outside the write API (the API's closed-session gate correctly refused edit-section; the operator explicitly sanctioned the direct route and the commit). Repairs: Decisions Produced filled with DEC-0369..0373 (was 'TBD.'); Conflicts Raised set to 'None.' (was 'TBD.'); a stray leftover 'TBD.' placeholder removed from the top of the Transcript; frontmatter completed with participant, participant-role, facilitator, and transcript-fidelity per sibling-session convention. No transcript turn content was altered. Root cause — the session-close step verified neither required-section completion nor frontmatter completeness before set-status closed — is folded into IDEA-0041's fix scope per the operator, alongside a fourth shipped instance of the phantom-heading defect found in SES-0069's Decisions Produced heading during this repair."

## Decisions Produced

DEC-0369 (fork-and-diff yields directionally-reliable but rationale-partial structural evidence for grouping decisions), DEC-0370 (the ActiveGraph fork-and-diff mechanism is viable for design-alternative evaluation), DEC-0371 (structural rulebases have a semantic blind spot bounding automated design evidence), DEC-0372 (ActiveGraph event-log provenance and deterministic replay), and DEC-0373 (ActiveGraph typed schemas with behavior-mediated gate enforcement) -- recorded proposed at T11/T13, sharpened and link-audited at T15, and held proposed at T16 with full adoption deferred to the post-SP-0016 cross-spike DEC-0337 adoption survey.

## Conflicts Raised

None.
