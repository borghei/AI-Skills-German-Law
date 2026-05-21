# Verification Log

A running log of source-verification passes on the skills in this repository. Every entry says what was checked, against which source, and what was found. The goal is provenance: any reader can re-verify what we relied on, and the gaps we knowingly left open.

## Verification pass — 2026-05-21

**Verifier:** Borghei (with AI assistance, knowledge cutoff January 2026)
**Scope:** All 15 skills across 13 areas. Focus on statutory citations, regulatory timelines, and Bußgeldhöhen.

### Methodology

- **Statutes:** Checked against the consolidated text on `buzer.de` (mirrors gesetze-im-internet.de in machine-readable form; cites BGBl. references).
- **EU regulations:** Cross-checked against EUR-Lex anchors, the EU AI Act Implementation Timeline tracker (artificialintelligenceact.eu, last updated 2024-08-01), and Wikipedia (en) summary articles for CSRD/CSDDD/NIS2 — Wikipedia not as authority, but as a freshness indicator for recent reforms.
- **Case law:** **Not verified.** Every BAG/BGH/EuGH citation in this repo continues to carry `[unverifiziert – prüfen in Beck-Online/juris]`. Verification requires Beck-Online or juris access. This is a known gap, see *Known gaps* below.

### What was verified-current ✅

| Skill / area | Anchor checked | Status |
|---|---|---|
| `arbeitsrecht/kuendigungs-pruefung` | § 23 KSchG (Geltungsbereich, Schwellen) | Current (last amendment 14.06.2021 BGBl. I S. 1762) |
| `arbeitsrecht/aufhebungsvertrag` | § 623 BGB Schriftform, § 159 SGB III Sperrzeit, § 34 EStG Fünftelregelung | Current — no recent reform |
| `arbeitsrecht/abmahnung` | §§ 314 Abs. 2, 626 BGB; § 83 BetrVG | Current |
| `datenschutzrecht/auskunftsersuchen-art-15` | Art. 12, 15, 82 DSGVO; § 34 BDSG | Stable since 2018; case-law continues to evolve |
| `vertragsrecht/agb-kontrolle` | §§ 305–310 BGB | Current — core unchanged since 2002 Schuldrechtsreform |
| `mietrecht/mieterhoehung-558-bgb` | §§ 558, 558a–e, 556d BGB | Current |
| `gesellschaftsrecht/gmbh-geschaeftsfuehrerhaftung` | §§ 43, 64 GmbHG; §§ 15a, 15b InsO | Current (§ 15b InsO seit StaRUG 2021) |
| `strafrecht/strafbefehl-pruefung` | §§ 407 ff. StPO, §§ 147, 257c StPO | Current |
| `ki-vo-compliance/hochrisiko-klassifizierung` | Art. 6, 26, 50, 99 + Anhang III KI-VO; phasierte Anwendung | Current |
| `nis2/meldepflicht-24h` | Richtlinie 2022/2555 — Art. 20, 21, 23 | EU-Recht current |
| `lieferkettengesetz/risikoanalyse-lksg` | §§ 4, 5, 9, 10, 24 LkSG | Statute current; Bußgeldnormen ⚠️ siehe Updates |
| `dora/ict-risikomanagement` | VO 2022/2554 Art. 5 ff., 17, 26, 28 | Current — in Kraft seit 17.01.2025 |
| `dsa-dma/dsa-statement-of-reasons` | Art. 16, 17, 20–22, 24 DSA | Current |

### What was updated 🔧

#### 1. `lieferkettengesetz/risikoanalyse-lksg/SKILL.md`

**Bußgeldrahmen korrigiert.** Vorher: „bis zu 8 Mio. EUR oder 2 % des weltweiten Jahresumsatzes". Korrekt nach § 24 Abs. 2 LkSG:

- bis **800.000 EUR** für Abhilfemaßnahmen (Abs. 1 Nr. 6, 7 lit. a)
- bis **500.000 EUR** für Risikoanalyse-, Festlegungs- u.a. Verletzungen (Abs. 1 Nr. 1, 2, 4, 5, 13)
- bis **100.000 EUR** in den übrigen Fällen

Die **2 %-Regelung** des § 24 Abs. 3 LkSG gilt **nur** für juristische Personen mit durchschnittlichem Jahresumsatz > 400 Mio. EUR und ist auf bestimmte Abhilfeverstöße beschränkt.

**CSDDD-Abschnitt erweitert** mit:
- Adoption 24.05.2024
- Phase 1: 26.07.2027 (> 6.000 EE und > 1,5 Mrd. EUR Nettoumsatz)
- Phase 2: 26.07.2028 (> 900 Mio. EUR Nettoumsatz)
- Hinweis auf Omnibus-Vereinfachungs-Initiative (Feb 2025) + November-2025-EP-Änderungen + Verschmelzungsplan CSRD/CSDDD/Taxonomie

#### 2. `arbeitsrecht/kuendigungs-pruefung/SKILL.md`

**Leiharbeitnehmer-Berücksichtigung in § 23 KSchG korrigiert.** Vorher: „außer Betracht". Korrekt nach BAG-Rechtsprechung (BAG, Urt. v. 24.01.2013 – 2 AZR 140/12, NZA 2013, 726 `[unverifiziert]`): Leiharbeitnehmer zählen im Entleiherbetrieb mit, wenn ihr Einsatz auf regelmäßigem Beschäftigungsbedarf beruht.

**Altbestands-Schwelle ergänzt:** Für AN mit Beschäftigungsbeginn vor 31.12.2003 gilt die Schwelle > 5 AN (§ 23 Abs. 1 Sätze 2, 3 KSchG).

