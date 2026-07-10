---
id: IDEA-0013
type: idea
title: "A paradigm export mechanism for using Groundwork outside the Groundwork application"
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-10
proposed-by: awakeinagi
overview: >-
  Once the method's delegation/contract pattern is confirmed
  permanent and destined to live inside the BG-0001 application
  (DEC-0346), a distinct question emerges: how does a project that
  isn't the Groundwork application itself obtain and use these
  skills and agents? The stakeholder's first hypothesis is that
  IDEA-0010's plugin is the export vehicle, but flagged this as
  needing its own deep grilling — versioning across consumer
  projects, update propagation, fork-vs-track semantics — not a snap
  answer. Closely related to IDEA-0010 without being identical; a
  take-up session should consider both together. Disposition
  pending.
links:
  derives-from: [SES-0060]
  relates-to: [IDEA-0010, DEC-0346]
---

# IDEA-0013: A Paradigm Export Mechanism for Using Groundwork Outside the Groundwork Application

## The Idea

Verbatim: "What we do need to define is agents and skills exporting
mechanism for using the Groundwork paradigm outside of the Groundwork
application. Add this as an idea to grill deeply on in a future
session. My first thought is that the plugin will be the export
vehicle."

## Spark Context

Raised mid-grilling on the pending Artifact Interaction Surface
epic's derivation (DEC-0339, epic not yet created), immediately after
correcting BG-0002's sacrificial framing (DEC-0346): once the method's pattern
(mandatory delegation, contract-first tooling) is confirmed permanent
and destined to live inside the BG-0001 application, a distinct
question emerges — how does a project that ISN'T the Groundwork
application itself (i.e., any other Groundwork-managed project, per
DEC-0326's "every project using the Groundwork documentation
paradigm" framing) obtain and use these skills and agents? The
stakeholder's first hypothesis is that IDEA-0010's plugin (packaging
the skills and agents for distribution) is the export vehicle — but
the idea is flagged as needing its own deep grilling, not a snap
answer, and relates closely to IDEA-0010 without being identical to
it (IDEA-0010 is about packaging as a unit; this idea is about what
"export" means and requires — versioning across consumer projects,
how updates propagate, whether consumer projects fork or track the
canonical source).

## Disposition

Pending — awaiting take-up via the change-intake protocol as its own
session. Closely related to IDEA-0010; a take-up session should
consider both together.
