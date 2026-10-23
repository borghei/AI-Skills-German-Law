---
skill: arbeitsrecht/mindestlohn-minijob-aktivrente
fact_pattern: |
  Ein Einzelhändler beschäftigt sechs Minijobber zu je 603 EUR monatlich
  bei „ca. 45 Stunden im Monat"; zwei Aushilfen arbeiten auf Abruf ohne
  vereinbarte Stundenzahl. Zudem möchte er einen langjährigen Verkäufer,
  der im Dezember 2026 die Regelaltersgrenze erreicht, sachgrundlos
  befristet für zwei Jahre weiterbeschäftigen und fragt, was der Mitarbeiter
  steuerfrei verdienen kann.
must_cite:
  - "§ 1 MiLoG"
  - "§ 3 MiLoG"
  - "§ 17 MiLoG"
  - "§ 8 Abs. 1a SGB IV"
  - "§ 12 TzBfG"
  - "§ 3 Nr. 21 EStG"
  - "§ 41 Abs. 2 SGB VI"
must_appear:
  - "Rechtsstand: Oktober 2026"
  - "13,90 EUR"
  - "14,60 EUR"
  - "603 EUR"
  - "633 EUR"
  - "Aktivrente"
  - "Geringfügigkeitsgrenze"
must_flag:
  - "Minijob-Grenze nicht mitgezogen"
  - "Arbeit auf Abruf ohne Stundenzahl"
  - "Ausschlussfrist ohne Mindestlohn-Ausnahme"
  - "§ 41 Abs. 2 SGB VI als Freibrief"
---

# Test — mindestlohn-minijob-aktivrente

Prüft die Werte 2026/2027, die Drift-Falle bei festen Beträgen und die
neue Befristungsmöglichkeit nach der Regelaltersgrenze.

Run: `python scripts/eval.py --skill arbeitsrecht/skills/mindestlohn-minijob-aktivrente`
