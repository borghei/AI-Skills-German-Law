# Arbeitsrecht

**Production-grade Arbeitsrechts-Skills für Claude / Gemini / GPT.** Tested workflows, primary-source citations, Researcher → Drafter → Reviewer sub-agents.

## Skills

14 Skills. Die mit **∑** markierten Skills rechnen Fristen deterministisch über [`scripts/legal_calc/`](../scripts/legal_calc/) (§§ 187–193 BGB, § 222 ZPO) — siehe [`references/rechner.md`](../references/rechner.md).

### Beendigung und Kündigungsschutz

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `kuendigungs-pruefung` | Vollprüfung einer ordentlichen oder außerordentlichen Kündigung | KSchG, § 102 BetrVG, §§ 622, 626 BGB, MuSchG, BEEG, SGB IX |
| `kuendigungsschutzklage` **∑** | Klageerhebung und Prozessführung: Frist, Präklusion, Anträge, Gütetermin | §§ 4–7, 9, 10 KSchG; §§ 54, 12a ArbGG; § 102 Abs. 5 BetrVG |
| `betriebsratsanhoerung` **∑** | Anhörungsschreiben, subjektive Determination, Fehlerkatalog | § 102 BetrVG; §§ 103, 26 BetrVG; § 626 Abs. 2 BGB |
| `sozialauswahl` | Vergleichsgruppe, Punkteschema, Leistungsträger, Auskunftsanspruch | § 1 Abs. 3–5 KSchG; § 95 BetrVG; § 106 GewO; § 10 AGG |
| `massenentlassungsanzeige` | Konsultationsverfahren und Anzeige, Sperr- und Freifrist | §§ 17, 18 KSchG; RL 98/59/EG; §§ 111 f. BetrVG |
| `aufhebungsvertrag` | Aufhebungsvertrag-Entwurf inkl. Sperrzeitprüfung | §§ 623, 779 BGB; § 159 SGB III; § 34 EStG |
| `abmahnung` | BAG-konforme Abmahnung mit Verhaltenserwartung und Sanktionsandrohung | §§ 314 Abs. 2, 626 BGB; BAG-Rspr. |
| `arbeitszeugnis` | Erteilung, Notenstufen, Geheimcodes, Berichtigungsklage | § 109 GewO; §§ 630, 241 Abs. 2 BGB |

### Vertrag, Bestand und Ansprüche

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `arbeitsvertrag-gestaltung` | AGB-Kontrolle, Ausschlussfristen, Vorbehalte, Nachweispflichten | §§ 305–310 BGB; §§ 2, 4 NachwG; § 3 MiLoG; § 623 BGB |
| `befristungskontrolle` | Schriftform, Sachgrund, Vorbeschäftigungsverbot, Entfristungsklage | §§ 14, 16, 17 TzBfG; RL 1999/70/EG |
| `betriebsuebergang` | Tatbestand, Unterrichtungskatalog, Widerspruch, Kündigungsverbot | § 613a BGB; RL 2001/23/EG |
| `urlaubsanspruch` | Umrechnung, Verfall nach Hinweisobliegenheit, Abgeltung, 15-Monats-Frist | §§ 1, 3, 7, 9, 11 BUrlG; §§ 195, 199 BGB; RL 2003/88/EG |

### Gleichbehandlung und Entgelt

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `agg-entschaedigung` **∑** | Indizienbeweis, zweistufiges Fristenregime, Bewerberfälle, AGG-Hopping | §§ 1, 3, 7, 15, 22 AGG; § 61b ArbGG; § 242 BGB |
| `entgelttransparenz` | EntgTranspG und die ab 08.06.2026 wirkende RL (EU) 2023/970 | §§ 10–15, 21 f. EntgTranspG; RL (EU) 2023/970; Art. 157 AEUV |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: Statute, Kommentare, BAG-Rechtsprechung
- [`agents/drafter.md`](./agents/drafter.md) – Erstellung im Gutachten- oder Urteilsstil
- [`agents/reviewer.md`](./agents/reviewer.md) – Risiko-, Frist- und Berufsrechts-Check

## Installation

