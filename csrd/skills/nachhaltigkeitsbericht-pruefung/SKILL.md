---
name: nachhaltigkeitsbericht-pruefung
description: "Vorbereitung und Durchführung der externen Prüfung der Nachhaltigkeitsberichterstattung nach CSRD-RL (EU) 2022/2464 – Prüferbestellung, Prüfungsumfang (limited assurance), ESRS-Konformität und Verbindung zum Lagebericht (§ 289b HGB). Use when ein CSRD-pflichtiges Unternehmen die Prüfung seines Nachhaltigkeitsberichts beauftragt oder den Prüfungsumfang klären muss."
language: de
provider_variants: [claude, gemini, openai]
test: ./test.md
---

# /csrd:nachhaltigkeitsbericht-pruefung

## Zweck

Die CSRD führt erstmals eine **verpflichtende externe Prüfung** der Nachhaltigkeitsberichterstattung ein. Diese Skill klärt, **wer prüft, mit welchem Sicherheitsniveau und in welcher Tiefe**. Geprüft wird zunächst mit **limited assurance** (begrenzte Sicherheit); ein späterer Übergang zu reasonable assurance ist angelegt. Ein unzureichend vorbereiteter Bericht führt zu eingeschränkten Prüfungsvermerken — mit unmittelbarer Außenwirkung gegenüber Kapitalmarkt und Aufsicht.

> **⚠️ Aktualität (Stand 2026-06):** Das deutsche **CSRD-Umsetzungsgesetz** ist noch nicht in Kraft (Regierungsentwurf 03.09.2025, Anhörung 13.04.2026). Die Prüfung soll dauerhaft auf **limited assurance** gestützt werden (geplant **§ 324i HGB-E**). Prüfungsniveau, Prüferzulassung und Übergangstermine sind durch das **Omnibus**-Verfahren in Bewegung und `[unverifiziert - prüfen]`.

## Eingaben

- Entwurf des Nachhaltigkeitsberichts (Lageberichtsabschnitt)
- Wesentlichkeitsanalyse mit Methodik und Schwellenwert-Begründung
- ESRS-Datenpunkte mit Datenherkunft und Kontrollen
- Bisheriger Abschlussprüfer / Prüfungsausschuss-Beschluss
- Vorjahres-Prüfungsvermerk (falls vorhanden)

## Sub-Agent-Architektur

Ein **Bestellungs-Agent** klärt die Prüferbestellung und Unabhängigkeit (Abschlussprüfer, anderer Wirtschaftsprüfer oder unabhängiger Erbringer von Bestätigungsleistungen). Ein **Scoping-Agent** legt den **Prüfungsumfang** fest: Prozess der Wesentlichkeitsanalyse, ESRS-Angaben, Digital-Tagging, Konformität mit den ESRS. Ein **Evidenz-Agent** prüft die **ESRS-Konformität** der einzelnen Datenpunkte gegen die zugrunde liegenden Nachweise und Kontrollen. Ein **Vermerks-Agent** formuliert den Prüfungsvermerk (limited assurance) und kennzeichnet jede ungeklärte Rechts- oder Datumsfrage mit `[unverifiziert - prüfen]`.

## Ablauf

### 1. Prüferbestellung und Unabhängigkeit

- Bestellung durch die Gesellschafter/Hauptversammlung; Vorbereitung durch den Prüfungsausschuss.
- Unabhängigkeit und Verbot bestimmter Nicht-Prüfungsleistungen beachten.
- Festlegung, ob der **Abschlussprüfer** zugleich die Nachhaltigkeitsprüfung übernimmt.

### 2. Prüfungsumfang (limited assurance)

Die Prüfung mit **limited assurance** umfasst:

- den **Prozess** der doppelten Wesentlichkeitsanalyse,
- die Einhaltung der **ESRS** bei den berichteten Angaben (**ESRS-Konformität**),
- die Vorgaben zum digitalen Auszeichnungsformat (Tagging),
- die Vollständigkeit gegenüber den taxonomiebezogenen Angaben (Art. 8 Taxonomie-VO).

