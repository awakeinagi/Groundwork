---
id: DEC-0292
type: decision
title: Create the system-architect project agent — design advisor and pre-gate reviewer, required at EP/ST/CMP, strongest-model pinned
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0054 @ T5-T12"
overview: >-
  Creates the system-architect project agent (.claude/agents/
  system-architect.md), taking up IDEA-0003. It serves two consultation
  moments: design advisor before/during refinement (candidate
  approaches, trade-offs, risks, seam/pattern suggestions the
  facilitator turns into grilling material) and design reviewer at gate
  prep (critiques the draft against best practices). Consultation is a
  required playbook step at epic, story/spike, and component
  refinement and gate prep; discretionary at business-goal level. The
  agent runs on the strongest available model — pinned in the agent
  definition's frontmatter AND passed explicitly at every spawn — with
  read-only tooling: it advises, never edits. Its knowledge comes from
  the companion skill established by DEC-0294.
links:
  derives-from: [SES-0054]
  relates-to: [IDEA-0003, DEC-0291, DEC-0293, DEC-0294, DEC-0295, DEC-0136]
---

# DEC-0292: Create the `system-architect` Project Agent

## Context

IDEA-0003 (captured at SES-0053 T11, right after DEC-0291 created the
project's first custom agent) proposed a system-architect agent whose
context is preloaded with architecture best practices, to help plan
system design at each stage of the artifact hierarchy. Without it,
architectural quality in refinement sessions depends entirely on
whatever the facilitating model brings to the session.

## Decision

Create a versioned project agent definition,
`.claude/agents/system-architect.md`, with two consultation moments:

- **Design advisor** — consulted before/during refinement of an
  artifact: given the artifact under refinement and its context, it
  returns architectural analysis (candidate approaches, trade-offs,
  risks, seam and pattern suggestions) that the facilitator turns into
  grilling questions and recommendations.
- **Design reviewer** — consulted at gate prep: critiques the draft
  against best practices; findings are addressed in-session before
  gating.

Invocation policy: consultation is a **required** playbook step at
epic, story/spike, and component refinement and gate prep;
**discretionary** (facilitator judgment or stakeholder request) at
business-goal level.

Model policy: the **strongest available model**, pinned in the agent
definition's frontmatter and additionally passed explicitly at every
spawn (the frontmatter pin alone is known not to take effect —
DEC-0291 precedent, inverted to the top of the model range).

Tooling: read-only (read/search over the corpus and its skill). The
agent advises; it never edits artifacts or runs git operations.

## Rationale

Advisor + reviewer covers both failure modes — designs shaped without
best-practice input, and drafts gated without best-practice critique —
at roughly double the invocation cost, which the stakeholder accepted.
EP/ST/CMP is where architecture lives; business goals are
business-shaped, so a required BG step would tax sessions for little
return. Design advice is quality-critical, the opposite end of the
spectrum from the Haiku-pinned overview-writer, so the model range
inverts while the pin-plus-explicit-override discipline carries over.

## Alternatives Considered

- **Advisor only / reviewer only** — each leaves one failure mode
  uncovered; rejected for full coverage at accepted cost.
- **Draft generator** — rejected: design content would originate
  outside the grilling dialogue, weakening provenance.
- **Required at every level including BG** — rejected: BG-level
  consultations would often return little for their cost.
- **Discretionary everywhere** — rejected: quality becomes
  facilitator-dependent, the exact gap IDEA-0003 exists to close.
- **Sonnet 5 or inherited model** — rejected: cheaper or simpler, but
  consultation quality would vary or silently degrade.

## Implications

`.claude/agents/system-architect.md` joins the repo alongside the
system-architecture-bp companion skill (DEC-0294); the agent is
unusable until the DEC-0295 corpus is ratified. The
refinement-process playbooks gain the required consultation step at
EP/ST/CMP refinement and gate prep, and the vendored .agents skill
copy syncs in the same session. At component gate prep the two
required steps compose in fixed order: the system-architect review
consultation runs **first**, then the DEC-0136 element-graduation
review — architecture critique may reshape design elements, and the
graduation review is the final structural checklist against the
settled draft, immediately before gating. Both remain separate,
explicitly-walked required checklist items (recall-audit finding,
ratified SES-0054 @ T17-T18).
