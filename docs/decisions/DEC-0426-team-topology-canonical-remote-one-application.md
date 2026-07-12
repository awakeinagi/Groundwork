---
id: DEC-0426
type: decision
title: "Team topology: canonical remote, one application instance per repository"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-12
source-span: "SES-0082 T13, T14, T19, T20, T31"
accepted-in: SES-0082
overview: >-
  In team use the git remote is the canonical consensus location;
  exactly one application instance serves a given repository,
  holding a local clone and participating as an ordinary git client
  (pull, write under the local lock, push, retry). Aligns with
  BG-0001's v1 single-process single-writer charter; multi-instance
  deployment stays deferred behind TRG-0001.
links:
  derives-from: [SES-0082]
  relates-to: [BG-0001, DEC-0391, DEC-0174]
---

# DEC-0426: Team topology: canonical remote, one application instance per repository

## Context

The stakeholder raised a topology question mid-session: when a team uses the application, is there one shared instance or does each user run their own? SES-0082 needed to settle the deployment topology before the collaboration protocol (branch-per-session, approval enforcement) could be specified concretely.

## Decision

In team use the git remote is the canonical consensus location. When a team uses the application for a repository, exactly one application instance serves that repository and all application users work through it; the instance holds a local clone and participates as an ordinary git client (pull, write under the local lock, push, retry on conflict).

## Rationale

A single instance per repository keeps the DEC-0391 lock model meaningful — one process, one exclusive-lock domain — without inventing a distributed-locking protocol across multiple instances. It also matches BG-0001's v1 charter directly: single-process, single-writer is the scale this decision is scoped to serve, and multi-instance deployment is deliberately deferred rather than solved speculatively.

## Alternatives Considered

A per-user application instance model (each user runs their own instance against the same remote) was considered and rejected for v1 — it would require either a distributed lock across instances or acceptance of push-conflict races as routine, neither of which the DEC-0391 model was designed for. Building multi-instance support now was rejected as premature; it's deferred behind TRG-0001 rather than designed ahead of an actual scale need.

## Implications

Team deployments must be told explicitly to run one application instance per repository. TRG-0001 remains the trigger that reopens multi-instance deployment as a live design question; until it fires, this single-instance topology is the only supported team-application configuration.
