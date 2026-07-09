---
id: DEC-0195
type: decision
title: A six-seam vertical-slicing catalog is adopted for epic derivation
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0036 @ T1-T3"
links:
  derives-from: [SES-0036]
  relates-to: [DEC-0196, DEC-0197, DEC-0191]
  supersedes: []
---

# DEC-0195: A Six-Seam Vertical-Slicing Catalog Is Adopted for Epic Derivation

## Context

The Epic derivation playbook asked "boundaries between epics" as a
question but gave no concrete method for finding good ones. The
stakeholder proposed five slicing heuristics (Access, Timeline, Protocol,
Integration, Sophistication), each with a Rule and Examples, labeled
"Horizontal Slicing" — which inverts standard agile/architecture
terminology (Cockburn's "Elephant Carpaccio," SAFe): the good practice
proposed (cutting through all architectural layers along a business
seam) is conventionally called *vertical* slicing; the anti-pattern
warned against ("Database Changes," "Frontend Components," "Stripe
Integration" as separate epics) is conventionally called *horizontal*
(layer) slicing.

## Decision

Adopt a six-seam catalog in `references/epic-slicing-seams.md` as the
epic-derivation slicing guidance: Access, Timeline, Protocol,
Integration, Sophistication, and a new sixth seam, Bounded-Context /
Domain-Capability — added because it's the seam
EP-0001..EP-0007
actually used, and the original five skew toward customer-facing product
decomposition rather than internal/platform tooling. Each seam is
documented with a Rule, Examples, and a "Why this seam works"
explanation. Terminology is corrected: the seam-based practice is named
**vertical slicing**; the anti-pattern is named **horizontal (layer)
slicing**, matching standard usage. The Sophistication seam carries an
explicit caveat: baseline error handling stays inside the core epic
(definition-of-done, not phase-2 work) — only genuinely advanced
hardening earns its own epic, consistent with
DEC-0191's existing
treatment of edge cases.

## Rationale

Correct terminology avoids confusing any future facilitator or
stakeholder who already knows the standard vocabulary. The
Bounded-Context seam fills a real gap: this project's own epic set isn't
explainable by any of the original five, and DDD bounded contexts
(Evans/Vernon) are the standard seam for exactly this project's
category of system (internal tooling / platform infrastructure).

## Alternatives Considered

- **Keep the stakeholder's original "Horizontal Slicing" label**:
  rejected — would actively conflict with near-universal industry usage
  and confuse readers who already have standard agile training.
- **Leave the catalog at five seams**: rejected — this project's own
  epics (`EP-0001`..`EP-0007`) wouldn't be explainable by any of them, a
  glaring gap for a skill that must also describe internal/platform
  systems like Groundwork itself.

## Implications

`references/epic-slicing-seams.md` created; `refinement-process.md`'s
Epic playbook and `SKILL.md`'s reference map point to it.
