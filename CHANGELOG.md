# Changelog

All notable changes to this project are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Dates are ISO 8601.

## [Unreleased]

### Fixed — superseded law (2026-07-21)

Four areas taught law that had been repealed, replaced or deferred. Corrections
verified against primary sources where marked:

- **`energierecht` / `baurecht` — GEG.** The **Gebäudemodernisierungsgesetz**
  passed the Bundestag on **10.07.2026 (323:271)**, deleting **§§ 71, 71b–71p and
  § 72 GEG**. The 65 %-renewables heating rule is gone; building-level duties now
  key off the municipal **Wärmeplan (WPG)**. Verified against bundestag.de.
- **`lieferkettengesetz` — LkSG-Berichtspflicht.** BAFA stopped reviewing reports
  under **§§ 12, 13 LkSG on 03.09.2025** and closed the submission portal. Encoded
  as an **executive Weisung, not a statutory repeal** — the duties formally remain.
  §§ 5, 6, 7, 8, 10, 14, 15 survive unchanged. Verified against bafa.de.
- **`ki-vo-compliance` — Digital Omnibus on AI.** High-risk obligations deferred
  (Anhang III → **02.12.2027**, Anhang I → **02.08.2028**), but **Art. 50
  transparency remains 02.08.2026** and **GPAI (Art. 51–55) was not deferred** —
  Commission enforcement and fines begin **02.08.2026**. Added the Art. 52(1)
  two-week notification, the mandatory training-content template, the Code of
  Practice signatory position, Art. 111(3) legacy models, and two new prohibitions
  (NCII, CSAM) from 02.12.2026. Germany's market surveillance authority is the
  **Bundesnetzagentur**, not the Datenschutzaufsicht.
- **`csrd` / `lieferkettengesetz` — Omnibus I** (RL (EU) 2026/470, in force
  18.03.2026): CSRD **> 1.000 Beschäftigte UND > 450 Mio. EUR**; CSDDD
  **> 5.000 UND > 1,5 Mrd. EUR**, duties from 26.07.2029.
- **`kapitalmarktrecht` — EU Listing Act** (applicable 05.06.2026): in a
  zeitlich gestreckter Vorgang only the **Endereignis** is ad-hoc disclosable.
  Zwischenschritte remain *Insiderinformation* for Art. 14/10/18 purposes — the
  decoupling of Art. 7 from Art. 17 is now stated explicitly.
- **`produktrecht`** — new Produkthaftungsregime from **09.12.2026**; because
  § 13 ProdHaftG runs ten years, both regimes coexist into the 2030s, so the skill
  gained a placing-on-market weichenstellung rather than a replacement.
- **`vergaberecht`, `geldwaesche-aml-kyc`, `it-recht`** — BTTG (01.05.2026),
  Vergabebeschleunigungsgesetz (01.07.2026), AMLD6/AMLR/AMLA, Data Act + DADG.

### Added

- **New area `cyber-resilience-act`** (4 skills, VO (EU) 2024/2847): scope test,
  the **24 h / 72 h / 14 d reporting regime starting 11.09.2026**, product
  requirements and SBOM, coordinated vulnerability disclosure.
- **`vertragsrecht` 2 → 14 skills** — Kaufmängel, Werkvertrag, Rücktritt/SE,
  Verbraucherwiderruf, Verjährung, Sicherheiten, Vertragsstrafe, § 313,
  Abtretung, Anfechtung, Vergleich, vorvertragliche Phase.
- **`arbeitsrecht` 3 → 14 skills** — Kündigungsschutzklage, Betriebsratsanhörung,
  Massenentlassung, Sozialauswahl, Zeugnis, Befristung, AGG, Vertragsgestaltung,
  § 613a, Urlaub, **Entgelttransparenz** (Germany in transposition default since
  08.06.2026; direct vertical effect against staatliche Stellen).
- **`mietrecht` 3 → 13 skills**, with the duplicated Mieterhöhungs-Skills merged
  and the freed slot spent on the genuinely missing § 559 Modernisierung.
- **Deterministic calculators extended** (`scripts/legal_calc/`): `kuendigungs-
  fristen.py` (§ 622 BGB) and `verzugszinsen.py` (§§ 288, 247 BGB). Test suite
  **29 → 47**. The Basiszinssatz is a required input, never hardcoded, and
  § 622 Abs. 2 S. 2 is not applied by default (Kücükdeveci). Calculator-wired
  skills: **2 → 11**.

### Changed

- **`scripts/verify_citations.py`** — a case citation carrying an authoritative
  source link (dejure.org, bverfg.de, curia.europa.eu, …) now counts as
  **verified** rather than "unmarked". Previously verifying a citation *raised*
  the warning count, so the metric inverted quality. Repo-wide warnings
  **498 → 437** despite the file count rising 189 → 226.

