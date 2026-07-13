---
id: IDEA-0064
type: idea
title: "Recall-audit judge packets must be self-sufficient"
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-13
proposed-by: awakeinagi
overview: >-
  SES-0089's audit judge packet was delivered containing only the
  candidate batches — the artifact overviews and generic judge
  instructions the packet was specified to embed were missing, so
  all eight judge subagents independently re-fetched epic content
  from docs/, duplicating work and risking inconsistent judgments
  against files that change mid-audit. Idea: harden the packet-
  assembly step of the recall-audit recipe (librarian side) so the
  packet file verifiably embeds the target-artifact overviews and
  judge instructions before judges spawn. Raised as a judge finding
  during SES-0089's decision-recall audit (T19) and ratified for
  capture by the stakeholder at T20.
links:
  derives-from: [SES-0089]
  relates-to: [SES-0089]
---

# IDEA-0064: Recall-audit judge packets must be self-sufficient

## The Idea

Harden the packet-assembly step of the recall-audit recipe (librarian side) so the packet file verifiably embeds the target-artifact overviews and the judge instructions before any judge subagent spawns — assembly should assert both are present and non-empty, refusing to hand off an incomplete packet.

## Spark Context

SES-0089's audit judge packet was delivered containing only the candidate batches — the artifact overviews and generic judge instructions the packet was specified to embed were missing. All eight judge subagents independently re-fetched epic content from docs/, duplicating work and risking inconsistent judgments against files that could change mid-audit. Raised as a judge finding during SES-0089's decision-recall audit (T19) and ratified for capture at T20.

## Disposition

Pending.
