# Repository Conventions

These conventions are **provider-neutral** and apply to every skill in this repository, regardless of whether the skill is loaded by Claude, Gemini, GPT, or a future LLM provider. Skill authors and reviewers must follow them.

## Language

- **Outputs in German.** English terms only when established (e.g. "Letter of Intent", "Term Sheet", "Due Diligence", "Discovery") — and explained in parentheses on first use.
- Address clients in `Sie`-form unless the Mandat explicitly specifies `Du`.
- Authority and court correspondence: sober, clear, no rhetoric.

## Methodology

- Default to **Gutachtenstil** for internal memos and client letters that need reasoning.
- **Urteilsstil** for briefs (Schriftsätze), Beschlüsse, and concise internal notes.
- **Anspruchsgrundlagenprüfung** in canonical order: Vertrag → c.i.c. → GoA → dinglich → Delikt → Bereicherung.
- Statutory interpretation applies all four classical methods (grammatical, systematic, historical, teleological) plus constitution-conforming and EU-law-conforming interpretation.
- See [`references/methodik.md`](./references/methodik.md) for the long-form methodology guide.

## Sources and citation

**Binding:** [`references/zitierweise.md`](./references/zitierweise.md).

- Every juridical assertion is sourced.
- Case law: court, decision type, date, file number (Aktenzeichen), citation (NZA, NJW, BGHZ, etc.), paragraph (Randnummer).
- Commentary: Bearbeiter, "in:" Kommentar, edition, year (Stand, if applicable), norm, Rn.
- Articles: author, journal, volume, opening page (specific page).
- Order: Rspr. before Lit., newest first.
- **Commentary and Aufsätze are argumentatively load-bearing** in civil-law practice — use them actively, especially where no Rspr. is on point.

### Verification markers (mandatory)

Skills must distinguish between three citation states:

| Marker | Meaning |
|---|---|
| **(no marker, with URL)** | Statute or official text linked to gesetze-im-internet.de or equivalent. Verified. |
| `[unverifiziert – prüfen]` | Case citation from model knowledge that has NOT been independently verified. User must check in Beck-Online, juris, openjur.net before reliance. |
| `[generiert – kein Fundstellenbeleg]` | Aktenzeichen or page reference the model invented to illustrate. Must NEVER appear in client-facing output. |

If the skill cannot reliably classify a citation, default to `[unverifiziert – prüfen]`.

## Forbidden

- **Präjudizienbindungs-Argumente.** Germany has no doctrine of binding precedent except § 31 BVerfGG. Do not argue "the BGH said X, therefore courts must follow."
- **Pre-procedural fact-finding tools** beyond what German law permits: §§ 142, 144, 421–432 ZPO, § 810 BGB, § 242 BGB, Art. 15 DSGVO, Auskunfts- und Stufenklage (§ 254 ZPO). No US-style Discovery suggestions.
- **Halluzinierte Aktenzeichen oder Fundstellen.** When uncertain, mark and recommend verification.
- **Mandantengeheimnis-Verletzung** (§ 43a Abs. 2 BRAO, § 203 StGB). Client data only in tools with AVV in place.

## Standard memo structure

1. Sachverhalt (concise)
2. Frage(n)
3. Kurzantwort (one sentence)
4. Rechtliche Bewertung (Gutachtenstil)
5. Gesamtergebnis
6. Risiken / offene Punkte
7. Quellenverzeichnis per `references/zitierweise.md`

## Standard client-communication structure

- Anrede + Bezug ("In dem Mandat … / In Sachen …")
- Sachstand
- Empfehlung
- Nächste Schritte / Frist
- Kostenhinweis (RVG / Honorarvereinbarung)
- Unterschrift mit Berufsbezeichnung

## Skill convention

Every skill lives at `<plugin>/skills/<skill-name>/SKILL.md` with YAML frontmatter:

```yaml
---
name: skill-name
description: One-sentence description of what the skill does and its main statutory anchors.
language: de
provider_variants:
  - claude
  - gemini
  - openai
test: ./test.md
---
```

The body follows this canonical structure:

1. **Zweck** (purpose, ~3 sentences)
2. **Eingaben** (inputs the skill needs)
3. **Ablauf** (numbered workflow with statutory anchors)
4. **Researcher → Drafter → Reviewer** sub-agent breakdown (where the area defines sub-agents)
5. **Quellen und Zitierweise** (primary-source links + verification markers)
6. **Ausgabeformat** (concrete output template)
7. **Beispiele** (one minimum, in Gutachtenstil or Urteilsstil)
8. **Risiken / typische Fehler**

Skills must be reproducible and auditable.

## When uncertain

- Ask back (Skill name, Mandat, Gegenstand, Frist).
- Name open legal questions explicitly.
- Recommend verification in Beck-Online / juris with a specific search string.

## Provider parity

These conventions apply identically whether the skill is loaded into:

- **Claude Code** via `.claude-plugin/plugin.json` + `skills/<name>/SKILL.md`
- **Gemini Gems** via the rendered `providers/gemini.md` adapter
- **OpenAI Custom GPTs / Assistants** via the rendered `providers/openai.md` adapter
- **Any other provider** via the canonical `SKILL.md` body pasted directly into system instructions

Provider-specific tooling (e.g., Gemini's web search, GPT's code interpreter) may be invoked **only** for verification tasks — never to surface unsourced legal claims as "research."
