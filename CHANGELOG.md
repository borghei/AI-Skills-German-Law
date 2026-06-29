# Changelog

All notable changes to this project are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Dates are ISO 8601.

## [Unreleased]

### Added
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
