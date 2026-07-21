# Kostenrecht / RVG

**Production-grade Kostenrechts-Skills für Claude / Gemini / GPT.** Anwaltsvergütung nach dem RVG, Kostenerstattung nach der ZPO, Gerichtskosten nach dem GKG und Prozess- beziehungsweise Verfahrenskostenhilfe. Researcher → Drafter → Reviewer.

> **Calculator-first.** Dieses Plugin ist das Referenzbeispiel für die Integration der deterministischen Rechner in [`../scripts/legal_calc/`](../scripts/legal_calc/). Der Rechner übernimmt Tabellenlookup und Arithmetik; **Gegenstandswert und die Bestimmung der Rahmengebühr nach § 14 RVG bleiben juristische Wertungen** und gehen als Eingabe in ihn ein. Die mitgelieferten Gebührentabellen sind versioniert und tragen einen `Stand` — er ist vor jeder mandantengerichteten Verwendung gegen die aktuelle Anlage 2 zu prüfen.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `rvg-gebuehrenberechnung` | Kostennote und Gegenkontrolle fremder Gebührenrechnungen: Wert, Wertgebühr, Gebührentatbestände, Anrechnung, Auslagen, Umsatzsteuer | §§ 13, 14, 15, 15a, 22, 23 RVG; Anlage 2; VV 2300, 3100, 3104, 1000/1003; Vorbem. 3 Abs. 4 VV; VV 7000–7002, 7008; § 10 RVG |
| `kostenfestsetzung-erstattung` | Kostenfestsetzungsantrag, Prüfung gegnerischer Aufstellungen, Wahl des Rechtsbehelfs | §§ 91–101 ZPO; §§ 103–107 ZPO; §§ 567, 569 ZPO; §§ 63, 68 GKG; § 32 Abs. 2 RVG; § 11 Abs. 2 RPflG |
| `verguetungsvereinbarung` | Entwurf und Wirksamkeitsprüfung von Honorarvereinbarungen, Zeit-, Pauschal- und Erfolgshonorar | §§ 3a, 4, 4a, 4b RVG; §§ 8, 9, 10, 34 RVG; § 49b Abs. 1 BRAO; § 126b BGB; §§ 305 ff. BGB |
| `gkg-gerichtskosten-pkh` | Kostenprognose nach GKG einschließlich Ermäßigung bei früher Beendigung sowie PKH-/VKH-Antrag | § 34 GKG + Anlage 2; KV 1210/1211/1220; §§ 12, 22, 39, 48, 63, 68 GKG; §§ 114–124 ZPO; § 76 FamFG; § 49 RVG |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: RVG, VV RVG, GKG, KV GKG, ZPO-Kostenrecht, BRAO, RPflG; Feststellung des Tabellenstands
- [`agents/drafter.md`](./agents/drafter.md) – Kostennote, Kostenfestsetzungsantrag, Vergütungsvereinbarung, Kostenprognose, PKH-Antrag; ruft den Rechner auf und übernimmt dessen Ausgabe unverändert
- [`agents/reviewer.md`](./agents/reviewer.md) – Fristen (Beschwerde, § 106 ZPO, § 120a ZPO), Wertansatz, Tabellenstand, Formcheck § 3a RVG, Berufsrecht

## Installation

