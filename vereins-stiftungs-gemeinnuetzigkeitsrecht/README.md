# Vereins-, Stiftungs- und Gemeinnützigkeitsrecht

**Production-grade Non-Profit-Skills für Claude / Gemini / GPT.** Rund 615.000 eingetragene Vereine und etwa 26.000 rechtsfähige Stiftungen — ein stark templatisiertes Rechtsgebiet, in dem formale Fehler unmittelbar steuerliche Folgen haben. Vereinsrecht (§§ 21–79 BGB), das seit 01.01.2023 bundeseinheitliche Stiftungsrecht (§§ 80–88 BGB), Gemeinnützigkeit (§§ 51–68 AO) und Spendenrecht (§ 10b EStG). Researcher → Drafter → Reviewer.

> Abgrenzung: Das steuerliche **Verfahrensrecht** (Einspruch, Betriebsprüfung, Selbstanzeige) liegt im Plugin `steuerrecht`; gesellschaftsrechtliche Fragen der gGmbH in `gesellschaftsrecht`. Dieses Plugin geht **in die Tiefe** für Satzungsgestaltung, Statuserhalt und die Haftung der Handelnden.

## Skills

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `vereinsgruendung-satzung` | Gründung, Satzungsgestaltung, Registeranmeldung, Organverfassung und Beschlussmängel des eingetragenen Vereins | §§ 21, 22 BGB (Nebenzweckprivileg); §§ 26, 30, 31, 31a, 31b BGB; §§ 32, 33, 36, 37 BGB; §§ 56–60, 64, 67, 71, 77, 78 BGB |
| `stiftungsrecht-2023` | Errichtung, Vermögensverwaltung, Organhaftung, Satzungsänderung und Umstrukturierung nach der Reform | §§ 80, 81, 82, 82a BGB; §§ 83b, 83c BGB; §§ 84, 84a, 84b BGB; § 85 BGB; §§ 86–86b, 87–87c BGB; StiftRG |
| `gemeinnuetzigkeit-ao` | Statusprüfung und -sicherung: Satzung gegen die Mustersatzung, Sphärenzuordnung, Mittelverwendung, Rücklagen | §§ 52–58 AO; § 60 AO und Anlage 1; §§ 60a, 61, 62, 63, 64 AO; §§ 65–68 AO; § 5 Abs. 1 Nr. 9 KStG |
| `spendenrecht-haftung` | Zuwendungsbestätigung, Sach- und Aufwandsspende, Sponsoring-Abgrenzung, Aussteller- und Veranlasserhaftung | § 10b Abs. 1, 1a, 3, 4 EStG; § 9 Nr. 5 GewStG; § 9 Abs. 1 Nr. 2 KStG; §§ 60a, 60b AO; § 50 EStDV |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: BGB Vereins- und Stiftungsrecht, AO §§ 51–68 mit Anlage 1, EStG, KStG, GewStG, AEAO und BMF-Schreiben (stets als Verwaltungsauffassung gekennzeichnet)
- [`agents/drafter.md`](./agents/drafter.md) – Satzungen, Stiftungsgeschäfte, Anträge nach § 60a AO, Registeranmeldungen, Gutachten und Verteidigungsschriften
- [`agents/reviewer.md`](./agents/reviewer.md) – Satzungs-, Frist-, Status- und Haftungs-Check (Anlage 1 zu § 60 AO Baustein für Baustein, Vermögensbindung § 61 Abs. 3 AO, zeitnahe Mittelverwendung, Betragsgrenzen)

## Installation

