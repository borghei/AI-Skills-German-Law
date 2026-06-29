---
name: praeventions-abhilfemassnahmen
description: "Ableitung und Priorisierung angemessener Präventionsmaßnahmen (§ 6 LkSG) und Abhilfemaßnahmen (§ 7 LkSG) im eigenen Geschäftsbereich und bei unmittelbaren Zulieferern, ausgehend von der Risikoanalyse (§ 5 LkSG) und dem Angemessenheitsmaßstab (§ 3 LkSG). Use when nach einer Risikoanalyse konkrete Präventions- oder Abhilfemaßnahmen festzulegen oder ein eingetretener Verstoß abzustellen ist."
language: de
provider_variants: [claude, gemini, openai]
test: ./test.md
---

# /lieferkettengesetz:praeventions-abhilfemassnahmen

## Zweck

Nach der Risikoanalyse verlangt das LkSG **Handeln**: angemessene **Präventionsmaßnahmen** (**§ 6 LkSG**) zur Verhinderung von Risiken und **Abhilfemaßnahmen** (**§ 7 LkSG**) bei bereits eingetretenen oder unmittelbar bevorstehenden Verletzungen. Maßstab ist stets die **Angemessenheit** (**§ 3 LkSG**). Diese Skill leitet aus den priorisierten Risiken die richtigen Maßnahmen ab, ordnet sie der zutreffenden Stufe (eigener Geschäftsbereich / unmittelbarer Zulieferer) zu und dokumentiert ihre Wirksamkeit.

## Eingaben

- Ergebnis der Risikoanalyse nach § 5 LkSG (priorisierte Risiken)
- Grundsatzerklärung zur Menschenrechtsstrategie (falls vorhanden)
- Betroffene Standorte / unmittelbare Zulieferer
- Bestehende Verträge, Einkaufspraktiken, Audit-Ergebnisse
- Eingegangene Beschwerden / Hinweise (Schnittstelle § 8 LkSG)

## Sub-Agent-Architektur

Ein **Strategie-Agent** überführt die priorisierten Risiken in die **Grundsatzerklärung** und leitet die menschenrechts- und umweltbezogenen Erwartungen an Beschäftigte und Zulieferer ab. Ein **Präventions-Agent** entwirft Maßnahmen je Stufe (eigener Geschäftsbereich, unmittelbarer Zulieferer): Beschaffungsstrategie, vertragliche Zusicherungen, Schulungen, risikobasierte Kontrollen. Ein **Abhilfe-Agent** prüft bei eingetretenen Verletzungen den Maßnahmenpfad nach § 7 LkSG und unterscheidet inländischen eigenen Geschäftsbereich (zwingende Beendigung) von Zulieferer-Konstellationen (Minimierungs-/Beendigungskonzept). Ein **Angemessenheits-Agent** wägt jede Maßnahme gegen die Kriterien des § 3 LkSG ab und markiert offene Punkte mit `[unverifiziert - prüfen]`.

## Ablauf

### 1. Angemessenheitsmaßstab (§ 3 LkSG)

Die **Angemessenheit** richtet sich nach: Art und Umfang der Geschäftstätigkeit, Einflussvermögen, typischerweise zu erwartender Schwere und Umkehrbarkeit der Verletzung, Wahrscheinlichkeit und Art des Verursachungsbeitrags.

### 2. Präventionsmaßnahmen im eigenen Geschäftsbereich (§ 6 Abs. 1, 3 LkSG)

- Abgabe einer **Grundsatzerklärung** zur Menschenrechtsstrategie durch die Unternehmensleitung (§ 6 Abs. 2 LkSG).
- Umsetzung der Strategie in den relevanten Geschäftsabläufen.
- Geeignete Beschaffungsstrategien und Einkaufspraktiken.
- Schulungen und risikobasierte Kontrollmaßnahmen.

### 3. Präventionsmaßnahmen beim unmittelbaren Zulieferer (§ 6 Abs. 4 LkSG)

Beim **unmittelbaren Zulieferer**:

- Berücksichtigung menschenrechtsbezogener Erwartungen bei der Auswahl,
- vertragliche Zusicherung der Einhaltung und deren Weitergabe in der Kette,
- Vereinbarung von Kontrollmechanismen (Audits) und deren Durchführung.

### 4. Abhilfemaßnahmen (§ 7 LkSG)

