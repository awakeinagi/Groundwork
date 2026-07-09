---
id: DEC-0071
type: decision
title: Participant profiles are supported, strictly opt-in, and user-owned via the UI
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0008 @ T4-T5"
links:
  derives-from: [SES-0008]
---

# DEC-0071: Opt-in, user-owned participant profiles

## Context

"Memory system for the agent" could mean only derived views of canonical
artifacts, or also cross-session memory about *people* — interaction
preferences that make sessions better (pacing, example style, questions
already answered) but that carry privacy weight.

## Decision

The memory layer is designed to support both consolidations/retrieval
**and** participant interaction profiles. Profiles are **opt-in by the
user**: no profile exists or accrues without explicit consent. Profile
data is **easily readable and editable by its subject via the UI** — users
see exactly what the agent remembers about them and can correct or delete
it. Profiles feed session conduct through the same bundle mechanism
(DEC-0068) as any other context element.

## Rationale

Interaction memory measurably improves repeat sessions, but profiling
colleagues without consent and visibility is a governance hole; making the
subject the owner of their profile resolves the tension without discarding
the value.

## Alternatives Considered

- **Consolidations only** (agent's recommendation): cleaner scope, forfeits
  session-quality gains.
- **Profiles without consent machinery**: invisible to gates, corrosive to
  trust.

## Implications

Profile storage is per-person, outside the canonical artifact store (it is
personal data, not design truth) — storage design at story level. New
impact edge EP-0007→EP-0006: profile viewer/editor and consent surface are
UI requirements. Org facts the agent learns still belong in artifacts
(glossary, decisions), never in profiles.
