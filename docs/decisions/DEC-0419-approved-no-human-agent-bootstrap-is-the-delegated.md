---
id: DEC-0419
type: decision
title: "Approved no-human agent bootstrap is the delegated write-then-SendMessage-ping method"
status: accepted
owner: awakeinagi
created: 2026-07-12
decided-by: awakeinagi (session SES-0083)
decided-on: 2026-07-12
source-span: "SES-0083 @ T3-T6"
overview: >-
  The approved no-human agent bootstrap is the delegated write-then-
  ping method: a teammate writes a new .claude/agents definition and
  reports readiness via SendMessage to the main session; that
  message is an incoming turn, which under DEC-0418's reload
  semantics refreshes the registry, making the new agent immediately
  spawnable with zero human action. The readiness signal must be a
  SendMessage — a plain subagent completion notification does not
  refresh the registry and is not a valid readiness signal. Editing
  an existing agent races the file watcher on the readiness-ping's
  own turn, so the protocol bakes an observable marker into the
  edited body, spawns, and on stale output performs one SendMessage
  ping-pong before respawning; one additional incoming turn
  deterministically cleared the race in testing. Fresh headless
  claude -p processes and --agents inline JSON definitions remain
  sanctioned alternatives when no session state is needed.
  Bootstrap/probe agents are minimally scoped, throwaway agents are
  deleted after use, and hooks stay confined to dedicated test
  agents. Verified end-to-end twice in SES-0083 (delegated create,
  delegated edit, ping-pong recovery), all with zero human action
  between file write and spawn.
links:
  derives-from: [SES-0083]
  relates-to: [DEC-0418, DEC-0348]
---

# DEC-0419: Approved no-human agent bootstrap is the delegated write-then-SendMessage-ping method

## Context

SES-0083 needed to ratify the approved way for a running session to create and start using a new agent definition without any human action, and to align that method with the incoming-turn-boundary reload semantics established in DEC-0418.

## Decision

When a running session needs to create and use a new agent definition without human intervention, the approved method is the delegated write-then-ping bootstrap: the session delegates to a teammate that writes the new definition file into .claude/agents and then reports readiness via SendMessage to the main session. The arrival of that message starts a new incoming turn, the agent registry refreshes under the semantics of DEC-0418, and the new agent is announced and immediately spawnable. The readiness signal must be a SendMessage; an ordinary subagent completion notification does not refresh the registry, so a plain "task finished" event is not a valid readiness signal. For edits to existing agents, a spawn on the readiness ping's own turn races the file watcher and may serve the stale definition, so the editing protocol bakes an observable marker into the new body, spawns the agent, and on stale output performs one SendMessage ping-pong with any teammate and respawns; the additional incoming turn deterministically refreshed the definition in both test rounds.

## Rationale

The delegated write-then-ping method is correct because a teammate's SendMessage is itself an incoming turn to the main session, which is the trigger DEC-0418 identified as reliably refreshing the registry; a plain task-completion notification is not such a trigger, which is why it is excluded as a valid readiness signal. The ping-pong recovery step for edits follows the same logic: one additional incoming turn is the deterministic way to clear the file-watcher race DEC-0418 documents.

## Alternatives Considered

Fresh headless claude -p processes and --agents inline JSON definitions remain sanctioned alternatives when no session state is needed, since both resolve definitions at their own startup rather than depending on a running session's registry refresh.

## Implications

Bootstrap and probe agents carry minimal toolsets and models sized to their task, throwaway agents are deleted immediately after use, and frontmatter hooks stay confined to dedicated test agents per existing practice. This method was verified end-to-end twice in SES-0083's originating conversation, including a delegated create, a delegated edit, and the ping-pong recovery, all with zero human action between file write and successful spawn.
