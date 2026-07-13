---
id: SES-0089
type: session
title: "Epic derivation for BG-0002 — Groundwork Core Technology, Engine & Delivery of the Paradigm"
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-12
participant: awakeinagi
participant-role: stakeholder
facilitator: Claude (Fable 5)
transcript-fidelity: reconstructed
kind: full
intake: {origin: user, proposed-by: awakeinagi}
overview: >-
  This session runs the epic-derivation pipeline step for BG-0002
  (Groundwork Core Technology, Engine & Delivery of the Paradigm).
  After stakeholder proposal, a system-architect consultation, and
  two grilling rounds settling the portability, checker-seam,
  customization, and artifact-model-stability questions, the
  stakeholder ratified the derived set and ten resulting decisions
  (DEC-0462 through DEC-0471). Derivation is now complete: seven
  epics (EP-0010 through EP-0016) drafted with reciprocal impact
  edges, EP-0009 continuing, and BG-0002's Derived Work section
  updated. The cross-epic coupling check found no mutual coupling;
  the deliverable-coverage pass found no gap. A decision-recall
  audit produced eleven findings, all dispositioned by the
  stakeholder and applied: eight missing-citation additions, one
  scope-collision risk entry, one weak-cite fold, and one recorded
  skip (DEC-0348 to EP-0011). BG-0002 and EP-0009 were re-affirmed
  as approved after byte-verified diff review (additive bookkeeping
  only). Before the three ratified process ideas were captured, the
  facilitator found the first — the grilling-affordance notes-
  preview idea — already resolved corpus-side by the parallel
  SES-0090 (DEC-0472 through DEC-0474), so it was recorded as
  obviated rather than captured; IDEA-0064 and IDEA-0065 were
  captured as proposed. Final integrity checker: OK, 746 artifacts,
  graph sound. Status: closed.
links:
  relates-to: [BG-0002, DEC-0462, DEC-0463, DEC-0464, DEC-0465, DEC-0466, DEC-0467, DEC-0468, DEC-0469, DEC-0470, DEC-0471, IDEA-0064, IDEA-0065]
---

# SES-0089: Epic derivation for BG-0002 — Groundwork Core Technology, Engine & Delivery of the Paradigm

## Purpose

This session derives the draft Epic set from the approved business goal
BG-0002 (Groundwork Core Technology, Engine & Delivery of the Paradigm,
rechartered in SES-0085). It covers seam selection, the draft epics with
impacts/impacted-by edges, the cross-epic coupling check, the
deliverable-coverage pass, and the update of BG-0002's Derived Work section.

## Transcript

### T1

Stakeholder (verbatim proposal): "Let's derive Epics for BG-0002"

### T2

Facilitator (restatement): "I restated the intent as: take the next
pipeline step for BG-0002 — Groundwork Core Technology, Engine & Delivery
of the Paradigm — by deriving its draft Epic set: slice the goal along
real domain seams (never architectural layers), draw impacts/impacted-by
edges with prose justification in each impactor's body, run the
cross-epic coupling check and the deliverable-coverage pass, update
BG-0002's Derived Work section in the same edit, and present the draft
set for ratification — each epic then refined in depth in its own later
session, in impact order. Alignment was requested before proceeding."

### T3

Facilitator: Reported the locate-first grounding: BG-0002 approved with
no blockers; EP-0009 the sole derived epic; fifteen anticipated topics
per DEC-0443/DEC-0446; two pre-flagged derivation questions
(Dogfooding-vs-Self-governance merge, static artifact-model placement
per DEC-0445). Stakeholder confirmed alignment to proceed.

### T4

Facilitator (system-architect consultation per DEC-0292/DEC-0293/DEC-0296):
Ran the dual-instance advisor debate — one record-grounded instance
(packet: BG-0002 body, DEC-0441..DEC-0446, DEC-0420..DEC-0423 delineation,
constraints) and one best-practice-independent instance (no record, no
roster). Initial positions: eight epics (record-grounded) vs six
(independent). Two rebuttal rounds converged on: Engine Core & Artifact
Model merged as the foundation; Agents+Skills one delivery-surface epic;
Adoption one epic (greenfield+brownfield); Self-Governance & Dogfooding
merged and standalone from Adoption; Collaboration+Concurrency absorbing
the human browsing surface; Observability standalone; Export/Packaging
left underived on the roster with a first-third-party-consumer trigger.
One documented disagreement survived: Runtime Portability & Modality
Parity standalone vs folded into Agent & Skill Surfaces — both instances
reversed positions across the rounds (a genuinely balanced call). The
joint verdict was presented to the stakeholder as a proposal with the
portability question flagged for arbitration.

