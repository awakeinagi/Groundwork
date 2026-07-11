---
id: SES-0064
type: session
title: "Change intake: evaluate applying activegraph to Groundwork"
status: open
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
  Change-intake session opened at the verbatim proposal (DEC-0255):
  the stakeholder asked to run and learn about a tool called
  activegraph, then evaluate applying it to the Groundwork project.
  Discussion (T3-T11) explored an "executable design knowledge"
  approach -- compiling design best practices and rule-type
  decisions into reactive rules firing over a typed projection of
  the design corpus, with ActiveGraph as candidate substrate -- and
  the stakeholder confirmed, via option selection, a five-spike
  exploratory program (projection, rule precision, compilation
  fidelity, hook-loop economics, fork-and- diff evidence),
  exploratory with no kill bar, ActiveGraph-only with the DEC-0337
  option survey deferred to after the spikes report, and the
  projection spike kept fully separate from SP-0007/DEC-0160. At T12
  the facilitator found the required parent epic (chartered by
  DEC-0339) did not yet exist -- IDEA-0015 recorded its derivation
  as deliberately deferred at SES-0061. T13-T14 presented unblock
  options; the stakeholder directed a facilitator fork to take up
  IDEA-0015. T15's fork (SES-0065) derived, debated, gated, and got
  approval for EP-0009, recording DEC-0350..DEC-0353 and disposing
  IDEA-0015. T16 recorded the four decisions (DEC-0354..DEC-0357:
  the approach and program, no kill-bar thresholds, ActiveGraph-only
  scope with the survey deferred, and SP-A's separation from
  SP-0007) and the five spike artifacts (SP-0013..SP-0017) under
  EP-0009, each with Evaluation Criteria and Data-Source Assumptions
  sections per the SES-0065 handback constraint. Status: open; the
  closing summary follows the recall audit.
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

## Decisions Produced

None yet — investigation is just starting.

## Conflicts Raised

None.
