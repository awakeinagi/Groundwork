---
id: SES-0094
type: session
title: "EP-0014 epic refinement: Self-Governance & Dogfooding"
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-13
participant: awakeinagi@gmail.com
participant-role: stakeholder/approver
facilitator: Claude
transcript-fidelity: reconstructed
kind: full
intake: {origin: user, proposed-by: awakeinagi@gmail.com}
overview: >-
  Full refinement session for EP-0014 (Self-Governance &
  Dogfooding), opened at the stakeholder's direct instruction and
  closed with the epic approved. The required system-architect
  advisor consultation ran as the DEC-0293 dual-instance debate,
  converging on four findings that grounded two grilling rounds
  producing nine decisions (DEC-0504..DEC-0512), played back and
  confirmed in-session along with two new CONTEXT.md glossary
  entries. Gate prep: the consistency sweep and terms check on the
  nine decisions came back clean or non-actionable; a decision-
  recall audit (15 candidates each, dedicated Sonnet 5 judges) on
  EP-0014 and SP-0021 surfaced DEC-0037, DEC-0484, and DEC-0252 as
  accepted enrichments, plus a contract-gap finding — CMP-0004 and
  all 16 BG-0001-era components are unreconciled with the BG-0002
  epic set — parked as IDEA-0070 for a future reframing session. The
  required system-architect reviewer consultation converged with no
  disagreement: gate-ready, with a fix set the stakeholder applied
  in full. The stakeholder added DEC-0513 (correctness bias toward
  false positives). EP-0014 gated, then approved
  (DEC-0504..DEC-0513; approved-by awakeinagi@gmail.com, approved-on
  2026-07-13), which also ratifies SP-0021's draft-ahead charter
  (DEC-0505) as the next refinement target. IDEA-0070 remains the
  session's only parked idea. Session closed: the affected-artifact
  hypothesis from session open — EP-0014 as focus, EP-0015 and
  SP-0021 as satellites — is confirmed, and the full checker is
  clean (zero FAIL, 798 artifacts).
links:
  relates-to: [EP-0014, DEC-0504, DEC-0505, DEC-0506, DEC-0507, DEC-0508, DEC-0509, DEC-0510, DEC-0511, DEC-0512, SP-0021, IDEA-0070, DEC-0513]
---

# SES-0094: EP-0014 epic refinement: Self-Governance & Dogfooding

## Purpose

This session refines EP-0014 (Self-Governance & Dogfooding) from draft toward gate, per the standard epic-refinement playbook. EP-0014 was ready by refinement order: its only impactor EP-0010 is approved (SES-0091), it has no open conflicts, stale flags, change proposals, or ideas touching it, and it ranks second by impact fan-out among the remaining draft epics.

## Transcript

### T1 (stakeholder, verbatim proposal)

Let's refine EP-0014

### T2 (facilitator, restatement)

Restated the intent as running EP-0014's epic-refinement session and confirmed readiness from the librarian prep read: EP-0014 is a well-formed draft; its one impactor EP-0010 is approved, making it ready; the corpus checker is clean for it; no conflicts, staleness, untriaged change proposals, or ideas reference it. Noted EP-0011 ranks marginally higher by unblock fan-out but EP-0014 is a legitimate next target; proceeded with EP-0014 per the stakeholder's instruction.

### T3 (facilitator, advisor consultation)

Ran the required system-architect advisor consultation (DEC-0292) as the DEC-0293 dual-instance debate — one record-grounded instance, one best-practice-independent instance, one rebuttal round exchanged (a second was unnecessary; positions converged). Joint verdict: (1) the EP-0010/EP-0014 seam (checker machinery vs. rule definitions, DEC-0469) is sound, but EP-0014 must name the rule-family authoring contract — the shape, registration, and policy-configuration schema of a rule family — as a contract it consumes from EP-0010's rule-hosting component doc (DEC-0484, DEC-0486), since "rule family" currently has no defined deliverable shape. (2) The EP-0014/EP-0015 governance-configuration seam (DEC-0443) is sound and evidenced — the schema has at least five documented consumers beyond EP-0014's evaluator (ST-0013, ST-0022, CMP-0004, CMP-0001, EP-0013's bootstrap seeding per DEC-0263) — but the frontmatter impact edge between the epics is missing: the seam prose was added during SES-0089's recall audit without the DEC-0249 edge bookkeeping; the grounded instance rated this the draft's one blocking-severity gap and recommended a one-directional EP-0015 impacts EP-0014 edge. (3) On the bootstrap-circularity open risk, both instances converged on substance — the rules accepted before a change govern that change; the initial ruleset is a documented genesis exception; a small frozen meta-tier protects the amendment process — but disagreed on procedure: the grounded instance recommends recording the principle now and commissioning a spike for the mechanism (transition-window protocol, re-validation policy, genesis documentation, test plan), while the independent instance holds it is fully resolvable in-session; left to stakeholder arbitration. (4) The dogfooding loop is presumptively served by the existing IDEA-*/change-intake path (IDEA-0064 and IDEA-0065 arrived that way in SES-0089); building dedicated capture machinery now would fail the DEC-0335 no-arbitrary-builds guard; whether the existing path loses observations is a stakeholder grilling question. Withdrawn during rebuttal: re-splitting governance and dogfooding into two epics (settled by DEC-0463), a rule development/testing plugin contract (presupposes extension points DEC-0470 declined), an epic-level rule-ordering/conflict contract (EP-0010's machinery domain per DEC-0484), and an EP-0014 checker-observability contract (the EP-0010/EP-0016 seam per DEC-0486). Also flagged for later grilling rounds: gate-time vs. continuous enforcement of DEC-0442's "mechanically checked," governance-as-code file schema ownership, an explicit artifact-type-agnosticism note for governance rules, and explicit internal story separation per DEC-0463's implications.

