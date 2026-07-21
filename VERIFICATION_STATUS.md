# Verification status — case-law citations in the 25 new plugins

This is the snapshot of the public-source verification pass on the 25 new plugins added on 2026-05-22. Per [`CONVENTIONS.md`](./CONVENTIONS.md), case citations get one of three states:

- **(no marker, with URL)** — verified against an official source
- **`[unverifiziert – prüfen]`** — from model knowledge, not externally confirmed (the user must check in juris / Beck-Online / openjur / curia before reliance)
- **`[generiert]`** — forbidden in client-facing output (never used in this repo)

## Plugins with completed verification pass (9 of 25)

| Plugin | Verified | Left flagged | Errors caught |
|---|---|---|---|
| `europarecht` | 15 | 0 | 1 (Art. 23d Abs. 5 GG → Art. 104a Abs. 6 GG) |
| `verfassungsrecht` | 14 | 2 | 2 (BVerfGE 8, 104 + 19, 206 topic mislabels) |
| `kartellrecht` | 22 | 5 | 3 (EDEKA/Tengelmann Az, Amazon § 19a Az, Illumina/Grail M-Nummer) |
| `patentrecht` | 12 | 3 | 0 (Schneidmesser III not publicly attested under that name) |
| `transportrecht` | 4 | 2 | 0 |
| `medizinrecht` | 11 | 0 | 0 |
| `baurecht` | 8 | 1 | 1 (BGH VII ZR 184/07 invalid; correct is VII ZR 55/07) |
| `versicherungsrecht` | 10 | 1 | 1 (BGH IV ZR 218/97 wrong Fundstelle/topic) |
| `vergaberecht` | 8 | 3 | 3 (X ZB 9/11 topic mismatch, VII ZR 24/08 + VII-Verg 1/18 wrong Fundstellen) |
| **Total** | **104** | **17** | **11** |

Verified citations have been edited in-place: the `[unverifiziert]` marker is removed and a parenthetical URL (curia, bverfg.de, dejure.org, lexetius.com, etc.) added.

The 11 caught errors are recorded in the per-plugin agent reports (transcript log) and the affected lines still carry `[unverifiziert]` markers because the cited form does not match what public sources show.

## Plugins where verification did NOT run (16 of 25)

These plugins keep all `[unverifiziert – prüfen]` markers intact and need a verification pass before client-facing use:

- `urheber-medienrecht`, `sozialrecht`, `umweltrecht`, `wettbewerbsrecht`, `produktrecht`, `migrationsrecht`, `handelsrecht`, `aussenwirtschaft-zoll-sanktionen`, `geldwaesche-aml-kyc`, `energierecht`, `verkehrsrecht`, `ki-governance`, `agrarrecht`, `sportrecht`, `berufsrecht-anwaltschaft`, `kapitalmarktrecht`

Reason: subagent verification runs were denied WebFetch permission by the harness, and the parent context's WebFetch returns empty content from JavaScript-heavy sources (curia.europa.eu, eur-lex.europa.eu) or 404s from German Wikipedia for most of the cited cases (which lack dedicated DE-Wikipedia articles).

## Citation conflicts surfaced even without web access

The blocked-but-still-useful inventory passes surfaced several internal Aktenzeichen conflicts in `urheber-medienrecht` that the user should resolve manually before relying on these citations:

- **"Das Boot II" vs. "Talking to Addison"** — `lizenzvertrag-urhg/SKILL.md` cites both with Az `I ZR 145/11`. Only one can be correct.
- **"Tchibo/Rolex II"** — `agents/researcher.md` cites `I ZR 60/96`; `skills/urheberrechtsverletzung-abmahnung/SKILL.md` cites `I ZR 6/06`. Inconsistent.
- **"Gemeinkostenanteil"** — `agents/researcher.md` cites `I ZR 34/02`; `skills/urheberrechtsverletzung-abmahnung/SKILL.md` cites `I ZR 246/98`. Inconsistent.

## How to complete the verification

Two paths for the remaining 16 plugins:

1. **Manual via juris / Beck-Online** (authoritative): each `[unverifiziert]` citation is looked up in a paywalled court database, the marker removed, and the journal Fundstelle (NJW/NZA/BGHZ/BVerfGE/BAGE) confirmed.
2. **Open-source pass with broader WebFetch permissions**: re-run the per-plugin verification subagent with allowlisted access to `dejure.org`, `bverfg.de`, `bverwg.de`, `bsg.bund.de`, `bundesgerichtshof.de`, `openjur.net`. Earlier successful agents used `dejure.org` heavily with the URL pattern `https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=<COURT>&Datum=YYYY-MM-DD&Aktenzeichen=<AZ>` — this works when the date is known, which is the case for all current citations.

## Repo-wide convention reminder

Skills MUST NOT be relied on for client-facing output where a citation still carries `[unverifiziert – prüfen]`. This is a structural feature, not a defect: the marker is the contract between the model's recall and the user's verification obligation.

---

## Verification pass — `urheber-medienrecht` (2026-07-21)

Method: `dejure.org` Vernetzungs-Endpunkt (`/dienste/vernetzung/rechtsprechung?Gericht=…&Datum=…&Aktenzeichen=…`) plus its `?Text=<Az>` fallback for citations whose date was unknown. No paywalled database was used.

| Plugin | Verified | Left flagged | Errors caught |
|---|---|---|---|
| `urheber-medienrecht` | 30 | 24 | 12 |

**Verified (30 decisions):** BGH I ZR 143/12, I ZR 121/08, I ZR 169/12, I ZR 19/16, I ZR 74/12, I ZR 246/98, I ZR 107/90, I ZR 127/10, I ZR 176/18, I ZR 39/14, I ZR 73/10, I ZR 41/12, I ZR 38/07, I ZR 19/09, I ZR 145/11, VI ZR 56/94; BVerfG 1 BvR 400/51, 1 BvR 112/65, 1 BvR 1602/07, 1 BvR 1861/93, 1 BvL 20/81, 1 BvR 653/96; EuGH C-5/08, C-466/12, C-160/15, C-161/17, C-683/17, C-833/18, C-682/18 + C-683/18, C-507/17. Each now carries court, date, Aktenzeichen, amtliche Sammlung and a parenthetical dejure.org URL, with the marker removed.

**Left flagged (24 marker instances):** none of these is a concrete Aktenzeichen. They are (a) Kommentar-Auflagenstände (Dreier/Schulze, Wandtke/Bullinger, Schricker/Loewenheim, Fechner, Soehring/Hoene u. a.), (b) unspezifische Rechtsprechungsverweise ohne Az („BGH-Linie", „BVerfG-Linie", „st. BGH-Rspr.", BGH VI. ZS Online-Archiv-Linie, „Promi-Spielraum-Entscheidungen"), (c) Landesrecht (Gegendarstellungsfristen der 16 Landespressegesetze, Konsolidierungsstand MStV) und (d) die noch im Aufbau befindliche EuGH-Spruchpraxis zu Art. 18 DSM-RL. These are unverifiable by construction, not by failure of the method.

### The three documented contradictions — all three resolved

1. **„Das Boot II" vs. „Talking to Addison" (both cited as `I ZR 145/11`)** — **neither** was correct. `I ZR 145/11` is BGH, Urt. v. 10.05.2012 – „Fluch der Karibik" (Nachvergütung ausübender Künstler). Correct: „Das Boot II" = BGH, Urt. v. 20.02.2020 – **I ZR 176/18**, GRUR 2020, 611; „Talking to Addison" = BGH, Urt. v. 07.10.2009 – **I ZR 38/07**, BGHZ 182, 337 = GRUR 2009, 1148. Both fixed; „Fluch der Karibik" added to the Rspr. list under its true name.
2. **„Tchibo/Rolex II"** — neither `I ZR 60/96` (researcher.md) nor `I ZR 6/06` (abmahnung SKILL.md) was correct. Correct: BGH, Urt. v. 17.06.1992 – **I ZR 107/90**, BGHZ 119, 20 = GRUR 1993, 55. Both files now agree.
3. **„Gemeinkostenanteil"** — the SKILL.md form was right, the agent file wrong. Correct: BGH, Urt. v. 02.11.2000 – **I ZR 246/98**, BGHZ 145, 366 = GRUR 2001, 329. `I ZR 34/02` corrected in `agents/researcher.md`, `agents/drafter.md` and in the Schadensberechnungs-Tabelle of `urheberrechtsverletzung-abmahnung/SKILL.md`.

### All 12 errors caught

