---
skill: geldwaesche-aml-kyc/gwg-risikoanalyse
fact_pattern: |
  Mandantin (BaFin-lizenzierte Vermögensverwaltung, 120 Mio. AuM,
  internationales Privatkundengeschäft inkl. Schweiz und VAE,
  vereinzelt Krypto-Verwahrung) hat seit zwei Jahren keine
  Risikoanalyse aktualisiert. Letzte BaFin-Sonderprüfung hat
  Dokumentationsmängel festgestellt. Geschäftsleitung möchte eine
  GwG-konforme Risikoanalyse nach § 5 GwG mit Risikofaktoren-
  matrix und Ableitung des Pflichtenniveaus.

must_cite:
  - "§ 4 GwG"
  - "§ 5 GwG"
  - "§ 6 GwG"
  - "§ 10 GwG"
  - "§ 15 GwG"
  - "§ 56 GwG"

must_appear:
  - "Risikoanalyse"
  - "Kunde"
  - "Produkt"
  - "Vertriebsweg"
  - "geografisch"
  - "Pflichtenniveau"
  - "Aktualisierung"
  - "PEP"

must_flag:
  - "Schubladendokument"
  - "nicht pauschal"
  - "Aktualisierung"
---

# Test — gwg-risikoanalyse

Struktureller Smoke-Test. Die vier Risikokategorien (Kunde / Produkt / Vertriebsweg / Geografie) müssen sämtlich im Output erscheinen; Aktualisierungsturnus jährlich + anlassbezogen muss adressiert werden; Bußgeldrisiko § 56 GwG ist zu erwähnen.

Run: `python ../../../scripts/eval.py --skill geldwaesche-aml-kyc/skills/gwg-risikoanalyse`
