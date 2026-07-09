---
id: DEC-0192
type: decision
title: Goal gates render a mandatory Context Diagram and conditional Process Flow diagram
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Mandates a Context Diagram (C4 Level 1 in Mermaid) at Business Goal
  gate, rendered from System Context answers, showing the system,
  actors, and external dependencies. Adds an optional Process Flow
  diagram if the session surfaced enough sequential detail; never
  fabricates steps. Both diagrams are embedded in the versioned
  Business Goal doc alongside prose review to catch boundary
  misunderstandings at gate time. Constrains Goal playbook, Gates
  section, and Business Goal template. Status accepted.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0035 @ T15-T17"
links:
  derives-from: [SES-0035]
  relates-to: [DEC-0190, DEC-0191]
  supersedes: []
---

# DEC-0192: Goal Gates Render a Mandatory Context Diagram and Conditional Process Flow Diagram

## Context

The stakeholder's proposed "Next Steps" flow ended in a visual workflow
diagram for stakeholder sign-off before technical design begins. System
Context's answers (per
DEC-0190) are inherently
box-and-boundary shaped and map cleanly onto a diagram.

## Decision

At Business Goal gate, render a **Context Diagram** (C4 Level 1, Mermaid —
the system as one box, its actors, and external systems) from the System
Context answers; this is mandatory. Render a **Process Flow** diagram
(Mermaid flowchart, trigger through output) only if the session surfaced
enough sequential detail to do so meaningfully — never fabricate steps to
fill it in; omit the subsection instead. Both are embedded directly in the
Business Goal doc (System Context's Context Diagram / Process Flow
subsections) and walked with the approver alongside the text summary at
gate time.

## Rationale

A diagram catches boundary misunderstandings (a missing actor, an unnamed
external system) faster than prose review. Keeping it embedded in the
versioned doc, rather than a separate diagramming tool or artifact,
preserves git-backed markdown as the single source of truth (per
DEC-0008).

## Alternatives Considered

- **A separate diagramming tool/step outside the doc**: rejected — adds a
  synchronization burden and a second source of truth for something the
  doc's own content already determines.

## Implications

`references/refinement-process.md`'s Goal playbook and Gates section, and
`references/templates.md`'s Business Goal template, carry the two Mermaid
subsections. BG-0001's gate presentation
includes both diagrams.
