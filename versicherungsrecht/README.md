# Versicherungsrecht

**Production-grade Versicherungsvertragsrechts-Skills für Claude / Gemini / GPT.** Deutsches Versicherungsvertragsrecht (VVG) aus Praxisperspektive: Deckungsprüfung, vorvertragliche Anzeigepflicht, Obliegenheiten, Versicherungsfall, Vermittlerhaftung. Researcher → Drafter → Reviewer.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `versicherungsfall-deckungspruefung` | Dreistufige Deckungsprüfung (Leistungsbeschreibung, Risikoausschluss, Leistungsfreiheit) inkl. AVB-Auslegung | §§ 1, 100 VVG; § 305c Abs. 2 BGB; §§ 307 ff. BGB |
| `obliegenheitsverletzung-vvg` | Rechtsfolgen vorvertraglicher Anzeigepflicht und vertraglicher Obliegenheiten inkl. Quotelung und Kausalitätsgegenbeweis | §§ 19–22, 28–32 VVG; § 123 BGB |
| `versicherungsmaklerhaftung` | Pflichtenprüfung und Schadensersatz bei Beratungs- oder Dokumentationsfehlern des Versicherungsmaklers | §§ 59–63 VVG; § 34d GewO; §§ 195, 199 BGB |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: VVG, BGB, IDD-Umsetzung, BGH IV. Zivilsenat, Standardkommentare
- [`agents/drafter.md`](./agents/drafter.md) – Erstellung im Gutachten- oder Urteilsstil; Mandantenschreiben, Deckungsablehnungs- bzw. Anspruchsschreiben, Klageschriftsatz
- [`agents/reviewer.md`](./agents/reviewer.md) – Risiko-, Frist- und Berufsrechts-Check inkl. Fristenkalender (§ 8 VVG Widerruf, § 21 VVG, § 124 BGB, §§ 195, 199 BGB)

## Installation

### Claude Code
```bash
# Über Marketplace (empfohlen)
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install versicherungsrecht

# Oder als ZIP
# Claude Code → Customize Plugins → Install from .zip → versicherungsrecht.zip
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area versicherungsrecht --out dist/gemini
# Inhalt der erzeugten Dateien in neue Gemini-Gems einfügen
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area versicherungsrecht --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Deckungsablehnung Wohngebäudeversicherung

```
/versicherungsrecht:versicherungsfall-deckungspruefung
Mandant hat Wohngebäudeversicherung. Wasserschaden durch undichte
Dusche im OG. Versicherer lehnt Eintrittspflicht mit Verweis auf
AVB-Klausel "Nässeschäden infolge Abnutzung sind ausgeschlossen" ab.
Bitte dreistufige Deckungsprüfung, AVB-Auslegung nach VN-Verständnis
und Unklarheitenregel § 305c Abs. 2 BGB.
```

### Szenario 2 – Rücktritt wegen Anzeigepflichtverletzung

```
/versicherungsrecht:obliegenheitsverletzung-vvg
Berufsunfähigkeitsversicherung. Versicherer hat nach Eintritt des
Leistungsfalls Rücktritt nach § 19 Abs. 2 VVG erklärt mit Verweis
auf nicht angegebene Rückenbehandlung 2018. Antrag war von Mai 2021.
Bitte Belehrung nach § 19 Abs. 5, Frist § 21 Abs. 1, Kausalität und
ggf. Arglistanfechtung § 22 VVG iVm § 123 BGB prüfen.
```

### Szenario 3 – Maklerhaftung wegen Unterversicherung

```
/versicherungsrecht:versicherungsmaklerhaftung
Gewerbekunde betreibt Lager mit Warenbestand ca. 1,2 Mio €. Makler
hatte Versicherungssumme 600.000 € empfohlen, Beratungsprotokoll
unvollständig. Nach Brand zahlt Versicherer quotal (50 %). Bitte
Pflichtverletzung §§ 60, 61, 62 VVG, Schadensersatz § 63 VVG,
Mitverschulden § 254 BGB und Verjährung §§ 195, 199 BGB prüfen.
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Standardkommentare: **Prölss/Martin** VVG, **Beckmann/Matusche-Beckmann** Versicherungsrechts-Handbuch, **MüKoVVG**, **BeckOK VVG**, **Bruck/Möller** VVG-Großkommentar (älter, weiterhin argumentativ relevant).

Rechtsprechung: BGH (IV. Zivilsenat), OLG, BVerfG im Format `BGH, Urt. v. TT.MM.JJJJ – IV ZR NN/JJ, NJW JJJJ, Seite Rn. N` bzw. `r+s JJJJ, Seite` oder `VersR JJJJ, Seite`. Unverifizierte Zitate werden mit `[unverifiziert – prüfen]` markiert.

## Hinweise

- **Adressierter Empfängerhorizont.** AVB werden so ausgelegt, wie sie ein durchschnittlicher Versicherungsnehmer ohne versicherungsrechtliche Spezialkenntnisse bei verständiger Würdigung verstehen muss (st. Rspr. BGH IV. ZS). Unklarheiten gehen nach § 305c Abs. 2 BGB zu Lasten des Verwenders.
- **Belehrungspflicht ist die Sollbruchstelle.** §§ 19 Abs. 5, 28 Abs. 4 VVG: ohne ordnungsgemäße Belehrung in Textform keine Leistungsfreiheit / kein Rücktritt. Prüfen Sie Belehrungstext und Drucksatz konkret.
- **Frist § 21 Abs. 1 VVG: ein Monat** ab Kenntnis der Anzeigepflichtverletzung. Versäumt der Versicherer die Frist, sind Rücktritt, Kündigung und Vertragsanpassung ausgeschlossen.
- **Keine Doppelung mit Sozialrecht.** Gesetzliche Krankenversicherung, gesetzliche Unfall- und Rentenversicherung sind im Plugin `sozialrecht` (SGB V/VII/VI) behandelt. Hier nur Privatversicherung nach VVG.
- **Mandatsgeheimnis (§ 43a BRAO, § 203 StGB):** Keine echten Versicherungsnummern, Schadennummern oder Gesundheitsdaten ohne § 203-konformen Gateway.
