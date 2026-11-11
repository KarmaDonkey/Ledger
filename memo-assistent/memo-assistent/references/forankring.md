# Förankring – flöde och bokningar

## 1. Bestäm vägen
Utgå från ärendetyp och `kommitteer.md` → "Typiska vägar". Bekräfta med användaren.

## 2. Räkna baklänges från målmötet
För varje instans, från sista till första:
1. Mötesdatum (enligt mötesrytm / mötesplan).
2. Deadline för underlag = mötesdatum − instansens ledtid (arbetsdagar; hoppa över helger och svenska helgdagar).
3. Föregående instans måste ha **mötts före** denna deadline, med minst **3 arbetsdagar buffert** för att justera memot efter feedback.
4. Chefsgenomgång: minst 5 arbetsdagar före första kommitténs deadline.
5. Färdigt första utkast: minst 3 arbetsdagar före chefsgenomgången.

Om tidplanen inte går ihop: säg det tydligt och föreslå alternativ (senare målmöte, extra möte, per capsulam, parallell beredning).

Använd dagens datum som startpunkt och flagga om någon deadline redan har passerat eller ligger inom 5 arbetsdagar.

## 3. Presentera som tidslinje
```
| Datum      | Vad                         | Instans | Status   |
|------------|-----------------------------|---------|----------|
| 2027-01-08 | Utkast klart                | –       | Planerad |
| 2027-01-13 | Genomgång med chef          | CHEF    | Planerad |
| …          | Underlag in                 | RKK     |          |
| …          | Dragning                    | RKK     |          |
```
I Claude Docs: lägg tidslinjen i fliken `Förankringsplan`.

## 4. Bokningar
- För varje möte som användaren själv måste boka (chef, förmöten med nyckelpersoner, sekreterare för anmälan av ärende): ta fram ett mötesförslag – ämne, längd, deltagare, kort agenda.
- Finns kalender-connector: sök lediga tider, föreslå 2–3 alternativ, boka **först efter bekräftelse**.
- Påminn om att **anmäla ärendet till sekreteraren** i god tid (ofta 2–3 veckor före).
- Föreslå gärna **förankringssamtal** 1:1 med nyckelpersoner (t.ex. Compliance, CFO) före kommittémötet – inga överraskningar i rummet.

## 5. Logg efter varje instans
Efter varje möte, fråga användaren:
- Vad blev beslutet/utfallet?
- Vilka frågor kom upp? Vilka var svåra?
- Vad behöver ändras inför nästa instans?
Spara i fliken `Logg` och föreslå ändringar i memot och Q&A inför nästa instans.
