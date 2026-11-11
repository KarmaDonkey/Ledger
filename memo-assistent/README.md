# Memoassistent – proof of concept

En Claude-native memoassistent som hjälper till att **planera, skriva, granska, förankra och förbereda** memon till chef, kommittéer och styrelse. Byggd som en **Claude Skill** som arbetar i **Claude Docs**.

> All data här (Exempelbolaget AB, kommittéer, personer, testutkast) är **påhittad**.

## Innehåll
```
memo-assistent/
├── memo-assistent/            ← själva skillen
│   ├── SKILL.md               ← instruktioner: fem lägen + Claude Docs-arbetssätt
│   └── references/
│       ├── skrivprinciper.md   mottagare, slutsats först, kundperspektiv, längd
│       ├── publikprofiler.md   Expert / Ledning / Styrelse ("SvD Näringsliv-läsaren") / Chef
│       ├── kommitteer.md       fiktivt register: ToR, ledamöter, mötesrytm, deadlines, längdkrav
│       ├── skrivregler-sv.md   klarspråk, siffror, förkortningar
│       ├── writing-rules-en.md brittisk engelska, plain English, svengelska-fällor
│       ├── mallar.md           memobrief, beslutsmemo sv/en, informationsmemo, styrelse-PM
│       ├── granskning.md       granskningsmetod och kommentarskategorier
│       ├── forankring.md       baklängesplanering, bokningar, logg
│       └── qa-traning.md       Q&A per ledamot, träningsläge med feedback
├── exempel/
│   └── utkast-digital-skadeanmalan.md   testutkast med avsiktliga brister
└── memo-assistent.skill       ← zip att ladda upp i Claude
```

## Installera
1. Ladda ner `memo-assistent.skill` (en zip-fil).
2. claude.ai → **Settings → Capabilities → Skills** → **Upload skill** → välj filen.
3. Se till att **Claude Docs** är påslaget (och gärna en kalender-connector).

Alternativ: skapa ett **Claude Project** och lägg `SKILL.md` som projektinstruktion och filerna i `references/` som projektkunskap.

## Prova
| Läge | Exempelprompt |
|---|---|
| Planera | "Jag behöver skriva ett memo om att byta skadesystem. Det ska till LG och sen styrelsen." |
| Skriva | "Skriv ett utkast utifrån briefen och den bifogade PDF:en." |
| Granska | Bifoga `exempel/utkast-digital-skadeanmalan.md`: "Granska det här, det ska till styrelsen." |
| Förankra | "Målet är styrelsemötet 21 april. Vilken väg och när måste allt vara klart?" |
| Förbereda | "Ta fram Q&A inför LG" → "Kör träningsläge, tuff nivå." |

## Byta till riktiga data
Ersätt `references/kommitteer.md` med ert riktiga register (samma rubriker), och lägg ev. företagets språkpolicy i `skrivregler-*.md`. Kör `zip -r memo-assistent.skill memo-assistent` i den här mappen för att bygga om paketet.

## Nästa steg (idéer)
- Bildspel ur färdigt memo (Slides-artifact eller .pptx).
- Statusöversikt över alla pågående memon och var de ligger i flödet.
- Minne per kommitté: vilka frågor som brukar komma, uppdateras från loggen.
