---
name: mietwucher-mietpreisueberhoehung
description: "Mietpreisüberhöhung und Mietwucher – Ordnungswidrigkeit § 5 WiStG (Überschreitung der üblichen Entgelte um mehr als 20 % infolge Ausnutzung eines geringen Angebots, Bußgeld bis 50.000 EUR), Straftat Wucher § 291 Abs. 1 Nr. 1 StGB (auffälliges Missverhältnis, Ausbeutung einer Zwangslage), Teilnichtigkeit der Mietabrede § 134 BGB und Rückforderung § 812 BGB bis zur Wesentlichkeitsgrenze (BGHZ 89, 316), Darlegungslast des Mieters für das Ausnutzen, Abgrenzung zur Mietpreisbremse §§ 556d ff. BGB, anhängige Reform BT-Drs. 21/1397. Rechtsstand: Oktober 2026. Use when eine Miete außerhalb oder neben der Mietpreisbremse als überhöht angegriffen, eine Anzeige bei der Bußgeldbehörde erwogen oder ein Vermieter gegen den Vorwurf der Mietpreisüberhöhung verteidigt wird."
language: de
provider_variants: [claude, gemini, openai]
test: ./test.md
---

# /mietrecht:mietwucher-mietpreisueberhoehung

## Zweck

Die Mietpreisbremse greift nur bei Vertragsschluss, nur in Gebieten mit Landesverordnung und nur nach einer Rüge. § 5 WiStG greift dagegen bundesweit, während der gesamten Mietzeit und ohne Rüge. Dafür liegt die Hürde höher: Der Mieter muss darlegen, dass der Vermieter ein **geringes Angebot ausgenutzt** hat. § 291 StGB erfasst die schweren Fälle. Diese Skill prüft beide Tatbestände, beziffert den Rückforderungsanspruch und grenzt ihn von der Mietpreisbremse ab. Sie markiert die anhängige Reform, die das Ausnutzungsmerkmal streichen will.

**Rechtsstand: Oktober 2026.**

- **Geltend:** § 5 WiStG mit dem Merkmal „infolge der Ausnutzung eines geringen Angebots", Bußgeld bis 50.000 EUR; § 291 StGB.
- **Anhängig, nicht geltend:** Gesetzentwurf des Bundesrates BT-Drs. 21/1397 v. 27.08.2025 (Streichung des Ausnutzungsmerkmals, Bußgeld bis 100.000 EUR). Die Expertenkommission zum Mietrecht soll bis 31.12.2026 berichten. Der Regierungsentwurf BT-Drs. 21/6807 enthält **keine** Mietwucherregelung.

## Eingaben

- Vereinbarte Nettokaltmiete, Datum des Vertragsschlusses, spätere Erhöhungen
- **Übliche Entgelte:** Mietspiegelwert (Feld, Spanne), Gutachten, Vergleichsmieten der letzten sechs Jahre
- **Wohnungsmarktlage:** Leerstandsquote, Zweckentfremdungs- oder Mietpreisbremsenverordnung, Statistiken der Gemeinde
- **Suchverhalten des Mieters:** Dauer der Suche, Zahl der Bewerbungen, Absagen, Gründe für die Anmietung
- Persönliche Lage bei Vertragsschluss (Zwangslage, Unerfahrenheit, Sprachkenntnis) — für § 291 StGB
- Laufende Aufwendungen des Vermieters (für die Kostendeckungseinrede des § 5 Abs. 2 S. 2 WiStG)

## Sub-Agent-Architektur

Die Prüfung wird in Prosa von spezialisierten Schritten getragen; einen `agents`-Block trägt diese Skill bewusst nicht (mietrecht-Konvention).

- Ein **Vergleichs-Rechner** ermittelt die üblichen Entgelte und die Überschreitung in Prozent.
- Ein **Markt-Prüfer** beurteilt das geringe Angebot im Teilmarkt.
- Ein **Ausnutzungs-Prüfer** baut die Darlegung des Mieters zum Kausalzusammenhang auf. Dieser Teil ist der Engpass jedes Verfahrens.
- Ein **Straf-Prüfer** prüft § 291 StGB gesondert.
- Ein **Anspruchs-Prüfer** beziffert die Rückforderung und die Verjährung und grenzt zur Mietpreisbremse ab.

## Ablauf

### 1. Tatbestand § 5 WiStG — unangemessen hohes Entgelt

