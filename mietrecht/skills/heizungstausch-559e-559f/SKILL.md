---
name: heizungstausch-559e-559f
description: "Heizungstausch und Wärmepumpe im Wohnraummietrecht – Modernisierungstatbestand § 555b Nr. 1a BGB (Heizungsanlage i.S.d. § 42 GModG), Ankündigung § 555c BGB, Duldung und Härte § 555d BGB, Umlageweg: 10-%-Umlage mit Förderabzug und 15-%-Erhaltungspauschale § 559e BGB, 8-%-Umlage § 559 BGB nur ohne gewährte Förderung oder bei zugleich vorliegender Nr. 1-Maßnahme, Kappung 0,50 EUR/m² § 559 Abs. 3a S. 3, § 559e Abs. 3 BGB, Jahresarbeitszahl-Nachweis und Halbierung der umlagefähigen Kosten bei Wärmepumpen § 559f BGB (seit 29.07.2026), vereinfachtes Verfahren § 559c BGB, Folgen für CO2-Kosten §§ 5a, 5b CO2KostAufG. Rechtsstand: Oktober 2026. Use when ein Vermieter einen Heizungstausch ankündigt oder umlegt oder ein Mieter eine Mieterhöhung nach Einbau einer neuen Heizung oder Wärmepumpe prüft."
language: de
provider_variants: [claude, gemini, openai]
test: ./test.md
---

# /mietrecht:heizungstausch-559e-559f

## Zweck

Der Heizungstausch hat seit 2024 ein eigenes Umlageregime, und seit dem **29.07.2026** gilt eine zusätzliche Bedingung für Wärmepumpen. Wer die Mieterhöhung nach dem allgemeinen § 559 BGB rechnet, rechnet oft falsch. Bei förderfähigen Heizungen gilt § 559e BGB mit anderer Quote, Pauschalen und Deckel. Bei Wärmepumpen halbiert § 559f BGB die umlagefähigen Kosten, wenn der Effizienznachweis fehlt. Diese Skill führt durch Qualifikation, Ankündigung, Bestimmung des Umlageweges, Rechnung und Kappung und weist die Folgewirkungen auf die CO2-Kosten aus. Allgemeine Modernisierung: `/mietrecht:modernisierung-559-bgb`.

**Rechtsstand: Oktober 2026.**

- **Geltend:** Das Gebäudeenergiegesetz heißt seit dem Gesetz v. 23.07.2026 (BGBl. 2026 I Nr. 226, in Kraft 29.07.2026) **Gebäudemodernisierungsgesetz (GModG)**. § 555b Nr. 1a BGB verweist auf die Heizungsanlage i.S.d. **§ 42 GModG**, § 559e Abs. 2 BGB auf **§ 43 GModG**. **§ 559f BGB** ist neu.
- **Anhängig, nicht geltend:** Regierungsentwurf BT-Drs. 21/6807 v. 01.07.2026 (Anhörung 14.10.2026; Stand 23.10.2026 nicht verabschiedet) mit Folgeänderungen zu § 559e BGB in §§ 555c, 556e, 557a, 561 BGB und der Anhebung der Schwelle des § 559c BGB auf 20.000 EUR.

## Eingaben

- **Maßnahme:** alte Anlage (Art, Baujahr, Zustand, defekt?), neue Anlage (Wärmepumpe, Fernwärmeanschluss, Biomasse, Hybrid, Gas/Öl nach § 43 GModG)
- **Kosten** je Wohnung, Aufteilung Gebäude/Wohnung, Rechnungen
- **Förderung:** beantragt, bewilligt, ausgezahlt (Höhe), zinsverbilligte Darlehen
- Bei Wärmepumpe: **Jahresarbeitszahl** nach VDI 4650 Blatt 1 durch einen Fachunternehmer, Gebäudebaujahr, Wärmeschutzstandard, Auslegungs-Vorlauftemperatur
- Wohnfläche, Nettokaltmiete pro m², frühere Modernisierungserhöhungen in den letzten sechs Jahren
- Ankündigungsschreiben (Wortlaut, Zugang) und Erhöhungserklärung
- Mietstruktur: Staffel- oder Indexmiete?

