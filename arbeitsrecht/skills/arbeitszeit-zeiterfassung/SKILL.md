---
name: arbeitszeit-zeiterfassung
description: "Arbeitszeitrecht und Pflicht zur Arbeitszeiterfassung – Höchstarbeitszeit und Ausgleichszeitraum § 3 ArbZG, Ruhepausen § 4 ArbZG, Ruhezeit § 5 ArbZG, Nachtarbeit § 6 ArbZG, tarifliche Abweichungen § 7 ArbZG, Sonn- und Feiertagsruhe §§ 9–11 ArbZG, Aufzeichnungspflicht § 16 Abs. 2 ArbZG, unionsrechtlich begründete Pflicht zur Erfassung der gesamten Arbeitszeit aus § 3 Abs. 2 Nr. 1 ArbSchG nach BAG 2022 und EuGH 2019, Mitbestimmung § 87 Abs. 1 Nr. 2, 3, 6 BetrVG, Überstundenprozess und Bußgelder § 22 ArbZG; Abgrenzung zum Referentenentwurf BMAS vom 18.06.2026. Use when ein Arbeitszeitmodell oder ein Zeiterfassungssystem geprüft, eingeführt oder ein Überstundenanspruch bewertet wird."
language: de
agents:
  researcher: ../../agents/researcher.md
  drafter: ../../agents/drafter.md
  reviewer: ../../agents/reviewer.md
provider_variants: [claude, gemini, openai]
test: ./test.md
---

# /arbeitsrecht:arbeitszeit-zeiterfassung

## Zweck

Die Pflicht, die **gesamte** Arbeitszeit zu erfassen, gilt in Deutschland bereits heute — nicht erst mit einer ArbZG-Reform. Sie folgt aus der unionsrechtskonformen Auslegung von § 3 Abs. 2 Nr. 1 ArbSchG, die das BAG im Jahr 2022 vorgenommen hat. Der Gesetzgeber hat sie bislang nicht ausgestaltet; ein Referentenentwurf des BMAS vom 18.06.2026 kursiert, ist aber **nicht beschlossen**. Dieser Skill trennt strikt das **geltende Recht** von der **geplanten Reform**, prüft Arbeitszeitmodelle gegen die Grenzen der §§ 3–6 ArbZG und gestaltet ein rechtssicheres Erfassungssystem samt Mitbestimmung.

> **Rechtsstand: Oktober 2026.** Das ArbZG ist seit 2024 inhaltlich unverändert. Alle Aussagen zum Referentenentwurf sind als `[unverifiziert – prüfen]` gekennzeichnet; der Primärtext lag bei Erstellung nicht vor.

## Eingaben

- Branche, Tarifbindung, Betriebsrat vorhanden?
- Arbeitszeitmodell: feste Zeiten, Gleitzeit, Vertrauensarbeitszeit, Schicht, Rufbereitschaft, Bereitschaftsdienst, mobiles Arbeiten
- Personenkreis: leitende Angestellte (§ 18 Abs. 1 Nr. 1 ArbZG), Chefärzte, Jugendliche (JArbSchG), Schwangere (MuSchG)
- Tatsächliche Arbeitszeiten (Stichprobe, Systemauswertung), Überschreitungen > 10 Stunden, Ruhezeitverstöße
- Vorhandenes Erfassungssystem (Papier, Excel, App, Terminal), Löschfristen, Zugriffsrechte
- Bei Streit: geltend gemachte Überstunden, Anordnung/Duldung durch den Arbeitgeber, Ausschlussfristen

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert ArbZG-, ArbSchG- und BetrVG-Normen mit URL, die RL 2003/88/EG, die Leitentscheidungen von EuGH und BAG sowie den aktuellen Stand des Gesetzgebungsverfahrens.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) erstellt Prüfvermerk, Betriebsvereinbarung „Arbeitszeiterfassung" oder Klageerwiderung im Überstundenprozess.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Höchstgrenzen, Ausgleichszeitraum, Mitbestimmung, Datenschutz und die saubere Trennung von geltendem Recht und Entwurf.

## Ablauf

### 1. Geltendes Recht: die Grenzen der §§ 3–6 ArbZG

