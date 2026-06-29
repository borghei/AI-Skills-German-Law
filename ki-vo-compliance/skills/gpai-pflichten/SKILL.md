---
name: gpai-pflichten
description: "Prüfung der Pflichten von Anbietern von KI-Modellen mit allgemeinem Verwendungszweck (GPAI) nach Art. 53 KI-VO und der Zusatzpflichten bei systemischem Risiko Art. 55 KI-VO – technische Dokumentation, Urheberrechtsstrategie, Praxisleitfäden (Codes of Practice). Use when ein Anbieter eines GPAI-Modells (Foundation Model) seine Dokumentations-, Transparenz- und Risikopflichten nach der KI-VO bestimmen muss."
language: de
provider_variants: [claude, gemini, openai]
test: ./test.md
---

# /ki-vo-compliance:gpai-pflichten

## Zweck

KI-Modelle mit allgemeinem Verwendungszweck (General-Purpose AI, **GPAI**) unterliegen einem eigenen Pflichtenregime nach **Art. 53 KI-VO** ([VO (EU) 2024/1689](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1689)); Modelle mit **systemischem Risiko** treffen zusätzlich die strengeren Pflichten nach **Art. 55 KI-VO**. Die Regeln gelten seit dem 2. August 2025 für neue Modelle. Dieser Skill bestimmt die Anbieterpflichten und prüft die Einstufung als systemisches Risiko.

## Eingaben

- Modelltyp und Trainingsumfang (Rechenleistung in FLOP, Datenmenge, Modalitäten)
- Rolle des Mandanten (Anbieter des Modells, nachgelagerter Anbieter, Open-Source-Bereitsteller)
- Vertriebsweg (proprietär, frei lizenziert/Open Source)
- Verwendete Trainingsdaten (urheberrechtlich geschützte Inhalte? TDM-Vorbehalte?)
- Beitritt zu einem Praxisleitfaden (Code of Practice)?

## Sub-Agent-Architektur

Drei gedankliche Rollen strukturieren die Analyse. Ein **Einstufungs-Prüfer** klärt, ob ein GPAI-Modell vorliegt und ob es nach Art. 51 i.V.m. Art. 55 KI-VO als Modell mit systemischem Risiko gilt (Schwellenwert > 10^25 FLOP Trainingsrechenleistung). Ein **Dokumentations-Architekt** stellt die Informations-, Dokumentations- und Urheberrechtspflichten nach Art. 53 KI-VO und Anhang XI/XII zusammen. Ein **Risiko-Analyst** ergänzt bei systemischem Risiko die Zusatzpflichten nach Art. 55 KI-VO. Der Einstufungs-Prüfer entscheidet zuerst über die Modellkategorie, bevor die beiden anderen Rollen ihre Kataloge anwenden.

## Ablauf

### 1. Einordnung als GPAI-Modell

Ein GPAI-Modell zeigt **erhebliche allgemeine Verwendbarkeit** und kann ein breites Spektrum nachgelagerter Aufgaben erfüllen. Reine Forschungs-/Prototyp-Modelle vor Marktbereitstellung sind ausgenommen.

### 2. Grundpflichten aller GPAI-Anbieter (Art. 53 KI-VO)

a) **Technische Dokumentation** des Modells erstellen und aktuell halten (Trainings-/Testverfahren, Bewertungsergebnisse) — mindestens Inhalt nach **Anhang XI**, auf Anfrage an das KI-Büro/Behörden
b) **Informationen für nachgelagerte Anbieter** bereitstellen, die das Modell integrieren (Fähigkeiten und Grenzen) — Inhalt nach **Anhang XII**
c) **Urheberrechtsstrategie**: schriftliche Strategie zur Einhaltung des Unionsrechts, insbesondere zur Beachtung des Rechtsvorbehalts (TDM-Opt-out) nach der DSM-Richtlinie
d) **Zusammenfassung der Trainingsinhalte** öffentlich bereitstellen (nach Vorlage des KI-Büros)

