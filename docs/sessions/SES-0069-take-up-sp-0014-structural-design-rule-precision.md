---
id: SES-0069
type: session
title: "Take up SP-0014: structural design-rule precision spike"
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-11
participant: awakeinagi@gmail.com
participant-role: operator/stakeholder
facilitator: Claude (Fable 5) via Claude Code
transcript-fidelity: reconstructed
overview: >-
  Closed. Session took up SP-0014 (structural design-rule precision
  spike) under DEC-0365's unblocking, per SES-0064's spike program.
  Ratified four stale-proposed program decisions DEC-0354..DEC-0357
  at T5. The stakeholder waived the DEC-0292 system-architect
  consultation as a one-off (T6/T7). Approved a 12-rule design (T8),
  then the stakeholder directed expansion with no upper limit (T9);
  the facilitator built a 24-rule structural rulebase (T10),
  approved at T11. The throwaway build fired cleanly against
  SP-0013's projection, all five calibration instruments passing,
  and produced 102 findings across 15 of 24 rules (T12). The
  stakeholder disposed all 102 findings -- 33 real/change-worthy, 9
  debatable, 60 noise -- and affirmed the executable-design-
  knowledge premise for decision-compiled rules specifically, versus
  ActiveGraph as a substrate (T13-T16). Captured six consolidated
  follow-up Ideas, IDEA-0035 through IDEA-0040, reviewed with the
  stakeholder at the gate summary with none further offered
  (T17-T18). A decision-recall audit at T19 produced three
  provenance enrichments, near-misses recorded. Gate prep checklist
  completed and SP-0014 set gated at T20. The stakeholder approved
  the gate at T21; SP-0014 set approved (awakeinagi@gmail.com,
  2026-07-11), DEC-0367 and DEC-0368 accepted, and the session
  closed with the T22 summary. Evidence files remain in the session
  scratchpad per the stakeholder's T17 instruction.
links:
  relates-to: [SP-0014, DEC-0354, DEC-0355, DEC-0359, DEC-0360, DEC-0356, DEC-0357, IDEA-0035, IDEA-0036, IDEA-0037, IDEA-0038, IDEA-0039, IDEA-0040]
---

## Purpose

Take-up session for SP-0014 (structural design-rule precision over the projected corpus), unblocked by DEC-0365 after SES-0066's corpus-wide Uses: backfill. The session opened with a ratification review of decisions the spike cites or rests on: initial triage flagged four decisions as proposed -- DEC-0354, DEC-0355, DEC-0359, DEC-0360 -- but on review DEC-0359 and DEC-0360 turned out already accepted (the earlier status trace misreported them). The corpus's actual four proposed decisions were DEC-0354 (five-spike ActiveGraph program), DEC-0355 (no kill-bar evaluation), DEC-0356 (spikes evaluate ActiveGraph only; DEC-0337 option survey deferred until after the spikes report), and DEC-0357 (projection spike proceeds fully separate from SP-0007). All four were ratified proposed -> accepted at T5. The session proceeds through the required system-architect advisor consultation, DEC-0335/DEC-0345 design-and-test-plan approval of the concrete rulebase, throwaway build and firing against SP-0013's projection, stakeholder disposition of every finding, and recording of Findings and Resulting Decisions on SP-0014.

## Transcript

T1 -- Stakeholder (verbatim): "Take up SP-0014"

T2 -- Facilitator: Restated the take-up after a corpus read: SP-0014 is unblocked (DEC-0358's precondition satisfied per DEC-0365; no open conflicts, no stale ancestors, parents BG-0002/EP-0009/SP-0013 all approved). Laid out the session plan: open the session record, set SP-0014 in-refinement, run the system-architect advisor consultation, present the concrete ~12-rule rulebase design and test plan for approval before any build (DEC-0335, DEC-0345), build and fire the throwaway rulebase against SP-0013's projected graph, take stakeholder dispositions on every finding (real / noise / change-worthy, no kill bar per DEC-0355), then record Findings and Resulting Decisions. Flagged two items: (a) the backfilled Uses: edges are 100% (interface) / zero (implementation), so the build-order/serialization rules will be vacuously satisfied -- acknowledged, non-blocking; (b) four decisions the spike rests on remain in proposed status (DEC-0354, DEC-0355, DEC-0359, DEC-0360) -- recommended ratifying them at the top of this session.

T3 -- Stakeholder (verbatim): "Yes, open the session. Present an overview of each DEC and let's get those closed."

T4 -- Facilitator: Presented the ratification picture with a correction: DEC-0359 and DEC-0360 were already accepted (the earlier status trace misreported them); the corpus's four proposed decisions are DEC-0354, DEC-0355, DEC-0356, DEC-0357, all distilled from SES-0064 stakeholder option selections whose statuses were never flipped at close. Presented each with its verbatim Decision text, source span, and ratified-citer blast radius: DEC-0354 (five-spike ActiveGraph program under EP-0009), DEC-0355 (exploratory program, no kill-bar thresholds; governs how this session treats SP-0014's findings), DEC-0356 (spikes evaluate ActiveGraph only; DEC-0337 option survey deferred until after the spikes report and required before any adoption decision), DEC-0357 (projection spike proceeded fully separate from SP-0007, parse-scope overlap deliberately accepted). Recommended accepting all four.

