#!/usr/bin/env bash
# Install the groundwork-design-session skill from this repo (the canonical home, DEC-0318)
# into a target project's .claude/skills/ or the user scope (DEC-0319).
# Usage: install.sh --project <target-repo> | --global
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
case "${1:-}" in
  --project) DEST="${2:?usage: install.sh --project <target-repo>}/.claude/skills" ;;
  --global)  DEST="$HOME/.claude/skills" ;;
  *) sed -n '2,5p' "${BASH_SOURCE[0]}"; exit 2 ;;
esac
mkdir -p "$DEST"
rsync -a --delete --exclude __pycache__ "$HERE/" "$DEST/groundwork-design-session/"
echo "installed groundwork-design-session -> $DEST/groundwork-design-session"
