---
id: SES-0036
type: session
title: Epic-slicing seam guidance, coupling check, and split-vs-merge heuristics
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Introduced six vertical-slicing seams for epic decomposition: Access,
  Timeline, Protocol, Integration, Sophistication, and Bounded-Context/
  Domain-Capability. Corrected "horizontal slicing" terminology to
  "vertical slice" (convention: vertical = through all layers on
  business seam). Drafted groundwork_epic_coupling.py to check
  bidirectional impacts, treating mutual coupling as actionable,
  one-way fan-out as informational. Zero false positives on project's
  own epic set. Documented split-vs-merge heuristics grounded in impact
  edges. Updated refinement-process.md and SKILL.md. Produced
  DEC-0195-DEC-0197.
participant: awakeinagi@gmail.com
participant-role: stakeholder
facilitator: Claude Sonnet 5 (claude-sonnet-5) via Claude Code CLI
transcript-fidelity: reconstructed
links:
  relates-to: [SES-0035]
---

# SES-0036: Epic-Slicing Seam Guidance, Coupling Check, and Split-vs-Merge Heuristics

## Purpose

Continuation of the goal-template redesign work
(SES-0035), turning to the next gap
identified there: the Epic derivation playbook asked "boundaries between
epics" as a question but gave no concrete method for finding good ones.
The stakeholder proposed a set of business/domain slicing heuristics for
discussion before any edits were made.

## Transcript

**T1 — Stakeholder.** Proposed epic-slicing guidance: "Horizontal
Slicing" across business, operational, or architectural seams, with five
named seams (Access, Timeline, Protocol, Integration, Sophistication),
each with a Rule and Examples. Warned against technical-layer epics
("Database Changes," "Frontend Components," "Stripe Integration") as the
anti-pattern that bottlenecks everything until every layer-epic is
(mostly) done.

**T2 — Facilitator.** Flagged a terminology inversion against standard
usage (Cockburn's "Elephant Carpaccio," SAFe): "vertical slice" is the
conventional term for cutting through all architectural layers along a
business seam (the good pattern proposed); "horizontal/layer slice" is
the conventional term for the DB/Frontend/Stripe anti-pattern being
warned against. Validated the five seams against this project's own
epics: the Integration Seam matches
EP-0005's isolation of
Jira/code-host/auth risk; the Protocol Seam's "Core Platform Engine & API
Foundation" example is nearly verbatim the still-pending `EP-0008`
identified in SES-0035. Caveated
the Sophistication Seam: baseline error
handling belongs in the core epic (definition-of-done), not deferred —
only genuinely advanced hardening should get its own epic, tying to
DEC-0191.
Proposed a sixth seam, Bounded-Context/Domain-Capability, since that's
what EP-0001..EP-0007
actually used and the given five skew toward customer-facing product
decomposition. Proposed tying seam quality to the existing
`impacts`/`impacted-by` mechanism
(DEC-0026,
DEC-0027) as a
self-check, and cautioned that stacking a six-seam checklist on top of
DEC-0194's
coverage pass risks over-fragmenting small goals. Proposed placement in a
new `references/epic-slicing-seams.md`.

**T3 — Stakeholder.** Approved the terminology fix — "Vertical Slicing."
Approved adding the Bounded-Context/Domain-Capability seam in the same
Rule-and-Examples format. Directed that a script be added to the skill to
check cross-epic impacts, wired into the Epic creation workflow so bad
splits are caught before further refinement is spent on them. Directed
explicit "no fixed epic count" guidance plus concrete split-vs-merge
heuristics.

**T4 — Facilitator.** Drafted `scripts/groundwork_epic_coupling.py`
(pure stdlib, mirroring `groundwork_consistency.py`'s frontmatter-parsing
conventions), computing mutual (bidirectional) `impacts` coupling between
sibling epics per goal. Smoke-tested against this project's own approved
epic set: a first design using a fan-out-ratio threshold flagged nearly
every epic (67-100% density) as "broad coupling" — pure false-positive
noise, because bounded-context slicing inherently produces heavy one-way
fan-out from foundational epics (the Artifact Store, Governance), which
is expected, not a defect. Redesigned the check to treat mutual coupling
as the only actionable finding and one-directional fan-out as
informational context. Re-tested: found exactly the three mutual pairs
(EP-0001↔EP-0003,
EP-0001↔EP-0005,
EP-0002↔EP-0006)
already documented as known, deliberate cycles in
SES-0002 — a clean validation against
real project history, zero false positives. Fixed a density-percentage
display bug (exceeding 100%) surfaced during testing, caused by dividing
a directed-edge count by an undirected-pair count.

**T5 — Facilitator.** Wrote `references/epic-slicing-seams.md`
(vertical-vs-horizontal framing; the six seams in Rule/Examples/Why
format; explicit no-fixed-count guidance with concrete split-vs-merge
signals referencing the coupling check in both directions). Wired the
coupling check and the seam catalog into `refinement-process.md`'s Epic
derivation playbook (required step, positioned right after impact edges
are drawn and before individual epic refinement) and into `SKILL.md`
(reference-map row, dedicated required-step paragraph mirroring the
existing consistency-check paragraph).

## Decisions Produced

DEC-0195,
DEC-0196,
DEC-0197

## Conflicts Raised

None.
