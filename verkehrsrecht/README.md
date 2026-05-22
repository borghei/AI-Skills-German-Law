# Verkehrsrecht

**Production-grade Verkehrsrechts-Skills für Claude / Gemini / GPT.** Deutsches Straßenverkehrsrecht in drei Säulen: zivilrechtliche Haftung, verwaltungsrechtliche Fahreignung, Verkehrs-OWi mit Schnittstelle zum Verkehrsstrafrecht. Researcher → Drafter → Reviewer.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `stvg-haftungspruefung` | Halter- und Fahrerhaftung nach Verkehrsunfall mit Quotelung und Schadensbezifferung | §§ 7, 17, 18 StVG; §§ 823, 249–254 BGB; § 115 VVG; PflVG |
| `mpu-anordnung-pruefung` | Rechtmäßigkeitsprüfung einer MPU-Anordnung und Entwurf Widerspruch/Klage | §§ 11, 13, 14, 46 FeV; § 3 StVG; § 80 V VwGO; § 74 VwGO |
| `ordnungswidrigkeit-stvo` | Prüfung Bußgeldbescheid, Einspruch, Fahrverbot, Messverfahren | §§ 24, 25 StVG; StVO; BKatV; §§ 66, 67, 71 OWiG; § 26 III StVG |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: StVG, StVO, FeV, BKatV, BGH-VI-ZS- und OLG-Bußgeldsenat-Rechtsprechung, Standardkommentare
- [`agents/drafter.md`](./agents/drafter.md) – Erstellung im Gutachten- oder Urteilsstil (Haftungsgutachten, Widerspruchsbegründung, Einspruchsschriftsatz)
- [`agents/reviewer.md`](./agents/reviewer.md) – Risiko-, Frist- und Berufsrechts-Check (Einspruchsfrist § 67 OWiG, Verfolgungsverjährung § 26 III StVG, Klagefrist § 74 VwGO, Antragsfrist § 80 III VwGO)

## Installation

### Claude Code
```bash
# Über Marketplace (empfohlen)
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install verkehrsrecht

# Oder als ZIP
# Claude Code → Customize Plugins → Install from .zip → verkehrsrecht.zip
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area verkehrsrecht --out dist/gemini
# Inhalt der erzeugten Dateien in neue Gemini-Gems einfügen
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area verkehrsrecht --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Auffahrunfall mit Mitverschulden

```
/verkehrsrecht:stvg-haftungspruefung
Mandant fährt auf vorausfahrendes Fahrzeug auf, das nach eigener Angabe
ohne erkennbaren Grund stark abgebremst hat. Reparaturkosten brutto
8.400 EUR, Wiederbeschaffungswert 7.000 EUR. Bitte Haftungsquote nach
§ 17 StVG, 130%-Grenze und Nutzungsausfall prüfen.
```

### Szenario 2 – MPU-Anordnung nach Alkoholfahrt

```
/verkehrsrecht:mpu-anordnung-pruefung
Mandant wurde mit 1,7 ‰ BAK angehalten, Fahrerlaubnis strafgerichtlich
entzogen, Sperrfrist abgelaufen, Wiedererteilungsantrag gestellt.
Fahrerlaubnisbehörde ordnet MPU nach § 13 S. 1 Nr. 2 lit. c FeV an.
Bitte Rechtmäßigkeit der Anordnung prüfen und Widerspruchsbegründung
entwerfen.
```

### Szenario 3 – Bußgeldbescheid Geschwindigkeit + Fahrverbot

```
/verkehrsrecht:ordnungswidrigkeit-stvo
Mandantin (Außendienstmitarbeiterin) hat Bußgeldbescheid wegen
Überschreitung der zulässigen Höchstgeschwindigkeit außerorts um
42 km/h erhalten — Bußgeld, Punkte FAER, einmonatiges Fahrverbot.
Messverfahren PoliScan Speed M1. Bitte Einspruch prüfen, Absehen vom
Fahrverbot wegen beruflicher Härte (§ 4 IV BKatV) und Akteneinsicht
in Rohmessdaten.
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Standardkommentare: **Hentschel/König/Dauer**, Straßenverkehrsrecht (BeckOK); **Burmann/Heß/Hühnermann/Jahnke**, Straßenverkehrsrecht; **Janker/Burhoff**, Straßenverkehrsrecht-Handbuch; **Göhler**, OWiG; **Krenberger/Krumm**, OWiG.

Rechtsprechung: BGH VI. Zivilsenat (Verkehrshaftung), OLG-Bußgeldsenate, BVerwG / OVG (Fahrerlaubnisentziehung), BVerfG zu standardisierten Messverfahren — im Format `BGH, Urt. v. TT.MM.JJJJ – VI ZR NN/JJ, NJW JJJJ, Seite Rn. N`. Unverifizierte Zitate werden mit `[unverifiziert – prüfen]` markiert.

## Hinweise

- **Abgrenzung zu Versicherungsrecht.** KfZ-Versicherungsregress (Quoten- und Sachverständigenstreit zwischen Haftpflicht- und Kaskoversicherer, §§ 86 VVG, 116 SGB X) wird im Plugin `versicherungsrecht` behandelt. Hier nur die Direktansprüche gegen Halter, Fahrer und Pflichtversicherer (§ 115 VVG).
- **Schnittstelle Verkehrsstrafrecht.** Bei Anhaltspunkten für §§ 142, 222, 229, 315c, 316 StGB ist die OWi-Prüfung nicht abschließend — Verteidigungsstrategie ist mit dem strafrechtlichen Mandat abzustimmen (Doppelverfolgungsverbot, § 21 OWiG).
- **Punkte und FAER.** Konkrete Punkte- und Bußgeldzahlen folgen der jeweils gültigen Anlage zur BKatV (Bußgeldkatalog); der Stand der Anlage ist vor Auslieferung zu verifizieren. Der Skill nennt Punktezahlen nicht ohne Stand-Hinweis.
- **Standardisierte Messverfahren.** Die Rechtsprechung zur Akteneinsicht in Rohmessdaten ist im Fluss (BVerfG, OLG-Linie uneinheitlich). Belegstellen sind als `[unverifiziert – prüfen]` zu kennzeichnen.
- **Mandatsgeheimnis (§ 43a BRAO, § 203 StGB):** Keine echten Mandatsdaten ohne § 203-konformen Gateway.
