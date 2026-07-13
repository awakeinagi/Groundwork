---
id: SES-0086
type: session
title: "Change intake: new Research (RSCH) artifact type for deep-investigation learnings"
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-12
participant: operator, Claude
participant-role: stakeholder, facilitator
facilitator: Claude
transcript-fidelity: verbatim
kind: full
intake: {origin: user, proposed-by: operator}
overview: >-
  Change-intake session for a stakeholder proposal to add a new
  Groundwork artifact type, Research (RSCH), for capturing learnings
  from deep investigations and tracing their influence on Business
  Goals and derived work. After a locate-first sweep found no
  duplicate, four grilling rounds resolved RSCH's lifecycle, its
  intake on-ramps and session trace, a method-level research-session
  workflow, three source modes, a source register with per-finding
  citations, a required Business-Goal applicability section, a new
  inspired-by/inspired link pair, its boundaries with Spikes and
  Ideas, and subfile governance, search indexing, and build
  placement along the DEC-0445 seam. The session paused mid-grilling
  to confirm SES-0085 had closed before deciding placement. Ten
  decisions were produced (DEC-0447 through DEC-0456). The
  stakeholder confirmed the closing summary and asked for the
  glossary to be updated. The facilitator then ran the distillation
  machinery: a consistency sweep over all ten decisions returned
  thirty-one informational citer hits and a clean terms check; a
  decision-recall audit produced twenty-two candidates, sixteen
  judged not-a-gap, four dispositioned as already-consistent
  precedent needing only cross-reference enrichment, and two
  presented as genuine open decisions. The stakeholder resolved
  both, choosing cites-sync checking under DEC-0247 and extending
  DEC-0104's deferred status to RSCH, and authorized close. Two
  supplementary decisions (DEC-0457, DEC-0458) were recorded, the
  four enrichment links added, and the glossary updated. Eighteen
  turns are recorded; the session is closed.
links:

  relates-to: [DEC-0447, DEC-0448, DEC-0449, DEC-0450, DEC-0451, DEC-0452, DEC-0453, DEC-0454, DEC-0455, DEC-0456, DEC-0457, DEC-0458]
---

# SES-0086: Change intake: new Research (RSCH) artifact type for deep-investigation learnings

## Purpose

This session intakes a stakeholder proposal to add a new Groundwork artifact type, Research (RSCH-*), for capturing learnings from deep investigations and tracing their influence on Business Goals and derived work. The session opens the change-intake protocol as a full grilling session because the proposal is a method-level change to the Groundwork paradigm itself.

## Transcript

### T1

**Stakeholder:** I would like to create new artifact called Research (RSCH) to be used to what's learned from deep investigations/research into a topic web search, books, videos, etc. What was learned? How could it apply to Business Goals? And track derived work like Spikes, Epics, and Stories (or new Business Goals); artifacts that it inspired. It should be traced back to an intake session (OK to be quick) that captured it with helpful context as to what inspired the investigation.

### T2

**Facilitator:** The facilitator restated the intent as a new Groundwork artifact type, Research (RSCH-*), that (1) captures the output of a deep investigation into a topic — web search, books, videos, or other sources — recording what was learned; (2) connects learnings to business intent with an explicit analysis of how findings could apply to existing Business Goals or motivate new ones; (3) tracks derived work — Spikes, Epics, Stories, or new Business Goals the research inspired — so the corpus shows that work exists because of the research; and (4) is traced to an intake session (which may be quick/lightweight) capturing the context of what inspired the investigation, so provenance starts at the motivating moment, not at the findings. The facilitator classified this as a method-level change to the Groundwork paradigm itself — specs, templates, gw CLI type support, checker rules, graph model, and a defined lifecycle are all in scope — and recommended a full grilling session.

### T3

**Stakeholder:** Confirmed the restatement matches intent and chose to begin a full grilling session (recommended option) over an expedited session or IDEA capture.

### T4

**Facilitator:** Reported the locate-first sweep (DEC-0266): no duplicate exists in the corpus; the nearest prior art is IDEA-0005, a captured researcher-agent tooling idea — adjacent, not a duplicate. DEC-0443's anticipated derived-work roster names "Artifact model" as the home topic for artifact-type additions under the rechartered BG-0002. The two boundaries doing most design work are RSCH versus Spike (SPEC-spike frames a Spike as a research unit inside the design tree, deriving from an Epic) and RSCH versus Idea (raw pre-classification capture versus post-investigation analyzed evidence). The typed-link vocabulary is closed (DEC-0009, DEC-0026), so derived-work tracking needs either reuse or a vocabulary extension. Flagged that SES-0085 (the BG-0002 recharter) appeared still open, recommending decisions be held until it lands.

### T5

**Facilitator:** Grilling round 1 asked: when an RSCH comes into existence; the RSCH/Spike boundary; how the trigger enters the corpus; and whether RSCH is gated.

### T6

