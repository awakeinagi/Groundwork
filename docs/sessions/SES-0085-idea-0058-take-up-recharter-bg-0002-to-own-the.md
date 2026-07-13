---
id: SES-0085
type: session
title: "IDEA-0058 take-up — recharter BG-0002 to own the Groundwork Engine as the core technology"
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-12
participant: awakeinagi
participant-role: stakeholder/operator
facilitator: Claude (Fable 5)
transcript-fidelity: reconstructed
kind: full
intake: {origin: idea, source-ref: IDEA-0058}
overview: >-
  Take-up session for IDEA-0058, opened 2026-07-12 per the change-
  intake protocol (DEC-0255) and closed the same day. A full
  grilling session rechartering BG-0002 around the Groundwork Engine
  as the core technology, superseding its prior method-track
  governance charter. Three grilling rounds and a re-gate distilled
  DEC-0441 (the recharter), DEC-0442 (governance subsumed), DEC-0443
  (thirteen-topic anticipated roster, later extended to fifteen by
  DEC-0446), and DEC-0444 (skill-mode definition), with DEC-0338
  superseded and CONTEXT.md updated. BG-0002's body was rewritten
  and retitled (Groundwork Core Technology — Engine & Delivery of
  the Paradigm) via a sanctioned direct title/H1 repair, the write
  API's IDEA-0042-class gap, and re-affirmed approved under the
  DEC-0267 stale-and-reapprove path rather than a fresh gate. The
  staleness cascade marked EP-0009 and SP-0013 through SP-0017
  stale; the five spikes were re-affirmed approved with fresh
  stamps. The stakeholder then broadened EP-0009 to Artifact
  Lifecycle & Interaction (DEC-0445) and, at the closing gate, added
  Observability and Dogfooding to the roster (DEC-0446), ratifying
  the recharter as approved. Two ideas were captured: IDEA-0060
  (per-artifact grilling scope) and IDEA-0061 (the title-rename
  write-operation gap). The recall audit judged all twenty
  candidates not-a-gap. Twenty-eight transcript turns recorded.
links:
  relates-to: [IDEA-0058, BG-0002, DEC-0441, DEC-0442, DEC-0443, DEC-0444, DEC-0445, DEC-0446]
---

# SES-0085: IDEA-0058 take-up — recharter BG-0002 to own the Groundwork Engine as the core technology

## Purpose

Take-up of IDEA-0058, captured at SES-0082 T51. This is a full grilling session at Business-Goal level: recharter BG-0002 around the Groundwork Engine as the core technology, resolve the fate of the current governance-track charter, run the DEC-0267 cascade over BG-0002's derived tree, and assess re-parenting of Engine-related deferred work. BG-0001's own reframing is explicitly out of scope (a separate step per the idea).

## Transcript

### T1 (stakeholder, verbatim proposal, reconstructed from IDEA-0058 "The Idea", originally SES-0082 T51)

"This dogfooding exercise has been very helpful in refining the trajectory for Groundwork. Looking back, I feel like I jumped the gun a bit in deciding for a full application from the start. I'm really seeing the benefit of the agents and skills working with methodology. The application itself really is mostly a presentation layer around the Groundwork Engine. Toward that realization, I'm starting to think that BG-0002 may be better suited to track the development and refinement of the Groundwork Engine itself as the core technology to work on, even if an application with a UI may have its own merits. Since BG-0002 is still relatively new, I think it might not be too hard to change its focus. What are your thoughts?"

### T2 (facilitator, restatement)

The facilitator restated the intent: recharter BG-0002 so it tracks the development and refinement of the Groundwork Engine itself as the core technology, rather than its current charter as the method-track governance goal ("The Method Track — Groundwork governs its own tooling"). The application UI is repositioned as a merit-bearing presentation layer atop the Engine, not discarded. The session must resolve: (1) the new charter wording; (2) the fate of the current governance-track charter — subsumed as self-governance or split out separately; (3) the DEC-0267 cascade over BG-0002's derived tree (EP-0009, SP-0013 through SP-0018, and citing decisions) with re-affirmations presented in-session; (4) re-parenting of Engine-related deferred work (the DEC-0423 library-extraction trigger, the DEC-0430/DEC-0437 ID-allocation mechanics, SP-0018). Explicitly out of scope: BG-0001's reframing toward a presentation-and-team layer, noted as a further separate step. Path: full grilling session.

### T3 (stakeholder, alignment)

