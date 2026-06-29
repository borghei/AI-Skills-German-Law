---
name: eu-taxonomie
description: "Einordnung von Wirtschaftstätigkeiten nach der Taxonomie-VO (EU) 2020/852 – Taxonomiefähigkeit und Taxonomiekonformität (Art. 3, sechs Umweltziele Art. 9, „Do no significant harm“) sowie Offenlegung der KPI Umsatz/CapEx/OpEx nach Art. 8. Use when ein Unternehmen seine taxonomiefähigen und -konformen Anteile bestimmen oder die Art.-8-Offenlegung vorbereiten muss."
language: de
provider_variants: [claude, gemini, openai]
test: ./test.md
---

# /csrd:eu-taxonomie

## Zweck

Die **Taxonomie-VO (EU) 2020/852** ist das Klassifikationssystem der EU für ökologisch nachhaltige Wirtschaftstätigkeit. Berichtspflichtige Unternehmen müssen offenlegen, welcher Anteil ihres **Umsatzes**, ihrer Investitionsausgaben (**CapEx**) und Betriebsausgaben (**OpEx**) auf taxonomiefähige bzw. taxonomiekonforme Tätigkeiten entfällt. Die Taxonomie verzahnt sich eng mit der CSRD/ESRS-Berichterstattung. Fehler in der Konformitätsprüfung (insbesondere bei „Do no significant harm“) führen zu Prüfungseinschränkungen und Greenwashing-Vorwürfen.

> **⚠️ Aktualität (Stand 2026-06):** Die Darstellung der Art.-8-KPI wurde durch die **Delegierte VO (EU) 2026/73** (Omnibus-Vereinfachung) geändert; zudem sind Anwendungskreis und Erleichterungen Teil des **Omnibus-I-Pakets** (Änderungs-RL (EU) 2026/470). Schwellen, Befreiungen und Templates sind daher `[unverifiziert - prüfen]` und gegen EUR-Lex tagesaktuell abzugleichen.

## Eingaben

- Tätigkeitsportfolio (NACE-Codes, Produkte/Dienstleistungen)
- Finanzdaten: Umsatzerlöse, CapEx, OpEx (mit Kontenzuordnung)
- Bestehende Umwelt-/Klimadaten (Emissionen, Energie, Wasser)
- Ergebnis der doppelten Wesentlichkeitsanalyse (Schnittstelle ESRS E1–E5)
- Vorjahres-Taxonomie-Offenlegung (Kontinuität)

## Sub-Agent-Architektur

Ein **Eligibility-Agent** ordnet jede Tätigkeit den delegierten Rechtsakten zu und bestimmt die **Taxonomiefähigkeit** (eligibility) je Umweltziel. Ein **Alignment-Agent** prüft die **Taxonomiekonformität** in drei Stufen: wesentlicher Beitrag zu mindestens einem Umweltziel, **„Do no significant harm“** gegenüber den übrigen Zielen und Einhaltung des **Mindestschutzes** (minimum safeguards, Art. 18). Ein **KPI-Agent** rechnet die Anteile für **Umsatz**, **CapEx** und **OpEx** und mappt sie in die Offenlegungs-Templates. Ein **Verifikations-Agent** gleicht jede Schwelle und jedes Template gegen EUR-Lex ab und kennzeichnet Unsicheres mit `[unverifiziert - prüfen]`.

## Ablauf

### 1. Begriff der nachhaltigen Tätigkeit (Art. 3 Taxonomie-VO)

Nach **Art. 3 Taxonomie-VO** ist eine Tätigkeit ökologisch nachhaltig, wenn sie kumulativ:

1. einen **wesentlichen Beitrag** zu mindestens einem Umweltziel leistet,
2. **kein anderes Umweltziel erheblich beeinträchtigt** („Do no significant harm“, Art. 17),
3. den **Mindestschutz** (Art. 18, u. a. OECD-Leitsätze, UN-Leitprinzipien) wahrt und
4. die technischen Bewertungskriterien der delegierten Rechtsakte erfüllt.

### 2. Sechs Umweltziele (Art. 9 Taxonomie-VO)

**Art. 9 Taxonomie-VO** definiert die sechs Umweltziele:

