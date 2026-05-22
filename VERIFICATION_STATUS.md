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
