# Kapitalmarktrecht

**Production-grade Kapitalmarktrechts-Skills für Claude / Gemini / GPT.** Deutsches Kapitalmarktrecht im engeren Sinne aus Emittenten- und Marktteilnehmer-Sicht: WpHG/MAR (Marktmissbrauch, Insiderhandel, Ad-hoc-Publizität, Directors' Dealings, Stimmrechtsmeldungen), Prospekt-VO 2017/1129 iVm WpPG, WpÜG (Übernahmeangebote). Researcher → Drafter → Reviewer.

> **Abgrenzung zu `bankrecht`.** Dieses Plugin deckt das **Wertpapier- und Emittentenrecht** ab. Aufsichtsrechtliche Tiefe zum **Kreditgeschäft (KWG)**, Verbraucherdarlehen, Bauspar- und Kontoführungsverträge bleibt im Plugin [`bankrecht`](../bankrecht/README.md). Bei Schnittstellen (z. B. Wertpapierdienstleistung nach §§ 63 ff. WpHG, die zugleich KWG-erlaubnispflichtige Tätigkeit ist) wird auf `bankrecht` verwiesen.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `wphg-marktmissbrauch` | Insiderhandel, Marktmanipulation, Ad-hoc-Publizität, Insiderliste, Directors' Dealings | MAR VO (EU) 596/2014 Art. 7, 8, 14, 15, 17, 18, 19, 30; §§ 38, 119 WpHG |
| `prospektpflicht-pruefung` | Trigger und Ausnahmen der Prospektpflicht, BaFin-Billigung, Prospekthaftung | VO (EU) 2017/1129 Art. 1, 3, 6, 7, 11, 23; §§ 3, 9–11 WpPG |
| `wpueg-uebernahmeangebot` | Pflichtangebot ab 30 % Stimmrechte, Acting in concert, Mindestpreis, Verhaltenspflichten Zielgesellschaft, Squeeze-out | §§ 10, 11, 14 ff., 27, 29, 30, 31, 33, 35, 37, 39a, 39b WpÜG |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: MAR/WpHG/WpÜG/Prospekt-VO, EuGH/BGH-Rspr., BaFin-Praxis, Standardkommentare (Assmann/Schneider/Mülbert, Klöhn, Schwark/Zimmer)
- [`agents/drafter.md`](./agents/drafter.md) – Erstellung im Gutachten- oder Urteilsstil mit Kapitalmarkt-Frist-Logik (Ad-hoc unverzüglich, BaFin 10/20/30 WT, WpÜG-Annahmefrist)
- [`agents/reviewer.md`](./agents/reviewer.md) – Risiko-, Frist- und Berufsrechts-Check (BLOCKER: Aufschub Ad-hoc ohne Dokumentation, Pflichtangebot-Umgehung)

## Installation

### Claude Code
```bash
# Über Marketplace (empfohlen)
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install kapitalmarktrecht

# Oder als ZIP
# Claude Code → Customize Plugins → Install from .zip → kapitalmarktrecht.zip
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area kapitalmarktrecht --out dist/gemini
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area kapitalmarktrecht --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Ad-hoc-Aufschub bei laufendem M&A-Prozess

```
/kapitalmarktrecht:wphg-marktmissbrauch
Vorstand einer börsennotierten AG verhandelt mit einem strategischen
Investor über die Veräußerung eines wesentlichen Geschäftsbereichs.
Term Sheet liegt vor, Closing in 6 Wochen geplant. Bitte prüfen, ob
Insiderinformation iSv Art. 7 MAR vorliegt, ob Aufschub nach Art. 17
Abs. 4 MAR zulässig ist (berechtigtes Interesse, Geheimhaltung,
Irreführungsverbot), und Insiderliste-Pflichten Art. 18 MAR
adressieren.
```

### Szenario 2 – IPO-Prospekt für mittelständischen Emittenten

```
/kapitalmarktrecht:prospektpflicht-pruefung
Mandantin (deutsche AG, Familienunternehmen) plant Börsengang mit
Aufnahme der Aktien zum regulierten Markt (Prime Standard FWB).
Volumen ca. 120 Mio. EUR. Bitte Prüfung der Prospektpflicht nach
Art. 3 Prospekt-VO, Ausnahmenkatalog Art. 1 IV, BaFin-Billigungs-
verfahren (20 / 30 Werktage), Inhaltsanforderungen und
Prospekthaftungs-Risiken nach §§ 9–11 WpPG.
```

### Szenario 3 – Kontrollerwerb und Pflichtangebot

```
/kapitalmarktrecht:wpueg-uebernahmeangebot
Strategischer Investor erwirbt 28 % der Stimmrechte an einer börsen-
notierten Ziel-AG und schließt eine Stimmbindungsvereinbarung mit
einem weiteren 5 %-Aktionär. Bitte prüfen, ob ein Pflichtangebot nach
§ 35 iVm § 29 WpÜG ausgelöst ist (Zurechnung § 30 – Acting in
concert), Mindestpreis nach § 31 WpÜG iVm WpÜG-AngVO, sowie
Befreiungsantrag § 37 prüfen.
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Standardkommentare: **Assmann/Schneider/Mülbert** WpHG/MAR, **Klöhn** MAR, **Schwark/Zimmer** Kapitalmarktrechts-Kommentar (KapMRK), **Just/Voß/Ritz/Becker** WpHG, **Versteegen** Prospekt-VO, **Habersack/Mülbert/Schlitt** Unternehmensfinanzierung, **Angerer/Geibel/Süßmann** WpÜG.

Rechtsprechung: BGH II. Zivilsenat, EuGH (Geltl, Lafonta), OLG Frankfurt (WpÜG-Senat), BaFin-Sanktionsentscheidungen — unverifizierte Zitate werden mit `[unverifiziert – prüfen in juris/BaFin-Website]` markiert.

## Hinweise

- **MAR ist unmittelbar anwendbar.** Die Marktmissbrauchsverordnung (VO (EU) 596/2014) gilt seit 03.07.2016 direkt; nationale Regelungen des WpHG sind als Ausführungs- und Sanktionsrecht zu lesen — vorrangig sind die Tatbestände der MAR.
- **Ad-hoc unverzüglich, Aufschub dokumentiert.** Art. 17 IV MAR erlaubt Selbstaufschub nur bei berechtigtem Interesse + voraussichtlich keiner Irreführung + Vertraulichkeit. Dokumentation und nachgelagerte Mitteilung an BaFin sind Pflicht.
- **Pflichtangebot ist nicht verhandelbar.** § 35 WpÜG wird automatisch durch Kontrollerwerb (30 % Stimmrechte, § 29 II WpÜG, Zurechnung § 30) ausgelöst. Befreiung nur über § 37 WpÜG iVm WpÜG-BefreiV.
- **Prospekthaftung mit Frist.** §§ 9–11 WpPG: 1 Jahr ab Kenntnis, spätestens 3 Jahre ab Veröffentlichung (§ 11 WpPG); Rückabwicklungsanspruch nach Kursrückgang.
- **Mandatsgeheimnis (§ 43a BRAO, § 203 StGB):** Keine echten Mandatsdaten ohne § 203-konformen Gateway. Insiderinformationen sind zusätzlich nach Art. 10 MAR weitergabebeschränkt.
