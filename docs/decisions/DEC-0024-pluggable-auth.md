---
id: DEC-0024
type: decision
title: Auth is a pluggable interface; start simple
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-05
overview: >-
  Authentication is a pluggable interface; v1 ships with simple email/OIDC
  provider; organizational SSO becomes swap-in adapter when required; auth contract
  exposes stable person identifiers so artifacts can reference them durably across
  provider swaps and identity matters only for attribution.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-05
source-span: "SES-0001 @ T12-T13"
links:
  derives-from: [SES-0001]
---

# DEC-0024: Auth is a pluggable interface; start simple

## Context

The application needs identity — decisions are attributed to named people and
gates need named approvers — but no organizational SSO mandate was
identified.

## Decision

Authentication sits behind a pluggable interface like every other boundary.
v1 ships with a simple provider (email/OIDC); organizational SSO becomes a
swap-in adapter when required.

## Rationale

Identity matters early only for attribution (`decided-by`, `approved-by`);
the provider behind it does not. Treating auth as a connector keeps it
consistent with the system's modularity principle.

## Alternatives Considered

- **Org SSO day one**: no mandate exists to satisfy.
- **Atlassian identity**: convenient (everyone has a Jira seat) — remains a
  candidate adapter, not a foundation.

## Implications

The auth contract must expose stable person identifiers that artifacts can
reference durably across provider swaps.
