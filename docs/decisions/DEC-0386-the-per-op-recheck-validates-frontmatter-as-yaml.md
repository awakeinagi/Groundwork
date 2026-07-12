---
id: DEC-0386
type: decision
title: "The per-op recheck validates frontmatter as YAML when PyYAML is available"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0072 @ T29-T31"
overview: >-
  The post-write recheck in gw_write.py runs yaml.safe_load on the
  touched file's frontmatter whenever PyYAML is importable; a parse
  failure or non-mapping result refuses the write, mirroring the
  full checker's validity bar exactly. Without PyYAML the check
  skips silently, preserving the write path's stdlib-only contract
  (DEC-0317), with the pre-commit checker as backstop. Closes the
  window where malformed frontmatter could sit undetected between a
  write and the next full check. yamllint was surveyed (DEC-0337)
  and set aside as a possible future style layer.
links:
  derives-from: [SES-0072]
---

# DEC-0386: The per-op recheck validates frontmatter as YAML when PyYAML is available

## Context

The write path edited frontmatter text-surgically and never parsed it as YAML; malformed frontmatter surfaced only at the pre-commit checker, leaving an undetected working-tree window — the historical unquoted-title defect lived exactly there.

## Decision

The recheck attempts yaml.safe_load on the touched file's frontmatter when PyYAML is importable, refusing on a parse failure or a non-mapping result; when PyYAML is absent the check skips silently.

## Rationale

Parity with the checker matters more than style enforcement — the failure mode that matters is "the checker will reject this frontmatter," so the recheck uses the checker's exact parser, and the try-import keeps DEC-0317's stdlib-only layering intact.

## Alternatives Considered

The yamllint package (the canonical Python YAML linter, with CLI and Python API) adds style-rule failure classes the corpus has never enforced — a separate adoption decision if ever wanted. The ruamel.yaml parser is stricter (YAML 1.2) and could reject frontmatter the checker accepts. Schema validators (yamale, StrictYAML-class) solve a different problem — frontmatter schema validation — and are out of scope.

## Implications

No hard PyYAML dependency enters the write path; environments without PyYAML keep today's behavior with the pre-commit gate as the sole YAML check.
