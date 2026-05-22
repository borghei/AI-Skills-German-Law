---
skill: vergaberecht/ausschreibungspruefung
fact_pattern: |
  Mandantin (IT-Dienstleister, GmbH) möchte sich auf eine
  EU-weite Ausschreibung einer Landesbehörde bewerben (offenes
  Verfahren, Auftragswert 800.000 EUR netto, Vertragslaufzeit
  vier Jahre). Die Vergabeunterlagen nennen vier Zuschlags-
  kriterien (Preis, Qualität, Konzept, Termin), jedoch ohne
  Gewichtung. Als Eignungsanforderung wird ein Mindestumsatz
  von 5 Mio. EUR pro Jahr in den letzten drei Jahren verlangt.
  Lose sind nicht vorgesehen. Angebotsfrist läuft in 18 Tagen.
  Bitte Vergabeunterlagen auf Vergaberechtskonformität prüfen
  und priorisierte Rügeliste mit Fristberechnung erstellen.

must_cite:
  - "§ 97 GWB"
  - "§ 122 GWB"
  - "§ 127 GWB"
  - "§ 31 VgV"
  - "§ 160 Abs. 3 S. 1"

must_appear:
  - "Eignung"
  - "Zuschlagskriterien"
  - "Gewichtung"
  - "Losaufteilung"
  - "Verhältnismäßigkeit"
  - "Rügeliste"
  - "Angebotsfrist"

must_flag:
  - "keine Gewichtung"
  - "Eignungsanforderungen unverhältnismäßig"
  - "Losaufteilung ohne ordnungsgemäße Begründung"
  - "Rügefrist"
---

# Test — ausschreibungspruefung

Struktureller Smoke-Test. Erwartet wird, dass der Output (1) die fehlende Gewichtung als Verstoß gegen § 127 Abs. 5 GWB identifiziert, (2) den Mindestumsatz von 5 Mio. EUR auf Verhältnismäßigkeit § 122 Abs. 4 GWB / § 45 Abs. 4 VgV prüft, (3) die unbegründete Verweigerung der Losaufteilung § 97 Abs. 4 GWB markiert und (4) die Rügefrist bis Ablauf der Angebotsfrist (§ 160 Abs. 3 S. 1 Nr. 3 GWB) konkret datiert.

Run: `python ../../../scripts/eval.py --skill vergaberecht/skills/ausschreibungspruefung`
