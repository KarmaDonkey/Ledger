#!/usr/bin/env bash
# Builds memo-assistent.skill for claude.ai chat: the skill plus the agent role descriptions.
set -euo pipefail
cd "$(dirname "$0")"
tmp=$(mktemp -d)
cp -r skills/memo-assistent "$tmp/memo-assistent"
mkdir -p "$tmp/memo-assistent/agents" && cp agents/*.md "$tmp/memo-assistent/agents/"
rm -f memo-assistent.skill
(cd "$tmp" && zip -qr - memo-assistent) > memo-assistent.skill
rm -rf "$tmp"
echo "Built memo-assistent.skill"