- Bei eingetretener oder unmittelbar bevorstehender Verletzung: **unverzüglich** angemessene **Abhilfemaßnahmen**.
- **Eigener Geschäftsbereich im Inland:** Maßnahmen müssen zur **Beendigung** der Verletzung führen.
- **Unmittelbarer Zulieferer:** wenn Beendigung kurzfristig nicht möglich — Konzept mit Zeitplan zur Beendigung/Minimierung; ultima ratio Abbruch der Geschäftsbeziehung (§ 7 Abs. 3 LkSG) nur bei schwerwiegenden Verstößen und erfolglosen Maßnahmen.

### 5. Priorisierung und Wirksamkeitskontrolle

- **Priorisierung** der Maßnahmen nach Angemessenheit und Einflussvermögen.
- Wirksamkeit der Präventions- und Abhilfemaßnahmen **mindestens jährlich** und anlassbezogen überprüfen (§ 6 Abs. 5, § 7 Abs. 4 LkSG).

### 6. Dokumentation

- Maßnahmen, Begründung der Angemessenheit und Wirksamkeitsprüfung dokumentieren (Schnittstelle § 10 LkSG, BAFA-Nachweis).

## Risiken / typische Fehler

- **Angemessenheit nicht begründet** — Maßnahme ohne nachvollziehbare Abwägung der **Angemessenheit** nach § 3 LkSG; in einem BAFA-Verfahren angreifbar.
- **Stufe verwechselt** — Maßnahmen gegen mittelbare Zulieferer statt gegen den **unmittelbarer Zulieferer**; § 6 erfasst primär den eigenen Geschäftsbereich und unmittelbare Zulieferer.
- **Abhilfemaßnahmen verspätet** — **Abhilfemaßnahmen** nicht unverzüglich oder im Inland ohne Beendigungswirkung ergriffen.
- **Vorschneller Abbruch** — Geschäftsbeziehung abgebrochen, statt zunächst ein Beendigungskonzept zu versuchen (Abbruch ist ultima ratio).
- **Wirksamkeit nicht geprüft** — keine jährliche/anlassbezogene Überprüfung; **BAFA** verlangt belastbaren Nachweis.
- **Grundsatzerklärung fehlt** — keine von der Leitung verabschiedete Menschenrechtsstrategie.

## Quellen

### Statute

- [LkSG](https://www.gesetze-im-internet.de/lksg/) — Volltext
- [§ 3 LkSG](https://www.gesetze-im-internet.de/lksg/__3.html), [§ 5 LkSG](https://www.gesetze-im-internet.de/lksg/__5.html), [§ 6 LkSG](https://www.gesetze-im-internet.de/lksg/__6.html), [§ 7 LkSG](https://www.gesetze-im-internet.de/lksg/__7.html), [§ 24 LkSG](https://www.gesetze-im-internet.de/lksg/__24.html)

### BAFA / Sekundärliteratur

- [BAFA – Lieferkettengesetz](https://www.bafa.de/) — Handreichungen zu Präventions- und Abhilfemaßnahmen
- Grabosch, LkSG, 1. Aufl. 2023; Hembach, BeckOK LkSG (aktualisiert)

## Ausgabeformat

```
PRÄVENTION & ABHILFE (LkSG) — <Unternehmen> — <Datum>

I.    Angemessenheitsmaßstab (§ 3 LkSG)
      Einflussvermögen / Schwere / Wahrscheinlichkeit / Beitrag: <…>
II.   Grundsatzerklärung
      Prioritäre Risiken / Erwartungen: <…>
III.  Prävention eigener Geschäftsbereich (§ 6 LkSG)
      Maßnahmen: <…>
IV.   Prävention unmittelbarer Zulieferer (§ 6 LkSG)
      Vertrag / Audit / Schulung: <…>
V.    Abhilfe (§ 7 LkSG)
      Verletzung eingetreten? [Ja/Nein]
      Inland eigener Geschäftsbereich → Beendigung: <…>
      Zulieferer → Konzept/Zeitplan / ultima ratio Abbruch: <…>
VI.   Priorisierung & Wirksamkeitskontrolle
      <…>
VII.  Dokumentation (§ 10 LkSG)
      <…>

Restrisiko: <…>
Wiedervorlage: jährlich + anlassbezogen
```
