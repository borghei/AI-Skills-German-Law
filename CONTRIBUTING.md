# Contributing to ai-skills-german-law

Welcome, and thank you for considering a contribution. **ai-skills-german-law** is a provider-agnostic skill collection for German legal practice. It works with Claude Code, Gemini Gems, and OpenAI custom GPTs.

We value contributions of all kinds:

- **New skills** -- Add a skill to an existing Rechtsgebiet or propose a new Rechtsgebiet.
- **Verified case citations** -- Replace `[unverifiziert – prüfen]` markers with a verified Beck-Online / juris / openjur.net / court-website URL.
- **Test cases** -- Real (anonymized) fact patterns are the most valuable contribution.
- **Provider adapters** -- Add or improve Claude / Gemini / OpenAI variants, or add a new provider (Mistral, DeepSeek, Llama).
- **Compliance corrections** -- §§ 203, 204 StGB; § 43e BRAO; DSGVO; KI-VO; Drittlandtransfer. Pull-request the checklist.
- **Bug fixes** -- Broken paths, wrong statute references, citation-format errors.
- **Documentation** -- Improve `SKILL.md` files, references, or examples.
- **Translations** -- Localize README / docs to additional languages (the skill content stays in German).

---

## Getting Started

### 1. Fork and Clone

```bash
gh repo fork borghei/ai-skills-german-law --clone
cd ai-skills-german-law
```

### 2. Branch from `main`

```bash
git checkout main
git pull origin main
git checkout -b <branch-name>
```

### 3. Branch Naming

| Prefix | Purpose | Example |
|--------|---------|---------|
| `feature/` | New skill, new area, new provider adapter | `feature/arbeitsrecht-massenentlassung` |
| `fix/` | Bug fix or citation correction | `fix/kuendigung-az-emmely` |
| `verify/` | Replacing `[unverifiziert]` with sourced citation | `verify/bag-emmely-az` |
| `docs/` | Documentation only | `docs/gateway-setup-windows` |

---

## Creating a New Skill

### Skill Package Structure

Every skill lives inside an area directory and follows this layout:

```
<area>/skills/<skill-name>/
├── SKILL.md                # canonical, provider-agnostic (required)
├── providers/              # provider-specific adapters (generated)
│   ├── claude.md
│   ├── gemini.md
│   └── openai.md
└── test.md                 # eval fact pattern (required for new skills)
```

### Authoring Workflow

1. Read [`CONVENTIONS.md`](./CONVENTIONS.md) and [`references/zitierweise.md`](./references/zitierweise.md) before writing anything.
2. Create the directory structure under the appropriate area (e.g., `arbeitsrecht/skills/<your-skill>/`).
3. Write `SKILL.md` following the canonical structure (frontmatter + Zweck / Eingaben / Ablauf / Researcher-Drafter-Reviewer / Quellen / Ausgabeformat / Beispiele / Risiken).
4. Add a `test.md` fact pattern.
5. Run `python scripts/validate.py` and `python scripts/eval.py --skill <area>/<skill>`.
6. Optionally regenerate provider adapters: `python scripts/route_provider.py --skill <area>/<skill>`.

---

## Skill Quality Requirements

Every skill must meet these standards before merge.

### SKILL.md Requirements

1. **YAML frontmatter** with `name`, `description` (one-sentence with main statutory anchors), `language: de`, optional `agents`, `provider_variants`, `test`.
2. **Trigger clause** in `description` — a "Use when …" sentence that tells the AI when to activate the skill.
3. **Numbered Ablauf** — explicit, statute-anchored workflow steps. Each step cites a primary source.
4. **Sub-agent split** — Researcher → Drafter → Reviewer roles described, even if the skill is a single prompt in practice.
5. **Verification markers** — every case citation carries one of: `(no marker, with URL)`, `[unverifiziert – prüfen]`, or `[generiert]` (the last is forbidden in client-facing output).
6. **Risiken / typische Fehler** section — at least 3 things the skill must avoid.
7. **Length** — under 500 lines and 5,000 words. Longer skills should be split.
8. **Concrete examples** — fact patterns with realistic but anonymized parties ("Mandantin A betreibt eine GmbH mit 35 AN ..."). Never use real Mandatsdaten.

### Validation

```bash
python scripts/validate.py
```

Skills failing structural validation will be sent back. Run before opening a PR.

---

## Citation Standard

Every legal assertion must be sourced. See [`references/zitierweise.md`](./references/zitierweise.md).

Three verification states are mandatory:

| Marker | When to use |
|---|---|
| (URL to gesetze-im-internet.de or EUR-Lex) | Statute |
| `[unverifiziert – prüfen]` | Case citation from model knowledge, not independently checked |
| `[generiert]` | **Forbidden** in skill outputs — only acceptable in pedagogical examples that are clearly framed as such |

If you replace `[unverifiziert]` with a verified citation, include the Beck-Online, juris, openjur.net, or court-website URL in your PR description.

---

## Pull Request Workflow

1. Run `python scripts/validate.py` — fix anything that fails.
2. If you changed a skill, run `python scripts/eval.py --skill <area>/<skill>`.
3. Open a PR with a one-paragraph summary including:
   - What changed (skill, area, citation, test, doc)
   - Statutory anchor(s) touched
   - Whether you tested the skill against a real Mandat (yes/no — both are fine)
   - Any `[unverifiziert]` citations you replaced with verified sources, with URL

**Conventional commits** are recommended:

```
feat(arbeitsrecht): add massenentlassung-anzeige skill
fix(zitierweise): correct BAG citation format
verify(kuendigung): replace [unverifiziert] for Emmely with juris URL
docs(gateway): add Windows 11 setup walkthrough
```

---

## Code of Conduct

Be respectful. Disagreements about legal substance are welcome and expected — frame them with sources, not opinions. We follow the [Contributor Covenant](https://www.contributor-covenant.org/) v2.1.

---

## License

Contributions are accepted under the same dual license as the project: **Apache-2.0** OR **MIT**, at the user's option. By submitting a PR you agree that your contribution may be distributed under either license.
