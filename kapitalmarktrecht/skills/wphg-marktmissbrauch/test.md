---
skill: kapitalmarktrecht/wphg-marktmissbrauch
fact_pattern: |
  Vorstand einer im Prime Standard der FWB notierten AG verhandelt seit
  acht Wochen mit einem strategischen Investor über die Veräußerung
  eines Geschäftsbereichs, der ca. 35 % des Konzernumsatzes ausmacht.
  Term Sheet seit gestern unterzeichnet, Signing in 4 Wochen geplant.
  Vorstandsvorsitzender will außerdem in 3 Wochen 5.000 Aktien aus
  einem Mitarbeiterprogramm verkaufen. Bilanzpressekonferenz steht in
  6 Wochen an. Bitte prüfen, ob Ad-hoc-Pflicht besteht, ob Aufschub
  nach Art. 17 IV MAR zulässig ist und welche Pflichten zu
  Insiderliste und Directors' Dealings (Closed Period) bestehen.

must_cite:
  - "Art. 7 MAR"
  - "Art. 14 MAR"
  - "Art. 17 MAR"
  - "Art. 17 IV MAR"
  - "Art. 18 MAR"
  - "Art. 19 MAR"
  - "§ 119 WpHG"
  - "§ 38 WpHG"

must_appear:
  - "Insiderinformation"
  - "präzise"
  - "kursrelevant"
  - "Selbstaufschub"
  - "Berechtigtes Interesse"
  - "Vertraulichkeit"
  - "Insiderliste"
  - "Directors' Dealings"
  - "Closed Period"
  - "unverzüglich"

must_flag:
  - "Aufschub Art. 17 IV ohne Dokumentation"
  - "Zwischenschritt"
  - "Closed Period"
  - "Selbst-Bewertung"
---

# Test — wphg-marktmissbrauch

Struktureller Smoke-Test. Die vier Kriterien der Insiderinformation müssen geprüft sein, die drei Voraussetzungen des Selbstaufschubs (Art. 17 IV MAR) explizit abgehakt, Insiderliste und Closed Period adressiert sein.

Run: `python ../../../scripts/eval.py --skill kapitalmarktrecht/skills/wphg-marktmissbrauch`