### Claude Code
```bash
# Über Marketplace (empfohlen)
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install vereins-stiftungs-gemeinnuetzigkeitsrecht
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area vereins-stiftungs-gemeinnuetzigkeitsrecht --out dist/gemini
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area vereins-stiftungs-gemeinnuetzigkeitsrecht --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Vereinsgründung mit Geschäftsbetrieb

```
/vereins-stiftungs-gemeinnuetzigkeitsrecht:vereinsgruendung-satzung
Neun Personen gründen einen Sportverein, der zugleich eine Vereinsgaststätte
und einen Fanartikelhandel betreiben soll. Bitte Prüfung des
Nebenzweckprivilegs nach §§ 21, 22 BGB, Mindest- und Sollinhalt der Satzung,
Vertretungsregelung nach § 26 BGB und Form der Anmeldung nach § 77 BGB.
```

### Szenario 2 – Stiftung in Ertragsnot

```
/vereins-stiftungs-gemeinnuetzigkeitsrecht:stiftungsrecht-2023
Eine 2004 errichtete Stiftung erwirtschaftet keine ausreichenden Erträge mehr.
Der Vorstand hat Teile des Grundstockvermögens verbraucht und
Umschichtungsgewinne ausgeschüttet. Bitte Prüfung nach §§ 83b, 83c BGB, der
Haftung nach § 84a Abs. 2 BGB, der Stufen des § 85 BGB und der Zulegung nach
§ 86 BGB.
```

### Szenario 3 – Betriebsprüfung beim gemeinnützigen Verein

```
/vereins-stiftungs-gemeinnuetzigkeitsrecht:gemeinnuetzigkeit-ao
Verein mit EUR 480.000 Jahreseinnahmen, EUR 61.000 aus Gaststätte und
Bandenwerbung, EUR 210.000 nicht verwendete Spenden aus 2022/2023, ohne
Rücklagenbeschluss. Vermögensbindungsklausel lautet nur "an gemeinnützige
Zwecke". Bitte Sphärenzuordnung, Mittelverwendungsrechnung, Rücklagenprüfung
nach § 62 AO und Bewertung des Entzugsrisikos nach § 61 Abs. 3 AO.
```

## Rechner

Fristen (zeitnahe Mittelverwendung, Rücklagenbildung und -auflösung, Ladungsfristen, Rechtsbehelfsfristen) rechnet der deterministische Fristenrechner:

```bash
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 1 --einheit monate --land BY
```

Er leistet **nur** die Arithmetik der §§ 187–193 BGB. **Fristbeginn und Zugang bleiben rechtliche Eingaben.** Siehe [`../references/rechner.md`](../references/rechner.md).

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Standardliteratur: **Hüttemann**, Gemeinnützigkeits- und Spendenrecht; **Seer** in Tipke/Kruse; **Leuschner** und **Weitemeyer** in MüKoBGB; **Hüttemann/Rawert** in Staudinger; **Ellenberger** in Grüneberg; **Sauter/Schweyer/Waldner**, Der eingetragene Verein; **Burgard**, Gestaltungsfreiheit im Stiftungsrecht.

**AEAO und BMF-Schreiben sind Verwaltungsauffassung** — für die Finanzämter bindend, für die Gerichte nicht. Sie werden in den Skills stets als solche gekennzeichnet, und ihre Fassung ist vor Verwendung zu prüfen. Unverifizierte Zitate tragen `[unverifiziert - prüfen]`; `[generiert]` ist im gesamten Repository verboten.

## Hinweise

- **Die Mustersatzung der Anlage 1 zu § 60 AO ist formstreng.** § 60 Abs. 1 S. 2 AO verlangt ihre Festlegungen; ein fehlender Baustein führt zur Ablehnung der Feststellung nach § 60a AO. Die Bausteine werden übernommen, nicht umformuliert.
- **§ 61 Abs. 3 AO ist die schärfste Sanktion des Gebiets.** Eine nachträglich unzureichende Vermögensbindung gilt von Anfang an als nicht ausreichend und eröffnet die Nachversteuerung für zehn Kalenderjahre.
- **Betragsgrenzen ändern sich.** Besteuerungsgrenze § 64 Abs. 3 AO, Einnahmegrenze für die Befreiung von der zeitnahen Mittelverwendung § 55 Abs. 1 Nr. 5 S. 4 AO, Vergütungsgrenze § 31a BGB und die Höchstbeträge des § 10b EStG sind vor jeder Auskunft gegen den amtlichen Wortlaut zu prüfen. Die Skills nennen die geltenden Werte mit Fundstelle und warnen ausdrücklich vor veralteten Beträgen.
- **Stiftungsregister (StiftRG).** Der operative Stand des Registers, der Beginn der Eintragungspflicht und die Publizitätswirkung sind gesondert in der amtlichen Fassung zu prüfen und in den Skills mit `[unverifiziert - prüfen]` gekennzeichnet.
- **Spendenhaftung.** § 10b Abs. 4 S. 3 EStG setzt die entgangene Steuer mit 30 Prozent an, § 9 Nr. 5 S. 16 GewStG mit weiteren 15 Prozent. Bei der Ausstellerhaftung gibt es keine Vorrangregel zugunsten der Körperschaft — der Ausstellende haftet unmittelbar.
- **Nicht privilegierte Haftung.** §§ 31a, 31b BGB und § 84a BGB schützen nicht vor § 69 AO (nicht abgeführte Steuern) und § 266a StGB (vorenthaltene Arbeitnehmerbeiträge).
- **Mandantengeheimnis (§ 43a Abs. 2 BRAO, § 203 StGB):** Mitglieder-, Spender- und Destinatärsdaten nur in Werkzeuge mit Auftragsverarbeitungsvertrag. Steuerliche Aussagen ersetzen keine Steuerberatung (StBerG beachten).
