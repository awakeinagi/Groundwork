---
id: DEC-0398
type: decision
title: "Overviews may never contain unresolvable artifact-ID tokens"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0077 @ T8-T9"
overview: >-
  The code-span carve-out for artifact-ID tokens is body-scoped
  only, and the recheck and checker had treated overview-field IDs
  inconsistently; DEC-0284 already defines overviews as plain, no-
  Markdown prose. Every artifact-ID-shaped token in a frontmatter
  overview must now resolve to a real artifact, and wrapping it in
  backticks grants no exemption on this surface. The body's code-
  span carve-out is unchanged. Overviews are freely regenerable, so
  rewording to avoid a literal unresolvable pattern costs nothing.
  Decided at SES-0077, paired with the recheck code-span-parity
  decision.
links:
  derives-from: [SES-0077]
  relates-to: [DEC-0284, DEC-0286, DEC-0399, DEC-0242]
---
# DEC-0398: Overviews may never contain unresolvable artifact-ID tokens

## Context

The code-span carve-out for artifact-ID tokens is body-scoped only, yet the recheck and the full checker had been treating overview-field IDs differently from each other. DEC-0284 already defines overviews as plain, no-Markdown prose.

## Decision

Every artifact-ID-shaped token that appears in a frontmatter overview must resolve to a real artifact; wrapping it in backticks grants no exemption on that surface. The body's code-span carve-out is unchanged.

## Rationale

Overviews are freely regenerable, so rewording an overview to avoid a literal unresolvable pattern costs nothing, unlike a body rewrite.

## Alternatives Considered

No alternatives were separately recorded at distillation (skeleton restored at SES-0077).

## Implications

No separate implications were recorded at distillation; the operative consequences are stated in the Decision (skeleton restored at SES-0077).
