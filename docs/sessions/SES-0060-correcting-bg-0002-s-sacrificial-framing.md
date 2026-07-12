---
id: SES-0060
type: session
title: "Correcting BG-0002's sacrificial framing"
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-10
participant: awakeinagi
participant-role: stakeholder
facilitator: Claude Code (Fable 5)
transcript-fidelity: reconstructed
overview: >-
  Change-intake session correcting BG-0002's "sacrificial by design"
  framing, surfaced mid-derivation of the Artifact Interaction
  Surface epic. BG-0002/DEC-0338 stated this track's tooling is
  decommissioned once BG-0001's application absorbs its functions;
  the stakeholder corrected this — the delegation/contract pattern
  this track establishes is permanent and BG-0001's application will
  implement it natively, inheriting the already-gated contracts.
  Only today's specific implementation (a CLI script plus a Claude-
  Code-specific subagent) may later be rebuilt natively. Produced
  DEC-0346, narrowing (not superseding) DEC-0338; edited BG-0002's
  Conflicts & Tensions section accordingly. Also captured IDEA-0013
  (a paradigm export mechanism for using Groundwork outside the
  Groundwork application, relating to IDEA-0010, plugin as first-
  hypothesis vehicle), parked per the focus-artifact test. Staleness
  sweep found no other ratified artifact referencing the sacrificial
  framing needing correction. Method-level change to an approved
  artifact; resolved fully in-session per DEC-0267.
links:
  relates-to: [BG-0002, DEC-0338, DEC-0267, DEC-0260, DEC-0259, IDEA-0010, DEC-0339, DEC-0346]
---

# SES-0060: Correcting BG-0002's Sacrificial Framing

## Purpose

Change-intake session correcting BG-0002's "sacrificial by design"
framing, surfaced mid-derivation of the Artifact Interaction Surface
epic (the epic DEC-0339 charters under BG-0002, not yet created).
BG-0002's Conflicts & Tensions section and DEC-0338 state this track's
tooling is decommissioned once BG-0001's application absorbs its
functions. The stakeholder corrected this: the delegation/contract
pattern this track establishes is a permanent design decision that
BG-0001's application will implement natively — not a throwaway. Only
the current implementation (a CLI script plus a Claude-Code-specific
subagent) may later be swapped for a native-application equivalent;
the pattern and its already-gated contracts are inherited, not
discarded. Narrows DEC-0338 (does not supersede it — the charter's
predicate, non-goals, and outcomes stand unchanged). Also captured
IDEA-0013 (paradigm export mechanism for use outside the Groundwork
application, relating closely to the existing plugin-packaging idea
IDEA-0010, parked for a future session per the focus-artifact test
and its idea/deferred-story boundary, DEC-0259/DEC-0260). Must fully
resolve before the epic-derivation session opens next (DEC-0267:
modifications to an approved artifact complete their cascade
in-session). Method-level change; touches BG-0002 (approved).

## Transcript

**T1 — Stakeholder.** Verbatim, given mid-grilling on the pending
epic's absorption-mapping question: "Actually, this agent and skill will
also be a part of the main application. What we do need to define is
agents and skills exporting mechanism for using the Groundwork
paradigm outside of the Groundwork application. Add this as an idea
to grill deeply on in a future session. My first thought is that the
plugin will be the export vehicle."

**T2 — Facilitator.** Restatement: BG-0002 and DEC-0338 currently say
this tooling is sacrificial — decommissioned once BG-0001's
application absorbs its functions. That's wrong: the librarian and
skill (or their design pattern) are meant to become part of the main
application, not be thrown away. Flagged this as a correction to an
approved artifact requiring in-session cascade resolution (DEC-0267);
separated the export-mechanism thought as a park-worthy tangent per
the focus-artifact test (DEC-0260) — different artifact, future
session. Round: (a) install-script scope under BG-0002's own
predicate; (b) how much of the sacrificial framing is wrong — nothing
temporary at all, vs. the pattern persists while today's specific
implementation may still be rebuilt natively; (c) defect-tracking
type shape for the pending epic's backfill divergence-disposition
mechanics; (d) session structuring — fold the correction into the
pending epic's session, or split into two.

**T3 — Stakeholder.** (a) Install script: in scope anyway — contract
it now, despite not strictly meeting the corpus-touching predicate.
(b) The pattern persists, implementation may still change — the
delegation/contract approach is the permanent design; today's
CLI-plus-subagent implementation might still be rebuilt natively once
the application exists, but that's an implementation swap, not
disposal of the pattern. (c) Fuller defect type: severity plus a
multi-state status workflow. (d) Two sessions — fix BG-0002 first,
close it, then a fresh session for the pending epic.

**T4 — Facilitator.** Close. This session (SES-0060) resolves only the
BG-0002 correction and the IDEA-0013 capture; the install-script scope
decision and the defect-type design belong to the pending epic's own
derivation session and will be recorded there, using the corrected
BG-0002 as its foundation.

### Post-Close Enrichment (2026-07-10)

Recall-audit disposition: nothing to add from the candidate sweep. Two contract-gap findings addressed: (1) SES-0060's body substantively names DEC-0339 but it was missing from relates-to — fixed via add-link enrichment. (2) A facilitator drafting error (the replacement content for BG-0002's Conflicts & Tensions section repeated the section heading, which edit-section also auto-preserves) produced a duplicate heading in BG-0002; the write API has no operation to target one occurrence among duplicate headings or delete a stray heading line, so the librarian correctly declined to freehand-fix it and reported the gap. The stakeholder authorized a one-off manual correction outside the typed write API to remove the stray heading, explicitly as a named exception rather than a precedent; the facilitator performed it directly. IDEA-0014 captured: a future session should design an occurrence-index parameter for edit-section, or a dedicated section-repair/delete operation, so this class of defect never again requires bypassing DEC-0312.

## Session Close

- **Classification:** method-level correction to an approved artifact
  (BG-0002); narrows DEC-0338 without superseding it.
- **Produced:** DEC-0346 (narrows DEC-0338); BG-0002 Conflicts &
  Tensions edited; IDEA-0013 captured.
- **Staleness:** per the locate-first sweep, no other ratified
  artifact cited DEC-0338's sacrificial clause or referenced
  "sacrificial" — no wider staleness walk required beyond BG-0002
  itself.
- **IDEA-0013's relation to IDEA-0010:** IDEA-0013 (the export
  mechanism) and IDEA-0010 (the plugin) are closely related but
  distinct — IDEA-0010 is about packaging skills and agents as a
  unit; IDEA-0013 is about what "export to a non-Groundwork-app
  project" requires beyond packaging (versioning, update propagation,
  fork-vs-track semantics). A future take-up session should consider
  both together, per the idea/deferred-story boundary DEC-0259 sets
  and the focus-artifact test DEC-0260 applies.
- **Deferred to the epic-derivation session next:** install-script
  contract scope; defect-tracking artifact-type design.

## Decisions Produced

- DEC-0346 — the method track's delegation/contract pattern is
  permanent; only the current implementation may be swapped, narrowing
  DEC-0338's sacrificial framing

## Conflicts Raised

None.
