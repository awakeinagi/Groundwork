---
id: DEC-0252
type: decision
title: Semantic changes to a Groundwork corpus happen only inside sessions — a hard rule with no waiver
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0050 @ T5, T10-T11"
links:
  derives-from: [SES-0050]
---

# DEC-0252: Semantic changes happen only inside sessions

## Context

The stakeholder proposed a standard change-intake workflow and
clarified its core rule: the paradigm must not present sessions as
optional for changes. What binding force does the session requirement
carry, and what happens when a user asks the agent to skip it?

## Decision

Under the Groundwork paradigm, no semantic change to the artifact
corpus is made outside a recorded session. Off-record discussion that
produces no changes is always allowed; the moment the user instructs a
change, a session must capture the intent and the decisions. When a
user asks to skip the session, the agent declines to edit artifacts
and offers the expedited path (DEC-0254) instead — the rule has no
waiver, including for users holding full authority.

## Rationale

Provenance is the paradigm's central guarantee; a waivable session
rule makes it advisory, and every un-sessioned change is a permanent
hole in the decision trail. Keeping compliance cheap (DEC-0253's
mechanical floor, DEC-0254's expedited path) is the mechanism that
makes a hard rule livable.

## Alternatives Considered

- **Warn once, then comply**: respects user authority in the moment
  but converts the rule into a preference; rejected by the stakeholder
  explicitly ("that should not be allowed").
- **Offer sessions as the default with opt-out**: the original
  proposal's phrasing implied this; superseded by the stakeholder's
  clarification at T5.

## Implications

The intake protocol (DEC-0255) is the sole entry point for semantic
change. AGENTS.md and the skill playbooks state the rule as
non-negotiable. Purely mechanical fixes are exempt via DEC-0253.
