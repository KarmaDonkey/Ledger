# Memoassistent – proof of concept

En Claude-native **memocoach** som hjälper till att **planera, skriva, granska, förankra och förbereda** committee papers genom vägen TC → GAC → GEC → RCC → Board. Byggd som en **Claude Skill** som arbetar i **Claude Docs**.

> All data här (kommittémandat, kalender, testutkast) är **påhittad**.

## Innehåll
```
memo-assistent/
├── memo-assistent/            ← själva skillen
│   ├── SKILL.md               ← coach-hållning, fem lägen, Claude Docs-arbetssätt
│   └── references/
│       ├── coachning.md        grindar G0–G6, kontrollfrågor, coachande motstånd
│       ├── kommitteer.md       TC, GAC, GEC, RCC, Board: mandat, roller, gemensamt format
│       ├── publikprofiler.md   Expert / Ledning / Styrelse ("SvD Näringsliv-läsaren")
│       ├── skrivprinciper.md   mottagare, slutsats först, kundperspektiv, längd
│       ├── writing-rules-en.md brittisk engelska, plain English, svengelska-fällor
│       ├── skrivregler-sv.md   klarspråk, siffror, förkortningar
│       ├── mallar.md           memobrief + gemensam mall (exec summary + max 5 sidor + appendix)
│       ├── granskning.md       granskningsmetod och kommentarskategorier
│       ├── forankring.md       kommittékalender (Excel), baklängesplanering, bokningar, logg
│       └── qa-traning.md       Q&A per generisk roll, träningsläge med feedback
├── exempel/
│   ├── draft-irrbb-limit-framework.md   testutkast (engelska) med avsiktliga brister
│   └── committee-calendar.xlsx          fiktiv kommittékalender dec 2026 – dec 2027
└── memo-assistent.skill       ← zip att ladda upp i Claude
```

## Installera
1. Ladda ner `memo-assistent.skill` (en zip-fil).
2. claude.ai → inställningarna för **Skills** (Settings → Capabilities/Customize) → **Upload skill**.
3. Slå på **Claude Docs** (och gärna kalender/mejl-connector).

Alternativ: ett **Claude Project** med `SKILL.md` som instruktion och `references/` + kalendern som projektkunskap. Då slipper man ladda upp kalendern varje gång.

## Prova
| Läge | Exempel |
|---|---|
| Planera (coach) | "Jag ska skriva ett papper om nya IRRBB-limiter, det ska hela vägen till styrelsen." |
| Granska | Bifoga `draft-irrbb-limit-framework.md`: "Granska – det ska till GAC och sedan GEC." |
| Förankra | Bifoga `committee-calendar.xlsx`: "Målet är styrelsen 21 april. Går det ihop?" |
| Förbereda | "Ta fram Q&A inför RCC" → "Kör träningsläge, tuff nivå, som styrelsemöte." |

## Byta till riktiga data
Ersätt `references/kommitteer.md` och kalendern med era (samma rubriker/kolumner). Bygg om paketet med `zip -r memo-assistent.skill memo-assistent` i den här mappen.

## Nästa steg (idéer)
- Bilder ur färdigt papper (Slides-artifact eller .pptx).
- Statusöversikt över alla pågående papper, kopplad till kalendern.
- Minne per kommitté: vilka frågor som brukar komma, uppdateras från loggen.