The stakeholder confirmed alignment via the structured question tool, selecting "Aligned — open the session," and instructed the facilitator to open the take-up session and proceed to locate-first and grilling.

### T4 (facilitator — locate-first findings, DEC-0266; presented in chat as follows, verbatim)

"Verdict: the recharter is structurally clean. The bulk of BG-0002's tree is already Engine-work in substance; the recharter is the charter-level completion of what SES-0082 already decided (DEC-0420–0423, 0432, 0433), not a duplicate of anything. No prior BG-level 'Engine as core technology' framing exists. What re-parents cleanly (the bulk): EP-0009 and all six spikes SP-0013–SP-0018, plus DEC-0339, DEC-0341, DEC-0351, DEC-0367/0368, the whole SES-0082 decision set, and captured ideas IDEA-0012/0013. The deferred Engine work IDEA-0058 flagged (DEC-0423's library-extraction trigger, DEC-0430/DEC-0437 ID-allocation mechanics landing with SP-0018) all sits naturally under an Engine-chartered BG-0002. The governance-specific residue is small: DEC-0338 (the current charter itself — the recharter directly supersedes it), DEC-0342 (SES-0058 backfill framing), DEC-0346 (sacrificial-pattern framing, already narrowed twice by DEC-0421/0422), SES-0060 (charter-history session, provenance only), and IDEA-0057 (captured: 'decide this repo's operating mode once the Application exists' — which is exactly the self-governance-vs-split question in live form). Cascade shape: every one of the ~33 citing decisions is accepted, so nothing gets edited — the recharter supersedes DEC-0338 (and possibly DEC-0342/0346), then the DEC-0267 staleness walk runs over the derived tree with re-affirmations in-session. Two flags from the context packet: (1) 'skill-mode' has no glossary entry despite being load-bearing in DEC-0421/0422/0433 — this session is a natural place to formalize it in CONTEXT.md. (2) DEC-0423's interim state is explicit: gw_write.py and siblings are the de facto Engine until the first non-CLI consumer triggers library extraction — the new charter should own that trigger rather than re-schedule extraction. One scoping note: BG-0002's current Constraints and Outcomes are almost entirely governance-process rules (no-arbitrary-builds, contracts-first, conformance checking). Under an Engine charter these become the self-governance portion — which is why the subsume-vs-split question is the load-bearing decision of this session."

### T5 (stakeholder — VERBATIM)

"Go ahead, open round 1. I would like to point out that Business Goals are the highest level of abstraction in the Groundwork paradigm. They only track original intention and what is to be achieved and say nothing about how it will be achieved or implementation details. So architect consultation doesn't make sense here. I would like to create an IDEA so we can follow up in the future on clearly defining the scope for each of the artifacts and how they should be grilled."

### T6 (facilitator)

Agreed and dropped the discretionary system-architect consultation: Business Goals track original intention and outcomes only, so there is no architecture to advise on at this level — and that framing constrains the recharter itself: the new charter must state what the Engine goal achieves, never how. Captured the stakeholder's follow-up proposal as IDEA-0060 ("Define per-level artifact scope and grilling method", status captured, verbatim quote preserved there). Opened grilling round 1 as three structured question cards, each option carrying a recommendation: (1) Charter object — what is rechartered BG-0002's object of intent? Options: Engine + its delivery surfaces (recommended); Engine mechanics only; Engine + full paradigm delivery. (2) Governance — what happens to BG-0002's current governance-track charter? Options: subsume as self-governance (recommended); split into a separate governance BG; demote governance to constraints only. (3) Glossary — should "skill-mode" become a defined CONTEXT.md term in this session? Options: define it now (recommended); leave undefined; fold into the new IDEA.

### T7 (stakeholder — VERBATIM answers to round 1)

On charter object: "Option 3. Plus I want topic specific epics to tackle the design of: agents, skills (to be used by Groundwork-owned agents and to be used users interacting with the system [e.g. upon entry into CC, no GW agent loaded], usage with or without the app, the artifacts used by the engine and their scoping/design. Any others we should list now? Some of this will be an partial exercise in brownfield work; i.e. taking a prexisting project and folding it into the Groundwork paradigm. In the future, we will have to take pre-existing projects and build the groundwork docs from what already exists. I want an epic (or two) to track Greenfield and Brownfield work." On governance: "This could be part of the goals and maybe deserves its own focused Epic." On skill-mode: "Let's grill on this further during this session. But to get us started, I would start the definition by saying it's when a user interfaces with the Groundwork paradigm via an agent chat only (using the skills like groundwork-design-session) like Claude Code, Github Copilot, Codex, OpenCode, etc., no app/UI. "

