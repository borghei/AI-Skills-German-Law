# Datenwirtschaftsrecht

**Production-grade Data-Act-Skills für Claude / Gemini / GPT.** Zugangsansprüche an Produktdaten, Datenlizenzverträge, Cloud-Exit und behördlicher Datenzugang — aus der Perspektive der Beratungspraxis. Researcher → Drafter → Reviewer.

> **Der gestaffelte Geltungsbeginn ist das strukturelle Fehlerrisiko dieses Rechtsgebiets.** Die Datenverordnung ([VO (EU) 2023/2854](https://eur-lex.europa.eu/eli/reg/2023/2854/oj)) gilt seit dem **12.09.2025**. Die Konzeptionspflicht des Art. 3 Abs. 1 greift jedoch erst für vernetzte Produkte und verbundene Dienste, die **nach dem 12.09.2026** in Verkehr gebracht werden. Die Missbrauchskontrolle des Kapitels IV erfasst Altverträge erst ab dem **12.09.2027**. Wechselentgelte für Datenverarbeitungsdienste entfallen erst ab dem **12.01.2027**. Jede Skill dieses Plugins macht die Prüfung nach Art. 50 deshalb zu einem eigenen Schritt.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `data-act-anwendungsbereich` | Betroffenheit, Rollenzuordnung je Datenstrom, Größenausnahme, Geltungsbeginn, Zuständigkeit und Sanktionsrahmen | Art. 1, 2, 3, 4, 5, 7, 13, 43, 50 Data Act; §§ 2, 6, 15, 16 DADG; Art. 6 DSGVO; § 2 GeschGehG |
| `data-act-nutzerdatenzugang` | Zugangsverlangen des Nutzers, Weitergabe an Dritte, Geschäftsgeheimnisverfahren, Verweigerung und Meldepflichten | Art. 3, 4, 5, 6, 10, 11, 38, 39 Data Act; §§ 2, 5, 6, 15 DADG; Art. 3 DMA |
| `data-act-vertragsklauseln` | Bereitstellungsbedingungen, Berechnung der Gegenleistung, Missbrauchskontrolle einseitig auferlegter Klauseln, Verhältnis zur AGB-Kontrolle | Art. 7 Abs. 2, 8, 9, 10, 12, 13, 41, 50 Data Act; §§ 305–310, 195 BGB; § 5 DADG |
| `cloud-anbieterwechsel` | Exit-Fahrplan für Datenverarbeitungsdienste, zwingender Klauselkatalog, Wechselentgelte, Funktionsäquivalenz | Art. 23–32, 34, 35 Data Act; §§ 2, 6, 15 DADG; Art. 28, 30 DORA |
| `datenzugang-oeffentliche-stellen` | Behördliches Datenverlangen: außergewöhnliche Notwendigkeit, Formprüfung, Ablehnungsfristen, Ausgleich; dazu DGA-Intermediäre | Art. 14–22 Data Act; §§ 2, 6, 15 DADG; VO (EU) 2022/868; §§ 2, 7, 8, 10 DGG; DNG |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: Data Act, DADG, DGA, DGG, DNG, DSGVO, DMA, DORA, Erwägungsgründe, Kommissionsleitlinien, BNetzA-Verlautbarungen
- [`agents/drafter.md`](./agents/drafter.md) – Entwürfe: Betroffenheitsanalyse, Antwort auf Zugangs- und Behördenverlangen, Klauselmatrix mit Alternativfassungen, Exit-Fahrplan
- [`agents/reviewer.md`](./agents/reviewer.md) – Regime-, Fristen-, Rollen- und Quellencheck (insbesondere Art. 50, Arbeitstage gegen Kalendertage, Kennzeichnung von Geschäftsgeheimnissen)

## Installation

### Claude Code
```bash
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install datenwirtschaftsrecht
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area datenwirtschaftsrecht --out dist/gemini
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area datenwirtschaftsrecht --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Betroffenheit eines Maschinenbauers

```
/datenwirtschaftsrecht:data-act-anwendungsbereich
Mandantin ist Herstellerin vernetzter Landmaschinen, 180 Beschäftigte,
Konzerntochter einer Holding mit 4.000 Beschäftigten. Eine neue Baureihe
kommt im Oktober 2026 auf den Markt; die Wartungsverträge stammen aus 2021
und sind unbefristet. Frage: Greift die Größenausnahme, ab wann gilt die
Konzeptionspflicht, ab wann die Klauselkontrolle?
```

### Szenario 2 – Zugangsverlangen abwehren oder erfüllen

```
/datenwirtschaftsrecht:data-act-nutzerdatenzugang
Ein Flottenbetreiber verlangt Telemetrie- und Fehlerspeicherdaten und
deren Weitergabe an eine freie Werkstattkette, die zu einem benannten
Torwächter gehört. Wir liefern bislang nur PDF-Reports und halten die
Fehlercode-Tabelle für ein Geschäftsgeheimnis. Bitte Antwortentwurf.
```

### Szenario 3 – Cloud-Exit mit Egress-Entgelten

```
/datenwirtschaftsrecht:cloud-anbieterwechsel
IaaS-Vertrag mit sechsmonatiger Kündigungsfrist, zehn Tagen Datenabruf,
ohne Löschklausel und mit Egress-Entgelten von rund 38.000 EUR. Der
Anbieter beruft sich auf eine Ausnahme für maßgeschneiderte Dienste.
Bitte Klauselabgleich nach Art. 25 und Exit-Fahrplan.
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). EU-Rechtsakte werden mit ELI- oder CELEX-Fundstelle zitiert, deutsche Normen mit gesetze-im-internet.de.

**Rechtsprechung:** Zum Data Act und zum Daten-Governance-Rechtsakt existiert bislang **keine gefestigte Judikatur**. Das Plugin arbeitet deshalb bewusst mit Normtext, Erwägungsgründen, Kommissionsleitlinien und Verlautbarungen der Bundesnetzagentur. Jede Entscheidung, die ein Modell zu diesen Rechtsakten nennt, ist als `[unverifiziert – prüfen]` zu behandeln, bis sie in juris, Beck-Online oder curia.europa.eu belegt ist.

## Hinweise

- **Zuständige Behörde ist die Bundesnetzagentur** ([§ 2 Abs. 1 DADG](https://www.gesetze-im-internet.de/dadg/__2.html)) — nicht die Datenschutzaufsicht. Für Geldbußen mit Bezug zu personenbezogenen Daten ist nach [§ 16 DADG](https://www.gesetze-im-internet.de/dadg/__16.html) die oder der BfDI zuständig.
- **Der Data Act ist keine Rechtsgrundlage nach Art. 6 DSGVO.** Beide Regime sind nebeneinander zu prüfen; ist der Nutzer nicht die betroffene Person, verlangt Art. 5 Abs. 7 eine eigenständige Rechtsgrundlage.
- **Geschäftsgeheimnisse werden prozeduralisiert, nicht aufgehoben.** Art. 4 Abs. 6 ff. verlangt Kennzeichnung und vereinbarte Schutzmaßnahmen; die Verweigerung ist die begründungs- und meldepflichtige Ausnahme.
- **Art. 43 sperrt den sui-generis-Datenbankschutz** für Datenbanken, die Produktdaten oder verbundene Dienstdaten enthalten. Die Berufung auf §§ 87a ff. UrhG trägt insoweit nicht.
- **Fristenarithmetik:** Art. 18 Abs. 2 rechnet in **Arbeitstagen** (5 bzw. 30), Art. 25 Abs. 2 in **Kalendertagen** (30). Der Rechner unter [`../scripts/legal_calc/`](../scripts/legal_calc/) unterscheidet beides und berücksichtigt Landesfeiertage.
- **Mandantengeheimnis (§ 43a Abs. 2 BRAO, § 203 StGB):** Telemetrie- und Kundendaten können personenbezogen sein; keine Verarbeitung ohne AVV und Pseudonymisierung (`scripts/pii_redact.py`).
