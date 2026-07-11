---
id: SES-0064
type: session
title: "Change intake: evaluate applying activegraph to Groundwork"
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-10
participant: awakeinagi
participant-role: stakeholder
facilitator: "Claude (Fable 5)"
transcript-fidelity: verbatim
kind: full
intake:
  origin: user
  proposed-by: awakeinagi
links:
  relates-to: []
overview: >-
  Change-intake session opened at the verbatim proposal (DEC-0255)
  to evaluate applying ActiveGraph to Groundwork. T3-T11 explored an
  "executable design knowledge" approach and confirmed a five-spike
  exploratory program, no kill bar, ActiveGraph-only scope. T12-T15
  forked to take up IDEA-0015, deriving and approving the required
  parent epic EP-0009 (DEC-0350..DEC-0353) in SES-0065. T16 recorded
  DEC-0354..DEC-0357 and SP-0013..SP-0017 under EP-0009. T17
  presented a three-judge recall-audit verdict; T18-T20 applied
  accepted fixes, gated and approved SP-0013, and spawned an empty-
  context executor for it. T21 the executor's SP-0013 findings
  arrived: 100% round-trip projection (16 Components, 53 Elements,
  346 ContractItems, 140 Decisions, 28 Stories), but zero typed
  Uses: lines exist anywhere despite the DEC-0299/DEC-0306/DEC-0309
  mandate, plus 10 provenance edge cases and a gap list. T22 the
  stakeholder deferred SP-0014's execution until the Uses: backfill
  completes (over a reduced rulebase), sent the provenance and
  audit-tooling defects to idea capture, approved SP-0015 with the
  arc42-section source (gate, approve, launch), and accepted the T17
  reject dispositions as final. T23 recorded SP-0013's Findings,
  DEC-0358 (the SP-0014 deferral), IDEA-0025..IDEA-0027, and
  SP-0015's gate/approve. T24-T26 recorded SP-0015's execution
  findings (arc42 §5 Building Block View source, 14 candidate rules
  plus 9 uncompilable, two novel failure modes) and the
  stakeholder's per-rule fidelity verdicts (12/14 ratified, 2
  downgraded to advisory, zero corrupted compiles). Decisions
  Produced lists DEC-0354..DEC-0358. T27 the stakeholder declined
  further ideas and closed the session; T28 recorded the closing
  summary. Status: closed.
---

## Purpose

Change-intake session for a stakeholder proposal to run and learn
about a tool called "activegraph," then evaluate applying it to the
Groundwork project. Per DEC-0255, this record opens at the verbatim
proposal, before any investigation. The tool's nature is unknown at
open time; the session will investigate it safely (help/docs before
quickstart, quickstart sandboxed outside the repo), run a locate-first
pass over the corpus for related prior art or decisions, and return
findings plus a path-pick recommendation. Adoption itself is a
tooling/technology decision gated by an option survey (DEC-0337)
before anything is built or adopted.

## Transcript

**T1 — awakeinagi (stakeholder):**
Run this and learn about what it is doing. I would like to apply this
to the Groundwork project. `activegraph quickstart`

**T2 — Claude (Fable 5), facilitator:**
Restating your intent: you want me to (1) run the `activegraph
quickstart` command and learn what the activegraph tool does, and (2)
evaluate applying it to the Groundwork project. Per intake, I am
opening this session record first, then investigating the tool safely
(help/docs before quickstart, quickstart sandboxed outside the repo),
then running locate-first over the corpus, and returning with findings
and a path-pick recommendation. The adoption itself is a
tooling/technology decision and will require an option survey per
DEC-0337 before anything is built or adopted.

**T3 — awakeinagi (stakeholder):**
Let's have a discussion about this first before we decide on the intake
path and inversions. How could it benefit this project? One of its
major claims is that it becomes a long term and working memory that
doesn't have to rely on the context window. That could be a
force-multiplier for the data we're catalogging in this project.
Moreover, I think this could be very helpful for the design and
implementation stages of this work. E.g right now our
system-architect agent has to rely on summarized documentation on
best practices. What if instead we could use a skill like
https://github.com/virgiliojr94/book-to-skill to extract all of the
information from sources like we found (doesn't have to be just
books; web pages work too, any docs really). Then we have an agent
parse the extracted text into rules coded using activegraphs approach
(a skill). Then we have another skill that adds hooks to a separate
design agent so that when it edits a design test file it then fires
the activegraph rules to test the design. This way the design agent
doesn't have to load a bunch of text into its context to apply what
it's learned. Explore this idea creatively; elaborate on it.

