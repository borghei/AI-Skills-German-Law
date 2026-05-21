---
skill: arbeitsrecht/kuendigungs-pruefung
fact_pattern: |
  Mandantin betreibt Maschinenbauunternehmen mit 35 AN, kein BR. Plant
  betriebsbedingte Kündigung einer von drei Stellen im Vertriebsinnendienst.
  Drei AN in Vergleichsgruppe:
    - A: 10 Jahre, 45, verheiratet, 2 Kinder
    - B: 3 Jahre, 30, ledig, anerkannt schwerbehindert (GdB 50)
    - C: 8 Jahre, 55, geschieden, 1 Kind
  Plant Aussprache zum Quartalsende. Massenentlassungsschwelle nicht
  erreicht. Mandantin möchte wissen, gegen wen sie sozialauswahl-konform
  kündigen kann.

must_cite:
  - "§ 1 KSchG"
  - "§ 1 Abs. 3 KSchG"
  - "§ 23 KSchG"
  - "§ 102 BetrVG"
  - "§ 622 BGB"
  - "§ 168 SGB IX"
  - "§ 17 MuSchG"
  - "§ 18 BEEG"

must_appear:
  - "Sonderkündigungsschutz"
  - "Sozialauswahl"
  - "Kündigungsfrist"
  - "Massenentlassung"
  - "BR-Anhörung"
  - "Ausgabeformat"
  - "Risiken"

must_flag:
  - "Massenentlassungsanzeige"
  - "Sozialauswahl"
  - "BEM"
  - "Sonderkündigungsschutz"
---

# Test — kuendigungs-pruefung

## Zweck dieses Tests

Strukturelle Assertion: Eine Kündigungsprüfung **muss** mindestens die oben genannten Statute zitieren, mindestens die genannten Sections im Output enthalten und die genannten Risiken im Risiken-Block flaggen.

Der Test sagt **nichts** über die textliche Qualität — das ist Sache des Reviewers ([`../../agents/reviewer.md`](../../agents/reviewer.md)).

## Erwartete Ausgabe (Skizze)

Ein Memo mit Trafficlight-Befund, Ablauf-Stufen I bis VIII (siehe `Ausgabeformat` im SKILL.md), Sozialauswahl-Tabelle, expliziter Sonderschutz-Flagge für B (§ 168 SGB IX → 🔴 Blocker), Empfehlung gegenüber C unter Sozialauswahl-Gesichtspunkten, Massenentlassungsschwelle als "nicht erreicht" markiert.

## Anti-Patterns

- **Kein** `[generiert]`-Marker im Output (→ Validator-Fehler).
- **Keine** Empfehlung der Diskriminierung von B aufgrund Schwerbehinderung.
- **Keine** Mandatsentscheidung in der Kurzantwort.

## Ausführung

```bash
python ../../../scripts/eval.py --skill arbeitsrecht/skills/kuendigungs-pruefung
```
