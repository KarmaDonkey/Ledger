# Förankring – flöde, kommittékalender och bokningar

## Kommittékalendern (Excel)
Organisationen har ett Excel-ark med alla kommittémöten. Förväntade kolumner (namnen kan variera – mappa mot det som finns och bekräfta med användaren):

| Kolumn | Innehåll |
|---|---|
| `Committee` | TC, GAC, GEC, RCC, Board |
| `Meeting date` | Mötesdatum |
| `Pre-read deadline` | Sista dag att skicka in pre-read |
| `Booked` | Yes/No – om användarens ärende är bokat på agendan |
| `Item` | Ärendets titel (om bokat) |
| `Owner` | Ansvarig för ärendet |
| `Status` | t.ex. Planned / Paper submitted / Presented / Approved / Returned |
| `Comment` | Fritext, t.ex. feedback eller villkor |

**Arbetssätt:**
- Be användaren ladda upp arket (eller använd det som redan finns i projektet). Läs det med kodverktyget – gissa aldrig datum.
- Finns inget ark: be om mötesdatumen för de aktuella kommittéerna och använd fallback-deadlines från `kommitteer.md`.
- Ändra aldrig i användarens original utan att fråga. Leverera i stället en **uppdaterad kopia** (samma kolumner) med föreslagna ändringar markerade, t.ex. `Booked = Proposed`, och sammanfatta ändringarna i chatten.

## 1. Bestäm vägen
Utgå från ärendets mandatbehov och `kommitteer.md` (typisk väg TC → GAC → GEC → RCC → Board). Bekräfta med användaren – många ärenden ska inte hela vägen.

## 2. Räkna baklänges från målmötet
1. Hitta målmötet i kalendern (sista instansen).
2. För varje föregående instans: välj **det senaste mötet** vars datum ligger minst **3 arbetsdagar före** nästa instans pre-read-deadline (tid att justera pappret efter feedback).
3. Chefsgenomgång (närmaste chef): minst 5 arbetsdagar före första instansens pre-read-deadline.
4. Första utkast klart: minst 3 arbetsdagar före chefsgenomgången.
5. Räkna i arbetsdagar; hoppa över helger och svenska helgdagar.

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
- Föreslå **förankringssamtal 1:1** med nyckelroller före varje möte (t.ex. CFO före GAC, CRO före RCC) – inga överraskningar i rummet.
- Finns kalender- eller mejl-connector: föreslå tider/utkast, men **skicka eller boka aldrig utan bekräftelse**.
- När användaren bekräftar att något är bokat: uppdatera kalenderkopian (`Booked = Yes`).

## 5. Logg efter varje instans
Efter varje möte, fråga:
- Utfall? (Approved / Approved with conditions / Returned / Noted)
- Vilka frågor kom? Vilka var svåra?
- Vad måste ändras inför nästa instans – och behöver nästa instans en annan nivå (t.ex. mindre tekniskt till RCC/Board)?

Spara i fliken `Logg`, uppdatera `Status`/`Comment` i kalenderkopian, och föreslå ändringar i pappret och i Q&A.
