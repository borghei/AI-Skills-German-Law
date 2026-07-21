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
