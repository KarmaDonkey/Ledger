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
memo-assistent/                      ← plugin "memo-studio" (källan till allt)
├── .claude-plugin/plugin.json
├── skills/memo-assistent/
│   ├── SKILL.md                     coach-hållning, lägen, agentteam, Claude Docs
│   ├── references/                  coachning, kommittéer (rytm + deadlines), mall, granskning,
│   │                                förankring, Q&A, team, språkregler
│   └── scripts/                     committee_rules.py + plan_path.py (vägen och deadlines)
├── agents/                          9 specialistagenter
├── commands/                        /memo-new  /memo-review  /memo-plan  /memo-qa
├── exempel/                         kalender (xlsx + csv, fiktiv), make_calendar.py, testutkast
├── build.sh                         bygger memo-assistent.skill och projekt/
├── memo-assistent.skill             skill-paket för claude.ai
└── projekt/                         instruktioner + kunskapsfiler för ett delat Claude-projekt
```

## Kom igång i team: ett delat Claude-projekt (rekommenderas)
1. claude.ai → **Projects → New project**, döp det till **Memo Studio**.
2. Klistra in `projekt/instruktioner.md` som projektets instruktioner.
3. Ladda upp allt i `projekt/kunskap/` som projektkunskap.
4. **Dela projektet** med teamet (Team/Enterprise). Alla får då samma coach, mallar och kommittéregler.
5. Slå på **Claude Docs**. Varje papper blir ett delat doc med flikarna Paper, Brief, Q&A, Plan och Log. Kollegor kommenterar och kallar på Claude i trådarna (`review as Board`, `shorten`, `source?` …).
6. Ladda upp den aktuella kommittékalendern i chatten när du planerar. Kopian i projektet blir inaktuell.

Övriga vägar:
- **Personlig skill:** ladda upp `memo-assistent.skill` i Skills-inställningarna.
- **Claude Code / Cowork med riktiga subagenter:** `/plugin install memo-studio --marketplace KarmaDonkey/Ledger` (efter merge till huvudbranchen).

## Kommittérytmen
| Kommitté | Möte | Pre-read-deadline |
|---|---|---|
| TC | torsdagar | måndag samma vecka |
| GAC | tisdagar | torsdag veckan innan |
| GEC | måndagar | fredag veckan innan |
| RCC | onsdag vecka 3 varje månad | 9 dagar innan |
| Board | 3:e torsdagen varje månad | 9 dagar innan |

Kalendern går alltid före reglerna, eftersom möten kan flyttas och extra- eller ad hoc-möten tillkomma.
`python3 skills/memo-assistent/scripts/plan_path.py --target Board --date 2027-04-15 --calendar exempel/committee-calendar.xlsx`

## Prova
| Kommando | Exempel |
|---|---|
| `/memo-new` | `/memo-new nya IRRBB-limiter, hela vägen till styrelsen` |
| `/memo-review` | `/memo-review exempel/draft-irrbb-limit-framework.md GAC` |
| `/memo-plan` | `/memo-plan Board 15 April exempel/committee-calendar.xlsx` |
| `/memo-qa` | `/memo-qa RCC tough` |

## Byta till riktiga data
Byt ut mandaten i `references/kommitteer.md` och kalendern mot era egna. Kör `./build.sh` för att bygga om `memo-assistent.skill` och `projekt/`.
