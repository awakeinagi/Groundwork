# Write operations reference (DEC-0313, DEC-0314, DEC-0315)

All operations: `python3 scripts/gw.py --root <project> write <op> …`.
Add `--json` after `--root <project>` for structured results. Exit
codes: 0 ok, 1 refused/invalid (message starts `REFUSED:` and names the
sanctioned alternative where one exists), 2 setup problem.

## create

```bash
gw.py --root . write create --type decision --title "…" \
  --overview "…(≤250 words)…" \
  --link derives-from=SES-0059 --link relates-to=DEC-0312,DEC-0313 \
  --cite DEC-0029 --field 'decided-by: name' --field 'source-span: "SES-0059 @ T3"' \
  --from-file body.md        # omit for a template-seeded body
```

- Allocates the next sequential ID for the type's prefix; never reuses.
- Filename `<ID>-<kebab-slug>.md` in the type's directory.
- Default status: `draft` (gate types), `proposed` (decision), `open`
  (session/conflict), `captured` (idea).
- Refuses: missing/oversized overview; a decision without
  `derives-from` a SES/SP (integrity rule 4); unknown link targets;
  impact links to a different type. Impact links write the reciprocal
  edge into the other file.
- Body via `--from-file` (or `--from-file -` for stdin); the default is
  a skeleton with the type's required sections.

## set-status

```bash
gw.py --root . write set-status EP-0009 gated
gw.py --root . write set-status EP-0009 approved --approved-by awakeinagi
gw.py --root . write set-status ST-0066 deferred --release backlog
```

- Validates the transition against the type's lifecycle (gate types per
  SPEC-artifact-common; reduced lifecycles for decision, session, idea,
  conflict). Change proposals are refused (they use `triage`).
- `approved` stamps `approved-by`/`approved-on`. `deferred` is
  ST/EP/SP-only and requires a `release`. `superseded` requires
  `--superseded-by NEW-ID` (decisions: prefer `supersede`, which does
  everything).

## add-link / add-cite

```bash
gw.py --root . write add-link EP-0009 impacts EP-0004   # reciprocates
gw.py --root . write add-cite ST-0066 DEC-0335
```

- Closed link vocabulary; `impacts`/`impacted-by` enforce same-type and
  write both sides. Accepted decisions accept only `relates-to`
  enrichment (DEC-0248); anything else directs to `supersede`.
- A cite added to frontmatter creates a body-prose obligation (the full
  checker enforces per DEC-0247) — reference the DEC in prose too.

## update-overview

```bash
echo "…new overview…" | gw.py --root . write update-overview DEC-0335
```

- ≤250 words, IDs must resolve. Legal on any artifact, including
  accepted decisions and closed sessions — overviews are derived and
  non-normative (DEC-0285).

## edit-section

```bash
gw.py --root . write edit-section ST-0066 "Acceptance Criteria" --from-file new.md
```

- Replaces one section's content (heading kept). Refuses accepted/
  superseded decisions (→ `supersede`) and closed sessions (→
  `append-turn --enrichment`, or a new session). `approved`/`stale`
  artifacts require `--amend` — the caller asserts a session sanctions
  the edit. If meaning changed, `update-overview` in the same change
  (DEC-0288); pass `--overview-ok` to silence the reminder.

## append-turn

```bash
gw.py --root . write append-turn SES-0059 --from-file turn.md
gw.py --root . write append-turn SES-0058 --enrichment --from-file xref.md
```

- Open session: appends at the end of the Transcript section.
- Closed session: refused unless `--enrichment`, which appends under a
  dated `### Post-Close Enrichment` subsection (DEC-0248). Transcript
  turns themselves are never edited.

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

`ops.json` is a list of operation objects: the `op` name plus that
operation's flags as keys (kebab-case as in the CLI), with `content`
allowed inline in place of `--from-file`:

```json
[
  {"op": "create", "type": "idea", "title": "…", "overview": "…",
   "field": ["proposed-by: name"]},
  {"op": "append-turn", "id": "SES-0059", "content": "**T9 — …**"},
  {"op": "set-status", "id": "SES-0059", "status": "closed"},
  {"op": "update-overview", "id": "SES-0059", "content": "…"}
]
```

Operations apply in order; the first refusal stops the batch (earlier
operations remain applied — order transactions so prerequisites come
first).

## Validation layering (DEC-0315)

Per-op: preconditions before disk; targeted re-check of touched files
after (parseability, ID/filename match, link resolution, overview cap,
reciprocity of touched pairs). The **full checker**
(`gw.py --root . check`) stays the pre-commit gate — it additionally
enforces prose obligations (cite referenced in body per DEC-0247,
impact edges explained per DEC-0249, coverage/tracing rules) that
per-op checks deliberately do not.
