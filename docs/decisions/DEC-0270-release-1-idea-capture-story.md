---
id: DEC-0270
type: decision
title: A release-1 UI story delivers Idea capture and a minimal list with decline; work-queue surfacing joins release 2
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0051 @ T6-T9"
links:
  derives-from: [SES-0051]
  relates-to: [DEC-0261]
---

# DEC-0270: Release-1 Idea capture in the UI

## Context

The facilitator recommended deferring all Idea UI to release 2 beside
the triage views; the stakeholder overrode: capture belongs in release
1. The follow-up question was how much release-1 scope that pulls in,
given that release 1's UI surface is deliberately session-centric and
every browsing/queue/triage story (ST-0050, ST-0051, ST-0055, ST-0056)
is deferred.

## Decision

A new release-1 story under EP-0006 (ST-0065) delivers: (1) an
in-session **"park as Idea"** action on the conversation surface — the
focus-artifact test's UI form, proposable by the agent and invocable
by the participant; (2) a **global quick-capture** in the application
shell for brain-dumps outside any session; (3) a **minimal
captured-Ideas list** (title, status, spark context); (4) **decline
with required rationale**, gate-policy-checked. Work-queue surfacing
beside untriaged CPs joins release 2: ST-0065 carries impact edges to
ST-0055 and ST-0056, and the surfacing is recorded as their revival
scope — visible now, built then.

## Rationale

Capture at the moment of inspiration is the point of the Idea type
(DEC-0261's brain-dump framing) — deferring it would leave release 1's
users with agent-only capture. But browsing/queue surfaces are a
settled release-2 seam; re-opening it for one artifact type would
re-scope two deferred stories for little payoff. Decline completes the
lifecycle so the release-1 UI exercises every status — a list that can
only grow trains users to ignore it.

## Alternatives Considered

- **Defer all Idea UI to release 2** (facilitator's recommendation):
  overridden — capture is release-1 value.
- **Full capture+browse+queue in release 1**: duplicates deferred
  ST-0055/ST-0056 territory.
- **Capture without a list**: captured Ideas invisible except via the
  agent — weakens the work-queue promise.

## Implications

ST-0065 is derived, refined, and gated in this session; EP-0006's
Derived Work updates in the same edit (DEC-0246); the impact edges get
impactor-side prose in ST-0065 (DEC-0249) and the cross-story coupling
check runs over the touched sibling set.
