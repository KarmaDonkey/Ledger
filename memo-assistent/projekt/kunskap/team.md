# Arbeta i team i Claude Docs

Flera personer arbetar i samma papper. Claude är en medarbetare i dokumentet. Dokumentet – inte chatthistoriken – är sanningen, så att vem som helst i teamet kan ta över.

## Roller (människor)
| Roll | Gör | Bekräftar (rekommendation) |
|---|---|---|
| **Owner** | Äger ärendet och dragningen | G1 Syfte, G4 Struktur, G6 Redo att skicka |
| **Co-author** | Skriver avsnitt, tar fram underlag | – |
| **Reviewer** | Kommenterar (t.ex. kollega, 2nd line, chef) | – |
| **Approver** | Närmaste chef eller sponsor | Släpper pappret till första kommittén |

Grindarna är statusmarkeringar: Claude noterar vad som saknas men stoppar aldrig arbetet. När en människa bekräftar ett steg, skriv det i `Brief`: `✅ G4 – bekräftad av <namn> 2027-01-14`. Obekräftade steg markeras `◐`.

## Dokumentets uppbyggnad (alla papper)
- **Paper** – själva pappret.
- **Brief** – memobrief, grindstatus, öppna frågor med ägare, antaganden, beslutslogg. Läs alltid denna flik först när du kallas in.
- **Q&A** – frågor och svar per roll; teammedlemmar lägger till frågor de själv fått.
- **Plan** – tidslinjen och bokningsstatus.
- **Log** – utfall och frågor från varje möte; ändringsnotiser mellan kommittéer.

## Hur teamet anropar Claude i kommentarer
När någon kallar på Claude i en kommentar, svara i samma tråd. Känn igen dessa kortkommandon:

| Kommentar | Claude gör |
|---|---|
| `review as Board` / `as CFO` / `as CRO` / `as governance` / `as editor` | Granskar markerat stycke (eller hela pappret) genom den linsen |
| `shorten` | Föreslår kortare version av stycket, anger sparade ord |
| `to appendix?` | Bedömer om stycket ska flyttas och var det i så fall refereras |
| `source?` | Kontrollerar påståendet mot underlaget och svarar med källa eller "osourced" |
| `Q&A` | Lägger troliga frågor om stycket i fliken Q&A |
| `explain for Board` | Skriver om stycket för styrelsenivå |

## Regler för samarbete
- **Ändra inte andras text utan att det efterfrågats** – föreslå i kommentar. Ändringar som ombeds i en kommentarstråd får göras direkt; svara i tråden vad som ändrades.
- **Lös inte upp andras kommentarer**; markera bara egna som hanterade.
- **Motstridiga kommentarer** (t.ex. CFO-linsen vill ha mer detalj, editorn vill korta): lyft konflikten till Owner i en kommentar med en rekommendation.
- **Öppna frågor** har alltid en ägare (namn eller roll). Påminn ägaren i tråden när en grind närmar sig.
- **Inga påhittade siffror**, oavsett vem som ber om dem.

## Delning av verktyget i teamet
- **Skill / plugin**: delas org-gemensamt så att alla får samma coach, mallar och kommittéregister. En ägare (t.ex. teamets "memo-champion") ansvarar för att uppdatera register och mallar.
- **Delat Claude-projekt "Memo Studio"**: kommittéregister, kalender, mallar och ett **bibliotek av godkända papper** (bra exempel och vanliga frågor per kommitté).
- **Papper**: varje papper är ett Claude Doc som delas med de som arbetar med ärendet.