### T8 (facilitator)

Consolidated the anticipated epic-topic roster from the answers — (1) Agents; (2) Skills, both audiences: consumed by Groundwork-owned agents, and for users entering bare (e.g. Claude Code with no GW agent loaded); (3) Artifact model — the artifacts the Engine operates on, their scoping and design (natural eventual home for IDEA-0060); (4) Usage with/without the app — modality parity, where DEC-0433's parity matrix would live; (5) Adoption: greenfield & brownfield; (6) Self-governance/dogfooding as a focused epic; (7) Paradigm export/packaging (IDEA-0010/IDEA-0013 territory); (8) EP-0009 continuing as-is. Opened round 2 as four cards: (1) Additional topics worth listing now (multi-select) — runtime portability; collaboration & concurrency (SP-0018, DEC-0430/0437); human browsing surface; or none. (2) Boundary with BG-0001 — App itself stays BG-0001 (recommended) vs BG-0002 owns everything technical. (3) Greenfield/brownfield — list one and split at derivation (recommended) vs two epics now. (4) skill-mode edge — does raw gw CLI use (scripts, CI, no agent) count? Agent-chat defines it, CLI is the substrate (recommended); any non-app use counts; keep grilling.

### T9 (stakeholder — VERBATIM answers to round 2)

On additional topics: "Runtime portability, Collaboration & concurrency, Human browsing surface, Any other you would recommend?" On the BG-0001 boundary: "App itself stays BG-0001 (Recommended)". On adoption: "Two epics now". On skill-mode: "Agent-chat defines it (Recommended)".

### T10 (facilitator)

Recommended one further topic — the Engine core itself: EP-0009 covers only the interaction surface (artifact-librarian + artifact-interact); no roster topic owned the Engine's internal mechanics (validation, gate state, ID allocation, graph sync, governance evaluation, format parsing — DEC-0423's list), the center of gravity for a goal whose object is the Engine. Proposed folding two smaller concerns into existing topics rather than listing them: corpus-format versioning (under export/packaging or artifact model) and team governance config (under collaboration & concurrency). Drafted six Outcomes & Success Criteria: (1) single-sourced paradigm — all paradigm mechanics in exactly one Engine, no surface reimplements paradigm logic (DEC-0423); (2) skill-mode first-class and permanent — agent-chat runtime plus the skills delivers the complete core paradigm, no Application required (DEC-0421, DEC-0433); (3) adoptable — greenfield bootstrap and brownfield fold-in both produce compliant, checker-passing corpora; (4) self-governing — every deployed execution surface documented, contracted, gated by the pipeline it implements, condensing the prior charter's five outcomes (DEC-0335, DEC-0338, DEC-0340, DEC-0341, DEC-0344, DEC-0345); (5) portable across runtimes; (6) deliverable to others. Opened round 3 as three cards: add Engine core (recommended yes); outcomes confirmed as drafted vs adjust; governance outcomes carried forward condensed under outcome 4 (recommended) vs all five verbatim.

### T11 (stakeholder — VERBATIM answers to round 3)

On Engine core: "Yes — list it (Recommended)". On outcomes: "Confirmed as drafted (Recommended)". On governance carry-forward: "Condense under outcome 4 (Recommended)".

### T12 (facilitator)

