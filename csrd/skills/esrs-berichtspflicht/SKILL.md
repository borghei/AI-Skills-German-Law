---
name: esrs-berichtspflicht
description: "Bestimmung der Nachhaltigkeitsberichtspflicht nach CSRD-RL (EU) 2022/2464 und ihrer HGB-Umsetzung – wer ab welchem Geschäftsjahr nach welchen ESRS-Standards berichtet (Anwendungsbereich, Größenkriterien, Konzernebene, Zeitplan). Use when geklärt werden muss, ob und ab wann ein Unternehmen einen Nachhaltigkeitsbericht erstellen muss und welchen Inhalt dieser hat."
language: de
provider_variants: [claude, gemini, openai]
test: ./test.md
---

# /csrd:esrs-berichtspflicht

## Zweck

Diese Skill klärt die Eingangsfrage jeder CSRD-Beratung: **Ist das Unternehmen berichtspflichtig, ab wann, und welchen Inhalt schuldet es?** Die Pflicht folgt aus der **RL (EU) 2022/2464** (CSRD) und ihrer Umsetzung in das HGB (Nachhaltigkeitsangaben im Lagebericht). Anwendungsbereich und Zeitplan sind seit dem EU-Omnibus-Verfahren stark in Bewegung — eine falsche Einordnung führt entweder zu unnötigem Aufwand oder zu einer Pflichtverletzung mit Prüfungs- und Haftungsfolgen.

> **⚠️ Aktualität (Stand 2026-06):** Das **Omnibus-I-Paket** wurde final beschlossen — der Rat hat die **Änderungsrichtlinie (EU) 2026/470** am **24.02.2026** angenommen, Veröffentlichung im Amtsblatt **26.02.2026**, Inkrafttreten 20 Tage später. Kernpunkt: Die CSRD-Pflicht gilt künftig nur für Unternehmen mit **mehr als 1.000 Beschäftigten** **und** **über 450 Mio. EUR Nettoumsatz**. Bereits die **Stop-the-Clock-RL (EU) 2025/794** (Amtsblatt April 2025) hatte Erstanwendungstermine verschoben. **Deutschland hat die CSRD bislang nicht umgesetzt** — der Regierungsentwurf eines CSRD-Umsetzungsgesetzes datiert vom 03.09.2025, die Anhörung im Rechtsausschuss fand am **13.04.2026** statt. Schwellenwerte und Erstanwendungstermine sind daher `[unverifiziert - prüfen]` und vor jeder Mandatsentscheidung tagesaktuell an EUR-Lex und dem Stand des deutschen Gesetzgebungsverfahrens abzugleichen.

## Eingaben

- Rechtsform, Kapitalmarktorientierung
- Beschäftigtenzahl (Jahresdurchschnitt), Bilanzsumme, Nettoumsatz — Einzel- und Konzernebene
- Konzernstruktur (Mutter-/Tochterunternehmen, Befreiungstatbestände)
- Bisherige Berichtspraxis (NFRD-Erklärung, freiwilliger Bericht)
- Geschäftsjahr (kalender- oder abweichend)

## Sub-Agent-Architektur

Die Bearbeitung folgt einer Kette spezialisierter Rollen. Ein **Scoping-Agent** prüft den Anwendungsbereich und die Größenkriterien auf Einzel- und Konzernebene und ermittelt das maßgebliche Erstanwendungs-Geschäftsjahr. Ein **Inhalts-Agent** leitet aus der Wesentlichkeitsanalyse die zu berichtenden ESRS-Datenpunkte ab und ordnet sie den §§ 289b–289e HGB (bzw. künftig den neuen HGB-Vorschriften) zu. Ein **Konzern-Agent** prüft Befreiungs- und Einbeziehungstatbestände nach § 315b HGB. Ein **Verifikations-Agent** gleicht jede Schwellenwert- und Datumsangabe gegen EUR-Lex und den aktuellen Gesetzesstand ab und markiert Unsicheres mit `[unverifiziert - prüfen]`.

## Ablauf

### 1. Anwendungsbereich und Größenkriterien

- Geltende Schwellenwerte (Beschäftigte / Bilanzsumme / Nettoumsatz) prüfen — nach Omnibus voraussichtlich **> 1.000 Beschäftigte und > 450 Mio. EUR Nettoumsatz** `[unverifiziert - prüfen]`.
- Übergang vom NFRD-Regime: Für das **Geschäftsjahr 2025** gelten in Deutschland mangels Umsetzung weiterhin die **nichtfinanzielle Erklärung** nach **§ 289b HGB** / **§ 315b HGB** für große kapitalmarktorientierte Unternehmen sowie Kredit- und Versicherungsinstitute mit mehr als 500 Beschäftigten.
- Erstanwendungs-Welle und maßgebliches Geschäftsjahr festhalten.

### 2. Nichtfinanzielle Erklärung / Nachhaltigkeitsbericht (§ 289b HGB)