### Claude Code
```bash
# Über Marketplace (empfohlen)
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install arbeitsrecht

# Oder als ZIP
# Claude Code → Customize Plugins → Install from .zip → arbeitsrecht.zip
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area arbeitsrecht --out dist/gemini
# Inhalt der erzeugten Dateien in neue Gemini-Gems einfügen
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area arbeitsrecht --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Betriebsbedingte Kündigung mit Sozialauswahl

```
/arbeitsrecht:kuendigungs-pruefung
Mandantin betreibt Maschinenbauunternehmen mit 35 AN, kein BR. Plant
Streichung einer von drei Stellen im Vertriebsinnendienst. Bitte
Sozialauswahl nach § 1 Abs. 3 KSchG durchführen, Sonderkündigungsschutz-
Check und Massenentlassungsschwelle prüfen.
```

### Szenario 2 – Aufhebungsvertrag mit Sperrzeitprüfung

```
/arbeitsrecht:aufhebungsvertrag
Arbeitnehmer (8 Jahre Betriebszugehörigkeit, 52 Jahre) soll Aufhebungs-
vertrag erhalten. Abfindung 8 × 0,5 Monatsgehälter (= 4 BMG).
Eigenkündigung droht. Bitte Sperrzeitfolgen § 159 SGB III prüfen und
steuerliche Behandlung § 34 EStG erläutern.
```

### Szenario 3 – Abmahnung wegen unentschuldigten Fehlens

```
/arbeitsrecht:abmahnung
AN war an 3 Tagen ohne Krankmeldung nicht erschienen. Erste Abmahnung.
Bitte BAG-konforme Abmahnung entwerfen: konkretes Verhalten, klare
Verhaltenserwartung, ausdrückliche Sanktionsandrohung.
```

### Szenario 4 – Kündigungsschutzklage mit Fristberechnung

```
/arbeitsrecht:kuendigungsschutzklage
Kündigung am 15.01.2026 in den Hausbriefkasten eingeworfen, Arbeitsgericht
in Bayern. Betriebsrat hat widersprochen. Bitte 3-Wochen-Frist § 4 KSchG
deterministisch berechnen, Anträge einschließlich Weiterbeschäftigung
formulieren und den Kostenhinweis § 12a ArbGG aufnehmen.
```

### Szenario 5 – Entgelttransparenz bei einer kommunalen Gesellschaft

```
/arbeitsrecht:entgelttransparenz
Kommunale Klinik-GmbH, 940 Beschäftigte, Anteile beim Landkreis.
Besteht vor dem deutschen Umsetzungsgesetz Handlungsbedarf? Bitte die
unmittelbare Wirkung der RL (EU) 2023/970 ab 08.06.2026 gegenüber
staatlichen Stellen prüfen und eine Roadmap bis zum Berichtsstichtag
07.06.2027 (Berichtsjahr 2026) aufstellen.
```

## Deterministische Fristberechnung

Drei Skills (`kuendigungsschutzklage`, `betriebsratsanhoerung`, `agg-entschaedigung`) rufen den Rechner in [`../scripts/legal_calc/`](../scripts/legal_calc/) auf, statt Fristen zu erzählen:

```bash
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 3 --einheit wochen --land BY
```

Der Rechner macht **nur die Arithmetik** nach §§ 187–193 BGB und § 222 ZPO. Zugang, Fristbeginn und das für die Feiertage maßgebliche Bundesland bleiben juristische Eingaben. Details: [`../references/rechner.md`](../references/rechner.md).

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Standardkommentare: **ErfK**, **APS**, **KR**, **MüKoBGB**, **BeckOK Arbeitsrecht**, **HWK**, **Schaub**.

Rechtsprechung: BAG, BGH, EuGH im Format `BAG, Urt. v. TT.MM.JJJJ – Az., NZA JJJJ, Seite Rn. N`. Unverifizierte Zitate werden mit `[unverifiziert – prüfen]` markiert.

## Hinweise

- **Standortkenntnis ist der Kern.** Bundesländer-Unterschiede, Betriebsgröße, BR-Vorhandensein, Tarifbindung beeinflussen jede Prüfung. Geben Sie diese Angaben mit.
- **Kündigungsprüfung ersetzt nicht das Gespräch mit HR und Führungskraft.** Sie ist eine Checkliste, die den vergessenen Punkt findet.
- **Lohn- und Arbeitszeitfragen** zitieren die Norm, kennzeichnen aber Grenzfälle zur menschlichen Prüfung.
- **Mandatsgeheimnis (§ 43a BRAO, § 203 StGB):** Keine echten Mandatsdaten ohne § 203-konformen Gateway. Siehe [`../references/gateway-setup.md`](../references/gateway-setup.md).
