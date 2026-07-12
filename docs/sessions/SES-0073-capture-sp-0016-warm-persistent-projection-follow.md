---
id: SES-0073
type: session
title: "Capture SP-0016 warm/persistent-projection follow-up findings"
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-12
participant: awakeinagi
participant-role: stakeholder
facilitator: sp0016
transcript-fidelity: reconstructed
overview: >-
  Post-close follow-up to spike SP-0016: captured warm and
  persistent-projection measurements taken after SES-0071 closed,
  which had lived only in a gitignored one-off file and were not
  otherwise part of the corpus. Holding the checker's parse warm
  cuts per-edit projection from about 836 milliseconds cold to
  79-106 milliseconds (8-11x), and a graph-held incremental update
  reaches about 38 milliseconds (22x), with the advantage
  compounding from about 6x at the current corpus size to 12.4x at
  four times that size, where cold reaches an unusable 2.3 seconds
  per edit; memory footprint stays a few megabytes even at that
  scale. Three implementation constraints emerged: incremental
  removal must restore severed incoming cross-references; the graph
  does not serialize, so packaging must be in-process per session or
  a sidecar daemon; and relation removal must be indexed by node.
  This session recorded a new accepted decision, DEC-0387 (warm the
  checker projection before adopting the reactive substrate),
  relating to SP-0016, DEC-0374, DEC-0375, and DEC-0368, and
  captured idea IDEA-0043. The decision-recall audit on DEC-0387
  returned "Nothing to add." SP-0016 was amended with this follow-up
  in its Findings and stayed status approved throughout: an earlier
  attempt to move it to gated was an illegal transition and was
  refused, so it was correctly re-affirmed via the DEC-0267 stale-
  then-reapprove path (approved-by awakeinagi) rather than re-gated.
  No edits touched the closed SES-0071, DEC-0374, or DEC-0375.
  Session closed.
links:
  relates-to: [SP-0016, DEC-0374, DEC-0375, DEC-0368, DEC-0387]
---

# SES-0073: Capture SP-0016 warm/persistent-projection follow-up findings

## Purpose

Capture SP-0016's post-close warm/persistent-projection follow-up findings into the corpus as durable evidence: a new session plus one accepted follow-up decision relating to SP-0016, and an idea capturing the build follow-up, per stakeholder-approved mechanism. No edits are made to the closed SP-0016, SES-0071, DEC-0374, or DEC-0375.

## Transcript

T1 — Facilitator (sp0016): "Change intent: capture SP-0016's post-close warm/persistent-projection follow-up findings into the corpus as durable evidence. The findings were measured after SES-0071 closed and currently live only in gitignored one-off files; they materially inform the ActiveGraph adoption direction. The build was strictly throwaway per DEC-0351. The stakeholder approved the mechanism (a new session plus one accepted follow-up decision that relates to SP-0016, and an IDEA capturing the build follow-up); no edits are made to the closed SP-0016, SES-0071, DEC-0374, or DEC-0375."

T2 — Facilitator (sp0016): "Findings (companion detail in the gitignored SP-0016 warm-results file, which is not part of the corpus). The reactive hook and the production checker both re-parse the whole docs tree per run, which is cold and costs roughly 0.6 to 0.8 seconds, dominated by reading the 368 decision files. Holding the parse warm cuts per-edit projection to roughly 79 to 106 milliseconds, an eight to eleven times improvement, with byte-identical findings. A graph-held incremental update that surgically swaps only the edited artifact's nodes reaches about 38 milliseconds, a twenty-two times improvement. The advantage compounds with corpus size: about six times at the current 368 decisions, 8.6 times at twice the corpus, and 12.4 times at four times the corpus, where the cold path reaches an unusable 2.3 seconds per edit. The in-memory footprint is negligible, about 3.9 megabytes now and 6.1 megabytes at four times the corpus. Three implementation constraints emerged from the measurements: incremental removal severs incoming cross-references and silently diverges from cold unless they are restored, so a standing warm-equals-cold findings test is required; the ActiveGraph graph does not serialize (it holds a thread lock), so packaging must be in-process per session or a sidecar daemon rather than a pickled base graph; and relation removal must be indexed by node, because a full-edge-scan mutation is proportional to total edges and degrades from about 17 milliseconds at 1,147 edges to about 1.3 seconds at 76,000 edges."

T3 — Stakeholder (awakeinagi@gmail.com): "Approved the intent and the Option A mechanism. Record the follow-up decision as accepted."

T4 — Facilitator (sp0016): "This session produces decision DEC-0387 (warm the checker projection before adopting the reactive substrate) and captures idea IDEA-0043 (warm and incrementalize Groundwork's integrity checker)."

facilitator (sp0016): "Decision-recall audit on DEC-0387 via a fresh Sonnet 5 judge: Nothing to add. SP-0016 amended with a post-close Follow-up experiments and recommendations subsection (warm latency ladder, scale compounding, negligible memory, O(edges) mutation confirmation, the restore-incoming-edges and cold-equivalence-test correctness constraints, and the recommendation to warm the checker before adopting the reactive substrate); SP-0016 returned to gated pending stakeholder re-approval. SES-0073 frontmatter conformed to spec (transcript-fidelity reconstructed; single-participant model per DEC-0021)."

T6 — facilitator (sp0016): "Actual outcomes, for the record. The decision-recall audit on DEC-0387 by a fresh Sonnet 5 judge returned 'Nothing to add.' SP-0016's post-close warm/persistent-projection follow-up amendment landed in its Findings, with a single `## Findings` heading and a single `## Resulting Decisions` heading (no duplicates). The preceding unlabeled trailing paragraph above is T5; its assertions were superseded: it stated SP-0016 was returned to gated pending stakeholder re-approval, but that approved-to-gated transition was in fact illegal and was refused by the write API (a ratified spike does not re-enter the gate lifecycle that way). The correct path was DEC-0267's stale-and-reaffirm route: SP-0016 was set to stale and then re-approved (approved-by awakeinagi, the re-affirmation of the amended content), so SP-0016 remains status approved throughout, never gated. Separately, SES-0073's frontmatter (transcript-fidelity: reconstructed; participant: awakeinagi; participant-role: stakeholder; facilitator: sp0016) was conformed to spec by an operator-sanctioned facilitator direct edit, performed by the coordinating facilitator in the SES-0072 session's context, with operator sanction on record there, citing the IDEA-0042 API-unreachable-frontmatter gap (no typed write op reaches session identity frontmatter directly)."

## Decisions Produced

DEC-0387 (warm the checker projection before adopting the reactive substrate) was recorded and accepted in this session (T4), relating to SP-0016, DEC-0374, DEC-0375, and DEC-0368.

## Conflicts Raised

None.