- **§ 289b HGB** verankert die Pflicht zur (nichtfinanziellen) Erklärung bzw. zum Nachhaltigkeitsbericht im **Lagebericht**.
- Ort: gesonderter Abschnitt des Lageberichts (CSRD verlangt Integration in den Lagebericht, nicht mehr den gesonderten Bericht der NFRD).
- Befreiung der Tochter bei Einbezug in einen Konzernbericht.

### 3. Inhalt der Berichterstattung (§ 289c HGB)

- **§ 289c HGB** bestimmt die inhaltlichen Mindestangaben (Umwelt-, Arbeitnehmer-, Sozialbelange, Achtung der Menschenrechte, Korruptionsbekämpfung).
- Unter der CSRD treten die **ESRS-Standards** an die Stelle der freien Rahmenwahl: **ESRS 1** (allgemeine Anforderungen) und ESRS 2 (allgemeine Angaben) sind verpflichtend, die themenbezogenen Standards E1–E5 / S1–S4 / G1 nach Maßgabe der Wesentlichkeitsanalyse.

### 4. Konzernebene (§ 315b HGB)

- **§ 315b HGB** regelt die **Konzern**-Nachhaltigkeitsberichterstattung im Konzernlagebericht.
- Befreiungstatbestände für Tochterunternehmen prüfen (Einbezug in den Konzernbericht der Mutter, auch Drittstaaten-Mutter mit gleichwertigem Bericht).

### 5. ESRS-Datenpunkte und Anhang

- Pflicht- und wesentlichkeitsabhängige Datenpunkte aus den **ESRS** ableiten.
- Digitales Format (XHTML/iXBRL-Tagging) und maschinenlesbare Auszeichnung berücksichtigen.

### 6. Prüfung und Zeitplan

- **Limited assurance** durch unabhängige Prüfer ab Erstanwendung; spätere Anhebung diskutiert.
- Zeitplan und Schwellenwerte abschließend mit dem Stand des CSRD-Umsetzungsgesetzes abgleichen.

## Risiken / typische Fehler

- **Omnibus-Stand ignoriert** — Beratung auf Basis überholter Schwellenwerte; der **Omnibus**-Prozess hat Anwendungsbereich und Termine geändert.
- **Schwellenwert falsch angesetzt** — der maßgebliche **Schwellenwert** (Beschäftigte/Umsatz) ist `[unverifiziert - prüfen]` und tagesaktuell zu bestätigen.
- **Konzernebene übersehen** — Befreiung auf **Konzernebene** nach § 315b HGB nicht geprüft, dadurch Doppelberichterstattung oder Lücke.
- **NFRD/CSRD-Übergang verwechselt** — für das Geschäftsjahr 2025 gilt in Deutschland noch das NFRD-Regime, nicht die ESRS.
- **Wesentlichkeit nicht vorgeschaltet** — ESRS-Datenpunkte ohne doppelte Wesentlichkeitsanalyse (siehe `/csrd:wesentlichkeitsanalyse-doppelt`) ausgewählt.
- **Erstanwendungstermin geschätzt** — Datum ohne Quelle angegeben statt mit `[unverifiziert - prüfen]` gekennzeichnet.

## Quellen

### EU-Rechtsakte

- [RL (EU) 2022/2464 (CSRD)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022L2464)
- [Delegierte VO (EU) 2023/2772 (ESRS Set 1)](https://eur-lex.europa.eu/eli/reg_del/2023/2772/oj)
- [Stop-the-Clock-RL (EU) 2025/794](https://eur-lex.europa.eu/eli/dir/2025/794/oj) · Änderungs-RL (EU) 2026/470 (Omnibus I) `[unverifiziert - prüfen]`

### Deutsches Recht

- [§ 289b HGB](https://www.gesetze-im-internet.de/hgb/__289b.html), [§ 289c HGB](https://www.gesetze-im-internet.de/hgb/__289c.html), [§ 315b HGB](https://www.gesetze-im-internet.de/hgb/__315b.html)
- CSRD-Umsetzungsgesetz (Regierungsentwurf 03.09.2025) — im Verfahren, `[unverifiziert - prüfen]`

## Ausgabeformat

```
ESRS-BERICHTSPFLICHT — <Unternehmen> — <Geschäftsjahr>

I.    Anwendungsbereich / Größenkriterien
      Beschäftigte / Bilanzsumme / Nettoumsatz: <…>
      Schwellenwert erfüllt: [Ja / Nein]   (Stand: [unverifiziert - prüfen])
II.   Erstanwendung
      Maßgebliches Geschäftsjahr: <…>
      Übergang NFRD → CSRD: <…>
III.  Berichtsort (§ 289b HGB)
      Lagebericht / Konzernlagebericht: <…>
IV.   Inhalt (§ 289c HGB / ESRS)
      Pflicht: ESRS 1, ESRS 2
      Wesentlich: <E…/S…/G…>
V.    Konzernebene (§ 315b HGB)
      Befreiung Tochter: [Ja / Nein]
VI.   Prüfung
      limited assurance: <Prüfer / Umfang>
VII.  Offene Punkte / tagesaktuell zu prüfen
      <… [unverifiziert - prüfen]>

Restrisiko: <…>
Wiedervorlage: vor Aufstellung des Lageberichts
```