- **Höchstarbeitszeit** ([§ 3 ArbZG](https://www.gesetze-im-internet.de/arbzg/__3.html)): werktäglich **acht Stunden**; Verlängerung auf **zehn Stunden**, wenn innerhalb von **sechs Kalendermonaten oder 24 Wochen** im Durchschnitt acht Stunden werktäglich nicht überschritten werden. Werktage sind Montag bis Samstag — rechnerisch also 48 Stunden pro Woche im Durchschnitt.
- **Ruhepausen** ([§ 4 ArbZG](https://www.gesetze-im-internet.de/arbzg/__4.html)): bei mehr als sechs bis neun Stunden **30 Minuten**, bei mehr als neun Stunden **45 Minuten**; aufteilbar in Abschnitte von mindestens 15 Minuten; nicht länger als sechs Stunden hintereinander ohne Pause.
- **Ruhezeit** ([§ 5 ArbZG](https://www.gesetze-im-internet.de/arbzg/__5.html)): nach Beendigung der täglichen Arbeitszeit **ununterbrochen elf Stunden**. Die abendliche E-Mail-Beantwortung kann die Ruhezeit unterbrechen; sie beginnt dann neu.
- **Nachtarbeit** ([§ 6 ArbZG](https://www.gesetze-im-internet.de/arbzg/__6.html)): Ausgleich innerhalb eines Kalendermonats oder vier Wochen, arbeitsmedizinische Untersuchung, angemessener Zuschlag oder freie Tage (§ 6 Abs. 5 ArbZG).
- **Abweichungen** ([§ 7 ArbZG](https://www.gesetze-im-internet.de/arbzg/__7.html)) nur durch **Tarifvertrag** oder aufgrund eines Tarifvertrags durch Betriebsvereinbarung; nicht tarifgebundene Arbeitgeber können abweichende Tarifregelungen nur im Geltungsbereich eines Tarifvertrags übernehmen (§ 7 Abs. 3 ArbZG).
- **Sonn- und Feiertage** ([§ 9 ArbZG](https://www.gesetze-im-internet.de/arbzg/__9.html), [§ 10 ArbZG](https://www.gesetze-im-internet.de/arbzg/__10.html), [§ 11 ArbZG](https://www.gesetze-im-internet.de/arbzg/__11.html)): Beschäftigungsverbot mit Ausnahmekatalog; mindestens 15 beschäftigungsfreie Sonntage im Jahr; Ersatzruhetag.
- **Persönlicher Anwendungsbereich** ([§ 18 ArbZG](https://www.gesetze-im-internet.de/arbzg/__18.html)): ausgenommen u. a. leitende Angestellte i. S. d. § 5 Abs. 3 BetrVG und Chefärzte.

### 2. Geltendes Recht: Pflicht zur Erfassung der gesamten Arbeitszeit

- **EuGH:** Die Mitgliedstaaten müssen Arbeitgeber verpflichten, ein **objektives, verlässliches und zugängliches System** zur Messung der täglichen Arbeitszeit einzurichten (EuGH, Urt. v. 14.05.2019 – C-55/18, *CCOO*, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2019-05-14&Aktenzeichen=C-55/18)).
- **BAG:** Diese Pflicht besteht in Deutschland bereits nach [§ 3 Abs. 2 Nr. 1 ArbSchG](https://www.gesetze-im-internet.de/arbschg/__3.html) in unionsrechtskonformer Auslegung; erfasst werden **Beginn, Ende und Dauer** der Arbeitszeit einschließlich Überstunden. Weil die Pflicht gesetzlich besteht, hat der Betriebsrat **kein Initiativrecht** für das „Ob" der Erfassung nach § 87 Abs. 1 Nr. 6 BetrVG (BAG, Beschl. v. 13.09.2022 – 1 ABR 22/21, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BAG&Datum=2022-09-13&Aktenzeichen=1%20ABR%2022/21)).
- **Form:** Eine **elektronische** Erfassung ist nach geltendem Recht **nicht** vorgeschrieben; Papier oder Tabellen genügen, wenn sie objektiv und verlässlich sind. Die Erfassung kann an Beschäftigte **delegiert** werden; die Verantwortung bleibt beim Arbeitgeber.
- **Vertrauensarbeitszeit** bleibt zulässig, soweit sie den Verzicht auf **Kontrolle der Lage** meint — nicht den Verzicht auf **Erfassung**.
- **Aufzeichnungspflicht** ([§ 16 Abs. 2 ArbZG](https://www.gesetze-im-internet.de/arbzg/__16.html)): Arbeitszeit über acht Stunden werktäglich ist aufzuzeichnen und **zwei Jahre** aufzubewahren. Daneben: § 17 MiLoG für Minijobber und Branchen nach § 2a SchwarzArbG (siehe `/arbeitsrecht:mindestlohn-minijob-aktivrente`).
- **Sanktionen:** Ein Bußgeld knüpft derzeit nur an die Verletzung von § 16 Abs. 2 ArbZG und der Höchstgrenzen an ([§ 22 ArbZG](https://www.gesetze-im-internet.de/arbzg/__22.html), bis 30.000 EUR); für die allgemeine Erfassungspflicht aus dem ArbSchG ist zunächst eine **Anordnung der Aufsichtsbehörde** ([§ 22 Abs. 3 ArbSchG](https://www.gesetze-im-internet.de/arbschg/__22.html)) erforderlich. Vorsätzliche, gesundheitsgefährdende Verstöße sind nach [§ 23 ArbZG](https://www.gesetze-im-internet.de/arbzg/__23.html) strafbar.

### 3. Geplantes Recht: Referentenentwurf BMAS vom 18.06.2026

Nur nach berichteten Inhalten, Primärtext nicht eingesehen, **kein Kabinettsbeschluss** (Stand Oktober 2026) `[unverifiziert – prüfen]`:

| Punkt | Berichteter Inhalt |
|---|---|
| Erfassung | elektronisch, am Tag der Arbeitsleistung (neuer § 16 ArbZG) |
| Übergang | gestaffelt 1, 2 oder 5 Jahre nach Betriebsgröße |
| Kleinbetriebe | bis 10 Beschäftigte dauerhaft von der elektronischen Form befreit |
| Höchstarbeitszeit | wöchentliche statt werktäglicher Höchstgrenze — nur durch oder aufgrund Tarifvertrag |
| Bußgeld | bis 30.000 EUR |

**Beratungsregel:** Systeme jetzt so auswählen, dass sie die elektronische Tageserfassung **bereits können**; Betriebsvereinbarungen mit einer Anpassungsklausel für das künftige Gesetz versehen. Nie den Entwurf als geltendes Recht darstellen.

### 4. Mitbestimmung ([§ 87 BetrVG](https://www.gesetze-im-internet.de/betrvg/__87.html))

- **§ 87 Abs. 1 Nr. 2 BetrVG** — Beginn und Ende der täglichen Arbeitszeit, Pausen, Verteilung auf Wochentage.
- **§ 87 Abs. 1 Nr. 3 BetrVG** — vorübergehende Verlängerung (Überstunden) oder Verkürzung.
- **§ 87 Abs. 1 Nr. 6 BetrVG** — technische Einrichtung zur Überwachung: Auswahl und Ausgestaltung des Systems sind mitbestimmt, das „Ob" der Erfassung nicht (BAG 2022, oben Nr. 2).
- Ohne Betriebsrat: Einführung per Weisung ([§ 106 GewO](https://www.gesetze-im-internet.de/gewo/__106.html)).
- **Datenschutz:** Rechtsgrundlage Art. 6 Abs. 1 lit. c DSGVO (rechtliche Verpflichtung) i. V. m. § 26 BDSG; Zweckbindung, Zugriffsrechte, Löschkonzept. GPS-Tracking oder Bildschirmüberwachung sind von der Erfassungspflicht **nicht** gedeckt.

### 5. Überstundenprozess

- Die Erfassungspflicht ändert die **Darlegungslast** im Vergütungsprozess nicht: Der Arbeitnehmer muss darlegen, dass er über die Normalarbeitszeit hinaus gearbeitet hat **und** dass der Arbeitgeber die Überstunden angeordnet, gebilligt oder geduldet hat (BAG, Urt. v. 04.05.2022 – 5 AZR 359/21, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BAG&Datum=2022-05-04&Aktenzeichen=5%20AZR%20359/21)).
- Ein vorhandenes Erfassungssystem verschiebt die Lage faktisch: Erfasste Zeiten, die der Arbeitgeber kennt und nicht beanstandet, begründen die **Duldung**.
- Pauschalabgeltungsklauseln („Überstunden sind mit dem Gehalt abgegolten") sind nur transparent, wenn der Umfang erkennbar ist (§ 307 Abs. 1 S. 2 BGB) — siehe `/arbeitsrecht:arbeitsvertrag-gestaltung`.
- Ausschlussfristen prüfen; der Mindestlohnanteil bleibt nach § 3 MiLoG unberührt.

### 6. Ergebnis

Ampelbefund je Modell (zulässig / anpassungsbedürftig / unzulässig), Maßnahmenplan mit Systemauswahl, Betriebsvereinbarung und Schulung.

## Quellen

### Statute

- [§ 3 ArbZG](https://www.gesetze-im-internet.de/arbzg/__3.html), [§ 4 ArbZG](https://www.gesetze-im-internet.de/arbzg/__4.html), [§ 5 ArbZG](https://www.gesetze-im-internet.de/arbzg/__5.html), [§ 6 ArbZG](https://www.gesetze-im-internet.de/arbzg/__6.html), [§ 7 ArbZG](https://www.gesetze-im-internet.de/arbzg/__7.html), [§ 16 ArbZG](https://www.gesetze-im-internet.de/arbzg/__16.html), [§ 18 ArbZG](https://www.gesetze-im-internet.de/arbzg/__18.html), [§ 22 ArbZG](https://www.gesetze-im-internet.de/arbzg/__22.html)
- [§ 3 ArbSchG](https://www.gesetze-im-internet.de/arbschg/__3.html), [§ 22 ArbSchG](https://www.gesetze-im-internet.de/arbschg/__22.html)
- [§ 87 BetrVG](https://www.gesetze-im-internet.de/betrvg/__87.html), [§ 106 GewO](https://www.gesetze-im-internet.de/gewo/__106.html), [§ 26 BDSG](https://www.gesetze-im-internet.de/bdsg_2018/__26.html)
- Richtlinie 2003/88/EG über bestimmte Aspekte der Arbeitszeitgestaltung, Art. 3, 5, 6, 31 Abs. 2 GRCh

### Gesetzgebung (nicht in Kraft)

- Referentenentwurf BMAS zur Änderung des Arbeitszeitgesetzes vom 18.06.2026 — kein Kabinettsbeschluss bekannt `[unverifiziert – prüfen]`

### Kommentare

- Wank, in: ErfK, 26. Aufl. 2026, § 3 ArbZG Rn. 1 ff. `[unverifiziert – prüfen]` (Auflage prüfen)
- Baeck / Deutsch / Winzer, ArbZG, 5. Aufl., § 16 Rn. 1 ff. `[unverifiziert – prüfen]`

### Rechtsprechung

- EuGH, Urt. v. 14.05.2019 – C-55/18, *CCOO* (Pflicht zu objektivem, verlässlichem, zugänglichem Erfassungssystem), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2019-05-14&Aktenzeichen=C-55/18)
- BAG, Beschl. v. 13.09.2022 – 1 ABR 22/21 (Erfassungspflicht aus § 3 Abs. 2 Nr. 1 ArbSchG; kein Initiativrecht des BR für das „Ob"), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BAG&Datum=2022-09-13&Aktenzeichen=1%20ABR%2022/21)
- BAG, Urt. v. 04.05.2022 – 5 AZR 359/21 (Darlegungslast im Überstundenprozess bleibt unberührt), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BAG&Datum=2022-05-04&Aktenzeichen=5%20AZR%20359/21)

## Ausgabeformat

```
ARBEITSZEIT UND ZEITERFASSUNG — <Mandat-ID> — <Datum>
Rechtsstand: Oktober 2026 (ArbZG unverändert; RefE 18.06.2026 nicht beschlossen)

Gesamtbefund: [🟢 konform / 🟡 Anpassungsbedarf / 🔴 Verstöße]

I.    Arbeitszeitmodell               <Modell, Personenkreis, Tarifbindung>
II.   Höchstarbeitszeit § 3 ArbZG     <max. Tageswerte, Ausgleichszeitraum>
III.  Ruhepausen § 4 / Ruhezeit § 5   <Befunde, Unterbrechungen durch Erreichbarkeit>
IV.   Nachtarbeit / Sonntag           <…>
V.    Erfassungspflicht (geltendes Recht)
      System:                         <Papier / Excel / elektronisch>
      Beginn, Ende, Dauer erfasst:    [ja / nein]
      Delegation / Kontrolle:         <…>
VI.   Mitbestimmung § 87 BetrVG       Nr. 2 / Nr. 3 / Nr. 6 — Stand BV: <…>
VII.  Datenschutz                     Rechtsgrundlage, Löschkonzept
VIII. Reform-Vorsorge (RefE 18.06.2026) [elektronikfähig ja/nein; Anpassungsklausel]
IX.   Überstundenrisiko               <Duldung, Pauschalabgeltung, Ausschlussfrist>
X.    Maßnahmenplan                   <Schritt — Verantwortlich — Termin>
```

## Beispiel (Gutachtenstil, verkürzt)

**Sachverhalt.** Softwareunternehmen, 140 Beschäftigte, Betriebsrat, keine Tarifbindung. „Vertrauensarbeitszeit" ohne Erfassung; in Release-Phasen elfstündige Tage, abends Ticketbearbeitung. Ein ausgeschiedener Entwickler verlangt Vergütung für 310 Überstunden.

**Frage 1: Besteht eine Erfassungspflicht?** Eine Pflicht zur Erfassung der gesamten Arbeitszeit könnte sich aus § 3 Abs. 2 Nr. 1 ArbSchG ergeben. Die Norm verpflichtet zu einer geeigneten Organisation des Arbeitsschutzes; in unionsrechtskonformer Auslegung (Art. 31 Abs. 2 GRCh, RL 2003/88/EG, EuGH *CCOO*) umfasst sie ein objektives, verlässliches und zugängliches Erfassungssystem. Das BAG hat dies 2022 bestätigt. Die Pflicht besteht also **bereits jetzt**; auf das künftige ArbZG zu warten, ist keine Option.

**Frage 2: Liegen Verstöße vor?** Elf Stunden überschreiten die Grenze des § 3 S. 2 ArbZG von zehn Stunden absolut, unabhängig vom Ausgleichszeitraum. Die abendliche Ticketbearbeitung unterbricht die Ruhezeit des § 5 Abs. 1 ArbZG; die elf Stunden beginnen neu. Beides ist bußgeldbewehrt (§ 22 ArbZG).

**Frage 3: Überstundenklage.** Der Kläger muss Arbeit über die Normalarbeitszeit hinaus und deren Veranlassung durch den Arbeitgeber darlegen (BAG 2022, oben Nr. 5). Die fehlende Erfassung kehrt die Darlegungslast nicht um, erschwert aber das substantiierte Bestreiten; Release-Pläne, Ticket-Zeitstempel und Kenntnis der Teamleitung sprechen für Duldung.

**Ergebnis.** Erfassungssystem unverzüglich mit dem Betriebsrat einführen (§ 87 Abs. 1 Nr. 6 BetrVG zum „Wie"), elektronikfähig für die geplante Reform; Höchstgrenzen und Ruhezeit organisatorisch sichern; Vergleichsbereitschaft im Überstundenprozess prüfen.

## Risiken / typische Fehler

- **Entwurf als geltendes Recht dargestellt** — die elektronische Tageserfassung und die Wochenhöchstarbeitszeit sind Stand Oktober 2026 **nicht** Gesetz.
- **Erfassungspflicht verneint, weil das ArbZG schweigt** — die Pflicht folgt bereits aus § 3 Abs. 2 Nr. 1 ArbSchG (BAG 2022, oben Nr. 2).
- **Vertrauensarbeitszeit als Verzicht auf Erfassung verstanden** — zulässig ist nur der Verzicht auf die Kontrolle der Lage.
- **Ausgleichszeitraum übersehen** — 10-Stunden-Tage sind nur bei Durchschnitt von acht Stunden in sechs Monaten oder 24 Wochen zulässig.
- **Ruhezeit durch Erreichbarkeit unterbrochen** — Arbeit am späten Abend lässt die elfstündige Ruhezeit neu beginnen.
- **Mitbestimmung beim System übergangen** — Auswahl und Ausgestaltung unterliegen § 87 Abs. 1 Nr. 6 BetrVG.
- **Überwachung über das Erforderliche hinaus** — GPS, Screenshots oder Leistungsprofile sind von der Erfassungspflicht nicht gedeckt.
- **Duldung von Überstunden unterschätzt** — erfasste und unbeanstandete Zeiten tragen den Vergütungsanspruch.
- **Leitende Angestellte falsch abgegrenzt** — § 18 ArbZG folgt dem engen Begriff des § 5 Abs. 3 BetrVG, nicht der Hierarchiebezeichnung.
