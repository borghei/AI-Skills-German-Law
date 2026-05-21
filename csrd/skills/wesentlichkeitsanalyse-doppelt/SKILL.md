---
name: wesentlichkeitsanalyse-doppelt
description: "Durchführung der doppelten Wesentlichkeitsanalyse nach ESRS 1 §§ 25–53 – Impact Materiality (Auswirkungen des Unternehmens auf Mensch und Umwelt) und Financial Materiality (Risiken/Chancen aus Nachhaltigkeitsthemen für das Unternehmen). Use when ein Unternehmen erstmals CSRD-pflichtig ist oder die jährliche Wesentlichkeitsanalyse aufgesetzt wird."
language: de
provider_variants: [claude, gemini, openai]
test: ./test.md
---

# /csrd:wesentlichkeitsanalyse-doppelt

## Zweck

Die doppelte Wesentlichkeit ist der Anker jedes CSRD-Berichts. Themen, die als wesentlich identifiziert werden, lösen die ausführliche Berichtspflicht nach den themenbezogenen ESRS aus (E1–E5, S1–S4, G1). Eine fehlerhafte Wesentlichkeitsanalyse macht den gesamten Bericht angreifbar — und führt zu Prüfungseinschränkungen.

> **⚠️ Aktualität (Stand 2026-05-21):** Die EU-Kommission hat am **26.02.2025** das **„Omnibus I"-Vereinfachungspaket** vorgeschlagen, darunter eine **„Stop-the-Clock"-Initiative**, die die Erstanwendung für **Wave-2- und Wave-3-Unternehmen** um zwei Jahre auf **2028** verschiebt. Im **November 2024** hatte die Kommission zusätzlich angekündigt, CSRD, CSDDD und EU-Taxonomie in eine einzige Verordnung zu überführen. Im **November 2025** hat das EU-Parlament mit konservativer Mehrheit Änderungen beschlossen. Der finale Stand der Schwellenwerte und Anwendungsdaten ist daher **vor jeder Mandatsentscheidung tagesaktuell** zu prüfen (EUR-Lex + EFRAG).

## Eingaben

- Geschäftsmodell, Wertschöpfungskette (Upstream + Downstream)
- Branche und geographische Tätigkeit
- Bestehende Stakeholder-Befragungen
- Risikomanagement-Output (für Financial Materiality)
- Ergebnis der vorherigen Wesentlichkeitsanalyse (Kontinuitätsprinzip)
- LkSG-Risikoanalyse (Schnittstelle)

## Ablauf

### 1. Konzept doppelte Wesentlichkeit (ESRS 1 § 25)

Ein Thema ist wesentlich, wenn **mindestens eine** der beiden Perspektiven es erfasst:

- **Impact Materiality (§§ 27–43)** — das Unternehmen hat **tatsächliche oder potenzielle, positive oder negative, kurz- oder langfristige** Auswirkungen auf Menschen oder Umwelt entlang der eigenen Tätigkeit und der Wertschöpfungskette.
- **Financial Materiality (§§ 44–53)** — Nachhaltigkeitsthemen können zu **Risiken** oder **Chancen** führen, die die finanzielle Lage, Performance, Cashflows, Zugang zu Finanzierung oder Kapitalkosten beeinflussen.

### 2. Universal-Themen aus ESRS-Standards

Ausgangsliste der zu prüfenden Themen aus den themenbezogenen ESRS:

| Cluster | ESRS | Thema |
|---|---|---|
| E – Umwelt | ESRS E1 | Klimawandel |
| | ESRS E2 | Umweltverschmutzung |
| | ESRS E3 | Wasser und Meeresressourcen |
| | ESRS E4 | Biologische Vielfalt und Ökosysteme |
| | ESRS E5 | Ressourcennutzung und Kreislaufwirtschaft |
| S – Soziales | ESRS S1 | Eigene Belegschaft |
| | ESRS S2 | Beschäftigte in der Wertschöpfungskette |
| | ESRS S3 | Betroffene Gemeinschaften |
| | ESRS S4 | Verbraucher und Endnutzer |
| G – Governance | ESRS G1 | Geschäftsgebaren |

### 3. Schwellenwerte und Bewertung

- **Schwellenwert** = Punkt, ab dem ein Thema „wesentlich" ist. Festlegung durch das Unternehmen, **mit Begründung**.
- Impact: Schweregrad × (Umfang + Umfang + Umkehrbarkeit) × Wahrscheinlichkeit (bei potenziellen Impacts).
- Financial: Höhe × Wahrscheinlichkeit × Zeithorizont.

