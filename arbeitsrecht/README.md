# Arbeitsrecht

**Production-grade Arbeitsrechts-Skills für Claude / Gemini / GPT.** Tested workflows, primary-source citations, Researcher → Drafter → Reviewer sub-agents.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `kuendigungs-pruefung` | Vollprüfung einer ordentlichen oder außerordentlichen Kündigung | KSchG, § 102 BetrVG, §§ 622, 626 BGB, MuSchG, BEEG, SGB IX |
| `aufhebungsvertrag` | Aufhebungsvertrag-Entwurf inkl. Sperrzeitprüfung | §§ 623, 779 BGB; § 159 SGB III; § 34 EStG |
| `abmahnung` | BAG-konforme Abmahnung mit Verhaltenserwartung und Sanktionsandrohung | §§ 314 Abs. 2, 626 BGB; BAG-Rspr. |

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

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Standardkommentare: **ErfK**, **APS**, **KR**, **MüKoBGB**, **BeckOK Arbeitsrecht**, **HWK**, **Schaub**.

Rechtsprechung: BAG, BGH, EuGH im Format `BAG, Urt. v. TT.MM.JJJJ – Az., NZA JJJJ, Seite Rn. N`. Unverifizierte Zitate werden mit `[unverifiziert – prüfen]` markiert.

## Hinweise

- **Standortkenntnis ist der Kern.** Bundesländer-Unterschiede, Betriebsgröße, BR-Vorhandensein, Tarifbindung beeinflussen jede Prüfung. Geben Sie diese Angaben mit.
- **Kündigungsprüfung ersetzt nicht das Gespräch mit HR und Führungskraft.** Sie ist eine Checkliste, die den vergessenen Punkt findet.
- **Lohn- und Arbeitszeitfragen** zitieren die Norm, kennzeichnen aber Grenzfälle zur menschlichen Prüfung.
- **Mandatsgeheimnis (§ 43a BRAO, § 203 StGB):** Keine echten Mandatsdaten ohne § 203-konformen Gateway. Siehe [`../references/gateway-setup.md`](../references/gateway-setup.md).
