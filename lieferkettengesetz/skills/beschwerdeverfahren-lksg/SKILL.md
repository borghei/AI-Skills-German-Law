---
name: beschwerdeverfahren-lksg
description: "Einrichtung und Wirksamkeitsprüfung des Beschwerdeverfahrens nach § 8 LkSG – Verfahrensordnung, Zugänglichkeit, Vertraulichkeit und Schutz vor Benachteiligung sowie der anlassbezogene Bezug zu mittelbaren Zulieferern (§ 9 LkSG). Use when ein Beschwerdeverfahren aufgesetzt, überarbeitet oder auf seine Wirksamkeit geprüft werden soll."
language: de
provider_variants: [claude, gemini, openai]
test: ./test.md
---

# /lieferkettengesetz:beschwerdeverfahren-lksg

## Zweck

Das **Beschwerdeverfahren** (**§ 8 LkSG**) ist das Frühwarnsystem der Lieferkette: Es macht Risiken und Verletzungen sichtbar, die die Risikoanalyse nicht erfasst hat. Diese Skill richtet ein wirksames Verfahren ein und prüft es gegen die gesetzlichen **Wirksamkeitskriterien**. Eingehende Beschwerden über **mittelbare Zulieferer** begründen regelmäßig die „substantiierte Kenntnis" i. S. v. **§ 9 LkSG** und lösen vertiefte Prüfpflichten aus.

## Eingaben

- Bestehendes Hinweisgeber-/Beschwerdesystem (Schnittstelle HinSchG)
- Stakeholder-/Zuliefererstruktur, betroffene Sprachen und Regionen
- Risikoanalyse (priorisierte Risiken als Beschwerde-Schwerpunkte)
- Bisher eingegangene Beschwerden und ihre Bearbeitung

## Sub-Agent-Architektur

Ein **Design-Agent** entwirft die **Verfahrensordnung** und die Zugangswege (Kanäle, Sprachen, Niedrigschwelligkeit). Ein **Wirksamkeits-Agent** prüft das Verfahren gegen die Kriterien des § 8 LkSG (Zugänglichkeit, Vertraulichkeit, Schutz vor Benachteiligung, Unparteilichkeit). Ein **Eskalations-Agent** verknüpft eingehende Beschwerden mit der Risikoanalyse und prüft, ob eine Beschwerde substantiierte Kenntnis nach **§ 9 LkSG** auslöst. Ein **Dokumentations-Agent** sichert die Nachweise für die BAFA-Berichterstattung (§ 10 LkSG) und markiert offene Punkte mit `[unverifiziert - prüfen]`.

## Ablauf

### 1. Pflicht und Reichweite (§ 8 Abs. 1 LkSG)

- Einrichtung eines internen oder Beteiligung an einem externen **Beschwerdeverfahren**.
- Erfasst Hinweise auf menschenrechtliche/umweltbezogene Risiken und Pflichtverletzungen im **eigenen Geschäftsbereich** und entlang der **gesamten Lieferkette** (auch mittelbare Zulieferer).

### 2. Verfahrensordnung (§ 8 Abs. 2 LkSG)

- Schriftliche, öffentlich zugängliche **Verfahrensordnung** in verständlicher Sprache.
- Klarheit über Zuständigkeit, Ablauf, Fristen und Rückmeldung an die hinweisgebende Person.

### 3. Wirksamkeitskriterien (§ 8 Abs. 3, 4 LkSG)

Das Verfahren muss wirksam sein. Maßgebliche Kriterien:

- **Zugänglichkeit** — niedrigschwellig, in relevanten Sprachen, für potenziell Betroffene erreichbar.
- **Vertraulichkeit** — Wahrung der Identität, Schutz der Daten.
- **Schutz vor Benachteiligung/Bestrafung** wegen einer Beschwerde.
- **Unparteilichkeit** — die mit dem Verfahren betrauten Personen handeln unabhängig, sind nicht weisungsgebunden und zur Verschwiegenheit verpflichtet.

