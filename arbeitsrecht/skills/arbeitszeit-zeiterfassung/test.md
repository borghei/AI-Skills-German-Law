---
skill: arbeitsrecht/arbeitszeit-zeiterfassung
fact_pattern: |
  Softwareunternehmen mit 140 Beschäftigten und Betriebsrat, nicht
  tarifgebunden, praktiziert „Vertrauensarbeitszeit" ohne jede Erfassung.
  Entwickler arbeiten in Release-Phasen regelmäßig 11 Stunden und
  beantworten abends Tickets. Ein ausgeschiedener Mitarbeiter verlangt
  Vergütung für 310 Überstunden und verweist auf die fehlende Erfassung.
  Die Geschäftsführung fragt, ob sie bis zum neuen Arbeitszeitgesetz warten
  kann.
must_cite:
  - "§ 3 ArbZG"
  - "§ 4 ArbZG"
  - "§ 5 ArbZG"
  - "§ 16 Abs. 2 ArbZG"
  - "§ 3 Abs. 2 Nr. 1 ArbSchG"
  - "§ 87 Abs. 1 Nr. 6 BetrVG"
  - "1 ABR 22/21"
  - "C-55/18"
must_appear:
  - "Rechtsstand: Oktober 2026"
  - "Erfassungspflicht"
  - "Ausgleichszeitraum"
  - "Ruhezeit"
  - "Referentenentwurf"
  - "Mitbestimmung"
  - "Maßnahmenplan"
must_flag:
  - "Entwurf als geltendes Recht dargestellt"
  - "Erfassungspflicht verneint"
  - "Vertrauensarbeitszeit als Verzicht auf Erfassung"
  - "Ruhezeit durch Erreichbarkeit unterbrochen"
  - "Duldung von Überstunden"
---

# Test — arbeitszeit-zeiterfassung

Prüft, ob der Skill die bereits geltende Erfassungspflicht aus dem ArbSchG
erkennt, den Referentenentwurf sauber als Entwurf behandelt und das
Überstundenrisiko bewertet.

Run: `python scripts/eval.py --skill arbeitsrecht/skills/arbeitszeit-zeiterfassung`
