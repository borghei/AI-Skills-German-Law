---
name: betriebsratswahl-anfechtung
description: "Anfechtung und Nichtigkeit der Betriebsratswahl nach den regelmäßigen Wahlen 2026 – Wahlzeitraum § 13 BetrVG, Wahlberechtigung und Wählbarkeit §§ 7, 8 BetrVG, Betriebsratsgröße § 9 BetrVG, Wahlgrundsätze und vereinfachtes Verfahren §§ 14, 14a BetrVG, Geschlechterquote § 15 Abs. 2 BetrVG, Wahlvorstand §§ 16–18 BetrVG, Anfechtung § 19 BetrVG mit Zwei-Wochen-Frist ab Bekanntgabe des Wahlergebnisses und Einspruchserfordernis gegen die Wählerliste § 19 Abs. 3 BetrVG, Nichtigkeit bei grobem und offensichtlichem Verstoß, Beschlussverfahren §§ 2a, 80 ff. ArbGG, Vollmacht bei Anfechtung durch Vertreter (BAG 28.01.2026), Wahlschutz § 20 BetrVG und Sonderkündigungsschutz § 15 Abs. 3–3b KSchG. Use when eine Betriebsratswahl angefochten, verteidigt oder auf Nichtigkeit geprüft wird."
language: de
agents:
  researcher: ../../agents/researcher.md
  drafter: ../../agents/drafter.md
  reviewer: ../../agents/reviewer.md
provider_variants: [claude, gemini, openai]
test: ./test.md
---

# /arbeitsrecht:betriebsratswahl-anfechtung

## Zweck

Die regelmäßigen Betriebsratswahlen fanden vom 01.03. bis 31.05.2026 statt. Die zweiwöchigen Anfechtungsfristen sind damit für fast alle Betriebe abgelaufen; offen sind laufende Anfechtungsverfahren, Wahlen außerhalb des regelmäßigen Zeitraums und die **nicht fristgebundene Nichtigkeit**. Dieser Skill prüft Wahlfehler, trennt Anfechtbarkeit von Nichtigkeit, berechnet die Frist deterministisch und strukturiert das Beschlussverfahren.

> **Rechtsstand: Oktober 2026.** BetrVG und Wahlordnung seit dem Betriebsrätemodernisierungsgesetz 2021 unverändert; neu sind zwei Entscheidungen des 7. Senats vom 28.01.2026.

## Eingaben

- Datum der **Bekanntgabe des Wahlergebnisses** (Aushang nach der Wahlordnung) — Fristauslöser
- Betrieb, Zahl der in der Regel beschäftigten Arbeitnehmer, Leiharbeitnehmer, Betriebsteile, Gemeinschaftsbetrieb
- Wahlverfahren (normal / vereinfacht), Wahlausschreiben, Wählerliste, Einsprüche gegen die Wählerliste
- Konkreter Wahlfehler mit Belegen
- Anfechtende: drei Wahlberechtigte, Gewerkschaft oder Arbeitgeber; bei Vertretung: Vollmacht mit Datum

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert BetrVG- und ArbGG-Normen mit URL, die Wahlordnung und die Rspr. des 7. Senats.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) erstellt Anfechtungsantrag, Antragserwiderung oder Feststellungsantrag auf Nichtigkeit.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Frist, Anfechtungsbefugnis, Vollmacht und Kausalität.

## Ablauf

### 1. Rahmen der Wahl

