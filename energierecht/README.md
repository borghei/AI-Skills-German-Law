# Energierecht

**Production-grade Energierechts-Skills für Claude / Gemini / GPT.** Deutsches Energierecht aus Beratungs- und Behördenperspektive: EnWG (Netzzugang, Entflechtung, BNetzA-Aufsicht), EEG (Förderung erneuerbarer Energien), KWKG, GEG, EnEfG/EDL-G sowie die einschlägigen unionsrechtlichen Vorgaben (RL (EU) 2019/944, VO (EU) 2019/943, RED III). Researcher → Drafter → Reviewer.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `enwg-netzanschluss` | Anschluss- und Versorgungsanspruch, Netzanschluss EEG-Anlagen, Konfliktfälle und BNetzA-Beschlussverfahren | §§ 17, 18 EnWG; §§ 8, 10, 12 EEG; §§ 31 ff. EnWG; NAV/NDAV |
| `eeg-foerderpruefung` | Marktprämie / Einspeisevergütung – Anspruchsvoraussetzungen, Inbetriebnahme, MaStR-Meldung, anzulegender Wert, Reduktionen | §§ 19 ff., 21b, 22, 27/27a, 36 ff., 49 ff., 51 EEG; § 8 MaStRV |
| `energieeffizienzpflicht` | EnMS-/UMS-Pflicht nach EnEfG ab 7,5 GWh/a, Energieaudit nach EDL-G für Nicht-KMU, BAFA-Nachweis, Schnittstelle GEG/CSRD | § 8 EnEfG; § 8 EDL-G; GEG; CSRD/ESRS E1 |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: EnWG, EEG, KWKG, GEG, EnEfG, EDL-G, NAV/NDAV, EU-Recht, BNetzA-Festlegungen, BGH-KZR und OLG-Düsseldorf-Vergabesenat
- [`agents/drafter.md`](./agents/drafter.md) – Entwurf in Gutachten- oder Behördenstil mit Verweis auf BNetzA-Verfahrensregeln
- [`agents/reviewer.md`](./agents/reviewer.md) – Risiko-, Frist- und Berufsrechts-Check (insb. IBN-Datum, MaStR-Meldung, BImSchG-Genehmigungsstatus, BNetzA-Anhörung § 67 EnWG)

## Installation

### Claude Code
```bash
# Über Marketplace (empfohlen)
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install energierecht

# Oder als ZIP
# Claude Code → Customize Plugins → Install from .zip → energierecht.zip
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area energierecht --out dist/gemini
# Inhalt der erzeugten Dateien in neue Gemini-Gems einfügen
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area energierecht --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Netzanschluss einer Freiflächen-PV-Anlage

```
/energierecht:enwg-netzanschluss
Mandantin (Projektentwicklerin Freiflächen-PV 12 MWp) hat Netzanschluss
beim örtlichen Verteilnetzbetreiber beantragt. Der VNB verweist auf
fehlende Kapazität und verlangt eine Wartezeit von 36 Monaten ohne
verbindlichen Realisierungsplan. Bitte prüfen, ob Anschlussanspruch
nach §§ 8, 12 EEG iVm § 17 EnWG besteht, Netzausbaupflicht, und
BNetzA-Beschlussverfahren §§ 31 ff. EnWG vorbereiten.
```

### Szenario 2 – EEG-Förderung einer Windenergieanlage

```
/energierecht:eeg-foerderpruefung
Mandantin (Windpark-Betreiberin, 6 WEA á 4,2 MW) hat im
Ausschreibungsverfahren BNetzA einen Zuschlag erhalten. Inbetriebnahme
geplant für 31.12. Streit um IBN-Datum (technische Betriebsbereitschaft
trotz fehlender 110-kV-Trafostation?) und Folgen für anzulegenden Wert
nach §§ 36 ff. EEG. Bitte Förderanspruch prüfen.
```

### Szenario 3 – Energieaudit-Pflicht eines Mittelständlers

```
/energierecht:energieeffizienzpflicht
Mandantin (Industrieunternehmen, ca. 600 MA, ca. 9 GWh/a Endenergie,
nicht KMU iSd KMU-Empfehlung) prüft Pflichten nach EnEfG / EDL-G.
Frage: EnMS- oder UMS-Pflicht nach § 8 EnEfG? Energieaudit nach
§ 8 EDL-G? Schnittstelle zur CSRD-Berichtspflicht E1. Bitte Übersicht
plus Nachweisführung gegenüber BAFA.
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Standardkommentare: **Säcker**, BerlinerKommentar Energierecht (EnWG/EEG); **Theobald/Kühling**, Energierecht (Loseblatt); **Britz/Hellermann/Hermes**, EnWG; **Frenz/Müggenborg**, EEG.

Rechtsprechung: BGH (KZR-Senat für energiekartellrechtliche Vor- und Folgenseite), BVerwG, OLG Düsseldorf (Vergabesenat / Beschwerdesenat gegen BNetzA-Entscheidungen), BNetzA-Beschlüsse und Festlegungen. Format: `OLG Düsseldorf, Beschl. v. TT.MM.JJJJ – VI-3 Kart Az., RdE Jahr, Seite`. Unverifizierte Zitate werden mit `[unverifiziert – prüfen]` markiert; BNetzA-Beschlüsse sind in der Beschlusskammer-Datenbank (bundesnetzagentur.de) zu verifizieren.

## Hinweise

- **Abgrenzung Energiekartellrecht.** Marktmissbrauchs- und Kartellrechtsfragen (§§ 19, 29 GWB iVm § 30 EnWG) bleiben dem Plugin `kartellrecht` vorbehalten. Die hier angelegten Skills adressieren ausschließlich das Regulierungs- und Förderrecht.
- **IBN-Datum und MaStR-Meldung sind die häufigsten Förderkiller.** Vor jeder förderrechtlichen Beratung müssen technische Betriebsbereitschaft iSd § 3 Nr. 30 EEG und die Eintragung im Marktstammdatenregister (§ 8 MaStRV) belegt sein.
- **BNetzA-Beschlüsse binden im konkreten Verfahren** (§ 73 EnWG); Beschwerde zum OLG Düsseldorf ist statthaft (§ 75 EnWG). Eine darüber hinausgehende Präjudizienbindung besteht nicht – aber Festlegungen entfalten faktisch Steuerungswirkung.
- **Übergangsmaßnahmen (Strompreisbremse, Gaspreisbremse)** sind in 2024 ausgelaufen oder modifiziert worden. Jeder Bezug darauf in einem Skill-Output ist mit `[unverifiziert – aktuelle Geltung prüfen]` zu markieren.
- **BImSchG-Schnittstelle.** Errichtung von Wind- und Großanlagen erfordert immissionsschutzrechtliche Genehmigung (§§ 4, 10 BImSchG); EEG-Förderfragen setzen den Genehmigungsstatus voraus, ersetzen ihn aber nicht.
- **Mandatsgeheimnis (§ 43a BRAO, § 203 StGB):** Keine echten Mandatsdaten ohne § 203-konformen Gateway.