## Sub-Agent-Architektur

Die Prüfung wird in Prosa von spezialisierten Schritten getragen; einen `agents`-Block trägt diese Skill bewusst nicht (mietrecht-Konvention).

- Ein **Qualifikations-Prüfer** ordnet die Maßnahme § 555b Nr. 1a BGB und gegebenenfalls zugleich Nr. 1 zu.
- Ein **Wege-Prüfer** klärt, ob § 559e BGB (Förderung in Anspruch genommen) oder § 559 BGB (keine Förderung trotz Förderfähigkeit) maßgeblich ist.
- Ein **Effizienz-Prüfer** prüft bei Wärmepumpen § 559f BGB: Nachweis, Ausnahmen, Halbierung.
- Ein **Rechen-Prüfer** rechnet die Erhöhung und spiegelt sie an allen Deckeln.
- Ein **Verfahrens-Prüfer** kontrolliert Ankündigung, Härteeinwand und Erhöhungserklärung.

## Ablauf

### 1. Qualifikation ([§ 555b Nr. 1, Nr. 1a BGB](https://www.gesetze-im-internet.de/bgb/__555b.html))

Nr. 1a erfasst bauliche Veränderungen, durch die eine **Heizungsanlage i.S.d. § 42 GModG** eingebaut oder aufgestellt wird. Spart die neue Anlage zugleich nachhaltig Endenergie ein, liegt auch eine **energetische Modernisierung** nach Nr. 1 vor. Dafür genügt eine zu erwartende, messbare und dauerhafte Einsparung (BGH, Urt. v. 26.03.2025 – VIII ZR 283/23, NJW 2025, 2023, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-03-26&Aktenzeichen=VIII%20ZR%20283/23).

Der Austausch einer **defekten** Anlage enthält einen **Erhaltungsanteil**, der nicht umlagefähig ist.

### 2. Welcher Umlageweg? ([§ 559e BGB](https://www.gesetze-im-internet.de/bgb/__559e.html), [§ 559 BGB](https://www.gesetze-im-internet.de/bgb/__559.html))

| Konstellation | Weg | Quote | Erhaltungsanteil | Deckel |
|---|---|---|---|---|
| Maßnahme nach Nr. 1a, dem Grunde nach förderfähig, **Drittmittel in Anspruch genommen** | § 559e Abs. 1 S. 1 BGB | **10 %** der Kosten abzüglich Drittmittel | **pauschal 15 %** (§ 559e Abs. 2 BGB; nicht bei Anlagen nach § 43 GModG) | **0,50 EUR/m²** monatlich in sechs Jahren (§ 559e Abs. 3 BGB) plus Gesamtgrenzen § 559 Abs. 3a S. 1, 2 BGB |
| Förderfähig, Förderung aber **nicht erfolgt** | § 559e Abs. 1 S. 2 → § 559 BGB | **8 %** | konkret zu ermitteln (§ 559 Abs. 2 BGB) | 0,50 EUR/m² für die Heizung (§ 559 Abs. 3a S. 3 BGB) plus 3 / 2 EUR/m² |
| Keine Nr. 1a-Maßnahme, aber Nr. 1 (z. B. Dämmung im selben Zug) | § 559 BGB | 8 % | konkret | 3 / 2 EUR/m² |

§ 559 Abs. 1 BGB nennt Nr. 1a **nicht**. Eine reine Nr. 1a-Maßnahme ist daher nur über § 559e BGB umlagefähig, sofern nicht zugleich Nr. 1 vorliegt oder der Fall des § 559e Abs. 1 S. 2 BGB greift. Ein freies Wahlrecht zwischen beiden Wegen besteht nicht. **Streitig** ist, ob der Vermieter durch bewussten Verzicht auf einen Förderantrag den Weg über § 559 BGB (8 %, ohne 15-%-Pauschale) selbst eröffnen kann `[unverifiziert – prüfen]`.

### 3. Wärmepumpe: Jahresarbeitszahl ([§ 559f BGB](https://www.gesetze-im-internet.de/bgb/__559f.html), seit 29.07.2026)

