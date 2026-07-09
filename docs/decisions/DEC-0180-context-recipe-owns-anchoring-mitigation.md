---
id: DEC-0180
type: decision
title: Context-recipe story owns anchoring-risk mitigation for the synthesized draft
status: accepted
owner: ds-lead
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0033 @ T2-T3"
links:
  derives-from: [SES-0033]
  supersedes: []
---

# DEC-0180: Context-Recipe Story Owns Anchoring-Risk Mitigation for the Synthesized Draft

## Context

EP-0002's Risks flagged
that the incremental synthesis draft
(DEC-0055), visible to
all participants for async comment, could leak into later 1:1 sessions
and bias their framing (anchoring). This needed a home: the synthesis
story (which produces the draft) or the context-assembly story (which
controls what enters a session's context).

## Decision

The context-recipe story (ST-0038)
owns the mitigation: strategy-pack context recipes
(DEC-0056) exclude the
synthesized draft's prose from 1:1 grilling context by default —
only structured facts (settled, accepted decisions) flow into a new
session, never the draft's framing or phrasing.

## Rationale

Anchoring is a retrieval-boundary problem, not a synthesis-production
problem — the draft itself is supposed to exist and be visible for
comment; the risk is specifically what a *pack* pulls into a fresh 1:1's
context. The component already responsible for that boundary
(context assembly) is the natural owner and the only place a testable
default can be enforced.

## Alternatives Considered

- **Synthesis story owns it**: would require the draft-producing story to
  reach into every consuming pack's retrieval behavior — inverts the
  dependency the context-recipe story already owns.
- **Pack-design note only, no AC**: leaves a known bias risk as
  implementer judgment with no contract to test against; rejected given
  the risk was explicit enough to name in the epic.

## Implications

ST-0038's
acceptance criteria state the default-exclusion rule as a testable
behavior.
