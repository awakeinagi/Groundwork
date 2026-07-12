---
id: DEC-0431
type: decision
title: "Develop-branch promotion is an optional corpus-release pattern, independent of ID allocation"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-12
source-span: "SES-0082 T22, T26, T27, T28, T31"
accepted-in: SES-0082
overview: >-
  A develop-to-main integration branch is an optional release-
  management pattern — batching sessions, checker validation across
  the combined result, format-version stamping, promoting pinnable
  snapshots — independent of ID allocation and carried in SP-0018's
  scope as its own concern.
links:
  derives-from: [SES-0082]
  relates-to: [SP-0018]
---

# DEC-0431: Develop-branch promotion is an optional corpus-release pattern, independent of ID allocation

## Context

The supplementary consultation round that resolved ID allocation (DEC-K) surfaced a genuinely new, separable idea from the stakeholder's original CHANGELOG-analogy proposal: even without merge-time ID reconciliation, a develop-to-main promotion branch could still be valuable purely as a release-management pattern. SES-0082 needed to capture that distinct value without conflating it back into the settled ID-allocation decision.

## Decision

A develop-to-main integration branch is an optional governance and topology pattern for corpus release management: batching sessions, running the integrity checker across the combined result, stamping the corpus format version, and promoting validated snapshots that consumer projects can pin. It is independent of ID allocation and is carried in SP-0018's scope as its own concern.

## Rationale

Separating this from ID allocation keeps DEC-K's ruling clean while still honoring the genuinely useful part of the stakeholder's original intuition: batched, checked, versioned promotion is valuable release-management hygiene regardless of how IDs are minted. Framing it as optional, not mandatory topology, respects that solo and small-team deployments may have no need for a develop/main split at all.

## Alternatives Considered

Folding this into DEC-K as a single combined decision was rejected — it would have made a settled item (ID allocation) harder to read alongside a still-optional, separately scoped pattern (release promotion). Discarding the idea entirely alongside the rejected merge-time-reconciliation proposal was rejected — the supplementary round explicitly credited it as the round's genuinely new, independently valuable capture.

## Implications

SP-0018 carries this as its own scoped concern alongside the ID-allocation fallback documentation (DEC-K). It ties naturally to DEC-F's format-version marker (stamped at promotion) and gives consumer projects a pinning mechanism once built.
