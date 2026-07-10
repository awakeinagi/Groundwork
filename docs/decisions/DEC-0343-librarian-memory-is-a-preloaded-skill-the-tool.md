---
id: DEC-0343
type: decision
title: Librarian memory is a preloaded skill; the tool-surface hot-fix is ratified
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0059 @ T14-T18"
overview: >-
  Two ratifications. Hot-fix: the deployed librarian carries no
  memory: frontmatter field — verified against official
  documentation to auto-enable Read/Write/Edit regardless of the
  tools: list, the root cause of the SES-0058 drift — and holds
  exactly its five declared tools. Mechanism: the DEC-0331
  behavioral memory is the artifact-librarian-memory skill, a git-
  tracked SKILL.md preloaded at every spawn via the skills: field
  (injects content, grants no tools), curated by the librarian via
  Bash under written rules (100-line cap, behavioral only, dated);
  it is the only file the librarian may write outside the typed
  write API, and every update is a reviewable diff. Chosen from a
  four-option survey over harness memory (unscopeable full grant),
  the interim notes file (no automatic recall; its .claude/agents/
  location risked being parsed as an agent definition — stakeholder
  catch), and operator-curated memory (agent could not update its
  own). Concretizes DEC-0331; already implemented in commits 6e5004f
  and c77333e.
links:
  derives-from: [SES-0059]
  relates-to: [DEC-0331, DEC-0312, DEC-0334, DEC-0342, DEC-0341, DEC-0337, DEC-0324]
---

# DEC-0343: Librarian Memory as a Preloaded Skill; Tool-Surface Hot-Fix Ratified

## Context

DEC-0331 ratified a learning memory for the librarian and left the
mechanism to the build — where it drifted: the facilitator chose
`memory: project` silently, and (verified at T17 against the official
documentation) that field auto-enables Read/Write/Edit regardless of
the `tools:` list. The stakeholder ordered an immediate fix (T14),
called out the fix's unpresented design (T16), and the corrected
sequence ran: research → option survey → approval (T17-T18).

## Decision

Two parts, both stakeholder-ratified in-session:

1. **Hot-fix:** the deployed librarian definition carries NO `memory:`
   field; its tool surface is exactly the five declared tools (Read,
   Bash, Grep, Glob, Skill). The undiscussed field's removal closes
   the live DEC-0312 tension.
2. **Memory mechanism:** the librarian's DEC-0331 behavioral memory is
   the `artifact-librarian-memory` skill — a git-tracked SKILL.md
   preloaded into the agent at every spawn via its `skills:` list
   (documented to inject content without granting tools). The
   librarian curates that one file via Bash under the rules written in
   it (≤100 entry lines, behavioral only, dated, consolidate at the
   cap); it is the ONLY file the librarian may write outside the typed
   write API. Every memory update is a reviewable git diff. The skill
   ships with the DEC-0334 deliverable; installs never overwrite an
   existing copy (accumulated memory survives upgrades).

Chosen from a four-option survey: harness-managed memory (rejected —
the grant is documented as unscopeable to full Write/Edit), the
interim Bash notes file (rejected — no automatic recall, and its
location under `.claude/agents/` risked being parsed as an agent
definition, a defect the stakeholder caught at T18), and
operator-curated memory (rejected — the agent could not update its own
memory, which the stakeholder required).

## Rationale

The preloaded-skill shape is the only surveyed option with BOTH
automatic recall (memory that is actually in front of the agent every
spawn) and the narrowest achievable write surface. Its residual
weakness — scoping by instruction rather than mechanism — is exactly
what DEC-0341's conformance check and the DEC-0342 contract watch.

## Alternatives Considered

Recorded inline above; the survey itself is the DEC-0337 pattern
applied.

## Implications

Already implemented and committed (repo commits 6e5004f, c77333e) as
this session's expedited steps. The backfill CMP (DEC-0342) contracts
this mechanism as the memory-policy clause. Concretizes DEC-0331; no
supersession — the mechanism was explicitly build territory.
