---
id: DEC-0194
type: decision
title: Epic derivation requires an explicit deliverable-coverage pass
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Requires an explicit deliverable-coverage pass before finalizing a
  draft epic set. Extract every deliverable named in goal's Decision/
  Scope and System Context sections, confirm each maps to at least one
  derived epic. Explicitly watch for structural and cross-cutting
  deliverables that read as generic connective tissue and get silently
  treated as covered by the union of domain epics. Mirrors existing
  Component Doc graduation-review discipline: citing a rule is not
  applying it. Constrains Epic playbook. Status accepted.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0035 @ T9-T10"
links:
  derives-from: [SES-0035]
  relates-to: [DEC-0190]
  supersedes: []
---

# DEC-0194: Epic Derivation Requires an Explicit Deliverable-Coverage Pass

## Context

Root cause of the missing backend-platform epic: nobody checked, at
epic-derivation time, whether every deliverable named in
BG-0001 (including
DEC-0001's "backend services") had
an owning epic. Domain-first (DDD bounded-context) decomposition naturally
produces domain epics and never surfaces structural/cross-cutting
deliverables like a composition root or API layer — it answers "what does
it do," never "what makes it a running program."

## Decision

Before finalizing a draft epic set, run a required **deliverable-coverage
pass**: extract every deliverable named in the goal's Decision/Scope text
and System Context section (per
DEC-0190), and confirm each maps
to at least one derived epic. Explicitly watch for structural/
cross-cutting deliverables that read as generic connective tissue and get
silently treated as covered by the union of domain epics. Record the
pass's outcome explicitly, even "checked, no gap found."

## Rationale

Mirrors the existing Component Doc graduation-review discipline: citing a
rule is not the same as applying it — the checklist must be walked
item-by-item at the stage it governs. This directly targets the failure
class that produced this session's retrospective.

## Alternatives Considered

- **Rely on the new System Context section alone to prevent future
  gaps**: rejected — System Context improves the goal's own completeness
  but doesn't itself force epic derivation to check coverage; a
  well-specified goal could still fail to translate into a complete epic
  set without an explicit pass.

## Implications

`references/refinement-process.md`'s Epic playbook gains the required
pass. Applies retroactively as a sanity check the next time this
project's own epic set is reviewed — motivating `EP-0008`'s eventual
derivation, still pending.
