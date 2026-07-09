---
id: DEC-0050
type: decision
title: Bitbucket Data Center is the sole v1 code-host connector
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
overview: >-
  v1 ships exactly one code-host connector: Bitbucket Data Center (self-hosted).
  GitHub, Bitbucket Cloud, and GitLab connectors are future work validated
  against the same contract (DEC-0045). The connector contract is
  host-agnostic; BBDC is chosen as the reference implementation because it
  matches the organization's actual hosting and implies Jira Data Center as the
  target Jira instance. The capability baseline is set by BBDC's features:
  no native CODEOWNERS-style path-scoped reviewer requirements, so the
  gate-policy required check carries more enforcement weight.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0005 @ T5"
links:
  derives-from: [SES-0005]
---

# DEC-0050: Bitbucket Data Center is the v1 host

## Context

The connector contract is host-agnostic
(DEC-0045); v1 needed its
reference implementation and capability-manifest baseline picked.

## Decision

v1 ships exactly one code-host connector: **Bitbucket Data Center**
(self-hosted). GitHub, Bitbucket Cloud, and GitLab connectors are future
work validated against the same contract.

## Rationale

Matches the organization's actual hosting; a self-hosted Atlassian stack
also implies the Jira connector targets Jira Data Center (assumption to
confirm during story refinement).

## Alternatives Considered

- **GitHub as reference**: richest APIs (good capability ceiling), wrong
  deployment reality.
- **Multiple hosts at v1**: validates the abstraction earlier, at real
  cost to the v1 slice.

## Implications

The capability baseline is BBDC's: no native CODEOWNERS-style path-scoped
reviewer requirements, so the `gate-policy` required check carries more
enforcement weight (DEC-0036);
merge checks / Code Insights are the native required-check surface;
reviewer groups and default reviewers approximate team routing. Webhook
payloads for drift diffs (DEC-0044)
use the Data Center event families.
