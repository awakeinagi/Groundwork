---
id: IDEA-0036
type: idea
title: "Resolve SP-0014's eight unresolved schema tokens per DEC-0089"
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-11
proposed-by: awakeinagi@gmail.com
overview: >-
  Declare value/event elements (or inline schemas) for the eight
  A-item type tokens SP-0014's schema-resolution rule found
  dangling: UnitOfWork (CMP-0003 AppDatabasePort.A-1), QueueEntry
  (CMP-0004 ReaffirmationService.A-2), PrHandle and ReviewState
  (CMP-0005 CodeHostConnector.A-3), PermissionSet (CMP-0005
  CodeHostConnector.A-10, CMP-0009 GitHubConnector.A-10),
  WebhookHandle (CMP-0005 CodeHostConnector.A-11), DeliveryResult
  (CMP-0008 NotifierConnector.A-1), JobId (CMP-0012 QueuePort.A-1).
  Heuristic-parse caveat: verify each before treating as a gap.
links:
  derives-from: [SES-0069]
---

# IDEA-0036: Resolve SP-0014's eight unresolved schema tokens per DEC-0089

## The Idea

Declare value/event elements (or inline schemas) for the eight A-item type tokens SP-0014's schema-resolution rule found dangling: UnitOfWork (CMP-0003 AppDatabasePort.A-1), QueueEntry (CMP-0004 ReaffirmationService.A-2), PrHandle and ReviewState (CMP-0005 CodeHostConnector.A-3), PermissionSet (CMP-0005 CodeHostConnector.A-10, CMP-0009 GitHubConnector.A-10), WebhookHandle (CMP-0005 CodeHostConnector.A-11), DeliveryResult (CMP-0008 NotifierConnector.A-1), JobId (CMP-0012 QueuePort.A-1). Heuristic-parse caveat: verify each before treating as a gap.

## Spark Context

SP-0014 findings disposition, SES-0069 (rule R13).

## Disposition

Pending.

