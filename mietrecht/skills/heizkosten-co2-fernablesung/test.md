---
skill: mietrecht/heizkosten-co2-fernablesung
fact_pattern: |
  Ein Frankfurter Vermieter (Mehrfamilienhaus Baujahr 1968, Gaszentral-
  heizung, Heizkostenverteiler aus 2015, nicht fernablesbar) fragt im
  Oktober 2026, ob er bis Jahresende handeln muss. Eine Mieterin hat die
  Heizkostenabrechnung 2025 erhalten: Verteilung 50 % nach Verbrauch, keine
  Angaben zur CO2-Einstufung, keine monatlichen Verbrauchsinformationen.
  Der Vermieter plant zudem eine neue Gasbrennwertheizung nach § 43 GModG
  und fragt, wie die CO2-Kosten ab 2028 zu teilen sind.
must_cite:
  - "§ 5 Abs. 3 HeizkostenV"
  - "§ 6a HeizkostenV"
  - "§ 7 HeizkostenV"
  - "§ 12 HeizkostenV"
  - "§ 7 Abs. 4 CO2KostAufG"
  - "§ 5a CO2KostAufG"
  - "§ 556 Abs. 3 BGB"
must_appear:
  - "Rechtsstand: Oktober 2026"
  - "31.12.2026"
  - "fernablesbar"
  - "Smart-Meter-Gateway"
  - "Stufenmodell"
  - "Gebäudemodernisierungsgesetz"
  - "Erstattungsanspruch"
  - "Deterministische Berechnung"
  - "Formulierungshilfe"
must_flag:
  - "Nachrüstfrist 31.12.2026 verpasst"
  - "Monatliche Verbrauchsinformation unterlassen"
  - "CO2-Ausweis fehlt"
  - "GModG-Teilung zu früh angewendet"
  - "Preiskorridor 2027 als feststehend behandelt"
---

# Test — heizkosten-co2-fernablesung

Struktureller Smoke-Test. Run: `python scripts/eval.py --skill mietrecht/skills/heizkosten-co2-fernablesung`
