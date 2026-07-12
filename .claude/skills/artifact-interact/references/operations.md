# Write operations reference (DEC-0313, DEC-0314, DEC-0315; guards: DEC-0376..DEC-0386)

All operations: `python3 scripts/gw.py --root <project> write <op> …`.
Add `--json` after `--root <project>` for structured results. Exit
codes: 0 ok, 1 refused/invalid (message starts `REFUSED:` and names the
sanctioned alternative where one exists), 2 setup problem.

**Read this file instead of the scripts' source.** It is kept in sync
with the code; if an op behaves differently from what is written here,
that mismatch is itself a defect worth reporting.

## Concurrency (DEC-0391; SES-0079, DEC-0411..DEC-0416)

- **Writes serialize at the apply moment, not the task level.** Every
  write op runs its whole span — corpus scan, ID allocation, edits,
  reciprocity, recheck, graph sync — under an exclusive `flock` on
  `<root>/.groundwork-lock`; reads take the same lock shared. Parallel
  write invocations are safe: they queue (writes wait up to 60s, reads
  10s; `GW_LOCK_TIMEOUT` overrides) and a timeout refuses cleanly
  naming the holder's PID — retry, don't force.
- **Applies are transactional.** Any failure (refusal, recheck, crash)
  rolls the corpus back to its pre-op state from the journal at
  `<root>/.groundwork-journal/`; "file written, fix required" is dead —
  a refused write leaves nothing behind. After a hard crash the next
  write op recovers automatically; `write recover` does it standalone
  when a read warns about an interrupted apply.
- **Content edits carry version tokens** (`--if-match`, DEC-0413) and
  **turn numbers are tool-assigned** (DEC-0414) — see edit-section,
  update-overview, and append-turn below.

## Structural guards (SES-0072 — apply across ops)

- **Payloads are body-only.** `edit-section` and `append-turn` refuse
  content containing a markdown heading line at the target section's
  level or higher (DEC-0376). The tool owns heading lines. Fenced code
  blocks and inline backtick code are exempt from every structural scan.
- **Ratifying transitions are gated.** `set-status` to `approved`,
  `accepted`, or `closed` refuses while the body carries duplicate
  same-level headings under one parent, or placeholder lines — a
  standalone `TBD`/`TODO`/`FIXME` (optional punctuation) or an
  unallocated ID like `SES-XXXX` (DEC-0378). To *mention* a placeholder
  token legitimately, wrap it in backticks.
- **Frontmatter must parse as YAML.** The post-write recheck validates
  the touched file's frontmatter via PyYAML when available (DEC-0386).
- **Body H1s carry the artifact's own ID.** Author pre-allocation
  bodies with `# <PREFIX>-XXXX: <title>` — `create` stamps the
  allocated ID (DEC-0384); a mismatched or placeholder H1 fails the
  recheck and checker rule 24.

## create

```bash
gw.py --root . write create --type decision --title "…" \
  --overview "…(≤250 words)…" \
  --link derives-from=SES-0059 --link relates-to=DEC-0312,DEC-0313 \
  --cite DEC-0029 --field 'decided-by: name' --field 'source-span: "SES-0059 @ T3"' \
  --status accepted \
  --from-file body.md        # omit for a template-seeded body
```

- Allocates the next sequential ID for the type's prefix; never reuses.
- Filename `<ID>-<kebab-slug>.md` in the type's directory.
- Default status: `draft` (gate types), `proposed` (decision), `open`
  (session/conflict), `captured` (idea). `--status accepted` is legal
  for decisions confirmed in-session.
- A `--from-file` body whose first line is `# <PREFIX>-XXXX: …` gets
  the allocated ID stamped into the H1 (DEC-0384).
- Refuses: missing/oversized overview; a decision without
  `derives-from` a SES/SP (integrity rule 4); unknown link targets;
  impact links to a different type. Impact links write the reciprocal
  edge into the other file.
- **Gate-required, create-only fields are demanded at creation**
  (SES-0081): types whose later lifecycle gates require fields that no
  op can add after creation must supply them via `--field` now —
  currently sessions need all four of `participant`,
  `participant-role`, `facilitator`, `transcript-fidelity` (the close
  gate demands them). The refusal names what's missing; future types
  are one `REQUIRED_AT_CREATE` table row.
- After creating a decision that derives from a session, **add the
  session-side mirror**: `add-link <SES> relates-to <DEC>` (checker
  rule 23, DEC-0382) and reference the DEC by literal ID in the
  session's body prose (rule 18). Cross-link tightly coupled sibling
  decisions (`relates-to`, both directions) at creation time.

## set-status

```bash
gw.py --root . write set-status EP-0009 gated
gw.py --root . write set-status EP-0009 approved --approved-by awakeinagi
gw.py --root . write set-status DEC-0369 accepted --session SES-0073
gw.py --root . write set-status SES-0068 closed --no-decisions-ok "idea-capture session (DEC-0258)"
gw.py --root . write set-status ST-0066 deferred --release backlog
```

- Validates the transition against the type's lifecycle (gate types per
  SPEC-artifact-common; reduced lifecycles for decision, session, idea,
  conflict). Change proposals are refused (they use `triage`).