- **Abs. 1:** Beim Einbau oder Aufstellen einer **Wärmepumpe** ist die volle Erhöhung nach § 559 Abs. 1 oder § 559e Abs. 1 BGB nur zulässig, wenn der Vermieter eine **Jahresarbeitszahl von mindestens 2,5** nachweist. Der Nachweis ist durch einen **Fachunternehmer** zu führen und regelmäßig nach **VDI 4650 Blatt 1** vor Inbetriebnahme zu berechnen; Betriebsdaten sind nicht erforderlich.
- **Ausnahmen (kein Nachweis nötig):**
  - Nr. 1: Gebäude, die **nach 1996 errichtet** worden sind (ein Gebäude mit Baujahr 1996 fällt nicht darunter);
  - Nr. 2: Gebäude, die nach den Anforderungen der Wärmeschutzverordnung 1994 (Fassung bis 31.01.2002) errichtet wurden, oder deren Jahres-Heizwärmebedarf diese Anforderungen nachweislich nicht überschreitet;
  - Nr. 3: Gebäude, die nach einer Sanierung mindestens den Anforderungen des **§ 38 GModG** entsprechen;
  - Gebäude, die bei Normaußentemperatur mit einer Vorlauftemperatur von höchstens 55 °C beheizbar sind.
- **Abs. 2 — Rechtsfolge ohne Nachweis:** Die Erhöhung darf nur auf Grundlage der **Hälfte** der für die Wohnung aufgewendeten Kosten berechnet werden.
- **Übergang:** Maßgeblich ist der Zeitpunkt der Maßnahme bzw. der Erhöhungserklärung. Eine ausdrückliche Übergangsregel ist vor Anwendung auf Maßnahmen, die vor dem 29.07.2026 begonnen wurden, im EGBGB zu prüfen `[unverifiziert – prüfen]`.

### 4. Vereinfachtes Verfahren ([§ 559c BGB](https://www.gesetze-im-internet.de/bgb/__559c.html))

Bei Kosten bis **10.000 EUR** je Wohnung (vor Abzug) kann der Vermieter vereinfacht mit einem pauschalen Erhaltungsabzug von **30 %** rechnen. Die Ankündigung und die Erklärung müssen das Verfahren benennen. Danach sind fünf Jahre lang weitere Erhöhungen nach § 559 oder § 559e BGB grundsätzlich gesperrt. Für Heizungsanlagen, die zur Inbetriebnahme in einem Gebäude eingebaut werden, bleibt der Härteeinwand nach § 559 Abs. 4 BGB erhalten (§ 559c Abs. 1 S. 3 BGB). Die Anhebung der Schwelle auf **20.000 EUR** ist bisher nur Entwurf (BT-Drs. 21/6807).

### 5. Ankündigung, Duldung, Härte ([§§ 555c, 555d BGB](https://www.gesetze-im-internet.de/bgb/__555c.html), [§ 559 Abs. 4, 5 BGB](https://www.gesetze-im-internet.de/bgb/__559.html))