| # | Where | Error | Action |
|---|---|---|---|
| 1 | abmahnung SKILL.md | „Tchibo/Rolex II" cited as 02.10.2008 – I ZR 6/06, GRUR 2009, 150. `I ZR 6/06` is a real BGH decision of that date but is „Whistling for a train" (GRUR 2009, 407) — different name, different Fundstelle | corrected to I ZR 107/90 |
| 2 | researcher.md | „Tchibo/Rolex II (I ZR 60/96)" — not retrievable under that Az | corrected to I ZR 107/90 |
| 3 | researcher.md | „Gemeinkostenanteil (I ZR 34/02)" | corrected to I ZR 246/98 |
| 4 | abmahnung SKILL.md, Schadensberechnungstabelle | „BGH I ZR 34/02" for Gemeinkostenanteil | corrected to I ZR 246/98 |
| 5 | lizenzvertrag SKILL.md (§ 32a-Abschnitt) | „Das Boot II" = I ZR 145/11 | corrected to I ZR 176/18 |
| 6 | lizenzvertrag SKILL.md, Rspr.-Liste | I ZR 127/10 labelled „Das Boot II" — it is „Das Boot" (I); the GRUR 2012, 496 Fundstelle was correct for I ZR 127/10 | name corrected; „Das Boot II" added as a separate entry |
| 7 | lizenzvertrag SKILL.md (Zweckübertragung) | „Talking to Addison" = I ZR 145/11 | corrected to I ZR 38/07; inline note added that the decision applies the Zweckübertragungslehre within § 32 UrhG (Übersetzervergütung) |
| 8 | lizenzvertrag SKILL.md, Rspr.-Liste | I ZR 41/12 labelled „Honorarbedingungen freie Journalisten" — it is „Rechteeinräumung Synchronsprecher" (GRUR 2014, 556) | name corrected; „Honorarbedingungen Freie Journalisten" added under its true Az I ZR 73/10 (BGHZ 193, 268) |
| 9 | researcher.md | „GVR Tageszeitungen (I ZR 73/10)" — I ZR 73/10 is Honorarbedingungen Freie Journalisten | corrected to I ZR 39/14; I ZR 73/10 kept under its true name |
| 10 | lizenzvertrag SKILL.md | „GVR Tageszeitungen" (I ZR 39/14) — dejure records the decision as „GVR Tageszeitungen **II**" | name corrected, GRUR 2016, 67 added |
| 11 | researcher.md | „Stern/Strauß (BVerfGE 63, 131)" — BVerfGE 63, 131 is BVerfG, Beschl. v. 08.02.1983 – 1 BvL 20/81 „Gegendarstellung" („Türken in Bingen"); the name „Stern/Strauß" is not attested for it | name corrected, Az and date added |
| 12 | mstv SKILL.md (2×), researcher.md | BVerfGE 120, 180 called „Caroline II" — dejure records it as „Caroline von Monaco III"; „Caroline von Monaco II" is BVerfGE 101, 361 (1 BvR 653/96) | names corrected, both decisions now cited separately |

### Honest note on the method's reach

- The `?Datum=…&Aktenzeichen=…` endpoint resolved **every** citation whose date was already in the file — 30 of 30.
- For citations carrying an Aktenzeichen but no date (`I ZR 145/11`), the `?Text=<Az>` fallback resolved the decision including its procedural history. Useful, but it only works for an Aktenzeichen, not a name.
- **dejure's `?Text=` search does not index Entscheidungsnamen.** Queries for „Talking to Addison" and „Tchibo/Rolex II" returned *Kein Eintrag* even though both decisions are in the database and were retrieved seconds later via their date + Az. Any name-only citation therefore had to be resolved by hypothesising a date/Az and confirming it — a method that can confirm a hypothesis but can never *exclude* one. Consequently `I ZR 60/96` and `I ZR 34/02` are recorded above as "not retrievable / not the cited decision", not as "non-existent".
- The endpoint returns a Fundstellen list that is occasionally garbled on extraction (for I ZR 121/08 it emitted both `GRUR 2010, 2061` and the correct `GRUR 2010, 633`). Fundstellen were therefore cross-read against the amtliche Sammlung (BGHZ/BVerfGE) wherever one exists, and BGHZ/BVerfGE was preferred in the corrected citations.
- No Aktenzeichen, date or Fundstelle in this pass was supplied from model recall alone; every figure written into the files came from a retrieved dejure.org record.

**Note on `scripts/verify_citations.py`:** its per-file "to review" count *rises* after a verification pass (urheber-medienrecht: 21 → 71 across the three SKILL.md files). This is expected and matches the already-verified areas: the script warns on any Aktenzeichen **without** an `[unverifiziert]` marker, so removing a marker converts a silent INFO into a WARN. The count is a marker census, not a quality signal.

---

## Verification pass — `it-recht` (2026-07-21)

Method: `dejure.org` Vernetzungs-Endpunkt (`/dienste/vernetzung/rechtsprechung?Gericht=…&Datum=…&Aktenzeichen=…`), plus the `?Text=<Az>` fallback to identify what a wrong Aktenzeichen actually resolves to. No WebSearch, no paywalled database.

| Plugin | Verified | Left flagged | Errors caught |
|---|---|---|---|
| `it-recht` | 6 | 1 | 2 |

**Verified (6 decisions, all retrieved, marker removed + dejure.org URL added):**

- BGH, Urt. v. 22.11.2001 – I ZR 138/99, BGHZ 149, 191 = GRUR 2002, 622 – „shell.de" (`domainrecht`)
- BGH, Urt. v. 17.05.2001 – I ZR 251/99, BGHZ 148, 13 = GRUR 2001, 1038 – „ambiente.de" (`domainrecht`)
- BGH, Urt. v. 15.11.2006 – XII ZR 120/04, NJW 2007, 2394 = MMR 2007, 243 (ASP/SaaS = Mietvertrag) (`saas-vertrag` 2×, `it-vertragspruefung`)
- EuGH, Urt. v. 30.05.2024 – C-400/22 (VT u. UR ./. Conny GmbH), NJW 2024, 2449 (Button-Lösung) (`e-commerce-pflichten`)
- EuGH, Urt. v. 03.07.2012 – C-128/11, NJW 2012, 2565 = GRUR 2012, 904 – UsedSoft (`softwarelizenz-agb` 2×)
- BGH, Urt. v. 17.07.2013 – I ZR 129/08, GRUR 2014, 264 = NJW 2014, 777 – UsedSoft II (`softwarelizenz-agb` 2×)

**Left flagged (1):** BGH „afilias.de" in `domainrecht/SKILL.md`. The citation carries neither Datum noch Aktenzeichen, and dejure's `?Text=` search does not index Entscheidungsnamen (`Kein Eintrag` for „afilias.de", as in the `urheber-medienrecht` pass). The marker stays; the line now names the reason. „ambiente.de", with which it was bundled on one line, was resolved and split out.

### The 2 errors caught

| # | Where | Error | Action |
|---|---|---|---|
| 1 | `it-vertragspruefung/SKILL.md` | „BGH, Urt. v. 18.12.2009 – V ZR 130/08, NJW 2010, 1962 (Cloud-Haftung)" — **wrong on every axis**. dejure: „Keine Entscheidung des BGH vom 18.12.2009 mit dem Aktenzeichen V ZR 130/08". The Az resolves to BGH, Urt. v. **06.02.2009** – V ZR 130/08, **NJW 2009, 1346** — Grundstücksübertragung gegen Pflegezusage, § 138 BGB. Nothing to do with Cloud-Haftung; the NJW 2010, 1962 Fundstelle is not attested for it. Exactly the `urheber-medienrecht` failure mode (real Az, real decision, different case) — here compounded by a date that yields no decision at all | Fundstelle **not** replaced with a guess: no leading BGH decision on Cloud-Haftung is publicly attested. The marker stays and the line now records the discrepancy and points to §§ 280, 535, 536a BGB + AGB-Kontrolle as the actual basis. Legal substance unchanged |
| 2 | `domainrecht/SKILL.md` | „BGH „ambiente.de" / „afilias.de"" cited as one line with no Datum, kein Az and no Fundstelle for either decision | „ambiente.de" resolved to I ZR 251/99 (BGHZ 148, 13) and verified; „afilias.de" split onto its own line and left flagged |

### Errors *not* found — and a finding about the area's shape

**6 of the 11 skills carry zero case citations**: `cloud-auftragsverarbeitung`, `ki-vertraege`, `open-source-compliance`, `providerhaftung`, `softwareerstellung-werkvertrag`, `it-sicherheit-meldepflichten`. This is **correct, not a defect**. These skills rest on statutory text (DSGVO Art. 28/32/44 ff., Data Act + DADG, DDG §§ 7–10 i. V. m. Art. 4–6 DSA, BSIG n. F., §§ 631 ff. BGB) and on standard licence terms (GPL/MIT/Apache-2.0), all of which are already linked to primary sources. No case law was manufactured for them.

One substantive gap is worth flagging to a human, without inventing a citation to fill it: `providerhaftung/SKILL.md` invokes the **Störerhaftung** and the Prüfpflichten-Trias without citing a single decision, although this doctrine is entirely richterrechtlich (BGH I. und VI. Zivilsenat, EuGH C-401/19, C-682/18/C-683/18). Adding the leading cases there is a content task, not a verification task, and was left out of scope.

### Honest note on the method's reach

