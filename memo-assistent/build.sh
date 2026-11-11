#!/usr/bin/env bash
# Builds the two claude.ai packages from the plugin sources:
#   memo-assistent.skill  – skill zip (skill + agent roles + scripts) for personal use
#   projekt/              – instructions + knowledge files for a shared Claude Project "Memo Studio"
set -euo pipefail
cd "$(dirname "$0")"

tmp=$(mktemp -d)
cp -r skills/memo-assistent "$tmp/memo-assistent"
rm -rf "$tmp/memo-assistent/scripts/__pycache__"
mkdir -p "$tmp/memo-assistent/agents" && cp agents/*.md "$tmp/memo-assistent/agents/"
rm -f memo-assistent.skill
(cd "$tmp" && zip -qr - memo-assistent) > memo-assistent.skill
rm -rf "$tmp"

rm -rf projekt && mkdir -p projekt/kunskap
{
  cat <<'PREFACE'
# Memo Studio – projektinstruktioner

Det här är ett delat Claude-projekt för teamets committee papers. Instruktionerna nedan kommer från skillen `memo-assistent`. I projektet gäller:
- Filer som nämns som `references/<namn>.md` finns i projektkunskapen som `<namn>.md`.
- Agentroller `agents/<namn>.md` finns som `agent-<namn>.md`. Subagenter finns inte i projektchatten: läs rollens fil och byt "hatt" själv.
- Skript `scripts/<namn>.py` finns som `<namn>.py`. Om kodkörning finns: använd dem för datumberäkningar (lägg dem i samma mapp som kalendern).
- Kommittékalendern: använd i första hand den som laddas upp i chatten (den är färskast). `committee-calendar.csv` i projektkunskapen kan vara inaktuell – säg det om du använder den.
- Flera i teamet använder projektet. Papperen bor i delade Claude Docs; läs fliken `Brief` först när du arbetar i ett befintligt papper.

---
PREFACE
  sed '1,/^---$/{/^---$/!d};1,/^---$/d' skills/memo-assistent/SKILL.md
} > projekt/instruktioner.md
cp skills/memo-assistent/references/*.md projekt/kunskap/
for f in agents/*.md; do cp "$f" "projekt/kunskap/agent-$(basename "$f")"; done
cp skills/memo-assistent/scripts/*.py projekt/kunskap/
cp exempel/committee-calendar.csv projekt/kunskap/
echo "Built memo-assistent.skill and projekt/ ($(ls projekt/kunskap | wc -l) knowledge files)"