Für **freie und quelloffene** GPAI-Modelle entfallen lit. a und b teilweise — nicht jedoch die Urheberrechts- und Trainingsdaten-Zusammenfassungspflichten (lit. c, d) und nicht bei systemischem Risiko.

### 3. Modelle mit systemischem Risiko (Art. 55 KI-VO)

Einstufung bei Trainingsrechenleistung **> 10^25 FLOP** (Art. 51 KI-VO) oder durch Benennung des KI-Büros. Zusatzpflichten:

- **Modellbewertung** inkl. adversarialer Tests (Red-Teaming)
- **Bewertung und Minderung systemischer Risiken** auf Unionsebene
- **Meldung schwerwiegender Vorfälle** an das KI-Büro und nationale Behörden
- angemessenes Niveau an **Cybersicherheit** für Modell und physische Infrastruktur

### 4. Praxisleitfäden / Codes of Practice (Art. 56 KI-VO)

Bis zur Verfügbarkeit harmonisierter Normen können Anbieter die Einhaltung über **Praxisleitfäden (Codes of Practice)** nachweisen. Der vom KI-Büro veröffentlichte GPAI-Code of Practice dient als zentrales Umsetzungsinstrument; ein Beitritt begründet die Vermutung der Konformität.

### 5. Sanktionen (Art. 101 KI-VO)

Gegen GPAI-Anbieter kann das KI-Büro Geldbußen bis **15 Mio. EUR oder 3 % des weltweiten Jahresumsatzes** verhängen.

## Risiken

- **Falsche Einstufung** — Überschreiten der 10^25-FLOP-Schwelle ohne Anerkennung des systemischen Risikos verletzt Art. 55 KI-VO.
- **Urheberrecht** — fehlende Strategie zur Beachtung des TDM-Vorbehalts verstößt gegen Art. 53 KI-VO; Klagerisiko von Rechteinhabern.
- **Dokumentationslücke** — unvollständige technische Dokumentation nach Anhang XI/XII gegenüber nachgelagerten Anbietern und Behörden.
- **Bußgeldrisiko** — bis 15 Mio. EUR / 3 % nach Art. 101 KI-VO.

## Ausgabeformat

```
GPAI-PFLICHTEN — PRÜFUNG — <Modell> — <Datum>

I.   GPAI-Modell?                               [ja / nein — Begründung]
II.  Rolle                                      [Anbieter / nachgelagert / Open Source]
III. Grundpflichten (Art. 53 KI-VO)
     Technische Dokumentation (Anhang XI)       [Status <…>]
     Info nachgelagerte Anbieter (Anhang XII)   [Status <…>]
     Urheberrechtsstrategie / TDM               [Status <…>]
     Trainingsdaten-Zusammenfassung             [Status <…>]
IV.  Systemisches Risiko (Art. 55 KI-VO)        [> 10^25 FLOP? / benannt?]
     Zusatzpflichten                            [Red-Teaming / Vorfallmeldung / Cybersicherheit]
V.   Code of Practice (Art. 56 KI-VO)           [beigetreten? <…>]
VI.  Bußgeldrisiko (Art. 101 KI-VO)             [bis 15 Mio. EUR / 3 %]

Empfehlung: <…>
Nächste Schritte: <…>
```

## Quellen

### Statute

- [VO (EU) 2024/1689 (KI-VO / EU AI Act)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1689) — Volltext mit Anhängen
- Art. 51 KI-VO (Einstufung systemisches Risiko), Art. 53 KI-VO (GPAI-Pflichten), Art. 55 KI-VO (systemisches Risiko), Art. 56 KI-VO (Praxisleitfäden), Art. 101 KI-VO (Geldbußen GPAI), Anhang XI, Anhang XII KI-VO

### Leitlinien

- KI-Büro der EU-Kommission, GPAI Code of Practice (Juli 2025)
- KI-Büro, Vorlage zur Zusammenfassung der Trainingsinhalte

### Sekundärliteratur

- Hilgendorf/Roth-Isigkeit, KI-VO, 1. Aufl. 2024
- BeckOK KI-VO (Online)
