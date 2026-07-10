---
id: DEC-0353
type: decision
title: "Defect-artifact shape travels with the backfill"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-10
decided-by: awakeinagi
decided-on: 2026-07-10
source-span: "SES-0065 @ T9-T10"
overview: >-
  The defect-tracking artifact type needed by DEC-0342's fix-via-
  defect disposition path (its sole named consumer) is not designed
  during EP-0009's derivation. SES-0065 (T9-T10) records the
  stakeholder's sketch -- a severity field plus a multi-state status
  workflow -- and defers the type's full design to the backfill
  fold-in Idea's take-up, where it can be shaped against the
  backfill's actual divergence list rather than a hypothetical one.
links:
  derives-from: [SES-0065]
  relates-to: [DEC-0342]
---

## Context

DEC-0342's backfill protocol names "fix via a defect item" as one of
two dispositions (alongside "keep via a recording decision") for
divergences found diffing the as-built surface against its
intent-first-drafted contracts. No defect-tracking artifact type
exists in the corpus yet. Grilling round 1 (T9) asked when to design
its shape; the stakeholder gave a stakeholder-sketched shape (severity
plus a multi-state status workflow) and chose timing (T10).

## Decision

The defect-tracking artifact type's shape (stakeholder sketch:
severity field plus a multi-state status workflow) is designed at the
backfill Idea's take-up, not in this session. This is deliberate
timing, not an unresolved gap: the type's sole consumer named so far
is DEC-0342's fix-via-defect disposition path, which only exercises
during the backfill itself, so designing the shape in the same session
that first needs it keeps the design grounded in real divergences
rather than speculative ones.

## Rationale

Designing an artifact type against a hypothetical need risks the
generality this corpus otherwise guards against (DEC-0311's anti-
generality stance, applied here to artifact-type proliferation);
waiting for the backfill's actual divergence list gives the shape a
concrete basis.

## Alternatives Considered

- **Design the defect type now, in EP-0009's derivation** — rejected;
  no divergences exist yet to shape it against, and it has no other
  consumer that would need it sooner.
- **Design it as part of DEC-0340/DEC-0341's build** — rejected;
  those decisions are already accepted and their build already
  shipped without a defect type, so retrofitting there is worse
  sequencing than doing it once at backfill take-up.

## Implications

The fold-in Idea created this session carries the stakeholder's sketch
(severity + multi-state status workflow) forward as a named open
question, so the shape isn't re-derived from scratch at take-up.