### Verified

- **`urheber-medienrecht` citation pass** — 30 decisions confirmed against
  dejure.org, **12 errors caught**. Both candidates for "Das Boot II" were wrong
  (`I ZR 145/11` is "Fluch der Karibik"); "Tchibo/Rolex II" is `I ZR 107/90`, and
  the previously cited `I ZR 6/06` is a real decision of that date but a different
  case with a different Fundstelle. See VERIFICATION_STATUS.md.

Counts: **50 areas / 226 skills** (3,922 eval assertions, 226/226 passing).
- **Thirty compliance/civil skills** bringing the last ten 1-skill areas to four
  each: **bankrecht** (Widerruf Verbraucherdarlehen, Bürgschaft, Zahlungsdienst-
  haftung), **betreuungsrecht** (Betreuerbestellung, Einwilligungsvorbehalt,
  Vorsorgevollmacht/Patientenverfügung — post-2023 BGB-Reform), **csrd** (ESRS-
  Berichtspflicht, EU-Taxonomie, Nachhaltigkeitsbericht-Prüfung), **lieferketten-
  gesetz** (Präventions-/Abhilfemaßnahmen, Beschwerdeverfahren, BAFA-Bericht),
  **dora** (Vorfallsmeldung, Resilienztests/TLPT, Drittparteienrisiko), **nis2**
  (Risikomanagement, Anwendungsbereich, Geschäftsleitungshaftung — BSIG n.F. nach
  NIS2UmsuCG), **dsa-dma** (Notice-and-Action, Beschwerde/Streitbeilegung, DMA-
  Gatekeeper-Pflichten), **ki-vo-compliance** (verbotene KI-Praktiken Art. 5,
  Transparenz Art. 50, GPAI Art. 53/55), **gewerblicher-rechtsschutz** (Marken-
  anmeldung, Designschutz, Patentverletzung), **hinweisgeberschutz** (interne
  Meldungsbearbeitung, Repressalienschutz, externe Meldung/Offenlegung). Counts:
  **49 areas / 189 skills** (2,982 eval assertions, 189/189 passing). Fast-moving
  CSRD/LkSG (EU Omnibus 2025/2026) and NIS2/BSIG items marked [unverifiziert - prüfen].
- **Forty litigation/IT skills** taking four areas from one skill to eleven each:
  **strafrecht** (notwendige-verteidigung, durchsuchung-beschlagnahme,
  untersuchungshaft, akteneinsicht-verteidiger, beschuldigtenvernehmung,
  opportunitaetseinstellung, beweisverwertungsverbot, revision-strafsachen,
  berufung-strafsachen, wiederaufnahme — StPO); **verwaltungsrecht**
  (anfechtungs-/verpflichtungsklage, §§ 80/123 Eilrechtsschutz, Rücknahme/Widerruf
  §§ 48/49 VwVfG, Ermessen, Nebenbestimmungen, Fortsetzungsfeststellung,
  Normenkontrolle, Verwaltungsvollstreckung); **prozessrecht** (Mahnverfahren,
  einstweilige Verfügung, Arrest, Zwangsvollstreckung, PKH, Versäumnisurteil,
  selbst. Beweisverfahren, Vollstreckungsabwehrklage, Berufung, Beweislast — ZPO);
  **it-recht** (SaaS, Softwareerstellung, Providerhaftung nach DDG/DSA,
  Softwarelizenz-AGB, Open-Source-Compliance, IT-Sicherheit/BSIG, Cloud-AVV,
  Domainrecht, E-Commerce-Pflichten, KI-Verträge). Counts: **49 areas / 159 skills**
  (2,555 eval assertions, 159/159 passing). All case-law marked
  [verifiziert]/[unverifiziert - prüfen]; Providerhaftung built on the current DDG
  (not the repealed TMG), IT-Sicherheit flags the NIS2UmsuCG/BSIG recast.
- **Eight more deepen skills** in four core civil/tax areas (each at one skill
  before): `erbrecht/pflichtteil-pruefung` (§§ 2303 ff. BGB) and
  `erbrecht/gesetzliche-erbfolge` (§§ 1924 ff., § 1931, § 1371 BGB);
  `familienrecht/ehegattenunterhalt` (§§ 1361, 1569 ff. BGB) and
  `familienrecht/kindesunterhalt` (§§ 1601 ff., § 1612a BGB, Düsseldorfer Tabelle);
  `gesellschaftsrecht/gesellschafterbeschluss-anfechtung` (§§ 47/51 GmbHG, analog
  §§ 241/243/246 AktG) and `gesellschaftsrecht/kapitalerhaltung` (§§ 30/31 GmbHG);
  `steuerrecht/einspruch-finanzamt` (§§ 347 ff. AO) and `steuerrecht/selbstanzeige`
  (§§ 371, 398a AO). Counts: **49 areas / 119 skills** (2,004 eval assertions,
  119/119 passing).