### 4. Bearbeitung und Abhilfe

- Eingangsbestätigung, Sachverhaltsaufklärung, Erörterung mit der hinweisgebenden Person.
- Verknüpfung mit Präventions-/Abhilfemaßnahmen (§§ 6, 7 LkSG).

### 5. Bezug zu mittelbaren Zulieferern (§ 9 LkSG)

- Eine substantiierte Beschwerde über einen **mittelbaren Zulieferer** begründet „substantiierte Kenntnis" nach **§ 9 Abs. 3 LkSG**.
- Folge: anlassbezogene Risikoanalyse, Präventionsmaßnahmen gegenüber dem Verursacher, ggf. Aktualisierung des Beschwerdeverfahrens.

### 6. Wirksamkeitsprüfung und Dokumentation

- Überprüfung der **Wirksamkeit** mindestens **jährlich** und anlassbezogen (§ 8 Abs. 5 i. V. m. § 4 Abs. 4 LkSG).
- Dokumentation für die interne Nachweisführung und die BAFA-Berichterstattung (§ 10 LkSG).

## Risiken / typische Fehler

- **Wirksamkeit nur behauptet** — die **Wirksamkeit** des Verfahrens ist nicht anhand der gesetzlichen Kriterien belegt; **BAFA** verlangt einen belastbaren Nachweis.
- **Zugänglichkeit zu hoch** — Verfahren nur intern/deutschsprachig; potenziell betroffene Beschäftigte bei **mittelbare Zulieferer** im Ausland erreichen es nicht.
- **Vertraulichkeit unzureichend** — fehlender Schutz vor Benachteiligung untergräbt die **Vertraulichkeit** und schreckt Hinweisgeber ab.
- **Substantiierte Kenntnis verkannt** — eingehende Beschwerde nicht als Auslöser des § 9 LkSG behandelt.
- **Keine Verzahnung mit HinSchG** — Doppelstrukturen statt eines integrierten Kanals.
- **Keine jährliche Überprüfung** — Wirksamkeitskontrolle unterbleibt.

## Quellen

### Statute

- [LkSG](https://www.gesetze-im-internet.de/lksg/) — Volltext
- [§ 8 LkSG](https://www.gesetze-im-internet.de/lksg/__8.html), [§ 9 LkSG](https://www.gesetze-im-internet.de/lksg/__9.html), [§ 3 LkSG](https://www.gesetze-im-internet.de/lksg/__3.html), [§ 10 LkSG](https://www.gesetze-im-internet.de/lksg/__10.html), [§ 24 LkSG](https://www.gesetze-im-internet.de/lksg/__24.html)
- [HinSchG](https://www.gesetze-im-internet.de/hinschg/) — Schnittstelle Hinweisgeberschutz

### BAFA / Sekundärliteratur

- [BAFA – Lieferkettengesetz](https://www.bafa.de/) — Handreichung Beschwerdeverfahren
- Grabosch, LkSG, 1. Aufl. 2023

## Ausgabeformat

```
BESCHWERDEVERFAHREN (LkSG) — <Unternehmen> — <Datum>

I.    Reichweite (§ 8 LkSG)
      Erfasste Risiken / Lieferkette: <…>
II.   Verfahrensordnung
      Kanäle / Sprachen / Zuständigkeit / Fristen: <…>
III.  Wirksamkeitskriterien
      Zugänglichkeit | Vertraulichkeit | Schutz vor Benachteiligung | Unparteilichkeit
IV.   Bearbeitungsprozess
      Eingang → Aufklärung → Abhilfe (§§ 6, 7 LkSG): <…>
V.    Bezug mittelbare Zulieferer (§ 9 LkSG)
      Substantiierte Kenntnis ausgelöst? [Ja/Nein]
VI.   Wirksamkeitsprüfung & Dokumentation (§ 10 LkSG)
      <… [unverifiziert - prüfen] soweit offen>

Restrisiko: <…>
Wiedervorlage: jährlich + anlassbezogen
```