### T5

Stakeholder: Began grilling. (Procedural note, faithful to the exchange:
the stakeholder reported the AskUserQuestion notes affordance was
missing on plain cards; investigation established notes require the
preview side-by-side layout — an undocumented conditionality
contradicting DEC-0461's "native in Claude Code" premise. Queued for the
close-out ideas check. Subsequent question cards carried previews.)

### T6

Facilitator: Grilling round 1: (a) ratify the converged set; (b)
arbitrate portability; (c) the checker-seam boundary both architect
instances flagged as the sharpest open question.

### T7

Stakeholder: Settled the checker seam: one checker, Engine-hosted —
Self-Governance defines which rules exist and their policy, Engine Core
owns the machinery running all rule families. On the set and
portability: noted the need for an epic to track support for different
agent-chat interfaces (non-app use: Claude Code, GitHub Copilot, Codex,
OpenCode, and similar) and asked to discuss portability further before
locking in.

### T8

Facilitator: Presented the portability discussion: the work is the
runtime survey spike, thin per-runtime adapters/translations, a parity
contract with documented degradation (precedent: SES-0088's
elaborate-keyword fallback for harnesses lacking notes), and modality
parity reducing largely to "every consumer consumes the same Engine"
per DEC-0423. Trade-off presented: standalone gives sponsor-level
tracking, own gate/Risks/derived work, 1:1 mapping to outcome 5, at the
cost of a permanent heavy impacts edge from Agent & Skill Surfaces;
folded saves a gate but buries runtime support at story level.
Recommended standalone given the stakeholder's stated tracking need,
with the boundary caveat: the epic consumes canonical skill/agent
definitions, owns translations/adapters/parity proof, never redefines
skill expression; spike first; fold-back if trivial.

### T9

Stakeholder: "Yes, standalone with that boundary caveat works."

### T10

Facilitator: Grilling round 2: formal set ratification; reference-runtime
vs equal-peers for the parity contract; third-party customization
posture; artifact-model stability posture.

### T11

Stakeholder: Deferred the reference-runtime call to the portability
epic's refinement, post-spike, carried in its Risks & Open Questions.
Chose the evolving artifact-model posture (schema migration and
backward compatibility first-class Engine Core scope). On
customization: opinionated for now, potentially up for debate in the
future, deferred until requested by users. On ratification: asked
whether translating a Claude Code agent config markdown to a different
markdown format for GitHub Copilot or another harness poses an issue,
noting core agent logic stays the same except where one harness
doesn't support another's features.

### T12

Facilitator: Answered: no issue — that is exactly the standalone
epic's chartered work; canonical definitions live in Agent & Skill
Surfaces, translations in the portability epic, ideally generated or
drift-checked against the canonical form per outcome 1
single-sourcing; capability gaps are the parity contract's
documented-degradation territory. Re-presented ratification and a
confirmation of the customization reading: opinionated-and-fixed now,
explicitly re-openable when adopters request flexibility.

### T13

Stakeholder: Ratified the set of seven new epics plus EP-0009
continuing with Export/Packaging underived; confirmed the
customization reading.

### T14

Facilitator: Played back the ten decisions in plain language and
proposed the sibling impact edges (one-way fan-out from Engine Core;
EP-0009 → Agent & Skill Surfaces and Collaboration; Agent & Skill
Surfaces → Portability and Adoption; Self-Governance & Dogfooding →
Observability; no mutual edges), noting EP-0009 and BG-0002 as approved
artifacts requiring touch (Derived Work per DEC-0246; EP-0009 edge
re-affirmation at gate).

### T15

Stakeholder: Confirmed all ten decisions and ratified the impact edges.

### T16

Facilitator: Reported the drafting execution: EP-0010 (Engine Core & Artifact Model), EP-0011 (Agent & Skill Surfaces), EP-0012 (Runtime Portability & Modality Parity), EP-0013 (Adoption), EP-0014 (Self-Governance & Dogfooding), EP-0015 (Collaboration, Concurrency & Browsing), EP-0016 (Observability) created as drafts with the ratified reciprocal impact edges and DEC-0249 prose; BG-0002's Derived Work section updated in the same edit per DEC-0246 (listing all eight members and the Export/Packaging remaining-anticipated line per DEC-0467) with overview and cites refreshed; EP-0009 given its reciprocal edges, one explanatory paragraph, and the DEC-0462 cite; full checker OK at 741 artifacts.

### T17