Ordnungswidrig handelt, wer vorsätzlich oder leichtfertig für die Vermietung von Räumen zum Wohnen **unangemessen hohe Entgelte** fordert, sich versprechen lässt oder annimmt (§ 5 Abs. 1 WiStG). Unangemessen hoch sind Entgelte, die infolge der **Ausnutzung eines geringen Angebots** an vergleichbaren Räumen die **üblichen Entgelte um mehr als 20 %** übersteigen (§ 5 Abs. 2 S. 1 WiStG). Üblich sind die Entgelte, die in der Gemeinde oder vergleichbaren Gemeinden für vergleichbaren Wohnraum in den letzten sechs Jahren vereinbart oder geändert worden sind, also ein Maßstab, der der ortsüblichen Vergleichsmiete entspricht.

**Kostendeckungseinrede:** Nicht unangemessen hoch sind Entgelte, die zur Deckung der laufenden Aufwendungen des Vermieters erforderlich sind und nicht in einem auffälligen Missverhältnis zu seiner Leistung stehen (§ 5 Abs. 2 S. 2 WiStG).

**Rechtsfolge:** Geldbuße bis **50.000 EUR** (§ 5 Abs. 3 WiStG), Abführung des Mehrerlöses nach §§ 8 ff. WiStG. Zuständig sind die Bußgeldbehörden der Gemeinden; einzelne Städte (z. B. Frankfurt am Main) verfolgen Mietpreisüberhöhungen aktiv.

### 2. Das Ausnutzungsmerkmal — Darlegungslast des Mieters

Der Mieter muss im Einzelfall darlegen und beweisen, dass der Vermieter ein geringes Angebot ausgenutzt hat. Ein **Anscheinsbeweis** besteht **nicht**, auch nicht, wenn in der Gemeinde eine Zweckentfremdungsverbotsverordnung gilt (BGH, Urt. v. 28.01.2004 – VIII ZR 190/03, NJW 2004, 1740, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2004-01-28&Aktenzeichen=VIII%20ZR%20190/03).

Darzulegen sind:

- das **geringe Angebot** im maßgeblichen Teilmarkt (Größe, Lage, Preissegment), nicht nur in der Gesamtstadt;
- die **eigenen Bemühungen** des Mieters, eine günstigere Wohnung zu finden: Dauer, Anzahl, Absagen;
- der **Kausalzusammenhang**: Der Mieter hat sich auf die hohe Miete nur eingelassen, weil er auf die Wohnung angewiesen war.

> In der Praxis scheitern die meisten Verfahren an diesem Punkt. Dokumentation der Wohnungssuche (Screenshots, Absagen, Besichtigungsliste) ist das wichtigste Beweismittel.

### 3. Zivilrechtliche Folge: Teilnichtigkeit und Rückforderung