### Claude Code
```bash
# Über Marketplace (empfohlen)
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install kostenrecht-rvg

# Oder als ZIP
# Claude Code → Customize Plugins → Install from .zip → kostenrecht-rvg.zip
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area kostenrecht-rvg --out dist/gemini
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area kostenrecht-rvg --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Kostennote nach Vergleich

```
/kostenrecht-rvg:rvg-gebuehrenberechnung
Werklohnforderung 25.000 EUR. Vorgerichtlich drei Schreiben und eine
Besprechung, dann Klage, im Termin Vergleich über 20.000 EUR.
Mandantin ist vorsteuerabzugsberechtigt, Vorschuss 1.000 EUR.
Bitte Kostennote nach § 10 RVG mit Anrechnung der Geschäftsgebühr
und Angabe, welcher Teil vom Gegner erstattungsfähig ist.
```

### Szenario 2 – Kostenfestsetzung mit Quotelung

```
/kostenrecht-rvg:kostenfestsetzung-erstattung
Streitwert 18.000 EUR, Tenor: Beklagte 4/5, Klägerin 1/5. Klägerin
in München, Prozessgericht in Hamburg, Anreise zum Termin. Beklagte
bestreitet Reisekosten und Umsatzsteuer. Festsetzungsbeschluss am
02.03.2026 zugestellt, weicht um 340 EUR ab. Antrag, Ausgleichung
nach § 106 ZPO und richtiger Rechtsbehelf mit Frist?
```

### Szenario 3 – Honorarvereinbarung im Honorarprozess

```
/kostenrecht-rvg:verguetungsvereinbarung
Stundensatz telefonisch besprochen, dann in einem Absatz der
Vollmacht festgehalten. Rechnung über 46.800 EUR, Gegenstandswert
12.000 EUR. Mandant beruft sich auf fehlende Vereinbarung.
Formcheck nach § 3a Abs. 1 RVG, Rechtsfolge § 4b RVG,
Vergleichsrechnung zur gesetzlichen Vergütung.
```

### Szenario 4 – Kostenprognose und PKH

```
/kostenrecht-rvg:gkg-gerichtskosten-pkh
Alleinerziehende, zwei Kinder, netto 1.980 EUR, Sparguthaben
3.400 EUR, keine Rechtsschutzversicherung. Schadensersatzklage
über 10.000 EUR. Gerichtskosten, Vorschuss, Wirkung eines
Vergleichs (KV 1211) und vollständiger PKH-Antrag mit
Ratenberechnung und Belehrung nach § 120a Abs. 2 ZPO.
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Rechner: [`../references/rechner.md`](../references/rechner.md). Standardkommentare: **Gerold/Schmidt** RVG, **Mayer/Kroiß** RVG, **Hartmann/Toussaint** Kostenrecht, **Schneider/Volpert/Fölsch** Gesamtes Kostenrecht, **Zöller** ZPO, **MüKoZPO**.

Rechtsprechung: BGH, OLG-Kostensenate, LG-Beschwerdekammern. Fundstellen typischerweise in **AGS**, **RVGreport**, **JurBüro**, **NJW-RR**. Unverifizierte Zitate werden mit `[unverifiziert – prüfen]` markiert; in diesem Plugin wird bewusst keine Entscheidung benannt, die nicht extern verifiziert wurde.

## Hinweise

- **Versionsdrift der Gebührentabellen.** Die Beträge der Anlage 2 zu § 13 RVG und zu § 34 GKG ändern sich durch Gesetz (zuletzt KostBRÄG 2025). Die Rechnerausgabe nennt den `Stand` der hinterlegten Tabelle mit; er ist vor jeder client-facing Verwendung gegen die amtliche Fassung zu prüfen.
- **Der Rechner ersetzt keine Wertung.** Gegenstandswert, Abgrenzung der Angelegenheit (§§ 15–18 RVG), Rahmengebühr nach § 14 RVG, Notwendigkeit der Kosten nach § 91 Abs. 1 ZPO und die Erfolgsaussicht nach § 114 ZPO sind juristische Entscheidungen und Eingaben.
- **Anrechnung und Ermäßigung sind nicht automatisiert.** Vorbem. 3 Abs. 4 VV ist als Position von Hand einzustellen, KV 1211 über den `--faktor` explizit anzugeben.
- **Formmangel kostet die Vergütung.** § 4b RVG kappt eine formfehlerhafte Vergütungsvereinbarung auf die gesetzliche Vergütung — die Formcheckliste des Reviewers ist kein Optional.
- **Mandantengeheimnis (§ 43a Abs. 2 BRAO, § 203 StGB):** Keine Kontodaten, Einkommensbelege oder PKH-Erklärungen ohne § 203-konformen Gateway verarbeiten.
