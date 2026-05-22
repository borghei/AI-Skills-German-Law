# Berufsrecht der Anwaltschaft

**Production-grade Berufsrechts-Skills für Claude / Gemini / GPT.** Deutsches anwaltliches Berufsrecht aus Kanzlei- und Kammerperspektive: BRAO (Zulassung, Grundpflichten, Aufsicht, anwaltsgerichtliche Maßnahmen), BORA (satzungsmäßige Konkretisierung), FAO (Fachanwaltschaften, Fortbildungspflicht), RDG (Abgrenzung erlaubter Rechtsdienstleistungen Nicht-Anwälte), RVG (Vergütung – Übersicht), § 203 StGB (Mandatsgeheimnis), EuRAG (europäische Rechtsanwälte). Researcher → Drafter → Reviewer.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `brao-pflichtenpruefung` | Checkliste anwaltlicher Grundpflichten vor Mandatsannahme und im laufenden Mandat | §§ 43, 43a, 43b, 43e, 44, 45, 46, 49b BRAO; §§ 2, 3, 6, 14, 18, 30 BORA; § 203 StGB; § 356 StGB |
| `fao-fortbildungsnachweis` | Nachweis der Fortbildungspflicht nach § 15 FAO und Verteidigung gegen Widerruf nach § 25 FAO | §§ 2, 4, 5, 14, 15, 25 FAO; § 43c BRAO |
| `rdg-abgrenzung` | Abgrenzung erlaubter Rechtsdienstleistungen Nicht-Anwälte (Nebenleistung, Inkasso, Legal-Tech) | §§ 1, 2, 3, 5, 6, 8, 10 RDG; § 3a UWG; § 134 BGB |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: BRAO/BORA/FAO/RDG-Statute, BGH-Anwaltssenat, BVerfG, Kammerrichtlinien
- [`agents/drafter.md`](./agents/drafter.md) – Erstellung im Gutachten- oder Urteilsstil mit Berufsrechtsfokus
- [`agents/reviewer.md`](./agents/reviewer.md) – Frist-, Verschwiegenheits- und Konfliktcheck (insb. § 203 StGB, § 43a IV BRAO, Verfolgungsverjährung § 115 BRAO)

## Installation

### Claude Code
```bash
# Über Marketplace (empfohlen)
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install berufsrecht-anwaltschaft

# Oder als ZIP
# Claude Code → Customize Plugins → Install from .zip → berufsrecht-anwaltschaft.zip
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area berufsrecht-anwaltschaft --out dist/gemini
# Inhalt der erzeugten Dateien in neue Gemini-Gems einfügen
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area berufsrecht-anwaltschaft --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Mandatsannahme bei vorbefasster Sozietät

```
/berufsrecht-anwaltschaft:brao-pflichtenpruefung
Mandatsanfrage einer GmbH gegen ihren ehemaligen Geschäftsführer wegen
Schadensersatzansprüchen. Vor zwei Jahren hat ein Partner unserer
Sozietät den GF persönlich in einer steuerlichen Angelegenheit beraten.
Bitte Interessenkollision § 43a IV BRAO + § 3 BORA prüfen, Sozietäts-
zurechnung, und Empfehlung Annahme/Ablehnung.
```

### Szenario 2 – Fortbildungspflicht-Stichprobe der RAK

```
/berufsrecht-anwaltschaft:fao-fortbildungsnachweis
Fachanwalt für Arbeitsrecht und Steuerrecht. RAK fordert Nachweis
nach § 15 FAO für 2024. Mandant hat 12 Std. Präsenz-Lehrgang
Arbeitsrecht + 8 Std. Online + zwei Aufsätze. Im Steuerrecht nur
9 Std. Bitte vollständigkeits- und Anerkennungs-Prüfung, ggf.
Stellungnahme an RAK entwerfen.
```

### Szenario 3 – Legal-Tech-Plattform vs. Anwaltsmonopol

```
/berufsrecht-anwaltschaft:rdg-abgrenzung
Startup will eine Online-Plattform betreiben, die Verbrauchern bei
Fluggastrechten (VO 261/2004) hilft – automatisierte Anspruchsprüfung,
Schreiben an Airlines, Einklagen via Partneranwälte. Bitte RDG-Status
(§§ 2, 10 RDG Inkasso? Nebenleistung § 5 RDG?), Folgen unerlaubter
RDL (§ 134 BGB, § 3a UWG), und Vergleich mit BGH wenigermiete.de.
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Standardkommentare: **Henssler/Prütting** BRAO, **Feuerich/Weyland** BRAO, **Hartung/Scharmer** Anwaltsberufsrecht, **Kleine-Cosack** BRAO, **Träger/Wickel/Decker** AGH (anwaltsgerichtliche Verfahren), **Offermann-Burckart** Anwaltsrecht.

Rechtsprechung: BGH (Anwaltssenat — AnwZ (Brfg) …), BVerfG (insb. zu Werbung und Vertraulichkeit), EuGH (Wouters, AKZO, Akzo Nobel zum Legal Privilege), Anwaltsgerichtshöfe. Format: `BGH, Urt. v. TT.MM.JJJJ – AnwZ (Brfg) N/JJ, NJW JJJJ, Seite Rn. N`. Unverifizierte Zitate werden mit `[unverifiziert – prüfen]` markiert; Beck-Online, juris, BRAK-Mitteilungen sind die primären Quellen.

## Hinweise

- **§ 203 StGB ist nicht verhandelbar.** Verschwiegenheitspflicht (§ 43a II BRAO + § 2 BORA) hat strafrechtliche Bewehrung. Jede Mandatsdaten-Verarbeitung — insbesondere KI-Auslagerung — muss durch § 43e BRAO und § 203 III StGB gedeckt sein (schriftliche Verpflichtung der Hilfsperson zur Verschwiegenheit). Brücke zur Skill-Familie `ki-governance`.
- **Interessenkollision § 43a IV BRAO ist Sozietäts-zugerechnet** (§ 3 BORA). Vorbefassung in „derselben Rechtssache" — auch außergerichtlich, auch beratend, auch durch andere Sozietätsmitglieder — sperrt die Mandatsannahme. Bei Übersehen drohen § 356 StGB (Parteiverrat), berufsgerichtliche Maßnahmen und zivilrechtliche Haftung.
- **Berufsrechtliche Verfolgungsverjährung beträgt 5 Jahre** (§ 115 BRAO). Rüge-Bescheid § 74 BRAO ist binnen 1 Monat anfechtbar. Anwaltsgerichtliche Maßnahmen reichen von Warnung über Geldbuße bis zur Ausschließung aus der Rechtsanwaltschaft (§ 114 BRAO).
- **Werbung § 43b BRAO + §§ 6 ff. BORA**: Sachliche Information über die berufliche Tätigkeit ist zulässig; Reklame und auf Erteilung eines Auftrags im Einzelfall gerichtete Werbung sind unzulässig. BVerfG hat das Werbeverbot mehrfach grundrechtskonform ausgelegt — Art. 12 GG.
- **Erfolgshonorar § 49b II BRAO** ist grundsätzlich verboten. Ausnahmen: § 4a RVG (Mandant aus wirtschaftlichen Gründen sonst gehindert), Inkassodienstleistungen und Auslandsfälle (§ 4a I RVG). Im Übrigen droht Nichtigkeit der Honorarvereinbarung.
- **Mandatsgeheimnis (§ 43a BRAO, § 203 StGB):** Keine echten Mandatsdaten ohne § 203-konformen Gateway. Siehe [`../references/gateway-setup.md`](../references/gateway-setup.md).
