---
id: SES-0079
type: session
title: "Build intake: the DEC-0391 concurrent-write lock model for gw"
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-12
kind: full
intake: {origin: user, proposed-by: awakeinagi}
participant: awakeinagi
participant-role: stakeholder
facilitator: Claude (Fable 5)
transcript-fidelity: reconstructed
overview: >-
  Build intake for the DEC-0391 shared/exclusive-lock concurrent-
  write model in the gw CLI's write path (SES-0076). The stakeholder
  approved the design and test plan verbatim at T6, producing
  DEC-0411 through DEC-0416; the build landed and was verified live
  by two parallel write-task librarians (T7/T8), retiring the
  DEC-0394 interim single-write-task-librarian rule. Recall audits
  on all six decisions returned five nothing-to-add outcomes and two
  DEC-0414 findings; the stakeholder ratified both dispositions at
  T9/T10, plus a self-containedness preference honored by amending
  EP-0009 to enumerate DEC-0411..DEC-0416 explicitly rather than
  citing DEC-0391 alone. Post-verification housekeeping
  (instruction-surface updates, memory reconciliation) is recorded
  at T10; IDEA-0054 was captured from a recall-audit judge's finding
  about the search-audit packet's considered field. Session closed
  at T11.
links:
  relates-to: [DEC-0391, DEC-0394, DEC-0411, DEC-0412, DEC-0413, DEC-0414, DEC-0415, DEC-0416, IDEA-0054]
---

# SES-0079: Build intake — the DEC-0391 concurrent-write lock model for gw

## Purpose

Take up build intake for the DEC-0391 shared/exclusive-lock concurrent-write model in the gw CLI's write path, replacing the DEC-0394 interim single-write-task-librarian rule once the build ships and is verified.

## Transcript

### T1 (stakeholder awakeinagi)

Let's implement the lock build for DEC-0391

### T2 (facilitator)

Restated: implement the ratified DEC-0391 concurrent-write lock model in the gw CLI tooling, replacing the DEC-0394 interim operating rule (one write-task librarian at a time). This is build intake under DEC-0335/DEC-0345: a written design including its test plan will be presented and approved before anything executable is built. Alignment pending.

### T3 (facilitator)

