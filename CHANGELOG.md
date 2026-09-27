# Changelog

All notable changes to this project are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Dates are ISO 8601.

## [Unreleased]

_Nothing yet._

## [0.4.1] - 2026-09-27

### Changed

- The eval harness and the gateway example default to current Claude models: the eval runs on `claude-opus-5` (was `claude-opus-4-8`) and the gateway example names `claude-sonnet-5` (was `claude-sonnet-4-6`). Eval scores from earlier runs were measured on the previous generation; re-baseline before comparing.

## [0.4.0] - 2026-08-14

Four areas built around **live 2026 deadlines**, not general topics. Every date
below was read out of the primary text during authoring, and
`verify_citations.py --online` resolves every derived statute link in all four
areas with zero failures.

### Added — the 2026 regulatory wave (62 → 66 areas, 275 → 291 skills)

- **`verbandsklage-vdug` (4 skills)** — Verbraucherrechtedurchsetzungsgesetz.
  Abhilfeklage §§ 14–21 mit Gleichartigkeit § 15, Abhilfegrundurteil § 16,
  kollektivem Gesamtbetrag § 19 iVm § 287 ZPO und **zulassungsfreier Revision**
  § 18 Abs. 4; Musterfeststellungsklage § 41 mit den drei Wirkungen des § 11 —
  einschließlich der übersehenen **Ausnahme des § 11 Abs. 3 S. 2 für
  Abhilfeendurteile**; Zulässigkeit §§ 1–8 mit Quorum von 50 Betroffenen und dem
  **Drittfinanzierungsverbot des § 4 Abs. 2** (Zehn-Prozent-Grenze); Anmeldung
  § 46 und Umsetzungsverfahren §§ 22–40 mit Sachwalter und Umsetzungsfonds.
  **Die schärfste Falle des Gebiets:** Die Anmeldefrist beträgt drei Wochen ab
  Schluss der mündlichen Verhandlung, und **§ 193 BGB ist ausdrücklich
  ausgeschlossen** — ein Fristende am Samstag verschiebt sich nicht.
- **`kritis-resilienz` (4 skills)** — KRITIS-Dachgesetz (CER-RL (EU) 2022/2557),
  **seit März 2026 in Kraft**. Zehn Sektoren § 4 Abs. 1, Registrierung § 8 binnen
  drei Monaten ab **Geltungszeitpunkt** beim **BBK**, Risikoanalyse § 12,
  Resilienzplan § 13 entlang von vier Zielen, Nachweise und Audits § 16,
  Vorfallmeldung § 18 mit **24 Stunden ab Kenntnis** und Monatsbericht,
  Geschäftsleiterpflicht § 20 und Bußgelder bis 1 Mio. EUR § 24. Zwei Fallen
  sind eigens ausgewiesen: Das Dachgesetz regelt die **physische** Resilienz
  neben NIS2/BSIG (zwei getrennte Registrierungen), und der Ausnahmekatalog des
  **§ 4 Abs. 2 erfasst § 8 nicht**.
- **`entgelttransparenz-eu` (4 skills)** — RL (EU) 2023/970. Die Umsetzungsfrist
  des Art. 34 lief am **07.06.2026 ab; Deutschland hat sie versäumt**. Die Skills
  trennen deshalb drei Ebenen: geltendes EntgTranspG in richtlinienkonformer
  Auslegung, unmittelbar wirkendes **Art. 157 AEUV** auch zwischen Privaten, und
  Richtlinienbestimmungen ohne Umsetzung — **keine** horizontale Wirkung,
  gegenüber staatlichen Arbeitgebern je Bestimmung zu prüfen, dazu Staatshaftung.
  Auskunft Art. 7 (zwei Monate) gegen §§ 10 ff. EntgTranspG (drei Monate),
  Berichterstattung Art. 9 ab **07.06.2027 über das vorangehende Kalenderjahr**,
  gemeinsame Entgeltbewertung Art. 10 ab **5 %** ohne Korrektur binnen sechs
  Monaten, und die **Beweislast-Vollumkehr des Art. 18 Abs. 2** bei verletzten
  Transparenzpflichten.
- **`krypto-mikar` (4 skills)** — MiCAR (VO (EU) 2023/1114) und **KMAG**.
  Vorrangprüfung gegen MiFID II, KWG, KAGB und ZAG, Tokenklassen mit dem
  Emittentenvorbehalt des Art. 48 für E-Geld-Token, Whitepaper Art. 6 (nach
  Art. 8 nur **übermittelt, nicht gebilligt**) mit doppelter Haftung aus Art. 15
  MiCAR **und** § 19 KMAG, CASP-Zulassung Art. 59 ff., Marktmissbrauch
  Art. 86–92. **Der zentrale Fund:** MiCAR lässt Bestandsanbieter nach
  Art. 143 Abs. 3 bis zum **01.07.2026** weiterarbeiten und erlaubt den
  Mitgliedstaaten ausdrücklich eine Verkürzung — **Deutschland hat verkürzt**:
  Nach **§ 50 Abs. 2 Nr. 3 KMAG** erlosch die fortbestehende Erlaubnis
  **spätestens mit Ablauf des 31.12.2025**. Wer mit dem Unionsdatum rechnet,
  liegt sechs Monate daneben.