- `?Datum=…&Aktenzeichen=…` resolved **every** citation that carried a date — 6 of 6, including both EuGH cases (`Gericht=EuGH` works for C-Nummern).
- The endpoint's *negative* answer is informative and was used as such: it is what exposed error #1. „Kein Eintrag" for a date+Az pair means dejure has no such decision — much stronger evidence than the `?Text=` fallback's silence.
- `?Text=` remains name-blind, so a name-only citation („afilias.de") can only be resolved by hypothesising a date/Az and confirming it. „ambiente.de" was resolved that way (hypothesis I ZR 251/99 → confirmed by the retrieved record). For „afilias.de" the first hypothesis (I ZR 82/01) returned a real but **different** decision — „kurt-biedenkopf.de", NJW 2004, 1793 — and was therefore discarded rather than written into the file. It is recorded as *not retrievable*, not as *non-existent*.
- No rate limiting was hit: the pass needed only 9 requests, paced.
- No Aktenzeichen, Datum or Fundstelle in this pass came from model recall. Every figure written into a file came from a retrieved dejure.org record.

### Note on the warning count

`scripts/verify_citations.py` for `it-recht`: **56 → 50 warnings**. All 6 removed warnings are the case-law ones; the area now has **zero** unmarked case-law citations.

The remaining **50 warnings contain no case law at all** and are not citation debt. They are gaps in the abbreviation map of `verify_citations.py`:

- 34 × `BSIG` in `it-sicherheit-meldepflichten` — BSI-Gesetz n. F., a real statute
- 15 × `DDG` in `providerhaftung` — Digitale-Dienste-Gesetz, a real statute
- 1 × `Art. 28 AVV` in `it-vertragspruefung` — a parser artefact: the text reads „AVV nach Art. 28 DSGVO", and the regex binds `Art. 28` to the wrong token

Adding `BSIG` and `DDG` to `GII_ABBR` in `scripts/verify_citations.py` would clear 49 of the 50 in one line each. That file was outside this pass's scope and was left untouched.

---

## Verification pass — `energierecht`, `migrationsrecht`, `aussenwirtschaft-zoll-sanktionen` (2026-07-21)

Method: `dejure.org` Vernetzungs-Endpunkt (`/dienste/vernetzung/rechtsprechung?Gericht=…&Datum=…&Aktenzeichen=…`), plus the `?Text=<Az>` fallback for two citations carrying no date. **dejure indexes EuGH and EGMR decisions as well as German courts** (`Gericht=EuGH`, `Gericht=EGMR`) — for joined EU cases the `P` suffix must be dropped from the `Aktenzeichen` parameter (`C-402/05`, not `C-402/05 P`). No paywalled database, no WebSearch.

| Plugin | Verified | Left flagged | Errors caught |
|---|---|---|---|
| `energierecht` | 0 | 1 | 1 (BGH KZR 17/07 not attested) |
| `migrationsrecht` | 17 | 1 | 4 |
| `aussenwirtschaft-zoll-sanktionen` | 6 | 3 | 3 |
| **Total** | **23** | **5** | **8** |

**Verified (23 decisions).** EuGH: C-465/07 Elgafaji; C-411/10 + C-493/10 N.S. u.a.; C-163/17 Jawo; C-199/12 bis C-201/12 X, Y und Z; C-578/08 Chakroun; C-540/03 Parlament/Rat; C-402/05 P + C-415/05 P Kadi I; C-584/10 P + C-593/10 P + C-595/10 P Kadi II; C-72/15 Rosneft; C-339/98 Peacock; C-486/06 Van Landeghem. EGMR: 14038/88 Soering; 30696/09 M.S.S.; 46410/99 Üner; 54273/00 Boultif. BVerwG: 9 C 58.96; 1 C 18.05; 1 C 33.18; 1 C 3.16; 1 C 17.09; 1 C 22.15. BVerfG: 2 BvR 939/14. Each now carries court, date, Aktenzeichen, amtliche Sammlung where one exists, and a parenthetical dejure.org URL, with the marker removed.

**Left flagged (5).** (1) BGH KZR 17/07 in `enwg-netzanschluss` — not retrievable, see error 1. (2) BVerwG 1 C 33.18 in `asylantrag-vorbereitung` — decision confirmed, § 3e-Bezug not confirmed, see error 5. (3) EuGH C-201/09 P ArcelorMittal in `ausfuhr-dual-use-pruefung` — see error 6. (4) „BGH, Urt. zu § 34 AWG a.F. / § 18 AWG" and (5) „BFH zu vZTA-Bindung … Art. 34 UZK" — placeholder entries carrying neither Aktenzeichen nor date; unresearchable by construction. All remaining `[unverifiziert]` instances across the three areas are Kommentar-Auflagenstände, Behördenpraxis (BAFA-Merkblatt, BMWK-FAQ, BNetzA-Festlegungen), Fassungs-Vorbehalte, or skeleton entries of the form „BGH, Urt. v. – VIII ZR Az." with no citation content at all.

### The 8 errors caught

| # | Where | Error | Action |
|---|---|---|---|
| 1 | `enwg-netzanschluss` | BGH, Urt. v. 18.11.2008 – KZR 17/07, RdE 2009, 184 — dejure returns *Kein Eintrag* both for date+Az and for the Az alone. EEG-Anschlussstreitigkeiten fall to the VIII. Zivilsenat, not the Kartellsenat, so the Senatszuordnung is doubtful; a probe for `VIII ZR 78/08` on the same date was also negative | marker kept and sharpened to `[unverifiziert – Aktenzeichen nicht belegbar]` with an inline note naming the Senat problem. **No substitute Az invented** |
| 2 | `abschiebungsschutz`, Rspr.-Liste Nr. 6 | BVerwG, Urt. v. 17.10.2006 – 1 C 18.05 labelled „Reisefähigkeit, inlandsbezogen". The decision (BVerwGE 127, 33) concerns a **zielstaatsbezogenes** Abschiebungsverbot nach § 60 VII AufenthG wegen Verschlimmerung einer Erkrankung im Zielstaat — the opposite category | label corrected, BVerwGE 127, 33 = NVwZ 2007, 712 added, the ziel-/inlandsbezogen distinction made explicit |
| 3 | `aufenthaltstitel-pruefung`, Nr. 1 + `agents/researcher.md` | BVerwG, Urt. v. 22.02.2017 – 1 C 3.16 labelled „Bleiberecht, § 25b AufenthG". The decision (BVerwGE 157, 325) concerns the **Ausweisung eines anerkannten Flüchtlings wegen Unterstützung der PKK** | label corrected in both files, BVerwGE 157, 325 = NVwZ 2017, 1883 added |
| 4 | `aufenthaltstitel-pruefung`, Nr. 2 | BVerwG, Urt. v. 16.11.2010 – 1 C 17.09 labelled „Identitätsklärung". The decision (BVerwGE 138, 122) concerns the **Nachholung des Visumverfahrens** beim Ehegattennachzug zu Deutschen | label corrected, BVerwGE 138, 122 = NVwZ 2011, 495 added |
| 5 | `asylantrag-vorbereitung`, Nr. 5 + `agents/researcher.md` | BVerwG, Urt. v. 04.07.2019 – 1 C 33.18 labelled „interner Schutz § 3e AsylG". dejure records the decision as concerning Flüchtlingsanerkennung syrischer Antragsteller, Maßstab der beachtlichen Wahrscheinlichkeit und gerichtliche Aufklärungspflicht; a § 3e-Bezug is not evident from the source | decision itself verified and URL added; the § 3e attribution kept under a **narrowed marker** `[unverifiziert – Einschlägigkeit für internen Schutz prüfen]` rather than silently corrected |
| 6 | `ausfuhr-dual-use-pruefung`, Nr. 2 | EuGH, Urt. v. 29.03.2011 – verb. Rs. C-201/09 P, C-216/09 P, ArcelorMittal, cited „zur Anwendung des Unionsrechts" in an **export-control** Rspr. list. Date and Aktenzeichen are correct, but the decision is a **Kartellsache** (Trägerkartell, Art. 65 EGKS, Kommissionszuständigkeit nach Auslaufen des EGKS-Vertrags) with no exportkontrollrechtlicher Gegenstand — the `urheber-medienrecht` failure mode: real decision, right date, wrong case for the proposition | marker kept, inline note names the discrepancy and flags the citation for deletion or replacement. Not silently removed |
| 7 | `sanktionslisten-screening`, Nr. 3 | EuGH C-72/15 Rosneft labelled „Auslegung Russland-VO, **Bereitstellungsverbot**". The decision's holding is the Zuständigkeit des EuGH für GASP-gestützte restriktive Maßnahmen plus Gültigkeit/Auslegung der Russland-Maßnahmen; Bereitstellungsverbot is not its subject | label corrected in both `sanktionslisten-screening` and `ausfuhr-dual-use-pruefung` |
| 8 | `zolltarif-vzta-antrag`, Nr. 2 | Rs. C-486/06 cited as „**BVBA** Van Landeghem". dejure records the case simply as „Van Landeghem" | name corrected; date 06.12.2007 and the 8703/8704-KN subject added (the citation had carried neither) |

### Substantive currency check

- **`energierecht` — the GModG correction is intact.** Every occurrence of the 65 % rule in `energieeffizienzpflicht/SKILL.md` (lines 22, 26, 27, 96, 136, 175, 201, 215) states it as **abolished** by the GModG (Bundestag 10.07.2026, 323 : 271), with duties keyed to the kommunaler Wärmeplan nach dem WPG. **No surviving 65 % rule was found** anywhere in the area, including the agent files. `test.md` already asserts the post-GModG state. Nothing reintroduced.
- **`aussenwirtschaft-zoll-sanktionen` — no package-number claims.** The skills describe the mechanism (Bereitstellungsverbot, > 50 %-/Kontroll-Faustregel, Screening-Pflichten) and route to the konsolidierte EU-Liste; no assertion about the content of any specific sanctions package or listing was found, so nothing had to be marked on that ground.
- **`migrationsrecht`** — noted in-place that N.S. (C-411/10) was decided under **Dublin II (VO 343/2003)**, not Dublin III, and that BVerwG 9 C 58.96 was decided under **§ 53 Abs. 6 S. 1 AuslG**, the predecessor of § 60 VII AufenthG. Both were previously cited without that qualification.

### Metric note — the "to review" count is not comparable across this pass

`scripts/verify_citations.py` was **modified by another agent during this session** (it gained a `VERIFICATION_HOSTS` allowlist so that an Aktenzeichen carrying a dejure/curia/bverfg link counts as verified rather than unmarked). The pre-pass baseline was therefore taken against a different script than the post-pass numbers, and the two are not directly comparable — e.g. `energieeffizienzpflicht` reads 10 → 0 although **no edit was made to that file** in this pass.

Post-pass, every remaining warning in the three areas was inspected individually and **not one is an unverified case citation**:

- `abschiebungsschutz` 8, `asylantrag-vorbereitung` 2, `aufenthaltstitel-pruefung` 1 — all are unknown-abbreviation warnings (`§ 60a IIc`, `Art. 24 GRCh`, `§ 53 Abs. 6 S. 1 AuslG`) or the regex reading `Art. 29 VO 604/2013` as an Aktenzeichen.
- `ausfuhr-dual-use-pruefung` 10, `sanktionslisten-screening` 3, `zolltarif-vzta-antrag` 1 — the regex reading `Anhang I VO 2021/821` and similar as Aktenzeichen, plus `Art. 65 EGKS`.
- `eeg-foerderpruefung` 4, `enwg-netzanschluss` 1 — pre-existing, untouched by this pass.

Two of these warnings are newly introduced *by correct verification work* (`§ 53 Abs. 6 S. 1 AuslG` and `Art. 65 EGKS` are abbreviations the script's map does not know, added while naming what the cited decisions actually decided). Adding `AuslG`, `GRCh` and `EGKS` to `GII_ABBR` would clear them; that file was outside this pass's scope and was left untouched.

`validate.py` and `eval.py` pass clean for all three areas (energierecht 55 checks, migrationsrecht 49, aussenwirtschaft 48; 0 failures). No `test.md` asserted any of the corrected citations, so no test file was changed.

---

## Verification pass — `arbeitsrecht` (2026-07-21)

Method: `dejure.org` Vernetzungs-Endpunkt (`/dienste/vernetzung/rechtsprechung?Gericht=…&Datum=…&Aktenzeichen=…`), dessen `?Text=<Az>`-Fallback sowie `bundesarbeitsgericht.de` für den amtlichen Leitsatz. Keine WebSearch, keine kostenpflichtige Datenbank.

| Plugin | Verified | Left flagged | Errors caught |
|---|---|---|---|
| `arbeitsrecht` | 14 | 40 | 1 |

### Ausgangsbefund: Aktenzeichen-Sweep über alle 14 Skills

Gesucht wurde nach `\d+ AZR \d+/\d+`, `\d+ ABR \d+/\d+`, `C-\d+/\d+`, `\d+ BvR|BvL \d+/\d+`.

- **Die 11 am 21.07.2026 neu geschriebenen Skills enthielten tatsächlich null Aktenzeichen** — die Angabe des Autors ist bestätigt. Rechtsprechung war dort ausschließlich als „st. Rspr. des BAG zu § …" oder über EuGH-Parteinamen (*Junk*, *Spijkers*, *Marshall*, *Foster*, *Francovich*) bezeichnet, jeweils mit `[unverifiziert – prüfen]`.
- Aktenzeichen fanden sich **nur in den drei Altskills** `kuendigungs-pruefung` (21), `abmahnung` (5), `aufhebungsvertrag` (1) sowie in `kuendigungs-pruefung/providers/claude.md` (20). **Alle** trugen bereits einen `[unverifiziert]`-Marker bzw. standen in einer explizit als unverifiziert deklarierten Rspr.-Liste; unmarkierte Aktenzeichen gab es nicht. Diese Altbestände wurden in diesem Durchgang **nicht** angefasst — sie sind ein eigener, noch offener Prüfauftrag.

### Von „st. Rspr." auf eine belegte Entscheidung hochgestuft (14)

| Proposition | Skill | Entscheidung |
|---|---|---|
| § 613a Abs. 5 BGB — Musterkatalog der Unterrichtung; Widerspruchsfrist läuft ohne ordnungsgemäße Unterrichtung nicht an | `betriebsuebergang` | BAG, Urt. v. 13.07.2006 – 8 AZR 305/05, BAGE 119, 91 = NZA 2006, 1268 |
| Betriebsübergang — Identitätswahrung, Gesamtwürdigung | `betriebsuebergang` | EuGH, Urt. v. 18.03.1986 – Rs. 24/85, *Spijkers* |
| Urlaubsverfall nur nach Erfüllung der Mitwirkungsobliegenheiten | `urlaubsanspruch` | EuGH, Urt. v. 06.11.2018 – C-619/16, *Kreuziger* |
| dito, Aufklärungspflicht „klar und rechtzeitig" | `urlaubsanspruch` | EuGH, Urt. v. 06.11.2018 – C-684/16, *Max-Planck-Gesellschaft/Shimizu* |
| Umsetzung der Hinweisobliegenheit in § 7 BUrlG | `urlaubsanspruch` | BAG, Urt. v. 19.02.2019 – 9 AZR 541/15, NZA 2019, 982 |
| Verjährung des Urlaubsanspruchs beginnt erst nach Erfüllung der Obliegenheiten | `urlaubsanspruch` | BAG, Urt. v. 20.12.2022 – 9 AZR 266/20, NZA 2023, 683 |
| 15-Monats-Frist bei Langzeiterkrankung | `urlaubsanspruch` | EuGH, Urt. v. 22.11.2011 – C-214/10, *KHS/Schulte* |
| Vererblichkeit des Urlaubsabgeltungsanspruchs | `urlaubsanspruch` | EuGH, Urt. v. 06.11.2018 – C-569/16 und C-570/16, *Bauer* / *Willmeroth* |
| § 14 Abs. 2 S. 2 TzBfG — Verwerfung der Drei-Jahres-Rspr., verfassungskonforme Einschränkung | `befristungskontrolle` | BVerfG, Beschl. v. 06.06.2018 – 1 BvL 7/14 und 1 BvR 1375/14, BVerfGE 149, 126 = NZA 2018, 774 |
| § 109 GewO — Darlegungslast oberhalb „befriedigend"; „zur vollen Zufriedenheit" = befriedigend | `arbeitszeugnis` | BAG, Urt. v. 18.11.2014 – 9 AZR 584/13, BAGE 150, 66 = NZA 2015, 435 |
| „Entlassung" = Ausspruch der Kündigung | `massenentlassungsanzeige` | EuGH, Urt. v. 27.01.2005 – C-188/03, *Junk* |
| § 17 Abs. 3 S. 1 KSchG — Abschrift vermittelt keine individuelle Rechtsposition | `massenentlassungsanzeige` | EuGH, Urt. v. 13.07.2023 – C-134/22 |
| Vorlage des 6. Senats zu den Folgen von Anzeigefehlern | `massenentlassungsanzeige` | BAG, Beschl. v. 23.05.2024 – 6 AZR 152/22 (A), BAGE 183, 254 = NZA 2024, 813 |
| Schlussentscheidung dazu (siehe Warnung unten) | `massenentlassungsanzeige` | BAG, Urt. v. 01.04.2026 – 6 AZR 152/22, NZA 2026, 669 |

### Gefundener Fehler (1) — und eine offene Sachfrage

**Fehler:** Aus dem Modellgedächtnis stammte für die Massenentlassungs-Zäsur das Datum **13.06.2024** zum Aktenzeichen 6 AZR 152/22. Der dejure-Abruf ergab: *keine* Entscheidung unter diesem Datum. Der `?Text=`-Fallback zeigte, dass 6 AZR 152/22 real ist, aber unter **zwei anderen** Daten geführt wird — Vorlagebeschluss 23.05.2024 und Schlussurteil 01.04.2026. Das erinnerte Datum wurde verworfen, beide echten Daten wurden einzeln verifiziert. Kein erfundenes Datum ist in die Dateien gelangt.

**Offene Sachfrage — § 17 KSchG.** Der amtliche Leitsatz des BAG-Urteils v. 01.04.2026 – 6 AZR 152/22 lautet (Volltext bundesarbeitsgericht.de): *„Erstattet der Arbeitgeber eine – erforderliche – Massenentlassungsanzeige vor Abschluss des Konsultationsverfahrens mit dem Betriebsrat, ist die daraufhin ausgesprochene Kündigung unwirksam."* Die Entscheidung führt weiter aus, dass Fehler im Anzeigeverfahren, die zur Unwirksamkeit der Anzeige führen, die dauerhafte Unwirksamkeit der Kündigung zur Folge haben.

Das steht in Spannung zur dritten Zeile der Fehlerfolgen-Tabelle des Skills („Anzeige fehlerhaft oder unvollständig → **keine** Unwirksamkeit"). **Die Tabelle und ihre drei `[unverifiziert]`-Marker wurden bewusst unverändert gelassen** — die Auflösung dieser Spannung ist eine dogmatische Entscheidung, keine Zitatpflege, und der Fall betrifft eine Verzahnung beider Stränge (Anzeige *vor* Abschluss der Konsultation), nicht den reinen Anzeigefehler. Stattdessen wurde ein deutlich markierter Hinweiskasten mit dem wörtlichen Leitsatz und beiden Fundstellen eingefügt. **Der Split ist damit erhalten und nicht zu einer sicheren Position verdichtet.** Die inhaltliche Nachführung ist dem Fachautor vorbehalten.

### Weiterhin markiert gelassen (40 Markerinstanzen)

- **Alle Aktenzeichen der drei Altskills** (`kuendigungs-pruefung`, `abmahnung`, `aufhebungsvertrag` sowie die Provider-Variante) — außerhalb des Auftrags dieses Durchgangs, kein Abruf erfolgt.
- **§ 102 BetrVG, subjektive Determination** (`betriebsratsanhoerung`): geprüft wurde BAG, Urt. v. 23.10.2008 – 2 AZR 163/07. Die Entscheidung existiert und betrifft § 102 BetrVG, formuliert den Grundsatz der subjektiven Determination aber **nicht** als tragende Aussage. Sie wurde daher **nicht** als Leitentscheidung zitiert — genau der Themen-Mismatch, an dem `urheber-medienrecht` gescheitert ist. Marker bleibt.
- **AGG, Entgelttransparenz, Sozialauswahl, Arbeitsvertragsgestaltung, Kündigungsschutzklage:** durchweg Verweise auf gefestigte Linien ohne Az (§ 22 AGG, § 15 Abs. 4 AGG, Ausschlussfristen, Widerrufsvorbehalt, Altersgruppenbildung, abgestufte Darlegungslast, § 130 BGB, Weiterbeschäftigungsanspruch des Großen Senats). Ohne Az oder Datum ist der dejure-Endpunkt hier konstruktionsbedingt blind; die Marker sind zutreffend.
- **Unionsrechtlicher Betriebsbegriff der RL 98/59/EG**, **betriebsmittelarme Tätigkeiten**, **Kettenbefristungs-Missbrauchskontrolle**, **Marshall / Foster / Francovich** in `entgelttransparenz`: nicht abgerufen (Ratenlimit-Budget), Marker bleiben. *Marshall* (Rs. 152/84) und *Francovich* (C-6/90, C-9/90) sind allerdings in `europarecht` bereits verifiziert belegt und könnten von dort übernommen werden.

### Zahlenbewegung bei `scripts/verify_citations.py`

Vorher 26 Warnungen im Bereich, nachher 25 — beide Zahlen betreffen **ausschließlich unbekannte Gesetzesabkürzungen**, nicht Rechtsprechung:

- 25× `EntgTranspG` in `entgelttransparenz` (die Abkürzung fehlt in der Statute-Map des Skripts; die Zitate selbst sind korrekt),
- 1× `SchwarzArbG` in `arbeitsvertrag-gestaltung` — **behoben ist keine davon**; entfallen ist stattdessen die zwischenzeitlich von diesem Durchgang selbst erzeugte Warnung.

Die neu eingefügten Entscheidungen erzeugten zunächst drei zusätzliche Warnungen (2× `Art. 2 Abs. 3 UAbs. 2`, 1× `Art. 31 Abs. 2 GRC`). Sie wurden ausgeschrieben (`Unterabsatz 2` bzw. „i.V.m. der Grundrechtecharta"; auch `GRCh` fehlt in der Statute-Map), womit sie verschwanden — eine reine Schreibweisen-, keine Inhaltsänderung. Die **Gesamtzahl der Zitate stieg** (z. B. `urlaubsanspruch` 40 → 54, `befristungskontrolle` 58 → 62, `betriebsuebergang` 52 → 54, `arbeitszeugnis` 31 → 33), weil dort nun echte, belegte Entscheidungen stehen, wo vorher nur eine Floskel stand — die Zunahme ist genau das Ziel des Durchgangs. Die „to review"-Spalte bleibt bei den betroffenen Dateien auf 0, weil jede neue Zitatstelle eine Primärquellen-URL trägt.

`scripts/validate.py --area arbeitsrecht` läuft sauber, `scripts/eval.py --area arbeitsrecht` besteht 14/14. Keine `test.md` musste geändert werden: es wurde kein bereits behauptetes Zitat korrigiert, sondern ausschließlich unbelegte Verweise durch belegte ersetzt.

---

## Verification pass — `agrarrecht` und `sportrecht` (2026-07-21)

Methode: ausschließlich `WebFetch` gegen öffentliche Primärquellen — dejure.org Vernetzungs-Endpunkt (`?Gericht=…&Datum=…&Aktenzeichen=…` sowie der `?Text=<Az>`-Fallback), HUDOC-Query-API des EGMR und buzer.de für nicht auf gesetze-im-internet.de auflösbare Gesetze (LwAnpG). Keine WebSearch, keine kostenpflichtige Datenbank. 22 Abrufe, kein Rate-Limit erreicht.

| Plugin | Verifiziert | Weiter markiert | Fehler gefunden |
|---|---|---|---|
| `agrarrecht` | 5 Entscheidungen + 3 Normen | 5 Rspr.-Linien ohne Az | 2 |
| `sportrecht` | 11 Entscheidungen | 2 CAS-Schiedssprüche + 2 Rspr.-Linien ohne Az | 1 |
| **Summe** | **19** | **9** | **3** |

### `agrarrecht` — der Befund vorweg

**Das Plugin enthielt vor diesem Durchlauf kein einziges konkretes Aktenzeichen.** Alle drei `### Rechtsprechung`-Abschnitte bestanden aus Gattungsverweisen („BGH-BLw-Senat zur ungesunden Verteilung …") ohne Gericht-Datum-Az-Tripel. Die von `verify_citations.py` gemeldeten 40 Warnungen sind **sämtlich Statut-Abkürzungs-Warnungen** (RSG, LPachtVG, LwVG, ALG, GAP-DZG fehlen in der Abkürzungstabelle des Skripts) — **keine einzige** betraf eine Fallzitierung. Der Durchlauf hat deshalb zwei Dinge getan: die vier belegbaren Leitentscheidungen erstmals mit Az und Fundstelle eingesetzt, und die Normzitate geprüft, an denen die Gutachtenlogik hängt.

**Verifizierte Entscheidungen (5):**
- BGH (BLw-Senat), Beschl. v. 26.11.2010 – **BLw 14/09**, NJW-RR 2011, 521 (§ 9 I Nr. 1 GrdstVG, Nichtlandwirt-Erwerb)
- BVerfG, Beschl. v. 12.01.1967 – **1 BvR 169/63**, BVerfGE 21, 73 (§ 9 I Nr. 1 GrdstVG mit Art. 14 GG vereinbar; keine Versagung allein wegen Kapitalanlage)
- BGH (BLw-Senat), Beschl. v. 29.11.2013 – **BLw 2/12**, EuZW 2014, 239 (EuGH-Vorlage, Art. 107 AEUV)
- BGH (BLw-Senat), Beschl. v. 29.04.2016 – **BLw 2/12**, BGHZ 210, 134 (Nachfolgeentscheidung: Verkehrswert, nicht innerlandwirtschaftlicher Preis)
- BGH (BLw-Senat), Beschl. v. 25.04.2014 – **BLw 5/13**, NJW-RR 2014, 1168 (grobes Missverhältnis, 50 %-Schwelle)

**Verifizierte Normen (3):** § 44 Abs. 6, § 51a und § 3b LwAnpG, je mit buzer.de-Beleg.

### `sportrecht` — verifizierte Entscheidungen (11)

EuGH C-415/93 (*Bosman*), C-519/04 P (*Meca-Medina und Majcen*), C-650/22 (*Diarra*); BAG 7 AZR 312/16 (*Müller ./. Mainz 05*); BGH I ZR 49/97 (*Marlene Dietrich*), KZR 6/15 (*Pechstein/ISU*), V ZR 253/08 (*Stadionverbot*); OLG München U 1110/14 Kart (*Pechstein*, Vorinstanz); BVerfG 1 BvR 3080/09 (*Stadionverbot*) und 1 BvR 2103/16 (*Pechstein*-Verfassungsbeschwerde, neu ergänzt); EGMR Nr. 40575/10 und 67474/10 (*Mutu und Pechstein/Schweiz*, ECLI und Datum über HUDOC bestätigt).

Datum und Aktenzeichen waren in allen elf Fällen bereits korrekt; ergänzt wurden Fundstellen, Entscheidungsnamen und Primärquellen-URLs.

### Die 3 gefundenen Fehler

| # | Wo | Fehler | Auflösung |
|---|---|---|---|
| 1 | `sportrecht/skills/vereinsrechtliche-sanktion/SKILL.md` (2×), `sportrecht/agents/researcher.md` | BGH, Urt. v. 30.10.2009 – V ZR 253/08 (*Stadionverbot*) zitiert als **BGHZ 183, 188**. dejure weist für diese Entscheidung **keine** BGHZ-Fundstelle aus; die Papierfundstellen sind NJW 2010, 534; VersR 2010, 825; SpuRt 2010, 28. Datum, Az und Gegenstand stimmen — nur die amtliche Sammlung ist nicht belegt | BGHZ-Angabe durch die belegten Fundstellen **NJW 2010, 534 = SpuRt 2010, 28** ersetzt |
| 2 | `agrarrecht/skills/lwanpg-pruefung/SKILL.md` (3×: Normenliste, Abschnitt 4, Gutachtenbeispiel), `agrarrecht/agents/reviewer.md` | **§ 51a LwAnpG als Verjährungssonderregel** bezeichnet. § 51a regelt in Wahrheit die Ansprüche der *vor dem 16.03.1990* ausgeschiedenen Mitglieder und deren Auszahlung in fünf gleichen Jahresraten. Die Verjährung steht in **§ 3b LwAnpG** (zehn Jahre, Beginn mit Schluss des Entstehungsjahres, ausdrücklich auch für Ansprüche nach § 44 Abs. 1) | § 3b LwAnpG eingesetzt, Abschnittsüberschrift und Gutachtenbeispiel entsprechend geändert; § 51a mit seinem tatsächlichen Inhalt neu beschrieben |
| 3 | `agrarrecht/skills/lwanpg-pruefung/SKILL.md`, `agrarrecht/agents/reviewer.md` | **§ 44 Abs. 6 LwAnpG als „Ratenzahlungsregelung, Verzinsung"**. Abs. 6 regelt die Ermittlung des Eigenkapitals auf Grundlage der nach Beendigung der Mitgliedschaft aufzustellenden ordentlichen Bilanz. Die Ratenzahlung steht in § 51a, die Fälligkeit in § 49 | Inhalt korrigiert, Zuordnung Ratenzahlung → § 51a / Fälligkeit → § 49 ausdrücklich ergänzt |

Fehler 2 und 3 sind keine Zitierfehler, sondern falsche Normzuordnungen mit unmittelbarer Mandatsrelevanz: eine auf § 51a gestützte Verjährungsprüfung greift an der Norm vorbei, die die Frist tatsächlich setzt.

### Behandlung von CAS-Schiedssprüchen und Verbandsregelwerken (`sportrecht`)

Der Auftrag, CAS-Awards nicht wie Gerichtsentscheidungen zu behandeln, wurde strukturell umgesetzt und nicht nur durch einen Marker:

- Die Liste in `dopingverfahren-verteidigung/SKILL.md` ist in **zwei** Abschnitte geteilt: „Staatliche Rechtsprechung (verifiziert)" und „Schiedssprüche und Verbandsregelwerke — **keine staatliche Rechtsprechung**". CAS 2009/A/1912 und CAS 2008/A/1644 standen zuvor als Positionen 3 und 4 zwischen BGH und BVerfG; das ist die Vermischung, die der Skill nicht reproduzieren soll.
- Der neue Abschnitt sagt ausdrücklich, dass CAS-Awards Schiedssprüche eines privaten Schiedsgerichts sind, in dejure und juris nicht nachgewiesen werden, nach deutschem Recht keine Bindungswirkung entfalten und nur über `jurisprudence.tas-cas.org` zu belegen sind. Der Versuch, den Volltext von CAS 2009/A/1912 abzurufen, blieb ergebnislos — beide Awards behalten ihren Marker, jetzt mit korrektem Quellenhinweis statt „prüfen in juris".
- WADC und NADC sind als **Verbandsregelwerke** gekennzeichnet, mit Verweis auf wada-ama.org bzw. nada.de; sie sind keine Rechtsnormen und werden im Skill auch nicht mehr in einer Reihe mit dem AntiDopG geführt.
- Dieselbe Trennung ist in `sportrecht/agents/researcher.md` nachgezogen: „Doping (staatliche Gerichte)" und „Doping (Schiedssprüche, **keine** Gerichtsentscheidungen — getrennt zitieren)".

Die Pechstein-Linie ist demgegenüber vollständig staatliche Rechtsprechung und vollständig verifiziert: OLG München → BGH → EGMR → BVerfG. Die BVerfG-Folgeentscheidung 1 BvR 2103/16 (03.06.2022) fehlte im Plugin und wurde ergänzt; sie ist für die Schiedsklausel-Prüfung tragend, weil sie dem BGH-Ergebnis den Justizgewährungsanspruch entgegenhält.

### Was weiterhin markiert bleibt (9)

- `agrarrecht`: Rspr.-Linien ohne Aktenzeichen zum Siedlungs-Vorkaufsrecht (§ 4/6 RSG), zu den OLG-Landwirtschaftssenaten sowie die drei LwAnpG-Linien (Auseinandersetzungsguthaben, Verjährungshemmung, Stufenklage). Für keine dieser Linien ließ sich eine namentlich belegte Entscheidung aus einer öffentlichen Quelle bestätigen. Sie sind jetzt als Suchauftrag gekennzeichnet, nicht als Zitat.
- `sportrecht`: CAS 2009/A/1912 und CAS 2008/A/1644 (s. o.); BGH zur Inhaltskontrolle der Vereinssatzung (st. Rspr., kein Az); BGH-Kartellsenat zum Reit-/Pferdesport — der im Researcher geführte Entscheidungsname „Bundesligaentscheidung Reiten" ließ sich **nicht** bestätigen und ist entsprechend als unbelegt gekennzeichnet.

### Was dejure nicht erreichen konnte

- **Kein Treffer über `?Datum=…&Aktenzeichen=…` bei Aktenzeichen mit Zusatz-Token**: `C-519/04 P` (Suffix „P") und `U 1110/14 Kart` (dejure führt „Kart." mit Punkt) liefen beide ins *Nichts gefunden*, obwohl beide Entscheidungen in der Datenbank stehen — der `?Text=<Az>`-Fallback fand sie sofort. Ein Fehlschlag des Datum-Az-Endpunkts ist also **kein** Beleg für die Nichtexistenz einer Entscheidung.
- **dejure hostet RSG, LPachtVG und LwAnpG nicht** (`/gesetze/RSG/4.html` leitet auf buzer.de weiter). Der sonst nützliche Weg, über die Normseite die zitierende Rechtsprechung zu finden, steht im Agrarrecht daher nicht offen — das ist der Hauptgrund, warum die BLw-Linien zu RSG und LwAnpG unbelegt bleiben. Dasselbe gilt für GrdstVG.
- **curia.europa.eu bleibt für WebFetch unbrauchbar**: der Aufruf leitet auf `infocuria.curia.europa.eu` um und liefert dort nur den Platzhalter „RPEX". Alle EuGH-Belege stammen deshalb aus dejure.
- **HUDOC funktioniert** über die Query-API (`/app/query/results?query=…&select=…`) und lieferte für 40575/10 Fallname, beide Beschwerde-Nummern, Datum und ECLI. Diese Route ist für künftige EGMR-Zitate zu bevorzugen.
- **CAS**: `jurisprudence.tas-cas.org` gibt über WebFetch keinen Volltext heraus.

### Zur Metrik `scripts/verify_citations.py`

Der Auftrag zu diesem Durchlauf ging davon aus, „to review" müsse **sinken**. Es steigt — agrarrecht 40 → 40, sportrecht 19 → 27 — und das ist korrekt, nicht defekt. Es bestätigt die bereits bei `urheber-medienrecht` (21 → 71) protokollierte Eigenschaft: das Skript zählt **Marker, nicht Belege**. Jede Fallzitierung *ohne* `[unverifiziert]` wird gewarnt, unabhängig davon, ob eine Primärquellen-URL danebensteht. Eine erfolgreiche Verifikation verwandelt daher ein stilles INFO in ein WARN. Die Zahl ist eine Markerzählung, kein Qualitätssignal, und taugt nicht als Fortschrittsmaß für diese Art von Durchlauf.

Ergänzend, weil es beim Inventarisieren auffiel: die 40 agrarrecht-Warnungen und 19 der sportrecht-Warnungen sind **unbekannte Gesetzesabkürzungen** (RSG, LPachtVG, LwVG, ALG, GAP-DZG, AntiDopG, KUG, EGV), die in der Abkürzungstabelle von `scripts/verify_citations.py` fehlen. Alle diese Gesetze existieren; die Warnung ist eine Lücke des Skripts, kein Zitierfehler. Eine Ergänzung der Tabelle lag außerhalb des Auftragsumfangs dieses Durchlaufs.

---

## Verification pass — long tail, 13 Bereiche (2026-07-21)

Abschlussdurchgang über die zuletzt verbliebenen, dünn verteilten Fallzitate. Methode: ausschließlich `WebFetch` gegen den dejure.org-Vernetzungs-Endpunkt (`?Gericht=…&Datum=…&Aktenzeichen=…`). Keine WebSearch, keine kostenpflichtige Datenbank. 9 Abrufe, kein Rate-Limit.

| Plugin | Verifiziert | Weiter markiert | Fehler gefunden | Art |
|---|---|---|---|---|
| `wohnungseigentumsrecht` | 1 (4 Fundstellen) | 0 | 0 | neu |
| `vertragsrecht` | 1 (3 Fundstellen) | 0 | 0 | neu |
| `patentrecht` | 2 (3 Fundstellen) | 0 | 1 | **Rest-Durchgang** |
| `mietrecht` | 1 (2 Fundstellen) | 0 | 0 | neu |
| `beamten-disziplinarrecht` | 1 (2 Fundstellen) | 0 | 0 | neu |
| `sozialrecht` | 1 | 0 | 0 | neu |
| `europarecht` | 1 | 0 | 0 | **Rest-Durchgang** |
| `berufsrecht-anwaltschaft` | 1 | 0 | 0 | neu |
| `aussenwirtschaft-zoll-sanktionen` | – | 0 | 0 | **Rest-Durchgang**, s. u. |
| `vergaberecht` | – | 0 | 0 | **Rest-Durchgang**, s. u. |
| `migrationsrecht` | – | 0 | 0 | **Rest-Durchgang**, s. u. |
| `zwangsvollstreckung` | – | 0 | 0 | neu, s. u. |
| `geldwaesche-aml-kyc` | – | 0 | 0 | neu, s. u. |
| **Summe** | **9 Entscheidungen / 17 Fundstellen** | **0** | **1** | |

### Der zentrale Befund: 18 der 35 gemeldeten „Fallzitate" sind keine

Die Aufgabenstellung ging von 35 unmarkierten Fallzitaten aus. Nach Sichtung jeder einzelnen Fundstelle sind **18 davon Regex-Artefakte** von `scripts/verify_citations.py` — Normzitate, die das Aktenzeichen-Muster `\d+/\d+` triggern. Kein einziges ist eine Rechtsprechungsangabe, keines war zu verifizieren, keines wurde geändert:

- `aussenwirtschaft-zoll-sanktionen` **9/9** — sämtlich `Anhang I VO 2021/821`, `Art. 3 / 4 / 5 VO 2021/821`, `Art. 2 Nr. 3 VO 2021/821`. Die Dual-Use-VO wird als „Az 2021/821" gelesen.
- `vergaberecht` **5/5** — `Art. 18 / 58 / 67 RL 2014/24/EU`, `Art. 4 RL 2014/24/EU`, `Art. 1, 2 RL 89/665/EWG`. Alle fünf tragen bereits einen EUR-Lex-CELEX-Link.
- `migrationsrecht` **2/2** — 2× `Art. 29 VO 604/2013` (Dublin-III-Überstellungsfrist).
- `geldwaesche-aml-kyc` **1/1** — `Art. 9 RL 2015/849`.
- `zwangsvollstreckung` **1/1** — die **Bruchzahlen** der Wertgrenzen: „7/10 und 5/10" in der Überschrift zu §§ 74a, 85a ZVG. Das Skript liest „10 und 5/10" als Aktenzeichen.

Damit bestätigt sich für `aussenwirtschaft-zoll-sanktionen`, `vergaberecht` und `migrationsrecht`, dass die früheren Durchgänge diese Bereiche **vollständig** abgearbeitet hatten: der Rest war nie Zitatschuld. Für `zwangsvollstreckung` und `beamten-disziplinarrecht` bestätigt sich die Zusage des Autors, unter strikter Kein-erfundenes-Az-Regel geschrieben zu haben — `beamten-disziplinarrecht` enthielt genau **ein** Aktenzeichen in vier Skills, und es ist korrekt.

### Verifizierte Entscheidungen (9)

Alle neun über dejure abgerufen, Gegenstand gegen die behauptete Proposition geprüft, Marker entfernt, amtliche Sammlung und `[dejure.org](…)`-Link ergänzt:

| Entscheidung | Fundstelle | Proposition — geprüft |
|---|---|---|
| BGH, Urt. v. 11.04.2025 – **V ZR 96/24** | NJW 2025, 1504 = NZM 2025, 351 | Teilanfechtung des Nachschuss-/Abrechnungsspitzen-Beschlusses post-WEMoG — trägt |
| BAG, Urt. v. 25.09.2018 – **8 AZR 26/18** | BAGE 163, 309 = NZA 2019, 121 | § 12a I 1 ArbGG schließt § 288 V BGB aus — trägt wörtlich |
| BGH, Urt. v. 26.03.2019 – **X ZR 109/16** | BGHZ 221, 342 = GRUR 2019, 496 | „Spannungsversorgungsvorrichtung", Restschadensersatz § 852 BGB / § 141 S. 2 PatG — trägt |
| BGH, Urt. v. 02.11.2000 – **I ZR 246/98** | BGHZ 145, 366 = GRUR 2001, 329 | „Gemeinkostenanteil", Verletzergewinn — trägt, aber s. Fehler 1 |
| BGH, Urt. v. 10.06.2015 – **VIII ZR 99/14** | NJW 2015, 2324 = NZM 2015, 532 | Schadensersatz § 280 I BGB bei vorgetäuschtem Eigenbedarf — trägt |
| BVerfG, Beschl. v. 29.07.2003 – **2 BvR 311/03** | BVerfGK 1, 292 = NVwZ 2004, 95 | Bewerbungsverfahrensanspruch, effektiver Rechtsschutz Art. 33 II iVm 19 IV GG — trägt |
| BVerfG, Urt. v. 05.11.2019 – **1 BvL 7/16** | BVerfGE 152, 68 = NJW 2019, 3703 | SGB-II-Sanktionsurteil — trägt |
| EuGH, Urt. v. 12.07.2005 – **C-304/02**, Kommission/Frankreich | Slg. 2005, I-6263 | Erstmals kombiniert Pauschalbetrag **und** Zwangsgeld (Zwangsgeld 316.500 €/Tag), Art. 228 EGV — trägt |
| BGH, Urt. v. 27.11.2019 – **VIII ZR 285/18** | BGHZ 224, 89 = NJW 2020, 208 | LexFox/wenigermiete.de, weiter Inkassobegriff § 10 RDG — trägt |

### Gefundener Fehler (1)

| # | Wo | Fehler | Auflösung |
|---|---|---|---|
| 1 | `patentrecht/skills/patentverletzung-klage/SKILL.md`, Schadensberechnung | „Gemeinkostenanteil", I ZR 246/98 in einer **patentrechtlichen** Schadensliste zitiert. Datum, Az und Gegenstand (Verletzergewinn, Anrechnung von Gemeinkosten) sind korrekt — die Entscheidung ist aber zum **Geschmacksmusterrecht** ergangen (§ 14a GeschmMG a.F.), nicht zum PatG. Ein leiser Herkunftswechsel derselben Art wie der `urheber-medienrecht`-Befund, nur milder: die Aussage trägt, die Rechtsquelle ist eine andere | Zitat behalten und um den ausdrücklichen Zusatz „ergangen zum Geschmacksmusterrecht, im Patentrecht entsprechend angewandt" ergänzt. Kein Marker, weil die Übertragung auf das Patentrecht gefestigt ist; die Herkunft wird aber nicht mehr verschwiegen |

Zwei ergänzende Beobachtungen ohne Fehlercharakter, aber protokollpflichtig:

- **Der `[verifiziert]`-Marker ist kein Konventions-Marker.** In `wohnungseigentumsrecht` (4×), `vertragsrecht` (2×) und `mietrecht` (1×) stand ein selbstgesetztes `[verifiziert]` bzw. „— Fundstelle verifiziert" ohne jede Quellenangabe. CONVENTIONS.md kennt nur drei Zustände, und „verifiziert" heißt dort *Marker weg plus URL*. Eine Behauptung der Verifikation ist kein Beleg. Alle sieben Instanzen sind jetzt durch echte Abrufe gedeckt und in Hausform gebracht.
- **Zwei Belege lagen auf nicht-autoritativen Hosts.** `patentrecht` verlinkte X ZR 109/16 auf einen **Kanzlei-Blog** (`preubohlig.de`) und I ZR 246/98 auf `openjur.**de**` (die Allowlist des Skripts kennt `openjur.**net**`). Beide sind durch dejure-Links ersetzt. `europarecht` verlinkte C-304/02 auf EUR-Lex, das nicht in `VERIFICATION_HOSTS` steht — ebenfalls auf dejure umgestellt, ohne den inhaltlichen Nachweis zu schwächen.

### Zur Metrik

Die **bereichsbezogene** Zahl ist eindeutig: die 13 realen Fallzitat-Warnungen in den 13 Zielbereichen sind auf **0** gegangen (`wohnungseigentumsrecht` 4→0, `vertragsrecht` 3→0, `patentrecht` 3→0, `mietrecht` 2→0, `beamten-disziplinarrecht` 2→0, `sozialrecht` 1→0, `europarecht` 1→0, `berufsrecht-anwaltschaft` 1→0). Diesmal *sinkt* die Zahl, weil der in dieser Session korrigierte Checker eine Fallzitierung mit autoritativem Link als *verifiziert* zählt.

Die **repo-weite** Zahl ging während dieses Durchgangs von 136 auf 93, aber **diese Differenz ist nicht diesem Durchgang zuzurechnen und darf nicht so gelesen werden.** Parallel arbeitende Agenten derselben Session haben währenddessen `reise-fluggastrecht`, `verfassungsrecht` und `arbeitsrecht` bearbeitet **und `scripts/verify_citations.py` selbst um 45 Zeilen erweitert**. Vorher- und Nachher-Wert stammen damit aus verschiedenen Messinstrumenten auf verschiedenen Dateiständen. Auf diesen Durchgang entfallen nachweislich **13** der entfallenen Warnungen. Die verbleibenden 18 Warnungen in den fünf oben genannten Bereichen sind die Normzitat-Artefakte und lassen sich nicht durch Zitatarbeit beseitigen, sondern nur durch eine Verschärfung von `AZ_RE` in `scripts/verify_citations.py` — außerhalb des Auftrags, Datei unberührt.

`scripts/validate.py` läuft über alle 58 Bereiche sauber, `scripts/eval.py` besteht 258/258. Keine `test.md` behauptete eines der korrigierten Zitate; keine Testdatei wurde geändert.

---

## Verification pass — `reise-fluggastrecht` (2026-07-21)

Methode: ausschließlich `WebFetch` gegen den dejure.org-Vernetzungs-Endpunkt (`?Gericht=…&Datum=…&Aktenzeichen=…`), für eine Entscheidung zusätzlich mit `&Ausgabe=Langtext` zur Kontrolle des Tenors. Keine WebSearch, keine kostenpflichtige Datenbank, kein curia-Abruf. **13 Abrufe, kein Rate-Limit erreicht.** dejure indexiert den EuGH vollständig; curia war nicht erforderlich.

| Plugin | Verifiziert | Weiter markiert | Fehler gefunden |
|---|---|---|---|
| `fluggastrechte-vo-261` | 10 Entscheidungen (9 geprüft + 1 neu belegt) | 3 Linien ohne Az | 1 |
| `pauschalreise-maengel` | 2 Entscheidungen | 1 Linie ohne Az | 0 |
| `reiseruecktritt-insolvenzschutz` | 2 Entscheidungen | 1 Linie ohne Az | 1 |
| `reisevermittlung-informationspflichten` | 2 Entscheidungen | 1 Linie ohne Az | 0 |
| **Summe (unique)** | **12 von 12 Zitaten geprüft, 11 bestätigt, 1 neu ergänzt** | **6 Linien ohne Az** | **2** |

Alle 25 unmarkierten Fallzitate des Bereichs betrafen zwölf unterschiedliche Entscheidungen (Mehrfachnennungen in Fließtext, Rspr.-Listen und `agents/researcher.md`). **Jede der zwölf wurde einzeln abgerufen.**

### Bestätigt — Gericht, Datum, Aktenzeichen und Fundstelle stimmen (11)

| Entscheidung | Fundstelle laut dejure | Bemerkung |
|---|---|---|
| EuGH, 19.11.2009 – verb. Rs. C-402/07 und C-432/07, *Sturgeon u.a.* | NJW 2010, 43 = EuZW 2009, 890 = Slg. 2009, I-10923 | joined case; beide Nummern korrekt geführt |
| EuGH, 23.10.2012 – verb. Rs. C-581/10 und C-629/10, *Nelson u.a.* | NJW 2013, 671 = EuZW 2012, 906 | joined case |
| EuGH, 22.12.2008 – Rs. C-549/07, *Wallentin-Hermann* | NJW 2009, 347 = EuZW 2009, 111 | |
| EuGH, 17.09.2015 – Rs. C-257/14, *van der Lans* | NJW 2015, 3427 | |
| EuGH, 17.04.2018 – verb. Rs. C-195/17 u.a., *Krüsemann u.a.* | NJW 2018, 1592 = EuZW 2018, 457 | dejure führt **25** verbundene Rechtssachen (C-195/17 bis C-292/17); die Zitierung als „C-195/17" allein ist verkürzt und wurde auf „verb. Rs. C-195/17 u.a." korrigiert |
| EuGH, 11.06.2020 – Rs. C-74/19, *Transportes Aéreos Portugueses* | NJW-RR 2020, 871 = EuZW 2020, 617 | Parteiname im Skill zuvor nicht genannt, ergänzt |
| EuGH, 26.02.2013 – Rs. C-11/11, *Air France/Folkerts* | NJW 2013, 1291 = EuZW 2013, 434 | |
| EuGH, 09.07.2009 – Rs. C-204/08, *Rehder* | EuZW 2009, 569 = NJW 2009, 487 (Ls.) | die NJW-Stelle ist nur ein Leitsatz; entsprechend gekennzeichnet |
| EuGH, 12.03.2002 – Rs. C-168/00, *Leitner* | NJW 2002, 1255 = EuZW 2002, 339 | ergangen zur Vorgänger-RL 90/314/EWG; ergänzt |
| EuGH, 08.06.2023 – Rs. C-407/21, *UFC-Que choisir und CLCV* | EuZW 2023, 709 = MDR 2023, 964 | Vorabentscheidung, RL (EU) 2015/2302, COVID-19-Rücktritt |
| EuGH, 08.06.2023 – Rs. C-49/22, *Austrian Airlines (Rückholflug)* | NJW 2023, 2629 = EuZW 2023, 815 | Az und Fundstelle korrekt, **Proposition falsch — siehe Fehler 2** |

### Neu ergänzt (1)

Die Aussage „Ankunftszeit ist der Zeitpunkt, zu dem mindestens eine Flugzeugtür geöffnet wird" stand ohne jeden Beleg und nur mit `[unverifiziert]`. Sie ist belegt durch **EuGH, Urt. v. 04.09.2014 – Rs. C-452/13, *Germanwings*, NJW 2015, 221 = EuZW 2014, 873** (dejure-Wortlaut: „der Zeitpunkt, zu dem mindestens eine der Flugzeugtüren geöffnet wird"). Der Marker konnte entfallen; die Formulierung wurde um die vom EuGH mitgeforderte Bedingung ergänzt, dass den Fluggästen das Verlassen des Flugzeugs gestattet ist.

### Die 2 gefundenen Fehler

| # | Wo | Fehler | Auflösung |
|---|---|---|---|
| 1 | `fluggastrechte-vo-261/SKILL.md` (Rspr.-Liste Nr. 9), `agents/researcher.md` | **BGH, Urt. v. 09.12.2014 – X ZR 147/13, NJW-RR 2015, 618** war als Beleg für die **„einheitliche Buchung"** von Anschlussflügen geführt. Datum, Aktenzeichen und Fundstelle sind bestätigt (dejure: NJW-RR 2015, 618 = MDR 2015, 447 = WM 2015, 1253) — die Entscheidung betrifft jedoch die **Anzahlungsklausel im Reisevertrag**: eine AGB-Klausel, die die Anzahlung auf nicht mehr als 20 % des Reisepreises begrenzt, benachteiligt den Reisenden nicht unangemessen und ist wirksam. Das ist der an diesem Tag wiederholt aufgetretene Typ: echte Entscheidung, richtiges Datum, richtiges Az, **falsche Proposition** | Die Entscheidung bleibt zitiert, aber mit ihrem **tatsächlichen** Gegenstand und einem ausdrücklichen Mismatch-Hinweis. Für die einheitliche Buchung wird auf die belegte Grundlage *Folkerts* verwiesen; eine BGH-Leitentscheidung hierzu ist als offener Rechercheauftrag mit `[unverifiziert - prüfen]` gekennzeichnet. **Kein Zitat gelöscht** |
| 2 | `fluggastrechte-vo-261/SKILL.md` (Art.-8-Abschnitt), `reiseruecktritt-insolvenzschutz/SKILL.md` (Rspr.-Liste Nr. 2) | **EuGH, 08.06.2023 – C-49/22** war zweifach falsch etikettiert: (a) im VO-261-Skill als Beleg für das **Wahlrecht des Art. 8 Abs. 1** — das ist reiner Verordnungstext, keine Aussage dieser Entscheidung; (b) im Rücktritts-Skill als **pauschalreiserechtliche** Entscheidung („Erstattung und Rückbeförderung"), obwohl sie zur **VO (EG) 261/2004** ergeht. Der über `&Ausgabe=Langtext` abgerufene Tenor lautet gegenteilig zur unterstellten Reichweite: ein konsularisch organisierter **Repatriierungsflug ist keine anderweitige Beförderung** iSd Art. 8 Abs. 1 lit. b; zugleich kennt die Verordnung „keine gesonderte Kategorie besonders außergewöhnlicher Umstände", die von Art. 8 vollständig befreite | Das Wahlrecht des Art. 8 wird jetzt der Norm selbst zugeordnet, nicht der Entscheidung. C-49/22 erhält einen eigenen Absatz mit beiden tatsächlichen Aussagen. Im Rücktritts-Skill ist ausdrücklich vermerkt, dass die Entscheidung Fluggastrecht und nicht Pauschalreiserecht betrifft und für § 651h BGB nur mittelbar heranzuziehen ist |

### Zur 3-Stunden-Linie

Der Skill kennzeichnete die Gleichstellung großer Verspätungen bereits korrekt als **richterrechtlich**. Das ist nach Prüfung von *Sturgeon* und *Nelson* bestätigt und wurde **nicht** zu einer Aussage des Verordnungstextes verdichtet. Ergänzt wurde ein ausdrücklicher Satz, dass diese Gleichstellung nicht in der Verordnung steht, sondern Auslegungsergebnis des EuGH ist und gegenüber Gericht und Gegenseite als solches zu kennzeichnen ist. Die Tabelle in Abschnitt 2 führt die große Verspätung unverändert als „richterrechtlich aus Art. 5–7 entwickelt".

Der pauschale Zusatz „Fundstellen verifiziert, Kernaussage im Volltext gegenzulesen `[unverifiziert - prüfen]`" ist entfallen: er behauptete eine Verifikation, die vor diesem Durchgang **nicht** stattgefunden hatte. Dieselbe Formel („— Fundstelle verifiziert") stand ohne Beleg hinter allen neun Positionen der Rspr.-Liste und in den drei anderen Skills; sie ist überall durch die tatsächlich abgerufene Primärquellen-URL ersetzt.

### Weiterhin markiert gelassen (6)

- `fluggastrechte-vo-261`: **Wetter** und **Vorfeldfolgen** als außergewöhnliche Umstände — instanzgerichtliche Kasuistik ohne belegbare Leitentscheidung. Der Sammel-Marker über der gesamten Kasuistik-Liste wurde auf genau diese beiden Punkte verengt, weil die übrigen vier jetzt belegt sind.
- `fluggastrechte-vo-261`: **BGH zur einheitlichen Buchung mit Anschlussflug** — offener Rechercheauftrag (Folge von Fehler 1).
- `pauschalreise-maengel`: Bemessung der Minderungsquote und Erheblichkeitsschwelle des § 651n Abs. 2 BGB.
- `reiseruecktritt-insolvenzschutz`: Auslegung des § 651h Abs. 3 BGB in Pandemie- und Krisenlagen.
- `reisevermittlung-informationspflichten`: Abgrenzung Veranstalter / Vermittler nach dem Auftreten gegenüber dem Reisenden.

Diese fünf Positionen tragen kein Aktenzeichen und kein Datum; der dejure-Endpunkt ist dort konstruktionsbedingt blind. Sie sind als Suchauftrag formuliert, nicht als Zitat.

### Was dejure nicht erreichen konnte

**Nichts.** Alle zwölf abgefragten Entscheidungen waren über `?Gericht=…&Datum=…&Aktenzeichen=…` beim ersten Versuch auflösbar — neun EuGH-Vorabentscheidungen, eine EuGH-Entscheidung mit 25 verbundenen Rechtssachen, eine weitere EuGH-Entscheidung von 2023 und ein BGH-Urteil. Der `?Text=`-Fallback war nicht nötig, das Weglassen von Zusatz-Token am Aktenzeichen ebenfalls nicht: keines der hier geführten Aktenzeichen trug ein Suffix (kein „P"-Rechtsmittel, kein „Kart."). Bei den beiden joined cases genügte jeweils die **erste** Rechtssachennummer; die zweite ist auf derselben Seite mit ausgewiesen. Das bestätigt die Vermutung des Auftrags nicht: die von der Sekundärliteratur nach Parteinamen zitierten Leitentscheidungen des Fluggastrechts waren im Bestand **durchgehend mit korrekter Nummer und korrektem Datum** geführt.

### Zahlenbewegung bei `scripts/verify_citations.py`

**Vorher 25 Warnungen, nachher 0.** Alle 25 waren `caselaw`-Warnungen über unmarkierte Fallzitate; keine einzige betraf eine unbekannte Gesetzesabkürzung. Nach der heutigen Korrektur des Prüfskripts zählt ein Zitat mit Link auf eine autoritative Quelle (`VERIFICATION_HOSTS`) als verifiziert, weshalb jede angehängte dejure-URL eine Warnung in ein INFO überführt. Die Gesamtzahl der Zitate stieg von 231 auf 235 (`fluggastrechte-vo-261` 40 → 43 durch *Germanwings* und die Aufspaltung des Art.-8-Absatzes, `reiseruecktritt-insolvenzschutz` 55 → 56).

`scripts/validate.py --area reise-fluggastrecht` läuft sauber, `scripts/eval.py --area reise-fluggastrecht` besteht 4/4 (104 Assertions). **Keine `test.md` musste geändert werden** — keine der vier Testdateien behauptete eines der korrigierten Zitate; die beiden Fehler standen ausschließlich in den Rechtsprechungslisten und im Researcher-Agenten.