T5 -- Stakeholder (verbatim): "Accept all four"

T6 -- Stakeholder (verbatim): "We don't need the system architect for this spike. This is an exploratory experiment."

T7 -- Facilitator: Surfaced the tension with DEC-0292, which makes the system-architect consultation required at spike sessions, and recorded the stakeholder's instruction as a one-off waiver for this session on the reasoning that SES-0069 is execution of an already-designed spike -- the architect debates for the program design ran at SES-0064/SES-0065 (DEC-0355 carries the reviewer-debate residual), so the requirement's intent was served upstream. Offered to distill a standing exemption for exploratory-spike execution sessions as a new decision narrowing DEC-0292; the stakeholder did not take it up. The waiver stands as one-off, session-scoped.

T8 -- Facilitator: Presented the concrete rulebase design and test plan per DEC-0335/DEC-0345: 12 rules -- six compiled from the system-architecture-bp corpus (dependency cycles, stability direction, orphaned interfaces, cross-boundary implementation coupling, fan-out hub, speculative contract items; each with honest grounding-strength tags, since the corpus grounds these via practitioner sources rather than Martin's named ADP/SDP/ISP principles) and six from Groundwork's accepted rule-type decisions (item citation completeness; superseded-decision citations; mandatory-contract-kind completeness per DEC-0088; Implements coverage and bidirectional agreement per DEC-0092/DEC-0094; Uses/depends-on projection equality per DEC-0309 as a null-calibration rule; build-order tier derivation per DEC-0299/DEC-0301/DEC-0309). Execution plan: throwaway venv (activegraph 1.9.0 per DEC-0354) in the session scratchpad, projection re-established per SP-0013's recorded Method with parser additions (Uses: edges, decision statuses, story Component Impact), everything scratchpad-confined per DEC-0351; the design's approval re-confirms the SP-0013-style read-only direct-parse executor sanction for this spike. Test plan: round-trip counts against SP-0013's recorded baselines (16 CMPs, 53 elements, 346 items, 581 CITES, 65 IMPLEMENTS, 26 DEPENDS_ON) and DEC-0359's (71 Uses edges, 20 Uses: none); calibration rules with known expected output (projection-equality must fire zero; item-citation completeness must fire exactly SP-0013's 10 recorded provenance edge cases); deviations halt execution before findings are cataloged. Two rules vacuous against current data (implementation-coupling, build-order) retained deliberately per DEC-0365's acknowledgment.

T9 -- Stakeholder (verbatim): "Add any structural rules that seem worthy for test, as many as you like with no upper limit"

T10 -- Facilitator: Expanded the rulebase to 24 rules from the same two curated sources. Groundwork additions: schema resolution (DEC-0089, unenforced today), test-double ownership plus fake-promotion-candidate detection (DEC-0306; should rediscover DEC-0359's three flagged fakes), staleness propagation (DEC-0096), seam-graduation candidates (the groundwork-system graduation rule), bundle closure with range expansion (DEC-0303; expected to fire on the CMP-0001/CMP-0004 range dispute IDEA-0026 records), deferred-only elements (checker rule 13 mirror), uncovered approved stories (DEC-0092/DEC-0094 family, must reproduce the 19 known checker coverage warnings). Best-practice additions: fan-in hub (weak grounding, tagged), mutual component coupling (partial grounding -- DEC-0196/DEC-0199's mutual-coupling seam smell applied to structural edges by analogy, tagged), cross-boundary data reach-in (Shopify/Azure exclusive data ownership; vacuous against current data), pass-through service degree-2 proxy (Azure N-tier probe, proxy-grade), happy-path-only contracts (Fowler & Lewis/Zalando, heuristic token scan). Excluded with recorded reasons: ISP/fat-interface and god-component (ungrounded in the corpus), gateway/storage-shape/org-chart rules (require node types a solo docs corpus lacks), networked-monolith (collapses into the implementation-cycle checks), artifact-tree checker mirrors DEC-0242/DEC-0246/DEC-0249 (out of the CMP-projection scope, already enforced). Final shape: 24 rules -- 14 discovery, 5 calibration (expected outputs: 10, 0, ⊇1, ⊇3, ≈19), 3 vacuous-by-data, 2 weak/proxy probes. Noted SP-0014's Method says "approximately 12" and that the stakeholder-directed expansion would be recorded as this session's amendment to the in-refinement spike.

T11 -- Stakeholder (verbatim): "Yes, please continue"

T12 -- Facilitator: Reported build completion and presented the findings catalog: round-trip validation green after two parser fixes (wrapped Uses: continuations; item-body bleed -- recovering SP-0013's bullet-plus-indented-continuation convention to hit 581 CITES exactly) and two baseline revisions (DEPENDS_ON 26->30 explained by DEC-0359's reconciliation; typed Uses edges 72 in the corpus against DEC-0359's recorded 71 -- an unexplained record discrepancy flagged as a change-worthy meta-finding). All five calibration gates passed: R7 exactly SP-0013's 10 provenance edge cases; R19 exactly the 19 known coverage warnings; R14 all three DEC-0359 fake candidates after an in-run fix (fakes appear in prose form, not CamelCase); R11 fired once on CMP-0006 -- the compiled rule omitted checker rule 20's element-less-doc carve-out, kept as compilation-fidelity noise; R17 zero per its execution-time-revised expectation (the IDEA-0026 range dispute is invisible at edge grain since both written edges target the undisputed portion). Presented all 102 findings from 15 of 24 rules grouped with recommended dispositions: change-worthy -- R8's four superseded-DEC-0014 citations (strongest discovery), R16's three ungraduated multi-consumer elements, R24's six happy-path-only services, R13's schema-token review list; real-previously-recorded -- R7's 10, R19's 19, R14's three candidates; noise -- R6's 24 (bare-element edge-convention mismatch), most of R3 (boundary roles/protocol indirection), fan hubs, R11, R12, R14's two cross-reference hits. Asked specifically about the four zero-consumer workflow services (WorktreeManager, GovernanceInit, StalenessSweepService, ReaffirmationService).

T13 -- Stakeholder (verbatim): "What is the full path to the findings?"

T14 -- Facilitator: Gave the scratchpad paths (findings.md, findings.json alongside the throwaway build), noted the scratchpad is session-scoped and volatile, and that the durable home for the catalog is SP-0014's Findings section once dispositions land.

T15 -- Stakeholder (verbatim): "What do these results reveal about the feasibility of using activegraph for this project? What benefits will it bring?"

T16 -- Facilitator: Assessed that the results say much about the executable-design-knowledge premise and little about ActiveGraph specifically. The DEC-0354 premise survived: roughly two dozen real or change-worthy findings that twenty checker rules and the gate process had not caught, the graduation misses showing mechanical enforcement catching what process discipline leaked. Precision proved strongly source-dependent: DEC-compiled rules near-perfect, prose-compiled rules noisy -- an early corroboration of the prose-to-rule fidelity concern. ActiveGraph itself served only as a passive store; nothing exercised its distinctive reactive/replay/fork machinery, so everything done could equally have been done by extending check_links.py -- the differential evidence belongs to SP-0016 (hook-loop economics) and SP-0017 (fork-and-diff). Conditional benefits if the DEC-0356-deferred survey favors it: continuous contract-grain enforcement of rule-type decisions, an element/item-grain query surface, provenance-carrying findings; the thin owned implementation remains a real competitor. Data caveat: with 100% interface edges the build-order/serialization/coupling rules remain untested, unmeasured rather than confirmed.

T17 -- Stakeholder (verbatim): "This was a great summary. Please be sure to include all of this in the Spike's write up. Let's also leave the findings files in place after we close out this Spike. I have an IDEA to start maintaining the results of Spikes.

Let's create follow up IDEAs to fix all of the issues in the corpus and architecture revealed by this Spike; try to consolidate similar problems into as few IDEAs as possible. For the problems that were debatable, let's grill them in a follow up session and/or future spikes."

T18 -- Facilitator: Recorded the disposition outcome -- recommendations accepted wholesale with debatable findings routed to a follow-up architecture-review session -- and captured six consolidated Ideas: IDEA-0035 (SP-0014 record-integrity repairs: superseded cites, uncited items, DEC-0359 count), IDEA-0036 (resolve SP-0014's eight unresolved schema tokens per DEC-0089), IDEA-0037 (complete error contracts for six happy-path-only services), IDEA-0038 (promote the three flagged test doubles to owned elements per DEC-0306), IDEA-0039 (architecture-review session over SP-0014's debatable structural findings), IDEA-0040 (maintain spike results durably). Noted R19's nineteen uncovered stories stay checker-tracked pipeline work rather than minting an Idea, and that the findings files remain in the session scratchpad per the stakeholder's instruction, with durable retention being IDEA-0040's open question.

**T19 — Facilitator:** Ran the required decision-recall audit at gate prep: 15 candidates, single Sonnet 5 judge. Three findings, all accepted and addressed by provenance enrichment in the same edit: DEC-0308 linked at the R8 disposition (it is the record that superseded DEC-0014 — the repair in IDEA-0035 reconciles against it); DEC-0234 linked at the R16 disposition and IDEA-0039 (GovernanceConfig already graduated once to CMP-0016, making its new flag a second-order graduation question — also recorded as the judge's contract-gap observation that nothing previously connected the new finding back to DEC-0234's resolution); DEC-0126 linked as decomposition provenance for the CMP-0001 element findings. Judge near-misses (DEC-0232, DEC-0162, DEC-0177, DEC-0366) rejected as precedent-not-provenance, recorded here for completeness. Consistency checks on DEC-0367/DEC-0368 returned clean terms and only routine sweep review hints, reviewed with no inconsistencies found.

T20 — Facilitator: Gate prep checklist completed and SP-0014 set gated: (1) overview faithfulness — rewritten at the write-up step to reflect the executed spike, re-checked after the recall-audit enrichments (no meaning change, left as-is); (2) system-architect reviewer consultation — covered by the stakeholder's one-off waiver recorded at T6/T7; (3) decision-recall audit — run at T19, three findings addressed by provenance enrichment, near-misses recorded; (4) consistency checks on DEC-0367/DEC-0368 — clean; (5) full checker — 586 artifacts, graph sound, only the 19 pre-existing R19-known coverage warnings. Presented SP-0014 for approval together with confirmation of proposed DEC-0367 and DEC-0368.

T21 — Stakeholder (verbatim): "Approve the gate and close out the session"

T22 — Facilitator: Recorded the approval: SP-0014 approved (awakeinagi@gmail.com, 2026-07-11); DEC-0367 and DEC-0368 accepted. Close summary per the intake protocol: the session took up SP-0014 under its DEC-0365 unblocking; ratified the four stale-proposed program decisions DEC-0354..DEC-0357; waived the system-architect consultation one-off (T6/T7); approved and executed the stakeholder-expanded 24-rule design under the DEC-0335/DEC-0345 guard with all five calibration instruments passing; took dispositions on all 102 findings (33 real/change-worthy, 9 debatable, 60 noise); captured six consolidated follow-up Ideas (IDEA-0035..IDEA-0040, reviewed with the stakeholder at the gate summary — the inspired-ideas check; none further offered); ran the recall audit with three provenance enrichments; and produced DEC-0367/DEC-0368 from the spike findings. Classification confirmed: spike execution touching SP-0014 (now approved), with follow-up work routed entirely through the captured Ideas queue. Evidence files remain in the session scratchpad per the stakeholder's T17 instruction; SES-0069 closes with this turn.

## Decisions Produced

## Decisions Produced

DEC-0367 (compiled structural rules fire true findings; precision is source-dependent) and DEC-0368 (no differential reactive-substrate evidence from ActiveGraph) produced from SP-0014's findings catalog, accepted at T21/T22 on stakeholder gate approval. DEC-0354, DEC-0355, DEC-0356, DEC-0357 ratified proposed -> accepted at T5 (recorded decisions originate from SES-0064; this session is the ratification record). The DEC-0292 system-architect reviewer consultation was waived as a one-off by the stakeholder at T6/T7, recorded here as a session outcome alongside the T5 ratification.

## Conflicts Raised

None so far.
