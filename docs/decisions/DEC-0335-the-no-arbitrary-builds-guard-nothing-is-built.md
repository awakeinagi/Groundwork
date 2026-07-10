---
id: DEC-0335
type: decision
title: The no-arbitrary-builds guard — nothing is built without a presented, approved design
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0059 @ T8-T9, T12-T15, T19"
overview: >-
  In every Groundwork-managed project, nothing is built without a
  written design presented to and approved by a human — however
  simple; the build-side sibling of DEC-0252. Mechanical floor:
  changes that cannot alter runtime behavior or any contract surface
  (comments, whitespace, invisible renames) pass without ceremony;
  configuration is never mechanical — tool lists, models,
  permissions, settings, dependencies are semantic by definition;
  when in doubt, semantic. Build intent enters through the intake
  protocol like change intent; the design may be a few sentences but
  the step is never skipped (the adopted anti-pattern: "This Is Too
  Simple To Need A Design"). Enforced like DEC-0326: standing
  instruction in AGENTS.md plus project memory in every Groundwork-
  paradigm project, verified at design-session startup. BG-0002
  cites this rule as its governing premise.
links:
  derives-from: [SES-0059]
  relates-to: [DEC-0252, DEC-0253, DEC-0255, DEC-0256, DEC-0326]
---

# DEC-0335: The No-Arbitrary-Builds Guard

## Context

SES-0058's deliverables were designed and built from a single
conversation; the deployed librarian acquired tools nobody discussed.
DEC-0252 guarantees no semantic corpus change happens outside a
session, but nothing guaranteed the same for construction. The
stakeholder's directive at T8: "The most important thing is that we
guard against any project building things arbitrarily."

## Decision

In every Groundwork-managed project, nothing is built without a
written design that has been presented to and approved by a human —
however simple the build. The rule has a mechanical floor: changes
that cannot alter runtime behavior or any contract surface (comments,
whitespace, renames invisible from outside) pass without ceremony;
**configuration is never mechanical** — any change to a tool list,
model, permission, setting, or dependency is semantic by definition;
when in doubt, it is semantic. Build intent enters through the intake
protocol exactly like change intent (DEC-0255/DEC-0256): the moment
"let's build X" is uttered, the path runs restate → design artifact →
approval → build. The design may be a few sentences for truly simple
work — the step is never skipped ("This Is Too Simple To Need A
Design" is the named anti-pattern, adopted from the superpowers
brainstorming skill the stakeholder cited at T12). Enforcement mirrors
DEC-0326: a standing instruction in every project's AGENTS.md
Groundwork section and project-level memory, verified at
design-session startup.

## Rationale

"Simple" work is where unexamined assumptions cause the most drift —
proven twice in this session alone (the SES-0058 build; the T15
hot-fix whose design was invented unpresented, called out at T16).
A paradigm rule at DEC-0252's altitude closes the class, not the
instance.

## Alternatives Considered

- **No floor** (every change incl. comments needs a design) — airtight
  but taxes changes that cannot drift; rejected at T19.
- **Scope to method tooling only** — the directive says ANY project;
  rejected.
- **Rely on gates alone** — gates catch what reaches them; arbitrary
  builds never reach them; rejected.

## Implications

BG-0002 cites this rule as a constraint (premise, not outcome). The
design-session skill's intake section and the AGENTS.md asset gain the
build-intent path and the standing instruction. DEC-0253's
zero-semantic-content definition is complemented, not changed: the
build-side floor is defined here.
