---
id: SES-0075
type: session
title: "Idea capture: frontmatter validation at create; --amend marks approved artifacts stale"
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-12
participant: awakeinagi
participant-role: stakeholder
facilitator: "Claude (Fable 5)"
transcript-fidelity: reconstructed
kind: idea-capture
intake:
  origin: agent
  proposed-by: awakeinagi
overview: >-
  Idea-capture micro-session (DEC-0258) recording two tooling-defect
  ideas surfaced by the SES-0073 aftermath analysis. First: write
  create accepts --field frontmatter values with no validation
  against the type's SPEC, which is how SES-0073 was created with an
  invalid transcript-fidelity value and list-valued participant
  fields that nothing caught until a human read the spec directly.
  Second: edit-section/delete-section --amend edits leave an
  approved artifact's status unchanged at approved, so its approval
  stamp silently covers content the approver never saw -- the reason
  SP-0016 needed a manual stale-then-reapprove during the SES-0073
  close-out, and why an illegal approved-to-gated transition was
  attempted first (no sanctioned move existed for a materially-
  changed approved artifact). Stakeholder approved capturing both as
  ideas ('Yes add those ideas'). Zero decisions produced (valid per
  DEC-0258).
links:

  relates-to: [IDEA-0044, IDEA-0045]
---

# SES-0075: Idea capture: frontmatter validation at create; --amend marks approved artifacts stale

## Purpose

Capture two tooling-defect ideas surfaced by the SES-0073 aftermath analysis: create's lack of type-aware frontmatter validation, and the lack of any re-approval mechanism when an --amend edit touches an already-approved artifact.

## Transcript

**T1 — Facilitator.** Presented two root-cause findings from the SES-0073 aftermath analysis. (a) `write create` accepts `--field` values with no validation against the type's SPEC — this is how SES-0073 was born with `transcript-fidelity: paraphrased` (not a valid enum value) and list-valued `participant` fields, and nothing caught either until a human read the spec by hand. (b) `--amend` edits leave an approved artifact's status as `approved`, so its `approved-on` stamp silently covers content the approver never actually saw — this is why SP-0016 needed a manual stale-then-reapprove during the SES-0073 close-out, and why the illegal approved-to-gated transition was attempted in the first place: the lifecycle offered no sanctioned move for "this approved thing changed materially."

**T2 — Stakeholder (awakeinagi).** "Yes add those ideas."

**T3 — Facilitator.** Captured both findings as ideas: IDEA-0044 (type-aware frontmatter validation at create time and in the checker) and IDEA-0045 (amending an approved artifact marks it stale: approval must re-cover amended content). Both derive from this session and relate to each other as findings from the same SES-0073 aftermath incident.

## Decisions Produced

None.

## Conflicts Raised

None.