- `approved` stamps `approved-by`/`approved-on`. `deferred` is
  ST/EP/SP-only and requires a `release`. `superseded` requires
  `--superseded-by NEW-ID` (decisions: prefer `supersede`).
- **`accepted` on a decision requires `--session SES-nnnn`** and stamps
  `accepted-in` — the ratification site of a later-accepted decision
  (DEC-0383). Decisions *created* with `--status accepted` need no
  stamp; `derives-from` already names the session.
- **Session close preconditions (DEC-0380, DEC-0381):** frontmatter
  must carry `participant`, `participant-role`, `facilitator`, and
  `transcript-fidelity`; and at least one decision must derive from the
  session, else pass `--no-decisions-ok "<reason>"` — the flag is the
  recorded zero-decision assessment. When a close is refused for zero
  decisions, surface the warning to the caller; never invent the flag.
- All three ratifying targets run the structural gate (see guards).

## add-link / add-cite

```bash
gw.py --root . write add-link EP-0009 impacts EP-0004   # reciprocates
gw.py --root . write add-link SES-0072 relates-to DEC-0376
gw.py --root . write add-cite ST-0066 DEC-0335
```

- Closed link vocabulary; `impacts`/`impacted-by` enforce same-type and
  write both sides. **`relates-to` does NOT auto-reciprocate** — add
  the reverse edge explicitly where wanted.
- Accepted decisions accept only `relates-to` enrichment (DEC-0248);
  anything else directs to `supersede`.
- A cite added to frontmatter creates a body-prose obligation (DEC-0247)
  — reference the DEC in prose too. A session's `relates-to` entries
  must be referenced in its body prose by literal ID (rule 18) — a
  compressed range ("DEC-0376 through DEC-0385") does not count.

## remove-cite (SES-0077, DEC-0403)

```bash
gw.py --root . write remove-cite ST-0066 DEC-0335
gw.py --root . write remove-cite SP-0014 DEC-0014 --amend  # approved/stale
```

- The sanctioned dead-cite repair (DEC-0247): removes one DEC from
  `cites:` (dropping the line when emptied). Refuses while the body
  prose still references the DEC — rework the body mention first, or
  earlier in the same batch; code-span quotations do not block.
- Immutability mirrors edit-section: accepted decisions and closed
  sessions refuse outright; `approved`/`stale` artifacts require
  `--amend`.

## update-overview

```bash
echo "…new overview…" | gw.py --root . write update-overview DEC-0335 --if-match v:1a2b3c4d5e6f
gw.py --root . write update-overview DEC-0335 --text "…" --if-match v:… # short texts
```

- ≤250 words, IDs must resolve. Legal on any artifact, including
  accepted decisions and closed sessions — overviews are derived and
  non-normative (DEC-0285).
- **`--if-match <token>` is required** (DEC-0413) unless the same
  invocation/batch created the artifact: `read overview <ID>` prints
  the current token; a mismatch means the overview changed since your
  read — re-read and recompose.
- **Batch key is `text` or `content`, never `overview`** (see apply).

## edit-section

```bash
gw.py --root . write edit-section ST-0066 "Acceptance Criteria" --if-match v:… --from-file new.md
gw.py --root . write edit-section SP-0002 "Findings" --occurrence 2 --if-match v:… --from-file fix.md
```

- Replaces one section's BODY (heading kept — never include the heading
  line in the payload; the guard refuses it, DEC-0376). Content is
  matched by case-insensitive heading substring; `--occurrence N`
  targets the Nth match (structural repair; default 1).
- **`--if-match <token>` is required** (DEC-0413) unless the same
  invocation/batch created the artifact: `read section <ID> "<heading>"
  [--occurrence N]` prints the section's current token (outline shows
  every `##` section's token). A mismatch means the section changed
  since your read — re-read and recompose; never retry blind.
- Refuses accepted/superseded decisions (→ `supersede`) and closed
  sessions (→ `append-turn --enrichment`, or a new session).
  `approved`/`stale` artifacts require `--amend` — the caller asserts a
  session sanctions the edit. If meaning changed, `update-overview` in
  the same change (DEC-0288); pass `--overview-ok` to silence the
  reminder.

## delete-section (recovery op — DEC-0377)

```bash
gw.py --root . write delete-section SP-0015 "Resulting Decisions" --occurrence 1 --amend
```

- Removes a heading and its span entirely — the sanctioned repair for
  phantom-heading duplicates. Refuses deleting the **last** occurrence
  of a section the artifact's type requires (duplicates are deletable,
  the template is not). Same immutability preconditions as
  edit-section (closed sessions, accepted decisions; `--amend` for
  approved/stale).

## append-turn

```bash
gw.py --root . write append-turn SES-0059 --from-file turn.md
gw.py --root . write append-turn SES-0058 --enrichment --from-file xref.md
```

- Open session: appends at the end of the Transcript section. Turn
  content may use `###`-level headings (`### T9 — …`) but is refused if
  it contains `##`-level lines (DEC-0376).
