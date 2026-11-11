# Förankring – flöde, kommittékalender och bokningar

## Kommittékalendern (Excel/CSV)
Organisationen har ett ark med alla kommittémöten. Förväntade kolumner (namnen kan variera – mappa mot det som finns och bekräfta med användaren):

| Kolumn | Innehåll |
|---|---|
| `Committee` | TC, GAAC, GEC, RCC, Board – eller namnet på en ad hoc-kommitté |
| `Meeting date` | Mötesdatum |
| `Pre-read deadline` | Sista dag att skicka in pre-read |
| `Type` | Ordinary / Moved / Extra / Ad hoc |
| `Booked` | Yes / No / Proposed – om ärendet är bokat på agendan |
| `Item` | Ärendets titel (om bokat) |
| `Owner` | Ansvarig för ärendet |
| `Status` | Planned / Paper submitted / Presented / Approved / Approved with conditions / Returned / Noted |
| `Comment` | Fritext, t.ex. feedback eller villkor |

**Arbetssätt:**
- **Räkna med skriptet när kodkörning finns**: `scripts/plan_path.py --target Board --date 2027-04-15 --calendar <fil> [--path TC,GAAC,GEC,RCC,Board] [--buffer 3]`. Det läser xlsx eller csv, tar med flyttade, extra och ad hoc-möten och skriver tidslinjen med flaggor. Utan kalender räknar det fram mötena från standardrytmen (`scripts/committee_rules.py`). Räkna aldrig datum i huvudet när skriptet går att köra.
- Be användaren ladda upp arket (eller använd det som redan finns i projektet). Läs det med kodverktyget – gissa aldrig datum.
- Finns inget ark: be om mötesdatumen för de aktuella kommittéerna och använd fallback-deadlines från `kommitteer.md`.
- Ändra aldrig i användarens original utan att fråga. Leverera i stället en **uppdaterad kopia** (samma kolumner) med föreslagna ändringar markerade, t.ex. `Booked = Proposed`, och sammanfatta ändringarna i chatten.

## 1. Bestäm vägen
Utgå från ärendets mandatbehov och `kommitteer.md` (typisk väg TC → GAAC → GEC → RCC → Board). Bekräfta med användaren – många ärenden ska inte hela vägen.

## 2. Räkna baklänges från målmötet
Ordningen är alltid TC → GAAC → GEC → RCC → Board (se `kommitteer.md` för rytm och deadlines). Använd kalendern; finns inte ett datum där, räkna fram det med reglerna i `kommitteer.md` och säg att det är beräknat.
1. Hitta målmötet (sista instansen) och dess pre-read-deadline.
2. För varje föregående instans: välj **det senaste mötet** som ligger minst **3 arbetsdagar före** nästa instans pre-read-deadline (tid att justera pappret efter feedback). Användaren kan ange en annan buffert.
3. Ta med **flyttade, extra och ad hoc-möten** från kalendern – ett extramöte kan rädda en tidplan som annars inte går ihop.
4. Chefsgenomgång: minst 5 arbetsdagar före första instansens pre-read-deadline.
5. Första utkast klart: minst 3 arbetsdagar före chefsgenomgången.
6. Arbetsdagar räknas utan helger och svenska helgdagar.

Exempel (beräknat på standardrytmen, buffert 3 arbetsdagar): för styrelsen 15 april 2027 måste RCC tas i mars, och första utkastet behöver vara klart i slutet av januari.

Utgå från dagens datum. Flagga:
- 🔴 deadline har passerat eller ligger inom 5 arbetsdagar
- 🟠 instans inte bokad (`Booked = No`) – föreslå att boka nu
- 🟢 bokad och nåbar

Om planen inte går ihop: säg det rakt ut och föreslå alternativ (nästa mötesomgång, extrainsatt möte, per capsulam, beredning parallellt i två instanser).

## 3. Presentera som tidslinje
```
| Datum      | Vad                          | Instans | Bokad | Flagga |
|------------|------------------------------|---------|-------|--------|
| 2027-01-11 | Utkast klart                 | –       | –     | 🟢     |
| 2027-01-14 | Genomgång med chef           | Chef    | –     | 🟢     |
| 2027-01-21 | Pre-read in                  | TC      | Nej   | 🟠     |
| 2027-02-02 | Möte                         | TC      | Nej   | 🟠     |
| …          |                              |         |       |        |
```
I Claude Docs: lägg tidslinjen i fliken `Förankringsplan`.

## 4. Bokningar
- För varje instans som inte är bokad: ta fram ett **utkast till mejl till kommittésekreteraren** (ärende, ansvarig, typ av ärende, önskat möte, uppskattad tid på agendan).
- Föreslå **förankringssamtal 1:1** med nyckelroller före varje möte (t.ex. CFO före GAAC, CRO före RCC) – inga överraskningar i rummet.
- Finns kalender- eller mejl-connector: föreslå tider/utkast, men **skicka eller boka aldrig utan bekräftelse**.
- När användaren bekräftar att något är bokat: uppdatera kalenderkopian (`Booked = Yes`).

## 5. Logg efter varje instans
Efter varje möte, fråga:
- Utfall? (Approved / Approved with conditions / Returned / Noted)
- Vilka frågor kom? Vilka var svåra?
- Vad måste ändras inför nästa instans – och behöver nästa instans en annan nivå (t.ex. mindre tekniskt till RCC/Board)?

Spara i fliken `Logg`, uppdatera `Status`/`Comment` i kalenderkopian, och föreslå ändringar i pappret och i Q&A.
