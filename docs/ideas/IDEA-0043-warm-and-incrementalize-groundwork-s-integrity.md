---
id: IDEA-0043
type: idea
title: "Warm and incrementalize Groundwork's integrity checker"
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-12
proposed-by: awakeinagi@gmail.com
overview: >-
  Groundwork's integrity checker re-parses the entire docs tree on
  every run, and the reactive hook explored in SP-0016 does the
  same. SP-0016's warm follow-up (DEC-0387) showed that holding the
  projection warm cuts per-edit checking eight to eleven times, and
  a graph-held incremental reaches twenty-two times, with the
  advantage compounding as the corpus grows. Proposes building a
  warm checker: start in-process per session, then add a graph-held
  incremental update that indexes relations by node and restores
  incoming cross-references, guarded by a standing warm-equals-cold
  findings test, so per-operation checking becomes affordable on
  every write rather than only at the pre-commit gate. To be scoped
  through a DEC-0337 survey and DEC-0335 design.
---

# IDEA-0043: Warm and incrementalize Groundwork's integrity checker

## The Idea

Groundwork's integrity checker re-parses the entire docs tree on every run, and the reactive hook explored in SP-0016 does the same. SP-0016's warm follow-up (recorded in DEC-0387) showed that holding the projection warm cuts per-edit checking eight to eleven times, and a graph-held incremental reaches twenty-two times, with the advantage compounding as the corpus grows. Build a warm checker: start in-process per session, then add a graph-held incremental update that indexes relations by node and restores incoming cross-references, guarded by a standing warm-equals-cold findings test. Consider running the integrity rules against the already-persistent graph index rather than a fresh cold parse, and consider a sidecar daemon for the multi-session case, so that per-operation checking becomes affordable on every librarian write rather than only at the pre-commit gate. To be scoped through a DEC-0337 survey and DEC-0335 design.

## Spark Context

Surfaced as a post-close follow-up to spike SP-0016 (SES-0073), which measured warm and persistent-projection checker latency after SES-0071 closed.

## Disposition

Captured; not yet taken up. To be scoped through a DEC-0337 option survey and DEC-0335 design intake before any build.