### 4. Stakeholder-Einbindung (ESRS 1 § 24)

- **Tatsächliche Stakeholder** (eigene Belegschaft, Lieferanten, Kunden, Investoren, Gemeinden)
- **Stille Stakeholder** für Umwelt-Themen (Natur, künftige Generationen)
- Methoden: Befragung, Workshop, NGO-Konsultation, Datenanbieter-Analyse

### 5. Verzahnung mit anderen Pflichten

- **EU-Taxonomie** (VO (EU) 2020/852) — taxonomiefähige und taxonomiekonforme Aktivitäten/Umsatzanteile
- **LkSG / CSDDD** — Risikoanalyse-Outputs sind Inputs der Wesentlichkeitsanalyse
- **NFRD** (vorherige Berichte) — Kontinuität der Berichterstattung
- **EU-Klimagesetz und Pariser Übereinkommen** — Zielreferenz

### 6. Dokumentation

- Methodik schriftlich beschreiben (ESRS 1 § 53)
- Bewertungsraster mit Skalen
- Stakeholder-Liste
- Ergebnistabelle mit Begründung pro Thema
- Verweise im Bericht (Lagebericht / Nachhaltigkeitsbericht)

### 7. Prüfung

- **Limited Assurance** durch unabhängige Prüfer ab erster Anwendung
- Übergang zu **Reasonable Assurance** geplant (EU-Kommission Roadmap)

## Quellen

### Statute / EU-Rechtsakte

- [RL (EU) 2022/2464 (CSRD, Corporate Sustainability Reporting Directive)](https://eur-lex.europa.eu/eli/dir/2022/2464/oj) — Volltext
- [Delegierte VO (EU) 2023/2772 (ESRS Set 1)](https://eur-lex.europa.eu/eli/reg_del/2023/2772/oj) — ESRS-Standards
- [VO (EU) 2020/852 (EU-Taxonomie)](https://eur-lex.europa.eu/eli/reg/2020/852/oj)

### EFRAG-Materialien

- EFRAG IG 1: Materiality Assessment Implementation Guidance
- EFRAG IG 2: Value Chain Implementation Guidance
- EFRAG IG 3: Detailed ESRS Datapoints

### Sekundärliteratur

- IDW PS 980 (Compliance-Management-Systeme; benachbart)
- Behnke / Hoff, CSRD und ESRS, 1. Aufl. 2024
- Beck'sches IFRS-Handbuch (Nachhaltigkeit)

## Ausgabeformat

```
DOPPELTE WESENTLICHKEITSANALYSE — <Unternehmen> — <Berichtsjahr>

I.    Methodik
      Impact-Bewertung:  Schweregrad / Umfang / Umkehrbarkeit / Wahrscheinlichkeit
      Financial-Bewertung: Höhe / Wahrscheinlichkeit / Zeithorizont
      Schwellenwert: <begründet>
II.   Stakeholder-Einbindung
      Methoden: <…>
      Stakeholder: <Liste>
III.  Themen-Bewertung
      ESRS  | Impact | Financial | Wesentlich?
      E1    |   …    |    …      |   ja
      E2    |   …    |    …      |   nein
      ...
IV.   Begründung pro wesentliches Thema
      <…>
V.    Verzahnung
      EU-Taxonomie: <…>
      LkSG-Inputs:  <…>
      Vorjahr-Kontinuität: <…>
VI.   Folgepflichten
      Datenpunkte: <Liste mit Modulen aus ESRS>
      Prüfungs-Vorbereitung: <…>

Restrisiko: <…>
Wiedervorlage: jährlich
```

## Risiken / typische Fehler

- **Nur Impact-Bewertung** — Financial Materiality vergessen oder nicht dokumentiert.
- **Schwellenwert ohne Begründung** — Prüfungs-Finding wahrscheinlich.
- **Wertschöpfungskette zu eng** — Downstream-Themen unterschätzt, insb. S4 (Verbraucher).
- **Stakeholder nicht eingebunden** — verstößt gegen ESRS 1 § 24.
- **Kontinuität verletzt** — Änderung der Methodik ohne Begründung gegenüber Vorjahr.
- **LkSG-Outputs ignoriert** — Schnittstelle ungenutzt; doppelte Arbeit.
