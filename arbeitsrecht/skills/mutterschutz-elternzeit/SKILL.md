---
name: mutterschutz-elternzeit
description: "Mutterschutz und Elternzeit im Arbeitsverhältnis – Schutzfristen § 3 MuSchG einschließlich der seit 01.06.2025 geltenden gestaffelten Schutzfristen nach Fehlgeburt ab der 13. Schwangerschaftswoche (§ 3 Abs. 5 MuSchG), Gefährdungsbeurteilung und Beschäftigungsverbote §§ 10–16 MuSchG, Mutterschutzlohn und Zuschuss §§ 18–20 MuSchG, Kündigungsverbot § 17 MuSchG mit Zwei-Wochen-Mitteilungsfrist und Zulässigkeitserklärung, nachträgliche Klagezulassung § 5 Abs. 1 S. 2 KSchG und § 4 S. 4 KSchG (BAG 03.04.2025), Elternzeitverlangen in Textform § 16 BEEG (Schriftform nur noch für vor dem 01.05.2025 geborene Kinder, § 28 Abs. 1b BEEG), Teilzeit in Elternzeit § 15 Abs. 4–7 BEEG, Sonderkündigungsschutz § 18 BEEG, Urlaubskürzung § 17 BEEG. Use when eine Schwangerschaft, Fehlgeburt oder Elternzeit Auswirkungen auf Beschäftigung, Vergütung oder eine Kündigung hat."
language: de
agents:
  researcher: ../../agents/researcher.md
  drafter: ../../agents/drafter.md
  reviewer: ../../agents/reviewer.md
provider_variants: [claude, gemini, openai]
test: ./test.md
---

# /arbeitsrecht:mutterschutz-elternzeit

## Zweck

Mutterschutz und Elternzeit erzeugen die strengsten Kündigungsverbote des deutschen Arbeitsrechts und eine Reihe von Fristen, die auf beiden Seiten versäumt werden: die Zwei-Wochen-Mitteilung nach § 17 MuSchG, die Sieben- bzw. Dreizehn-Wochen-Anmeldung der Elternzeit, die Ablehnungsfristen beim Teilzeitantrag. Seit dem 01.06.2025 gelten zudem **Schutzfristen nach einer Fehlgeburt**. Dieser Skill prüft Beschäftigung, Vergütung und Bestandsschutz in einem Durchgang.

> **Rechtsstand: Oktober 2026.** § 3 Abs. 5 MuSchG gilt seit 01.06.2025. Eine Elterngeldreform ist nur als Referentenentwurf berichtet (`[unverifiziert – prüfen]`) und nicht in Kraft.

## Eingaben

- Datum der Mitteilung der Schwangerschaft, voraussichtlicher Entbindungstermin, tatsächliches Entbindungsdatum, Frühgeburt / Mehrlinge / Behinderung des Kindes
- Bei Fehlgeburt: Schwangerschaftswoche (13., 17., 20. SSW maßgeblich)
- Tätigkeit und Gefährdungsbeurteilung; ärztliches Beschäftigungsverbot?
- Kündigung: Datum des Zugangs, Kenntnis des Arbeitgebers, Datum der ärztlichen Feststellung der Schwangerschaft
- Elternzeit: Geburtsdatum des Kindes, Verlangen (Datum, Form, Zeiträume), Teilzeitwunsch (Stunden, Verteilung), Betriebsgröße, Beschäftigungsdauer

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert MuSchG-, BEEG- und KSchG-Normen mit URL und die BAG-Linien zu Mitteilung, Klagefrist und Form des Elternzeitverlangens.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) erstellt Elternzeitverlangen, Ablehnung oder Zustimmung zum Teilzeitantrag, Antrag auf Zulässigkeitserklärung oder Klageschrift mit Antrag auf nachträgliche Zulassung.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Fristen, Form, Kenntnisstand und behördliche Zustimmung.

## Ablauf

### 1. Schutzfristen ([§ 3 MuSchG](https://www.gesetze-im-internet.de/muschg_2018/__3.html))

