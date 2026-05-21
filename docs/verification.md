# Verification

The verification log records what was checked, against which source, on which date. Provenance, not promises.

The full log lives on GitHub: [VERIFICATION_LOG.md](https://github.com/borghei/AI-Skills-German-Law/blob/main/VERIFICATION_LOG.md). What follows is the executive summary.

## Last pass: 2026-05-21

**Verifier:** Borghei (with AI assistance, knowledge cutoff January 2026)
**Scope:** All 28 skills across 23 areas.

## Production-grade today

<div class="trust-row" markdown>
<span class="state state-green">VERIFIED</span>
Every plugin manifest validates against the schema. CI runs `validate.py` on every push to catch structural drift.
</div>

<div class="trust-row" markdown>
<span class="state state-green">VERIFIED</span>
Every statute citation links to the authoritative public source: [gesetze-im-internet.de](https://www.gesetze-im-internet.de) or [EUR-Lex](https://eur-lex.europa.eu). One click, verifiable.
</div>

<div class="trust-row" markdown>
<span class="state state-green">VERIFIED</span>
Methodology: Gutachtenstil, Anspruchsgrundlagen-Reihenfolge (Vertrag then c.i.c. then GoA then dinglich then Delikt then Bereicherung), BGH/Beck-Zitierweise, no Präjudizienbindungs-Argumente. Documented in [CONVENTIONS.md](https://github.com/borghei/AI-Skills-German-Law/blob/main/CONVENTIONS.md) and enforced by the reviewer sub-agent.
</div>

<div class="trust-row" markdown>
<span class="state state-green">VERIFIED</span>
Multi-provider parity: one canonical SKILL.md per skill; the router regenerates Claude / Gemini / OpenAI adapters on demand, no drift.
</div>

## In active improvement

<div class="trust-row" markdown>
<span class="state state-amber">PARTIAL</span>
**Case-law verification.** Every BAG / BGH / EuGH citation the model could not independently confirm carries `[unverifiziert, prüfen]`. The verification path is one PR per citation with a Beck-Online / juris / openjur URL. Highest-leverage contribution.
</div>

<div class="trust-row" markdown>
<span class="state state-amber">PARTIAL</span>
**Legal-accuracy eval.** Today eval is structural (does the workflow mention § 1 KSchG; does the risks-block flag massenentlassung). The next layer compares actual model output to expert-drafted gold answers.
</div>

<div class="trust-row" markdown>
<span class="state state-amber">PARTIAL</span>
**Rechtsanwalt review per area.** Each area benefits from a 2-hour pass by a licensed Anwalt for that Rechtsgebiet. Reviews are credited in the area README.
</div>

## Hard limitations

<div class="trust-row" markdown>
<span class="state state-red">DO NOT</span>
**Send real Mandatsdaten without a § 203-compliant gateway.** Anthropic, Google, OpenAI do not sign Verschwiegenheitserklärungen directly for German lawyers. Route through Langdock, deepset Cloud, or comparable before processing privileged data. Setup walkthrough on [GitHub](https://github.com/borghei/AI-Skills-German-Law/blob/main/references/gateway-setup.md).
</div>

<div class="trust-row" markdown>
<span class="state state-red">DO NOT</span>
**Treat any output as signature-ready.** Every output is a draft for review by a licensed Rechtsanwalt under § 43a Abs. 2 BRAO and § 2 BORA. The Berufspflicht stays with the licensed Anwalt.
</div>

## Recent updates in the verification log

The 2026-05-21 pass corrected several factual claims:

- **LkSG § 24 Bußgeldhöhe** — the skill incorrectly cited "8 Mio. EUR"; actual ceiling under § 24 Abs. 2 is **800,000 EUR** (or 2 % of turnover only for entities over 400 Mio. EUR turnover and only for certain Abhilfeverstöße). Corrected.
- **KSchG § 23 + Leiharbeitnehmer** — the skill said "außer Betracht"; correct per BAG 2013 (Az. 2 AZR 140/12) is that they DO count at the user-Betrieb if their use is based on regelmäßigem Beschäftigungsbedarf. Corrected.
- **KI-VO timeline** — specific dates added (02.02.2025, 02.05.2025, 02.08.2025, 02.08.2026, 02.08.2027) plus the 02.08.2030 milestones I previously missed.
- **CSRD Omnibus** — Feb 2025 "Stop-the-Clock" proposal plus November 2024 merger plan plus November 2025 EP amendments. Skill now hedges the timeline accordingly.
- **HinSchG amendment** — last amended 02.12.2025 (BGBl. 2025 I Nr. 301). HinSchGOWiZustV v. 09.04.2025: Bundesamt für Justiz is the verfolgungs-Behörde.

## Verification path to "I'd use this on a real Mandat"

1. Open the area you need (e.g. `arbeitsrecht/`).
2. Read the SKILL.md. Identify every `[unverifiziert]` citation.
3. Verify each in Beck-Online or juris (~30 sec each). Open a PR removing the marker — that PR helps everyone.
4. Run the skill against an anonymized historical Mandat you already know the answer to. Compare.
5. Wire a § 203-compliant gateway.
6. Use on live Mandate **only** after steps 1–5 plus your own Berufsrechts-Freigabe.