### T4 (facilitator)

Presented grilling round 1 as preview cards, each question carrying a recommended answer: (1) bootstrap-circularity procedure — recommended recording the governing-version principle now and commissioning a spike for the mechanism, versus resolving fully in-session or deferring entirely; (2) the missing EP-0015 frontmatter edge — recommended a one-directional EP-0015-impacts-EP-0014 edge, versus mutual edges or prose only; (3) the rule-family authoring contract — recommended naming it as consumed from EP-0010's rule-hosting component doc with governance-rule stories sequenced after it, versus naming without sequencing or co-drafting it here; (4) the dogfooding mechanism — recommended formalizing the existing IDEA-*/change-intake path as the loop's contract, versus light tagging or dedicated capture machinery.

### T5 (stakeholder)

Accepted all four recommendations without amendment.

### T6 (facilitator)

Read back round 1's outcomes, then presented round 2: (5) enforcement posture — recommended stating check-time rule families per DEC-0475 with continuous enforcement deferred to story level, versus committing to continuous now or ruling it out permanently; (6) governance/ file ownership — recommended a written three-way split (schema EP-0015, policy content EP-0014, machinery EP-0010), versus moving file schemas under the Engine or leaving ownership unstated; (7) rule scope — recommended stating artifact-type-agnosticism with no direct edges to EP-0011 or EP-0013, versus drawing either edge; (8) story separation — recommended making DEC-0463's two-lane implication explicit in the body, versus leaving it to story derivation or allowing mixed stories.

### T7 (stakeholder)

Accepted the check-time posture, the artifact-type-agnosticism with no new edges, and the explicit two-lane separation. On the governance-file ownership question, selected no option and asked, verbatim: "Please elaborate, describing the 3-way split. I'm not following".

### T8 (facilitator)

