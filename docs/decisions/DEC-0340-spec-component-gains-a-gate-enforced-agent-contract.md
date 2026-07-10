---
id: DEC-0340
type: decision
title: SPEC-component gains a gate-enforced agent-contract profile
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0059 @ T10-T12, T17, T19"
overview: >-
  A Component Doc describing an agent must carry a runtime-policy
  section (component-type: agent) enumerating as decision-cited
  contract items: every configuration field and its value —
  explicitly including the fields verified to expand capability
  implicitly (memory auto-grants Read/Write/Edit; mcpServers grants
  those tools; tools: Agent(...) grants spawning) — plus the deny-
  by-default tool surface with per-grant rationale, the double-
  pinned model, memory policy, refusal semantics, spawn contract,
  concurrency obligations, and an explicit breaking-change list
  (tool grants, model class, memory scope, refusal semantics, spawn
  contract require re-gate; DEC-0322 eval-loop build details and
  memory content do not). A gate cannot pass an agent CMP missing
  any clause — mechanically checked, not reviewer-memory. Chosen
  over a new element type per DEC-0311's anti-generality stance,
  with a recorded revisit trigger if the agent population grows past
  three. Executes as a gated SPEC-component amendment.
links:
  derives-from: [SES-0059]
  relates-to: [DEC-0011, DEC-0311, DEC-0329, DEC-0322, DEC-0335, DEC-0338, DEC-0341, DEC-0342]
---

# DEC-0340: The Agent-Contract Profile in SPEC-component

## Context

The librarian's drift lived in configuration no artifact type forced
anyone to write down. Component Docs are the contract artifact
(DEC-0011), but their element types (entity/value/service/event/
protocol) have no mandatory home for an agent's runtime policy. Both
architect instances converged on a gate-checkable profile; the
record-grounded instance located it as a SPEC-component extension
honoring DEC-0311's anti-generality stance. The T17 research supplied
the verified field inventory.

## Decision

SPEC-component gains an agent-contract profile (as a
`component-type: agent` extension): a CMP describing an agent MUST
carry a runtime-policy section enumerating, as decision-cited contract
items —

1. **Every configuration field** of the agent definition and its
   chosen value, explicitly including the fields verified to expand
   capability implicitly: `memory` (auto-grants Read/Write/Edit),
   `mcpServers` (grants those servers' tools), `tools: Agent(...)`
   (grants spawning); plus `disallowedTools` where used.
2. **Tool surface** — deny-by-default enumeration; anything unlisted
   is denied; each grant carries its rationale.
3. **Model** — class and the double-pin mechanism (DEC-0329 pattern).
4. **Memory policy** — mechanism, the single writable path, content
   rules.
5. **Refusal semantics** and the result/report contract.
6. **Spawn contract** — who may call it, required spawn parameters.
7. **Concurrency** — caller obligations included.
8. **Breaking-change list** — changes requiring re-gate (tool grants,
   model class, memory scope, refusal semantics, spawn contract)
   versus compatible changes (eval-loop build details per DEC-0322;
   memory content).

A gate cannot pass an agent CMP missing any clause — the check is
mechanical, not reviewer-memory. Revisit whether agents warrant a
distinct element type if the agent population grows past three
(currently: librarian, overview-writer, system-architect).

## Rationale

A contract that lists only operations has covered a fifth of what an
agent can do; the incident lived in the uncovered policy dimension.
Making the profile mandatory turns "we forgot to discuss the memory
field" into a mechanically impossible state.

## Alternatives Considered

- **New agent element type** — larger SPEC surface for a population of
  three; rejected per DEC-0311's stance, with the revisit trigger
  recorded.
- **Advisory checklist** — decays like any unmeasured boundary;
  rejected.

## Implications

A gated SPEC-component amendment executes this (SPEC edits are
semantic; the DEC-0335 intake applies to the checker changes too).
The backfill CMPs (DEC-0342) are the profile's first instances.
DEC-0341's conformance check reads the profile as its ground truth.
