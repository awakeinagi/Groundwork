---
name: artifact-interact
description: Groundwork corpus artifact toolbelt (reads, semantic search, graph queries, guardrailed typed writes) via the unified gw CLI. EXPLICIT LOAD ONLY — never load this skill because conversational context mentions artifacts, documentation, or Groundwork; it does not serve ad-hoc triggering (DEC-0326). It is loaded exclusively by (a) the artifact-librarian agent, whose toolbelt this is, (b) another agent definition that explicitly charters it (DEC-0327), or (c) a direct operator instruction naming this skill. Every other agent interacts with Groundwork artifacts by spawning the artifact-librarian subagent instead (DEC-0325).
---

# artifact-interact

The single home of every artifact-touching ability in a Groundwork
project (DEC-0310): concise reads, hybrid semantic search, the graph
index, consistency and coupling checks, the status report, the full
integrity checker — and the **typed write API that is the sole
sanctioned way to mutate corpus artifacts** (DEC-0312). The API is
Groundwork-specific and SPEC-driven: `docs/specs/SPEC-*.md` is the
normative basis for everything it validates (DEC-0311).

If you are reading this without being the artifact-librarian agent, a
definition-chartered agent, or under a direct operator instruction:
stop — spawn the `artifact-librarian` agent (model: sonnet, passed
explicitly) with a task-level intent instead (DEC-0325, DEC-0329).

## The unified CLI (DEC-0316)

One entry point, subcommand families, uniform `--root`:

```bash
python3 <skill-dir>/scripts/gw.py --root <project> <family> [args...]
```

| Family | Runs via | What it serves |
|---|---|---|
| `read` | python3 | overview, outline, section, element, item, turns, term, citers |
| `write` | python3 | create, set-status, add-link, add-cite, update-overview, edit-section, delete-section, append-turn, supersede, apply |
| `check` | python3 | the full integrity suite — the pre-commit gate (DEC-0315) |
| `status` | python3 | project status report (counts, open items, frontier, mode) |
| `consistency` | python3 | post-distillation `sweep` and `terms` checks |
| `coupling` | python3 | sibling impact-coupling check (`--type story` for story sets) |
| `search` | uv | hybrid semantic search, `similar`, recall `audit` |
| `graph` | uv | LadybugDB openCypher: `trace`, `impact`, `gaps`, `order`, `query`, … |

Dependencies are layered (DEC-0317): read/write/check/status/
consistency/coupling are pure stdlib; search and graph resolve their
engines through `uv run` only when invoked. `gw.py <family> --help`
gives each family's full usage.

## Reading: progressive disclosure first

Read overviews before bodies; a `read overview` batch or a search hit
list frequently answers the question with zero file opens. Whole-file
reads are for artifacts being actively edited or gated.

## Writing: the guardrailed path (DEC-0312, DEC-0313)

Every mutation goes through `write`. Operations validate their
preconditions against the SPECs before touching disk, do their
bookkeeping atomically (ID allocation, reciprocity, approval/
supersession stamping), re-validate what they touched (DEC-0315), and
print a compact result — do not re-read the file to confirm. Refusals
name the sanctioned alternative (e.g. editing an accepted decision
directs to `supersede`); report refusals to your caller rather than
improvising around them.

Payloads are finished prose: complete sentences with normal
capitalization and punctuation. If a caller's payload opens a sentence
with a label-continuation fragment or a lowercase code identifier,
reword it (or push back) rather than transcribing the fragment
verbatim under a section heading (SES-0072 casing repair).

Long content travels via stdin, `--from-file PATH`, or `--from-file -`
(explicit stdin) — never shell-quoted arguments (DEC-0314). Multi-op
transactions (e.g. close-session = append turns + set status + update
overview) go through `write apply ops.json`; see
[references/operations.md](references/operations.md) for every
operation's flags, invariants, refusal conditions, and batch schema.

Structural guards (SES-0072): section payloads are **body-only** —
`edit-section`/`append-turn` refuse content carrying a heading line at
the target section's level or higher (the IDEA-0041 phantom-heading
defect); repair existing corruption with `edit-section --occurrence N`
or `delete-section` (duplicate occurrences are deletable, a type's
required template is not). Ratifying transitions (`approved`,
`accepted`, `closed`) refuse bodies with duplicate sibling headings or
placeholder lines (TBD/TODO/FIXME, unallocated `…-XXXX` IDs — quote
them in backticks to mention them legitimately). Session close
additionally requires participant/participant-role/facilitator/
transcript-fidelity frontmatter, and either a produced decision or
`--no-decisions-ok "<reason>"` (DEC-0258). Accepting a proposed
decision requires `--session SES-nnnn` (stamped as `accepted-in`).
Bodies given to `create` may write their H1 as `# <PREFIX>-XXXX: …` —
the allocated ID is stamped in.

The full `check` family remains the pre-commit gate: run it before any
commit; per-op re-checks do not replace it. Git itself belongs to the
caller (DEC-0333) — nothing in this skill stages or commits.

## Concurrency (DEC-0391; SES-0079, DEC-0411..DEC-0416)

Read/search/graph invocations parallelize freely and take a shared
lock, so they never observe a torn mid-apply state. Write operations
serialize themselves at the apply moment on an exclusive lock — ID
allocation, edits, reciprocity, recheck, and graph sync are one
transactional unit that rolls back on any failure. Parallel write
invocations are safe: they queue on the lock (60s default,
`GW_LOCK_TIMEOUT` overrides) rather than corrupt. Content edits carry
`--if-match` version tokens and turn numbers are tool-assigned — see
[references/operations.md](references/operations.md) §Concurrency.

## Installing into a project

`install.sh` installs this skill (and the artifact-librarian agent
definition, DEC-0334) project-locally or globally — see
[install.sh](install.sh) usage header. Bootstrap also copies
`scripts/check_links.py` and `scripts/serve_docs.py` into the target
project's `tools/` (DEC-0310).
