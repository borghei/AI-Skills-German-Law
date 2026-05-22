---
skill: energierecht/energieeffizienzpflicht
fact_pattern: |
  Mandantin (Industrieunternehmen, ca. 600 MA, ca. 9 GWh/a
  Endenergieverbrauch im 3-Jahres-Mittel, keine verbundenen
  Großunternehmen) prüft Pflichten nach EnEfG / EDL-G. Frage:
  EnMS- oder UMS-Pflicht nach § 8 EnEfG? Energieaudit-Pflicht nach
  § 8 EDL-G? Schnittstelle zur CSRD-Berichtspflicht E1.
  Bitte Übersicht plus Nachweisführung gegenüber BAFA.

must_cite:
  - "§ 8 EnEfG"
  - "§ 9 EnEfG"
  - "§ 8 EDL-G"
  - "Empfehlung 2003/361/EG"

must_appear:
  - "KMU"
  - "Energiemanagementsystem"
  - "ISO 50001"
  - "EMAS"
  - "BAFA"
  - "7,5 GWh"
  - "Nicht-KMU"
  - "CSRD"

must_flag:
  - "verbundene Unternehmen"
  - "Übergangsfristen"
  - "Sanktion"
---

# Test — energieeffizienzpflicht

Struktureller Smoke-Test. Die KMU-Einstufung (Empfehlung 2003/361/EG) muss als Vorfrage geprüft werden; die EnEfG-Schwelle (7,5 GWh/a) muss klar von der EDL-G-Audit-Pflicht (Nicht-KMU) getrennt werden; ISO 50001 / EMAS müssen als Befreiungstatbestand vom Audit nach § 8 Abs. 3 EDL-G erkannt werden; CSRD/ESRS-E1-Schnittstelle muss erwähnt werden.

Run: `python ../../../scripts/eval.py --skill energierecht/skills/energieeffizienzpflicht`
