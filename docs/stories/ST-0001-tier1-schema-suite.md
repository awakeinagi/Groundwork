---
id: ST-0001
type: story
title: Tier-1 schema suite and validation library
status: gated
owner: eng-lead
created: 2026-07-06
links:
  derives-from: [EP-0001]
  satisfies: [BG-0001]
  impacts: [ST-0002, ST-0007]
cites: [DEC-0009, DEC-0018, DEC-0034, DEC-0037, DEC-0047, DEC-0080, DEC-0082,
        DEC-0097, DEC-0098, DEC-0104]
---

# ST-0001: Tier-1 Schema Suite and Validation Library

## Summary

Machine-readable JSON Schemas for every artifact type's frontmatter and
every governance config file, plus the validation library the storage
service runs on every write — the executable form of the SPEC documents.

## Acceptance Criteria

1. A JSON Schema exists for the frontmatter of every artifact type — BG,
   EP, ST, SP, CMP, SES, DEC, CFL, CON, CP — exactly matching its SPEC
   document (per [DEC-0034](../decisions/DEC-0034-two-tier-validation.md), [DEC-0009](../decisions/DEC-0009-typed-links-stable-ids.md), [DEC-0047](../decisions/DEC-0047-change-proposal-artifact.md)).
2. Schemas exist for `governance/roles.yaml` (including decision-rights),
   `domains.yaml`, `gate-policies.yaml`, `people.yaml`, and `repos.yaml`
   (per [DEC-0037](../decisions/DEC-0037-governance-as-code.md), [DEC-0054](../decisions/DEC-0054-guardrails-authority-limits.md), [DEC-0046](../decisions/DEC-0046-person-registry.md), [DEC-0049](../decisions/DEC-0049-repo-read-allowlist.md)).
3. The validation library rejects any write failing its schema with
   actionable, field-level errors; rejected writes never reach the repo
   (per [DEC-0034](../decisions/DEC-0034-two-tier-validation.md)).
4. Unknown link types and malformed IDs are tier-1 rejections; impact-link
   *reciprocity* is explicitly NOT tier-1 (it is a tier-2/PR check, since
   the reciprocal edit may arrive in the same branch later) (per [DEC-0009](../decisions/DEC-0009-typed-links-stable-ids.md),
   [DEC-0026](../decisions/DEC-0026-directional-impact-links.md), [DEC-0034](../decisions/DEC-0034-two-tier-validation.md)).
5. Schemas are published as language-neutral assets alongside the SPECs so
   any reimplementation validates identically (per [DEC-0018](../decisions/DEC-0018-python-backend-language-agnostic-specs.md)).
6. The element-type enum (entity, value, service, event, protocol) is
   published as a language-neutral schema asset, and the CMP frontmatter
   schema validates the optional `component-type` field (standalone
   element CMPs) against it; unknown types are tier-1 rejections (per
   [DEC-0080](../decisions/DEC-0080-hybrid-component-granularity.md), [DEC-0082](../decisions/DEC-0082-closed-element-type-taxonomy.md), [DEC-0018](../decisions/DEC-0018-python-backend-language-agnostic-specs.md)).
7. Story, epic, and spike frontmatter schemas accept the `deferred`
   status and validate the `release:` field grammar — `backlog` or a
   SemVer version-core prefix (`MAJOR`, `MAJOR.MINOR`, or
   `MAJOR.MINOR.PATCH`; numeric identifiers, no leading zeroes, no `v`
   prefix, no pre-release/build metadata); malformed values, and the
   field or status on any other artifact type, are tier-1 rejections.
   Cross-file validity — the label matching a release declared in the
   governing Business Goal — is explicitly NOT tier-1 (tier-2/PR check)
   (per [DEC-0097](../decisions/DEC-0097-deferred-status.md), [DEC-0098](../decisions/DEC-0098-semver-release-labels.md), [DEC-0104](../decisions/DEC-0104-deferred-extends-to-spikes.md), [DEC-0034](../decisions/DEC-0034-two-tier-validation.md)).

## Component Impact

[CMP-0001](../components/CMP-0001-artifact-store-service.md) — supplies
its tier-1 validation behavior and the schema assets in its Data Contract.

## Out of Scope

Tier-2 completeness rules ([ST-0007](ST-0007-tier2-check-suite.md)); schema *evolution*/migration
machinery (future story once a spec change first occurs post-launch).

## Notes for Implementers

The SPECs in `docs/specs/` are normative; where a SPEC is ambiguous,
resolve the SPEC first (PR-gated edit), then encode. This repo's 96
bootstrap artifacts are the initial conformance corpus.