Das Niveau **limited assurance** verlangt eine Aussage in negativer Formulierung („keine Hinweise auf wesentliche Falschdarstellungen"); **reasonable assurance** (positive Aussage) ist als Ausbaustufe angelegt.

### 3. ESRS-Konformität der Angaben

- Datenpunkte gegen **ESRS 1** (allgemeine Anforderungen) und ESRS 2 sowie die wesentlichen themenbezogenen Standards abgleichen.
- Datenherkunft, Schätzverfahren und interne Kontrollen prüfen.
- Konsistenz zwischen Nachhaltigkeits- und Finanzberichterstattung.

### 4. Verbindung zum Lagebericht (§ 289b HGB)

- Der Nachhaltigkeitsbericht ist Teil des **Lageberichts** (**§ 289b HGB**); die Prüfung knüpft an diese Verortung an.
- Abgrenzung zur Lageberichtsprüfung nach den allgemeinen Vorschriften.
- Befund: gesonderter Prüfungsvermerk zur Nachhaltigkeitsberichterstattung.

### 5. Berichterstattung über die Prüfung

- Prüfungsvermerk mit Einschränkungen/Hinweisen, Verweis auf das Sicherheitsniveau.
- Kommunikation an Prüfungsausschuss und Aufsichtsorgan.

## Risiken / typische Fehler

- **Niveau verwechselt** — **limited assurance** als reasonable assurance dargestellt; die Aussageform unterscheidet sich grundlegend.
- **ESRS-Konformität nur formal** — **ESRS-Konformität** auf Vollständigkeit der Überschriften reduziert, ohne Datennachweis und Kontrollen.
- **Wesentlichkeitsprozess nicht prüffähig** — Methodik und Schwellenwert nicht dokumentiert; führt zu Einschränkung.
- **Prüferzulassung offen** — Zulassung/Unabhängigkeit nicht abschließend geklärt; Stand `[unverifiziert - prüfen]`.
- **Omnibus-Änderungen übersehen** — Prüfungsumfang nach altem Stand; das **Omnibus**-Paket kann Niveau und Termine verschieben.
- **Lageberichtsverortung ignoriert** — Verbindung nach § 289b HGB nicht hergestellt, Prüfungsvermerk falsch adressiert.

## Quellen

### EU-Rechtsakte

- [RL (EU) 2022/2464 (CSRD)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022L2464) — Prüfungspflicht (geänderte Bilanz-RL 2013/34/EU, Art. 34)
- [Delegierte VO (EU) 2023/2772 (ESRS Set 1)](https://eur-lex.europa.eu/eli/reg_del/2023/2772/oj)

### Deutsches Recht / Standards

- [§ 289b HGB](https://www.gesetze-im-internet.de/hgb/__289b.html) · § 324i HGB-E (CSRD-UmsG, im Verfahren) `[unverifiziert - prüfen]`
- IDW-Verlautbarungen zur Prüfung der Nachhaltigkeitsberichterstattung (aktuelle Fassung)

## Ausgabeformat

```
PRÜFUNG NACHHALTIGKEITSBERICHT — <Unternehmen> — <Geschäftsjahr>

I.    Prüferbestellung
      Prüfer / Unabhängigkeit / Prüfungsausschuss: <…>
II.   Prüfungsumfang
      Sicherheitsniveau: limited assurance
      Gegenstand: Wesentlichkeitsprozess / ESRS-Angaben / Tagging / Taxonomie
III.  ESRS-Konformität
      Datenpunkt | Standard | Nachweis | Befund
IV.   Verbindung Lagebericht (§ 289b HGB)
      <…>
V.    Prüfungsvermerk
      Einschränkungen / Hinweise: <…>
VI.   Offene Punkte
      <… [unverifiziert - prüfen]>

Restrisiko: <…>
Wiedervorlage: jährlich
```