- **Zeitraum** ([§ 13 BetrVG](https://www.gesetze-im-internet.de/betrvg/__13.html)): alle vier Jahre vom 1. März bis 31. Mai; außerhalb nur in den Fällen des § 13 Abs. 2 BetrVG.
- **Wahlberechtigung** ([§ 7 BetrVG](https://www.gesetze-im-internet.de/betrvg/__7.html)): ab **16 Jahren**; Leiharbeitnehmer bei Einsatz von mehr als drei Monaten.
- **Wählbarkeit** ([§ 8 BetrVG](https://www.gesetze-im-internet.de/betrvg/__8.html)): ab 18 Jahren, sechs Monate Betriebszugehörigkeit.
- **Größe** ([§ 9 BetrVG](https://www.gesetze-im-internet.de/betrvg/__9.html)): Staffel nach in der Regel beschäftigten Arbeitnehmern; Leiharbeitnehmer zählen mit.
- **Wahlverfahren** ([§ 14 BetrVG](https://www.gesetze-im-internet.de/betrvg/__14.html), [§ 14a BetrVG](https://www.gesetze-im-internet.de/betrvg/__14a.html)): geheim und unmittelbar; vereinfachtes Verfahren zwingend in Betrieben mit 5 bis 100 Wahlberechtigten, durch Vereinbarung bis 200.
- **Minderheitengeschlecht** ([§ 15 Abs. 2 BetrVG](https://www.gesetze-im-internet.de/betrvg/__15.html)): Mindestsitze entsprechend dem Anteil in der Belegschaft.
- **Wahlvorstand** ([§ 16 BetrVG](https://www.gesetze-im-internet.de/betrvg/__16.html), [§ 18 BetrVG](https://www.gesetze-im-internet.de/betrvg/__18.html)): Bestellung spätestens zehn Wochen vor Ablauf der Amtszeit; Zuordnung leitender Angestellter nach [§ 18a BetrVG](https://www.gesetze-im-internet.de/betrvg/__18a.html).

### 2. Anfechtung ([§ 19 BetrVG](https://www.gesetze-im-internet.de/betrvg/__19.html))

**Voraussetzungen (§ 19 Abs. 1 BetrVG):**

1. Verstoß gegen **wesentliche** Vorschriften über Wahlrecht, Wählbarkeit oder Wahlverfahren,
2. keine Berichtigung des Verstoßes vor Abschluss der Wahl,
3. **Kausalität:** Das Wahlergebnis konnte durch den Verstoß geändert oder beeinflusst werden — es genügt die hypothetische Möglichkeit.

**Typische wesentliche Fehler:** Verkennung des Betriebsbegriffs, falsche Betriebsratsgröße, Nichtberücksichtigung von Leiharbeitnehmern, fehlerhaftes Wahlausschreiben, Missachtung der Geschlechterquote, Verletzung des Wahlgeheimnisses bei der Briefwahl, fehlerhafte Stimmauszählung.

**Einschränkung seit 2021 (§ 19 Abs. 3 BetrVG):** Eine Anfechtung durch **Wahlberechtigte** wegen Unrichtigkeit der **Wählerliste** ist ausgeschlossen, wenn nicht zuvor **Einspruch** gegen die Wählerliste eingelegt wurde; für den Arbeitgeber gilt dies, soweit die Unrichtigkeit auf seinen Angaben beruht.

**Anfechtungsberechtigt** (§ 19 Abs. 2 BetrVG): mindestens **drei** Wahlberechtigte, eine im Betrieb vertretene **Gewerkschaft** oder der **Arbeitgeber**. Bei Anfechtung durch drei Arbeitnehmer müssen alle drei während des gesamten Verfahrens beteiligt bleiben `[unverifiziert – prüfen]`.

**Frist:** **zwei Wochen** ab dem Tag der Bekanntgabe des Wahlergebnisses (§ 19 Abs. 2 S. 2 BetrVG). Deterministisch rechnen:

```bash
python -m scripts.legal_calc.cli frist --ereignis 12.05.2026 --menge 2 --einheit wochen --land NW
# Fristbeginn 13.05.2026, Fristende 26.05.2026 (Dienstag)
```

**Vollmacht:** Wird die Anfechtung durch einen Vertreter ohne Vertretungsmacht eingelegt, kann sie nach Ablauf der Zwei-Wochen-Frist **nicht rückwirkend genehmigt** werden; der Nachweis einer **rechtzeitig erteilten** Vollmacht bleibt möglich (BAG, Beschl. v. 28.01.2026 – 7 ABR 26/24, [bundesarbeitsgericht.de](https://www.bundesarbeitsgericht.de/entscheidung/7-abr-26-24/)). Vollmachtsurkunde daher **vor** Einreichung datiert unterzeichnen lassen ([§ 80 ZPO](https://www.gesetze-im-internet.de/zpo/__80.html) i. V. m. § 46 Abs. 2, § 80 Abs. 2 ArbGG).

**Vollmacht im Original:** Wird die Anfechtung durch einen Bevollmächtigten eingereicht, muss die Vollmacht innerhalb der Anfechtungsfrist erteilt sein und auf Rüge **im Original** nachgewiesen werden; eine Kopie genügt nicht, eine nach Fristablauf datierte Vollmacht heilt nicht. Das BAG hat deshalb die Annahme einer rechtzeitigen Arbeitgeberanfechtung durch das LAG beanstandet und zurückverwiesen (BAG, Beschl. v. 28.01.2026 – 7 ABR 40/24, Plattformbetrieb, [bundesarbeitsgericht.de](https://www.bundesarbeitsgericht.de/entscheidung/7-abr-40-24/)).

### 3. Nichtigkeit

- Nur bei **grobem und offensichtlichem** Verstoß gegen allgemeine Wahlgrundsätze, sodass nicht einmal der Anschein einer dem Gesetz entsprechenden Wahl besteht (z. B. Wahl ohne Wahlvorstand, offene Abstimmung per Handzeichen in einer Versammlung, Wahl in einem nicht betriebsratsfähigen Betrieb) `[unverifiziert – prüfen]`.
- **Keine Frist**; Geltendmachung jederzeit, auch inzident (z. B. im Kündigungsschutzprozess bei § 102 BetrVG).
- Eine Häufung von Anfechtungsgründen begründet für sich keine Nichtigkeit.

### 4. Verfahren und Rechtsfolgen

- **Beschlussverfahren** ([§ 2a ArbGG](https://www.gesetze-im-internet.de/arbgg/__2a.html), [§ 80 ArbGG](https://www.gesetze-im-internet.de/arbgg/__80.html) ff.) vor dem Arbeitsgericht; Amtsermittlung im Rahmen des Vortrags; Beteiligte: Betriebsrat, Arbeitgeber, Anfechtende, ggf. Gewerkschaft.
- **Anfechtung wirkt ex nunc:** Der Betriebsrat bleibt bis zur Rechtskraft im Amt; seine Beschlüsse und Beteiligungen bleiben wirksam.
- Ist nur die Sitzverteilung fehlerhaft, kann das Gericht das Ergebnis **berichtigen**, statt die Wahl für unwirksam zu erklären.
- **Nichtigkeit wirkt ex tunc:** Es hat nie ein Betriebsrat bestanden — Anhörungen nach § 102 BetrVG gehen ins Leere, Betriebsvereinbarungen sind unwirksam.
- Nach rechtskräftiger Anfechtung: Neuwahl außerhalb des regelmäßigen Zeitraums (§ 13 Abs. 2 Nr. 4 BetrVG).

### 5. Wahlschutz und Sonderkündigungsschutz

- **Wahlbehinderung und -beeinflussung** verboten ([§ 20 BetrVG](https://www.gesetze-im-internet.de/betrvg/__20.html)); Kosten trägt der Arbeitgeber; strafbar nach [§ 119 BetrVG](https://www.gesetze-im-internet.de/betrvg/__119.html).
- **Kündigungsschutz** ([§ 15 KSchG](https://www.gesetze-im-internet.de/kschg/__15.html)): Wahlvorstand und Wahlbewerber (Abs. 3) bis sechs Monate nach Bekanntgabe des Ergebnisses; einladende bzw. antragstellende Arbeitnehmer (Abs. 3a); Vorfeld-Initiatoren mit öffentlich beglaubigter Erklärung (Abs. 3b, nur gegen verhaltens- und personenbedingte Kündigungen). Für Mitglieder des Wahlvorstands und Wahlbewerber bedarf die außerordentliche Kündigung der Zustimmung nach [§ 103 BetrVG](https://www.gesetze-im-internet.de/betrvg/__103.html); für einladende und antragstellende Arbeitnehmer (Abs. 3a) und Vorfeld-Initiatoren (Abs. 3b) gilt § 103 BetrVG **nicht** — dort genügt für die außerordentliche Kündigung der wichtige Grund.

## Quellen

### Statute

- [§ 7 BetrVG](https://www.gesetze-im-internet.de/betrvg/__7.html), [§ 8 BetrVG](https://www.gesetze-im-internet.de/betrvg/__8.html), [§ 9 BetrVG](https://www.gesetze-im-internet.de/betrvg/__9.html), [§ 13 BetrVG](https://www.gesetze-im-internet.de/betrvg/__13.html), [§ 14 BetrVG](https://www.gesetze-im-internet.de/betrvg/__14.html), [§ 14a BetrVG](https://www.gesetze-im-internet.de/betrvg/__14a.html), [§ 15 BetrVG](https://www.gesetze-im-internet.de/betrvg/__15.html), [§ 16 BetrVG](https://www.gesetze-im-internet.de/betrvg/__16.html), [§ 18 BetrVG](https://www.gesetze-im-internet.de/betrvg/__18.html), [§ 18a BetrVG](https://www.gesetze-im-internet.de/betrvg/__18a.html), [§ 19 BetrVG](https://www.gesetze-im-internet.de/betrvg/__19.html), [§ 20 BetrVG](https://www.gesetze-im-internet.de/betrvg/__20.html), [§ 103 BetrVG](https://www.gesetze-im-internet.de/betrvg/__103.html), [§ 119 BetrVG](https://www.gesetze-im-internet.de/betrvg/__119.html)
- Erste Verordnung zur Durchführung des Betriebsverfassungsgesetzes (Wahlordnung), [gesetze-im-internet.de/betrvgdv1wo](https://www.gesetze-im-internet.de/betrvgdv1wo/index.html)
- [§ 15 KSchG](https://www.gesetze-im-internet.de/kschg/__15.html), [§ 2a ArbGG](https://www.gesetze-im-internet.de/arbgg/__2a.html), [§ 80 ArbGG](https://www.gesetze-im-internet.de/arbgg/__80.html), [§ 80 ZPO](https://www.gesetze-im-internet.de/zpo/__80.html)

### Kommentare

- Koch, in: ErfK, 26. Aufl. 2026, § 19 BetrVG Rn. 1 ff. `[unverifiziert – prüfen]` (Auflage prüfen)
- Fitting, BetrVG, 33. Aufl., § 19 Rn. 1 ff. `[unverifiziert – prüfen]`

### Rechtsprechung

- BAG, Beschl. v. 28.01.2026 – 7 ABR 26/24 (keine rückwirkende Genehmigung einer vollmachtlosen Anfechtung nach Fristablauf), [bundesarbeitsgericht.de](https://www.bundesarbeitsgericht.de/entscheidung/7-abr-26-24/)
- BAG, Beschl. v. 28.01.2026 – 7 ABR 40/24 (Arbeitgeberanfechtung durch Bevollmächtigten: Vollmacht im Original, rechtzeitige Bevollmächtigung; Zurückverweisung), [bundesarbeitsgericht.de](https://www.bundesarbeitsgericht.de/entscheidung/7-abr-40-24/)

## Ausgabeformat

```
BETRIEBSRATSWAHL — ANFECHTUNG / NICHTIGKEIT — <Betrieb> — <Datum>
Rechtsstand: Oktober 2026

I.    Wahl                            Datum <…>; Verfahren [normal / vereinfacht]
      Bekanntgabe Wahlergebnis:       <Datum>
II.   Anfechtungsfrist § 19 Abs. 2 BetrVG
      Fristende (Rechner):            <Datum> [offen / abgelaufen]
III.  Anfechtungsbefugnis             [3 Wahlberechtigte / Gewerkschaft / AG]
      Vollmacht (BAG 28.01.2026):        [vor Einreichung erteilt ✓ / ✗]
IV.   Wahlfehler
      Fehler | Norm | wesentlich? | berichtigt? | Kausalität
      <…>
      Einspruch gegen Wählerliste (§ 19 Abs. 3): [erfolgt / nicht erfolgt]
V.    Nichtigkeit                     [grob + offensichtlich? → ja / nein]
VI.   Rechtsfolge                     [ex nunc / Berichtigung / ex tunc]
VII.  Folgen für laufende Maßnahmen   <§ 102-Anhörungen, BV, Kündigungsschutz § 15 KSchG>
VIII. Antrag / Empfehlung
```

## Beispiel (Gutachtenstil, verkürzt)

**Sachverhalt.** 230 Arbeitnehmer und 40 Leiharbeitnehmer (Einsatz jeweils über sechs Monate); gewählt wurde ein siebenköpfiger Betriebsrat. Aushang des Wahlergebnisses am 12.05.2026; Anfechtung durch einen Anwalt für drei Arbeitnehmer am 26.05.2026, Vollmachten erst im Juni unterschrieben.

**Frage 1: Liegt ein Anfechtungsgrund vor?** Leiharbeitnehmer zählen bei der Betriebsratsgröße nach § 9 BetrVG mit. Bei 270 Arbeitnehmern sind neun Mitglieder zu wählen, nicht sieben. Die Verkennung der Betriebsratsgröße ist ein Verstoß gegen eine wesentliche Wahlvorschrift, der das Ergebnis beeinflusst hat. Ein Anfechtungsgrund nach § 19 Abs. 1 BetrVG liegt vor. § 19 Abs. 3 BetrVG steht nicht entgegen, weil die Größe keine Frage der Wählerliste ist.

**Frage 2: Ist die Anfechtung fristgerecht?** Die Zwei-Wochen-Frist endete am 26.05.2026 (Rechner). Die Antragsschrift ging rechtzeitig ein, aber der Anwalt hatte zu diesem Zeitpunkt keine Vollmacht. Eine rückwirkende Genehmigung nach Fristablauf ist ausgeschlossen (BAG vom 28.01.2026, oben Nr. 2). Die Anfechtung ist unzulässig.

**Frage 3: Nichtigkeit?** Eine falsche Betriebsratsgröße ist kein grober und offensichtlicher Verstoß. Die Wahl ist nicht nichtig.

**Ergebnis.** Der Betriebsrat bleibt im Amt; die Fehlbesetzung kann erst bei der nächsten Wahl korrigiert werden.

## Risiken / typische Fehler

- **Anfechtungsfrist ab Wahltag statt ab Bekanntgabe gerechnet** — maßgeblich ist der Tag der Bekanntgabe des Wahlergebnisses.
- **Vollmacht nachgereicht und rückwirkend genehmigt** — nach BAG vom 28.01.2026 (oben Nr. 2) ausgeschlossen; nur eine rechtzeitig erteilte Vollmacht trägt.
- **Fehler in der Wählerliste ohne vorherigen Einspruch gerügt** — § 19 Abs. 3 BetrVG schließt die Anfechtung insoweit aus.
- **Anfechtbarkeit mit Nichtigkeit verwechselt** — nach Fristablauf hilft nur ein grober und offensichtlicher Verstoß.
- **Ex-nunc-Wirkung übersehen** — bis zur Rechtskraft bleibt der Betriebsrat im Amt; Anhörungen sind an ihn zu richten.
- **Kausalität nicht dargelegt** — der Verstoß muss das Ergebnis zumindest beeinflussen können.
- **Sonderkündigungsschutz der Wahlbewerber übersehen** — sechs Monate Nachwirkung nach Bekanntgabe des Ergebnisses.
