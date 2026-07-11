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
  unblocking. First order of business was a ratification review:
  initial triage flagged four decisions as proposed (DEC-0354,
  DEC-0355, DEC-0359, DEC-0360), but DEC-0359 and DEC-0360 turned
  out already accepted (a misreported status trace); the corpus's
  actual four proposed decisions were DEC-0354, DEC-0355, DEC-0356,
  DEC-0357, all distilled from SES-0064 stakeholder option
  selections whose statuses were never flipped at close. All four
  were presented with verbatim Decision text, source span, and
  ratified-citer blast radius, and accepted by the stakeholder at
  T5. Ratification review is complete; spike execution (system-
  architect advisor consultation, DEC-0335/DEC-0345 design-and-test-
  plan approval, throwaway build and firing, stakeholder disposition
  of findings) proceeds next. Session in progress.
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

## Decisions Produced

No new decisions distilled at this step. DEC-0354, DEC-0355, DEC-0356, DEC-0357 ratified proposed -> accepted at T5 (recorded decisions originate from SES-0064; this session is the ratification record).

## Conflicts Raised

None so far.