§ 5 WiStG ist ein **Verbotsgesetz** i.S.d. [§ 134 BGB](https://www.gesetze-im-internet.de/bgb/__134.html). Die Mietabrede ist nur insoweit nichtig, als sie die zulässige Miete übersteigt. Der Mietvertrag im Übrigen bleibt wirksam, und an die Stelle der unzulässigen Vereinbarung tritt der gesetzlich zulässige Preis (BGH, Beschl. v. 11.01.1984 – VIII ARZ 13/83, BGHZ 89, 316 = NJW 1984, 722, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=1984-01-11&Aktenzeichen=VIII%20ARZ%2013/83). Geschuldet bleibt die Miete bis zur **Wesentlichkeitsgrenze** von 120 % der üblichen Entgelte. Der Überschuss ist nach [§ 812 BGB](https://www.gesetze-im-internet.de/bgb/__812.html) zurückzufordern.

**Verjährung:** drei Jahre ab Schluss des Jahres der Entstehung und Kenntnis ([§§ 195, 199 BGB](https://www.gesetze-im-internet.de/bgb/__199.html)). Die Rückforderung ist für jeden Monat gesondert zu berechnen.

### 4. Wucher ([§ 291 Abs. 1 S. 1 Nr. 1 StGB](https://www.gesetze-im-internet.de/stgb/__291.html))

Strafbar ist, wer die **Zwangslage**, die Unerfahrenheit, den Mangel an Urteilsvermögen oder die erhebliche Willensschwäche eines anderen dadurch ausbeutet, dass er sich für die Vermietung von Räumen zum Wohnen Vermögensvorteile versprechen oder gewähren lässt, die in einem **auffälligen Missverhältnis** zur Leistung stehen. In der Praxis wird ein auffälliges Missverhältnis ab etwa 50 % über der ortsüblichen Miete angenommen `[unverifiziert – prüfen]`. Strafrahmen: Freiheitsstrafe bis zu drei Jahren oder Geldstrafe; in besonders schweren Fällen bis zu zehn Jahren (§ 291 Abs. 2 StGB). Zivilrechtlich kommt neben § 134 BGB auch [§ 138 Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__138.html) in Betracht. Typische Fallgruppen sind Vermietungen an Geflüchtete, Saisonarbeitskräfte und Personen ohne Sprachkenntnisse, oft in überbelegten Unterkünften.

### 5. Abgrenzung zur Mietpreisbremse ([§§ 556d ff. BGB](https://www.gesetze-im-internet.de/bgb/__556d.html))

| | Mietpreisbremse | § 5 WiStG |
|---|---|---|
| Gebiet | nur mit Landesverordnung (bis 31.12.2029) | bundesweit |
| Grenze | Vergleichsmiete + 10 % | übliche Entgelte + 20 % |
| Ausnutzen | nicht erforderlich | **erforderlich** |
| Zeitpunkt | Mietbeginn (Wiedervermietung) | gesamte Mietzeit |
| Rüge | erforderlich (§ 556g Abs. 2 BGB) | nicht erforderlich |
| Sanktion | zivilrechtlich | Bußgeld + zivilrechtlich |
| Neubau / umfassende Modernisierung | ausgenommen (§ 556f BGB) | nicht ausgenommen |

In Gebieten mit Mietpreisbremse ist diese regelmäßig der leichtere Weg. § 5 WiStG bleibt wichtig für Neubauten, Orte ohne Verordnung, Mieten oberhalb der Vormiete und als **Bußgeldhebel**. Vertiefung: `/mietrecht:mietpreisbremse`.

### 6. Anhängige Reform (BT-Drs. 21/1397)

Der Gesetzentwurf des Bundesrates ([BT-Drs. 21/1397](https://dserver.bundestag.de/btd/21/013/2101397.pdf)) will:

- das Merkmal „infolge der Ausnutzung" durch das bloße Vorliegen eines **geringen Angebots** ersetzen,
- den Bußgeldrahmen auf **100.000 EUR** anheben.

**Stand 23.10.2026:** nicht verabschiedet; der Bericht der Expertenkommission ist bis 31.12.2026 angekündigt. Bis zu einer Verkündung gilt die Darlegungslast nach VIII ZR 190/03 unverändert. Eine neue Fassung wirkt als Ordnungswidrigkeitenrecht nicht zurück ([§ 4 OWiG](https://www.gesetze-im-internet.de/owig_1968/__4.html)) (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2004-01-28&Aktenzeichen=VIII%20ZR%20190/03).

## Deterministische Berechnung

```bash
# Verjährung des Rückforderungsanspruchs für zu viel gezahlte Miete aus März 2024
python -m scripts.legal_calc.cli verjaehrung --entstehung 03.03.2024 --kenntnis 03.03.2024

# Verfolgungsverjährung der Ordnungswidrigkeit (§ 31 Abs. 2 Nr. 1 OWiG: drei Jahre bei Höchstmaß > 15.000 EUR) — Planungsrechnung
python -m scripts.legal_calc.cli frist --ereignis 01.10.2026 --menge 3 --einheit jahre --kein-rollover
```

**Rechenweg Rückforderung** (von Hand):

```
Übliches Entgelt (EUR/m²) × 1,2 × Wohnfläche = Wesentlichkeitsgrenze (EUR/Monat)
Vereinbarte Miete − Wesentlichkeitsgrenze     = monatlicher Rückforderungsbetrag
× Zahl der nicht verjährten Monate             = Gesamtanspruch
```

## Quellen

### Statute

- § 5 WiStG (Wirtschaftsstrafgesetz 1954, amtl. Abk. WiStrG 1954) — https://www.gesetze-im-internet.de/wistrg_1954/__5.html
- [§ 291 StGB](https://www.gesetze-im-internet.de/stgb/__291.html), [§ 4 OWiG](https://www.gesetze-im-internet.de/owig_1968/__4.html), [§ 31 OWiG](https://www.gesetze-im-internet.de/owig_1968/__31.html)
- [§ 134 BGB](https://www.gesetze-im-internet.de/bgb/__134.html), [§ 138 BGB](https://www.gesetze-im-internet.de/bgb/__138.html), [§ 812 BGB](https://www.gesetze-im-internet.de/bgb/__812.html), [§ 195 BGB](https://www.gesetze-im-internet.de/bgb/__195.html), [§ 199 BGB](https://www.gesetze-im-internet.de/bgb/__199.html)
- [§ 556d BGB](https://www.gesetze-im-internet.de/bgb/__556d.html), [§ 556f BGB](https://www.gesetze-im-internet.de/bgb/__556f.html), [§ 558 BGB](https://www.gesetze-im-internet.de/bgb/__558.html)

### Gesetzgebung

- Gesetzentwurf des Bundesrates, BT-Drs. 21/1397 v. 27.08.2025 — https://dserver.bundestag.de/btd/21/013/2101397.pdf (Stand 23.10.2026: nicht verabschiedet)

### Kommentare

- Blank/Börstinghaus, Miete, aktuelle Auflage, § 5 WiStG
- Schmidt-Futterer, Mietrecht, 16. Aufl. 2024, § 5 WiStG (Bearbeiter und Rn. vor Zitat prüfen)
- Fischer, StGB, aktuelle Auflage, § 291 Rn. 1 ff.

### Rechtsprechung

- BGH, Urt. v. 28.01.2004 – VIII ZR 190/03, NJW 2004, 1740 = NZM 2004, 381 (Darlegung und Beweis der Ausnutzung durch den Mieter; kein Anscheinsbeweis) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2004-01-28&Aktenzeichen=VIII%20ZR%20190/03
- BGH, Beschl. v. 11.01.1984 – VIII ARZ 13/83, BGHZ 89, 316 = NJW 1984, 722 (Teilnichtigkeit; zulässiger Preis tritt an die Stelle) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=1984-01-11&Aktenzeichen=VIII%20ARZ%2013/83
- Zur Schwelle des auffälligen Missverhältnisses bei § 291 StGB ist die strafgerichtliche Rechtsprechung heranzuziehen `[unverifiziert – prüfen]`.

## Formulierungshilfe — Rückforderung wegen Mietpreisüberhöhung

```
Sehr geehrte Damen und Herren,

für die Wohnung <Anschrift> (<…> m²) zahle ich seit <Datum> eine
Nettokaltmiete von <Betrag> EUR (<…> EUR/m²). Die üblichen Entgelte für
vergleichbaren Wohnraum betragen nach dem Mietspiegel <Ort> (Feld <…>)
<…> EUR/m². Die Miete übersteigt sie damit um <…> %.

Ich habe vor Anmietung <…> Monate gesucht, mich auf <…> Wohnungen beworben
und <…> Absagen erhalten (Aufstellung anbei). Vergleichbarer Wohnraum war
nicht verfügbar. Ich war auf die Anmietung angewiesen.

Die Mietabrede ist nach § 134 BGB i.V.m. § 5 WiStG nichtig, soweit sie
120 % der üblichen Entgelte (<Betrag> EUR) übersteigt. Ich fordere Sie auf,
die Miete auf <Betrag> EUR herabzusetzen und die seit <Datum> zu viel
gezahlten <Betrag> EUR bis zum <Datum> zu erstatten.

Mit freundlichen Grüßen
```

## Ausgabeformat

```
MIETPREISÜBERHÖHUNG / MIETWUCHER — Prüfung — <Mandat-ID> — <Datum>

I.    Übliche Entgelte                  <…> EUR/m² (Quelle: <…>)
      Vereinbarte Miete                 <…> EUR/m²  → Überschreitung <…> %
II.   § 5 WiStG
      - > 20 %                          [✅ / ❌]
      - geringes Angebot (Teilmarkt)    [dargelegt / zweifelhaft]
      - Ausnutzung (VIII ZR 190/03)     [dargelegt / fehlt ⚠️]
      - Kostendeckungseinrede           [N/A / erhoben: <…>]
III.  § 291 StGB                        [kein Anhalt / auffälliges Missverhältnis + Zwangslage]
IV.   Rückforderung (§§ 134, 812)       Grenze 120 %: <Betrag>/Monat
      Überzahlung                       <Betrag>/Monat × <Monate> = <Betrag>
      Verjährung §§ 195, 199            nicht verjährt ab <Datum>
V.    Mietpreisbremse parallel          [N/A / einfacher: Rüge § 556g]
VI.   Reform BT-Drs. 21/1397            [nicht verabschiedet]

Ergebnis: <…>
Risiko: [🟢 / 🟡 / 🔴]
```

## Risiken / typische Fehler

- **Ausnutzung nicht dargelegt** — ohne konkrete Darlegung der eigenen Suche scheitert der Anspruch (VIII ZR 190/03); ein Anscheinsbeweis existiert nicht (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2004-01-28&Aktenzeichen=VIII%20ZR%20190/03).
- **Gesamtstadt statt Teilmarkt betrachtet** — das geringe Angebot ist für vergleichbaren Wohnraum im Teilmarkt darzulegen.
- **Rückforderung bis zur Vergleichsmiete berechnet** — zurückzufordern ist nur der Betrag über der Wesentlichkeitsgrenze von 120 %.
- **Mietpreisbremse übersehen** — in Gebieten mit Verordnung ist sie regelmäßig der einfachere Weg.
- **Reform als geltendes Recht behandelt** — die Streichung des Ausnutzungsmerkmals ist bisher nur Bundesratsentwurf (BT-Drs. 21/1397).
- **Verjährung übersehen** — für jeden Monat läuft die dreijährige Regelverjährung gesondert.