Elaborated the ownership split with a concrete scenario — supporting "any 2 of 3 approvers" would involve adding a min-approvals field to gate-policies.yaml (a schema change, EP-0015's per DEC-0443), setting min-approvals to 2 in this project's file (policy content, EP-0014's per DEC-0484's tunable tables), and teaching the checker to count approvals (machinery, EP-0010's per DEC-0469) — clarifying that the note moves no ownership, it only writes down assignments that already follow from accepted decisions. Re-presented the ownership question with a rider on scheduling the bootstrap spike, recommending the spike run as the next refinement target after EP-0014's approval, before story derivation, versus normal queue order or just-in-time deferral.

### T9 (stakeholder)

Accepted the three-way split note and the spike-next scheduling.

### T10 (facilitator)

Played back the nine decisions distilled from the session in plain language for in-session confirmation, and proposed as a rider adding two CONTEXT.md glossary entries: transition rule and dogfooding loop.

### T11 (stakeholder)

Confirmed all nine decisions as played back and approved both glossary entries.

### T12 (facilitator)

Ran the post-distillation integrity machinery. The consistency sweep over DEC-0504..DEC-0512 returned hits only on approved artifacts citing the widely-referenced parent decisions the new records relate to; I reviewed each and found no new decision narrows or contradicts what any citer ratified. The terms check was clean. The decision-recall audit ran on EP-0014 and SP-0021 (15 candidates each), each judged by a dedicated Sonnet 5 judge.

### T13 (facilitator)

Audit outcomes: the SP-0021 judge surfaced DEC-0484 (the rule-family definition its placement question reasons against) and DEC-0252 (the sessions-only hard rule its mechanism must reconcile with) — both accepted and woven into the spike. The EP-0014 judge surfaced DEC-0037 (the foundational placement of governance configuration as versioned repo files) — accepted and cited in Domain Context — and a contract-gap note: CMP-0004, the approved BG-0001-era monolithic Governance & Gate Engine, is architecturally unreconciled with the BG-0002 three-way split, and investigation confirmed a systemic gap — all 16 BG-0001-era components lack any mapping to the new epic set, the separate future step DEC-0441 named. Also recorded: the write librarian, unprompted, self-assigned a second audit pass and applied a DEC-0154 enrichment to EP-0014's Domain Context (the role-to-review-path mapping lives in deployment configuration, not governance files); I verified the sentence against DEC-0154 post-hoc and found it faithful, and flagged the process deviation for stakeholder ratification.

### T14 (stakeholder)

Dispositions: parked the BG-0001-era reconciliation as IDEA-0070 for the future reframing session rather than expanding this epic's scope; confirmed the consistency-sweep no-amendments disposition.

### T15 (facilitator)

Ran the required system-architect reviewer consultation as the DEC-0293 dual-instance debate (record-grounded and best-practice-independent); the positions converged with no disagreement, so no rebuttal rounds were needed. Joint verdict: gate-ready, nothing blocking, with a fix set — an epic-level quality-goals statement (auditability, correctness bias, coverage completeness, modifiability), an execution-risk line for EP-0010 contract-shape drift, provider/consumer direction on the rule-family and dogfooding interface items, repair of a stale no-outgoing-edges sentence this session's own EP-0015 edit left behind, a placement caveat in SP-0021, and one clarity rewrite in Domain Context. The correctness bias was posed as a fresh decision; DEC-0154's ratification was requested.

### T16 (stakeholder)

Applied the full fix set; chose the over-report bias — governance rules prefer false positives over false negatives (recorded as DEC-0513); ratified the DEC-0154 enrichment.

### T17 (facilitator)

Actual outcomes of the pre-gate batch: DEC-0513 (Governance rules prefer false positives over false negatives) was created accepted, derives-from this session, relates-to DEC-0509 and DEC-0442. EP-0014's Why (Goal Alignment) now carries the quality-goals paragraph citing DEC-0513; its Interfaces & Contracts to Define section names provider/consumer direction on the governance-rule-family and dogfooding-loop items; its Risks & Open Questions section carries the EP-0010 contract-shape execution risk; its Domain Context rewrite lands as specified. EP-0015's Domain Context now states the one outgoing EP-0014 impact edge in place of the stale no-outgoing-edges sentence; its overview already stated the edge accurately and needed no change. SP-0021 carries the placement caveat at the end of the Question section. None of the fix-set edits were refused. EP-0014's overview was refreshed (242 words) to reflect the quality goals, the resolved bootstrap-circularity risk, and the new interfaces direction; EP-0014 is now set to gated. Consistency sweep on DEC-0513 returned two REVIEW hits, both on EP-0014 itself citing the same DEC-0509/DEC-0442 parents DEC-0513 relates to — reviewed, non-actionable, since EP-0014's own edits already incorporate the new decision's content. The terms check on DEC-0513 was clean (zero hits). The full checker now reports zero FAIL across 798 artifacts — the SES-0094/IDEA-0070 gap has cleared now that this transcript references IDEA-0070 — with only the same 19 pre-existing, unrelated approved-story coverage-gap WARNs seen in earlier sessions.

### T18 (stakeholder)

Approved EP-0014 as gated — recording approved-by awakeinagi@gmail.com, approved-on 2026-07-13 — which also ratifies SP-0021's draft-ahead charter per DEC-0505. On the DEC-0261 closing ideas check: no further ideas; IDEA-0070 stands as the session's only capture.

### T19 (facilitator)

EP-0014's status walk landed as applied: gated -> approved, with approved-by awakeinagi@gmail.com and approved-on 2026-07-13 stamped by the write API. The full checker reports zero FAIL across 798 artifacts, graph sound, with only the same 19 pre-existing, unrelated approved-story coverage-gap WARNs seen earlier in this session. Session close: EP-0014 refined from draft to approved in this session via DEC-0504..DEC-0513, SP-0021 chartered draft-ahead and ratified with the epic as the next refinement target, IDEA-0070 parked, and the EP-0015 edge and repairs applied; the affected-artifact hypothesis from session open — EP-0014 as focus, EP-0015 and SP-0021 as satellites — is confirmed.

## Decisions Produced

- DEC-0504 — Method transition principle: pre-change rules govern rule changes.
- DEC-0505 — Bootstrap-circularity spike (SP-0021) commissioned as draft-ahead work.
- DEC-0506 — One-directional EP-0015→EP-0014 impact edge on the governance-configuration seam.
- DEC-0507 — Rule-family authoring contract consumed from EP-0010; governance-rule stories sequence after it.
- DEC-0508 — Dogfooding-loop contract: the existing intake path, no dedicated machinery.
- DEC-0509 — Check-time enforcement posture for governance rules.
- DEC-0510 — Three-way ownership split for the governance/ configuration files.
- DEC-0511 — Governance rules are artifact-type-agnostic; no direct edges to EP-0011 or EP-0013.
- DEC-0512 — Two-lane story separation for EP-0014's derived work.
- DEC-0513 — Governance rules prefer false positives over false negatives when uncertain.

## Conflicts Raised

None raised in this session so far.
