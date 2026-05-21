---
name: risikoanalyse-lksg
description: "Risikoanalyse nach § 5 LkSG – Identifikation menschenrechtlicher und umweltbezogener Risiken im eigenen Geschäftsbereich und bei unmittelbaren Zulieferern; anlassbezogene Erweiterung auf mittelbare Zulieferer (§ 9 LkSG). Use when ein Unternehmen die jährliche Risikoanalyse aufsetzt oder ein anlassbezogenes Risiko bei einem mittelbaren Zulieferer eingegangen ist."
language: de
provider_variants: [claude, gemini, openai]
test: ./test.md
---

# /lieferkettengesetz:risikoanalyse-lksg

## Zweck

Die Risikoanalyse ist der Anker des LkSG. Eine unzureichende Risikoanalyse macht die nachfolgenden Pflichten (Prävention, Abhilfe, Beschwerdeverfahren, Bericht) angreifbar — und führt regelmäßig zu BAFA-Anfragen mit Bußgeldrisiko nach **§ 24 LkSG**: bis zu **800.000 EUR** (Abs. 2 Satz 1 Nr. 1) für Pflichtverletzungen wie Abhilfemaßnahme nicht ergriffen, **500.000 EUR** für Risikoanalyse-Verletzung (Nr. 2), **100.000 EUR** in den übrigen Fällen. Bei juristischen Personen mit durchschnittlichem Jahresumsatz **> 400 Mio. EUR** kann eine Geldbuße nach § 24 Abs. 3 LkSG bis zu **2 % des weltweiten durchschnittlichen Jahresumsatzes** verhängt werden — beschränkt auf Verstöße gegen Abhilfepflichten (Abs. 1 Nr. 6, Nr. 7 lit. a).

## Eingaben

- Geschäftsbereich (Branchen, Geographie, Produkte/Dienstleistungen)
- Direkte Zulieferer (Liste, Länder, Risikoprofile)
- Bekannte Vorfälle / Beschwerden / NGO-Berichte
- Ergebnis der vorherigen Risikoanalyse
- CSDDD-Anwendungszeitraum (für Vorbereitung)

## Ablauf

### 1. Geltungsbereich (§ 1 LkSG)

- Hauptverwaltung in DE und **≥ 1.000 Beschäftigte** im Inland (seit 2024)
- Konzernzurechnung: Beschäftigte verbundener Unternehmen in DE werden berücksichtigt (§ 1 Abs. 3 LkSG)

### 2. Geschützte Rechtspositionen (§ 2 LkSG)

- **Menschenrechtliche Risiken** § 2 Abs. 2 (Verbot Kinderarbeit, Zwangsarbeit, Diskriminierung, unzureichende Arbeitssicherheit, Vorenthalten angemessenen Lohns, Verstoß gegen Vereinigungsfreiheit, Folter, rechtswidrige Landnahme, Einsatz von Sicherheitskräften mit Übergriff)
- **Umweltbezogene Risiken** § 2 Abs. 3 (Minamata-Übereinkommen Quecksilber, Stockholmer Konvention POPs, Basler Konvention Abfälle)

### 3. Risikoanalyse-Stufen (§ 5 LkSG)

**Stufe 1 – eigener Geschäftsbereich:**

- Standorte, Tochterunternehmen
- Beschäftigte, Subunternehmer auf dem Werksgelände

**Stufe 2 – unmittelbare Zulieferer:**

- Vertragliche Direktbeziehung
- Risikobewertung mind. **jährlich** und **anlassbezogen**

**Stufe 3 – mittelbare Zulieferer (§ 9 LkSG):**

- Nur **anlassbezogen** bei "substantiierter Kenntnis" eines möglichen Verstoßes
- Trigger: NGO-Bericht, Medienbericht, interne Hinweise, Audit-Findings

### 4. Methodik der Risikobewertung

Pro Risiko bewerten:

1. **Schweregrad** – wie gravierend ist der mögliche Verstoß?
2. **Umkehrbarkeit** – wie umkehrbar ist der Schaden?
3. **Wahrscheinlichkeit** – wie wahrscheinlich tritt er ein?
4. **Beitragsleistung** – verursacht / trägt bei / steht in unmittelbarer Geschäftsbeziehung?
5. **Einflussvermögen** – wie viel Einfluss hat das Unternehmen?

### 5. Priorisierung (§ 5 Abs. 2 LkSG)

Risiken werden nach Angemessenheits-Kriterien priorisiert:

- Art und Umfang der Geschäftstätigkeit
- Einflussvermögen
- typische Schwere und Umkehrbarkeit
- Wahrscheinlichkeit
- Art des Verursachungsbeitrags

### 6. Dokumentation (§ 10 LkSG)

- **Dokumentationspflicht** intern (§ 10 Abs. 1)
- **Berichtspflicht** an BAFA jährlich (§ 10 Abs. 2)
- Aufbewahrung **7 Jahre**