**T4 — Claude (Fable 5), facilitator:**
Elaborated the idea as "compile knowledge into self-firing rules"
versus "text in context": three rule tiers (structural patterns, LLM-
judgment behaviors, scoped heuristics); a reactive hook loop that
returns findings rather than textbooks to the editing agent; fork-
and-diff as empirical evidence in the dual-architect debate; compiling
Groundwork's own rule-type DECs into self-enforcing behaviors; and a
long-lived run acting as cross-session working memory. Flagged
tensions: compilation lossiness, linter-style noise, DEC-0010
preserved only if the design graph stays a derived projection of the
docs (never a second source of truth), ActiveGraph's alpha-stage
maturity, and the third-derived-store precedent already set by
DEC-0116.

**T5 — awakeinagi (stakeholder):**
Our component artifacts already store a wealth of information on our
proposed design. This information can be used to test and evolve our
design into something more aligned with best practices.

**T6 — Claude (Fable 5), facilitator:**
Commissioned schema grounding. The report confirmed the 16 CMP docs
carry rich element-scoped, contract-item-scoped (Element.K-n, C-n,
IG-n), and Uses:-typed dependency data, and that the current graph
index models none of it below whole-component level. Surfaced
SP-0007 and DEC-0160 as direct precedent: DEC-0160 already deferred
contract-item-level graph nodes to a dedicated spike (SP-0007), which
remains draft and unscoped in detail under EP-0004.

**T7 — awakeinagi (stakeholder):**
Let's design some spikes to test ideas and confirm the usefulness of
this approach.

**T8 — Claude (Fable 5), facilitator:**
Proposed a five-spike set — projection, rule precision, compilation
fidelity, hook-loop economics, and fork-and-diff evidence — each with
a recommended success bar, and framed as feeding into (not replacing)
the DEC-0337 option survey.

**T9 — awakeinagi (stakeholder, option selections):**
Confirmed all five spikes including the fork-and-diff spike (E);
confirmed the program is exploratory with no kill bar; confirmed
ActiveGraph-only scope for the spikes, with the DEC-0337 option
survey (baseline vs. thin owned implementation vs. ActiveGraph)
deferred until after the spikes report; confirmed the home epic as
the epic chartered by DEC-0339.

**T10 — Claude (Fable 5), facilitator:**
Surfaced the collision between the proposed projection spike (SP-A)
and SP-0007's existing draft scope, and the tension over which epic
should house the new spikes given SP-0007 sits under EP-0004. Asked
the stakeholder for disposition.

**T11 — awakeinagi (stakeholder, option selections):**
Confirmed SP-A proceeds fully separate from SP-0007 (SP-0007 remains
draft, unmodified, under its original EP-0004 scoping; the parse-scope
overlap is a deliberately accepted duplication); confirmed all five
new spikes are housed under the epic chartered by DEC-0339.

**T12 — Claude (Fable 5), facilitator:**
Attempted to resolve the epic chartered by DEC-0339 (the Artifact
Interaction Surface epic under BG-0002) as the required parent for the
five spikes. Found no EP artifact deriving from DEC-0339 exists in the
corpus: IDEA-0015 records that this epic derivation was deliberately
deferred at SES-0061 and remains status `captured` (never taken up).
Per the spike-derivation gate (spikes must derive from an approved
parent epic), stopped before creating any DEC or SP artifacts for the
program. This transcript record stands; the four decisions and five
spike artifacts described in the session's design discussion are not
yet recorded in the corpus pending that epic's derivation. Session
remains open.

**T13 — Claude (Fable 5), facilitator:**
Presented the unblock options for the epic-derivation gate found at
T12: take up IDEA-0015 to derive the required parent epic, re-house
the spike program under a different existing epic, or park the
program as detailed IDEAs for later take-up.

**T14 — awakeinagi (stakeholder):**
Initially selected parking as detailed IDEAs, then withdrew that
selection and instructed: spawn a facilitator fork to take up
IDEA-0015 interactively; return here for spike creation afterward.

**T15 — Claude (Fable 5), facilitator:**
Spawned SES-0065 (take-up of IDEA-0015): EP-0009 was derived, refined
through dual-instance architect debate (converged
GATE-READY-WITH-CHANGES, all-LOW), gated, and approved by the
stakeholder (2026-07-10); DEC-0350..DEC-0353 were recorded; IDEA-0015
was disposed; IDEA-0024 was captured. The handback constraint folded
into this session: every SP artifact states evaluation criteria and
data-source assumptions.

