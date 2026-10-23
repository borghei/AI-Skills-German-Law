---
skill: arbeitsrecht/entgeltfortzahlung-bem
fact_pattern: |
  Ein Lagermitarbeiter (seit 2017 beschäftigt) kündigt am 02.09.2026 zum
  30.09.2026 und legt am 03.09.2026 eine AU-Bescheinigung bis exakt
  30.09.2026 vor. Im Vorjahr war er an insgesamt 58 Tagen in mehreren
  Phasen arbeitsunfähig; ein BEM wurde nie angeboten. Der Arbeitgeber
  will die Entgeltfortzahlung für September verweigern und fragt, ob er
  einem Kollegen mit ähnlicher Fehlzeitenhistorie krankheitsbedingt
  kündigen kann.
must_cite:
  - "§ 3 EFZG"
  - "§ 4 EFZG"
  - "§ 5 EFZG"
  - "§ 7 EFZG"
  - "§ 167 Abs. 2 SGB IX"
  - "5 AZR 149/21"
must_appear:
  - "Rechtsstand: Oktober 2026"
  - "Fortsetzungserkrankung"
  - "Beweiswert"
  - "eAU"
  - "BEM"
  - "Drei-Stufen-Prüfung"
must_flag:
  - "Fortsetzungserkrankung nicht geprüft"
  - "Beweiswert der AU ohne Tatsachen bestritten"
  - "BEM nur schwerbehinderten Beschäftigten angeboten"
  - "Krankheitsbedingte Kündigung ohne BEM"
---

# Test — entgeltfortzahlung-bem

Prüft, ob der Skill die Erschütterung des Beweiswerts bei passgenauer AU
erkennt und die BEM-Pflicht als Verhältnismäßigkeitsmaßstab der
krankheitsbedingten Kündigung einordnet.

Run: `python scripts/eval.py --skill arbeitsrecht/skills/entgeltfortzahlung-bem`
