---
name: massenentlassungsanzeige
description: "Massenentlassung nach §§ 17, 18 KSchG – Schwellenwerte § 17 Abs. 1 KSchG und Betriebsbegriff, Konsultationsverfahren mit dem Betriebsrat § 17 Abs. 2 KSchG, Abschrift an die Agentur für Arbeit § 17 Abs. 3 S. 1 KSchG, Muss- und Soll-Angaben der Anzeige § 17 Abs. 3 S. 4 und 5 KSchG, Entlassungssperre und Freifrist § 18 KSchG, Umsetzung der Richtlinie 98/59/EG, Rechtsfolgen von Konsultations- und Anzeigefehlern. Use when ein Arbeitgeber einen Personalabbau plant, der die Schwellen des § 17 KSchG erreichen könnte, oder wenn eine ausgesprochene Kündigung auf Massenentlassungsfehler geprüft wird."
language: de
agents:
  researcher: ../../agents/researcher.md
  drafter: ../../agents/drafter.md
  reviewer: ../../agents/reviewer.md
provider_variants: [claude, gemini, openai]
test: ./test.md
---

# /arbeitsrecht:massenentlassungsanzeige

## Zweck

Die Massenentlassungsanzeige ist ein Verfahren mit zwei getrennten Strängen: das **Konsultationsverfahren** mit dem Betriebsrat (§ 17 Abs. 2 KSchG) und die **Anzeige** an die Agentur für Arbeit (§ 17 Abs. 1, 3 KSchG). Beide sind vor Ausspruch der Kündigungen abzuschließen, beide haben eigene Fehlerfolgen — und das BAG unterscheidet nach dem **Rechtsstand Oktober 2026** drei Fehlerstufen (EuGH v. 30.10.2025; BAG v. 19.03.2026, 01.04.2026 und 25.06.2026 — Nachweise unter Nr. 5): Konsultations- und Reihenfolgefehler sowie die fehlende Anzeige führen zur Unwirksamkeit, bloße Inhaltsfehler der Anzeige nur dann, wenn sie die Arbeitsverwaltung an ihrer Aufgabe hindern. Dieser Skill trennt die Stränge und dokumentiert den Ablauf prüffest.

> **Rechtsstand: Oktober 2026.** Berücksichtigt: EuGH 30.10.2025, BAG 19.03.2026, 01.04.2026 und 25.06.2026.
## Eingaben

- **Betriebsbegriff:** Welche organisatorische Einheit ist „Betrieb" im Sinne der Richtlinie 98/59/EG? (unionsrechtlich autonom, nicht identisch mit § 1 BetrVG)
- Regelmäßige Beschäftigtenzahl des Betriebs (§ 17 Abs. 5 KSchG: Organmitglieder, Geschäftsführer, Betriebsleiter zählen nicht)
- Geplante Zahl der Entlassungen und **Zeitraum** (30 Kalendertage, rollierend)
- Andere vom Arbeitgeber veranlasste Beendigungen (Aufhebungsverträge!) — § 17 Abs. 1 S. 2 KSchG
- Betriebsrat vorhanden? Interessenausgleich und Sozialplan (§§ 111, 112 BetrVG) geplant?
- Beherrschendes Unternehmen im Konzern beteiligt? (§ 17 Abs. 3a KSchG)

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert §§ 17, 18 KSchG mit URL, Richtlinie 98/59/EG, EuGH- und BAG-Linien zu Anzeige- und Konsultationsfehlern.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) erstellt Unterrichtungsschreiben an den Betriebsrat, Anzeigetext und Zeitplan.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Schwellenberechnung, Reihenfolge der Verfahrensschritte und Vollständigkeit der Angaben.

## Ablauf

### 1. Schwellenwerte ([§ 17 Abs. 1 KSchG](https://www.gesetze-im-internet.de/kschg/__17.html))

Anzeigepflicht besteht, wenn innerhalb von **30 Kalendertagen** entlassen werden:

