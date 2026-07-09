---
id: SES-0013
type: session
title: Typed obligations refinement — entity behavior/API, service I/O coverage
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-07
participant: awakeinagi@gmail.com
participant-role: stakeholder
facilitator: Claude Fable 5 (claude-fable-5) via Claude Code CLI
transcript-fidelity: reconstructed
links:
  relates-to: [SES-0012, ST-0007, CMP-0001]
---

# SES-0013: Typed Obligations Refinement

## Purpose

Follow-up to SES-0012: the
sponsor challenged the typed-obligations table of
DEC-0083 on two
points — entity behavior/API coverage and service input/output coverage.
SES-0012 is closed, so this is a new session.

## Transcript

**T1 — Sponsor.** Shouldn't entity elements need to define behavior
contracts and API contracts (as in the public API of the object)? And
should a service element have to define data contracts for its inputs
and outputs?

**T2 — Agent.** Analysis and recommendations. (a) Entity behavior:
agreed the table under-stated it — "identity & lifecycle invariants" is
a B-kind obligation and should be a full behavior contract (identity
semantics, lifecycle states, allowed transitions, domain-operation
semantics). Entity API: mandating A-kind for every entity would force
method-level signatures onto internal classes, over-specifying
implementation shape against
DEC-0011's
observable-guarantee standard and
DEC-0018's
language-agnostic requirement; everything an entity's public methods
must guarantee is expressible as behavior items. Recommended: B+D
mandatory, A conditional — required exactly when the entity's operations
are exposed at the component boundary (e.g., a graduated standalone
entity CMP). (b) Service I/O: a mandatory D-kind would misfire — a
service is stateless and owns no data, and the A-kind already mandates
request/response schemas per operation; the real failure mode is an API
item naming a payload type nobody defines. Recommended a
schema-resolution gate rule instead: every request/response schema in an
API item is defined inline or resolves to a declared value/event
element; dangling type references are gate-blockers. Noted this nudges
shared payloads into first-class value/event elements with their own
citable D items.

**T3 — Sponsor.** Both as recommended: entity B+D mandatory with
conditional A; schema-resolution rule for service I/O.

**T4 — Agent (synthesis).** Distilled
DEC-0088
(superseding DEC-0083 with the revised table) and
DEC-0089; updated
[SPEC-design-elements](../specs/SPEC-design-elements.md),
[SPEC-component](../specs/SPEC-component.md), ST-0007's element-validation
criterion, and CMP-0001's cites.

## Decisions Produced

DEC-0088,
DEC-0089

## Conflicts Raised

None.
