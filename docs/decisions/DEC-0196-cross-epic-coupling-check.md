---
id: DEC-0196
type: decision
title: A cross-epic impact-coupling check is required at epic derivation
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Adds scripts/groundwork_epic_coupling.py to flag mutual (bidirectional)
  impacts coupling between sibling epics as a candidate for re-seaming.
  Run immediately after draft epic set's impact edges are drawn, before
  deep refinement. One-directional fan-out reported as context only;
  bounded-context slicing routinely produces legitimate heavy one-way
  fan-out. Advisory only, never auto-blocking. Constrains Epic playbook
  and SKILL.md. Status accepted.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0036 @ T3-T4"
links:
  derives-from: [SES-0036]
  relates-to: [DEC-0195, DEC-0197, DEC-0026, DEC-0027]
  supersedes: []
---

# DEC-0196: A Cross-Epic Impact-Coupling Check Is Required at Epic Derivation

## Context

The stakeholder wanted mechanical detection of bad epic splits before
deep refinement burns time on them. Groundwork already tracks cross-epic
coupling via `impacts`/`impacted-by` edges
(DEC-0026,
DEC-0027), but nothing read
that graph back for split quality.

## Decision

A new pure-stdlib script, `scripts/groundwork_epic_coupling.py`, is
added to the skill. Run immediately after a draft epic set's impact
edges are drawn — before any epic is refined in depth — it flags
**mutual** (bidirectional) `impacts` coupling between sibling epics as a
candidate for re-seaming. One-directional fan-out is reported as context
only, never as a finding: bounded-context slicing (per
DEC-0195's sixth seam)
routinely produces heavy one-way fan-out from foundational epics without
indicating a bad split. The check is advisory only — findings are
reviewed and dispositioned in-session, never auto-blocking, consistent
with refinement-process.md's existing "cycles are normal" guidance.

## Rationale

A first design used a fan-out-ratio threshold instead of a
mutual-coupling-only signal. Smoke-tested against this project's own
approved 7-epic set, it flagged 67-100% coupling density on *every*
epic — pure noise, since foundational bounded-context epics (the
Artifact Store, Governance) are legitimately referenced broadly by
design. Mutual coupling is the signal that survived validation: it found
exactly the three cycles
(EP-0001↔EP-0003,
EP-0001↔EP-0005,
EP-0002↔EP-0006)
already documented as known, deliberate cycles in
SES-0002, with zero
false positives.

## Alternatives Considered

- **A density/ratio threshold on total fan-out**: rejected after the
  smoke test showed it can't distinguish a bad technical-layer split
  from normal foundational-epic fan-out in bounded-context-sliced
  systems; a noisy check trains facilitators to ignore its warnings.
- **A blocking check (nonzero exit on findings)**: rejected — contradicts
  the existing "cycles are normal" guidance; must stay advisory like the
  consistency sweep/terms checks and the decision-recall audit.

## Implications

`refinement-process.md`'s Epic playbook and `SKILL.md` gain a required
step citing this script; `epic-slicing-seams.md` documents its usage and
the split-vs-merge signals it feeds
(DEC-0197).
