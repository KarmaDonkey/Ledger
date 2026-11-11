# Memo Studio – proof of concept

En Claude-native **memocoach med ett agentteam** som hjälper ett team att **planera, skriva, granska, förankra och förbereda** committee papers genom vägen TC → GAC → GEC → RCC → Board, och att samarbeta kring papperen i **Claude Docs**.

> All data här (kommittémandat, kalender, testutkast) är **påhittad**.

## Agentteamet
```
                         ┌──────────────────────────────┐
     Människan  ◀──────▶ │  MEMO LEAD (coach, master)   │  äger brief + grindar G0–G6
     (Owner/team)        │  coachning · träningsläge    │  konsoliderar · kvalitetskontroll
                         └──────────────┬───────────────┘
        ┌──────────────┬────────────────┼─────────────────┬──────────────────┐
        ▼              ▼                ▼                 ▼                  ▼
 evidence-analyst  memo-author   GRANSKNINGSPANEL     devils-advocate   committee-secretary
 fakta + källor    skriver       (parallellt)         invändningar,     kalender, tidslinje,
 faktakontroll     utkast        · board-lens         Q&A per roll      bokningsmejl
                                 · finance-risk-lens
                                 · governance                           audience-adapter
                                 · plain-language-editor                ny nivå per instans
                                                                        + ändringsnotis
```
- **Memo Lead** är huvudkonversationen: den intervjuar, delegerar, slår ihop granskningar, löser konflikter och ser till att bara människor godkänner grindar.
- I **Claude Code / Cowork** körs specialisterna som riktiga subagenter, med granskningspanelen parallellt. I **vanlig chatt** byter Memo Lead ”hatt” och tar rollerna i tur och ordning.

## Innehåll
```
memo-assistent/                      ← plugin "memo-studio"
├── .claude-plugin/plugin.json
├── skills/memo-assistent/           ← coach-skillen
│   ├── SKILL.md
│   └── references/                  coachning, kommittéer, mallar, granskning, förankring, Q&A, team, språkregler
├── agents/                          ← 9 specialistagenter
├── commands/                        ← /memo-new  /memo-review  /memo-plan  /memo-qa
├── exempel/                         ← committee-calendar.xlsx, draft-irrbb-limit-framework.md
├── build.sh                         ← bygger memo-assistent.skill för claude.ai-chatten
└── memo-assistent.skill
../.claude-plugin/marketplace.json   ← gör repot till en plugin-marknadsplats för teamet
```

## Installera
**Claude Code / Cowork (pluginet med agenter och kommandon):**
```
/plugin install memo-studio --marketplace KarmaDonkey/Ledger
```

**claude.ai-chatten (bara skillen):** ladda upp `memo-assistent.skill` under inställningarna för Skills. Slå på Claude Docs.

## Dela med teamet
1. **Samma verktyg för alla:** teamet installerar pluginet från marknadsplatsen, eller så lägger en admin ut skillen för hela organisationen.
2. **Delat projekt ”Memo Studio”:** kommittéregister, kalender och ett bibliotek med godkända papper som kunskap.
3. **Ett papper = ett delat Claude Doc** med flikarna Paper, Brief, Q&A, Plan och Log. Kollegor kommenterar och kan kalla på Claude i tråden med kortkommandon som `review as Board`, `shorten`, `source?` och `to appendix?`. Se `skills/memo-assistent/references/team.md`.

## Prova
| Kommando | Exempel |
|---|---|
| `/memo-new` | `/memo-new nya IRRBB-limiter, hela vägen till styrelsen` |
| `/memo-review` | `/memo-review exempel/draft-irrbb-limit-framework.md GAC` |
| `/memo-plan` | `/memo-plan Board 21 April exempel/committee-calendar.xlsx` |
| `/memo-qa` | `/memo-qa RCC tough` |

## Byta till riktiga data
Byt ut `references/kommitteer.md` och kalendern mot era egna. Kör `./build.sh` för att bygga om chattpaketet.
