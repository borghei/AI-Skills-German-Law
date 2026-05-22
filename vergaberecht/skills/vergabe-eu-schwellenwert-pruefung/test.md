---
skill: vergaberecht/vergabe-eu-schwellenwert-pruefung
fact_pattern: |
  Kommunaler Auftraggeber (Stadt mit 60.000 EW, juristische Person
  des öffentlichen Rechts) plant Beschaffung einer Fachsoftware
  einschließlich vierjähriger Wartung. Geschätzter Wert: 70.000 EUR
  netto pro Jahr, Gesamtlaufzeit 48 Monate, Verlängerungsoption
  zweimal 12 Monate. Eine Aufteilung in Lose (Lizenz / Wartung /
  Schulung) wird erwogen. Bitte Auftragswert nach § 3 VgV ermitteln,
  Schwellenwertprüfung durchführen und Verfahrensart vorschlagen.

must_cite:
  - "§ 99 GWB"
  - "§ 106 GWB"
  - "§ 3 VgV"
  - "§ 14 VgV"
  - "RL 2014/24/EU"

must_appear:
  - "Vollwertprinzip"
  - "Lossplitting"
  - "Schwellenwert"
  - "Oberschwellen"
  - "Verfahrensart"
  - "VO (EU)"

must_flag:
  - "Verlängerungsoption"
  - "Splittingverbot"
  - "Schwellenwert-Stand"
---

# Test — vergabe-eu-schwellenwert-pruefung

Struktureller Smoke-Test. Erwartet wird, dass der Output das Vollwertprinzip § 3 Abs. 1 VgV anwendet, Verlängerungsoptionen in die Schätzung einrechnet, das Splittingverbot § 3 Abs. 7 VgV adressiert und die Schwellenwerte mit `[unverifiziert]`-Markierung versieht.

Run: `python ../../../scripts/eval.py --skill vergaberecht/skills/vergabe-eu-schwellenwert-pruefung`
