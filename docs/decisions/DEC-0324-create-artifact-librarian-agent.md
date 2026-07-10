---
id: DEC-0324
type: decision
title: Create the artifact-librarian project agent — the single artifact-interaction surface
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0058 @ T1-T5, T9"
overview: >-
  Creates the artifact-librarian project agent
  (.claude/agents/artifact-librarian.md): a subagent that any agent
  working in a Groundwork project — the design-session facilitator
  included — spawns whenever it needs to interact with corpus
  artifacts. Callers delegate task-level intents ("record these
  decisions with cites", "find precedent for X and return the
  relevant DECs"), not individual operations; the librarian plans and
  executes the reads, searches, graph queries, and typed writes via
  the artifact-interact skill and returns a distilled result — IDs,
  statuses, key excerpts, what was written, validation outcome — with
  verbatim sections or full artifacts included when the task requests
  fidelity (e.g. gate review). Chosen over an operation-level proxy
  (a spawn per CLI call forfeits the isolation benefit) and over
  facilitator-direct tooling. The name follows the role-shaped
  convention of system-architect and overview-writer: a librarian
  both retrieves and files. Binding force, enforcement, model,
  refusal semantics, statefulness, concurrency, and packaging are
  fixed by DEC-0325..DEC-0334.
links:
  derives-from: [SES-0058]
  relates-to: [DEC-0310, DEC-0312, DEC-0313, DEC-0292, DEC-0291]
---

# DEC-0324: Create the artifact-librarian Project Agent

## Context

SES-0057 extracted all artifact tooling into the artifact-interact
skill (DEC-0310) and made its write API the sole sanctioned write
path (DEC-0312). The stakeholder's next proposal: an agent that the
default agent calls as a subagent any time it needs to interact with
artifacts — moving the interaction surface itself out of the caller's
context. Precedents for project agents: system-architect (DEC-0292)
and overview-writer (DEC-0291).

## Decision

Create the `artifact-librarian` project agent in
`.claude/agents/artifact-librarian.md`. Its contract:

- **Callers**: every agent working in the project, the facilitator
  included.
- **Granularity**: task-level intent — the caller states what it
  needs; the librarian plans and executes all the reads, searches,
  graph queries, and typed writes required, using the
  artifact-interact skill as its toolbelt.
- **Result contract**: distilled by default (IDs, statuses, key
  excerpts, operations performed, validation outcomes); verbatim
  sections or whole artifacts on request in the task.

## Rationale

Task-level delegation is where subagent isolation pays: many tool
calls, none in the caller's context. An operation-level proxy would
cost a spawn per CLI call while saving nothing. A single interaction
surface also gives the corpus one place to enforce guardrails and one
behavior to tune.

## Alternatives Considered

- **Operation-level proxy** — spawn per operation; isolation benefit
  lost; rejected.
- **Facilitator keeps direct tooling, others delegate** — two paths
  to keep consistent; rejected at T5 in favor of one path for all.
- **Names `artifact-interactor`, `archivist`** — rejected at T9 for
  `artifact-librarian` (role-shaped, matches sibling naming).

## Implications

DEC-0325 makes delegation mandatory; DEC-0326 enforces it and
supersedes DEC-0321; DEC-0328 recharters the existing agents;
DEC-0334 ships the librarian inside the artifact-interact build.