1. Klimaschutz,
2. Anpassung an den Klimawandel,
3. Wasser- und Meeresressourcen,
4. Kreislaufwirtschaft,
5. Vermeidung und Verminderung der Umweltverschmutzung,
6. Schutz und Wiederherstellung der Biodiversität und der Ökosysteme.

### 3. Taxonomiefähigkeit (eligibility)

- Tätigkeit ist in einem delegierten Rechtsakt **beschrieben** → taxonomiefähig.
- Erste Stufe der Offenlegung: Anteil taxonomiefähiger vs. nicht-fähiger Umsätze/CapEx/OpEx.

### 4. Taxonomiekonformität (alignment)

- Wesentlicher Beitrag + **Do no significant harm** + Mindestschutz + technische Kriterien erfüllt → taxonomiekonform.
- Pro Tätigkeit dokumentieren, welche DNSH-Kriterien geprüft wurden.

### 5. KPI-Berechnung (Art. 8 Taxonomie-VO)

Nach **Art. 8 Taxonomie-VO** und der Delegierten VO (EU) 2021/2178 (i. d. F. (EU) 2026/73) sind drei KPI offenzulegen:

- **Umsatz-KPI** — Anteil taxonomiekonformer Umsatzerlöse,
- **CapEx-KPI** — Anteil taxonomiekonformer Investitionsausgaben,
- **OpEx-KPI** — Anteil taxonomiekonformer Betriebsausgaben.

Doppelzählungen vermeiden; Zähler/Nenner sauber abgrenzen.

### 6. Offenlegung und Verzahnung

- Darstellung in den vorgegebenen Templates; Verbindung zur ESRS-Berichterstattung (E1–E5).
- Konsistenz mit der Wesentlichkeitsanalyse und den Klimadaten herstellen.

## Risiken / typische Fehler

- **Do no significant harm verkürzt** — nur wesentlicher Beitrag geprüft, **Do no significant harm** und Mindestschutz nicht dokumentiert; häufigster Prüfungs-Finding.
- **Taxonomiefähigkeit mit -konformität verwechselt** — fähige als konforme Anteile ausgewiesen; die **Taxonomiekonformität** verlangt zusätzlich DNSH + Mindestschutz.
- **CapEx falsch abgegrenzt** — **CapEx** aus Übergangs-/Anpassungsplänen nicht berücksichtigt oder doppelt gezählt.
- **Template veraltet** — alte Offenlegungsvorlage statt der aktuellen Fassung; Stand `[unverifiziert - prüfen]`.
- **Mindestschutz ignoriert** — Art. 18 (OECD/UN-Leitprinzipien, LkSG-Schnittstelle) nicht geprüft.
- **Greenwashing-Risiko** — überzeichnete Konformitätsquote ohne belastbare technische Kriterien.

## Quellen

### EU-Rechtsakte

- [Taxonomie-VO (EU) 2020/852](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32020R0852) — Art. 3, Art. 8, Art. 9, Art. 17, Art. 18
- [Delegierte VO (EU) 2021/2178 (Art.-8-Offenlegung)](https://eur-lex.europa.eu/eli/reg_del/2021/2178/oj) · Delegierte VO (EU) 2026/73 (Vereinfachung) `[unverifiziert - prüfen]`
- [Delegierte VO (EU) 2021/2139 (Klima-Bewertungskriterien)](https://eur-lex.europa.eu/eli/reg_del/2021/2139/oj)

### Schnittstellen

- [RL (EU) 2022/2464 (CSRD)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022L2464) · ESRS E1–E5
- LkSG / CSDDD (Mindestschutz Art. 18)

## Ausgabeformat

```
EU-TAXONOMIE — <Unternehmen> — <Berichtsjahr>

I.    Tätigkeitsmapping
      Tätigkeit | NACE | Umweltziel (Art. 9) | fähig?
II.   Konformitätsprüfung (Art. 3)
      Wesentlicher Beitrag | Do no significant harm | Mindestschutz | techn. Kriterien
III.  KPI (Art. 8)
      Umsatz:  fähig __ %   konform __ %
      CapEx:   fähig __ %   konform __ %
      OpEx:    fähig __ %   konform __ %
IV.   Verzahnung ESRS / Klimadaten
      <…>
V.    Offene Punkte
      <… [unverifiziert - prüfen]>

Restrisiko: <…>
Wiedervorlage: jährlich
```