| Betriebsgröße (i.d.R. Beschäftigte) | Schwelle |
|---|---|
| > 20 und < 60 | mehr als 5 Arbeitnehmer |
| ≥ 60 und < 500 | 10 % der regelmäßig Beschäftigten **oder** mehr als 25 Arbeitnehmer |
| ≥ 500 | mindestens 30 Arbeitnehmer |

Drei Fallen bei der Berechnung:

1. **„Entlassung" ist der Ausspruch der Kündigung**, nicht das Ende des Arbeitsverhältnisses (richtlinienkonforme Auslegung nach EuGH, Urt. v. 27.01.2005 – C-188/03, *Junk*; [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=27.01.2005&Aktenzeichen=C-188/03)). Maßgeblich ist der Zeitraum, in dem die Kündigungen **erklärt** werden.
2. **Aufhebungsverträge zählen mit** (§ 17 Abs. 1 S. 2 KSchG: „andere Beendigungen, die vom Arbeitgeber veranlasst werden"). Der Versuch, unter der Schwelle zu bleiben, indem man Aufhebungsverträge vorschaltet, geht regelmäßig fehl.
3. **Fristlose Entlassungen** werden nach § 17 Abs. 4 S. 2 KSchG bei der Mindestzahl **nicht** mitgerechnet.

Der **Betriebsbegriff** ist unionsrechtlich auszulegen: eine unterscheidbare Einheit von gewisser Dauer und Stabilität mit eigener Belegschaft und technischen Mitteln — organisatorische Selbständigkeit oder ein eigener Betriebsrat sind nicht erforderlich (EuGH-Rspr. zum Betriebsbegriff der Richtlinie 98/59/EG `[unverifiziert – prüfen]`).

### 2. Konsultationsverfahren ([§ 17 Abs. 2 KSchG](https://www.gesetze-im-internet.de/kschg/__17.html))

Der Arbeitgeber hat dem Betriebsrat **rechtzeitig** die zweckdienlichen Auskünfte zu erteilen und ihn **schriftlich** zu unterrichten über:

1. die Gründe für die geplanten Entlassungen,
2. Zahl und Berufsgruppen der zu entlassenden Arbeitnehmer,
3. Zahl und Berufsgruppen der in der Regel beschäftigten Arbeitnehmer,
4. den Zeitraum, in dem die Entlassungen vorgenommen werden sollen,
5. die vorgesehenen Auswahlkriterien,
6. die für die Berechnung etwaiger Abfindungen vorgesehenen Kriterien.

Anschließend ist mit dem Betriebsrat **ernsthaft zu beraten**, ob Entlassungen vermieden oder eingeschränkt und ihre Folgen gemildert werden können (§ 17 Abs. 2 S. 2 KSchG). Das Verfahren muss vor Ausspruch der Kündigungen **abgeschlossen** sein — der Abschluss ist zu dokumentieren (abschließende Stellungnahme des Betriebsrats, Protokoll, Interessenausgleich).

**Konzernklausel:** Nach § 17 Abs. 3a KSchG gelten die Pflichten auch, wenn die Entscheidung von einem beherrschenden Unternehmen getroffen wurde; der Arbeitgeber kann sich nicht darauf berufen, dieses habe die Auskünfte nicht übermittelt.

### 3. Anzeige an die Agentur für Arbeit ([§ 17 Abs. 3 KSchG](https://www.gesetze-im-internet.de/kschg/__17.html))

Zwei getrennte Übermittlungen:

- **Abschrift der BR-Unterrichtung** (§ 17 Abs. 3 S. 1 KSchG): gleichzeitig mit der Unterrichtung des Betriebsrats an die Agentur; sie muss mindestens die Angaben zu Abs. 2 S. 1 Nr. 1–5 enthalten.
- **Anzeige** (§ 17 Abs. 3 S. 2 KSchG): schriftlich, unter Beifügung der **Stellungnahme des Betriebsrats**. Liegt keine Stellungnahme vor, ist die Anzeige nur wirksam, wenn der Arbeitgeber glaubhaft macht, den Betriebsrat mindestens **zwei Wochen** vor Erstattung der Anzeige unterrichtet zu haben, und den Stand der Beratungen darlegt (§ 17 Abs. 3 S. 3 KSchG).

**Muss-Angaben** der Anzeige (§ 17 Abs. 3 S. 4 KSchG): Name des Arbeitgebers, Sitz und Art des Betriebes, Gründe für die geplanten Entlassungen, Zahl und Berufsgruppen der zu entlassenden und der in der Regel beschäftigten Arbeitnehmer, Zeitraum der Entlassungen, vorgesehene Auswahlkriterien.

**Soll-Angaben** (§ 17 Abs. 3 S. 5 KSchG): im Einvernehmen mit dem Betriebsrat Angaben über Geschlecht, Alter, Beruf und Staatsangehörigkeit der zu entlassenden Arbeitnehmer — sie dienen der Arbeitsvermittlung. Ihr Fehlen ist nach h.M. unschädlich.

Dem Betriebsrat ist eine Abschrift der Anzeige zuzuleiten (§ 17 Abs. 3 S. 6 KSchG); er kann gegenüber der Agentur weitere Stellungnahmen abgeben.

### 4. Entlassungssperre und Freifrist ([§ 18 KSchG](https://www.gesetze-im-internet.de/kschg/__18.html))

- **Sperrfrist:** Entlassungen werden vor Ablauf eines Monats nach Eingang der Anzeige nur mit Zustimmung der Agentur wirksam; die Zustimmung kann rückwirkend bis zum Tag der Antragstellung erteilt werden (§ 18 Abs. 1 KSchG).
- Die Agentur kann im Einzelfall bestimmen, dass die Entlassungen erst nach **längstens zwei Monaten** wirksam werden (§ 18 Abs. 2 KSchG).
- **Freifrist:** Werden die Entlassungen nicht innerhalb von **90 Tagen** nach dem Zeitpunkt durchgeführt, zu dem sie zulässig wurden, ist eine **erneute Anzeige** erforderlich (§ 18 Abs. 4 KSchG).

Die Sperrfrist betrifft die Wirksamkeit der **Beendigung**, nicht die des Kündigungsausspruchs — die Kündigung darf nach wirksamer Anzeige ausgesprochen werden, das Arbeitsverhältnis endet aber frühestens nach Ablauf der Sperrfrist.

### 5. Rechtsfolgen von Fehlern — das Drei-Stufen-Modell (Rechtsstand Oktober 2026)

Historisch behandelte die Rechtsprechung **jeden** Verstoß gegen §§ 17, 18 KSchG als zur Unwirksamkeit der Kündigung führend. Nach EuGH C-134/22 (2023; [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=13.07.2023&Aktenzeichen=C-134/22)) entwickelte sich eine Gegenlinie, die Fehler im **Anzeigeverfahren** sanktionslos stellen wollte. **Diese pauschale Entlastungslinie ist überholt.** EuGH und BAG haben 2025/2026 ein abgestuftes Modell entwickelt:

| Fehler | Rechtsfolge (Rechtsstand Oktober 2026) |
|---|---|
| **Konsultationsverfahren § 17 Abs. 2 KSchG** nicht oder nicht vollständig durchgeführt / nicht abgeschlossen | Kündigung **unwirksam** — die Vorschrift ist arbeitnehmerschützend |
| **Anzeige vor Abschluss der Konsultation** erstattet (Reihenfolgefehler) | Kündigung **unwirksam** — amtlicher Leitsatz BAG 01.04.2026 – 6 AZR 152/22 ([dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BAG&Datum=2026-04-01&Aktenzeichen=6%20AZR%20152/22)) |
| **Anzeige § 17 Abs. 1, 3 KSchG** ganz unterblieben | Kündigung **unwirksam**; die Sperrfrist des Art. 4 Abs. 1 der Richtlinie 98/59/EG beginnt ohne wirksame Anzeige nicht zu laufen, eine **Nachholung heilt nicht** — der 2. Senat hält daran fest (BAG, Beschl. v. 19.03.2026 – 2 AS 22/23, [bundesarbeitsgericht.de](https://www.bundesarbeitsgericht.de/entscheidung/2-as-22-23/)) |
| **Anzeige inhaltlich fehlerhaft** bei korrekter Reihenfolge | **Unwirksamkeit nur**, wenn der Fehler die Arbeitsverwaltung daran hindert, ihre gesetzliche Aufgabe zu erfüllen; ein unschädlicher Fehler (dort: 34 angezeigte statt 31 tatsächlich ausgesprochener Entlassungen) lässt die Kündigungen wirksam (BAG, Urt. v. 25.06.2026 – 6 AZR 7/26, [bundesarbeitsgericht.de](https://www.bundesarbeitsgericht.de/entscheidung/6-azr-7-26/)). Ob fehlende Muss-Angaben nach § 17 Abs. 3 S. 4 KSchG stets aufgabenrelevant sind, ist offen `[unverifiziert – prüfen]`. **Spannung zwischen den Senaten:** Der 2. Senat (2 AS 22/23) spricht von einer „nicht oder nicht ordnungsgemäß erstatteten“ Anzeige; ob er die Erheblichkeitsschwelle des 6. Senats teilt, ist nicht geklärt — im Zweifel die strengere Linie zugrunde legen |

> **Was sich geändert hat und warum es zählt.** Der EuGH verlangt in **C-134/24 (*Tomann*)** ([dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2025-10-30&Aktenzeichen=C-134/24)) und **C-402/24 (*Sewel*)** ([dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2025-10-30&Aktenzeichen=C-402/24)), beide vom **30.10.2025**, dass das Konsultationsverfahren der Anzeige **vorausgeht** und dass die Verfahrensschritte **erfüllt**, nicht bloß **eingeleitet** sind; eine nachträgliche Heilung ist ausgeschlossen. Das BAG hat dies mit Urt. v. **01.04.2026 – 6 AZR 152/22** ([dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BAG&Datum=2026-04-01&Aktenzeichen=6%20AZR%20152/22); Fundstelle NZA 2026, 669 `[unverifiziert – prüfen]`) umgesetzt. Wer noch mit der Entlastungslinie von 2024 arbeitet, verteidigt auf einer aufgegebenen Position.

Hintergrund ist die unionsrechtliche Vorgabe: Der EuGH hat entschieden, dass die Übermittlung der Abschrift der Unterrichtung an die Arbeitsverwaltung (Art. 2 Abs. 3 Unterabsatz 2 der Richtlinie 98/59/EG, umgesetzt in § 17 Abs. 3 S. 1 KSchG) dem einzelnen Arbeitnehmer **keine individuelle Rechtsposition** vermittelt, sondern allein der Information und Vorbereitung der zuständigen Behörde dient (EuGH, Urt. v. 13.07.2023 – C-134/22; [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=13.07.2023&Aktenzeichen=C-134/22)). Das BAG hat die Sanktionsfolge von Anzeigefehlern seither abgestuft: kein Wegfall der Unwirksamkeitsfolge bei fehlender Anzeige (2. Senat, 19.03.2026), aber Folgenlosigkeit aufgabenneutraler Inhaltsfehler (6. Senat, 25.06.2026) — Nachweise in der Tabelle und unter Rechtsprechung.

> **Verfahrensgeschichte.** Der Sechste Senat hat **6 AZR 152/22** mit Beschl. v. 23.05.2024 (BAGE 183, 254 = NZA 2024, 813; [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BAG&Datum=2024-05-23&Aktenzeichen=6%20AZR%20152/22)) dem EuGH vorgelegt und nach dessen Antwort mit Urt. v. **01.04.2026** entschieden (NZA 2026, 669 `[unverifiziert – prüfen]`; [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BAG&Datum=2026-04-01&Aktenzeichen=6%20AZR%20152/22)). Amtlicher Leitsatz: „Erstattet der Arbeitgeber eine – erforderliche – Massenentlassungsanzeige vor Abschluss des Konsultationsverfahrens mit dem Betriebsrat, ist die daraufhin ausgesprochene Kündigung unwirksam."

> **Praxishinweis:** Entlastung gibt es nur auf der dritten Stufe und nur für aufgabenneutrale Inhaltsfehler. Das Konsultationsverfahren ist **vor** der Anzeige abzuschließen, die Anzeige vollständig zu erstatten, und beides zu dokumentieren. Hinzu kommen das Bußgeld nach § 121 SGB III und die Verzögerung durch die Sperrfrist. Eine Verteidigung, die auf der Sanktionslosigkeit von Konsultations- oder Reihenfolgefehlern aufbaut, ist nach dem Rechtsstand Oktober 2026 nicht tragfähig; bei bloßen Inhaltsfehlern ist die Aufgabenrelevanz konkret darzulegen.

### 6. Reihenfolge — der prüffeste Zeitplan

```
T-0    Unternehmerische Entscheidung dokumentieren (Beschluss, Datum)
T+1    Unterrichtung des Betriebsrats § 17 Abs. 2 S. 1 KSchG (schriftlich)
       GLEICHZEITIG: Abschrift an die Agentur für Arbeit § 17 Abs. 3 S. 1 KSchG
T+2..  Beratung § 17 Abs. 2 S. 2 KSchG — Protokolle führen
       ggf. Verhandlung Interessenausgleich / Sozialplan §§ 111, 112 BetrVG
T+n    Abschluss des Konsultationsverfahrens dokumentieren
       (abschließende Stellungnahme des BR oder Nachweis nach
        § 17 Abs. 3 S. 3 KSchG: Unterrichtung ≥ 2 Wochen zuvor)
T+n+1  Anzeige § 17 Abs. 3 S. 2 KSchG bei der örtlich zuständigen
       Agentur für Arbeit, mit Stellungnahme des BR
       Abschrift der Anzeige an den Betriebsrat § 17 Abs. 3 S. 6 KSchG
T+n+2  BR-Anhörung zu den einzelnen Kündigungen § 102 BetrVG
       (eigenständiges Verfahren — NICHT durch § 17 Abs. 2 KSchG ersetzt)
T+n+3  Ausspruch der Kündigungen
       Beendigung frühestens nach Ablauf der Sperrfrist § 18 Abs. 1 KSchG
       Durchführung binnen 90 Tagen § 18 Abs. 4 KSchG
```

### 7. Formulierungshilfe — Unterrichtung des Betriebsrats

```
An den Betriebsrat
z. Hd. des Vorsitzenden

Unterrichtung und Konsultation nach § 17 Abs. 2 KSchG

Sehr geehrte(r) Herr/Frau <Name>,

wir unterrichten den Betriebsrat hiermit schriftlich über eine
geplante anzeigepflichtige Massenentlassung und laden zur
Beratung nach § 17 Abs. 2 S. 2 KSchG ein.

1. Gründe für die geplanten Entlassungen
   <unternehmerische Entscheidung, Beschlussdatum, wirtschaftlicher
    Hintergrund, Wegfall welcher Funktionen>
2. Zahl und Berufsgruppen der zu entlassenden Arbeitnehmer
   <Tabelle: Berufsgruppe / Anzahl>
3. Zahl und Berufsgruppen der in der Regel beschäftigten Arbeitnehmer
   <Tabelle; Berechnung nach § 17 Abs. 5 KSchG erläutern>
4. Zeitraum der Entlassungen
   <Datum bis Datum — Ausspruch der Kündigungen>
5. Vorgesehene Auswahlkriterien
   <Vergleichsgruppenbildung, Sozialauswahlkriterien § 1 Abs. 3 KSchG,
    ggf. Punkteschema>
6. Kriterien für die Berechnung etwaiger Abfindungen
   <Formel oder Verweis auf Sozialplanentwurf>

Wir schlagen als Beratungstermin den <Datum> vor. Gegenstand der
Beratung sind insbesondere Möglichkeiten, Entlassungen zu vermeiden
oder einzuschränken und ihre Folgen zu mildern.

Eine Abschrift dieser Unterrichtung haben wir zeitgleich der Agentur
für Arbeit <Ort> gemäß § 17 Abs. 3 S. 1 KSchG zugeleitet.

<Ort, Datum, Unterschrift>
Empfangsbestätigung: ____________________
```

## Quellen

### Statute

- [§ 17 KSchG](https://www.gesetze-im-internet.de/kschg/__17.html), [§ 18 KSchG](https://www.gesetze-im-internet.de/kschg/__18.html), [§ 1 KSchG](https://www.gesetze-im-internet.de/kschg/__1.html), [§ 4 KSchG](https://www.gesetze-im-internet.de/kschg/__4.html)
- [§ 102 BetrVG](https://www.gesetze-im-internet.de/betrvg/__102.html), [§ 111 BetrVG](https://www.gesetze-im-internet.de/betrvg/__111.html), [§ 112 BetrVG](https://www.gesetze-im-internet.de/betrvg/__112.html)
- Richtlinie 98/59/EG des Rates vom 20.07.1998 über Massenentlassungen

### Kommentare

- Kiel, in: ErfK, 24. Aufl. 2024, § 17 KSchG Rn. 1 ff.
- Moll, in: APS, 6. Aufl. 2021, § 17 KSchG Rn. 40 ff. (Konsultationsverfahren)
- Weigand, in: KR, 13. Aufl. 2022, § 17 KSchG Rn. 1 ff.
- Spelge, in: BeckOK Arbeitsrecht, § 18 KSchG Rn. 1 ff. (Sperr- und Freifrist)

### Rechtsprechung

- EuGH, Urt. v. 27.01.2005 – C-188/03, *Junk* (Begriff der „Entlassung" = Ausspruch der Kündigung, nicht Beendigung des Arbeitsverhältnisses), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=27.01.2005&Aktenzeichen=C-188/03)
- EuGH-Rspr. zum unionsrechtlichen Betriebsbegriff der Richtlinie 98/59/EG `[unverifiziert – prüfen]`
- EuGH, Urt. v. 13.07.2023 – C-134/22 (Art. 2 Abs. 3 Unterabsatz 2 der Richtlinie 98/59/EG bzw. § 17 Abs. 3 S. 1 KSchG: Abschrift an die Agentur dient der Behördeninformation und vermittelt keine individuelle Rechtsposition), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=13.07.2023&Aktenzeichen=C-134/22)
- BAG, Beschl. v. 23.05.2024 – 6 AZR 152/22 (A), BAGE 183, 254 = NZA 2024, 813 (Vorlage an den EuGH zu den Folgen von Fehlern im Anzeigeverfahren), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BAG&Datum=2024-05-23&Aktenzeichen=6%20AZR%20152/22)
- BAG, Urt. v. 01.04.2026 – 6 AZR 152/22, NZA 2026, 669 `[unverifiziert – prüfen]` (Anzeige vor Abschluss des Konsultationsverfahrens → Kündigung unwirksam), [bundesarbeitsgericht.de](https://www.bundesarbeitsgericht.de/entscheidung/6-azr-152-22/)
- BAG, Beschl. v. 19.03.2026 – 2 AS 22/23 (§ 45 Abs. 3 ArbGG; Kündigung ohne wirksame Anzeige unwirksam, keine Heilung durch Nachholung), [bundesarbeitsgericht.de](https://www.bundesarbeitsgericht.de/entscheidung/2-as-22-23/)
- BAG, Urt. v. 25.06.2026 – 6 AZR 7/26 (Inhaltsfehler der Anzeige nur beachtlich, wenn sie die Arbeitsverwaltung an ihrer Aufgabe hindern), [bundesarbeitsgericht.de](https://www.bundesarbeitsgericht.de/entscheidung/6-azr-7-26/)
- st. Rspr. des BAG zu § 17 Abs. 2 KSchG (Konsultationsverfahren ist arbeitnehmerschützend; Kündigung vor Abschluss ist unwirksam) `[unverifiziert – prüfen]`

> Die Entscheidungen von 2026 sind über die [BAG-Entscheidungsdatenbank](https://www.bundesarbeitsgericht.de/entscheidungen/) verifiziert; Fundstellen in Fachzeitschriften vor Verwendung in juris abgleichen.

## Ausgabeformat

```
MASSENENTLASSUNG §§ 17, 18 KSchG — <Mandat-ID> — <Datum>
VERTRAULICH — MANDATSGEHEIMNIS — § 43a Abs. 2 BRAO

Gesamtbefund: [🟢 anzeigefrei / 🟡 anzeigepflichtig, Verfahren läuft /
               🔴 Fehler im laufenden Verfahren]

I.    Betriebsbegriff                    <Einheit, Begründung>
II.   Regelmäßige Beschäftigtenzahl      <N>  (§ 17 Abs. 5 KSchG bereinigt)
III.  Geplante Entlassungen im 30-Tage-Zeitraum
      Kündigungen:                       <N>
      Aufhebungsverträge (§ 17 I 2):     <N>
      Summe / Schwelle:                  <N> / <Schwelle>   [🟢 / 🔴]
IV.   Konsultationsverfahren § 17 Abs. 2
      Unterrichtung am:                  <Datum>  [🟢 vollständig / 🔴]
      Beratung am:                       <Datum>
      Abschluss dokumentiert:            [🟢 / 🔴]
V.    Abschrift an Agentur § 17 Abs. 3 S. 1  [🟢 am <Datum> / 🔴]
VI.   Anzeige § 17 Abs. 3 S. 2
      Eingang bei der Agentur:           <Datum>
      Muss-Angaben vollständig:          [🟢 / 🔴 fehlt: <…>]
      Soll-Angaben:                      [🟢 / entfallen]
      BR-Stellungnahme beigefügt:        [🟢 / Nachweis § 17 III 3]
VII.  Sperrfrist § 18 Abs. 1              Ende: <Datum>
VIII. Freifrist § 18 Abs. 4               Ende: <Datum>
IX.   BR-Anhörung § 102 BetrVG            [🟢 gesondert erfolgt / 🔴]

Offene Verifizierungen:
  - Fehlerstufe bestimmen (Konsultation / fehlende Anzeige / Inhaltsfehler) und Fundstellen in juris abgleichen
Empfehlung: <…>
```

## Risiken / typische Fehler

- **§ 17 Abs. 2 KSchG mit § 102 BetrVG verwechselt** — Konsultationsverfahren und Kündigungsanhörung sind zwei eigenständige Verfahren mit eigenen Fehlerfolgen. Eine kombinierte Unterrichtung ist zulässig, muss dann aber beide Anforderungen erfüllen und beides ausdrücklich benennen.
- **Aufhebungsverträge nicht mitgezählt** — § 17 Abs. 1 S. 2 KSchG erfasst alle vom Arbeitgeber veranlassten Beendigungen; die Schwelle wird dadurch häufig unbemerkt überschritten.
- **„Entlassung" als Beendigungszeitpunkt verstanden** statt als Kündigungsausspruch — der 30-Tage-Zeitraum wird dann falsch abgegrenzt.
- **Kündigung vor Abschluss des Konsultationsverfahrens** ausgesprochen — führt zur Unwirksamkeit; der Abschluss muss dokumentiert sein.
- **Abschrift nach § 17 Abs. 3 S. 1 KSchG vergessen** — sie ist **gleichzeitig** mit der BR-Unterrichtung zu übersenden, nicht erst mit der Anzeige.
- **Betriebsbegriff nach § 1 BetrVG bestimmt** statt unionsrechtlich autonom — bei mehreren Standorten kippt dadurch die Schwellenberechnung.
- **Freifrist § 18 Abs. 4 KSchG verstreichen lassen** — nach 90 Tagen ist erneut anzuzeigen; werden Kündigungen gestaffelt ausgesprochen, wird das leicht übersehen.
- **Auf die Entlastungslinie von 2024 vertraut** — sie ist überholt; entlastet sind nach BAG vom 25.06.2026 nur Inhaltsfehler, die die Agentur nicht an ihrer Aufgabe hindern. Konsultationsverfahren, Reihenfolge und die Anzeige als solche bleiben voll sanktioniert.
- **Inhaltsfehler der Anzeige ohne Prüfung der Aufgabenrelevanz für unschädlich erklärt** — fehlende Muss-Angaben hindern die Agentur regelmäßig an ihrer Aufgabe.
- **Örtlich unzuständige Agentur für Arbeit** adressiert — maßgeblich ist die Agentur am Sitz des Betriebs, nicht am Sitz der Konzernzentrale.
