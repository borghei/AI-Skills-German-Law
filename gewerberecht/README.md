# Gewerbe- und Handwerksrecht

**Production-grade Gewerberechts-Skills für Claude / Gemini / GPT.** Gewerbeanzeige, Erlaubnisse, Untersagung und Handwerksrolle aus der Perspektive der verwaltungsgerichtlichen Praxis. Researcher → Drafter → Reviewer.

> **Die Wahl der Ermächtigungsgrundlage ist das strukturelle Fehlerrisiko dieses Rechtsgebiets.** [§ 15 Abs. 2 GewO](https://www.gesetze-im-internet.de/gewo/__15.html) knüpft an das **Fehlen einer Zulassung** an und steht im Ermessen. [§ 35 GewO](https://www.gesetze-im-internet.de/gewo/__35.html) knüpft an die **materielle Unzuverlässigkeit** an, ist gebunden — und nach seinem Absatz 8 **gesperrt**, sobald für das Gewerbe eine besondere Untersagungsvorschrift besteht oder eine erteilte Erlaubnis wegen Unzuverlässigkeit zurückgenommen oder widerrufen werden kann. Dann gelten §§ 48, 49 VwVfG mit ihrer Jahresfrist. Im Handwerk tritt [§ 16 Abs. 3 HwO](https://www.gesetze-im-internet.de/hwo/__16.html) hinzu, dessen Untersagung ohne **gemeinsame Erklärung von Handwerkskammer und IHK** rechtswidrig ist. Jede Skill dieses Plugins bestimmt die Ermächtigungsgrundlage deshalb in Schritt 1.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `gewerbeuntersagung-35-gewo` | Untersagung wegen Unzuverlässigkeit: Prognose, Erforderlichkeit, erweiterte Untersagung, Sofortvollzug, Wiedergestattung | § 35 Abs. 1–9 GewO; §§ 28, 39 VwVfG; §§ 42, 70, 74, 80, 114 VwGO; §§ 70, 266a StGB; § 148 GewO |
| `gewerbeerlaubnis-34-gewo` | Erlaubnispflichtige Gewerbe: Versagungsgründe und Regelvermutungen, Sachkunde, Versicherung, Weiterbildung, MaBV, Rücknahme und Widerruf | §§ 34a, 34c, 34d, 34f, 34h, 34i, 144 GewO; MaBV; §§ 48, 49 VwVfG; § 26 InsO; § 882b ZPO |
| `gewerbeanzeige-reisegewerbe` | Gewerbebegriff und Anwendungsausnahmen, Anzeigepflichten, Betrieb ohne Zulassung, Reisegewerbekarte, Marktprivileg | §§ 4, 6, 14, 15, 55, 55a, 56, 57, 60c, 64–71a, 145, 146 GewO; § 16 HwO; Landesgaststättenrecht |
| `handwerksrolle-hwo` | Meistervorbehalt und wesentliche Tätigkeiten, Wege in die Handwerksrolle, Nebenbetrieb, Untersagung mit Kammererklärung | §§ 1, 3, 6–10, 7b, 8, 9, 16, 117 HwO; Anlagen A und B; § 14 GewO; § 53 BBiG |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: GewO, MaBV, HwO samt Anlagen, VwVfG, VwGO, Landeszuständigkeits- und Vollstreckungsrecht, BVerwG- und OVG-Rechtsprechung
- [`agents/drafter.md`](./agents/drafter.md) – Entwürfe: Stellungnahme im Anhörungsverfahren, Erlaubnis- und Eintragungsantrag, Widerspruch, Klage, Eilantrag, Wiedergestattungsantrag
- [`agents/reviewer.md`](./agents/reviewer.md) – Ermächtigungsgrundlagen-, Verfahrens-, Fristen- und Quellencheck (insbesondere § 35 Abs. 8 GewO, § 48 Abs. 4 VwVfG, § 35 Abs. 4 GewO, § 16 Abs. 3 S. 2 HwO)

## Installation

### Claude Code
```bash
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install gewerberecht
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area gewerberecht --out dist/gemini
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area gewerberecht --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Untersagung wegen Steuerrückständen

```
/gewerberecht:gewerbeuntersagung-35-gewo
Mandant betreibt einen Kfz-Handel und ist Geschäftsführer einer Bau-GmbH.
96.000 EUR Steuerrückstände, seit vierzehn Monaten keine Voranmeldungen.
Untersagung vom 12.03.2026 erstreckt auf alle Gewerbe und die
Geschäftsführertätigkeit, Sofortvollzug angeordnet, IHK nicht angehört.
Nach Erlass wurde eine Ratenvereinbarung geschlossen. Bitte Bewertung,
Eilantrag und Planung der Wiedergestattung.
```

### Szenario 2 – Widerruf einer Erlaubnis nach § 34c GewO

```
/gewerberecht:gewerbeerlaubnis-34-gewo
WEG- und Mietverwaltung seit 2019 mit Erlaubnis nach § 34c GewO. Der
Geschäftsführer wurde 2023 wegen Untreue verurteilt; die Behörde kannte
das seit 15.09.2025 und hat am 20.05.2026 widerrufen. Berufshaftpflicht
fehlt seit 2024, Weiterbildungsnachweise fehlen. Bitte Prüfung von
Rücknahme, Widerruf und Jahresfrist.
```

### Szenario 3 – Badsanierung ohne Eintragung in die Handwerksrolle

```
/gewerberecht:handwerksrolle-hwo
Fliesen verlegen, Duschelemente montieren, Sanitärobjekte anschließen;
Gesellenprüfung 2018, seit 01.09.2019 im Betrieb, ab 01.03.2021
Vorarbeiter mit Kolonnenverantwortung. Untersagung vom 15.04.2026, dem
Bescheid liegt nur eine Stellungnahme der Handwerkskammer bei. Bitte
Tätigkeitsanalyse, § 7b HwO und Angriff gegen die Untersagung.
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Bundesnormen werden mit gesetze-im-internet.de zitiert; die **MaBV** liegt dort unter dem Slug `gewo_34cdv`.

**Landesrecht ist konkret zu benennen.** Gewerberecht wird von Landesbehörden vollzogen: Zuständigkeit, Fortbestand des Vorverfahrens nach §§ 68 ff. VwGO, Verwaltungsvollstreckung und Gaststättenrecht richten sich nach dem Recht des jeweiligen Landes. Eine pauschale Aussage „Widerspruch nach § 68 VwGO" ist ohne Landesprüfung unzulässig; das Plugin markiert solche Stellen mit `[unverifiziert – prüfen]`.

**Rechtsprechung:** Zuständig sind die Verwaltungsgerichte und in der Revision das BVerwG. Zu Unzuverlässigkeit, Beurteilungszeitpunkt, erweiterter Untersagung und zur Abgrenzung wesentlicher Tätigkeiten nach § 1 Abs. 2 HwO besteht gefestigte Judikatur; jede konkrete Entscheidung ist vor Verwendung in juris, Beck-Online oder auf bverwg.de zu verifizieren.

## Hinweise

- **§ 35 Abs. 8 GewO ist die erste Frage jedes Untersagungsmandats.** Bei erlaubnispflichtigen Gewerben ist die Untersagung gesperrt; maßgeblich sind Rücknahme (§ 48 VwVfG) oder Widerruf (§ 49 VwVfG) — beide mit der **Jahresfrist des § 48 Abs. 4 VwVfG**, dem wirksamsten formalen Angriffspunkt.
- **Der maßgebliche Beurteilungszeitpunkt liegt bei der letzten Behördenentscheidung.** Wer Rückstände erst nach dem Widerspruchsbescheid tilgt, gewinnt den Anfechtungsprozess nicht mehr — er braucht den Wiedergestattungsantrag nach § 35 Abs. 6 GewO mit seiner Jahressperre.
- **Die Kammeranhörung nach § 35 Abs. 4 GewO** und die **gemeinsame Erklärung nach § 16 Abs. 3 S. 2 HwO** sind eigenständige Verfahrensvoraussetzungen und in jedem Mandat zu prüfen.
- **Reisegewerbe hat zwei kumulative Merkmale.** § 55 Abs. 1 GewO verlangt das Handeln **ohne vorhergehende Bestellung** **und** außerhalb der gewerblichen Niederlassung; eine vom Kunden veranlasste Terminvereinbarung schließt es aus.
- **Handwerksrecht wird tätigkeitsbezogen geprüft.** § 1 Abs. 2 HwO fragt nach den konkreten Arbeitsschritten, nach der Dreimonatsgrenze der Anlernzeit und nach der Gesamtbetrachtung mehrerer für sich unwesentlicher Tätigkeiten — nicht nach dem Firmennamen.
- **Mandantengeheimnis (§ 43a Abs. 2 BRAO, § 203 StGB):** Steuer-, Register- und Gewerbezentralregisterdaten sind besonders sensibel; keine Verarbeitung ohne AVV und Pseudonymisierung (`scripts/pii_redact.py`).