- **Turn numbers are tool-assigned** (DEC-0414): the writer reads the
  live transcript maximum under the lock and renumbers your payload's
  turn headings to continue from it, reporting what it assigned in the
  OK line (`assigned T7-T9`) — compose with any numbers, they are
  provisional. Pass `--expect-first-turn N` to refuse cleanly if the
  transcript advanced past where you composed.
- Closed session: refused unless `--enrichment`, which appends under a
  dated `### Post-Close Enrichment` subsection (DEC-0248). Transcript
  turns themselves are never edited.
- **Known gap:** the old workaround for adding a missing required
  section (append-turn content opening with the new `##` heading) is
  dead — the guard refuses it. There is currently NO sanctioned path to
  add a missing top-level section; refuse-and-report, citing IDEA-0042.

## supersede

```bash
gw.py --root . write supersede DEC-0333 --title "…" --overview "…" \
  --session SES-0059 --source-span "SES-0059 @ T4-T5" [--from-file body.md]
```

- Creates the new accepted decision (`supersedes: [old]`,
  `derives-from` the session), flips the old to `superseded` with the
  `superseded-by` backlink, and prints ratified citers of the old
  decision as the stale-walk hint — run `graph impact <old>` for the
  full walk.

## apply — JSON batch (DEC-0314)

```bash
gw.py --root . write apply ops.json
```

`ops.json` is a list of operation objects: `"op"` plus that operation's
**argparse attribute names** as keys (dashes tolerated — they are
normalized to underscores). Positional arguments use their names (`id`,
`status`, `heading`, `rel`, `target`). `content` may replace
`--from-file` for any payload-taking op. The batch validates as a unit:
IDs and re-checks defer to the end so members may reference each other.

**Pre-validation (DEC-0400):** the whole batch is checked before
anything applies — an unknown op name, an unknown batch key (e.g. the
CLI-style `link` string), or a malformed `links` value (non-dict, rel
outside the closed vocabulary, non-list targets) refuses the entire
batch with nothing written.

**Failure accounting (DEC-0401) + rollback (DEC-0412):** per-op `OK`
lines are flushed as each op lands; an apply-time refusal stops the
batch, prints a manifest (`applied N of M; not attempted: …; rolling
back`), and then the **whole batch rolls back** — ops that had already
landed are restored too, so a failed batch leaves the corpus
byte-identical to before it started. The terminal line
`apply: applied N/N; post-batch validation clean` is the success
signal — if it is missing, nothing from the batch is on disk: fix the
failing op and re-run the **entire** batch.

**Batch key table (the traps in bold):**

| op | keys |
|---|---|
| create | type, title, overview, status, owner, **links** (a DICT: `{"derives-from": ["SES-…"], "relates-to": […]}` — the CLI's `link` string form is **refused**, DEC-0400), cites (list), field (list of `"key: value"`), content or from-file |
| set-status | id, status, approved-by, superseded-by, release, session, no-decisions-ok |
| add-link | id, rel, target |
| add-cite | id, target |
| remove-cite | id, target, amend |
| update-overview | id, **text** (or content), if-match — the key `overview` does not exist and fails with "provide overview text" |
| edit-section | id, heading, occurrence, amend, overview-ok, content or from-file, if-match |
| delete-section | id, heading, occurrence, amend |
| append-turn | id, enrichment, content or from-file, expect-first-turn |
| supersede | id, title, overview, session, source-span, owner, cites, content or from-file |

```json
[
  {"op": "create", "type": "idea", "title": "…", "overview": "…",
   "links": {"derives-from": ["SES-0059"]},
   "field": ["proposed-by: name"]},
  {"op": "append-turn", "id": "SES-0059", "content": "**T9 — …**"},
  {"op": "update-overview", "id": "SES-0059", "text": "…"},
  {"op": "set-status", "id": "SES-0059", "status": "closed",
   "no-decisions-ok": "idea-capture session (DEC-0258)"}
]
```

A wrong batch key now refuses the whole batch instead of being
silently ignored (DEC-0400). The verification habit still matters
after an abnormal end (timeout, kill): the flushed per-op lines are
the truthful record of what landed (DEC-0401) — diff-verify each
target rather than assuming all-or-nothing.

## Validation layering (DEC-0315, DEC-0386)

Per-op: preconditions before disk; targeted re-check of touched files
after (frontmatter parses as YAML when PyYAML is available, typed
frontmatter fields against the FIELD_SCHEMA table — enums, dates,
scalar shapes — per DEC-0402, ID/filename match, link resolution with
body IDs scanned code-span-aware per DEC-0399 while overview IDs must
always resolve per DEC-0398, overview cap, reciprocity of touched
pairs, body-H1 identity). The **full checker** (`gw.py --root . check`) stays
the pre-commit gate — it additionally enforces prose obligations (cite
referenced in body per DEC-0247, impact edges explained per DEC-0249,
session relates-to mentions per DEC-0250, produced-decision back-links
per rule 23, duplicate-heading/placeholder rules 21-22, coverage/
tracing) that per-op checks deliberately do not. Note: the per-op
recheck is not code-span-aware for bare-ID resolution (IDEA-0022) —
backticked example IDs can false-positive there while the full checker
stays clean.
