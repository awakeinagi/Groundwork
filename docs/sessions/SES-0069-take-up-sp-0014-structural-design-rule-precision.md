---
id: SES-0069
type: session
title: "Take up SP-0014: structural design-rule precision spike"
status: open
owner: awakeinagi@gmail.com
created: 2026-07-11
participant: awakeinagi@gmail.com
participant-role: operator/stakeholder
facilitator: Claude (Fable 5) via Claude Code
transcript-fidelity: reconstructed
overview: >-
  Session opened to take up and execute spike SP-0014 (structural
  design-rule precision over the projected corpus) per its DEC-0365
  unblocking. A ratification review closed four proposed decisions
  (DEC-0354, DEC-0355, DEC-0356, DEC-0357) at T5. The stakeholder
  waived the DEC-0292 system-architect consultation for this session
  as a one-off (T6-T7), on the reasoning that the architect debates
  for the program design already ran at SES-0064/SES-0065. The
  facilitator presented a 12-rule structural rulebase design and
  test plan per DEC-0335/DEC-0345 (T8); the stakeholder then
  directed expansion to every worthy structural rule from the two
  curated sources with no upper limit (T9), and the facilitator
  expanded the rulebase to 24 rules -- 14 discovery, 5 calibration
  with recorded expected outputs, 3 vacuous against current data,
  and 2 weak/proxy probes -- recorded as this session's amendment to
  SP-0014's Method (T10). The stakeholder approved continuing at
  T11. Design approved; throwaway build and firing against SP-0013's
  projection is now underway, to be followed by stakeholder
  disposition of every finding and recording of Findings and
  Resulting Decisions on SP-0014.
links:
  relates-to: [SP-0014, DEC-0354, DEC-0355, DEC-0359, DEC-0360, DEC-0356, DEC-0357]
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

## Decisions Produced

No new decisions distilled at this step. DEC-0354, DEC-0355, DEC-0356, DEC-0357 ratified proposed -> accepted at T5 (recorded decisions originate from SES-0064; this session is the ratification record).

## Conflicts Raised

None so far.
