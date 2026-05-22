# Umweltrecht

**Production-grade Umweltrechts-Skills für Claude / Gemini / GPT.** Tested workflows, primary-source citations, Researcher → Drafter → Reviewer sub-agents.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `bimschg-genehmigungsverfahren` | Vollprüfung Genehmigungsbedürftigkeit, Verfahrensart und materielle Voraussetzungen einer Industrieanlage | §§ 4–7, 10, 17, 20 BImSchG; 4. und 9. BImSchV; TA Luft, TA Lärm; IE-RL 2010/75/EU |
| `krwg-abfallrechtliche-pruefung` | Abfallbegriff, Hierarchie, Getrennthaltung, Anzeige- und Erlaubnispflichten, Überwachung | §§ 3, 6, 14, 17, 23, 47, 53, 54 KrWG; AbfRRL 2008/98/EG |
| `uvp-verfahrenspruefung` | UVP-Pflicht (Anlage 1, Vorprüfung), Verfahrensschritte, Verfahrensfehler-Folgen | §§ 5, 7, 15, 18, 25 UVPG; § 4 UmwRG; UVP-RL 2011/92/EU |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: Statute, Kommentare, BVerwG-/EuGH-Rechtsprechung
- [`agents/drafter.md`](./agents/drafter.md) – Erstellung im Gutachten- oder Urteilsstil
- [`agents/reviewer.md`](./agents/reviewer.md) – Verfahrens-, Frist- und EU-Recht-Check

## Installation

### Claude Code
```bash
# Über Marketplace (empfohlen)
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install umweltrecht

# Oder als ZIP
# Claude Code → Customize Plugins → Install from .zip → umweltrecht.zip
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area umweltrecht --out dist/gemini
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area umweltrecht --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Errichtung einer Tierhaltungsanlage

```
/umweltrecht:bimschg-genehmigungsverfahren
Mandantin plant Mastanlage mit 2.000 Mastschweinen am Standort Niedersachsen.
Bitte Genehmigungsbedürftigkeit nach 4. BImSchV (Nr. 7.1) prüfen,
Verfahrensart (förmlich vs. vereinfacht) und Pflicht zur
Öffentlichkeitsbeteiligung § 10 BImSchG / 9. BImSchV einordnen.
```

### Szenario 2 – Behördliche Anordnung zur Abfalltrennung

```
/umweltrecht:krwg-abfallrechtliche-pruefung
Industriebetrieb hat Anordnung der unteren Abfallbehörde nach § 47 KrWG
erhalten, gemischte gewerbliche Siedlungsabfälle entgegen § 14 KrWG
nicht getrennt zu halten. Bitte Anordnung auf Rechtmäßigkeit prüfen und
Verhältnismäßigkeit der Sanktion bewerten.
```

### Szenario 3 – UVP-Vorprüfung Windenergie

```
/umweltrecht:uvp-verfahrenspruefung
Vorhabenträger plant Windpark mit 18 Anlagen Gesamthöhe je 230 m.
Bitte UVP-Pflicht prüfen (UVPG Anlage 1 Nr. 1.6), Vorprüfung des
Einzelfalls § 7 UVPG durchführen und Rechtsfolgen einer unterbliebenen
Vorprüfung nach § 4 UmwRG erläutern.
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Standardkommentare: **Jarass BImSchG**, **Landmann/Rohmer Umweltrecht** (Loseblatt), **Schink/Versteyl KrWG**, **Czychowski/Reinhardt WHG**, **Lütkes/Ewer BNatSchG**, **Hoppe/Beckmann UVPG**.

Rechtsprechung: BVerwG, EuGH, BVerfG im Format `BVerwG, Urt. v. TT.MM.JJJJ – Az., NVwZ JJJJ, Seite Rn. N`. Unverifizierte Zitate werden mit `[unverifiziert – prüfen]` markiert.

## Hinweise

- **Vorhabenstandort entscheidet.** Schutzgebiete (FFH, Vogelschutz, Wasserschutz), Bauleitplanung, Landesimmissionsschutzrecht und Zuständigkeit variieren je Bundesland. Bitte mit Genehmigungsbescheid und Lageplan abgleichen.
- **EU-Vorgaben sind tragend.** IE-RL, UVP-RL, FFH-RL und Vogelschutz-RL überlagern nationales Recht; richtlinienkonforme Auslegung ist Pflicht.
- **Verbandsklage (§ 64 BNatSchG, § 2 UmwRG)** verschiebt Klagebefugnis – Drittschutz-Argumentation immer mitprüfen.
- **Mandatsgeheimnis (§ 43a BRAO, § 203 StGB):** Keine echten Mandatsdaten ohne § 203-konformen Gateway. Siehe [`../references/gateway-setup.md`](../references/gateway-setup.md).
