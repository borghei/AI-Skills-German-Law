# Patentrecht

**Production-grade Patentrechts-Skills für Claude / Gemini / GPT.** Deutsches Patentrecht (PatG), Gebrauchsmuster (GebrMG), Arbeitnehmererfindungsrecht (ArbnErfG), Europäisches Patentübereinkommen (EPÜ) und Einheitspatent / UPC aus deutscher Praxisperspektive. Researcher → Drafter → Reviewer.

> Abgrenzung: Marken- und Designschutz liegen im Plugin `gewerblicher-rechtsschutz`. Dieses Plugin geht **in die Tiefe** für technische Schutzrechte (Patent, Gebrauchsmuster) und das ArbnErfG.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `patentanmeldung-vorpruefung` | Vor-Check Patentierbarkeit (technischer Charakter, Neuheit, erfinderische Tätigkeit, gewerbliche Anwendbarkeit) und Anmeldungsstrategie DPMA / EPA / PCT | §§ 1–5 PatG; Art. 52, 54, 56 EPÜ; § 1 GebrMG; Aufgabe-Lösungs-Ansatz; Pariser Übereinkunft (Prioritätsrecht) |
| `patentverletzung-klage` | Klageschrift-Gerüst Patentverletzung mit dreifacher Schadensberechnung und Düsseldorfer Praxis | §§ 9, 10, 14, 139–142a PatG; §§ 143–145 PatG; Art. 64 EPÜ; UPC-Optionen |
| `freedom-to-operate` | FTO-Analyse zu Drittschutzrechten vor Markteintritt mit Designaround- / Lizenz- / Nichtigkeitsoptionen | §§ 9, 14 PatG; § 81 PatG (Nichtigkeit); Art. 138 EPÜ; DEPATISnet / esp@cenet / Patentscope |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: PatG, EPÜ, GebrMG, ArbnErfG, BGH X. ZS, BPatG, EPA-Beschwerdekammern, Standardkommentare
- [`agents/drafter.md`](./agents/drafter.md) – Erstellung in Gutachten- oder Urteilsstil, Anmeldungs- und Klagentwürfe, FTO-Berichte
- [`agents/reviewer.md`](./agents/reviewer.md) – Fristen-, Quellen- und Berufsrechts-Check (Einspruchsfristen, Nichtigkeit, Verletzungsverjährung § 141 PatG, UPC-Opt-out)

## Installation

### Claude Code
```bash
# Über Marketplace (empfohlen)
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install patentrecht

# Oder als ZIP
# Claude Code → Customize Plugins → Install from .zip → patentrecht.zip
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area patentrecht --out dist/gemini
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area patentrecht --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Vorprüfung einer computerimplementierten Erfindung

```
/patentrecht:patentanmeldung-vorpruefung
Start-up will ein KI-gestütztes Verfahren zur Steuerung einer
Werkzeugmaschine anmelden. Frage: technischer Charakter trotz
Software-Anteil? Anmeldung beim DPMA oder direkt EPA (mit Option
Einheitspatent)? Eigene Vorveröffentlichung auf einer Fachkonferenz
vor 3 Monaten – schadet sie der Neuheit?
```

### Szenario 2 – Patentverletzungsklage (Düsseldorf)

```
/patentrecht:patentverletzung-klage
Mandantin (deutsche Mittelständlerin) hält ein erteiltes EP-Patent
(validiert in DE, ohne UPC-Opt-out). Konkurrentin vertreibt seit
14 Monaten ein Konkurrenzprodukt, das wortlautidentisch unter den
Hauptanspruch fällt. Bitte Klageschrift-Gerüst (LG Düsseldorf vs.
UPC Lokalkammer München), Anspruchskatalog § 139 ff. PatG inkl.
dreifacher Schadensberechnung, Verjährungs-Check § 141 PatG.
```

### Szenario 3 – Freedom-to-Operate vor Markteintritt

```
/patentrecht:freedom-to-operate
Mandantin plant Markteintritt mit medizintechnischem Gerät
(DE + EU). Welche Drittschutzrechte sind zu prüfen, wie wird der
Schutzbereich ausgelegt (Hauptanspruch / Äquivalenz), welche
Handlungsoptionen bestehen bei Treffer (Designaround, Lizenz,
Nichtigkeitsantrag § 81 PatG, Verzicht)?
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Standardkommentare: **Benkard** PatG / EPÜ, **Schulte** PatG, **Mes** PatG, **Busse/Keukenschrijver** PatG; **Bartenbach/Volz** ArbnErfG; **Singer/Stauder** EPÜ.

Rechtsprechung: BGH X. Zivilsenat (Patentsenat), BPatG, EPA-Beschwerdekammern. Format: `BGH, Urt. v. TT.MM.JJJJ – X ZR NN/JJ, GRUR Jahr, Seite Rn. N`. EPA: `EPA, Entsch. v. TT.MM.JJJJ – T NNNN/JJ, ABl. EPA Jahr, Seite`. Unverifizierte Zitate werden mit `[unverifiziert – prüfen in juris/epo.org]` markiert.

## Hinweise

- **Einheitspatent / UPC.** Seit `01.06.2023 [unverifiziert – Datum prüfen]` Geltung des UPC-Übereinkommens; für EP-Bündelpatente besteht Opt-out-Möglichkeit. Strategische Entscheidung pro Mandat zu treffen.
- **Verletzungsverjährung § 141 PatG.** 3 Jahre ab Kenntnis (§§ 195, 199 BGB analog); 10-Jahres-Höchstfrist. Bei laufender Verletzung Wiedereintritt der Frist mit jeder Handlung.
- **Einspruchsfrist 9 Monate** ab Veröffentlichung der Erteilung (§ 59 PatG / Art. 99 EPÜ). Keine Wiedereinsetzung im EPÜ-Einspruch ohne Weiteres.
- **Schutzbereich § 14 PatG.** Patentansprüche maßgeblich, Beschreibung und Zeichnungen als Auslegungshilfe. Äquivalenzlehre nach BGH „Schneidmesser"-Trias `[unverifiziert – prüfen]`.
- **Mandantengeheimnis (§ 43a BRAO, § 203 StGB):** Keine echten Erfindungsmeldungen oder Sperrlistinhalte ohne § 203-konformen Gateway. Patentanwaltsrecht zusätzlich beachten (PAO).