Facilitator: Ran the mechanical cross-epic coupling check (DEC-0196/DEC-0199) over the eight-member sibling set. Verbatim verdict: no mutual (bidirectional) coupling — clear; 12 one-directional impact edges across 12 pairs, density 43% of 28 possible pairs; fan-out led by EP-0010 at 7/7 siblings (informational, expected of a foundational epic); zero findings to review.

### T18

Facilitator: Ran the deliverable-coverage pass: all six BG-0002 outcomes and all fifteen DEC-0443/DEC-0446 roster topics map to the derived set — outcome 6 (deliverable to others) deliberately underived per DEC-0467 as its recorded disposition; the structural/cross-cutting miss check found no uncovered deliverable. Outcome recorded: checked, no gap found.

### T19

Facilitator: Ran the decision-recall audit: 63 unique accepted-decision candidates across the seven drafts, judged by eight Sonnet 5 batch judges. Eleven findings: eight strong missing-citation findings (DEC-0080→EP-0010; DEC-0340→EP-0011; DEC-0433→EP-0012; DEC-0019, DEC-0263→EP-0014; DEC-0244, DEC-0030, DEC-0427→EP-0015), one scope-collision finding (DEC-0121's port assignments to BG-0001's EP-0004/EP-0007 overlapping EP-0010's graph/search claims), one weak fold (DEC-0310 into EP-0015's SP-0018 seam note), one recorded skip (DEC-0348→EP-0011, wrong altitude). Judges also flagged: the EP-0014/EP-0015 governance-config seam unnamed; the audit packet missing its embedded overviews; retrieval unfiltered by BG lineage; and the coupling check not yet visible in this transcript at judging time (resolved by T17's record).

### T20

Stakeholder: Ratified all audit dispositions as proposed; re-affirmed BG-0002 and EP-0009 as approved after reviewing the byte-verified diff summaries (additive derivation bookkeeping only — no scope, contract, or deliverable changed in either); approved capturing the session's three process ideas, adding none further.

### T21

Facilitator: Applied the ratified audit dispositions as eight edit-section/add-cite pairs plus one recorded skip across the seven draft epics — EP-0010 gained the DEC-0080 static-artifact-model mention and a new DEC-0121 port-ownership-overlap risk entry (overview refreshed to match); EP-0011 gained the DEC-0340 agent-contract mention; EP-0012 gained the DEC-0433 modality-parity mention; EP-0014 gained the DEC-0019 and DEC-0263 dogfooding/governance-variant mentions; EP-0015 gained the DEC-0244, DEC-0030, and DEC-0427 mentions and the DEC-0310 fold into its SP-0018 seam note; EP-0014 and EP-0015 gained the matching governance-configuration seam line named in each Interfaces section; DEC-0348→EP-0011 was left unedited, recorded skip. All edits landed clean; the full checker's own post-edit run surfaced two additional cites-sync gaps on the newly written seam prose (EP-0014 referencing DEC-0443, EP-0015 referencing DEC-0469) not caught by the audit itself, both closed with follow-up add-cite calls. Before capturing the three process ideas the stakeholder approved at T20, the facilitator checked the corpus and found the first — the grilling-affordance notes-preview idea — already resolved: SES-0090 (run in parallel) settled it directly, superseding DEC-0460 and DEC-0461 with DEC-0472 (preview-layout cards), DEC-0473, and DEC-0474. That idea was recorded as obviated rather than captured. IDEA-0064 (recall-audit judge packets must be self-sufficient) and IDEA-0065 (BG-lineage filter for recall-audit retrieval) were captured as proposed, both derived from and relating to this session. The full integrity checker reports OK: 746 artifacts, graph is sound (19 pre-existing story-coverage warnings unrelated to this session's edits).

## Decisions Produced

Ten decisions, all accepted in-session (T15): DEC-0462 (the set of seven
new epics plus EP-0009), DEC-0463 (Dogfooding merges into
Self-Governance), DEC-0464 (the static artifact model lands in Engine
Core), DEC-0465 (Adoption is one epic), DEC-0466 (Runtime Portability &
Modality Parity is standalone, with a strict consumer boundary),
DEC-0467 (Export/Packaging stays underived; trigger is the first
third-party consumer), DEC-0468 (the human browsing surface folds into
Collaboration & Concurrency), DEC-0469 (one checker, Engine-hosted),
DEC-0470 (customization posture: opinionated-and-fixed, re-openable on
demand), and DEC-0471 (the artifact model is evolving; migration is
first-class Engine Core scope).

## Conflicts Raised

None yet.