**Stakeholder:** Chose both entry points for creation (commissioned and post-hoc). Chose the direction-of-derivation boundary with Spikes (recommended). On intake, said all three on-ramps make sense (direct quick session, IDEA take-up, parked tangent from any session) and asked to grill the workflow of a dedicated research session, describing it near-verbatim: capture the user's intent (what is to be researched and why) and research goals; decide what sources to use (the user provides a complete source list, or the user provides a seed list and the agent expands the search to find more information, or the agent searches for sources on its own); the agent does a deep dive into each source; the agent decides whether the user's intents and goals have been met, and if not looks for more sources and repeats the deep dive and assessment in a loop until they are met; the agent compiles all findings and presents them to the user; the agent outputs the research into the RSCH artifact. Also asked for the option of multi-file detailed write-ups living within a directory under the research artifact's main directory (for example docs/research/RSCH-0123/ containing multiple subtopic .md files). Chose ungated with a reviewed close.

### T7

**Facilitator:** Grilling round 2 asked: the multi-file structure; the status lifecycle; where the research-execution workflow lives; and source-provenance rigor.

### T8

**Stakeholder:** Chose all four recommendations: one canonical main file plus supporting subtopic files without their own IDs or frontmatter; statuses commissioned to in-progress to concluded plus abandoned, with post-hoc entries created directly at concluded; the method defines the workflow while the executable harness becomes derived build work; and a source register with per-finding citations.

### T9

**Facilitator:** Grilling round 3 asked: how "inspired by this research" enters the link vocabulary; whether the Business-Goal applicability analysis is required; where the build work lands and IDEA-0005's disposition; and how the RSCH traces to its intake session.

### T10

**Stakeholder:** Chose the new reciprocal inspired-by/inspired link pair, amending it so that IDEAs and other RSCH artifacts can also be inspired-by an RSCH. Confirmed the applicability section as required at conclusion, the new Artifact-model epic under BG-0002 as the build home, and derives-from as the session trace.

### T11

**Facilitator:** Verified via bounded gw reads that SES-0085 had closed and DEC-0441, DEC-0442, and DEC-0443 were accepted, dissolving the sequencing hold. Noted DEC-0445's dynamic-versus-static seam: EP-0009 broadened to Artifact Lifecycle & Interaction while static artifact-type design stays with the anticipated Artifact-model epic — confirming the stakeholder's placement choice and implying the build work deliberately straddles the seam.

### T12

**Facilitator:** Grilling round 4 asked: whether a concluded RSCH can change; the rules governing subtopic files; and their visibility to semantic search.

### T13

**Stakeholder:** Overrode the immutability recommendation: a concluded RSCH is reopenable, with each research round recorded in its own timestamped section. Accepted owned/referenced/checked subfile governance and semantic indexing of subfiles attributed to the parent.

### T14

**Facilitator:** Presented the detailed closing summary covering the type, lifecycle, boundaries, intake, workflow, provenance, links, and placement, and ran the inspired-ideas check.

### T15

**Stakeholder:** Confirmed the summary as the session's outcome, asked that the glossary be updated as needed, and reported no new ideas to capture.

### T16

**Facilitator:** Reported the distillation machinery results. The consistency sweep over DEC-0447 through DEC-0456 returned thirty-one citer hits, all informational: DEC-0454 extends rather than narrows the DEC-0009/DEC-0026 vocabulary, so their ratified citers (BG-0001, CMP-0001, EP-0001 through EP-0007, ST-0001, ST-0005, ST-0007, ST-0045) remain consistent, and the remaining hits via DEC-0258, DEC-0335, DEC-0443, and DEC-0445 are likewise additive context with no contradiction; the terms check was clean. The decision-recall audit then produced twenty-two candidates, judged in three Sonnet 5 shards; sixteen were judged not-a-gap and six flagged. Four flagged items were dispositioned as already-consistent precedent needing only cross-reference enrichment: DEC-0261 composes with DEC-0449 because the IDEA take-up on-ramp is itself a quick intake session with the captured IDEA as trigger context; DEC-0159 is the sole prior vocabulary-extension precedent and its spec/checker/graph ripple is exactly the derived build work DEC-0456 routes; DEC-0423's single-sourcing constrains how the build epics implement RSCH mechanics without contradicting where DEC-0456 routes the work; and DEC-0248 sanctions retroactively adding inspired-by links to ratified artifacts without re-gating. Two flagged items were presented as genuine open decisions: whether RSCH is cites-sync-checked under DEC-0247, and whether the deferred status of DEC-0104 extends to RSCH.

### T17

**Stakeholder:** Chose cites-sync checked like design-tree artifacts, overriding the facilitator's exemption recommendation, and chose extending deferred to RSCH. Asked the facilitator to elaborate on what confirming the four dispositions meant; after a plain-language explanation that they add precedent pointers and an audit-outcome transcript turn without changing any decision, confirmed the dispositions and authorized close and commit.

### T18

**Facilitator:** Recorded the two supplementary decisions and the four enrichment links, updated the glossary, and closed the session.

## Decisions Produced

Twelve decisions: DEC-0447 (new artifact type: Research (RSCH)), DEC-0448 (RSCH lifecycle and gating), DEC-0449 (RSCH intake on-ramps and session trace), DEC-0450 (research-session workflow at method level), DEC-0451 (source modes), DEC-0452 (source provenance inside findings), DEC-0453 (required Business-Goal applicability section), DEC-0454 (link-vocabulary extension: inspired-by and inspired), DEC-0455 (boundary rules for RSCH), DEC-0456 (subfile governance, search, and build placement), DEC-0457 (RSCH is subject to the cites-sync check), and DEC-0458 (the deferred status extends to Research artifacts).

## Conflicts Raised

None yet.
