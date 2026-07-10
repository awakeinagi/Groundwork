---
id: IDEA-0016
type: idea
title: "Reconcile the system-architect model-invocation mechanism"
status: taken-up
owner: awakeinagi@gmail.com
created: 2026-07-10
proposed-by: awakeinagi
overview: >-
  The system-architect agent's frontmatter already reads model
  claude-opus-4-6, effort high — the literal change requested
  already exists. The real open question is narrower: DEC-0292
  requires the model be pinned in frontmatter AND passed explicitly
  at every spawn, and this session's own consultations passed the
  alias "fable" rather than the literal claude-opus-4-6 string. A
  future session should verify what "fable" resolves to, and
  reconcile the frontmatter pin and spawn-time practice so they
  agree.
links:
  derives-from: [SES-0061]
  relates-to: [DEC-0292, DEC-0329, IDEA-0023]
---

# IDEA-0016: Reconcile the System-Architect Model-Invocation Mechanism

## The Idea

Verbatim: "We need to switch the architect subagent to use
`claude-opus-4-6` with high effort. We can set that in the frontmatter
of the agent's .md file."

## Spark Context

Checked at capture time: `.claude/agents/system-architect.md`'s
frontmatter already reads `model: claude-opus-4-6` and `effort: high`
— the literal change requested already exists on disk. The genuinely
open question is narrower and was not what the stakeholder's wording
implied: DEC-0292 requires the strongest available model be "pinned
in the agent definition's frontmatter AND passed explicitly at every
spawn — the frontmatter pin alone has been observed not to take
effect," and every system-architect consultation run so far in this
session's own work passed the explicit spawn-time alias `"fable"`
(per DEC-0292's own documented alias wording, "model 'fable', or the
strongest then available"), not the literal string
`claude-opus-4-6`. Whether `"fable"` and `claude-opus-4-6` name the
same underlying model, whether the alias is the intended long-term
mechanism or drift to reconcile, and whether the frontmatter string
should be updated to match actual spawn practice are the real
questions a future session should settle.

## Disposition

## Disposition

Taken up by SES-0062. That session pulled this idea's full payload and
found the literal requested change already existed in
`.claude/agents/system-architect.md` frontmatter; the real gap —
whether DEC-0292's spawn-time practice (the alias `"fable"`) matches
its own frontmatter-pin mandate — was investigated there. The
investigation went deeper than a naming reconciliation: it surfaced
that DEC-0292's premise is empirically contradicted and its mandated
explicit-override practice itself silently drops reasoning effort (see
IDEA-0023). This idea's own literal ask turned out moot (already true
on disk) and its real underlying concern is now tracked and superseded
in scope by IDEA-0023, which a future session should read first before
resolving either idea. No further action against this idea itself;
IDEA-0023 carries the open work.

Update (2026-07-10): a diagnostic investigation prompted by taking up
this idea found the underlying premise runs deeper than "which alias
resolves to what" — see IDEA-0023, which found DEC-0292's explicit-
override mandate itself is backwards (it silently drops reasoning
effort; the frontmatter-only path it distrusts actually preserves
both model and effort) and separately confirmed `claude-opus-4-6` is
not a real Anthropic model identifier. A future session resolving
this idea should read IDEA-0023 first.

