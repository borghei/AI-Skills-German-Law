# Compliance & Berufsrecht

This repo is a **technical skill collection**. It does not certify any deployment. The following obligations stay with the user.

| Topic | Norm | Who decides |
|---|---|---|
| **Mandatsgeheimnis** | §§ 203, 204 StGB · § 43e BRAO · § 2 BORA | Kanzlei / Compliance |
| **DSGVO / BDSG** | Art. 28 AVV · Art. 35 DPIA · Art. 44 ff. Drittlandtransfer | DSB |
| **Drittlandtransfer** | EU-US DPF · Standardvertragsklauseln · TIA (Schrems II) | Datenschutzkonferenz / EuGH |
| **EU KI-VO** | Art. 6 plus Anhang III · Art. 26 Betreiberpflichten · Art. 50 Transparenz | Compliance / Geschäftsleitung |
| **Beschlagnahmeverbote** | §§ 97, 160a StPO vs. US Cloud Act / FISA § 702 | Mandantenanwalt |

The repo ships three helpers:

- [`references/compliance-checklist.md`](https://github.com/borghei/AI-Skills-German-Law/blob/main/references/compliance-checklist.md) — the full nine-section pre-deployment checklist
- [`references/gateway-setup.md`](https://github.com/borghei/AI-Skills-German-Law/blob/main/references/gateway-setup.md) — § 203-compliant routing walkthrough (Claude Desktop, Claude Code, OpenAI SDK, Gemini)
- [`scripts/pii_redact.py`](https://github.com/borghei/AI-Skills-German-Law/blob/main/scripts/pii_redact.py) — German PII scrubber (IBAN, Steuer-ID, Telefon, PLZ+Ort, Datum, Aktenzeichen, Person names in strict mode)

## Gateway routing (recommended deployment pattern)

For § 203-sensitive use, route all model traffic through a German gateway:

```bash
launchctl setenv ANTHROPIC_BASE_URL https://api.<gateway>.de/anthropic
launchctl setenv ANTHROPIC_AUTH_TOKEN <your-gateway-key>
launchctl setenv ANTHROPIC_API_KEY ""
```

Then start Claude Code / Claude Desktop and pick the gateway-routed login. Same pattern (different env-var names) for OpenAI and Gemini SDKs.

## Why this matters

Anthropic, Google, and OpenAI do not sign Verschwiegenheitserklärungen directly for German lawyers as of May 2026. Sending Mandatsdaten directly to their APIs is not § 203-compliant. The established route is a German Zwischenanbieter (Langdock, deepset Cloud, or comparable) that signs the § 203-Zusatzvereinbarung and routes via an Anthropic/OpenAI/Google-compatible base URL.

## EU KI-VO phased application

The KI-VO (VO (EU) 2024/1689) is in force. Phased application (verified 2026-05-21):

- **02.02.2025** — Verbotene Praktiken Art. 5 plus KI-Kompetenzpflicht Art. 4
- **02.05.2025** — Verhaltenskodizes fertiggestellt
- **02.08.2025** — Notifizierte Stellen, GPAI-Anbieterpflichten Art. 51 ff., Governance, Sanktionsrahmen
- **02.08.2026** — Hauptanwendung (Hochrisiko nach Anhang III, Transparenz Art. 50)
- **02.08.2027** — Hochrisiko-Pflichten Art. 6 Abs. 1 (Anhang I); Pflichten für GPAI-Modelle pre-02.08.2025
- **02.08.2030** — Hochrisiko-KI bei Behörden plus Großdatenbanken

The `ki-vo-compliance/hochrisiko-klassifizierung` skill walks through the classification decision tree.

## Built-in compliance checklist

The nine sections in [`references/compliance-checklist.md`](https://github.com/borghei/AI-Skills-German-Law/blob/main/references/compliance-checklist.md):

1. Mandatsgeheimnis (§§ 203, 204 StGB; § 43e BRAO; § 2 BORA)
2. DSGVO / BDSG (AVV Art. 28, Rechtsgrundlage Art. 6, § 26 BDSG, Informationspflichten Art. 13/14, DPIA Art. 35, VVT Art. 30, Löschkonzept)
3. Drittlandtransfer / Schrems II (Angemessenheitsbeschluss, SCC, TIA, Schrems II-Risiken)
4. KI-VO (Klassifizierung Art. 5/6, GPAI Art. 51 ff., Transparenz Art. 50, Betreiberpflichten Art. 26)
5. Berufsrecht (Werbung, Fortbildung, Vermögensbetreuung, andere freie Berufe StBerG/WPO/PAO/BNotO)
6. Beschlagnahmeverbote / extraterritorialer Zugriff
7. Technische Mindeststandards (PII-Redaktion, Audit-Log, Versionskontrolle, Backups)
8. Organisatorisches (KI-Richtlinie, Schulung, Eskalation, Mandanteneinwilligung, Versicherung)
9. Skill-spezifische Prüfungen (Verifikationsmarker, Mandantsausgaben, Eval-Tests)

Run through it before any production deployment.

## Disclaimer

This page is a checklist. It is not legal advice. You remain responsible under § 43a Abs. 2 BRAO and § 2 BORA for everything you do with these skills.
