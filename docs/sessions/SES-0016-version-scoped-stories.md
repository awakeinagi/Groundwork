---
id: SES-0016
type: session
title: Version-scoping of stories — deferred status and SemVer release labels
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-07
overview: >-
  Supported version-scoping of stories via deferred lifecycle status and
  release labels. Settled: `deferred` as a lifecycle status with
  `release:` frontmatter field carrying target release (SemVer format
  with major required, minor/patch optional); labels declared in
  Business Goal's Scope section; deferral and revival each cite a
  decision; tooling excludes deferred artifacts from metrics/coverage
  warnings, provides dedicated deferred listing grouped by release, and
  flags elements implementing only deferred stories. Deferred status also
  applies to epics (which default their stories).
participant: awakeinagi@gmail.com
participant-role: eng-lead
facilitator: Claude Code (claude-fable-5)
transcript-fidelity: reconstructed
links:
  relates-to: [DEC-0022, DEC-0093, DEC-0095]
---

# SES-0016: Version-Scoping of Stories — Deferred Status and SemVer Release Labels

## Purpose

The participant wants the system to support scoping stories by version:
nice-to-have features surfacing during design sessions should be captured
as real stories but marked out of scope for the current release, with an
easy way to rediscover them when the time is right. Already settled going
in: the status lifecycle is a closed set meaning refinement maturity
([SPEC-artifact-common](../specs/SPEC-artifact-common.md)); the link
vocabulary is closed
(DEC-0009); "v1"
already exists informally in accepted decisions
(DEC-0022,
DEC-0073); uncovered approved
stories are flagged as design gaps
(DEC-0093) and
design percent-complete is equal-weighted over stories
(DEC-0095) — any
scoping mechanism must tell those tools which stories don't count yet.

## Transcript

**T1 — awakeinagi.** I would like to update the system to support scoping
of stories by version. During design sessions I may come up with
nice-to-have features that aren't necessarily in scope for a v1 or MVP
version of the system I'm building. We should still create the stories,
but they need a status indicating they are on hold. And we need a way to
discover these on-hold items easily so they can be brought back into
scope when the time is right. What are our options for handling that?

**T2 — facilitator.** Presented four mechanisms with trade-offs:
(A) a new lifecycle status (`deferred`) — one field, all tools read it,
but it conflates refinement maturity with build intent and loses an
approved story's lifecycle position while parked; (B) an orthogonal
scope field alongside status (recommended) — a story could be approved
and parked with provenance intact; (C) a release-roster artifact type —
best audit trail but a new artifact type, link type, and reciprocity
machinery; (D) a "future enhancements" bucket epic — rejected-shaped, as
it corrupts the derivation tree. Also asked: value vocabulary (named
releases + reserved `backlog`, recommended; vs binary flag; vs free-form
tags) and type reach (stories + epics, recommended; vs stories only; vs
all pipeline artifacts).

**T3 — awakeinagi.** On the mechanism: "I think deferred is correct in
this case. It doesn't seem sensible to approve a story before it is in
scope." Accepted the recommendations on vocabulary (named releases plus
reserved `backlog`, absence of the field meaning current release) and
type reach (stories and epics; an epic's label defaults its stories).

**T4 — facilitator.** Read back the hybrid the answers compose into:
`deferred` as a lifecycle status (gates ratify work feeding the next
stage, so out-of-scope stories shouldn't pass one) plus a `release:`
frontmatter field carrying the target, since a status can say *that*
something is parked but not *for which release*. Noted a deferred epic
automatically blocks story derivation via the existing
nothing-derives-from-unapproved-parent rule. Asked round 2: lifecycle
edges (recommended: defer from any active status, revive to `draft`),
where release labels are declared (recommended: the Business Goal's
Scope section, checker-validated), provenance (recommended: deferral and
revival each cite a decision), and tooling treatment (recommended:
exclude deferred items from metrics/coverage warnings, add a dedicated
deferred listing grouped by release, and flag elements whose
`Implements:` references only deferred stories).

**T5 — awakeinagi.** Accepted all four recommendations as presented.

**T6 — facilitator.** Played back five decisions for confirmation:
deferred lifecycle status; release field with controlled vocabulary;
labels declared in the goal's Scope; both scope moves cite decisions;
tooling exclusion plus discovery view.

**T7 — awakeinagi.** Asked for a full overview of each decision in chat
before confirming.

**T8 — facilitator.** Presented the five decision records in full —
context, decision, rationale, alternatives, implications.

**T9 — awakeinagi.** Amendment: use Semantic Versioning for the release
values. Release values must at least contain a major version but can be
specified down to minor or patch versions as well. Directed the
facilitator to find the spec via web search.

**T10 — facilitator.** Fetched the official SemVer 2.0.0 specification
from the semver.org source repository. Amended the vocabulary decision:
release values are prefixes of a SemVer version core — `MAJOR`,
`MAJOR.MINOR`, or `MAJOR.MINOR.PATCH` — numeric identifiers with no
leading zeroes; a partial value is a scope, not a version; no `v` prefix
(the spec's FAQ is explicit that `v1.2.3` is not a semantic version); no
pre-release or build metadata in release labels; deferred reporting
sorts by SemVer precedence with `backlog` last. Added one clause to the
declaration decision, flagged as the facilitator's call: a `release:`
value must exactly match a declared release or `backlog` — no
prefix-matching, to avoid ambiguity about which declared release owns a
story.

**T11 — awakeinagi.** "Those decisions are confirmed."

## Decisions Produced

- DEC-0097 — `deferred`
  joins the lifecycle for stories and epics; revival lands at `draft`
- DEC-0098 —
  `release:` frontmatter field with SemVer-prefix values plus reserved
  `backlog`
- DEC-0099 —
  release labels declared in the Business Goal's Scope section,
  checker-validated by exact match
- DEC-0100 —
  deferral and revival each cite a decision
- DEC-0101 —
  deferred items leave metric denominators and coverage warnings; gain a
  dedicated discovery view

## Conflicts Raised

None.
