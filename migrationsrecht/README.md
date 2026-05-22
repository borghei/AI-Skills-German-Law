# Migrationsrecht

**Production-grade Skills für deutsches Migrations- und Asylrecht für Claude / Gemini / GPT.** AufenthG, AsylG, FreizügG/EU, StAG und einschlägiges EU-Recht (Dublin III, Qualifikations- und Verfahrens-RL) aus deutscher anwaltlicher Praxisperspektive. Researcher → Drafter → Reviewer.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `aufenthaltstitel-pruefung` | Prüfung der einschlägigen Titelart und der allgemeinen Erteilungsvoraussetzungen, Entwurf von Antrag und Begründung | §§ 4, 5, 7, 9, 9a, 16b, 18 ff., 25, 25a–c, 28, 30 AufenthG |
| `asylantrag-vorbereitung` | Vorbereitung des Asylantrags und der BAMF-Anhörung inkl. Dublin- und Schutzformen-Triage | §§ 3, 4, 13, 14, 25, 29, 30, 71 AsylG; § 60 V/VII AufenthG; VO (EU) 604/2013; RL 2011/95/EU |
| `abschiebungsschutz` | Eilrechtsschutz gegen Abschiebung und Duldungsantrag | § 80 V VwGO, § 123 VwGO; § 36 III, § 74 I AsylG; § 60a, § 60 V/VII AufenthG; Art. 8 EMRK |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: AufenthG/AsylG, EU-Recht, BVerwG/EuGH/EGMR, Bergmann/Dienelt, Hailbronner, Marx
- [`agents/drafter.md`](./agents/drafter.md) – Erstellung im Gutachten- oder Urteilsstil mit Behörden- und Gerichtsadressaten
- [`agents/reviewer.md`](./agents/reviewer.md) – Frist-, Quellen- und Berufsrechts-Check inkl. Frist-Kalender (1 Woche § 36 III AsylG, 2 Wochen § 74 I AsylG, Dublin 6/12/18 Monate, Folgeantrag 3 Monate § 71 IV AsylG)

## Installation

### Claude Code
```bash
# Über Marketplace (empfohlen)
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install migrationsrecht

# Oder als ZIP
# Claude Code → Customize Plugins → Install from .zip → migrationsrecht.zip
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area migrationsrecht --out dist/gemini
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area migrationsrecht --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Aufenthaltstitel zum Zweck der Erwerbstätigkeit

```
/migrationsrecht:aufenthaltstitel-pruefung
Mandantin (Drittstaatsangehörige, Indien, Informatikerin) hat
Arbeitsangebot eines deutschen IT-Unternehmens (Bruttogehalt 60.000 €).
Bitte prüfen: Blaue Karte EU § 18b AufenthG oder § 18a, Voraussetzungen
nach § 5 AufenthG, Visumverfahren § 6 III, Vorabzustimmung BA.
```

### Szenario 2 – Asylantrag mit Dublin-Bezug

```
/migrationsrecht:asylantrag-vorbereitung
Mandant (Syrien, 28 J.) ist über Griechenland in das Bundesgebiet
eingereist. Eurodac-Treffer vorhanden. BAMF-Anhörung in 3 Wochen.
Bitte Strategie: Dublin-Überstellungsfristen § 29 I Nr. 1 AsylG iVm
VO (EU) 604/2013, Vorbereitung der Anhörung § 25 AsylG zu
Flüchtlingseigenschaft § 3 / subsidiärem Schutz § 4 AsylG.
```

### Szenario 3 – Eilrechtsschutz vor Abschiebung

```
/migrationsrecht:abschiebungsschutz
BAMF-Bescheid (Asylantrag als offensichtlich unbegründet abgelehnt,
§ 30 AsylG, Abschiebungsandrohung § 34 AsylG) ist gestern zugestellt.
Mandant ist herzkrank (ärztliche Bescheinigung liegt vor). Bitte
Eilantrag § 80 V VwGO iVm § 36 III AsylG entwerfen und § 60 VII
AufenthG-Argumentation aufbereiten.
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Standardkommentare: **Bergmann/Dienelt** Ausländerrecht (Loseblatt, jeweils aktueller Stand), **Hailbronner** Ausländerrecht, **GK-AsylG** (Marx u. a.), **Marx** AsylG, **NK-AuslR** (Hofmann).

Rechtsprechung: BVerwG (1. Senat – Migrationssenat), EuGH (Dublin, Qualifikations-RL, Verfahrens-RL), EGMR (Art. 3, Art. 8 EMRK; Rule 39). Aktenzeichen werden mit `[unverifiziert – prüfen in juris/curia/hudoc]` markiert, soweit sie nicht extern verifiziert sind.

## Hinweise

- **Frist-Kalender ist tödlich.** § 36 III AsylG (1 Woche Eilantrag bei offensichtlich unbegründet), § 74 I AsylG (2 Wochen Klage), Dublin-Überstellungsfristen 6/12/18 Monate nach Art. 29 VO (EU) 604/2013, § 71 IV AsylG (3 Monate Folgeantrag).
- **Schnittstelle Sozialrecht.** AsylbLG-Leistungen und SGB II für anerkannte Schutzberechtigte werden im `sozialrecht`-Plugin behandelt; hier nur Querverweis.
- **Trauma- und Kultursensibilität.** Mandantenkommunikation in Migration / Asyl erfordert kultur- und traumasensible Anrede und idR Dolmetscher (§ 17 AsylG für das BAMF-Verfahren). Anrede in `Sie`-Form, keine Suggestivfragen.
- **Mandatsgeheimnis (§ 43a BRAO, § 203 StGB):** Keine echten Mandatsdaten ohne § 203-konformen Gateway. Pflicht zur Eintragung in das beA-System bei Schriftsätzen an Gerichte.
- **Keine Präjudizienbindung** deutscher Gerichte außer § 31 BVerfGG; EuGH-Urteile binden gem. Art. 260 AEUV im konkreten Verfahren; EGMR-Urteile binden Vertragsstaat nach Art. 46 EMRK.