**T16 — Claude (Fable 5), facilitator:**
Recorded the four decisions and five spikes under EP-0009: DEC-0354
(the executable-design-knowledge approach and five-spike program),
DEC-0355 (exploratory, no kill-bar thresholds), DEC-0356 (ActiveGraph-
only scope, DEC-0337 survey deferred until after the spikes report),
and DEC-0357 (the projection spike proceeds fully separate from
SP-0007). Created SP-0013 (projection, "ActiveGraph projection of
component contract data"), SP-0014 (structural rule precision,
impacted-by SP-0013), SP-0015 (prose-to-rule compilation fidelity,
independent), SP-0016 (reactive hook-loop economics, impacted-by
SP-0014), and SP-0017 (fork-and-diff design-debate evidence,
impacted-by SP-0014, queued last). Every spike cites DEC-0354 and
DEC-0351; SP-0014 additionally cites DEC-0355; each carries
"Evaluation Criteria" and "Data-Source Assumptions" sections and notes
its throwaway script's validation approach is part of the spike design
per DEC-0345, sized minimally per DEC-0336.

**T17 — Claude (Fable 5), facilitator:**
Presented the consolidated recall-audit verdict from three Sonnet 5 judges across all six artifacts (SP-0013..SP-0017, DEC-0356). Accepted additions: SP-0013 add-cites DEC-0309, DEC-0299, DEC-0081, DEC-0087; SP-0014 add-cites DEC-0315, DEC-0309, DEC-0299, DEC-0086; SP-0015 add-cite DEC-0294; SP-0016 add-cites DEC-0315, DEC-0118; SP-0017 add-cite DEC-0293; DEC-0356 relates-to DEC-0336. Rejected findings held for discussion: DEC-0354 (DEC-0157/DEC-0345/DEC-0348 proposed adds); DEC-0355 (nothing-to-add); DEC-0357 (a DEC-0172/DEC-0173 chain judged a topic-misread); SP-0017 (a DEC-0348 proposed add judged a misread -- run-forks, not agent-spawns); SP-0016 (a DEC-0340 proposed add judged already covered by the DEC-0351 guardrail); SP-0014 (a DEC-0338 proposed add judged already carried via EP-0009). Judges also surfaced audit-packet tooling defects -- missing artifact content, identical considered-lists across findings, stderr leaking into JSON output, and a stale-graph warning -- flagged for idea capture at session close.

**T18 — awakeinagi (stakeholder, option selections):**
Apply accepts, discuss rejects. SP-0013 path: gate, then approve, then execute.

**T19 — awakeinagi (stakeholder):**
Spawn a subagent (inherit your model) with empty context to take up SP-0013

**T20 — Claude (Fable 5), facilitator:**
Applied the accepted fixes: cites and their required DEC-0247 body mentions added to SP-0013..SP-0017 (Method sections), plus SP-0013's Data-Source Assumptions gained two confirmed/scoped lines; DEC-0356 gained a relates-to DEC-0336 link. SP-0013 was gated then approved (approved-by awakeinagi@gmail.com, approved-on 2026-07-10) on T19's execute authority. An empty-context executor subagent was spawned with SP-0013's Method section as its brief. Reject dispositions from T17 remain pending stakeholder discussion before session close.

**T21 — Claude (Fable 5), facilitator:**
SP-0013's executor subagent reported back: it honored the read-only-over-`docs/` and scratchpad-only-store constraints throughout. Findings -- 100% round-trip projection (16 Components, 53 Elements, 346/346 ContractItems, 140 Decisions, 28 Stories; 53 HAS_ELEMENT, 346 HAS_ITEM, 65 IMPLEMENTS, 581 CITES, 26 DEPENDS_ON, parser/graph/grep counts agreeing three ways); a central negative finding that zero typed `Uses:` lines exist anywhere in the corpus despite the DEC-0299/DEC-0306/DEC-0309 mandate, leaving structural dependency data as 26 untyped component edges plus prose only; 10 provenance edge cases out of 346 items (story-AC citations, implemented-protocol-item citations, four effectively uncited items); and a gap list covering unrepresentable non-DEC provenance, range-item cardinality loss, sibling-scoped citation attribution, dropped item-body semantics, and bare-ID `Implements:` lines versus DEC-0092's link mandate, plus two corpus ambiguities (CMP-0006's non-conforming shape, CMP-0001/CMP-0004's family-size disagreement).

