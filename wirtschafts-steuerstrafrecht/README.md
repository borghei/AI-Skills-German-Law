# Wirtschafts- und Steuerstrafrecht

**Production-grade Wirtschaftsstrafrechts-Skills für Claude / Gemini / GPT.** Steuerhinterziehung nach der AO, die zentralen Vermögensdelikte des StGB, Unternehmenssanktion nach §§ 30, 130 OWiG und die unternehmensinterne Untersuchung. Researcher → Drafter → Reviewer.

> Abgrenzung: Das allgemeine Strafverfahrensrecht liegt im Plugin `strafrecht`, das Besteuerungsverfahren und die **strafbefreiende Selbstanzeige (§§ 371, 398a AO)** im Plugin `steuerrecht`. Dieses Plugin dupliziert beides nicht, sondern verweist darauf.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `steuerhinterziehung-370-ao` | Tatbezogene Prüfung des Steuerstrafvorwurfs je Steuerart und Veranlagungszeitraum, Vollendung, Verjährung, Verteidigungsziel Leichtfertigkeit | § 370 AO (Abs. 1–4 einschl. Kompensationsverbot Abs. 4 S. 3); § 376 AO; § 378 AO; §§ 153, 168, 169, 393 AO; §§ 78, 78a, 78c StGB |
| `untreue-betrug-wirtschaftsstrafrecht` | Untreue, Betrug, Vorenthalten von Arbeitsentgelt, Korruption im geschäftlichen Verkehr und die Bezifferung des Abschöpfungsrisikos | §§ 263, 266, 266a, 299, 300 StGB; §§ 73–73e StGB; § 111e StPO; § 30 GmbHG; Art. 103 Abs. 2 GG |
| `unternehmenssanktion-130-owig` | Bußgeldrisiko des Unternehmens nach einer Mitarbeitertat, Compliance als Entlastung, Abschöpfung und Rechtsnachfolge | §§ 30, 130 OWiG; §§ 9, 17, 29a, 47 OWiG; §§ 73 ff. StGB; §§ 91 Abs. 2, 93 AktG; § 43 GmbHG |
| `internal-investigation` | Aufsetzen und Durchführen einer internen Untersuchung: Mandatsstruktur, Befragung, Mitbestimmung, Datenschutz, Beschlagnahmerisiko | §§ 97, 160a, 136 StPO; § 87 Abs. 1 Nr. 1 und Nr. 6 BetrVG; § 26 BDSG; Art. 6, 88 DSGVO; § 43a BRAO; § 203 StGB |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: AO, StGB, OWiG, StPO, BetrVG, BDSG/DSGVO; Verifikation über dejure.org; Markierung strittiger Fragen und des Gesetzgebungsstands
- [`agents/drafter.md`](./agents/drafter.md) – Einlassung, Verteidigungsschrift, Stellungnahme an die Bußgeldbehörde, Untersuchungsplan; tatbezogene Prüfungsreihenfolge und Bezifferungspflicht
- [`agents/reviewer.md`](./agents/reviewer.md) – Verjährung je Tat, Bezifferung des Nachteils, Abschöpfung, Belehrungen, Datenschutz-Doppelgrundlage, Quellenmarker

## Installation

