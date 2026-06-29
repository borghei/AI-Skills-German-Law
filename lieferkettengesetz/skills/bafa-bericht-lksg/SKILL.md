---
name: bafa-bericht-lksg
description: "Erfüllung der Dokumentationspflicht (§ 10 LkSG) und Berichtspflicht (§ 12 LkSG) sowie Vorbereitung auf die BAFA-Kontrolle und Anordnungen (§§ 14, 15 LkSG) und das Bußgeldrisiko (§ 24 LkSG), mit Ausblick auf die CSDDD-Schnittstelle. Use when ein Unternehmen seine Dokumentation/Berichterstattung an die BAFA aufsetzt oder sich auf eine behördliche Kontrolle oder ein Bußgeldverfahren vorbereitet."
language: de
provider_variants: [claude, gemini, openai]
test: ./test.md
---

# /lieferkettengesetz:bafa-bericht-lksg

## Zweck

Diese Skill bündelt die **Nachweis- und Durchsetzungsebene** des LkSG: die interne **Dokumentationspflicht** (**§ 10 LkSG**), die **Berichtspflicht** gegenüber dem BAFA (**§ 12 LkSG**), die behördliche Kontrolle und **Anordnungen** (**§§ 14, 15 LkSG**) sowie das **Bußgeld** (**§ 24 LkSG**). Sie ordnet die Pflichten dem aktuellen Rechtsstand zu und bereitet auf eine **BAFA**-Kontrolle vor.

> **⚠️ Aktualität (Stand 2026-06):** Die **Berichtspflicht** nach **§ 12 LkSG** und die behördliche Berichtsprüfung (§ 13 LkSG) werden durch eine LkSG-Novelle **rückwirkend zum 01.01.2023 gestrichen**; das **BAFA** prüft Unternehmensberichte nach §§ 12, 13 LkSG bereits seit Herbst 2025 nicht mehr und verlangt keine Einreichung. Die behördliche **Kontrolle** der Sorgfaltspflichten bleibt; Ordnungswidrigkeiten sollen künftig nur bei besonders schweren Verstößen (z. B. unterlassene **Abhilfemaßnahmen** oder fehlende Präventionskonzepte) verfolgt werden. Außerdem überlagert die **CSDDD** das LkSG. Konkreter Inkrafttretens- und Anwendungsstand: `[unverifiziert - prüfen]`.

## Eingaben

- Risikoanalyse, Präventions-/Abhilfemaßnahmen, Beschwerdeverfahren (Vorgewerke)
- Bisherige Dokumentation und (frühere) BAFA-Berichte
- Anfragen/Auskunftsersuchen oder Anordnungen des BAFA
- Umsatzkennzahlen (für Bußgeldbemessung § 24 Abs. 3 LkSG)

## Sub-Agent-Architektur

Ein **Dokumentations-Agent** stellt die fortlaufende interne Dokumentation nach § 10 Abs. 1 LkSG zusammen (Risikoanalyse, Maßnahmen, Wirksamkeitsprüfungen, Beschwerden) und sichert die siebenjährige Aufbewahrung. Ein **Berichts-Agent** prüft, ob und in welcher Form eine **Berichtspflicht** nach § 12 LkSG noch besteht (Novelle beachten). Ein **Aufsichts-Agent** bereitet auf die **BAFA**-Kontrolle nach §§ 14, 15 LkSG vor und prüft Auskunfts-, Duldungs- und Mitwirkungspflichten. Ein **Sanktions-Agent** bewertet das **Bußgeld**risiko nach § 24 LkSG und die CSDDD-Schnittstelle und markiert Unsicheres mit `[unverifiziert - prüfen]`.

## Ablauf

### 1. Dokumentationspflicht (§ 10 Abs. 1 LkSG)

- Fortlaufende, interne **Dokumentationspflicht** über die Erfüllung der Sorgfaltspflichten.
- Inhalt: Risikoanalyse, Grundsatzerklärung, Präventions-/Abhilfemaßnahmen, Beschwerdeverfahren, Wirksamkeitsprüfungen.
- Aufbewahrung **mindestens sieben Jahre**.

### 2. Berichtspflicht (§ 12 LkSG)

- Ursprünglich: jährlicher Bericht über die Erfüllung der Sorgfaltspflichten, Veröffentlichung und Einreichung beim **BAFA**.
- **Aktuell:** Die **Berichtspflicht** nach § 12 LkSG wird durch die Novelle gestrichen; das BAFA fordert derzeit keine Berichte. Maßgeblichen Stand prüfen `[unverifiziert - prüfen]`.

### 3. Behördliche Kontrolle (§ 14 LkSG)

