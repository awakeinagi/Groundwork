---
id: IDEA-0018
type: idea
title: "A skill for quick Idea-artifact creation and followups"
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-10
proposed-by: awakeinagi
overview: >-
  Idea capture already has a sanctioned lightweight path (DEC-0258),
  but every capture still routes through full session machinery and
  general typed write operations. A narrower, purpose-built skill
  with its own small contracted script (create an Idea from a short
  prompt; append a followup to an existing open Idea) could be a
  faster on-ramp into the existing protocol, not a replacement for
  it. Open design question: whether the script lives inside
  artifact-interact as a new operation or as its own small skill.
  Any implementation is itself build work requiring a presented
  design and test plan (DEC-0335) when taken up.
links:
  derives-from: [SES-0061]
  relates-to: [DEC-0258, DEC-0312, DEC-0335]
---

# IDEA-0018: A Skill for Quick Idea-Artifact Creation and Followups

## The Idea

Verbatim: "Let's create an additional skill to quickly create new
IDEA artifacts (creation only; can append followups to open Idea
artifacts; done through a contracted script in the skill)."

## Spark Context

Idea capture already has a sanctioned path (DEC-0258: a micro-session,
zero decisions required) and this session used it seven times in one
batch — but every capture still goes through the facilitator drafting
full Idea bodies, the librarian's general typed `create`/`append-turn`
operations, and a session record wrapping the whole thing. For a
genuinely quick "capture this thought and move on" moment — closer to
a brain-dump than even an expedited session — a narrower, purpose-built
skill with its own small contracted script (create an Idea from a
short prompt; append a followup note to an existing open Idea) could
be lighter-weight than routing through the general write API's full
session machinery every time. Relates to DEC-0258's existing idea-
capture protocol (this would be a faster on-ramp into it, not a
replacement) and to the artifact-librarian's contract (would this
script live inside artifact-interact as a new operation, or as its
own small skill the librarian or facilitator loads separately? — an
open design question for take-up).

## Disposition

Pending — awaiting take-up. Needs to be reconciled with DEC-0312 (sole
sanctioned write path) and DEC-0335 (no build without a presented
design) — a new script touching the corpus is itself build work
requiring its own short design and test plan when this is taken up,
not an exception to those rules.