#### 3. `ki-vo-compliance/README.md`

**Phasierte Anwendung präzisiert** mit den konkreten Daten (verifiziert via artificialintelligenceact.eu):

- 02.02.2025 — Verbotene Praktiken Art. 5 + KI-Kompetenzpflicht Art. 4
- 02.05.2025 — Verhaltenskodizes fertiggestellt
- 02.08.2025 — Notifizierte Stellen, GPAI, Sanktionen
- 02.08.2026 — Hauptanwendung
- 02.08.2027 — Anhang I + Altbestand GPAI
- 02.08.2030 — Behörden + Großdatenbanken

#### 4. `csrd/wesentlichkeitsanalyse-doppelt/SKILL.md`

**Omnibus-Hinweis ergänzt.** Klarstellung: EU-Kommission hat am 26.02.2025 das „Omnibus I"-Vereinfachungspaket vorgeschlagen, darunter eine „Stop-the-Clock"-Initiative für Wave 2/3 (Verschiebung auf 2028). November 2024 zusätzlich Verschmelzungsplan CSRD/CSDDD/Taxonomie. November 2025 EU-Parlamentsänderungen mit konservativer Mehrheit. Empfehlung: aktueller Stand vor jeder Mandatsentscheidung tagesaktuell prüfen.

#### 5. `hinweisgeberschutz/skills/meldestelle-einrichten/SKILL.md`

**Bußgeldspanne präzisiert.** Beibehalten: 20.000 EUR für fehlende Meldestelle (§ 40 Abs. 2 Nr. 2). Ergänzt: 50.000 EUR für Vertraulichkeitsverletzung (§ 8) und Repressalien (§ 36); Behindern einer Meldung (§ 7 Abs. 2). Stand verifiziert via buzer.de: HinSchG zuletzt geändert durch Art. 14 G. v. 02.12.2025 (BGBl. 2025 I Nr. 301). Zusätzlich HinSchGOWiZustV v. 09.04.2025 (BGBl. 2025 I Nr. 111) genannt — BfJ ist Verfolgungsbehörde.

### Known gaps ⚠️

**1. Case-law citations.** Alle BAG/BGH/EuGH-Zitate tragen `[unverifiziert – prüfen]`. Verifikation erfordert Beck-Online / juris / openjur / Gerichtsdatenbank. Höchste Contributing-Priorität — siehe [CONTRIBUTING.md](./CONTRIBUTING.md).

**2. NIS2UmsuCG (deutsche NIS2-Umsetzung).** Status zum Verifikationsdatum 2026-05-21 **nicht abschließend geklärt**. Knowledge-Cutoff der AI-Assistenz (Januar 2026): Gesetz war im Bundestag noch nicht beschlossen, mehrfach verzögert seit Transpositionsfrist 17.10.2024. Mögliche Beschlussfassung zwischen 2026-02 und 2026-05 nicht überprüft. **Vor Mandatsanwendung Stand prüfen:** Bundesgesetzblatt, BMI / BSI.

**3. CSDDD-Umsetzungsstand in Deutschland.** Transpositionsfrist Mitte 2026. Deutsches Umsetzungsgesetz war bei Knowledge-Cutoff noch nicht in Sicht. **Vor Mandatsanwendung Stand prüfen.**

**4. CSRD-Omnibus.** Vorschlag 26.02.2025; finaler Verabschiedungs- und Inkrafttretensstand nicht abschließend geklärt. Wikipedia-Quelle markiert „proposed but not yet adopted" zum Zeitpunkt der Artikelaktualisierung. **Vor Mandatsanwendung Stand prüfen.**

**5. EU-US Data Privacy Framework.** Beibehalten, keine Statusaussage in den Skills. Im Knowledge-Cutoff: in Kraft, aber durch Schrems III angreifbar. **Vor Mandatsanwendung Stand prüfen.**

### Quellen dieser Verifikationsrunde

- `buzer.de` (mit `dejure.org` als Redirektor) — Bundesrecht konsolidiert, BGBl.-Referenzen
- `artificialintelligenceact.eu/implementation-timeline/` — KI-VO Timeline, Stand 2024-08-01
- `en.wikipedia.org/wiki/Corporate_Sustainability_Reporting_Directive` — CSRD/Omnibus-Stand
- `en.wikipedia.org/wiki/Corporate_Sustainability_Due_Diligence_Directive` — CSDDD-Stand und Verschmelzungsplan
- `gesetze-im-internet.de` — direkter Zugriff per WebFetch geblockt; statutory anchors validated via mirrors

### CI-Status

- `python scripts/validate.py` → 13/13 areas valid
- `python scripts/eval.py` → 15/15 skills passing structural assertions

---

## Wie eine künftige Verifikationsrunde durchgeführt wird

1. Datum stempeln, neuen Abschnitt anlegen.
2. Liste der seit der letzten Runde betroffenen Rechtsgebiete (z. B. via Newsletter Beck-Online, Behördenberichte, EU-Amtsblatt RSS).
3. Pro betroffenem Skill: statutory anchor gegen das öffentliche Mirror prüfen; falls Aktenzeichen verifizierbar geworden, Marker entfernen.
4. Updates committen, in diesem Log dokumentieren.
5. Bei Bedarf neuen Eintrag in `tests/<skill>.test.md` für die neue Anchor-Citation.

---

**Disclaimer.** This log records what was checked when. It is not legal advice. Statute texts evolve; case law evolves faster. Re-verification is a continuous obligation, not a one-time event.