- Das **BAFA** wird von Amts wegen oder auf Antrag tätig (**§ 14 LkSG**).
- Auskunftsersuchen, Betretensrechte, Herausgabe von Unterlagen; Duldungs- und Mitwirkungspflichten des Unternehmens.

### 4. Anordnungen und Maßnahmen (§ 15 LkSG)

- Das BAFA kann **Anordnungen** und Maßnahmen treffen, um Verstöße festzustellen, zu beseitigen und zu verhindern (**§ 15 LkSG**).
- Unternehmen muss angemessene Maßnahmen vorlegen; Durchsetzung ggf. mit Zwangsgeld (§ 23 LkSG).

### 5. Bußgeld (§ 24 LkSG)

- **§ 24 LkSG** sanktioniert Pflichtverletzungen mit **Bußgeld** bis **800.000 EUR** (z. B. unterlassene Abhilfemaßnahme), gestaffelt bis **500.000 EUR** und **100.000 EUR**.
- Bei durchschnittlichem Jahresumsatz **> 400 Mio. EUR** Geldbuße bis **2 % des weltweiten durchschnittlichen Jahresumsatzes** (§ 24 Abs. 3 LkSG) — beschränkt auf bestimmte Abhilfeverstöße.
- Nebenfolge: möglicher Ausschluss von der Vergabe öffentlicher Aufträge (§ 22 LkSG).

### 6. CSDDD-Schnittstelle

- Die **CSDDD** (Richtlinie (EU) 2024/1760) wird das LkSG ablösen/überlagern (zivilrechtliche Haftung, Klimaplan, breitere Wertschöpfungskette).
- Umsetzungs- und Anwendungstermine sind durch das Omnibus-Verfahren in Bewegung `[unverifiziert - prüfen]`.

## Risiken / typische Fehler

- **Bußgeld unterschätzt** — das **Bußgeld** nach § 24 LkSG kann umsatzbezogen (2 %) ausfallen; Abhilfeverstöße wiegen schwer.
- **Berichtspflicht falsch eingeschätzt** — Bericht nach altem Stand eingereicht oder versäumt, obwohl die Pflicht durch die Novelle gestrichen wird; Stand `[unverifiziert - prüfen]`.
- **BAFA-Kontrolle unvorbereitet** — Mitwirkungs- und Auskunftspflichten gegenüber dem **BAFA** unterschätzt; Anordnungen nach §§ 14, 15 LkSG nicht fristgerecht befolgt.
- **Dokumentation lückenhaft** — die Dokumentation ist beweispflichtig; Lücken gehen zu Lasten des Unternehmens.
- **CSDDD-Vorbereitung versäumt** — die **CSDDD** verschärft Pflichten und Haftung; späte Datenbasis ist riskant.
- **Aufbewahrungsfrist verkürzt** — Sieben-Jahres-Frist nicht eingehalten.

## Quellen

### Statute

- [LkSG](https://www.gesetze-im-internet.de/lksg/) — Volltext
- [§ 10 LkSG](https://www.gesetze-im-internet.de/lksg/__10.html), [§ 12 LkSG](https://www.gesetze-im-internet.de/lksg/__12.html), [§ 14 LkSG](https://www.gesetze-im-internet.de/lksg/__14.html), [§ 15 LkSG](https://www.gesetze-im-internet.de/lksg/__15.html), [§ 24 LkSG](https://www.gesetze-im-internet.de/lksg/__24.html)
- [Richtlinie (EU) 2024/1760 (CSDDD)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024L1760) · Änderungs-RL (EU) 2026/470 (Omnibus I) `[unverifiziert - prüfen]`

### BAFA

- [BAFA – Lieferkettengesetz](https://www.bafa.de/DE/Lieferketten/ueberblick_node.html) — Kontrolle, Anordnungen, Bußgeldverfahren

## Ausgabeformat

```
BAFA-DOKUMENTATION & DURCHSETZUNG (LkSG) — <Unternehmen> — <Datum>

I.    Dokumentation (§ 10 LkSG)
      Inhalt / Aufbewahrung 7 Jahre: <…>
II.   Berichtspflicht (§ 12 LkSG)
      Status: [gestrichen lt. Novelle / zu prüfen]  ([unverifiziert - prüfen])
III.  Behördliche Kontrolle (§ 14 LkSG)
      Auskunfts-/Mitwirkungspflichten: <…>
IV.   Anordnungen (§ 15 LkSG)
      Vorliegende Anordnung / Reaktion: <…>
V.    Bußgeldrisiko (§ 24 LkSG)
      Tatbestand | Rahmen (800k/500k/100k/2 %): <…>
      Vergabeausschluss (§ 22 LkSG): <…>
VI.   CSDDD-Ausblick
      <… [unverifiziert - prüfen]>

Restrisiko: <…>
Wiedervorlage: jährlich + bei BAFA-Anfrage
```
