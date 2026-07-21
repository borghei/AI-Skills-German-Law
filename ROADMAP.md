# Expansion & Correction Roadmap — ai-skills-german-law

Research date: **2026-07-21**. Repo state at time of the original audit: **49 areas / 189 skills**.
**Current state: 58 areas / 258 skills.** Phases 1–5 are done; what remains is Part 4 (verification) and the Tier-2 areas in Part 2b.

> Verification status is marked per item: **[verified]** = confirmed against a primary source; **[reported]** = single-sourced, re-check before it enters skill text; **[DO NOT ASSERT]** = actively could not be confirmed, treat as unknown.

---

## Status — what shipped on 2026-07-21

| Phase | Status |
|---|---|
| 1 — correct superseded law | **done** (PR #2) — `ki-vo-compliance`, `lieferkettengesetz`, `energierecht`/`baurecht`, `csrd`, `kapitalmarktrecht`, `produktrecht`, `vergaberecht`, `geldwaesche-aml-kyc`, `it-recht` |
| 2 — `cyber-resilience-act` | **done** (PR #2) — 4 skills, ahead of the 11.09.2026 reporting deadline |
| 3 — depth + calculators | **done** (PR #2) — `vertragsrecht` 2→14, `arbeitsrecht` 3→14, `mietrecht` 3→13 (duplicate merged); `legal_calc` gained § 622 BGB and §§ 288/247 BGB, tests 29→47, wired skills 2→11 |
| — bilingual site | **done** (PR #3) — EN at root, DE at `/de/`, reciprocal hreflang, EN URL set unchanged |
| — validator fixes | **done** (PR #4) — 5 gaps closed, plugin versions aligned to 0.2.0 |
| 5 — eight new areas | **done** (PR #4) — see Part 2b Tier 1 |
| 4 — verification | **in progress** — the remaining priority; see Part 4 |

### Corrections found by reading primary text rather than trusting recall

These all contradicted the planning assumptions in this document or the briefs derived from it. They are the argument for fetching statutes:

- **§ 34 BDG is no longer *Disziplinarklage*.** Since the Neuregelung des Bundesdisziplinarrechts (Art. 6 G v. 19.7.2024, BGBl. 2024 I Nr. 247) every federal measure — including Entfernung aus dem Beamtenverhältnis — issues as **Disziplinarverfügung** (§§ 33, 34 Abs. 4 BDG). The Disziplinarklage survives in most Länder, so the Bund/Land determination changes the entire procedural posture.
- **§ 64 Abs. 3 AO is 50.000 EUR**, not 45.000. Also: § 55 Abs. 1 Nr. 5 S. 4 AO exempts bodies with income up to 100.000 EUR from zeitnahe Mittelverwendung.
- **§ 84a Abs. 2 BGB codifies** the business judgment rule for Stiftungsvorstände — not an analogy to § 93 Abs. 1 S. 2 AktG.
- **[verified] The Stiftungsregister starts 01.01.2028, not 01.01.2026.** Postponed by **Art. 33 G v. 08.12.2025 (BGBl. 2025 I Nr. 319)**. The Inkrafttretensfußnote on §§ 18 and 20 StiftRG reads: *"Tritt gem. Art. 11 Abs. 1 Nr. 2 G v. 16.7.2021 I 2947 idF d. Art. 33 G v. 8.12.2025 I Nr. 319 am 1.1.2028 in Kraft"*. Only § 19 (Verordnungsermächtigung) is in force. Much of the literature still says 2026; building on that terminates Eintragungspflicht, Namenszusatz and Publizitätswirkung two years early.
- **§ 13 ProdHaftG runs ten years**, so the 1989 and 2026 liability regimes coexist into the 2030s — the skill needed a placing-on-market weichenstellung, not a replacement.
- **Art. 17 MAR decoupling:** intermediate steps are no longer ad-hoc disclosable but remain *Insiderinformation* for Art. 14/10/18. The mirror-image error (treating a Zwischenschritt as legally irrelevant) is the one the correction itself invites.

---

## PART 0 — Priority queue by deadline

| Date | Item | Repo state |
|---|---|---|
| **31 Jul 2026** | NIS2 BSI-registration Nachfrist (~11.5k of ~29.5k entities registered) | `nis2` exists; Nachfrist absent |
| **31 Jul 2026** | Right-to-Repair transposition (Dir 2024/1799) — Germany likely to miss | no coverage |
| **2 Aug 2026** | **AI Act general application + Art. 50 transparency; GPAI enforcement/fines begin** | `ki-vo-compliance` dates wrong |
| **12 Aug 2026** | PPWR applies; PFAS limits on food-contact packaging | no coverage |
| **11 Sep 2026** | CRA reporting: 24h / 72h / 14d | no dedicated area |
| **27 Sep 2026** | EmpCo greenwashing regime via UWG | `wettbewerbsrecht` (3 skills) |
| **2 Dec 2026** | Platform Work transposition; 2 new AI prohibitions (NCII, CSAM) | no coverage |
| **9 Dec 2026** | New ProdHaftG — software becomes a product, €85m cap gone | `produktrecht` stale |
| **30 Dec 2026** | EUDR (large/medium) | no coverage |
| **1 Jan 2027** | eRechnung mandatory issuing >€800k turnover | `steuerrecht` (3 skills) |
| *in force* | GModG (10 Jul), Listing Act MAR (5 Jun), Vergabebeschleunigungsgesetz (1 Jul), BTTG (1 May), Pay Transparency (8 Jun) | 4 areas stale, 2 uncovered |

---

## PART 1 — Corrections to existing skills (do first)

Skills teaching superseded law are worse than missing skills: they generate confident wrong output.

### 1.1 `lieferkettengesetz/skills/bafa-bericht-lksg` — **[verified]**
BAFA's own page confirms review of §§ 12, 13 LkSG reports **stopped 3 Sep 2025** and the submission portal is **closed**.
**Nuance that matters:** this is a *Weisung an das BAFA* preempting the amendment ("greift der Gesetzesnovelle vor"), **not a statutory repeal**. The duty formally exists but is unenforced and unfileable.
→ Action: rewrite as a status/transition skill, or retire it. Risikoanalyse + Beschwerdeverfahren remain live.

### 1.2 `energierecht` + `baurecht` — **[verified]**
**GModG passed Bundestag 10 Jul 2026, 323:271.** Struck: **§§ 71, 71b–71p, § 72 GEG**. The 65%-renewables rule is **gone**; replaced by a Bio-Quote from 2029, climate-neutral fuels by 2045, free heating choice from Nov 2026. Building-level duties now key off the municipal **Wärmeplan (WPG)** — deadline 30 Jun 2026 (>100k inhabitants) / 30 Jun 2028 (<100k).
→ Action: purge all 65%-rule content; re-anchor to WPG.

### 1.3 `ki-vo-compliance` (4 skills) — **[reported]**
Digital Omnibus on AI: EP 16 Jun 2026, Council 29 Jun 2026.
- Annex III standalone high-risk → **2 Dec 2027**
- Annex I embedded high-risk → **2 Aug 2028**
- **Art. 50 transparency unchanged → 2 Aug 2026**
- **GPAI (Arts. 51–55) NOT deferred**; enforcement powers + fines from **2 Aug 2026** (Art. 101: 3% worldwide turnover or €15m)
- Art. 57 sandbox deadline **2 Aug 2026 → 2 Aug 2027**
- Two **new prohibitions** (non-consensual intimate imagery, CSAM) from **2 Dec 2026** → update `verbotene-ki-praktiken`

GPAI detail for `gpai-pflichten`:
- Code of Practice final **10 Jul 2025**; 23 signatories. **Meta did not sign.** xAI signed Safety & Security chapter only.
- Training-content summary **template mandatory**, published 24 Jul 2025; refresh every 6 months or on material change.
- **Art. 52(1)**: notify Commission **within 2 weeks** of crossing/expecting to cross **10^25 FLOP**.
- **Art. 53(2)** open-source exemption covers (a)+(b) only — copyright policy and training summary apply regardless.
- **Art. 111(3)**: models on market before 2 Aug 2025 have until **2 Aug 2027**.

### 1.4 German KI-MIG — new content, high value — **[reported]**
**KI-Marktüberwachungs- und Innovationsförderungsgesetz (KI-MIG)**, Art. 1 of the Gesetz zur Durchführung der VO (EU) 2024/1689.
Bundestag **11 Jun 2026** (BT-Drs. 21/6407) · Bundesrat **10 Jul 2026** (BR-Drs. 375/26(B)) · **NOT yet promulgated in BGBl. as of 21 Jul 2026** — sits between Bundesrat approval and Ausfertigung. Art. 5: in force the day after Verkündung. Intent is clearly to beat 2 Aug 2026.

Authority map:
- **BNetzA = Auffangzuständigkeit** (§ 2 Abs. 1) — not a new AI agency
- **KoKIVO** (§ 5) — coordination/competence centre
- **KI-Marktüberwachungskammer (UKIM)** (§§ 2 Abs. 5, 4) — *independent* 3-member chamber for Annex III No. 1 biometrics in law enforcement/border/justice/democracy + Annex III Nos. 6, 7, 8
- **BaFin** (§ 2 Abs. 3, 4) — AI in regulated financial activity
- **Annex I Section A products** (§ 2 Abs. 2) — existing sectoral authorities (KBA etc.); Germany does **not** use the Art. 74(3) derogation
- **BSI** — notifying authority for Annex III No. 1 *interim only*, until the CRA Art. 52(2) authority is designated
- **Länder** — public bodies of the Länder; Landesmedienanstalten for media services
- **BMF** (§ 2 Abs. 7) — BNetzA needs Einvernehmen against Bundesfinanzbehörden
- National add-on Bußgelder: **up to €50,000** (§ 15); the KI-VO's own fines apply directly

**Two traps to encode:**
1. **BfDI is NOT the AI market surveillance authority** for biometrics/law enforcement — the DSK claimed it (Positionspapier 3 May 2024), the legislator routed it to UKIM instead. Many secondary sources get this wrong.
2. **Notifying authority is sectoral/decentralised (§ 3)** — *not* BNetzA, *not* DAkkS. The RegE's own Erfüllungsaufwand section says "BNetzA is the notifying authority," contradicting its operative § 3; law-firm summaries repeat the error. DAkkS only assesses/monitors conformity assessment bodies.

⚠️ § numbers above are from the **Regierungsentwurf**; Bundestag adopted a modified text (21/6407) not obtained. Verify against the promulgated version.

### 1.5 `csrd` + `lieferkettengesetz` scope — **[reported]**
**Omnibus I = Dir (EU) 2026/470**, OJ 26 Feb 2026, **in force 18 Mar 2026**.
- CSRD: **>1,000 employees AND >€450m** net turnover (Parliament's 1,750 rejected); transposition 19 Mar 2027
- CSDDD: **>5,000 employees AND >€1.5bn**; transposition 26 Jul 2028, substantive duties 26 Jul 2029
- Wave-1 companies below the new thresholds are out for FY2025–2026
- Third-country: >€450m parent EU turnover / >€200m subsidiary or branch
- ESRS revision still running → mark as in flux

### 1.6 `kapitalmarktrecht/wphg-marktmissbrauch` — **[reported]**
EU Listing Act, final wave applied **5 Jun 2026**: under Art. 17 MAR only the **final event** in a protracted process is ad-hoc disclosable — intermediate steps no longer. A Delegated Regulation lists **35 protracted processes** across 7 categories. Material change to German Ad-hoc practice; Ad-hoc committees need retraining.

### 1.7 `produktrecht/prodhaftg-herstellerhaftung` — **[reported]**
Dir (EU) 2024/2853, transposition **9 Dec 2026**. Germany: RefE 11 Sep 2025 · RegE Dec 2025 (BT-Drs. 21/4297) · 1. Lesung 4 Mar 2026 · in Rechtsausschuss. The 1989 ProdHaftG is **fully repealed and replaced**. Software/SaaS/AI are products regardless of embodiment; **€85m cap abolished**; damage extends to data loss and medically recognised psychological harm; disclosure duties + rebuttable causation presumptions. Products placed on market up to 8 Dec 2026 stay under the old regime.

### 1.8 Delete, don't update — **[reported]**
**Green Claims Directive was withdrawn** (Commission announcement 20 Jun 2025). Greenwashing risk moves entirely to **Empowering Consumers Dir (EU) 2024/825** → UWG, applying **27 Sep 2026**.

### 1.9 Other stale anchors — **[reported]**
- `vergaberecht`: **Vergabebeschleunigungsgesetz in force 1 Jul 2026** (do NOT cite the old Ampel-era name "Vergaberechtstransformationsgesetz"); **BTTG** (Bundestariftreuegesetz) BGBl. 2026 I Nr. 119, in force **1 May 2026**, threshold €50,000 net
- `geldwaesche-aml-kyc`: AMLD6 UBO-register transposition **10 Jul 2026**; AMLR applies 10 Jul 2027; AMLA operational in Frankfurt since 1 Jul 2025; EU-wide €10,000 cash cap
- `it-recht`: Data Act applicable 12 Sep 2025; German **DADG** in BGBl. 29 May 2026, **BNetzA** competent; Art. 3(1) access-by-design for products placed on market after **12 Sep 2026**; switching fees abolished 12 Jan 2027

---

## PART 2 — New areas, ranked

### 2a. EU compliance regimes (deadline-driven)
1. **`cyber-resilience-act`** — 11 Sep 2026 reporting (24h early warning / 72h full / 14d final via ENISA Single Reporting Platform); 11 Dec 2027 full application; fines to €15m or 2.5%
2. **`data-act`** — IoT contract re-papering, Art. 5 third-party requests, cloud exit clauses
3. **`cbam`** — definitive regime live 1 Jan 2026; 50t threshold; DEHSt authorisation; certificates from Feb 2027; first surrender 30 Sep 2027
4. **`barrierefreiheit-bfsg`** — in force 28 Jun 2025, **actively enforced** (MLBF Magdeburg since Sep 2025, Abmahnwellen); €100k fines; written Unverhältnismäßigkeit assessment (§ 17 BFSG) required
5. **`entgelttransparenz`** — Germany **in default** since 8 Jun 2026; direct vertical effect against public employers; joint pay assessment at ≥5% unexplained gap; reversed burden of proof
6. **`eudr`** — 30 Dec 2026 / 30 Jun 2027; TRACES DDS; treat dates as unstable (twice delayed)
7. **`ppwr`** — applies 12 Aug 2026; PFAS food-contact limits
8. **`forced-labour-regulation`** — prohibition 14 Dec 2027; market-ban regime with no due-diligence duty, so it catches companies *outside* the narrowed CSDDD scope

### 2b. German practice areas — top 20 (volume × automatability)
No FAO Fachanwaltstitel is missing at area level. Gaps are sub-domains and non-FAO commercial/public-law markets.

1. **Immobilien-, Grundstücks- u. Grundbuchrecht + Beurkundung** — largest German document market. §§ 311b, 873, 925, 1113 BGB; GBO §§ 13, 19, 29, 39; BeurkG §§ 17, 13a; § 24 BauGB Vorkaufsrecht
2. **Zwangsvollstreckung / ZVG** — PfÜB §§ 829, 835 ZPO, § 850c, P-Konto § 850k, § 802c, ZVG §§ 15, 30a, 180
3. **Kostenrecht RVG/GKG + Anwaltshaftung** — every mandate; § 14 RVG, VV 2300/3100, §§ 103–107 ZPO, § 3a, § 4a
4. **Wirtschafts- u. Steuerstrafrecht + Internal Investigations** — §§ 370, 371, 398a AO; §§ 263, 266, 266a, 299 StGB; §§ 30, 130 OWiG; § 73 StGB; Beschlagnahmeschutz § 97 StPO
5. **M&A / Transaktionsrecht** — § 15 III/IV GmbHG, § 613a BGB, § 25 HGB, § 1 IIa/IIb GrEStG
6. **Vereins-, Stiftungs- u. Gemeinnützigkeitsrecht** — ~615k Vereine; §§ 21–79, 80–88 BGB (2023 reform); §§ 51–68 AO, § 60 Mustersatzung
7. **Beamten- u. Disziplinarrecht** — BeamtStG §§ 33–47, BDG, Konkurrentenstreit Art. 33 II GG + § 123 VwGO
8. **Reiserecht + Fluggastrechte** — VO 261/2004; §§ 651a–651y BGB. Highest-automation mass market
9. **Bauplanungsrecht / Raumordnung / Denkmalschutz / Enteignung** — BauGB §§ 1–13b, 29–35, 11, 127 ff., 85 ff.
10. **Vertragsarzt-, Krankenhaus- u. Pflegerecht** — §§ 95–103, 106–106c SGB V; KHEntgG; §§ 84 ff. SGB XI
11. **IPR/Kollisionsrecht + Schiedsverfahren** — Rom I/II, Brüssel Ia, §§ 1025–1066 ZPO, DIS-SchO. *Completes the FAO "Internationales Wirtschaftsrecht" title*
12. **Schul-, Hochschul- u. Prüfungsrecht** — Bewertungsspielraum vs. Antwortspielraum, Überdenkensverfahren, KapVO
13. **Erbschaft-/Schenkungsteuer + Unternehmensnachfolge** — §§ 13a/13b, 28a ErbStG; §§ 199 ff. BewG. Highly computational → strong calculator fit
14. **Polizei-, Ordnungs-, Versammlungs- u. Waffenrecht** — Länder-PolG, VersammlG §§ 15, 17a, WaffG §§ 4–6, 45
15. **Vertriebsrecht** — §§ 84–92c HGB, § 89b, Vertikal-GVO (EU) 2022/720, Franchise-c.i.c.
16. **Arzneimittel-, Medizinprodukte- u. Apothekenrecht** — AMG, MDR + MPDG, HWG, ApoG, §§ 35a, 130b SGB V
17. **Kommunal- u. Kommunalabgabenrecht** — GO/KV, KAG, § 47 VwGO
18. **Kapitalanlage-/Fondsrecht (KAGB)** — §§ 20–22 VermAnlG, §§ 63, 64 WpHG, KapMuG
19. **Gewerbe-, Gaststätten- u. Glücksspielrecht** — GewO §§ 33c–33i, 34c, 35; GlüStV 2021; § 134 BGB Rückforderungswelle
20. **Telekommunikations-, Post- u. Rundfunkrecht** — TKG 2021 §§ 51–71 (§ 56 Laufzeit, § 57 Minderung) — Massengeschäft

**Sub-domain fills inside existing areas:** Architekten-/Ingenieurrecht (HOAI 2021, § 650p BGB) inside `baurecht`; Vertragsarztrecht inside `medizinrecht`; Restrukturierung/IDW S 6 inside `insolvenzrecht`.

**Tier 2:** Lebensmittelrecht, Jugendhilferecht SGB VIII, EU-Beihilfen-/Subventionsrecht, Wasser-/Bergrecht, Berufsrecht anderer Berufe, Kunst-/Kulturgüterrecht, Seerecht, Eisenbahnrecht, Wein-, Tier-/Jagdrecht, Staatskirchenrecht, Wehrrecht.
**Skip:** Weltraumrecht, Futtermittel/Kosmetik as standalone, Legal-Tech-Recht, Handwerksrecht (→ skill inside Gewerberecht).

---

## PART 3 — Depth in existing thin areas

The four areas expanded to 11 skills average **93–113 lines**; original hand-built areas average **169**. Growth traded depth for count. Full per-area task lists (with §§ anchors) were produced for: arbeitsrecht, mietrecht, familienrecht, erbrecht, vertragsrecht, gesellschaftsrecht, handelsrecht, steuerrecht, datenschutzrecht, versicherungsrecht, verkehrsrecht, sozialrecht.

Highest-ROI targets:
- **`vertragsrecht` 2 → 14** — largest relative gap; its own plugin.json advertises c.i.c., Leistungsstörung, Anfechtung, Rücktritt, none of which exist. Add: Kaufmängel §§ 434–441, Werkvertrag §§ 631–650v, Rücktritt/SE §§ 280–325, Verbraucherwiderruf §§ 312g/355, Verjährung §§ 195–204, Sicherheiten, Vertragsstrafe §§ 339–345, § 313, Abtretung, Anfechtung §§ 119–124, Vergleich § 779, NDA/LOI/c.i.c., Freelancer/Scheinselbständigkeit § 7 SGB IV
- **`arbeitsrecht` 3 → 14** — Kündigungsschutzklage § 4 KSchG, Betriebsratsanhörung § 102 BetrVG, Massenentlassung §§ 17/18 KSchG (BAG-Wende 2024), Sozialauswahl § 1 III, Zeugnis § 109 GewO, Befristung § 14 TzBfG, AGG § 15, § 613a, Urlaub/BUrlG, Wettbewerbsverbot §§ 74–75d HGB, BEM § 167 II SGB IX, § 87 BetrVG — **plus Entgelttransparenz**
- `mietrecht` 3 → 13, `familienrecht` 3 → 13, `erbrecht` 3 → 13, `gesellschaftsrecht` 3 → 13 (incl. MoPeG §§ 705–740c + § 47 II GBO Voreintragungsobliegenheit)

---

## PART 4 — Structural / engineering debt

### 4.1 Verification debt (quantified)
- **660 `[unverifiziert]` markers** across 143 skills; **498 citation warnings** from `verify_citations.py`
- `VERIFICATION_STATUS.md`: of 9 plugins verified, **11 citation errors caught (~10% error rate)**; **16 plugins never verified**; 40 of 49 areas have no verification record
- Worst: urheber-medienrecht (55), geldwaesche-aml-kyc (40), agrarrecht (38), energierecht (35), sportrecht (34)
- Unresolved contradictions in `urheber-medienrecht`: "Das Boot II" vs "Talking to Addison" both cited as I ZR 145/11; Tchibo/Rolex II and Gemeinkostenanteil cited inconsistently between `agents/researcher.md` and the skill

### 4.2 `legal_calc/` is orphaned
29 tests, deterministic Fristen/Verjährung/RVG/GKG — referenced by **2 of 189 skills**. This is the repo's clearest differentiator (LLMs hallucinate exactly here).
Extend to: Düsseldorfer Tabelle (Kindesunterhalt), Zugewinnausgleich, Pflichtteilsquote, ErbSt §§ 13a/13b, Kündigungsfristen § 622 BGB, Verzugszinsen § 288, Handelsvertreterausgleich § 89b HGB, Mieterhöhungs-Kappungsgrenze, Pfändungsfreigrenzen § 850c ZPO.

### 4.3 Empty scaffolding advertised as features
- `adapters/claude|gemini|openai/` — **all empty**, while README/llms.txt advertise multi-provider adapters
- root `tests/` — empty
- **22 areas have empty `agents/`**, yet **81 SKILL.md files declare `agents:` frontmatter** pointing at `../../agents/*.md` that don't exist. Nothing validates these paths
- 28 of 29 `providers/` dirs empty (only `arbeitsrecht/kuendigungs-pruefung/providers/claude.md` exists, auto-generated)

### 4.4 Duplicates
- **`mietrecht/mieterhoehung-558-bgb` vs `mieterhoehung-pruefung`** — genuine duplicate; both cover §§ 558a, 558 III, 558b. Merge into one skill with Entwurf/Prüfung modes, or split cleanly § 558 Vergleichsmiete vs § 559 Modernisierung
- `gewerblicher-rechtsschutz/patentverletzung-pruefung` vs `patentrecht/patentverletzung-klage` — the latter is a strict superset. Patent is outside `gewerblicher-rechtsschutz`'s declared scope (MarkenG/DesignG/UWG). Drop or cross-reference

### 4.5 Count/date drift
- `skills.json:3` says "48 plugins" — actual 49
- README badge "Last verified 2026-05-22" vs QUICKSTART "2026-05-21"; `skills.json` updated 2026-06-29
- "2,982 eval assertions" hard-coded in README:192 and CHANGELOG:19, recomputed by nothing
- Version: `skills.json` 0.2.0 vs all 49 `plugin.json` at 0.1.0; everything still under `## [Unreleased]`
- Area READMEs systematically stale (`it-recht/README.md` lists 1 shipped + 4 *(geplant)* against 11 actually shipped, with wrong names)

### 4.6 Machinery — what a new AREA requires
Five hard-coded lists plus generators:
- `scripts/validate.py` AREAS (lines 33–83) — omit and the area is **silently never validated**
- `scripts/eval.py` AREAS (lines 30–80)
- `scripts/build_skills_json.py` **DOMAINS_ORDER (19–41) AND DOMAIN_META (43–96)** — **KeyError if you add to one only**
- `.claude-plugin/marketplace.json` plugins[]
- README badges/prose (:10, :11, :43, :89, :106, :231, :336), QUICKSTART (:11, :58), VERIFICATION_STATUS.md, CHANGELOG
- Generator order: `build_skills_json.py` → `generate_site.py` → `build_eval_config.py`
- New SKILL additionally always needs `test.md` (validate.py:180 errors; eval.py:165 fails)

**CI gap:** `.github/workflows/pages.yml` deploys `site/` but does **not** run the generators — a stale site ships silently.
**Validator gaps:** `agents/` and `tests/` are in the docstring but never checked; `name:` frontmatter is never compared to the directory name; `--strict` case-law heuristic only recognises NZA/NJW, so a GRUR- or BVerwGE-only skill fails spuriously.

---

## PART 5 — Do NOT assert (verification failed this session)

1. **No Commission list of designated systemic-risk GPAI models exists.** Art. 52(6) requires one; none found. Do **not** repeat the secondary claim naming GPT-4/Gemini Ultra/Claude 3 Opus/Llama 3 405B.
2. **No confirmed Vertragsverletzungsverfahren** against Germany over Art. 70 KI-VO. Commission page still shows "–" for Germany; ~8 of 27 Member States have notified. Risk is real; an opened proceeding is not confirmed.
3. **No BGBl. citation for KI-MIG** as of 21 Jul 2026.
4. **ZuFinG II** enactment status unconfirmed — check DIP.
5. **PSD3/PSR** application dates — texts agreed 23 Apr 2026, OJ publication unconfirmed. No firm date.
6. **Blaue-Karte-EU 2026 salary thresholds** — check BeschV.
7. **OLG Hamburg (LAION appeal, 10 Dec 2025) Aktenzeichen** — commonly cited as 5 U 145/24, unverified; BGH Revision docketing unknown.
8. **BAG 1 ABR 24/22** (ChatGPT/Mitbestimmung) — cited from memory, unverified.
9. **No LG/OLG Köln decision on AI training data** could be found. The other leading case is LG München I, 11 Nov 2025 (GEMA ./. OpenAI), a different doctrinal question.
10. **FIDA** — still in trilogue, application realistically 2029–30. Do not build for it.
11. **MDR/IVDR reform** (proposal 16 Dec 2025) — adoption not before Q2 2027 and it does **not** extend transition periods. Clients hoping for relief are wrong.
12. **Digital Omnibus OJ L citation** and **Bundeserprobungsgesetz BGBl. citation** unverified.

---

## PART 6b — Verification method (proven 2026-07-21)

The dejure.org vernetzung endpoint resolves a decision whenever its **date** is known, without a paywalled database:

```
https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=YYYY-MM-DD&Aktenzeichen=<AZ-urlencoded>
```

For EuGH use `curia.europa.eu` (`C-###/##`); the dejure endpoint covers German courts.

**Three limits learned the hard way:**

1. **dejure's text search does not index Entscheidungsnamen.** Searching "Talking to Addison" returns *Kein Eintrag* even though the decision is in the database and resolves fine by date + Az. So a name-only citation can be **confirmed but never excluded** — record such cases as "not retrievable", never "non-existent".
2. **Rate limiting is real** (HTTP 420 mid-run). When it hits, stop and leave the remainder marked rather than guessing.
3. **Existence is not verification.** The dangerous failure mode is an Aktenzeichen that resolves to a *real decision of the cited date but a different case*. `I ZR 6/06` is a genuine BGH decision on the cited date — it is just not Tchibo/Rolex II, and its Fundstelle differs. Always check subject matter.

**Measured error rate: ~10 %** in the areas verified so far, and the errors are not obvious junk. In `urheber-medienrecht`, 30 decisions were confirmed and **12 errors caught**, including two competing citations for one case where *neither* was correct (`I ZR 145/11` is "Fluch der Karibik").

**Metric note:** `verify_citations.py` was fixed so that a citation carrying an authoritative source link counts as *verified*. Before that fix, verifying a citation **raised** the warning count — the metric inverted quality. Any historical "warnings" figure predating 2026-07-21 is a marker census, not a quality signal.

---

## PART 6 — Recommended sequencing

~~Phases 1, 2, 3 and 5~~ — **done 2026-07-21** (see Status table at the top). Housekeeping items are likewise closed: the mietrecht duplicate is merged, `skills.json` counts are generated, the empty `adapters/` scaffolding is gone, and the validator now resolves `agents:` frontmatter paths.

**What remains, in priority order:**

**1. Verification (Part 4) — the highest-value work left, by some distance.**
Coverage is the binding constraint on how far this library can be trusted. At the measured ~10 % error rate, an unverified area is not neutral — it is a set of confident-looking citations of unknown quality. This outranks any further breadth.

**2. Tier-2 areas (Part 2b)** — Lebensmittelrecht, SGB VIII Jugendhilfe, EU-Beihilfen/Subventionsrückforderung, Architektenrecht/HOAI inside `baurecht`, Vertragsarztrecht inside `medizinrecht`, IPR/Schiedsverfahren to complete the FAO "Internationales Wirtschaftsrecht" title.

**3. Standing watch items** — these move and will silently go stale:
- KI-VO: Hochrisiko 02.12.2027 (Anhang III) / 02.08.2028 (Anhang I); harmonised standards still not cited in the OJ
- CRA: full application 11.12.2027
- New ProdHaftG: 09.12.2026, and the German enactment was still in the Rechtsausschuss
- Pay Transparency: German transposition targeted for early 2027, duties from June 2028
- EUDR: 30.12.2026 / 30.06.2027, twice delayed already — treat as unstable
- CSDDD: transposition 26.07.2028, duties 26.07.2029
- Stiftungsregister: **01.01.2028**
- KI-MIG: passed both chambers, **not promulgated** as of 21.07.2026 — no BGBl. cite exists yet

**4. Known gaps not worth fixing yet** — 28 skills contain no case-law citation at all (surfaced by `validate.py --strict`). For form-driven skills (Markenanmeldung, Einspruch ans Finanzamt) that is legitimate; for others it is thin. Triage before treating it as a defect.

> **Strategic note:** the repo's competitive advantage is the audit trail, not the skill count. 189 skills with ~10% citation error rate is a weaker — and under § 43a BRAO riskier — product than 120 verified ones. Weight correction and verification over breadth.
