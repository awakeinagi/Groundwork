---
name: groundwork-overview
description: Write or refresh the frontmatter `overview:` field on a Groundwork artifact (docs/specs/SPEC-artifact-common.md; DEC-0284..DEC-0288) — a self-sufficient, ≤250-word summary every artifact of every type must carry. Use for same-edit updates when an artifact's meaning changes, drift repair on an existing overview, writing one from scratch, or bulk regeneration across many files. Typically loaded explicitly by another skill or agent (e.g. the overview-writer agent, or a Groundwork editing workflow) rather than triggered by conversational context — load it by name whenever you are about to touch an `overview:` field.
---

# Groundwork Overview

Every Groundwork artifact — goal, epic, story, spike, component, session,
decision, conflict, change proposal, idea, consolidation — carries a
frontmatter `overview:` field: the progressive-disclosure entry point an
agent reads before deciding whether the body is worth opening at all
(DEC-0284). It exists so batch triage over dozens of artifacts costs a
cheap YAML parse instead of dozens of full-file reads.

This skill has one job: produce a correct `overview:` field and prove it's
correct. You (the model) write the prose — that's a judgment call about
what matters in the artifact. The two bundled scripts handle everything
mechanical around that judgment call, and you should let them, rather than
hand-editing the YAML:

- **`scripts/set_overview.py`** inserts or replaces the field, in the
  right place, correctly formatted, touching nothing else in the file.
- **`scripts/validate_overview.py`** checks the result against the actual
  rule the project's integrity checker enforces (rule 19 of
  `tools/check_links.py`) — presence, the 250-word cap, and that every
  bare artifact ID inside it resolves.

Hand-editing frontmatter YAML is exactly the kind of mechanical step that
silently breaks (wrong indent, a block scalar that swallows the next key,
an off-by-one in the word count) without either script or human noticing
until the checker runs later, out of context. Routing through both scripts
turns those failure modes into an immediate, explicit error.

## The standard (DEC-0284, DEC-0285, DEC-0286, DEC-0288)

- **Derived, non-normative.** An overview is a faithful summary of what
  the file already says — never a new claim, never interpretation beyond
  the text. The body always wins on conflict, and because of that,
  writing or fixing one is never a semantic change: it's legal on closed
  sessions and accepted decisions, and requires no session, gate, or
  re-approval of its own.
- **Self-sufficient plain prose, at most 250 words** (aim for 60–150 on
  most artifacts — reach for the ceiling only on genuinely dense ones,
  like a long session transcript or a component with a large element
  inventory). Readable with zero other context: what the artifact is, its
  core content or outcome, and its current disposition (e.g. "deferred
  behind TRG-0010", "gated, awaiting eng-lead sign-off", "superseded by
  DEC-0200").
- **No markdown formatting.** Bare artifact IDs (`DEC-0050`, `EP-0005`)
  are fine — but only ones that already appear somewhere in the file
  you're summarizing. Never introduce an ID from memory or from a related
  artifact you happen to know about; that would be adding a claim the
  file itself doesn't make.
- **Same-edit rule (DEC-0288).** Any edit that changes an artifact's
  meaning updates its overview in the same edit — an edit that leaves the
  overview stale is an incomplete edit. If you're loading this skill
  because you just changed a status, a decision's text, a story's
  acceptance criteria, etc., that's the trigger: write/refresh the
  overview before you consider the edit done.

## Per-type guidance

One line of what the overview should center on, per type (full templates
in the design-session skill's `references/templates.md` if you want the
worked examples):

| Type | Overview centers on |
|---|---|
| Business Goal | the business intent, who it serves, headline outcomes, current standing |
| Epic | what it delivers and for whom, its bounded context, where it stands (derived work, open risks) |
| Story | the change and its value, the shape of its acceptance criteria, components touched, disposition |
| Spike | the research question, why it blocks sibling work, and — once complete — the answer and resulting decisions |
| Component | what it is, what its contract covers (element inventory in broad strokes), refinement state |
| Session | what it set out to refine, what it settled, what it produced (decisions, ideas, conflicts) |
| Decision | the decision in one breath, plus what it constrains or unlocks downstream |
| Conflict | the tension, the parties and their intents, the mediation/resolution state |
| Change Proposal | the proposed change, where it arose, its triage state |
| Idea | the idea in brief, its spark context, its disposition |
| Consolidation | the graph neighborhood covered, for which audience, freshness state |

## Workflow

1. **Read the target file** in full (body included, not just frontmatter)
   — the overview must be faithful to content you've actually seen, and
   any bare ID you use in it has to already appear in the file.
2. **Compose the overview text** as plain prose, following the standard
   and the per-type line above. Don't worry about line width or where in
   the frontmatter it goes — the script handles both.
3. **Write it into the file** with `set_overview.py`. Pass the text
   through a scratch file rather than a shell argument (multi-sentence
   prose with punctuation is painful to quote safely on a command line):

   ```
   python3 scripts/set_overview.py <artifact-path> --text-file <scratch-text-path>
   ```

   This strips any existing `overview:` field, wraps your text into a
   YAML folded block scalar, and inserts it at the position every
   real Groundwork artifact uses — immediately before whichever of
   `component-type:` / `links:` / `sources:` comes first. Nothing else
   in the file changes.
4. **Validate it**:

   ```
   python3 scripts/validate_overview.py <artifact-path>
   ```

   If it fails — over the word cap, or a bare ID that doesn't
   resolve — that's real signal that your prose needs revision (trim it,
   or drop the unresolvable reference). Fix the *text* and re-run step 3;
   never hand-patch the YAML to silence a validation failure.
5. **Report** which files got a clean `ok` and which didn't, with the
   specific reason for any that failed — don't just say "done."

## Bulk usage

For many files at once, either loop steps 1–4 per file, or (files already
known, no per-file judgment needed beyond composing text) validate a
whole batch in one call: `validate_overview.py <file1> <file2> ...` or
`--all` to sweep every artifact under `<root>/docs`. For large batches
(dozens+), fan out across parallel subagents, each covering a partition
of files and each independently running this same read → compose → write
→ validate loop — this is what `.claude/agents/overview-writer.md` does.
If you're one of those subagents: touch only your assigned files, never
run git operations, and never guess at another file's content to save a
read.