Verifikationsstand: Für keine der vier Areas wurde ein Rechtsprechungslauf
durchgeführt — zu VDuG, KRITIS-DachG, RL (EU) 2023/970, MiCAR und KMAG existiert
**praktisch keine Judikatur**. Die Skills behaupten deshalb keine Aktenzeichen,
benennen die Streitfelder und markieren jede erinnerte Entscheidung mit
`[unverifiziert – prüfen]`.

### Fixed

- **`scripts/verify_citations.py` — BörsG-Slug.** Die Abkürzung war auf
  `boersg_2007` gemappt; gesetze-im-internet.de kodiert den Umlaut als
  Unterstrich und serviert das Börsengesetz unter **`b_rsg_2007`**. Alle
  BörsG-Zitate des Repos schlugen im `--online`-Lauf mit HTTP 404 fehl. Durch
  einen Regressionstest gepinnt.
- **`scripts/verify_citations.py` — fehlende Abkürzungen.** Ergänzt: VDuG,
  KapMuG, KRITISDachG nebst der Kurzform KRITIS (aus „§ 18 KRITIS-Dachgesetz")
  und KMAG.
- **`scripts/generate_site.py` — Navigationsleiste auf dem Telefon.** Bei 390 px
  umbrach die Serifen-Wortmarke auf vier Zeilen und die Sprachumschaltung wurde
  über den rechten Rand gedrückt. Die Leiste stapelt jetzt unterhalb von 480 px,
  die Wortmarke bleibt einzeilig, und die Navigationslinks scrollen horizontal
  statt überzulaufen. Gefunden bei der Live-UI-Prüfung des v0.3.0-Ships.

### Changed

- README, QUICKSTART, `skills.json`, die generierte Website und die
  Eval-Konfiguration spiegeln 66 Areas und 291 Skills.


## [0.3.0] - 2026-08-14

Everything below this heading was on `main` but never tagged. `0.3.0` is the
first annotated release; it carries the four new practice areas of 2026-08-14
together with the previously untagged 2026-07-21 corrections.

### Added — four new practice areas (2026-08-14)

The library grows from **58 areas / 258 skills** to **62 areas / 275 skills**.
Each new area was drafted against the primary sources, not from model memory:
the statute texts were pulled from gesetze-im-internet.de and EUR-Lex during
authoring, and every derived statute URL resolves in `--online` mode.

- **`datenwirtschaftsrecht` (5 skills)** — EU-Datenverordnung (Data Act,
  VO (EU) 2023/2854) und ihre deutsche Durchführung im **DADG**. Betroffenheit
  und Rollen je Datenstrom, Zugangsanspruch Art. 4/5 mit dem prozeduralen
  Geschäftsgeheimnisschutz des Art. 4 Abs. 6–8, Gegenleistung Art. 9 mit dem
  KMU-Kostendeckel des Abs. 4, Missbrauchskontrolle Art. 13 gegenüber
  §§ 305 ff. BGB, Cloud-Wechsel Art. 23–31 und B2G-Zugang Art. 14–22.
  Zuständige Behörde ist die **Bundesnetzagentur** (§ 2 Abs. 1 DADG), für
  personenbezogene Daten die BfDI (§ 16 DADG); Bußgeldrahmen aus § 15 DADG.
  Der gestaffelte Geltungsbeginn des Art. 50 (12.09.2025 / 12.09.2026 /
  12.01.2027 / 12.09.2027) ist in jeder Skill ein eigener Prüfungsschritt.
- **`barrierefreiheit-bfsg` (4 skills)** — BFSG und BFSGV, anwendbar seit dem
  **28.06.2025**. Abschließende Produkt- und Dienstleistungskataloge des § 1,
  Kleinstunternehmensausnahme des § 3 Abs. 3 **nur für Dienstleistungen**,
  Konformitätsnachweis §§ 6/18/19 mit Anlage 2, Dienstleisterpflichten § 14 mit
  den vier Pflichtbestandteilen der Anlage 3, Ausnahmen §§ 16/17 mit Anlage 4
  und der Sperre des § 17 Abs. 4, Marktüberwachung mit der Zehn-Tage-Untergrenze
  des § 22 Abs. 2 S. 2 und Bußgeld bis 100.000 EUR. Eine vierte Skill deckt das
  getrennte Regime der öffentlichen Stellen ab (BGG §§ 12a/12b, BITV 2.0,
  Gebärdensprache und Leichte Sprache nach § 4 BITV 2.0 — ohne Bußgeldtatbestand).
- **`schiedsverfahren-adr` (4 skills)** — Zehntes Buch der ZPO §§ 1025–1066.
  Schiedsvereinbarung mit der Verbraucherform des § 1031 Abs. 5, Verfahrensführung
  §§ 1034–1058, Aufhebung § 1059 mit der **Dreimonatsfrist ab Empfang** und der
  Präklusion des § 1060 Abs. 2 S. 3, Vollstreckbarerklärung §§ 1060/1061 mit
  Art. V und VII des New Yorker Übereinkommens. Alle Skills weisen aus, dass die
  Änderungen des **G v. 20.05.2026 (BGBl. 2026 I Nr. 152)** auf
  gesetze-im-internet.de textlich nachgewiesen, dokumentarisch aber noch nicht
  abschließend eingearbeitet sind, und markieren das mit `[unverifiziert – prüfen]`.
- **`gewerberecht` (4 skills)** — GewO und HwO. Untersagung § 35 einschließlich
  der **Sperrwirkung des Abs. 8**, erlaubnispflichtige Gewerbe §§ 34a/34c/34d/34f/34i
  nebst MaBV mit den widerlegbaren Regelvermutungen des § 34c Abs. 2, Anzeige § 14
  und Betrieb ohne Zulassung § 15 Abs. 2, Reisegewerbe §§ 55 ff. und Marktprivileg
  §§ 69/69a, Handwerksrolle §§ 1/7/7b/8 und Untersagung § 16 Abs. 3 HwO mit der
  gemeinsamen Erklärung von Handwerkskammer und IHK als Zulässigkeitsvoraussetzung.

Coverage note: keine der vier Areas hat bislang einen Verifikationslauf nach
`VERIFICATION_STATUS.md`. Zu Data Act, DGA und BFSG existiert praktisch **keine
Rechtsprechung**; die Skills arbeiten deshalb bewusst mit Normtext,
Erwägungsgründen und Behördenverlautbarungen und markieren jede erinnerte
Entscheidung als `[unverifiziert – prüfen]`.

### Fixed — toolchain defects found while adding the areas (2026-08-14)

- **`scripts/verify_citations.py` — UWG-Slug.** Die Abkürzung war auf `uwg`
  gemappt; gesetze-im-internet.de serviert das UWG unter `uwg_2004`. Im
  `--online`-Lauf schlugen dadurch **alle 144 UWG-Zitate** des Repos mit HTTP 404
  fehl, obwohl die Zitate korrekt waren.
- **`scripts/verify_citations.py` — EGBGB.** gesetze-im-internet.de veröffentlicht
  für das EGBGB **keine** Einzelartikel-Seiten (`art_1`, `art_229`, `art_246`,
  `art_247` sind sämtlich 404). Der abgeleitete Link wurde als Fehler gewertet;
  betroffen waren alle 44 EGBGB-Zitate. Solche Normen werden jetzt informativ auf
  den konsolidierten Volltext verwiesen statt als Fehlschlag gemeldet.
- **`scripts/verify_citations.py` — fehlende Abkürzungen und Nicht-Normen.**
  Ergänzt: DADG, DGG, DNG, BFSG, BFSGV, BGG, BITV 2.0, HwO, GastG, MaBV
  (`gewo_34cdv`), MediationsG, BBiG, WpIG, UKlaG, RDGEG sowie die CELEX-Nummern
  für RL (EU) 2019/882 und 2016/2102. `UAbs.`, `Unterabs.` und `CE` werden nicht
  mehr als Gesetzesabkürzung gelesen.
- **`produktrecht/skills/prodhaftg-herstellerhaftung/test.md` — kaputtes YAML.**
  Ein deutsches Schlusszeichen innerhalb eines doppelt gequoteten Scalars beendete
  den String vorzeitig; die Frontmatter war nicht parsebar und die Skill fiel
  **still aus der Eval-Konfiguration heraus**. `build_eval_config.py` erfasst
  jetzt wieder alle Skills (275 statt 274).
- **`scripts/eval.py` — Frontmatter-Parser.** Der Tiny-Parser entfernte nur
  **doppelte** Anführungszeichen um einen Scalar. Ein einfach gequoteter Eintrag —
  die korrekte YAML-Form, sobald der Wert selbst ein doppeltes Anführungszeichen
  enthält — behielt seine Delimiter und konnte nie gegen den SKILL.md-Body
  matchen. Jetzt werden beide Quote-Arten entfernt.
- **`scripts/build_skills_json.py` — Plugin-Zahl.** Die Beschreibung in
  `skills.json` nannte hartkodiert „48 plugins" und war damit 14 Areas hinter dem
  Katalog, den sie beschreibt. Sie wird jetzt wie die Skill-Zahl abgeleitet.

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