Code reconnaissance of the gw write path grounded the design: no locking exists anywhere in the scripts; `Artifact.write` is a bare in-place `write_text` with no atomicity; batch apply pre-validates but leaves partial writes on disk on mid-batch failure, with the code comment at the op_apply failure path explicitly deferring rollback to the DEC-0391 machinery; ID allocation is an in-memory max-scan that races across processes (the SES-0078/SES-0079 H1 collision earlier this same day is a live instance); reads emit no version information; turn numbers are caller-embedded with no precondition; graph/search sync is fully out-of-band. The facilitator presented the written design and test plan (distilled below as this session's decisions) per DEC-0335/DEC-0345, with SES-0076's mechanism comparison standing as the DEC-0337 option survey per DEC-0395.

### T4 (stakeholder awakeinagi)

"Would it be possible to use a context manager in the python script around the actual write operations so the lock can be released when the write ops are done instead of waiting for the OS to clean up after the process?"

### T5 (facilitator)

Confirmed the lock helpers are context managers releasing explicitly at block exit — flock LOCK_UN plus descriptor close the moment the with-block ends; OS release-on-death is only the crash fallback. Accepted as a design amendment: the exclusive lock wraps the apply span precisely (corpus scan through graph sync, since ID allocation reads the scan) rather than the whole command execution, with argument parsing and output formatting outside it; tightest-possible scoping around bare writes alone was rejected because the lock must cover the read-modify-write unit or the allocation race returns.

### T6 (stakeholder awakeinagi)

"Approved"

### T7 — Facilitator: build record

Build record: the DEC-0391 machinery landed. New module `gw_lock.py` (fcntl.flock shared/exclusive context managers on `.groundwork-lock`, explicit release at block exit; journal-based all-or-nothing applies under `.groundwork-journal` with writer-only crash recovery; derived sha256 version tokens). `gw_write.py` wraps its whole apply span in the exclusive lock — corpus scan, ID allocation, atomic tempfile-plus-replace writes, reciprocity, recheck, rollback on any failure, and targeted graph sync as a `GW_LOCK_BYPASS` child (DEC-0415). `groundwork_read.py`, `check_links.py` (import-optional for the standalone `tools/` copy), and the search/graph live-file scans all take the shared lock; reads emit per-section version tokens and read section gained `--occurrence` so repairs can fetch the right token. `append-turn` auto-numbers from the live transcript maximum with `--expect-first-turn` as precondition, reporting assigned numbers loudly in the OK line (DEC-0376 reconciliation). Tests: new `test_gw_lock.py` 18/18 (parallel-create race, lock semantics, timeouts, batch rollback, crash recovery, tokens, turn numbering); `test_gw_guards.py` 48/48 after updating to the token contract and repairing the rule-26 fixture breakage SES-0078 left; `test_audit_packet.py` 8/8. `operations.md` gained a Concurrency section and per-op token/turn-numbering documentation; the `artifact-interact` SKILL.md concurrency section now describes apply-moment serialization. This turn is being appended by one of two deliberately parallel write-task librarians as the DEC-0416 live acceptance run.

### T8 — Facilitator: recall-audit outcomes for DEC-0411 through DEC-0416

Recall-audit outcomes for DEC-0411 through DEC-0416 (three Sonnet 5 judges over the six search-audit packets): DEC-0411, DEC-0412, DEC-0413, DEC-0415, and DEC-0416 returned nothing-to-add; near-misses DEC-0031, DEC-0139, DEC-0284, DEC-0117, and DEC-0348 were each judged lexically adjacent but out of scope. One judge flagged DEC-0412's phrase that the next process to acquire the lock rolls back a leftover journal as ambiguous between the shared and exclusive lock; the build resolves it conservatively — crash recovery runs only under the exclusive write lock, readers merely warn — recorded here as the operative interpretation. DEC-0414 drew two findings: first, tension with DEC-0376's no-silent-mutation principle, dispositioned by making renumbering loud (the append OK line reports the assigned turn numbers) plus a relates-to link between the two decisions; second, a supersede-check against DEC-0392's one-in-flight-turn-appender rule, dispositioned as complementary rather than superseded — DEC-0392 remains operative as the ordering rule (order-dependent writes stay one batch or explicitly sequenced) while DEC-0414 removes the corruption risk from unordered parallel appends; relates-to link added. Both DEC-0414 dispositions await stakeholder ratification at session close. This turn is being appended by one of two deliberately parallel write-task librarians as the DEC-0416 live acceptance run.

### T9 (stakeholder awakeinagi)

Answering the facilitator's three ratification questions on the DEC-0414 dispositions and the EP-0009 enumeration: "Yes; Yes; No, I value the self-containedness"

### T10 (facilitator)

Ratifications recorded: (1a) the DEC-0376 tension resolves as loud-not-silent — turn renumbering is reported in every append's OK line, turn numbers are tool-owned bookkeeping like heading lines; (1b) DEC-0392 is narrowed, not superseded — the lock owns corruption prevention, DEC-0392 remains the ordering rule (order-dependent writes one batch or explicitly sequenced); (2) EP-0009 amended this session to enumerate DEC-0411..DEC-0416 per the stakeholder's self-containedness preference. Post-verification housekeeping completed: DEC-0394 expired by its own terms at verification; instruction surfaces updated to the parallel-write contract (project AGENTS.md, design-session skill and its AGENTS.md asset, artifact-librarian agent description [restart required per DEC-0347], artifact-interact SKILL.md and operations.md); librarian memory reconciled (dead file-left-on-disk claims annotated); facilitator memory updated. Design-review ceilings recorded for provenance (stakeholder-requested critique, kept-not-acted-on): required `--if-match` costs one extra read per edit — revisit only on observed librarian friction; `GW_LOCK_BYPASS` env reentrancy for the graph-sync child is the one clever construct to watch; `write recover` kept as the only side-effect-free crash-recovery path; the corpus-global lock showed zero waits under parallel load, so per-file locking stays correctly unbuilt.

### T11 — Facilitator: closing summary

Session complete — DEC-0391 machinery designed (T3-T6 gate), built, tested (18/18 new, 48/48 guards updated to the token contract plus repair of the rule-26 fixture breakage from SES-0078, 8/8 audit-packet), and verified live by two parallel write-task librarians (T7/T8 of this very transcript are the acceptance artifacts). Classification: method-track tooling build under EP-0009/BG-0002. Recall audits: five DECs nothing-to-add, DEC-0414's two findings dispositioned and ratified. Inspired-ideas check: one captured, IDEA-0054, below.

## Decisions Produced

DEC-0411 (lock primitive and chokepoint), DEC-0412 (transactional applies with journal rollback), DEC-0413 (per-section version tokens), DEC-0414 (turn appends auto-number under the lock), DEC-0415 (graph sync under the lock), and DEC-0416 (verification gate retiring DEC-0394) were produced and accepted at T6, when stakeholder awakeinagi approved the design and test plan presented at T3 with the T4/T5 lock-scoping amendment.

## Conflicts Raised

None yet.
