# Barrierefreiheit (BFSG / BFSGV / BGG / BITV 2.0)

**Production-grade Barrierefreiheits-Skills für Claude / Gemini / GPT.** Anwendungsbereich, Produktkonformität, E-Commerce-Pflichten und das getrennte Regime der öffentlichen Stellen. Researcher → Drafter → Reviewer.

> **Die Trennung zwischen privatem und öffentlichem Regime ist das strukturelle Fehlerrisiko dieses Rechtsgebiets.** Für **private Wirtschaftsakteure** gegenüber **Verbrauchern** gelten das [BFSG](https://www.gesetze-im-internet.de/bfsg/) und die [BFSGV](https://www.gesetze-im-internet.de/bfsgv/) — anwendbar seit dem **28.06.2025**, mit Marktüberwachung durch die Länder und Bußgeldern bis 100.000 EUR. Für **öffentliche Stellen des Bundes** gelten [§§ 12a ff. BGG](https://www.gesetze-im-internet.de/bgg/__12a.html) und die [BITV 2.0](https://www.gesetze-im-internet.de/bitv_2_0/) — mit Erklärung zur Barrierefreiheit, Gebärdensprache und Leichter Sprache, aber **ohne Bußgeldtatbestand**. Für Länder und Kommunen gilt das jeweilige Landesrecht. Jede Skill dieses Plugins macht die Regimezuordnung deshalb zu Schritt 1.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `bfsg-anwendungsbereich` | Ist das Angebot erfasst, in welcher Rolle, ab wann — abschließende Kataloge, Kleinstunternehmensausnahme, Übergangsfristen | §§ 1, 2 Nr. 17, 3 Abs. 3, 38 BFSG; §§ 12a, 12b BGG; RL (EU) 2019/882 |
| `bfsg-produktkonformitaet` | Pflichtenkataloge der Lieferkette, technische Dokumentation, EU-Konformitätserklärung, CE-Kennzeichnung, Marktüberwachungsverfahren | §§ 4–13, 16–19, 20–23, 37 BFSG; Anlagen 2 und 4; §§ 4–11 BFSGV; VO (EU) 2019/1020 |
| `bfsg-dienstleistung-ecommerce` | Konformität von Online-Shops, Apps und Bankangeboten, Barrierefreiheitsinformationen, Verbraucher- und Verbandsverfahren, Schlichtung | § 14 BFSG + Anlage 3; §§ 16, 17 + Anlage 4; §§ 28–34, 37 BFSG; §§ 12, 13, 19, 21 BFSGV; § 3a UWG |
| `bitv-oeffentliche-stellen` | Gestaltungspflicht, Erklärung zur Barrierefreiheit, Gebärdensprache und Leichte Sprache, Überwachung, Schlichtung, Verbandsklage | §§ 12a, 12b, 15, 16 BGG; §§ 2a, 3, 4, 6–10 BITV 2.0 + Anlage 2; RL (EU) 2016/2102 |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: BFSG, BFSGV, BGG, BITV 2.0, Landesrecht, RL (EU) 2019/882 und 2016/2102, VO (EU) 2019/1020, EN 301 549, Bundesfachstelle und Überwachungsstelle
- [`agents/drafter.md`](./agents/drafter.md) – Entwürfe: Betroffenheitsanalyse, Befundmatrix, Barrierefreiheitsinformationen nach Anlage 3, Erklärung nach § 12b BGG, Behördenstellungnahme, Maßnahmenplan
- [`agents/reviewer.md`](./agents/reviewer.md) – Regime-, Nachweis-, Ausnahmen- und Fristencheck (insbesondere Anlage-3-Vollständigkeit, § 17 Abs. 4 BFSG, zehn Tage nach § 22 Abs. 2 S. 2 BFSG, ein Monat nach § 12b Abs. 4 BGG)

## Installation

### Claude Code
```bash
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install barrierefreiheit-bfsg
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area barrierefreiheit-bfsg --out dist/gemini
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area barrierefreiheit-bfsg --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Betroffenheit eines Online-Händlers

```
/barrierefreiheit-bfsg:bfsg-anwendungsbereich
Mandantin betreibt einen Shop für Fahrradzubehör (B2C und B2B), acht
Beschäftigte, 3,4 Mio. EUR Umsatz, vertreibt seit August 2025 einen
eigenen E-Book-Reader und betreibt Zahlungsterminals aus 2013. Frage:
Greift die Kleinstunternehmensausnahme, was gilt für die Terminals,
und wie sind Altverträge zu behandeln?
```

### Szenario 2 – Marktüberwachungsverfahren gegen einen Importeur

```
/barrierefreiheit-bfsg:bfsg-produktkonformitaet
Import von Zahlungsterminals, Vertrieb unter eigener Marke seit November
2025, keine EU-Konformitätserklärung, CE nur auf dem Karton. Die Behörde
hat mit fünf Tagen Anhörungsfrist zur Stellungnahme aufgefordert. Wir
erhalten einen Landeszuschuss zur Barrierefreiheit. Bitte Stellungnahme.
```

### Szenario 3 – Verbandsantrag gegen einen Shop

```
/barrierefreiheit-bfsg:bfsg-dienstleistung-ecommerce
Prüfbericht weist Bezahlseite ohne Tastaturbedienbarkeit, Captcha ohne
Alternative und fehlende Textalternativen aus. In der Fußzeile steht nur
"Wir bemühen uns um Barrierefreiheit nach WCAG 2.1 AA". Ein anerkannter
Verband hat ein Verfahren beantragt und zugleich Schlichtung eingeleitet.
Bitte Bewertung, Maßnahmenplan und Entwurf der Barrierefreiheitsinformationen.
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Deutsche Normen werden mit gesetze-im-internet.de zitiert, EU-Rechtsakte mit ELI- oder CELEX-Fundstelle.

**Technische Normen sind keine Rechtsnormen.** EN 301 549 und die WCAG entfalten Wirkung nur über die Konformitätsvermutung des § 4 BFSG bzw. über § 3 BITV 2.0 und Anlage 2 — und nur in der jeweils im Amtsblatt der EU gelisteten Fassung. Der Fassungsstand ist vor Verwendung zu prüfen.

**Rechtsprechung:** Das BFSG ist erst seit dem 28.06.2025 anwendbar; eine gefestigte Judikatur existiert **nicht**. Zu §§ 12a ff. BGG gibt es nur vereinzelte Entscheidungen. Jede Entscheidung, die ein Modell zu diesen Normen nennt, ist als `[unverifiziert – prüfen]` zu behandeln, bis sie in juris oder Beck-Online belegt ist.

## Hinweise

- **Die Kleinstunternehmensausnahme des § 3 Abs. 3 BFSG gilt nur für Dienstleistungen.** Ein Kleinstunternehmen, das erfasste Produkte herstellt, einführt oder vertreibt, bleibt vollständig gebunden. Kleinstunternehmen ist nach § 2 Nr. 17 BFSG, wer **weniger als zehn** Personen beschäftigt **und** höchstens 2 Mio. EUR Umsatz **oder** Bilanzsumme aufweist.
- **§ 12 BFSG macht Händler und Einführer zu Herstellern**, sobald sie unter eigenem Namen oder eigener Marke in Verkehr bringen oder das Produkt konformitätsrelevant verändern.
- **Die Barrierefreiheitsinformationen nach Anlage 3 Nr. 1 BFSG haben vier Pflichtbestandteile** — die Angabe der zuständigen Marktüberwachungsbehörde (Buchst. d) fehlt in der Praxis fast immer.
- **§ 17 Abs. 4 BFSG sperrt die Berufung auf unverhältnismäßige Belastung**, wenn nichteigene öffentliche oder private Mittel zur Verbesserung der Barrierefreiheit bezogen wurden.
- **§ 4 BITV 2.0 verlangt Erläuterungen in Deutscher Gebärdensprache und in Leichter Sprache.** Diese Pflicht hat kein Gegenstück im BFSG und wird bei Übertragung privatwirtschaftlicher Konzepte auf Behördenauftritte regelmäßig übersehen.
- **Ob ein BFSG-Verstoß nach § 3a UWG abmahnfähig ist, ist ungeklärt.** Das Plugin behandelt die Frage als offen und kennzeichnet sie entsprechend.
- **Mandantengeheimnis (§ 43a Abs. 2 BRAO, § 203 StGB):** Prüfberichte und Nutzerrückmeldungen können personenbezogene Daten enthalten; keine Verarbeitung ohne AVV und Pseudonymisierung (`scripts/pii_redact.py`).