Presented the complete rechartered BG-0002 draft for review — title "BG-0002: The Groundwork Engine — Core Technology of the Paradigm"; Problem (dogfooding proved the paradigm's value lives in agents and skills working with the methodology; the application-first framing jumped the gun — the Application is mostly a presentation layer around the Engine per DEC-0423; the charter had drifted three times, DEC-0338 → DEC-0346 → DEC-0421/DEC-0422, until it no longer named what the track is: the home of the core technology); Intent (BG-0002 tracks development and refinement of the Groundwork Engine as the core technology and full delivery of the paradigm around it — skill-mode first-class, adoptable, portable, exportable, self-governed; the Application's UI is a layer atop the Engine owned by BG-0001, whose own reframing stays a separate future step per IDEA-0058; stated as intent only); the six confirmed Outcomes; Scope in (the Engine's mechanics and everything delivering the paradigm without the Application) and out (the Application itself — UI, team-facing features, hosting, native reimplementations — BG-0001; re-deciding ratified architecture; BG-0001's reframing); the thirteen-topic anticipated derived-work roster (Engine core; Agents; Skills dual-audience; Artifact model; Modality parity; Adoption-greenfield; Adoption-brownfield; Self-governance; Export/packaging; Runtime portability; Collaboration & concurrency; Human browsing surface; EP-0009 continuing); Constraints carried forward (DEC-0335, DEC-0336, DEC-0337, DEC-0345, DEC-0388, DEC-0423's extraction trigger); solo governance (DEC-0263); Tensions (two coexisting descriptions of artifact handling until native rebuild per DEC-0346/DEC-0422; deliberate breadth with the anticipated-roster pressure valve; human browsing surface near the BG-0001 presentation line, kept because it serves skill-mode users without the app). Also presented the four decisions to distill (recharter superseding DEC-0338; governance subsumed; the epic roster; the skill-mode definition) and the DEC-0267 cascade plan (supersede DEC-0338 with narrowings DEC-0346/0421/0422 carried forward; staleness walk marking EP-0009 and SP-0013–SP-0018 stale with in-session re-affirmation; glossary updates — Method Track rewritten, skill-mode added; consistency sweep + terms; recall audit; re-gate; checker; commit).

### T13 (stakeholder — VERBATIM)

"Please make sure the transcript for this session is detailed. You may even consider using raw transcripts from the chat log."

### T14 (facilitator)

Confirmed the transcript would carry the raw exchanges verbatim (this transcript is the result), verified IDEA-0060's capture on disk, and proceeded to record: decisions, BG-0002 rewrite, supersession of DEC-0338, glossary updates, and the staleness cascade, with the re-gated charter to be presented for approval.

### T15 (facilitator)

Reported decision recording: DEC-0441 (recharter, supersedes DEC-0338), DEC-0442 (governance subsumed), DEC-0443 (thirteen-topic roster), DEC-0444 (skill-mode) all accepted; DEC-0338 superseded; CONTEXT.md gained the skill-mode entry and a rewritten historical Method Track entry; the consistency sweep flagged 24 ratified citers (the expected cascade set) and terms found zero unlinked co-occurrences. Launched the BG-0002 rewrite and staleness walk.

### T16 (stakeholder — VERBATIM)

"Go ahead with the re-affirmations once the walk completes"

### T17 (facilitator)

Cascade results. BG-0002's body was rewritten per the T12 draft with links and cites resynced and the overview rewritten. Two write-API refusals surfaced with sanctioned alternatives: (1) title rename — no API operation targets an existing artifact's title/H1, so the facilitator performed the sanctioned direct repair per the SES-0073 precedent, setting the title/H1 and renaming the file; (2) set-status gated — the approved→gated transition is illegal for gate types (IDEA-0045 precedent): ratification of the rewrite is a fresh approval stamp via the DEC-0267 stale-and-reapprove path, so BG-0002 remained approved with its prior stamp pending stakeholder re-approval. The staleness walk marked EP-0009 and SP-0013 through SP-0017 stale; SP-0018 stayed draft; DEC-0367/DEC-0368 sit outside the stale lifecycle (decisions); nothing in BG-0001's tree was touched. The consistency review found SP-0013 through SP-0017 and BG-0001 CLEAN and EP-0009 SUBSTANTIVE — four present-tense method-track self-descriptions. The five clean spikes were re-affirmed stale→approved with fresh stamps (approved-by awakeinagi, approved-on 2026-07-12) under T16's standing authorization; the full checker passed.

### T18 (facilitator)

Presented EP-0009's four before/after amendment lines (summary lead; bounded context "Method track"; the method-track scope-out rationale; the absorption-trigger line asserting "the method-track pattern" where DEC-0422's surviving term is skill-mode delivery) and asked whether to apply and re-affirm.

### T19 (stakeholder — VERBATIM)

"I think we should broaden the focus of the Epic to more general interaction with the artifacts. Creation, editing, evolution, governence, data capture, where do the interactions happen, who interacts with them, and how, etc. Please help me with the wording here. What term(s) capture these needs best?"

### T20 (stakeholder — VERBATIM)

"Let's update the title of BG-0002 to be more representative"

### T21 (facilitator)

Proposed terminology: the described domain is the artifact lifecycle (creation, editing, evolution, governance) combined with the interaction model (actors, loci, modes); "surface" named only the tooling seam. Flagged the boundary with DEC-0443's anticipated Artifact model epic — keeping EP-0009 to the dynamic side (operations on artifacts through their lifecycle) versus the static type/schema design gives a clean seam. Offered three BG-0002 titles, three EP-0009 names, and a depth choice (recharter the framing lines now and grill the detailed re-scope at EP-0009's own session, versus full re-scope now).

