---
id: DEC-0339
type: decision
title: One method epic — the Artifact Interaction Surface — with two component contracts
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0059 @ T10-T11, T19"
overview: >-
  One epic derives from BG-0002 now: the Artifact Interaction
  Surface — artifact-librarian plus artifact-interact, built and
  gated together per DEC-0334 — with two Component Docs beneath it
  because the two artifacts answer to different consumer sets (the
  skill to the librarian and DEC-0327-chartered agents; the
  librarian to all agents per DEC-0325). Runtime/capability
  configuration is a mandatory contract section inside each CMP, not
  an epic — the architect debate's convergent verdict: the tool-
  grant bug marks a real change axis at contract granularity, but a
  config epic could never gate independently. The
  distribution/packaging seam (DEC-0319 install scripts, the
  IDEA-0010 plugin) is named in BG-0002 with its epic deferred to
  IDEA-0010's take-up.
links:
  derives-from: [SES-0059]
  relates-to: [DEC-0334, DEC-0338, DEC-0327, DEC-0325, DEC-0311, DEC-0292, DEC-0194, IDEA-0010]
---

# DEC-0339: One Method Epic — the Artifact Interaction Surface, Two CMPs

## Context

Epic slicing for the method track was debated by both architect
instances (T10): three change-axis seams (delegation surface, core
CLI, runtime/packaging config) versus one epic honoring DEC-0334's
one-deliverable coupling. The best-practice instance conceded its
third seam could not gate independently — by its own seam-rent test.

## Decision

One method epic derives from BG-0002 now: the Artifact Interaction
Surface — the artifact-librarian agent and the artifact-interact
skill, built and gated together per DEC-0334 — with TWO Component
Docs beneath it, one per artifact, because they serve different
consumer sets (the skill's consumers are the librarian and
DEC-0327-chartered agents; the librarian's consumers are all agents
per DEC-0325). Runtime/capability configuration is a mandatory
CONTRACT section within each CMP (DEC-0340), not an epic. The
distribution/packaging seam (install scripts, the IDEA-0010 plugin)
is named in BG-0002 as a future epic but derives only when IDEA-0010
is taken up — chartering an epic from an undisposed Idea would invert
the intake order.

## Rationale

Separate epics for skill and agent would fight DEC-0334's ratified
coupling; one CMP for both would hide that their contracts answer to
different consumers. The bug's change-axis evidence (the grant
drifted while operation semantics held) is real but lives at contract
granularity — a config epic that always gates with the surface epic
is coupling with extra ceremony.

## Alternatives Considered

- **Three epics** (best-practice opening position) — the config epic
  fails independent-gate cadence; conceded in rebuttal.
- **Distribution epic now** — inverts intake for IDEA-0010; rejected.

## Implications

After BG-0002 approval: derive the epic, run its refinement session
(system-architect advisor moment is REQUIRED at epic level,
DEC-0292), then the two backfill CMPs per DEC-0342. The DEC-0194
deliverable-coverage pass runs at the epic set's gate.