- **Ankündigung** drei Monate vor Beginn in Textform, mit Art, Umfang, Beginn, Dauer, zu erwartender Erhöhung und voraussichtlichen Betriebskosten. Fehler verschieben die Erhöhung um sechs Monate (§ 559b Abs. 2 S. 2 BGB).
- **Baubezogene Härte** (§ 555d Abs. 2 BGB): bis zum Ablauf des Monats nach Zugang der Ankündigung in Textform.
- **Wirtschaftliche Härte** (§ 559 Abs. 4 BGB, über § 559e Abs. 4 BGB auch für die Umlage nach § 559e): Die Abwägung entfällt grundsätzlich, wenn die Maßnahme auf Umständen beruht, die der Vermieter nicht zu vertreten hat (§ 559 Abs. 4 S. 2 Nr. 2 BGB). Das gilt aber **nicht** für den Heizungstausch: Nach der Rückausnahme („es sei denn") findet die Härteabwägung statt, wenn die Maßnahme auch § 555b Nr. 1 oder Nr. 1a erfüllt und mittels Einbaus oder Aufstellung einer Heizungsanlage zum Zwecke der Inbetriebnahme in einem Gebäude durchgeführt wurde. Auch eine gesetzliche Austauschpflicht nach dem GModG schließt den Härteeinwand des Mieters daher nicht aus. Die Härtegründe sind bis zum Ablauf des Monats nach Zugang der **Modernisierungsankündigung** in Textform mitzuteilen (§ 559 Abs. 5 S. 1 i.V.m. § 555d Abs. 3 S. 1 BGB); die Ausschlussfrist gilt nicht, wenn die tatsächliche Erhöhung die angekündigte um mehr als 10 % übersteigt (§ 559 Abs. 5 S. 2 BGB).
- **Minderung:** Der dreimonatige Minderungsausschluss des § 536 Abs. 1a BGB gilt nach geltendem Wortlaut für Maßnahmen nach § 555b **Nr. 1**. Bei einer reinen Nr. 1a-Maßnahme ist er nicht ausdrücklich erfasst.

### 6. Rechenbeispiel

Wohnung 70 m², Nettokaltmiete 9,00 EUR/m². Wärmepumpe, anteilige Kosten 18.000 EUR, Förderung 6.000 EUR. Altbau 1965, keine Ausnahme nach § 559f BGB.

| | mit JAZ-Nachweis ≥ 2,5 | ohne Nachweis (§ 559f Abs. 2) |
|---|---|---|
| Kostenbasis | 18.000 | 9.000 (Hälfte) |
| − 15 % Erhaltungspauschale (§ 559e Abs. 2) | 15.300 | 7.650 |
| − Drittmittel (§ 559e Abs. 1) | 9.300 | 1.650 `[Abzugsreihenfolge bei § 559f Abs. 2 ungeklärt – prüfen]` |
| × 10 % / 12 | 77,50 EUR/Monat | 13,75 EUR/Monat |
| Deckel 0,50 EUR/m² × 70 m² | **35,00 EUR/Monat** | 13,75 EUR/Monat |

Ergebnis: Mit Nachweis greift der Deckel, die Erhöhung beträgt 35,00 EUR monatlich. Ohne Nachweis sinkt sie unter den Deckel. Der Nachweis kostet den Vermieter regelmäßig weniger als die Differenz über sechs Jahre.

### 7. Folgewirkungen

- **CO2-Kosten:** Bei einer neuen Gas-/Ölheizung nach § 43 GModG werden ab 2028 die CO2-Kosten und Netzentgelte, ab 2029 die Beimischungskosten hälftig geteilt (§§ 5a, 5b CO2KostAufG). Vertiefung: `/mietrecht:heizkosten-co2-fernablesung`.
- **Staffelmiete:** § 557a Abs. 2 S. 2 BGB sperrt nach seinem Wortlaut nur Erhöhungen nach §§ 558 bis 559b BGB. Ob auch die Erhöhung nach **§ 559e BGB** während einer Staffelmiete gesperrt ist, ist **offen** `[unverifiziert – prüfen]`; der Regierungsentwurf BT-Drs. 21/6807 will § 559e BGB ausdrücklich in die Sperre aufnehmen (Folgeänderung zu § 557a BGB). **Indexmiete:** Eine Erhöhung nach § 559 oder § 559e BGB ist grundsätzlich nur bei Maßnahmen zulässig, die der Vermieter nicht zu vertreten hat, **es sei denn, es wurde eine Modernisierungsmaßnahme nach § 555b Nr. 1a BGB durchgeführt** (§ 557b Abs. 2 S. 2 BGB). Der Heizungstausch ist also auch bei Indexmiete umlagefähig. Vertiefung: `/mietrecht:indexmiete-staffelmiete`.
- **Mietpreisbremse:** Eine Modernisierung in den letzten drei Jahren vor Mietbeginn erhöht die zulässige Miete nach § 556e Abs. 2 BGB. Die Einbeziehung des § 559e BGB dort ist Gegenstand des Entwurfs.

## Deterministische Berechnung

```bash
# Ankündigungsfrist § 555c Abs. 1 S. 1 BGB: „spätestens drei Monate vor ihrem Beginn".
# Baubeginn 01.03.2027 → Zugang spätestens am 30.11.2026 (sichere Rückrechnung).
# Gegenprobe vorwärts: Zugang 30.11.2026 + 3 Monate → Fristende 28.02.2027, Beginn am 01.03.2027 liegt danach.
# Kein § 193 BGB (Rückrechnung zugunsten des Mieters).
python -m scripts.legal_calc.cli frist --ereignis 30.11.2026 --menge 3 --einheit monate --kein-rollover --land NI
```

**Fälligkeit der erhöhten Miete (§ 559b Abs. 2 BGB)** ist eine Kalenderregel ohne Rechneraufruf: geschuldet „mit Beginn des dritten Monats nach dem Zugang der Erklärung" — Zugang im November 2026 → erhöhte Miete ab **01.02.2027**. Die Frist verlängert sich um **sechs Monate** (→ 01.08.2027), wenn die Maßnahme nicht nach § 555c Abs. 1 bis 3 BGB angekündigt wurde oder die tatsächliche Erhöhung die angekündigte um mehr als 10 % übersteigt (§ 559b Abs. 2 S. 2 BGB).

Der Rechner macht nur die Arithmetik der Fristen. Die Umlagerechnung ist nach dem Schema in Nr. 6 von Hand zu führen und gegen den Gesetzeswortlaut zu prüfen.

## Quellen

### Statute

- [§ 555b BGB](https://www.gesetze-im-internet.de/bgb/__555b.html), [§ 555c BGB](https://www.gesetze-im-internet.de/bgb/__555c.html), [§ 555d BGB](https://www.gesetze-im-internet.de/bgb/__555d.html), [§ 536 BGB](https://www.gesetze-im-internet.de/bgb/__536.html)
- [§ 559 BGB](https://www.gesetze-im-internet.de/bgb/__559.html), [§ 559a BGB](https://www.gesetze-im-internet.de/bgb/__559a.html), [§ 559b BGB](https://www.gesetze-im-internet.de/bgb/__559b.html), [§ 559c BGB](https://www.gesetze-im-internet.de/bgb/__559c.html), [§ 559e BGB](https://www.gesetze-im-internet.de/bgb/__559e.html), [§ 559f BGB](https://www.gesetze-im-internet.de/bgb/__559f.html)
- [§ 557a BGB](https://www.gesetze-im-internet.de/bgb/__557a.html), [§ 557b BGB](https://www.gesetze-im-internet.de/bgb/__557b.html), [§ 556e BGB](https://www.gesetze-im-internet.de/bgb/__556e.html)
- Gebäudemodernisierungsgesetz (GModG, vormals GEG; amtliche URL weiter unter `geg`): [§ 42 GModG](https://www.gesetze-im-internet.de/geg/__42.html), [§ 43 GModG](https://www.gesetze-im-internet.de/geg/__43.html)
- [CO2KostAufG](https://www.gesetze-im-internet.de/co2kostaufg/) §§ 5a, 5b; Gebäudemodernisierungsgesetz (vormals GEG) i.d.F. des Gesetzes v. 23.07.2026, BGBl. 2026 I Nr. 226

### Gesetzgebung

- Regierungsentwurf, BT-Drs. 21/6807 v. 01.07.2026 — https://dserver.bundestag.de/btd/21/068/2106807.pdf (Stand 23.10.2026: nicht verabschiedet)

### Kommentare

- Börstinghaus, in: Schmidt-Futterer, Mietrecht, 16. Aufl. 2024, § 559 BGB (die Kommentierung des § 559f BGB ist nach dessen Inkrafttreten erst in Nachträgen bzw. Online-Kommentaren zu erwarten)
- Artz, in: MüKoBGB, 9. Aufl. 2023, § 559 Rn. 1 ff.

### Rechtsprechung

- BGH, Urt. v. 26.03.2025 – VIII ZR 283/23, NJW 2025, 2023 (energetische Modernisierung; zu erwartende Einsparung genügt) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-03-26&Aktenzeichen=VIII%20ZR%20283/23
- Zu §§ 559e, 559f BGB liegt nach dem Kenntnisstand dieser Skill (Oktober 2026) **keine** verifizierte BGH-Rechtsprechung vor.

## Formulierungshilfe — Erhöhungserklärung nach § 559e BGB (Auszug)

```
Für die Wohnung entfallen auf die Maßnahme Kosten von 18.000,00 EUR.
Nach § 559e Abs. 2 BGB bleiben pauschal 15 % (2.700,00 EUR) als
Erhaltungsanteil außer Ansatz. Von den verbleibenden 15.300,00 EUR sind die
in Anspruch genommenen Fördermittel von 6.000,00 EUR abzuziehen
(§ 559e Abs. 1 BGB). 10 % von 9.300,00 EUR ergeben 930,00 EUR jährlich,
also 77,50 EUR monatlich. Nach § 559e Abs. 3 BGB ist die Erhöhung auf
0,50 EUR/m² begrenzt; bei 70 m² Wohnfläche erhöht sich die Miete daher um
35,00 EUR monatlich.

Die Wärmepumpe erreicht nach der beigefügten Berechnung des
Fachunternehmers <Name> nach VDI 4650 Blatt 1 eine Jahresarbeitszahl von
<…> (§ 559f Abs. 1 BGB).

Die erhöhte Miete ist ab dem <Beginn des dritten Monats nach Zugang> zu
zahlen.
```

## Ausgabeformat

```
HEIZUNGSTAUSCH — Prüfung — <Mandat-ID> — <Datum>

I.    Qualifikation                    [§ 555b Nr. 1a / zugleich Nr. 1 / Erhaltung]
II.   Umlageweg                        [§ 559e (Förderung) / § 559 (keine Förderung) / § 559c]
III.  Wärmepumpe § 559f                [N/A / JAZ ≥ 2,5 nachgewiesen / Ausnahme / Halbierung]
IV.   Rechnung
      Kosten / Basis                   <…>
      Erhaltung (15 % pauschal / konkret / 30 %) <…>
      Drittmittel                      <…>
      Quote (10 % / 8 %)               <…> EUR/Monat
      Deckel 0,50 EUR/m² (+ 3/2 EUR)   <…> EUR/Monat
      Ergebnis                         <…> EUR/Monat
V.    Verfahren
      Ankündigung § 555c               [✅ / ❌ → +6 Monate]
      Härteeinwand § 555d / § 559 Abs. 4 [N/A / erhoben / ausgeschlossen]
VI.   Folgewirkungen                   [CO2 §§ 5a/5b ab 2028 / Staffel- oder Indexsperre]

Ergebnis: <…>
Risiko: [🟢 / 🟡 / 🔴]
```

## Risiken / typische Fehler

- **Wärmepumpe ohne JAZ-Nachweis voll umgelegt** — seit 29.07.2026 ist nur die Hälfte der Kosten umlagefähig (§ 559f Abs. 2 BGB), wenn keine Ausnahme greift.
- **Nr. 1a-Maßnahme nach § 559 Abs. 1 BGB mit 8 % gerechnet** — § 559 Abs. 1 BGB erfasst Nr. 1a nicht; maßgeblich ist § 559e BGB, außer im Fall des § 559e Abs. 1 S. 2 BGB.
- **Deckel 0,50 EUR/m² übersehen** — er gilt für die Heizungsanlage auf beiden Wegen.
- **Fördermittel nicht abgezogen** — bei § 559e BGB sind die in Anspruch genommenen Drittmittel von den Kosten abzuziehen.
- **15-%-Pauschale bei Anlage nach § 43 GModG angesetzt** — § 559e Abs. 2 BGB nimmt diese Anlagen aus.
- **Staffelmiete ignoriert** — §§ 558 bis 559b BGB sind während der Staffelmiete gesperrt; ob das auch für § 559e BGB gilt, ist offen und vor einer Erhöhung zu klären.
- **Indexmiete als Sperre behandelt** — für Maßnahmen nach § 555b Nr. 1a BGB lässt § 557b Abs. 2 S. 2 BGB die Erhöhung ausdrücklich zu.
- **Entwurfsänderungen angewendet** — die Schwelle von 20.000 EUR für § 559c BGB und die Folgeänderungen sind bisher nur Regierungsentwurf (BT-Drs. 21/6807).
