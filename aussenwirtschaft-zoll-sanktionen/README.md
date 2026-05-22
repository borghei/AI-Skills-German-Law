# Außenwirtschaftsrecht, Zollrecht, Sanktionsrecht

**Production-grade Skills für Claude / Gemini / GPT.** Außenwirtschaftsrecht (AWG/AWV), Unionszollrecht (UZK), EU-Dual-Use- und Sanktionsrecht aus deutscher Praxisperspektive: Ausfuhrkontrolle, BAFA-Genehmigungen, Sanktionslisten-Screening, Tarifierung und verbindliche Zolltarifauskunft. Researcher → Drafter → Reviewer.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `ausfuhr-dual-use-pruefung` | 4-Stufen-Prüfung Güterklassifikation, Listung Anhang I, Catch-all, BAFA-Antrag | VO (EU) 2021/821; §§ 4, 8 AWG; §§ 8 ff. AWV; § 18 AWG |
| `sanktionslisten-screening` | Treffer-Workflow Bereitstellungsverbot, Frostung, Meldung an BMWK/Bundesbank/Zoll | Art. 215 AEUV; VO (EU) 833/2014, 269/2014, 2017/1509 u.a.; § 18 AWG; GwG-Schnittstelle |
| `zolltarif-vzta-antrag` | TARIC-Tarifierung nach AV 1–6, Antrag verbindliche Zolltarifauskunft Art. 33 UZK | VO (EU) 952/2013 (UZK); VO 2015/2446 (UZK-DA); VO 2015/2447 (UZK-IA) |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: AWG/AWV, EU-Sekundärrecht, BAFA-Merkblätter, Zoll-Dienstvorschriften, Standardkommentare
- [`agents/drafter.md`](./agents/drafter.md) – Erstellung im Gutachten- oder Urteilsstil; BAFA-/vZTA-/Sanktions-Meldungsentwürfe
- [`agents/reviewer.md`](./agents/reviewer.md) – Fristen-, Genehmigungs-, Straf-/Bußgeldrisiko-Check (§§ 17–19 AWG, § 18 KrWaffG) und Sanktions-BLOCKER-Prüfung

## Installation

### Claude Code
```bash
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install aussenwirtschaft-zoll-sanktionen
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area aussenwirtschaft-zoll-sanktionen --out dist/gemini
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area aussenwirtschaft-zoll-sanktionen --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Dual-Use-Ausfuhr in Drittland

```
/aussenwirtschaft-zoll-sanktionen:ausfuhr-dual-use-pruefung
Mandantin (Maschinenbau, Baden-Württemberg) will eine CNC-5-Achs-
Fräsmaschine in die Türkei ausführen. Endkunde ist ein türkisches
Luft- und Raumfahrt-Unternehmen. Bitte 4-Stufen-Prüfung nach VO (EU)
2021/821: Anhang-I-Listung, Catch-all Art. 4, BAFA-Genehmigungspflicht
und EU-AGG-Anwendbarkeit prüfen.
```

### Szenario 2 – Sanktions-Treffer im Onboarding

```
/aussenwirtschaft-zoll-sanktionen:sanktionslisten-screening
Beim Onboarding eines neuen B2B-Kunden (Zypern-GmbH) zeigt das
Screening einen möglichen Treffer auf einen Geschäftsführer in der
konsolidierten EU-Liste (Anhang I VO 269/2014, Russland). Bitte
False-positive-Bewertung, Bereitstellungsverbot Art. 2, Frostung,
Meldung an Bundesbank und Risiko § 18 AWG einschätzen.
```

### Szenario 3 – Verbindliche Zolltarifauskunft

```
/aussenwirtschaft-zoll-sanktionen:zolltarif-vzta-antrag
Importeur (Elektronik) will ein neuartiges Bauteil (smartes
Sensor-Modul mit eingebauter SIM-Karte) erstmalig aus China
einführen. Tarifierung ist streitig (Kap. 85 vs. 90). Bitte vZTA-
Antrag nach Art. 33 UZK entwerfen, mit AV 1–6 begründen.
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Standardkommentare: **Friedrich/Lieser** AWR, **Hocke/Sachs/Pelz** AWG/AWV, **Karpenstein/Mayer** Loseblatt Außenwirtschafts- und Zollrecht, **Krenzler/Herrmann/Niestedt** EU-Außenwirtschafts- und Zollrecht.

Rechtsprechung: EuGH (Sanktionen, Listing), BFH (Zollrecht), VG/OVG (Genehmigungsablehnungen) im Format gemäß `references/zitierweise.md`. Unverifizierte Zitate werden mit `[unverifiziert – prüfen]` markiert; EuGH-Entscheidungen sind in curia.europa.eu, BFH-Entscheidungen in juris/BFH-Datenbank zu verifizieren.

## Hinweise

- **Sanktionsrecht ist nicht verhandelbar.** Treffer auf einer EU-Sanktionsliste oder Bezug zu einem Russland-/Iran-/DVRK-gelisteten Gut sind ein **🔴 BLOCKER**: kein Geschäftsabschluss bis Klarheit. Strafbarkeit § 18 AWG: Freiheitsstrafe bis 5 Jahre, gewerbsmäßig bis 15 Jahre.
- **Vorrang länderspezifischer VOen vor Dual-Use.** Bei Russland (VO 833/2014, 269/2014, 692/2014), Iran (VO 267/2012), Syrien (VO 36/2012), DVRK (VO 2017/1509) ist zuerst die länderspezifische VO zu prüfen; sie ist regelmäßig strenger als die Dual-Use-VO.
- **BAFA-Bearbeitungsdauer ~10–12 Wochen** (Genehmigungsantrag ELAN-K2). Vorab-Anfragen / Nullbescheide vorsehen.
- **vZTA Art. 33 UZK:** 120 Tage Bearbeitung, 3 Jahre Bindung; Auskunft bindet auch andere Mitgliedstaaten.
- **Schnittstellen:** Geldwäsche/KYC (`geldwaesche-aml-kyc`), Strafrecht (`strafrecht`, § 18 KrWaffG), Steuerrecht/Einfuhrumsatzsteuer (`steuerrecht`).
- **US-Recht (EAR, OFAC, Re-Export-Kontrollen) nur als Hinweis** auf parallele Risiken; keine Beratung zu US-Recht — Verweis auf US-Counsel.
- **Mandatsgeheimnis (§ 43a BRAO, § 203 StGB):** Keine echten Geschäftspartner- oder Transaktionsdaten ohne § 203-konformen Gateway.
