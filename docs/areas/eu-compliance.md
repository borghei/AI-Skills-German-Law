# EU / cross-cutting compliance

7 frameworks every European company touches. Each ships as a separate installable plugin.

| Area | Plugin | Triggers when | Source |
|---|---|---|---|
| **EU KI-VO / AI Act** | `ki-vo-compliance` | Any company deploying AI in the EU | [GitHub](https://github.com/borghei/AI-Skills-German-Law/tree/main/ki-vo-compliance) |
| **NIS2** | `nis2` | ~30,000 German entities (essential plus important) | [GitHub](https://github.com/borghei/AI-Skills-German-Law/tree/main/nis2) |
| **HinSchG** | `hinweisgeberschutz` | Every employer with 50 or more EE | [GitHub](https://github.com/borghei/AI-Skills-German-Law/tree/main/hinweisgeberschutz) |
| **LkSG** | `lieferkettengesetz` | Companies over 1,000 EE in DE (CSDDD soon broader) | [GitHub](https://github.com/borghei/AI-Skills-German-Law/tree/main/lieferkettengesetz) |
| **DORA** | `dora` | Banks, insurers, investment firms, crypto, CASPs | [GitHub](https://github.com/borghei/AI-Skills-German-Law/tree/main/dora) |
| **DSA / DMA** | `dsa-dma` | Hosting providers, online platforms, VLOPs, gatekeepers | [GitHub](https://github.com/borghei/AI-Skills-German-Law/tree/main/dsa-dma) |
| **CSRD / ESRS** | `csrd` | Large companies, phased 2024 to 2028 (Omnibus pending) | [GitHub](https://github.com/borghei/AI-Skills-German-Law/tree/main/csrd) |

## Highlighted skills

- **ki-vo-compliance/hochrisiko-klassifizierung** — Art. 6 KI-VO + Anhang III. Drei Pfade: Sicherheitsbauteil (Anhang I), Anhang-III-Bereiche, Ausnahme Art. 6 Abs. 3. Folgepflichten Anbieter und Betreiber.
- **nis2/meldepflicht-24h** — Kaskadierte Fristen (24h Frühwarnung, 72h Erstmeldung, 1-Monats-Endbericht). Verzahnung mit DSGVO Art. 33 und Strafverfolgung (§ 202a StGB).
- **hinweisgeberschutz/meldestelle-einrichten** — Pflicht-Aufbau interne Meldestelle, Meldekanäle, Bearbeitungsfristen, Repressalienverbot § 36 HinSchG mit Beweislastumkehr.
- **lieferkettengesetz/risikoanalyse-lksg** — Jährliche und anlassbezogene Risikoanalyse, drei Stufen (eigener Geschäftsbereich → unmittelbare Zulieferer → mittelbare Zulieferer bei substantiierter Kenntnis), CSDDD-Ausblick.
- **dora/ict-risikomanagement** — Sechs DORA-Säulen, Verhältnis zu BAIT/MaRisk, TLPT, Drittparteien-Register.
- **dsa-dma/dsa-statement-of-reasons** — Art. 17 DSA-konforme Begründung von Inhaltsmoderationsentscheidungen, DSA Transparency Database, Rechtsbehelfsbelehrung.
- **csrd/wesentlichkeitsanalyse-doppelt** — Impact Materiality + Financial Materiality, ESRS E1–E5/S1–S4/G1, Omnibus-Stop-the-Clock-Hinweis.

## Why these are in one repo with the German legal practice areas

Compliance frameworks shape Kanzlei work, and Kanzlei expertise shapes compliance. Examples:

- A § 203 StGB review touches both `ki-vo-compliance/hochrisiko-klassifizierung` (technical) and `it-recht/it-vertragspruefung` (vendor contract).
- A DSGVO-Datenpanne triggers `datenschutzrecht/auskunftsersuchen-art-15` plus `nis2/meldepflicht-24h` plus potentially strafrechtliche Anzeige (`§ 202a StGB`).
- An insolvency triggers `insolvenzrecht/*` plus (if NIS2-relevant) the requirement to notify the BSI of operational disruption.

The orchestrator preset `ki-deployment-compliance` chains three relevant skills in this exact way:

```bash
python scripts/orchestrate.py --preset ki-deployment-compliance --fact "..."
```
