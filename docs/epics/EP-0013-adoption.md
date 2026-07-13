---
id: EP-0013
type: epic
title: "Adoption"
status: draft
owner: awakeinagi@gmail.com
created: 2026-07-13
overview: >-
  Adoption tracks BG-0002's outcome that greenfield bootstrap and
  brownfield fold-in both produce compliant, checker-passing
  corpora, merged into one epic by DEC-0465. In scope: greenfield
  bootstrap workflows; brownfield fold-in and migration of pre-
  existing projects; compliance verification against the Engine's
  checker; adopter onboarding documentation; the
  greenfield/brownfield distinction lives at story level, not epic
  level. Out of scope: export/packaging for third parties (an
  underived roster topic per DEC-0467) and customization/extension
  points (adopters get the standard corpus shape; DEC-0470 draws a
  firm, on-demand-reopenable line). No outgoing impact edges among
  current siblings; impacted-by Engine Core & Artifact Model and
  Agent & Skill Surfaces. Open risks: implementation stories block
  on Engine Core & Artifact Model's compliance definition
  stabilizing, though research spikes may run earlier; what
  brownfield fold-in actually looks like for a real pre-existing
  repo is a candidate spike; corpus-compatibility promises depend on
  the Engine's migration mechanism (DEC-0471). Derives from BG-0002;
  draft status pending its own refinement session.
links:
  impacted-by: [EP-0010, EP-0011]
  derives-from: [BG-0002]
cites: [DEC-0462, DEC-0465, DEC-0470, DEC-0471, DEC-0443, DEC-0467]
---

# EP-0013: Adoption

## Summary

BG-0002's outcome that greenfield bootstrap and brownfield fold-in
both produce compliant, checker-passing corpora, tracked as one epic
per DEC-0465.

## Why (Goal Alignment)

BG-0002 requires the paradigm be adoptable by both greenfield and
brownfield projects. DEC-0465 merged what could have been two epics
into one, since both paths converge on the same compliance definition
and the same checker verification. This is one of BG-0002's
anticipated derived-work topics named by DEC-0443's roster.

## Scope

**In:**
- Greenfield bootstrap workflows.
- Brownfield fold-in and migration of pre-existing projects.
- Compliance verification against the Engine's checker.
- Adopter onboarding documentation.

The greenfield/brownfield distinction lives at story level, not epic
level (DEC-0465).

**Out:**
- Export/packaging for third parties — an underived roster topic, per
  DEC-0467.
- Customization/extension points — adopters get the standard corpus
  shape; DEC-0470 draws this as a firm line, re-openable on demand.

## Domain Context

Bounded context: **Groundwork adoption — greenfield & brownfield**
(per DEC-0462, DEC-0465). Verifies against Engine Core & Artifact
Model's compliance definition and bootstraps Agent & Skill Surfaces'
canonical skills; has no outgoing impact edges among current
siblings.

## Interfaces & Contracts to Define

- The compliance-verification contract: what "checker-passing" means
  for a freshly adopted corpus (consumed from Engine Core & Artifact
  Model, the EP-0010→EP-0013 impact edge landing here).
- The brownfield fold-in/migration contract, dependent on the
  Engine's migration mechanism (DEC-0471).
- Adopter onboarding documentation structure and scope.

## Risks & Open Questions

- Blocks on Engine Core & Artifact Model's compliance definition
  stabilizing — implementation stories should not start before the
  artifact-model formalization gates; research spikes may run
  earlier.
- What brownfield fold-in actually looks like for a real pre-existing
  repo is a candidate spike.
- Corpus-compatibility promises depend on Engine Core & Artifact
  Model's migration mechanism (DEC-0471).

## Derived Work

None yet; this epic derives stories and spikes at its own refinement
session.
