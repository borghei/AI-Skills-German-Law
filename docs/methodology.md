# Methodology

Provider-neutral conventions that every skill follows. Full text in [CONVENTIONS.md](https://github.com/borghei/AI-Skills-German-Law/blob/main/CONVENTIONS.md), citation style in [references/zitierweise.md](https://github.com/borghei/AI-Skills-German-Law/blob/main/references/zitierweise.md), legal methodology in [references/methodik.md](https://github.com/borghei/AI-Skills-German-Law/blob/main/references/methodik.md).

## Language

- **Outputs in German.** English terms only when established (e.g. "Letter of Intent", "Term Sheet", "Due Diligence") and explained on first use.
- Sie-form unless the Mandat specifies Du.
- Authority and court correspondence: sober, clear, no rhetoric.

## Stil

| Zielgruppe | Stil |
|---|---|
| Mandantenbrief mit Begründungsanspruch | Gutachtenstil |
| Internes Memo | Gutachtenstil oder Hybrid |
| Schriftsatz / Beschluss / Kurzvermerk | Urteilsstil |
| Mandantenbrief ohne Begründungstiefe | Urteilsstil (Empfehlung statt Subsumtion) |

## Anspruchsgrundlagenprüfung

Canonical order:

1. **Vertrag** (einschl. vertragsähnlicher Schuldverhältnisse)
2. **culpa in contrahendo** (§§ 280 Abs. 1, 311 Abs. 2, 241 Abs. 2 BGB)
3. **Geschäftsführung ohne Auftrag** (§§ 677 ff. BGB)
4. **Dingliche Ansprüche** (§§ 985, 1004 BGB)
5. **Deliktsrecht** (§§ 823 ff. BGB)
6. **Bereicherungsrecht** (§§ 812 ff. BGB)

Strafrecht: dreistufiger Deliktsaufbau (Tatbestand then Rechtswidrigkeit then Schuld). Öffentliches Recht: Eingriff in Schutzbereich then Eingriff then verfassungsrechtliche Rechtfertigung.

## Auslegungsmethoden

Die vier klassischen Methoden:

1. Grammatikalisch (Wortlaut)
2. Systematisch
3. Historisch (Wille des Gesetzgebers)
4. Teleologisch (Sinn und Zweck)

Plus verfassungskonforme, unionsrechtskonforme, völkerrechtsfreundliche Auslegung.

## Zitierweise (BGH/Beck-Standard)

Rechtsprechung:

```
[Gericht], [Entscheidungsform] v. [TT.MM.JJJJ] - [Az.], [Fundstelle] Rn. [N].
```

Beispiel:

```
BAG, Urt. v. 10.06.2010 - 2 AZR 541/09, NZA 2010, 1227 Rn. 24 ("Emmely").
```

Kommentar:

```
[Bearbeiter], in: [Kommentar], [Auflage]. Aufl. [Jahr], [Norm] Rn. [N].
```

Beispiel:

```
Preis, in: ErfK, 24. Aufl. 2024, § 626 BGB Rn. 1.
```

## Verification markers

Mandatorisch in jedem SKILL.md:

| Marker | When |
|---|---|
| (kein Marker, mit URL) | Statute or official text verified |
| `[unverifiziert, prüfen]` | Case citation from model knowledge, not independently checked |
| `[generiert]` | **Forbidden** in skill outputs (only acceptable in pedagogical examples clearly framed as such) |

## Verboten

- **Präjudizienbindungs-Argumente.** Germany has no doctrine of binding precedent except § 31 BVerfGG.
- **Pre-procedural fact-finding tools** beyond what German law permits (§§ 142, 144, 421-432 ZPO; § 810 BGB; § 242 BGB; Art. 15 DSGVO; § 254 ZPO).
- **Halluzinierte Aktenzeichen oder Fundstellen.** Mark and recommend verification.
- **Mandantengeheimnis-Verletzung** (§ 43a Abs. 2 BRAO, § 203 StGB). Client data only in tools with AVV in place.

## Standard memo structure

1. Sachverhalt (knapp)
2. Frage(n)
3. Kurzantwort (ein Satz)
4. Rechtliche Bewertung (Gutachtenstil)
5. Gesamtergebnis
6. Risiken / offene Punkte
7. Quellenverzeichnis

## Standard client communication

1. Anrede + Bezug ("In dem Mandat ...")
2. Sachstand
3. Empfehlung
4. Nächste Schritte / Frist
5. Kostenhinweis (RVG / Honorarvereinbarung)
6. Unterschrift mit Berufsbezeichnung

## Skill convention

Every skill: `<plugin>/skills/<skill-name>/SKILL.md`.

YAML frontmatter:

```yaml
---
name: skill-name
description: One-sentence with main statutory anchors.
language: de
provider_variants:
  - claude
  - gemini
  - openai
test: ./test.md
---
```

Body structure:

1. **Zweck** (purpose, ~3 sentences)
2. **Eingaben** (inputs the skill needs)
3. **Ablauf** (numbered workflow with statutory anchors)
4. **Researcher → Drafter → Reviewer** sub-agent breakdown (where the area defines sub-agents)
5. **Quellen und Zitierweise**
6. **Ausgabeformat** (concrete output template)
7. **Beispiele**
8. **Risiken / typische Fehler**

Skills must be reproducible and auditable.
