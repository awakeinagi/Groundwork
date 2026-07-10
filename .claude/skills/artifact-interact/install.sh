#!/usr/bin/env bash
# Install the artifact-interact skill (and the artifact-librarian agent,
# DEC-0334) from this repo into a target project or the user scope
# (DEC-0319). The repo copy is canonical (DEC-0318); installed copies
# are conveniences installed FROM it, never edited in place.
#
# Usage:
#   install.sh --project <target-repo>   # -> <target>/.claude/skills + agents
#   install.sh --global                  # -> ~/.claude/skills + ~/.claude/agents
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$HERE/../../.." && pwd)"
AGENT="$REPO_ROOT/.claude/agents/artifact-librarian.md"

case "${1:-}" in
  --project)
    TARGET="${2:?usage: install.sh --project <target-repo>}"
    SKILLS="$TARGET/.claude/skills"; AGENTS="$TARGET/.claude/agents"
    ;;
  --global)
    SKILLS="$HOME/.claude/skills"; AGENTS="$HOME/.claude/agents"
    ;;
  *)
    sed -n '2,11p' "${BASH_SOURCE[0]}"; exit 2 ;;
esac

mkdir -p "$SKILLS" "$AGENTS"
rsync -a --delete --exclude '__pycache__' "$HERE/" "$SKILLS/artifact-interact/"
[ -f "$AGENT" ] && cp "$AGENT" "$AGENTS/"
# The librarian's memory skill ships with the deliverable (SES-0059);
# don't overwrite an existing copy — it holds accumulated memory.
MEMSKILL="$REPO_ROOT/.claude/skills/artifact-librarian-memory"
if [ -d "$MEMSKILL" ] && [ ! -d "$SKILLS/artifact-librarian-memory" ]; then
  rsync -a "$MEMSKILL/" "$SKILLS/artifact-librarian-memory/"
fi

# Bootstrap tool copies for Groundwork projects (DEC-0310)
if [ "${1}" = "--project" ] && [ -d "$TARGET/docs" ]; then
  mkdir -p "$TARGET/tools"
  for t in check_links.py serve_docs.py; do
    [ -f "$TARGET/tools/$t" ] || cp "$HERE/scripts/$t" "$TARGET/tools/$t"
  done
fi

echo "installed artifact-interact -> $SKILLS/artifact-interact"
[ -f "$AGENT" ] && echo "installed artifact-librarian -> $AGENTS/artifact-librarian.md"
