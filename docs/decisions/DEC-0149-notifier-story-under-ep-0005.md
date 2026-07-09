---
id: DEC-0149
type: decision
title: The notifier connector contract is sliced as an EP-0005 story; the epic scope is amended
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Story derivation slices a notifier-connector story (contract,
  capability manifest, v1 email adapter) under EP-0005, and the epic's
  Scope gains a matching bullet. The assignment was already decided by
  DEC-0075; parking it would orphan v1 email delivery while the
  notification center is refined.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0026 @ T2-T3"
links:
  derives-from: [SES-0026]
  relates-to: [DEC-0075]
---

# DEC-0149: Notifier Connector Story Under the Connectors Epic

## Context

DEC-0075 (accepted after
EP-0005's approval)
assigns the notifier connector contract to this epic, but its
approved Scope names only code-host, Jira, and identity — leaving an
accepted decision's assignment dangling at story derivation.

## Decision

Story derivation slices a notifier-connector story (contract +
capability manifest + the v1 email adapter) under
EP-0005, and the epic's
Scope gains a matching bullet citing
DEC-0075. The amendment
is presented for sponsor re-affirmation in the same gate bundle as the
stories.

## Rationale

The assignment was already decided; the alternative — parking it — would
leave v1 email delivery without an owner while the notification center
(EP-0006) is refined against a
contract that doesn't exist.

## Alternatives Considered

- **Park until EP-0006
  refinement**: defensible dependency argument
  (the center defines the events to deliver), but orphans v1 email.
- **Move delivery into the UI epic**: contradicts
  DEC-0075's explicit
  assignment; would need a superseding decision.

## Implications

EP-0005 is amended and
re-affirmed; ST-0024
carries the contract; Slack/Teams adapters are future work captured per
DEC-0156.