### 7. CSDDD-Ausblick (Richtlinie (EU) 2024/1760)

- Förmlich angenommen **24.05.2024**; Umsetzung durch Mitgliedstaaten bis Mitte 2026.
- Phasierung (Stand: ursprüngliche Fassung):
  - **Phase 1 (26.07.2027)** – EU-Unternehmen mit **> 6.000 EE und > 1,5 Mrd. EUR Nettoumsatz** weltweit; Drittland-Unternehmen mit > 1,5 Mrd. EUR EU-Nettoumsatz.
  - **Phase 2 (26.07.2028)** – Unternehmen mit **> 900 Mio. EUR Nettoumsatz**.
- **Sorgfaltspflichten auf die gesamte „Chain of Activities"** (Upstream + Teile Downstream).
- Klimaplan-Pflicht (Art. 22 CSDDD).
- Zivilrechtliche Haftung für Verletzungen (Art. 29 CSDDD).
- **⚠️ Aktualität:** Die Kommission hat im **November 2024** die Verschmelzung von CSRD, CSDDD und EU-Taxonomie zu einer einzigen Verordnung angekündigt; im **Februar 2025** kam eine **Omnibus-Vereinfachungs-Initiative** („Stop-the-Clock") hinzu, die Anwendungsfristen verlängern soll. Im **November 2025** hat das EU-Parlament Änderungen mit konservativer Mehrheit beschlossen. **Vor jeder Mandatsentscheidung den aktuellen Stand der CSDDD und etwaiger Umsetzungsgesetze (DE: bislang offen) prüfen.**

## Quellen

### Statute

- [LkSG (Lieferkettensorgfaltspflichtengesetz)](https://www.gesetze-im-internet.de/lksg/) — Volltext, §§ 1–24
- [§ 5 LkSG](https://www.gesetze-im-internet.de/lksg/__5.html), [§ 9 LkSG](https://www.gesetze-im-internet.de/lksg/__9.html), [§ 10 LkSG](https://www.gesetze-im-internet.de/lksg/__10.html), [§ 24 LkSG](https://www.gesetze-im-internet.de/lksg/__24.html)
- [Richtlinie (EU) 2024/1760 (CSDDD)](https://eur-lex.europa.eu/eli/dir/2024/1760/oj)
- UN-Leitprinzipien für Wirtschaft und Menschenrechte (UNGPs)
- ILO-Kernarbeitsnormen

### BAFA

- [BAFA – Lieferkettengesetz](https://www.bafa.de/) — Anlaufstelle, Handreichungen, Berichtsformulare
- BAFA-Handreichungen zur Risikoanalyse (aktuelle Fassung)

### Sekundärliteratur

- Grabosch, LkSG, 1. Aufl. 2023
- Hembach, in: Beck'scher Online-Kommentar LkSG (aktualisiert)

## Ausgabeformat

```
LkSG-RISIKOANALYSE — <Berichtsjahr> — <Datum>

I.    Geltungsbereich                [Ja / Nein — Beschäftigtenzahl]
II.   Methodik
      Schwere | Umkehrbarkeit | Wahrscheinlichkeit | Beitragsleistung | Einfluss
III.  Stufe 1 — eigener Geschäftsbereich
      Identifizierte Risiken: <Liste>
      Bewertung: <Priorisierung>
IV.   Stufe 2 — unmittelbare Zulieferer
      Top-N nach Risikoexposition: <…>
      Methodik: <Self-Assessment / Audit / Datenanbieter>
V.    Stufe 3 — mittelbare Zulieferer
      Substantiierte Kenntnis: [keine / Ja — Quelle: …]
      Vertiefte Prüfung: <…>
VI.   Priorisierte Risiken (Top 5)   <…>
VII.  Folgemaßnahmen
      - Prävention § 6              <…>
      - Abhilfe § 7                  <…>
      - Vertragliche Verankerung     <…>
VIII. BAFA-Bericht-Vorbereitung      <…>

Risiko-Restrisiko: <…>
Wiedervorlage: jährlich + ad-hoc
```

## Risiken / typische Fehler

- **Stufenfolge ignoriert** — direkter Sprung auf mittelbare Zulieferer ohne substantiierten Anlass.
- **Self-Assessment ohne Verifizierung** — BAFA verlangt belastbare Methodik.
- **CSDDD-Vorbereitung vergessen** — Übergangsfristen sind kurz für eine valide Datenbasis.
- **Dokumentation lückenhaft** — Pflicht ist beweispflichtig in BAFA-Verfahren.
- **Beschwerden ignoriert** — eine eingehende Beschwerde ist regelmäßig „substantiierte Kenntnis" i.S.v. § 9 LkSG.
- **Klimaschutz / Umwelt eng ausgelegt** — LkSG erfasst Quecksilber/POPs/Abfall, CSDDD wird breiter (Pariser Klimaabkommen).