### T22 (stakeholder — VERBATIM answers)

BG-0002 title: "Core Technology & Delivery" (selecting "Groundwork Core Technology — Engine & Delivery of the Paradigm"). EP-0009 name: "Artifact Lifecycle & Interaction (Recommended)". Depth: "Recharter lines now, grill later (Recommended)".

### T23 (facilitator)

Applied both sanctioned direct title repairs (BG-0002 title/H1 set to "Groundwork Core Technology — Engine & Delivery of the Paradigm", file renamed to BG-0002-groundwork-core-technology-engine-delivery-of-the-paradigm.md; EP-0009 frontmatter title set to "Artifact Lifecycle & Interaction", file renamed to EP-0009-artifact-lifecycle-and-interaction.md; no literal path references existed). Proceeded to record the broadening decision and EP-0009's amendments.

### T24 (stakeholder — VERBATIM)

"I'd also like to mention an Epic for observability under BG-0002 if not already captured."

### T25 (facilitator)

Confirmed observability was not on DEC-0443's roster; proposed the mechanics (an extension decision, since accepted decisions are immutable, plus the matching Derived Work line) and the charter gloss "Observability — visibility into the Engine's operation and the corpus's health: audit trails, agent-interaction telemetry, gate/checker metrics, session analytics", with concrete scope grilled at the epic's own derivation. The write queued behind the in-flight transcript task.

### T26 (facilitator)

Reported the consolidation results (DEC-0445 accepted; EP-0009 amended, retitled Artifact Lifecycle & Interaction, and re-affirmed approved; the orphaned DEC-0389 cite cleared by the sanctioned dead-cite repair, with proper re-citation deferred to EP-0009's own refinement session) and the recall-audit outcome: all 20 candidates judged NOT-A-GAP by three Sonnet judge shards — nothing to add, recorded as the audit's outcome; the close call DEC-0019 was ruled narrative-not-normative. Presented the gate: BG-0002's fresh approval stamp, the observability wording, capturing the title-rename API gap as an idea, and the optional DEC-0019 citation.

### T27 (stakeholder — VERBATIM, gate ratification)

On approval: "Approved. And let's add Dogfooding as a topic to the roster as well; this is a core feature of the engine refinement process (NOTE: by people working on the Groundwork project itself, not for people using Groundwork on their own projects). Not sure if it needs its own topic." On observability wording: "As proposed (Recommended)". On the API gap: "Capture it (Recommended)". On DEC-0019: "Leave uncited (Recommended)".

### T28 (facilitator)

Resolved dogfooding as a standalone fifteenth topic — distinct from Self-governance (compliance outcomes) and from Adoption (users applying Groundwork to their own projects) — with the standalone-versus-merge call assessed at derivation via the epic coupling check. Recorded the roster-extension decision (DEC-0446), amended BG-0002's Derived Work, stamped the re-approval, captured the API-gap idea (IDEA-0061), marked IDEA-0058's disposition complete, and closed the session.

## Decisions Produced

DEC-0441 rechartered BG-0002 to make the Groundwork Engine, plus full paradigm delivery, its object of intent — superseding DEC-0338's method-track charter framing while carrying DEC-0346, DEC-0421, and DEC-0422's narrowings forward unchanged. DEC-0442 subsumed the method-track governance charter into the rechartered goal as its self-governance outcome, condensing DEC-0338's five outcomes and their underlying decisions (DEC-0335, DEC-0340, DEC-0341, DEC-0344, DEC-0345) into one, with no separate governance Business Goal created. DEC-0443 set the rechartered goal's anticipated derived-work roster at thirteen epic topics, including EP-0009 continuing as-is. DEC-0444 defined skill-mode as agent-chat delivery of the paradigm through the Groundwork skills, with no Application involved, entering CONTEXT.md as a glossary term. DEC-0445 renamed and broadened EP-0009 to Artifact Lifecycle & Interaction — the dynamic domain of Groundwork artifact creation, editing, evolution, governance interactions, and data capture, including where those interactions happen, who performs them, and how — while leaving the static design of artifact types and their scoping to DEC-0443's anticipated Artifact model epic; the detailed re-scope is deferred to EP-0009's own refinement session.

## Conflicts Raised

None yet.
