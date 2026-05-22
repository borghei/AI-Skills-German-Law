# Transportrecht

**Production-grade Transportrechts-Skills für Claude / Gemini / GPT.** Deutsches Transportrecht aus Praxisperspektive – Schwerpunkt Straßengüterverkehr und multimodale Beförderung: HGB Frachtvertrag (§§ 407 ff.), Speditionsvertrag (§§ 453 ff.), Lagervertrag (§§ 467 ff.), CMR als innerstaatlich anwendbares Bundesrecht für grenzüberschreitende Beförderungen, ADSp 2017. Researcher → Drafter → Reviewer.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `hgb-frachtfuehrerhaftung` | Obhutshaftung des Frachtführers, Haftungsausschlüsse, Haftungsbegrenzung 8,33 SZR/kg, qualifiziertes Verschulden, Schadensanzeige und Verjährung | §§ 425, 426, 427, 428, 429, 430, 431, 433–435, 438, 439 HGB |
| `cmr-grenzueberschreitender-transport` | Anwendungsbereich CMR, Frachtbrief, Haftung Art. 17 ff., Haftungsbegrenzung Art. 23, qualifiziertes Verschulden Art. 29, Schadensanzeige Art. 30, Gerichtsstand Art. 31, Verjährung Art. 32 | Art. 1, 4–9, 17–23, 29, 30, 31, 32 CMR; Verhältnis zum HGB |
| `lieferbedingungen-adsp` | Einbeziehung und Inhaltskontrolle der ADSp 2017, Haftungsbegrenzung Ziff. 23, Lagerhaltung Ziff. 24, Pfandrecht Ziff. 19, Aufrechnungsverbot Ziff. 27 | ADSp 2017; §§ 305–310 BGB; § 449 HGB |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: HGB, CMR, ADSp, BGH-I-ZS- und OLG-Rechtsprechung, Koller, Thume, MüKoHGB
- [`agents/drafter.md`](./agents/drafter.md) – Erstellung im Gutachten- oder Urteilsstil mit SZR-Berechnung und Fristenkalender
- [`agents/reviewer.md`](./agents/reviewer.md) – Risiko-, Frist- und Berufsrechts-Check (§ 438 HGB / Art. 30 CMR; § 439 HGB / Art. 32 CMR; § 435 HGB / Art. 29 CMR)

## Installation

### Claude Code
```bash
# Über Marketplace (empfohlen)
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install transportrecht

# Oder als ZIP
# Claude Code → Customize Plugins → Install from .zip → transportrecht.zip
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area transportrecht --out dist/gemini
# Inhalt der erzeugten Dateien in neue Gemini-Gems einfügen
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area transportrecht --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Verlust einer Palette im innerdeutschen Straßentransport

```
/transportrecht:hgb-frachtfuehrerhaftung
Mandantin (Versender) hat einem Frachtführer 24 Paletten Elektronik
(Bruttogewicht 6.300 kg, Warenwert 84.000 EUR) zur Beförderung Hamburg
– München übergeben. Bei Ablieferung fehlen 3 Paletten (790 kg).
Frachtführer behauptet "Diebstahl auf bewachtem Parkplatz". Bitte
Haftung nach § 425 HGB prüfen, Haftungsbegrenzung § 431 mit aktuellem
SZR-Kurs berechnen und mögliche Durchbrechung über § 435 HGB
einschätzen. Fristenkalender § 438, § 439 HGB.
```

### Szenario 2 – Beschädigung bei grenzüberschreitender CMR-Beförderung

```
/transportrecht:cmr-grenzueberschreitender-transport
Beförderung Lyon (FR) – Stuttgart (DE) per LKW. Bei Ablieferung
Wassereintritt, 12 von 18 Kartons Beschädigung, Schaden 22.000 EUR
bei Eigengewicht 480 kg. Empfänger hat zwei Tage nach Ablieferung
schriftlich gerügt. Bitte Anwendbarkeit CMR, Haftung Art. 17 ff.,
Höchstbetrag Art. 23 III, Rechtzeitigkeit Schadensanzeige Art. 30 II
und Verjährung Art. 32 prüfen. Gerichtsstand Art. 31 für Klage gegen
französischen Frachtführer.
```

### Szenario 3 – ADSp-Einbeziehung im Speditionsauftrag

```
/transportrecht:lieferbedingungen-adsp
Spediteur hat den Auftrag per E-Mail bestätigt mit Hinweis "Es gelten
die ADSp in ihrer jeweils gültigen Fassung". Versender hat AGB nicht
ausdrücklich erhalten. Schaden 45.000 EUR an einer Maschine (Gewicht
2.100 kg). Bitte Einbeziehungskontrolle § 305 II BGB / § 449 HGB
prüfen, Wirksamkeit der Haftungsbegrenzung Ziff. 23 ADSp, sowie
Aufrechnungsverbot Ziff. 27 gegen offene Frachtforderung.
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Standardkommentare: **Koller**, Transportrecht; **Thume**, CMR-Kommentar; **MüKoHGB**, Bd. 7 (Transportrecht); **Beck'scher CMR-Handkommentar** (Boesche/de la Motte/Hartenstein); **Ebenroth/Boujong/Joost/Strohn**, HGB.

Rechtsprechung: BGH (insb. I. Zivilsenat als Transport-Senat), OLG Düsseldorf, OLG Hamburg, OLG Karlsruhe im Format `BGH, Urt. v. TT.MM.JJJJ – I ZR NN/JJ, TranspR JJJJ, Seite Rn. N`. Unverifizierte Zitate werden mit `[unverifiziert – prüfen in juris/TranspR]` markiert.

## Hinweise

- **SZR-Wert ist tagesaktuell.** Der Sonderziehungsrecht-Kurs (IMF/IWF) schwankt täglich. § 431 HGB und Art. 23 III CMR begrenzen auf 8,33 SZR/kg des Rohgewichts der beschädigten/verlorenen Sendung; in EUR-Beträgen wird nur die Berechnungsmethode dargestellt, nie ein fixer Wechselkurs ohne Datumsangabe.
- **CMR geht HGB vor**, soweit der CMR-Anwendungsbereich (Art. 1 CMR – entgeltliche grenzüberschreitende Straßenbeförderung zwischen mind. zwei Staaten, einer davon Vertragsstaat) eröffnet ist. Bei rein innerdeutscher Beförderung gilt HGB.
- **Qualifiziertes Verschulden bricht jede Haftungsbegrenzung.** § 435 HGB und Art. 29 CMR setzen Vorsatz oder Leichtfertigkeit mit dem Bewusstsein voraus, dass ein Schaden mit Wahrscheinlichkeit eintreten werde. Die Darlegungs- und Beweislast trägt regelmäßig der Geschädigte, mit Erleichterungen aus dem Obhutsverhältnis.
- **Fristen sind harte Tatfristen, keine Verjährungsfristen.** § 438 HGB und Art. 30 CMR (Schadensanzeige) sind Ausschlussfristen mit Beweislastumkehr-Wirkung; § 439 HGB und Art. 32 CMR (Verjährung) sind Verjährungsfristen.
- **Keine Präjudizienbindung deutscher Gerichte** außer § 31 BVerfGG; CMR-Rspr. ausländischer höchstrichterlicher Gerichte wirkt nur überzeugend (Auslegung des einheitlichen Übereinkommens).
- **Mandatsgeheimnis (§ 43a BRAO, § 203 StGB):** Keine echten Mandatsdaten ohne § 203-konformen Gateway.
