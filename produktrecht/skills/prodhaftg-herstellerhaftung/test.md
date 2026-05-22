---
skill: produktrecht/prodhaftg-herstellerhaftung
fact_pattern: |
  Verbraucherin (Privathaushalt) wurde durch einen berstenden Akku
  eines Haushaltsgeräts der Marke X am Arm verletzt (Verbrennungen
  zweiten Grades, ambulante Behandlung, Arbeitsausfall 3 Wochen).
  Inverkehrbringen des Geräts: 03/2022. Schadensereignis: 11/2024.
  Hersteller sitzt in DE; Akku-Zulieferer in CN. Erste Hinweise auf
  ähnliche Vorfälle in einem Online-Forum bereits 04/2024. Hersteller
  hat keine Warnung oder Rückrufaktion durchgeführt. Mandantin
  (Geschädigte) will Schmerzensgeld und Schadenersatz geltend machen.

must_cite:
  - "§ 1 ProdHaftG"
  - "§ 3 ProdHaftG"
  - "§ 4 ProdHaftG"
  - "§ 12 ProdHaftG"
  - "§ 13 ProdHaftG"
  - "§ 823"
  - "§ 253"
  - "Hühnerpest"

must_appear:
  - "Konstruktionsfehler"
  - "Fabrikationsfehler"
  - "Instruktionsfehler"
  - "Produktbeobachtung"
  - "Beweislastumkehr"
  - "Schmerzensgeld"
  - "Anspruchskonkurrenz"
  - "Risikosphäre"

must_flag:
  - "Erlöschen"
  - "Versicherer"
  - "Produktbeobachtungspflicht"
---

# Test — prodhaftg-herstellerhaftung

Struktureller Smoke-Test. Beide Anspruchsgrundlagen (§ 1 ProdHaftG und § 823 BGB) müssen parallel geprüft werden; die Fehlertypologie (Konstruktion / Fabrikation / Instruktion / Produktbeobachtung) muss explizit erscheinen; Schmerzensgeld muss auf § 253 II BGB gestützt werden; Verjährung und Erlöschen § 12 / § 13 ProdHaftG müssen sauber getrennt sein.

Run: `python ../../../scripts/eval.py --skill produktrecht/skills/prodhaftg-herstellerhaftung`
