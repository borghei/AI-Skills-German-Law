# Europarecht

**Production-grade Europarechts-Skills für Claude / Gemini / GPT.** EU-Primär- und Sekundärrecht aus deutscher Praxisperspektive: AEUV, EUV, GRCh, EuGH-Verfahren, Wirkung von EU-Sekundärrecht in deutschen Verfahren. Researcher → Drafter → Reviewer.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `vorabentscheidung-art-267` | Vorlagepflicht und Entwurf der Vorlagefrage an den EuGH | Art. 267 AEUV; CILFIT/acte clair; Art. 101 I 2 GG |
| `vertragsverletzungsverfahren` | Reaktionsstrategie auf Mahnschreiben und Begründete Stellungnahme der Kommission | Art. 258–260 AEUV; Art. 4 Abs. 3 EUV; Art. 23d Abs. 5 GG |
| `eu-richtlinien-umsetzungspruefung` | Prüfung von Umsetzung, unmittelbarer Wirkung, RL-konformer Auslegung, Francovich-Haftung | Art. 288 AEUV; Art. 4 Abs. 3 EUV; Marshall, Faccini Dori, von Colson, Francovich |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: Vertragsrecht, EuGH-Rechtsprechung, Kommentarliteratur
- [`agents/drafter.md`](./agents/drafter.md) – Erstellung im Gutachten- oder Urteilsstil mit Verweis auf EuGH-Verfahrensregeln
- [`agents/reviewer.md`](./agents/reviewer.md) – Risiko-, Frist- und Berufsrechts-Check (inkl. Anwendungsbereich GRCh, Vorlagepflicht-Falle)

## Installation

### Claude Code
```bash
# Über Marketplace (empfohlen)
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install europarecht

# Oder als ZIP
# Claude Code → Customize Plugins → Install from .zip → europarecht.zip
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area europarecht --out dist/gemini
# Inhalt der erzeugten Dateien in neue Gemini-Gems einfügen
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area europarecht --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Vorlagepflicht in letzter Instanz

```
/europarecht:vorabentscheidung-art-267
Mandantin (mittelständischer Online-Händler) klagt gegen einen
Bescheid des BfArM. BVerwG ist letztinstanzlich. Streit dreht sich
um die Auslegung von Art. 6 der EU-VO 2017/745 (MDR). Bitte prüfen,
ob Vorlagepflicht nach Art. 267 III AEUV besteht oder acte
clair/éclairé greift, und Vorlagefrage entwerfen.
```

### Szenario 2 – Mahnschreiben der Kommission an die Bundesrepublik

```
/europarecht:vertragsverletzungsverfahren
Bundesland hat eine EU-Richtlinie zur Luftqualität verspätet
umgesetzt. KOM hat Mahnschreiben verschickt (Art. 258 AEUV). Bitte
Reaktionsstrategie, Fristen, Beteiligung des Bundes nach Art. 23d
GG, und Risiko von Zwangsgeld/Pauschalbetrag nach Art. 260 II AEUV
einschätzen.
```

### Szenario 3 – Unmittelbare Wirkung einer nicht umgesetzten RL

```
/europarecht:eu-richtlinien-umsetzungspruefung
Umsetzungsfrist einer EU-Richtlinie zum Verbraucherschutz ist seit
6 Monaten abgelaufen, DE hat nicht umgesetzt. Mandant (Verbraucher)
will sich vor dem Amtsgericht direkt auf RL-Bestimmung berufen.
Bitte prüfen: unmittelbare Wirkung (vertikal/horizontal),
richtlinienkonforme Auslegung, Francovich-Haftung gegen die BRD.
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Standardkommentare: **Calliess/Ruffert** EUV/AEUV, **Grabitz/Hilf/Nettesheim**, **von der Groeben/Schwarze/Hatje**, **Jarass** GRCh, **Streinz** EUV/AEUV.

Rechtsprechung: EuGH, EuG, BVerfG, BVerwG, BGH im Format `EuGH, Urt. v. TT.MM.JJJJ – Rs. C-NN/JJ, ECLI:EU:C:JJJJ:NNN Rn. N`. Unverifizierte Zitate werden mit `[unverifiziert – prüfen]` markiert; EuGH-Entscheidungen sind in curia.europa.eu zu verifizieren.

## Hinweise

- **Anwendungsbereich der GRCh (Art. 51 I).** Charta gilt nur, soweit Mitgliedstaaten Unionsrecht durchführen. Nicht bei rein nationalem Sachverhalt.
- **Vorlagepflicht ist nicht optional.** Verstoß durch letztinstanzliches Gericht ist Verletzung des gesetzlichen Richters (Art. 101 I 2 GG) – BVerfG-Beschwerde möglich.
- **Keine Präjudizienbindung deutscher Gerichte** außer § 31 BVerfGG; EuGH-Urteile binden gem. Art. 260 AEUV im konkreten Verfahren und gelten faktisch erga omnes für die ausgelegte Norm.
- **Mandatsgeheimnis (§ 43a BRAO, § 203 StGB):** Keine echten Mandatsdaten ohne § 203-konformen Gateway.