**T22 — awakeinagi (stakeholder, option selections):**
SP-0014 waits: full deferral until the corpus-wide `Uses:` backfill is taken up and completed, over proceeding now with a reduced rulebase. The provenance and tooling defects SP-0013's findings and the T17 audit surfaced are captured as Ideas, not fixed inline. SP-0015 proceeds gate, approve, launch, with the arc42-section source (system-architecture-bp) rather than the book-to-skill extraction alternative. The T17 reject dispositions are accepted as final.

**T23 — Claude (Fable 5), facilitator:**
Recorded SP-0013's Findings section from T21's digest (status remains `approved` -- SPEC-spike defines no post-execution status beyond the common gate lifecycle). Recorded DEC-0358 (SP-0014's execution deferred until the `Uses:` backfill completes), with a corresponding precondition note added to SP-0014's Data-Source Assumptions. Captured IDEA-0025 (backfill typed `Uses:` lines and arm checker enforcement, blocking SP-0014), IDEA-0026 (repair contract-item provenance defects), and IDEA-0027 (fix the recall-audit packet generator), each cross-referencing SES-0064. SP-0015 gained a Method note recording the arc42-section source selection, then was gated and approved (approved-by awakeinagi@gmail.com, approved-on 2026-07-10). Per T22, the T17 reject dispositions are now final. Session remains open.

**T24 — Claude (Fable 5), facilitator:**
SP-0015's executor report arrived (read-only-over-`docs/` and scratchpad-only-store constraints honored throughout). Findings: source was arc42 Section 5, Building Block View (lines 340-546 of the vendored template in system-architecture-bp), compiled in full; output was 14 candidate rules (3 structural-presence, 3 judgment-class, 5 guarded heuristics, 3 meta-constraints) plus 9 pieces of source content correctly judged uncompilable, with the full candidate table retained as throwaway scratchpad evidence per DEC-0351; a failure-mode catalog extending the three anticipated modes with two novel ones -- contradiction-generating rule pairs (R3 vs R11, resolved only by the uncompilable meta-principle R12 riding along as a guard) and a template-vs-invariant genre effect (a documentation-template source compiles mostly into presence checks, not design-correctness invariants).

**T25 — awakeinagi (stakeholder, option selections):**
Fidelity review verdicts via per-rule side-by-side option selection: R1, R3, R4, R5, R6, R13 ratified as-is; R7, R8, R11 ratified in guarded compiled form (R8 guarded to author-flagged complex interfaces only, phrased as confirming a signature isn't sufficient; R11 guarded to author-supplied importance metadata, graph proxies rejected); R2, R9 ratified but downgraded to advisory severity; R14 ratified as an LLM-judgment rule; R10, R12 reclassified as meta-guards on the ruleset rather than firing rules. 12 of 14 ratified in compiled form; zero corrupted compiles ratified.

**T26 — Claude (Fable 5), facilitator:**
Recorded SP-0015's Findings section from T24's digest and T25's per-rule verdicts (status unchanged, `approved` -- SPEC-spike defines no post-execution status beyond the common gate lifecycle). Session remains open.

**T27 — awakeinagi (stakeholder):**
No new ideas, close the session.

**T28 — Claude (Fable 5), facilitator:**
Closing summary presented: this session investigated applying ActiveGraph to Groundwork and confirmed a five-spike exploratory program (no kill bar) housed under EP-0009; SP-0013 and SP-0015 were executed and answered their questions (100% round-trip projection with a central Uses:-absence finding; 12/14 rules ratified with a two-mode extension to the failure catalog); DEC-0358 recorded SP-0014's deferral until the Uses: backfill completes; IDEA-0025..IDEA-0027 were captured and queued; the T17 recall-audit dispositions are final. No inspired ideas at close. Session closed.

## Decisions Produced

DEC-0354, DEC-0355, DEC-0356, DEC-0357, and DEC-0358 have been recorded in this session (T16, T23): DEC-0354 (the executable-design-knowledge approach and five-spike program), DEC-0355 (exploratory, no kill-bar thresholds), DEC-0356 (ActiveGraph-only scope, DEC-0337 survey deferred), DEC-0357 (the projection spike proceeds fully separate from SP-0007), and DEC-0358 (SP-0014's execution deferred until the corpus-wide `Uses:` backfill completes).

## Conflicts Raised

None.