- **New area — Wohnungseigentumsrecht (WEG, post-WEMoG)**: a standalone plugin with
  three skills — `beschlussanfechtung` (Anfechtungsklage gegen die Gemeinschaft der
  Wohnungseigentümer §§ 44/45 WEG, Nichtigkeit vs. Anfechtbarkeit § 23 WEG,
  ordnungsmäßige Verwaltung § 19 WEG), `hausgeldabrechnung` (Wirtschaftsplan,
  Abrechnungsspitze und Vermögensbericht § 28 WEG, Verteilung § 16 WEG), and
  `bauliche-veraenderung` (Gestattungsbeschluss und privilegierte Maßnahmen §§ 20/21 WEG
  inkl. E-Mobilität und Steckersolargeräte). All paragraphs verified against the
  post-01.12.2020 WEMoG numbering.
- **Five new deepen skills** in existing areas: `datenschutzrecht/avv-pruefung`
  (AVV-Prüfung Art. 28 DSGVO) and `datenschutzrecht/datenpanne-meldung` (72-Stunden-
  Meldung Art. 33/34 DSGVO); `mietrecht/mieterhoehung-pruefung` (§§ 558 ff. BGB) and
  `mietrecht/eigenbedarfskuendigung` (§§ 573 ff. BGB); `vertragsrecht/verzug-mahnung`
  (Verzug und Verzugszinsen §§ 286, 288 BGB). Counts: **49 areas / 111 skills** (+1 area,
  +8 skills).
- **Deterministic legal calculators** (`scripts/legal_calc/`, stdlib-only, unit-tested):
  Fristenberechnung (§§ 187-193 BGB, § 222 ZPO), Verjährung (§§ 195-199 BGB),
  RVG and GKG fee calculation from version-pinned statutory tables, and a
  Feiertags-engine for all 16 Bundesländer (Easter via Gauß-Algorithmus). CLI
  at `python -m scripts.legal_calc.cli`; documented in `references/rechner.md`.
- **Citation verifier** (`scripts/verify_citations.py`): parses every `§`-anchor,
  ECLI and CELEX in the skills and resolves statute anchors against
  gesetze-im-internet.de. Offline-informational by default; `--online` and
  `--strict` for hard gating.
- **NeuRIS MCP wiring**: a working top-level `.mcp.json` enabling the official
  rechtsinformationen.bund.de open API via a community MIT-licensed server
  (public statutes/case-law only, § 203-safe).
- **Behavioural eval harness** (`scripts/build_eval_config.py` + `evals/`):
  generates a promptfoo config from the `test.md` files with deterministic
  assertions plus LLM-graded `expected_behavior` rubrics (cross-family judge).
  Python remains LLM-free.

### Changed
- CI (`.github/workflows/validate.yml`) now also runs the structural eval,
  the calculator unit tests, and the offline citation check.
- `references/mcp-template.json` updated: the NeuRIS open API and its MCP
  wrapper now exist, replacing the prior "no public legal MCP server" note.

### Fixed
- `scripts/validate.py` and `scripts/route_provider.py` area lists were stale at
  23 areas; synced to the full 48 (closed a CI coverage gap and a provider-parity
  drift the README claimed not to have).
- Fristenberechnung Beginnfrist end-of-month case (§ 188 Abs. 2 Alt. 2 i.V.m.
  Abs. 3 BGB): leap-day and short-month deadlines were one day too early.
- Calculator CLI accepts `--json` after the subcommand and reports domain
  errors cleanly instead of raising a traceback.
- Citation verifier no longer mis-parses German compounds ("DSGVO-konform"),
  trailing Roman-numeral Absätze, four-digit docket years, or example citations
  inside fenced code blocks.

## [0.1.0] - 2026-05-22

### Added
- 48 installable plugins covering 103 skills across German legal practice,
  Fachanwaltschaften, and EU/cross-cutting compliance frameworks.
- Researcher / Drafter / Reviewer sub-agent architecture per area, with
  primary-source statute links and verified/`[unverifiziert]` case-law markers.
- Provider router (`scripts/route_provider.py`) emitting Claude / Gemini / OpenAI
  adapters from one canonical `SKILL.md`.
- Structural eval harness (`scripts/eval.py`), PII redaction
  (`scripts/pii_redact.py`), multi-skill orchestrator (`scripts/orchestrate.py`),
  and the reference set under `references/`.
- Hand-coded static documentation site (166 pages) generated by
  `scripts/generate_site.py`, deployed to GitHub Pages.
