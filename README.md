<p align="center">
  <img src="assets/header.svg" alt="AI Skills · German Law" width="100%"/>
</p>

<h1 align="center">AI Skills – German Law</h1>
<p align="center"><b>Production-grade AI skills for German legal practice. Works with Claude, Gemini, and GPT.</b></p>

<p align="center">
  <img src="https://img.shields.io/badge/Areas-13-brightgreen.svg" alt="13 Areas">
  <img src="https://img.shields.io/badge/Providers-Claude_%7C_Gemini_%7C_GPT-purple.svg" alt="Providers">
  <img src="https://img.shields.io/badge/Tested-CI_eval_harness-success.svg" alt="Tested">
  <img src="https://img.shields.io/badge/Compliance-DSGVO_%7C_KI--VO_%7C_NIS2_%7C_HinSchG_%7C_LkSG_%7C_DORA_%7C_DSA_%7C_CSRD-red.svg" alt="Compliance">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache--2.0_OR_MIT-yellow.svg" alt="License"></a>
</p>

---

> **An experimental skill set for legal practice in German law** – skills, sub-agents, workflows, and reference material intended as **inspiration for law firm processes**. It is based on **German legal practice** and the high value placed on commentaries and articles (Kommentare, Aufsätze). It contains **no expert opinions or legal advice**; all information is provided **without guarantee** – each user calibrates the skills for their own practice.

---

## Why this exists

Most "legal AI" projects are one of two things: a clever prompt with no sourcing, or a 100-skill experiment that no one tested end-to-end. German legal practice tolerates neither. A `[Modellwissen]` hallucination in a Kündigungsschreiben isn't a bug — it's malpractice exposure under § 43a Abs. 2 BRAO.

This repo takes a different approach. **Fewer skills. Each one tested. Every statute cited links to a verifiable source. Every case-law citation that the model cannot independently confirm is explicitly marked `[unverifiziert – prüfen]`.** A built-in evaluation harness lets you check a skill against fact patterns before you trust it on a real Mandat.

