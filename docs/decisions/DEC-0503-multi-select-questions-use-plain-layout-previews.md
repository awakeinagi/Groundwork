---
id: DEC-0503
type: decision
title: "Multi-select questions use plain layout; previews are never attached to them"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi
decided-on: 2026-07-13
source-span: "SES-0093 @ T6, T7, T8"
overview: >-
  DEC-0472 already routes genuinely multi-select grilling questions
  to plain layout, and superseding DEC-0473 removes the Other-routed
  elaborate keyword those plain cards relied on. A live probe in
  this session confirmed multi-select cards with previews attached
  silently discard the previews — no error — while descriptions and
  checkboxes render and the inline Other field works and combines
  with listed selections. This decision gives multi-select questions
  their own explicit affordance story: option descriptions carry
  per-option analysis, Other is the free-text and elaborate-keyword
  channel (mirroring the preview cards' blank-note convention), no
  separate 'Something else/Please elaborate' option is added, and
  previews are never attached to multi-select questions since the
  harness drops them without warning.
links:
  relates-to: [DEC-0472, DEC-0499, DEC-0500, DEC-0502]
  derives-from: [SES-0093]
---

# DEC-0503: Multi-select questions use plain layout; previews are never attached to them

## Context

DEC-0472 already drops genuinely multi-select questions to plain layout because the harness supports previews only on single-select questions, and superseding DEC-0473 removes the elaborate keyword machinery plain cards relied on. A live probe in this session verified the harness behavior: a multi-select question with previews attached renders in plain layout with the previews silently discarded — no error — while descriptions render, checkboxes work, and the inline "Type something" (Other) option is present and combinable with listed selections; no notes affordance exists there.

## Decision

Multi-select questions keep DEC-0472's plain layout, with an explicit affordance story: per-option trade-off prose may ride option descriptions, which render on plain cards; Other is the free-text channel; and typing elaborate into Other — or any answer resembling "I don't understand" — triggers the same elaboration behavior as the preview cards' blank-note convention. No "Something else/Please elaborate" option is listed on plain cards, since Other natively occupies that role. Previews are never attached to multi-select questions: the harness discards them silently, and any content placed only in them is lost to the stakeholder.

## Rationale

Without an explicit plain-card decision, superseding DEC-0473 would orphan the elaborate guarantee on multi-select cards. The silent-discard behavior makes the never-attach rule a data-loss guard, not a style preference.

## Alternatives Considered

Phrasing every question single-select, which DEC-0472 already prefers where feasible, but genuinely multi-select questions exist. Attaching previews to multi-select questions anyway, verified non-functional by the probe.

## Implications

Multi-select card authoring deliberately differs from preview-card authoring: analysis may live in descriptions there. The question text continues to disclose the affordance difference, per DEC-0472.
