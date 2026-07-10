# Grilling: the interview technique

> Adapted from Matt Pocock's [`grilling` skill](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md).
> Thanks, Matt — the original description of this technique is solid enough
> that Groundwork's entire refinement process is best understood as an
> elaboration of it, not a replacement.

## The core technique

Interview the stakeholder relentlessly about every aspect of the artifact
being refined until you reach shared understanding. Walk down each branch
of the design tree, resolving dependencies between decisions one by one.
For each question, provide your recommended answer.

Ask questions one at a time, or in small rounds (see
[refinement-process.md](refinement-process.md) for Groundwork's specific
round size and format), waiting for feedback before continuing. Asking too
many things at once is bewildering.

If a *fact* can be found by exploring the codebase or the existing artifact
tree, look it up rather than asking. The *decisions*, though, belong to the
stakeholder — put each one to them and wait for their answer.

Do not treat the artifact as refined, and do not derive downstream work
from it, until the stakeholder confirms shared understanding has been
reached.

## How Groundwork applies it

[refinement-process.md](refinement-process.md) is the full elaboration of
this technique for design-doc grilling specifically: dependency ordering,
round size, recommendation etiquette, the three affordances (annotate,
free-text, elaborate), and stage-specific stop criteria. This file exists
to name the underlying technique on its own terms and keep its origin
visible.

**Grilling has no round limit.** A session runs as many rounds as it takes
for the artifact under refinement to be clearly, unambiguously specified —
contract-complete for component docs, decision-complete for goals, epics,
stories, and spikes. Stopping early because a session "feels long enough"
is a failure mode, not efficiency: it's always better to ask one more
question than to leave a gap that later surfaces as a stale artifact, a
conflict, or a decision-recall audit finding. Session length has no
relationship to session quality — only coverage of the open questions does.
