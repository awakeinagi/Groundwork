---
id: IDEA-0048
type: idea
title: "Pipe-safe CLI output for gw read commands"
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-12
proposed-by: awakeinagi@gmail.com
overview: >-
  The gw.py read commands emit a BrokenPipeError traceback when a
  downstream consumer closes the pipe early (for example, piping
  through head). Cosmetic but noisy, and the DEC-0388 direct-read
  charter has just created a much larger audience of agents invoking
  these commands directly. Handle SIGPIPE/BrokenPipeError
  gracefully.
links:
  derives-from: [SES-0076]
  relates-to: [DEC-0389]
---

# IDEA-0048: Pipe-safe CLI output for gw read commands

## The Idea

Handle SIGPIPE/BrokenPipeError gracefully in the gw.py read commands so a downstream consumer closing the pipe early (for example, piping through `head`) does not produce a traceback.

## Spark Context

The gw.py read commands emit a BrokenPipeError traceback when a downstream consumer closes the pipe early. Cosmetic but noisy, and DEC-0389's direct-read charter has just created a much larger audience of agents invoking these commands directly.

## Disposition

Pending — awaiting take-up. Relates to DEC-0389, the charter that expanded direct invocation of these commands.
