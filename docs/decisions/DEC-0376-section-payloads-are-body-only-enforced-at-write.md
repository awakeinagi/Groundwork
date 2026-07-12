---
id: DEC-0376
type: decision
title: "Section payloads are body-only, enforced at write time: edit-section and append-turn reject heading-bearing content"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0072 @ T11-T12"
overview: >-
  The edit-section and append-turn operations refuse replacement/turn content
  containing a markdown heading line at the target section's level
  or higher (fenced/inline code exempt), with an error naming the
  body-only contract — rejection chosen over auto-strip so the tool
  never silently mutates a submitted payload. Closes the IDEA-0041
  phantom-heading defect at its source; clean edits are idempotent.
links:
  relates-to: [DEC-0315, DEC-0377]
  derives-from: [SES-0072]
---

# DEC-0376: Section payloads are body-only, enforced at write time: edit-section and append-turn reject heading-bearing content

## Context

IDEA-0041's phantom-heading defect (four shipped/caught instances) arose from heading-bearing payloads that edit-section accepted silently, creating unaddressable duplicate headings.

## Decision

The edit-section and append-turn operations scan payload content (outside code) for heading lines at the target section's level or higher and refuse with a clear error; payloads are body-only, the tool owns heading lines.

## Rationale

Rejection keeps caller discipline honest and never silently alters submitted content; the librarian is the sole caller and adapts immediately.

## Alternatives Considered

Auto-stripping a leading matching heading (convenient, hides caller bugs); strip+warn (warnings ignorable by unattended agents).

## Implications

The librarian's operational pre-write grep becomes a fail-fast aid rather than the only defense; IDEA-0041's mechanism cannot recur through the write API.
