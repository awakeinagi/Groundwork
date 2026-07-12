---
id: DEC-0440
type: decision
title: "Governance keys people by email, with per-host identity mappings"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: stakeholder
source-span: "SES-0082 @ T41-T42"
overview: >-
  Governance configuration continues to key each person by email
  address; entries may now additionally carry host-identity mappings
  (e.g. a git-host username) that the DEC-0429 projection and
  DEC-0436 approver-group enforcement use to match approvals and
  merges to real host identities. Email remains the canonical, host-
  independent key, preserving DEC-0428's no-host-dependency
  principle; solo mode is unaffected. Accepted at SES-0082 T42,
  confirming the T41 recommendation.
links:
  derives-from: [SES-0082]
  relates-to: [DEC-0263, DEC-0428, DEC-0429, DEC-0436, DEC-0234, DEC-0174, DEC-0172]
---

# DEC-0440: Governance keys people by email, with per-host identity mappings

## Context

DEC-0429 has governance declare an enforcement level and project one-way into host configuration, and DEC-0436 needs approver-group enforcement to match approvals and merges to real host identities. Team-mode enforcement requires reconciling governance-configured people with git-host accounts, and a decision was needed on how those two identities relate.

## Decision

The governance configuration keys each person by email address, as today. A person's entry may additionally carry host-identity mappings (for example a git-host username) which the DEC-0429 projection and the DEC-0436 approver-group enforcement use to match approvals and merges to real host identities.

## Rationale

Email remains the canonical, host-independent person key, preserving DEC-0428's principle that no paradigm semantics depend on a specific git host. Host-identity mappings are additive metadata layered on top for team-mode enforcement, not a replacement for the canonical key.

## Alternatives Considered

Keying governance directly by git-host identity was implicitly available but declined, since it would tie paradigm semantics to a specific host, contrary to DEC-0428. Keeping email-only with no host mapping was also insufficient, since it leaves DEC-0429 and DEC-0436 enforcement with no way to match approvals and merges to real host accounts.

## Implications

Solo mode requires nothing new — it already keys people by email. Team-mode enforcement can now add host-identity mappings per person as needed, and the DEC-0429 projection and DEC-0436 approver-group enforcement rely on those mappings to reconcile governance configuration with actual host accounts.