### Claude Code
```bash
# Über Marketplace (empfohlen)
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install wirtschafts-steuerstrafrecht

# Oder als ZIP
# Claude Code → Customize Plugins → Install from .zip → wirtschafts-steuerstrafrecht.zip
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area wirtschafts-steuerstrafrecht --out dist/gemini
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area wirtschafts-steuerstrafrecht --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Steuerstrafverfahren nach Betriebsprüfung

```
/wirtschafts-steuerstrafrecht:steuerhinterziehung-370-ao
Bau-GmbH, nicht verbuchte Barumsätze 2018–2022. Mehrsteuern
140.000 EUR USt (Voranmeldungen) und 260.000 EUR KSt/GewSt.
Beschuldigter beruft sich auf den Steuerberater. Zu den
Mehrumsätzen gehören nicht berücksichtigte Schwarzlöhne.
Einleitung bekanntgegeben am 14.01.2026. Bitte Prüfung je Tat,
Vollendung, Verjährung und Kompensationsverbot.
```

### Szenario 2 – Untreuevorwurf gegen den Geschäftsführer

```
/wirtschafts-steuerstrafrecht:untreue-betrug-wirtschaftsstrafrecht
Vorauszahlungen von 800.000 EUR ohne Sicherheiten an einen später
insolventen Lieferanten. Gesellschafter hatten die Geschäfts-
beziehung allgemein gebilligt. Parallel drei Monate keine
Sozialversicherungsbeiträge abgeführt. Vermögensarrest über
800.000 EUR gegen die GmbH. Bitte Bezifferung des Nachteils,
§ 266a StGB und Abschöpfungsrisiko.
```

### Szenario 3 – Verbandsgeldbuße nach Korruptionsfall

```
/wirtschafts-steuerstrafrecht:unternehmenssanktion-130-owig
Vertriebsleiter zahlt über drei Jahre Provisionen an Einkäufer
von Kunden. Compliance-Handbuch vorhanden, seit 2019 keine
Schulungen, Compliance-Beauftragter nicht nachbesetzt.
Mehrumsatz 6,4 Mio. EUR, Deckungsbeitrag 1,1 Mio. EUR.
Verschmelzung auf Schwestergesellschaft geplant.
Bußgeldrahmen, Zumessung, Abschöpfung, Rechtsnachfolge?
```

### Szenario 4 – Interne Untersuchung aufsetzen

```
/wirtschafts-steuerstrafrecht:internal-investigation
Hinweis über das Meldesystem auf Rückvergütungen im Einkauf.
Kein Ermittlungsverfahren eingeleitet. Geplant: Auswertung von
14 Postfächern über sechs Jahre, Zugangs- und Reisedaten,
30 Interviews. Betriebsrat vorhanden, IT-Betriebsvereinbarung
von 2016. Zwei Betroffene haben eigene Verteidiger.
Bitte Untersuchungsplan, Belehrungstext und Bewertung des
Beschlagnahmerisikos.
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Standardkommentare: **Joecks/Jäger/Randt** Steuerstrafrecht, **Kohlmann** Steuerstrafrecht, **Klein** AO, **MüKoStGB**, **Schönke/Schröder** StGB, **Karlsruher Kommentar zum OWiG**, **Göhler** OWiG, **Meyer-Goßner/Schmitt** StPO, **Knierim/Rübenstahl/Tsambikakis** Internal Investigations.

Extern verifizierte Ankerentscheidungen dieses Plugins:

- **BVerfG, Beschl. v. 23.06.2010 – 2 BvR 2559/08, 2 BvR 105/09, 2 BvR 491/09** — § 266 StGB ist mit Art. 103 Abs. 2 GG vereinbar, aber restriktiv und präzisierend auszulegen; der Vermögensnachteil ist eigenständig festzustellen und zu beziffern.
- **BVerfG, Beschl. v. 27.06.2018 – 2 BvR 1405/17, 2 BvR 1780/17** — Durchsuchung bei Jones Day und Sicherstellung von Unterlagen aus einer internen Untersuchung.
- **EuGH, Urt. v. 30.03.2023 – C-34/21** — Anforderungen des Art. 88 DSGVO an mitgliedstaatliche Regelungen zur Beschäftigtendatenverarbeitung.

Alle übrigen Entscheidungsangaben tragen `[unverifiziert – prüfen]`; wo eine Entscheidung nicht verifiziert werden konnte, wird die Doktrin ohne Entscheidungsnamen wiedergegeben.

## Hinweise

- **Kein Verbandssanktionengesetz.** Ein solches Gesetz ist wiederholt vorgeschlagen und **nicht in Kraft getreten**. §§ 30, 130 OWiG bleiben das operative Recht; jede Aussage über Reformvorhaben ist mit `[unverifiziert – prüfen]` markiert.
- **§ 97 StPO bei internen Untersuchungen ist streitig.** Reichweite und Voraussetzungen des Beschlagnahmeschutzes für Interviewprotokolle und Untersuchungsunterlagen sind nicht abschließend geklärt. Die Untersuchung ist so zu führen, dass ihre Ergebnisse auch bei Kenntnisnahme durch die Staatsanwaltschaft vertretbar bleiben.
- **§ 26 BDSG steht nicht sicher.** Nach der EuGH-Rechtsprechung zu Art. 88 DSGVO ist jede Beschäftigtendatenverarbeitung zusätzlich auf eine eigenständige Grundlage nach Art. 6 DSGVO zu stützen.
- **Bezifferung statt Behauptung.** Verkürzungsbetrag, Vermögensnachteil und Abschöpfungsbetrag werden je Tat beziffert; die bloße Pflichtverletzung ersetzt die Feststellung des Nachteils nicht.
- **Abschöpfung schlägt oft schwerer zu als die Strafe.** Bruttoprinzip (§ 73d StGB) und § 17 Abs. 4 OWiG können das nominelle Höchstmaß übersteigen; der Vermögensarrest nach § 111e StPO trifft das Unternehmen regelmäßig vor der Anklage.
- **Mandantengeheimnis (§ 43a Abs. 2 BRAO, § 203 StGB):** Keine Interviewprotokolle, Personaldaten oder Steuerunterlagen ohne § 203-konformen Gateway verarbeiten. Bei internen Untersuchungen zusätzlich § 43a Abs. 4 BRAO (widerstreitende Interessen) beachten.