It is **not legal advice**, **not a substitute for Beck-Online or juris**, and **not authorized for use with privileged client data** unless you have a § 203 StGB-compliant gateway in place (see [Compliance](#compliance--berufsrecht)).

---

## Install any skill in one command

```bash
# Claude Code (native plugin marketplace)
/plugin marketplace add borghei/ai-skills-german-law

# Or clone and install a single area
git clone https://github.com/borghei/ai-skills-german-law.git
cd ai-skills-german-law
python scripts/route_provider.py --provider claude  --area arbeitsrecht --out dist/claude
```

**Alternative paths:**

- **Claude Code native plugin.** Run `/plugin marketplace add borghei/ai-skills-german-law` in Claude Code, then enable the legal areas you need.
- **Gemini (Gems).** `python scripts/route_provider.py --provider gemini --skill arbeitsrecht/kuendigungs-pruefung` → paste output into a new Gem at [gemini.google.com](https://gemini.google.com).
- **OpenAI (Custom GPT / Assistants).** `python scripts/route_provider.py --provider openai --skill arbeitsrecht/kuendigungs-pruefung` → paste output into a new Custom GPT or `assistants.create()` system instructions.
- **No setup, any AI chat.** Open any `SKILL.md`, copy the body, paste into Claude.ai, ChatGPT, or Gemini.

---

## What's different from existing German legal-AI repos

| Differentiator | Most repos | This repo |
|---|---|---|
| **Primary-source citations** | Free-form, often hallucinated | Statutes link to [gesetze-im-internet.de](https://www.gesetze-im-internet.de); case law explicitly marked verified/unverified |
| **Sub-agent structure** | One monolithic prompt | Researcher → Drafter → Reviewer split per skill |
| **Test suite** | None or a manual smoke-test | Fact-pattern eval harness (`scripts/eval.py`) with expected-shape assertions |
| **Compliance scaffolding** | A README disclaimer | PII redaction pre-hook, gateway-routing helper, audit-log skeleton, DSGVO / § 203 / KI-VO checklist |
| **Provider lock-in** | Claude only | Provider-agnostic canonical SKILL.md + thin adapters for Claude Code, Gemini Gems, and OpenAI custom GPTs |

---

## Multi-provider support

Each skill ships as a **provider-agnostic canonical** (`SKILL.md`) plus **adapter wrappers** for each LLM provider:

```
arbeitsrecht/skills/kuendigungs-pruefung/
├── SKILL.md                    # canonical (German content, provider-agnostic)
├── providers/
│   ├── claude.md               # Claude Code plugin format
│   ├── gemini.md               # Gemini Gem system prompt
│   └── openai.md               # GPT custom-instructions format
└── test.md                     # fact pattern + expected output
```

You maintain **one file per skill** (`SKILL.md`); the router (`scripts/route_provider.py`) regenerates the provider adapters on demand.

| Provider | Install path | Native format |
|---|---|---|
| **Claude Code** | Claude Code → Customize Plugins → Install from .zip | `.claude-plugin/plugin.json` + `skills/<name>/SKILL.md` |
| **Gemini (Gems)** | gemini.google.com → Gems → Create new gem → paste system prompt | `providers/gemini.md` |
| **OpenAI (Custom GPT / Assistants)** | chatgpt.com → Create a GPT → Configure → Instructions | `providers/openai.md` |

---

## Areas

**13 areas — 6 substantive areas of German law + 7 broad-applicability compliance frameworks** that affect virtually every European company. Each ships as its own installable plugin.

### German legal practice

| Area | Plugin | Coverage |
|---|---|---|
| **Arbeitsrecht** | [`arbeitsrecht/`](./arbeitsrecht/) | KSchG-Prüfung, § 102 BetrVG, Aufhebungsvertrag, Abmahnung, Sozialauswahl, Massenentlassung |
| **Datenschutzrecht / GDPR** | [`datenschutzrecht/`](./datenschutzrecht/) | DSGVO/BDSG, AVV-Review, Art. 15 Auskunft, Art. 33/34 Datenpanne, DPIA, Drittlandtransfer |
| **Vertragsrecht** | [`vertragsrecht/`](./vertragsrecht/) | AGB-Kontrolle §§ 305 ff. BGB, Klauselgestaltung, c.i.c., Leistungsstörung, Anfechtung |
| **Mietrecht** | [`mietrecht/`](./mietrecht/) | Wohnraummiete, Mieterhöhung § 558 BGB, Kündigung §§ 573 ff., Betriebskostenabrechnung, WEG |
| **Gesellschaftsrecht** | [`gesellschaftsrecht/`](./gesellschaftsrecht/) | GmbH-Recht (GmbHG), Geschäftsführerhaftung, Gesellschafterbeschlüsse, AG-Grundzüge |
| **Strafrecht** | [`strafrecht/`](./strafrecht/) | Strafbefehl-Verteidigung, Aktenaufbereitung, OWi-Verkehrsrecht, Beschuldigtenbelehrung |

### EU / cross-cutting compliance

| Area | Plugin | Coverage | Triggers when |
|---|---|---|---|
| **EU KI-VO / AI Act** | [`ki-vo-compliance/`](./ki-vo-compliance/) | Hochrisiko-Klassifizierung Art. 6 + Anhang III, Betreiberpflichten Art. 26, Transparenz Art. 50, GPAI-Anbieter Art. 51 ff. | Any company deploying AI in the EU |
| **NIS2** | [`nis2/`](./nis2/) | Risikomanagement Art. 21, 24h-Frühwarnung Art. 23, Geschäftsleitungs-Haftung, KRITIS-Schnittstelle | ~30,000 German entities (essential + important) |
| **HinSchG** | [`hinweisgeberschutz/`](./hinweisgeberschutz/) | Interne Meldestelle § 12, Vertraulichkeit § 8, Anonymität § 16, Repressalienverbot § 36 | Every employer with ≥ 50 EE |
| **LkSG** | [`lieferkettengesetz/`](./lieferkettengesetz/) | Risikomanagement § 4, Risikoanalyse § 5, Präventionsmaßnahmen § 6, BAFA-Bericht § 10 | Companies with > 1,000 EE in DE (CSDDD soon broader) |
| **DORA** | [`dora/`](./dora/) | IKT-Risikomanagement Art. 5 ff., Vorfallsmeldung Art. 19, TLPT Art. 26, Drittparteien Art. 28 ff. | Banks, insurers, investment firms, crypto, CASPs |
| **DSA / DMA** | [`dsa-dma/`](./dsa-dma/) | Notice-and-Action Art. 16, Statement of Reasons Art. 17, VLOP-Risikobewertung Art. 34, Gatekeeper Art. 5–7 DMA | Hosting providers, online platforms, VLOPs, gatekeepers |
| **CSRD / ESRS** | [`csrd/`](./csrd/) | Doppelte Wesentlichkeitsanalyse, ESRS E1–E5/S1–S4/G1, Prüfungspflicht, EU-Taxonomie | Large companies, phased 2024–2028 |

Each plugin includes a researcher sub-agent (Quellensuche), a drafter sub-agent (Entwurf nach Gutachtenstil), a reviewer sub-agent (Risiko- und Berufsrechts-Check), German conventions per [`CONVENTIONS.md`](./CONVENTIONS.md), and at least one test case under `<area>/tests/`.

---

## How much you can rely on it

A skill collection for the German legal profession needs to be unsentimental about trust. Here is what is verified, what is in active improvement, and what is the user's responsibility.

### What is production-grade today

- **Repo structure, install path, CI.** Every plugin manifest validates; CI runs `validate.py` + `eval.py` on every push (130+ structural assertions). `/plugin marketplace add` works end-to-end.
- **Statute citations.** Every `§ X` and every EU regulation links to the **authoritative public source** ([gesetze-im-internet.de](https://www.gesetze-im-internet.de) and [EUR-Lex](https://eur-lex.europa.eu)). These are stable and verifiable in one click.
- **Methodology.** Gutachtenstil, Anspruchsgrundlagen-Reihenfolge (Vertrag → c.i.c. → GoA → dinglich → Delikt → Bereicherung), BGH/Beck citation format, no Präjudizienbindungs-Argumente — textbook-correct conventions, documented in [`CONVENTIONS.md`](./CONVENTIONS.md) and applied by the reviewer sub-agent.
- **Compliance scaffolding.** PII redaction (`scripts/pii_redact.py`), gateway-routing guide ([`references/gateway-setup.md`](./references/gateway-setup.md)), § 203 / DSGVO / KI-VO checklist ([`references/compliance-checklist.md`](./references/compliance-checklist.md)), Berufsrechts-Reviewer-Stufe per area.
- **Multi-provider parity.** One canonical `SKILL.md` per skill; `scripts/route_provider.py` regenerates Claude / Gemini / OpenAI adapters on demand — no drift between providers.

### What is in active improvement (contributions welcome)

- **Case-law verification.** Every BAG / BGH / EuGH citation in a SKILL.md that the model could not independently confirm carries an explicit `[unverifiziert – prüfen]` marker. The verification path is one PR per citation, with a Beck-Online / juris / openjur.net / court-website URL. **This is the highest-impact contribution.** See [CONTRIBUTING.md](./CONTRIBUTING.md).
- **Legal-accuracy eval (vs. structural eval).** Today `eval.py` asserts a skill's *output shape* (does the workflow mention § 1 KSchG; does the risks-block flag massenentlassung). A future layer compares actual model output against expert-drafted gold answers — design captured in [CONTRIBUTING.md](./CONTRIBUTING.md).
- **Rechtsanwalt review.** Each area benefits from a 2-hour pass by a licensed Rechtsanwalt for that Rechtsgebiet. Reviews are credited in the area README.

### Hard limitations to plan around

- **No real Mandatsdaten without a § 203-compliant gateway.** Anthropic / Google / OpenAI do not sign Verschwiegenheitserklärungen directly for German lawyers. Until you route through a German Zwischenanbieter (Langdock, deepset Cloud, comparable), this is a drafting aid — not a Mandats-Tool. Setup walkthrough: [`references/gateway-setup.md`](./references/gateway-setup.md).
- **Every output is a draft.** No skill in this repo will produce a Schriftsatz, Mandantenbrief, or Beschluss-Vorlage that is signature-ready. The author obligation under § 43a Abs. 2 BRAO and § 2 BORA stays with the licensed Anwalt.

### The verification path to "I'd use this on a real Mandat"

1. Open the area you care about (e.g. `arbeitsrecht/`).
2. Read the SKILL.md you plan to use. Identify every `[unverifiziert]` citation.
3. Verify each citation in Beck-Online or juris (30 sec/each). Open a PR removing the marker — that PR helps everyone.
4. Run the skill against an anonymized historical Mandat you already know the answer to. Compare.
5. Wire a § 203-compliant gateway ([`references/gateway-setup.md`](./references/gateway-setup.md)).
6. Use on live Mandate **only** after steps 1–5 plus your own Berufsrechts-Freigabe.

---

## Quickstart

```bash
# 1. Validate the repo structure
python scripts/validate.py

# 2. Run the eval suite (smoke check that skills produce expected shape)
python scripts/eval.py --area arbeitsrecht

# 3. Redact German PII from a sample document before sending it to a model
python scripts/pii_redact.py --in beispiel-mandat.txt --out beispiel-redacted.txt

# 4. Generate provider-specific bundles
python scripts/route_provider.py --provider claude  --out dist/claude
python scripts/route_provider.py --provider gemini  --out dist/gemini
python scripts/route_provider.py --provider openai  --out dist/openai
```

---

## Compliance & Berufsrecht

This repository is a **technical skill collection**. It does not certify legality of any deployment. The following obligations remain with the user:

- **Mandatsgeheimnis (§§ 203, 204 StGB; § 43e BRAO; § 2 BORA).** AI providers headquartered outside the EU/EEA cannot receive Mandatsgeheimnis-protected data unless they have signed a Verschwiegenheitserklärung. As of May 2026, **Anthropic, Google, and OpenAI do not sign one directly** for German lawyers. The established route is a German Zwischenanbieter (e.g. Langdock, deepset Cloud) that contracts § 203-compliance and routes via an Anthropic/OpenAI/Google-compatible base URL.
- **DSGVO/BDSG.** Auftragsverarbeitungsvertrag (Art. 28), Drittlandtransfer-Prüfung (Art. 44 ff. + Schrems II), TIA, and DPIA (Art. 35) are the user's responsibility.
- **EU KI-VO (VO (EU) 2024/1689).** Use in Justiz, Strafverfolgung, or democratic processes can trigger Hochrisiko-classification (Art. 6 + Anhang III). Transparency obligations (Art. 50) and Betreiberpflichten (Art. 26) apply.
- **Beschlagnahmeverbote (§§ 97, 160a StPO)** vs. US Cloud Act / FISA § 702 / Executive Order 12333.

A built-in compliance checklist is at [`references/compliance-checklist.md`](./references/compliance-checklist.md). It is a checklist, not legal advice.

### Gateway routing (recommended deployment pattern)

```bash
launchctl setenv ANTHROPIC_BASE_URL https://api.<gateway>.de/anthropic
launchctl setenv ANTHROPIC_AUTH_TOKEN <your-gateway-key>
launchctl setenv ANTHROPIC_API_KEY ""
```

See [`references/gateway-setup.md`](./references/gateway-setup.md) for the full walkthrough.

---

## Methodology and citation style

All skills follow [`CONVENTIONS.md`](./CONVENTIONS.md) and [`references/zitierweise.md`](./references/zitierweise.md):

- **Gutachtenstil** for internal memos; **Urteilsstil** for briefs and Beschlüsse.
- Anspruchsgrundlagenprüfung in canonical order: Vertrag → c.i.c. → GoA → dinglich → Delikt → Bereicherung.
- Citations follow BGH/Beck convention: `BAG, Urt. v. TT.MM.JJJJ – Az., NZA JJJJ, Seite Rn. N.`
- Commentary literature (Kommentare) is treated as argumentatively load-bearing in line with civil-law practice (ErfK, MüKoBGB, BeckOK, KR, APS).
- **No Präjudizienbindung** — German law has none (except § 31 BVerfGG). Skills do not argue from binding precedent.
- Unverified case citations carry an explicit `[unverifiziert – prüfen in Beck-Online/juris]` marker.

---

## Testing

```bash
# Run the full eval suite
python scripts/eval.py

# Run a single skill's eval
python scripts/eval.py --skill arbeitsrecht/kuendigungs-pruefung

# Validate plugin structure (CI runs this on every PR)
python scripts/validate.py
```

Test cases live in `<area>/tests/<skill>.test.md`. Each file is a fact pattern + an expected-shape assertion (sections present, statutes cited, risk flags raised). Tests assert that the skill behaves like a competent junior lawyer drafted the output — not exact text.

---

## Documentation

- **Repository conventions:** [CONVENTIONS.md](CONVENTIONS.md)
- **Verification log** (per-skill source check, last pass 2026-05-21): [VERIFICATION_LOG.md](VERIFICATION_LOG.md)
- **Citation style (verbindlich):** [references/zitierweise.md](references/zitierweise.md)
- **Legal methodology:** [references/methodik.md](references/methodik.md)
- **Primary sources (verified URLs):** [references/primary-sources.md](references/primary-sources.md)
- **Compliance checklist:** [references/compliance-checklist.md](references/compliance-checklist.md)
- **Gateway setup (§ 203 routing):** [references/gateway-setup.md](references/gateway-setup.md)
- **Contributing:** [CONTRIBUTING.md](CONTRIBUTING.md)

---

## Contributing

Contributions welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Especially valued:

- **Verified case-law citations** that replace `[unverifiziert – prüfen]` markers — include a Beck-Online, juris, openjur.net, or court-website URL.
- **Additional Rechtsgebiete or compliance frameworks** — agrar-, bau-, erbe-, familien-, sozial-, steuer-, verwaltungsrecht / DGA, eIDAS 2.0, EU Cyber Resilience Act, MiCA, etc. Start by copying `arbeitsrecht/` as a template.
- **Test cases** — real (anonymized) fact patterns are the most valuable contribution.
- **Provider adapters** for other models (Mistral, DeepSeek, etc.).

Fork the repo, create a feature branch, run `python scripts/validate.py`, and submit a PR.

---

## Contributors

| Contributor | GitHub |
|-------------|--------|
| Borghei | [@borghei](https://github.com/borghei) |

---

## Disclaimer

> **This project is built with the assistance of AI tools (Claude, GPT, Gemini).** While every effort is made to ensure accuracy, AI-generated content — including skill definitions, reference guides, citations, and templates — may contain errors, inaccuracies, or outdated information. **This is not legal advice.** Any output of these skills is a draft for review by a licensed Rechtsanwalt or Syndikusrechtsanwalt under § 43a BRAO and § 2 BORA. Always verify case-law citations independently in Beck-Online, juris, or openjur.net before any client-facing or court-facing use. The author accepts no liability for decisions made based on the content in this repository. **Use at your own risk.**

---

## License

Dual-licensed under **Apache-2.0** ([LICENSE-APACHE](./LICENSE-APACHE)) **OR** **MIT** ([LICENSE-MIT](./LICENSE-MIT)) at your option. See [`NOTICE`](./NOTICE) for attribution.

---

<p align="center">
  <strong>13 areas · 3 LLM providers · Researcher → Drafter → Reviewer · DSGVO / KI-VO / NIS2 / HinSchG / LkSG / DORA / DSA / CSRD scaffolding</strong><br>
  <a href="https://borghei.me">borghei.me</a>
</p>

<p align="center">
  <a href="https://buymeacoffee.com/borghei"><img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me a Coffee"></a>
</p>
