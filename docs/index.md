---
title: AI Skills, German Law
---

<div class="hero" markdown>

<div class="paragraph-sign">§</div>

# AI Skills, German Law

<p class="tagline">Tested AI skills for German legal practice and EU compliance.</p>

<div class="chips">
<span class="chip">CLAUDE</span>
<span class="chip">GEMINI</span>
<span class="chip">GPT</span>
</div>

</div>

<div class="stats" markdown>
<div class="stat"><div class="number">23</div><div class="label">Areas</div></div>
<div class="stat"><div class="number">28</div><div class="label">Skills</div></div>
<div class="stat"><div class="number">370+</div><div class="label">Assertions</div></div>
<div class="stat"><div class="number">3</div><div class="label">Providers</div></div>
</div>

A `[Modellwissen]`-Halluzination in einem Kündigungsschreiben ist kein Bug. Sie ist Haftungsexposure unter § 43a Abs. 2 BRAO. This library is a focused, **provider-agnostic** alternative: every statute citation linked to its authoritative source, every case-law citation explicitly marked verified or `[unverifiziert, prüfen]`, a built-in evaluation harness, and a dated verification log.

It is **not legal advice**, **not a Beck-Online substitute**, and **not for Mandatsdaten without a § 203 StGB-compliant gateway**. It is a tested drafting aid with an honest paper trail.

---

## Install in 60 seconds

```bash
# Claude Code (native plugin marketplace)
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install arbeitsrecht
```

See [Installation](getting-started/installation.md) for Gemini, GPT, and manual paths.

---

## Areas at a glance

<div class="grid" markdown>

<div class="card" markdown>
### German legal practice
11 substantive areas of everyday Kanzlei work.
<div class="anchor">arbeitsrecht · datenschutzrecht · vertragsrecht · mietrecht · gesellschaftsrecht · strafrecht · insolvenzrecht · prozessrecht · erbrecht · familienrecht · betreuungsrecht</div>

[Browse →](areas/german-law.md)
</div>

<div class="card" markdown>
### Fachanwaltschaften
5 specialty practice areas tied to the bar's Fachanwalt qualifications.
<div class="anchor">it-recht · bankrecht · gewerblicher-rechtsschutz · steuerrecht · verwaltungsrecht</div>

[Browse →](areas/fachanwaltschaften.md)
</div>

<div class="card" markdown>
### EU compliance
7 cross-cutting frameworks every European company touches.
<div class="anchor">ki-vo-compliance · nis2 · hinweisgeberschutz · lieferkettengesetz · dora · dsa-dma · csrd</div>

[Browse →](areas/eu-compliance.md)
</div>

</div>

---

## What is different

| | Most repos | This repo |
|---|---|---|
| **Source citations** | Free-form, often hallucinated | Statutes link to gesetze-im-internet.de; case law explicitly marked verified or `[unverifiziert]` |
| **Architecture** | One monolithic prompt | Researcher then drafter then reviewer split per skill |
| **Testing** | A README disclaimer | Fact-pattern eval harness with 370+ assertions, runs on every CI build |
| **Compliance** | A warning paragraph | PII redaction script, gateway-routing walkthrough, dated [verification log](verification.md), DSGVO/§203/KI-VO checklist |
| **Provider lock-in** | Claude only | Canonical SKILL.md plus Claude Code / Gemini Gems / OpenAI adapters |

---

## How much you can rely on it

We are unsentimental about trust. The dated [verification log](verification.md) records what was checked, when, against which source. The summary view:

<div class="trust-row" markdown>
<span class="state state-green">PRODUCTION</span>
Repo structure plus CI. Plugin manifests validate. Statute citations link to gesetze-im-internet.de and EUR-Lex. Methodology textbook-correct. Multi-provider parity via `scripts/route_provider.py`.
</div>

<div class="trust-row" markdown>
<span class="state state-amber">IN PROGRESS</span>
Case-law verification (every BAG/BGH/EuGH citation marked `[unverifiziert]`). Legal-accuracy eval (currently structural-only). Rechtsanwalt review per area.
</div>

<div class="trust-row" markdown>
<span class="state state-red">HARD LIMIT</span>
No real Mandatsdaten without a § 203-compliant gateway. Every output is a draft for review by a licensed Rechtsanwalt under § 43a BRAO and § 2 BORA.
</div>

[Read the full trust model →](verification.md)

---

## Disclaimer

> **This project is built with the assistance of AI tools (Claude, GPT, Gemini).** While every effort is made to ensure accuracy, AI-generated content may contain errors. **This is not legal advice.** Any output is a draft for review by a licensed Rechtsanwalt under § 43a BRAO and § 2 BORA. Always verify case-law citations independently in Beck-Online, juris, or openjur.net before client-facing or court-facing use. The author accepts no liability. **Use at your own risk.**
