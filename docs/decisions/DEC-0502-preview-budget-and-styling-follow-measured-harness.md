---
id: DEC-0502
type: decision
title: "Preview budget and styling follow measured harness behavior"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi
decided-on: 2026-07-13
source-span: "SES-0093 @ T2, T4, T8"
overview: >-
  Consequence-sketch preview panes on grilling cards were previously
  budgeted at two to eight lines on a guessed truncation width. This
  session measured the actual AskUserQuestion preview pane: it
  renders a viewport-height window of post-wrap rows (about thirty-
  three at typical size) with no scroll and a silent 'lines hidden'
  cutoff beyond it, wraps wide lines without loss, holds the option-
  label column fixed near thirty characters, and renders markdown
  only partially (headers/bold/strikethrough/inline code/fenced
  code/blockquotes/links work; tables, checkboxes, and rules do
  not). This decision replaces the guessed budget with the measured
  one: previews stay within about twenty post-wrap rows with must-
  read content never below that line, labels stay within about
  twenty-eight characters, per-option analysis rides the preview
  pane rather than descriptions (which do not render in preview
  layout), and styling relies on bold pseudo-headers, hand-aligned
  monospace columns, fenced code, and blockquotes.
links:
  relates-to: [DEC-0472, DEC-0499, DEC-0501, DEC-0503]
  derives-from: [SES-0093]
---

# DEC-0502: Preview budget and styling follow measured harness behavior

## Context

Prior guidance sized consequence-sketch previews at roughly two to eight lines on the belief that panes hard-truncate near forty characters per line. This session measured actual behavior: the preview pane renders a viewport-height window of post-wrap rows (about thirty-three at the stakeholder's window size, fewer on smaller windows) and hard-cuts the remainder with a "lines hidden" rule and no scroll affordance; wide lines wrap at the pane edge without loss; the option-label column is fixed near thirty characters regardless of terminal width and cannot be widened or traded against the preview pane; and markdown renders partially — headers as bold, bold, strikethrough, inline code, syntax-highlighted code fences, blockquote bars, and styled links work, while tables, task checkboxes, and horizontal rules degrade to raw source.

## Decision

Preview sketches are budgeted to the measured envelope: up to about twenty post-wrap rows is the safe size, and nothing a stakeholder must read may sit below that line, because hidden content is unreachable. Labels stay within about twenty-eight characters per row. Per-option analysis rides the preview pane, never option descriptions, which do not render in preview layout; comparative or must-read analysis precedes the card in chat. The styling toolkit is bold pseudo-headers, hand-aligned monospace columns instead of markdown table syntax, fenced code blocks, and blockquote callouts.

## Rationale

The measured envelope replaces a guessed one that was far too conservative on width and not conservative enough about the missing scroll.

## Alternatives Considered

Keeping the two-to-eight-line guidance, which wastes most of the pane. Setting no budget at all, which risks decision-relevant content silently lost below the viewport fold.

## Implications

The playbook's preview guidance is rewritten to these numbers. The budget is viewport-dependent, so authors keep a margin rather than designing to the maximum.