| Lage | Schutzfrist |
|---|---|
| Vor der Entbindung | sechs Wochen; Beschäftigung nur bei ausdrücklicher, jederzeit widerruflicher Erklärung (§ 3 Abs. 1 MuSchG) |
| Nach der Entbindung | acht Wochen, **absolutes** Beschäftigungsverbot (§ 3 Abs. 2 MuSchG) |
| Früh-, Mehrlingsgeburt, Behinderung des Kindes | zwölf Wochen (Behinderung auf Antrag) |
| **Fehlgeburt ab der 13. SSW** (seit 01.06.2025) | **zwei Wochen** |
| **Fehlgeburt ab der 17. SSW** | **sechs Wochen** |
| **Fehlgeburt ab der 20. SSW** | **acht Wochen** |

Bei der Fehlgeburt (§ 3 Abs. 5 MuSchG) darf die Frau beschäftigt werden, wenn sie sich **ausdrücklich** dazu bereit erklärt; die Erklärung ist jederzeit widerruflich. Mutterschaftsleistungen (Mutterschaftsgeld, Zuschuss) laufen während der Schutzfrist.

### 2. Gefährdungsbeurteilung und Beschäftigungsverbote

- Anlassunabhängige Gefährdungsbeurteilung für jeden Arbeitsplatz und anlassbezogene Konkretisierung nach Mitteilung ([§ 10 MuSchG](https://www.gesetze-im-internet.de/muschg_2018/__10.html)); Mitteilung an die Aufsichtsbehörde ([§ 27 MuSchG](https://www.gesetze-im-internet.de/muschg_2018/__27.html)).
- Rangfolge der Schutzmaßnahmen ([§ 13 MuSchG](https://www.gesetze-im-internet.de/muschg_2018/__13.html)): Umgestaltung → Umsetzung → betriebliches Beschäftigungsverbot.
- **Ärztliches Beschäftigungsverbot** ([§ 16 MuSchG](https://www.gesetze-im-internet.de/muschg_2018/__16.html)) — abzugrenzen von der krankheitsbedingten Arbeitsunfähigkeit, für die das EFZG gilt.
- **Mutterschutzlohn** ([§ 18 MuSchG](https://www.gesetze-im-internet.de/muschg_2018/__18.html)): Durchschnittsentgelt der letzten drei Monate; Erstattung über die **U2-Umlage** (AAG) zu 100 %.
- **Mutterschaftsgeld und Zuschuss** ([§ 19 MuSchG](https://www.gesetze-im-internet.de/muschg_2018/__19.html), [§ 20 MuSchG](https://www.gesetze-im-internet.de/muschg_2018/__20.html)).

### 3. Kündigungsverbot ([§ 17 MuSchG](https://www.gesetze-im-internet.de/muschg_2018/__17.html))

Unzulässig ist die Kündigung

- während der Schwangerschaft,
- bis zum Ablauf von **vier Monaten nach einer Fehlgeburt nach der zwölften Schwangerschaftswoche**,
- bis zum Ende der Schutzfrist nach der Entbindung, mindestens aber bis **vier Monate nach der Entbindung**,

wenn dem Arbeitgeber die Schwangerschaft, Fehlgeburt oder Entbindung bekannt war oder **innerhalb von zwei Wochen** nach Zugang der Kündigung mitgeteilt wird. Das Überschreiten der Frist ist unschädlich, wenn es auf einem von der Frau nicht zu vertretenden Grund beruht und die Mitteilung unverzüglich nachgeholt wird. Erfasst sind auch **Vorbereitungsmaßnahmen** (z. B. Stellenausschreibung für die Nachfolge).

**Ausnahme:** Zulässigkeitserklärung der zuständigen Landesbehörde in besonderen, nicht mit der Schwangerschaft zusammenhängenden Fällen; die Kündigung bedarf dann der **Schriftform** und muss den Kündigungsgrund angeben (§ 17 Abs. 2 MuSchG).

### 4. Klagefrist und nachträgliche Zulassung

- Die Drei-Wochen-Frist des § 4 S. 1 KSchG gilt auch für die Geltendmachung des § 17 MuSchG.
- [§ 4 S. 4 KSchG](https://www.gesetze-im-internet.de/kschg/__4.html) (Fristbeginn erst mit Bekanntgabe der behördlichen Entscheidung) greift nur, wenn der Arbeitgeber bei Zugang **Kenntnis** von der Schwangerschaft hatte.
- Erfährt die Arbeitnehmerin **ohne Verschulden** erst nach Ablauf der drei Wochen von der Schwangerschaft, ist die Klage nachträglich zuzulassen ([§ 5 Abs. 1 S. 2 KSchG](https://www.gesetze-im-internet.de/kschg/__5.html)). Maßgeblich ist die **ärztliche Feststellung**, nicht ein positiver Selbsttest (BAG, Urt. v. 03.04.2025 – 2 AZR 156/24, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BAG&Datum=2025-04-03&Aktenzeichen=2%20AZR%20156/24)).
- Fristberechnung deterministisch: `python -m scripts.legal_calc.cli frist --ereignis <Zugang> --menge 3 --einheit wochen --land <BL>`; für die Zwei-Wochen-Mitteilung entsprechend `--menge 2`.

### 5. Elternzeit — Verlangen ([§ 15 BEEG](https://www.gesetze-im-internet.de/beeg/__15.html), [§ 16 BEEG](https://www.gesetze-im-internet.de/beeg/__16.html))

- Anspruch bis zur Vollendung des **dritten** Lebensjahres; bis zu **24 Monate** sind zwischen dem dritten und achten Geburtstag übertragbar.
- **Anmeldefrist:** **sieben Wochen** vor Beginn (Zeitraum bis zum 3. Geburtstag), **13 Wochen** vor Beginn (Zeitraum zwischen 3. und 8. Geburtstag).
- **Form:** **Textform** (§ 126b BGB; § 16 Abs. 1 S. 1 BEEG i. d. F. des BEG IV) — E-Mail genügt. Das gilt für Kinder, die **ab dem 01.05.2025** geboren oder zur Adoption aufgenommen wurden. Für **vorher** geborene Kinder bleibt es bei der **Schriftform** des § 126 BGB (§ 28 Abs. 1b BEEG); dort genügen Telefax oder E-Mail nicht (BAG, Urt. v. 10.05.2016 – 9 AZR 145/15 `[unverifiziert – prüfen]`). **Erst das Geburtsdatum klären, dann die Form prüfen.** Die Erklärung bindet für die ersten **zwei Jahre**.
- Der Arbeitgeber soll die Elternzeit bescheinigen (§ 16 Abs. 1 S. 8 BEEG); Zustimmung ist nicht erforderlich.

### 6. Teilzeit in Elternzeit (§ 15 Abs. 4–7 BEEG)

- Zulässig bis **32 Wochenstunden** im Monatsdurchschnitt.
- **Anspruch** bei mehr als 15 Arbeitnehmern, mehr als sechs Monaten Bestand, mindestens zwei Monaten Dauer, 15–32 Stunden und ohne entgegenstehende **dringende betriebliche Gründe** (§ 15 Abs. 7 BEEG).
- **Ablehnung** mit Begründung in **Textform** (§ 15 Abs. 7 BEEG; Altfälle vor dem 01.05.2025: Schriftform) innerhalb von **vier Wochen** (Zeitraum bis zum 3. Geburtstag) bzw. **acht Wochen** (danach); sonst gilt die Zustimmung als erteilt (**Zustimmungsfiktion**, § 15 Abs. 7 BEEG).

### 7. Sonderkündigungsschutz ([§ 18 BEEG](https://www.gesetze-im-internet.de/beeg/__18.html)) und Urlaub ([§ 17 BEEG](https://www.gesetze-im-internet.de/beeg/__17.html))

- Kündigungsverbot ab dem Verlangen, frühestens **acht Wochen** vor Beginn (bis 3. Geburtstag) bzw. **14 Wochen** vor Beginn (danach), und während der Elternzeit; Ausnahme nur durch Zulässigkeitserklärung der Behörde.
- Urlaubskürzung um ein Zwölftel je vollen Monat Elternzeit nur durch **ausdrückliche Erklärung** im bestehenden Arbeitsverhältnis — nicht bei Teilzeit in Elternzeit beim selben Arbeitgeber.

### 8. Elterngeld — Hinweis

Elterngeld ist Sozialleistung (Elterngeldstelle), nicht Arbeitgeberleistung. Für Geburten ab 01.04.2025 gilt eine Einkommensgrenze von 175.000 EUR zu versteuerndem Einkommen ([§ 1 BEEG](https://www.gesetze-im-internet.de/beeg/__1.html)). Ein Referentenentwurf (berichtet Juli 2026) zur Kürzung der Bezugsdauer ist **nicht** in Kraft `[unverifiziert – prüfen]`.

## Quellen

### Statute

- [§ 3 MuSchG](https://www.gesetze-im-internet.de/muschg_2018/__3.html), [§ 10 MuSchG](https://www.gesetze-im-internet.de/muschg_2018/__10.html), [§ 13 MuSchG](https://www.gesetze-im-internet.de/muschg_2018/__13.html), [§ 16 MuSchG](https://www.gesetze-im-internet.de/muschg_2018/__16.html), [§ 17 MuSchG](https://www.gesetze-im-internet.de/muschg_2018/__17.html), [§ 18 MuSchG](https://www.gesetze-im-internet.de/muschg_2018/__18.html), [§ 19 MuSchG](https://www.gesetze-im-internet.de/muschg_2018/__19.html), [§ 20 MuSchG](https://www.gesetze-im-internet.de/muschg_2018/__20.html)
- Mutterschutzanpassungsgesetz v. 24.02.2025, BGBl. 2025 I Nr. 59 (Schutzfristen nach Fehlgeburt, in Kraft 01.06.2025)
- [§ 1 BEEG](https://www.gesetze-im-internet.de/beeg/__1.html), [§ 15 BEEG](https://www.gesetze-im-internet.de/beeg/__15.html), [§ 16 BEEG](https://www.gesetze-im-internet.de/beeg/__16.html), [§ 17 BEEG](https://www.gesetze-im-internet.de/beeg/__17.html), [§ 18 BEEG](https://www.gesetze-im-internet.de/beeg/__18.html)
- [§ 4 KSchG](https://www.gesetze-im-internet.de/kschg/__4.html), [§ 5 KSchG](https://www.gesetze-im-internet.de/kschg/__5.html)

### Kommentare

- Schlachter, in: ErfK, 26. Aufl. 2026, § 17 MuSchG Rn. 1 ff. `[unverifiziert – prüfen]` (Auflage prüfen)
- Gallner, in: ErfK, 26. Aufl. 2026, § 15 BEEG Rn. 1 ff. `[unverifiziert – prüfen]`

### Rechtsprechung

- BAG, Urt. v. 03.04.2025 – 2 AZR 156/24 (nachträgliche Zulassung; ärztliche Feststellung maßgeblich; § 4 S. 4 KSchG nur bei Kenntnis des Arbeitgebers), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BAG&Datum=2025-04-03&Aktenzeichen=2%20AZR%20156/24)
- BAG, Urt. v. 10.05.2016 – 9 AZR 145/15 (Schriftform des Elternzeitverlangens — nur noch für vor dem 01.05.2025 geborene Kinder) `[unverifiziert – prüfen]`

## Ausgabeformat

```
MUTTERSCHUTZ / ELTERNZEIT — <Mandat-ID> — <Datum>
Rechtsstand: Oktober 2026

I.    Schutzfristen § 3 MuSchG        <Beginn — Ende; Fehlgeburt SSW <N> → <Wochen>>
II.   Beschäftigung                   Gefährdungsbeurteilung / Beschäftigungsverbot
      Vergütung:                      [Mutterschutzlohn § 18 / Zuschuss § 20 / EFZG]
III.  Kündigungsverbot § 17 MuSchG
      Kenntnis bei Zugang:            [ja / nein]
      Zwei-Wochen-Mitteilung:         <Fristende> [gewahrt / versäumt — Verschulden?]
      Zulässigkeitserklärung:         [beantragt / erteilt / fehlt]
IV.   Klagefrist
      § 4 S. 1 KSchG:                 <Fristende>
      § 4 S. 4 / § 5 Abs. 1 S. 2 KSchG: <…>
V.    Elternzeit §§ 15, 16 BEEG
      Verlangen (Datum, Form):         <Textform / Schriftform bei Geburt vor 01.05.2025>
      Anmeldefrist 7 / 13 Wochen:     [gewahrt / nicht gewahrt → Beginn <Datum>]
VI.   Teilzeit in Elternzeit          Antrag <Datum>; Ablehnungsfrist <Datum>
      Zustimmungsfiktion:             [droht / eingetreten / ausgeschlossen]
VII.  Sonderkündigungsschutz § 18 BEEG ab <Datum>
VIII. Urlaubskürzung § 17 BEEG        [erklärt / nicht erklärt]
IX.   Empfehlung
```

## Beispiel (Gutachtenstil, verkürzt)

**Sachverhalt.** Kündigung in der Probezeit, Zugang 07.09.2026. Positiver Selbsttest 15.09.2026, ärztliche Feststellung 24.09.2026, Mitteilung an den Arbeitgeber 25.09.2026.

**Frage 1: Kündigungsverbot nach § 17 MuSchG?** Die Kündigung einer Schwangeren ist unzulässig, wenn dem Arbeitgeber die Schwangerschaft bekannt war oder binnen zwei Wochen nach Zugang mitgeteilt wird. Die Zwei-Wochen-Frist endete am 21.09.2026 (Rechner). Die Mitteilung am 25.09.2026 ist verspätet. Das Überschreiten ist unschädlich, wenn es auf einem nicht zu vertretenden Grund beruht und die Mitteilung unverzüglich nachgeholt wird. Die Arbeitnehmerin hatte vor der ärztlichen Feststellung keine gesicherte Kenntnis; die Mitteilung am Folgetag ist unverzüglich. Das Kündigungsverbot greift; die Kündigung ist ohne Zulässigkeitserklärung unwirksam.

**Frage 2: Klagefrist.** Die Drei-Wochen-Frist des § 4 S. 1 KSchG endet am 28.09.2026. § 4 S. 4 KSchG hilft nicht, weil der Arbeitgeber bei Zugang nichts wusste. Eine nachträgliche Zulassung nach § 5 Abs. 1 S. 2 KSchG kommt **nicht** in Betracht: Sie setzt voraus, dass die Arbeitnehmerin erst **nach Ablauf** der Frist von der Schwangerschaft erfährt. Hier lag die ärztliche Feststellung am 24.09.2026 — vier Tage **vor** Fristende. Maßgeblich ist die ärztliche Feststellung, nicht der Selbsttest (BAG 03.04.2025, oben Nr. 4).

**Ergebnis.** Kündigungsschutzklage **spätestens am 28.09.2026** erheben; auf § 5 KSchG nicht verlassen. Hätte die Ärztin die Schwangerschaft erst nach dem 28.09.2026 festgestellt, wäre die Klage mit Antrag auf nachträgliche Zulassung binnen zwei Wochen nach Kenntnis zu erheben (§ 5 Abs. 3 KSchG), die ärztliche Bescheinigung als Glaubhaftmachungsmittel beigefügt.

## Risiken / typische Fehler

- **Schutzfrist nach Fehlgeburt übersehen** — seit 01.06.2025 gelten ab der 13. SSW gestaffelte Schutzfristen von zwei, sechs oder acht Wochen.
- **Zwei-Wochen-Mitteilung falsch berechnet** — die Frist beginnt mit Zugang der Kündigung; unverschuldete Überschreitung ist bei unverzüglicher Nachholung unschädlich.
- **Selbsttest statt ärztlicher Feststellung zugrunde gelegt** — für die nachträgliche Zulassung zählt die ärztliche Feststellung (BAG 03.04.2025, oben Nr. 4).
- **§ 4 S. 4 KSchG ohne Kenntnis des Arbeitgebers angewandt** — dann bleibt es bei der Drei-Wochen-Frist; nur § 5 KSchG hilft.
- **Kündigung ohne Zulässigkeitserklärung** — nichtig; die Erklärung muss vor Zugang vorliegen.
- **Elternzeit per E-Mail verlangt** — für ab dem 01.05.2025 geborene Kinder **wirksam** (Textform); nur bei früher geborenen Kindern ist die Schriftform verfehlt, und dann fehlt der Sonderkündigungsschutz des § 18 BEEG ab diesem Zeitpunkt. Geburtsdatum klären.
- **Kenntnis vor Fristende mit nachträglicher Zulassung verwechselt** — erfährt die Arbeitnehmerin noch innerhalb der drei Wochen von der Schwangerschaft, ist fristgerecht zu klagen; § 5 Abs. 1 S. 2 KSchG greift nur bei Kenntnis nach Fristablauf.
- **Ablehnungsfrist beim Teilzeitantrag versäumt** — die Zustimmungsfiktion tritt ein.
- **Beschäftigungsverbot und Arbeitsunfähigkeit verwechselt** — Mutterschutzlohn (U2) und Entgeltfortzahlung (U1) folgen unterschiedlichen Regeln.
- **Elterngeldreform als geltendes Recht behandelt** — der Entwurf ist nicht beschlossen.
