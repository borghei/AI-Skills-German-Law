---
skill: geldwaesche-aml-kyc/kyc-identifikationspflicht
fact_pattern: |
  Neukunde einer deutschen Privatbank ist die A-GmbH. Anteilseigner
  ist eine luxemburgische SARL mit 100 %; deren Anteile werden zu
  60 % von einer zypriotischen Holding und zu 40 % von einer
  natürlichen Person Y gehalten. Die zypriotische Holding wird ihrer-
  seits über einen Trust auf Jersey gehalten, wirtschaftlich
  Begünstigter laut Trust Deed ist eine natürliche Person X. Es
  wird ein Investmentkonto mit Anlagevolumen 5 Mio. EUR eröffnet.
  Bitte KYC-Memo mit Identifizierung, wirtschaftlich Berechtigtem,
  Transparenzregister-Abgleich und Pflichtenniveau erstellen.

must_cite:
  - "§ 3 GwG"
  - "§ 10 GwG"
  - "§ 11 GwG"
  - "§ 12 GwG"
  - "§ 15 GwG"
  - "§ 8 GwG"

must_appear:
  - "wirtschaftlich Berechtigt"
  - "Transparenzregister"
  - "25 %"
  - "verstärkte Sorgfalt"
  - "PEP"
  - "Identifizierung"
  - "Aufbewahrung"
  - "fiktiv"

must_flag:
  - "fiktiver WB"
  - "Transparenzregister-Abgleich"
  - "komplexe Struktur"
---

# Test — kyc-identifikationspflicht

Struktureller Smoke-Test. Trigger der Identifizierungspflicht, WB-Kette über mehrstufige Auslandsstruktur und Transparenzregister-Abgleich müssen sämtlich behandelt werden; bei Jersey-Trust ist verstärkte Sorgfalt nach § 15 III Nr. 3 GwG zu adressieren.

Run: `python ../../../scripts/eval.py --skill geldwaesche-aml-kyc/skills/kyc-identifikationspflicht`
