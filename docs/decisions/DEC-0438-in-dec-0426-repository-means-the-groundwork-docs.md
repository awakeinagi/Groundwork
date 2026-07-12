---
id: DEC-0438
type: decision
title: "In DEC-0426, repository means the Groundwork docs repository"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0082 @ T35-T38"
overview: >-
  DEC-0426's one-application-instance-per-repository rule binds to
  the Groundwork docs repository (the corpus repo), not to code
  repositories. An umbrella project may comprise many applications
  and libraries in their own code-only repositories, all governed by
  a single Groundwork docs repo that the one application instance
  serves. The wider multi-repo linkage, checker/gate reach into code
  repositories, and instance scope across an umbrella project is
  captured as IDEA-0056 for a future session. Confirmed by the
  stakeholder at SES-0082 T37.
links:
  derives-from: [SES-0082]
  relates-to: [DEC-0426, IDEA-0056]
---

# DEC-0438: In DEC-0426, repository means the Groundwork docs repository

## Context

DEC-0426 fixed team topology as one application instance per repository, but the stakeholder raised a scenario where an umbrella project spans many code repositories alongside a single documentation corpus, and asked for the term "repository" to be pinned precisely rather than left ambiguous.

## Decision

The one-application-instance-per-repository rule of DEC-0426 binds to the Groundwork docs repository — the corpus repo — not to code repositories.

## Rationale

An umbrella project may comprise many applications and libraries in their own code-only repositories, all governed by a single Groundwork docs repo; that corpus is what the single application instance serves, and the code repositories link back to it. This reading is consistent with DEC-0426's own context: the application instance holds a clone of the corpus and participates as a git client against the corpus's canonical remote, not against arbitrary code repositories.

## Alternatives Considered

Reading "repository" as any repository touched by the project (code or docs) was rejected: it would require one application instance per code repository in a multi-repo umbrella project, contradicting the single-corpus, single-instance topology DEC-0426 was written to establish.

## Implications

The wider multi-repo territory — the code-to-corpus linkage mechanism, the reach of checker and gate enforcement into code repositories, and the application instance's scope across an umbrella project — is captured as IDEA-0056 for a future session.
