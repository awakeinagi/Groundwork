---
id: DEC-0346
type: decision
title: "The method track's pattern is permanent; only its implementation may be swapped"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-10
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-10
source-span: "SES-0060 @ T1-T3"
overview: >-
  Narrows DEC-0338's "sacrificial by design" framing without
  reversing it: the method track's design pattern — mandatory
  delegation through a governed subagent, contract-restricted corpus
  access, gate-enforced agent/tool contracts — is a permanent
  decision BG-0001's application is expected to implement natively,
  inheriting this track's already-gated contracts rather than re-
  deciding them. What remains provisional is narrower: today's
  specific implementation (a CLI script plus a Claude-Code-specific
  subagent) may later be rebuilt as a native application feature —
  an implementation swap behind a stable pattern, not disposal of
  the pattern. Per-component absorption triggers in docs/TRIGGERS.md
  now describe when an implementation may be retired, never when the
  capability is discontinued. Chosen over full DEC-0338 supersession
  (disproportionate — only the sacrificial clause was wrong) and
  over "nothing is temporary" (the stakeholder confirmed the
  specific implementation may still change).
links:
  derives-from: [SES-0060]
  relates-to: [DEC-0338]
---

# DEC-0346: The Method Track's Pattern Is Permanent; Only Its Implementation May Be Swapped

## Context

DEC-0338 charters BG-0002 as "sacrificial by design": each method
component carries an absorption clause, decommissioned when the
BG-0001 application ships the absorbing capability. Deriving the
pending Artifact Interaction Surface epic (DEC-0339) surfaced the
question of which BG-0001 epic absorbs the librarian —
and the stakeholder corrected the premise: the librarian and skill (or
the pattern they embody) are meant to become part of the main
application, not be thrown away.

## Decision

DEC-0338's "sacrificial by design" framing is narrowed, not reversed:
the method track's **design pattern** — mandatory delegation through a
governed subagent, corpus interaction restricted to a typed contract
API, gate-enforced agent/tool contracts — is a **permanent** decision.
BG-0001's application is expected to implement this pattern natively,
inheriting the already-gated contracts this track produces rather than
re-deciding delegation and write-authority from scratch. What remains
genuinely provisional is narrower: today's **specific implementation**
— a CLI script plus a Claude-Code-specific subagent — may be rebuilt
as a native application feature once BG-0001 ships it. That is an
implementation swap behind a stable pattern, not disposal of the
pattern itself. Per-component absorption clauses (armed triggers in
docs/TRIGGERS.md) still apply, but they now describe *when an
implementation may be retired*, never *when the pattern is
discontinued*.

## Rationale

Conflating "the tooling" (implementation) with "the capability"
(pattern) in DEC-0338 implied the whole thing gets discarded, which
misrepresents the intent: this track's contracts and decisions are
meant to carry forward into BG-0001's design, not be redone. This is
the ordinary shape of sacrificial architecture done right (build the
pattern now, cheaply; the concrete implementation is what's
disposable) rather than the stronger, incorrect reading BG-0002's text
invited.

## Alternatives Considered

- **Nothing is temporary at all** — rejected; the stakeholder confirmed
  today's specific CLI-plus-subagent implementation may still be
  rebuilt natively, so *something* remains provisional.
- **Full supersession of DEC-0338** — rejected as disproportionate;
  only the sacrificial clause is wrong, the charter's predicate,
  non-goals, and outcomes stand unchanged. A narrowing decision
  (precedent: DEC-0138 narrowing DEC-0116) fits the actual scope of
  the correction.

## Implications

BG-0002's Conflicts & Tensions section is edited in the same session
to reflect this narrowing. Absorption-trigger language in future
Component Docs under this track should name what may be rebuilt
(implementation), not imply the capability disappears. The pending
epic's absorption-mapping question (which BG-0001 epic eventually
hosts a native equivalent of today's implementation) is deferred to
that epic's derivation session, now correctly framed as "which epic
may someday rebuild this implementation," not "which epic makes this
agent unnecessary."
