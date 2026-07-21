# M&A / Transaktionsrecht

**Production-grade Transaktionsrechts-Skills für Claude / Gemini / GPT.** Unternehmenskauf aus deutscher Praxisperspektive: Share Deal und Asset Deal, Garantie- und Freistellungsregime, Due Diligence mit Datenschutz- und Kartellrechtsrahmen sowie die zwingenden Haftungstatbestände der Betriebsübernahme. Researcher → Drafter → Reviewer.

> Abgrenzung: Gesellschaftsrechtliche Grundfragen (Kapitalerhaltung, Beschlussmängel, Geschäftsführerhaftung) liegen im Plugin `gesellschaftsrecht`, der Betriebsübergang in seiner arbeitsrechtlichen Tiefe in `arbeitsrecht/skills/betriebsuebergang`, die Fusionskontrolle in `kartellrecht` und die steuerliche Verfahrensseite in `steuerrecht`. Dieses Plugin geht **in die Tiefe** für den Transaktionsvertrag selbst und verweist im Übrigen, statt zu duplizieren.

## Skills

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `share-deal-spa` | Anteilskaufvertrag über GmbH-Geschäftsanteile: Form, Kaufgegenstand, Kaufpreismechanik, Signing/Closing-Struktur, Registervollzug | § 15 Abs. 3, 4, 5 GmbHG; § 16 Abs. 1–3 GmbHG; § 40 GmbHG; §§ 125, 158, 317, 1365 BGB; § 41 GWB |
| `garantien-freistellungen` | Garantiekatalog, Rechtsfolgenregime und Haftungsbegrenzung; Freistellungen und W&I-Versicherung | § 311 Abs. 1 BGB; §§ 434, 442, 443, 444 BGB; § 276 Abs. 3 BGB; §§ 195, 199, 202 BGB; §§ 30, 31 GmbHG |
| `due-diligence` | Request List, Datenraum, Disclosure und Übersetzung der Findings in Vertragsinstrumente | Art. 6 Abs. 1 lit. f, 9, 13, 14, 30 DSGVO; § 26 BDSG; §§ 1, 41 GWB; § 2 GeschGehG; § 203 StGB |
| `asset-deal-betriebsuebergang` | Einzelrechtsnachfolge, Vertragsübernahme und die zwingenden Haftungs- und Steuertatbestände der Betriebsübernahme | § 613a BGB; § 25 HGB; § 75 AO; § 1 Abs. 1a UStG; §§ 1, 13, 22 GrEStG; §§ 311b, 398, 929 ff. BGB |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: GmbHG, HGB, BGB, AO, UStG, GrEStG, GWB, DSGVO, Standardkommentare und Transaktionshandbücher
- [`agents/drafter.md`](./agents/drafter.md) – Erstellung in Gutachten-, Urteils- oder Vertragssprache, mit ausgewiesener Verhandlungsperspektive und Fallback-Positionen
- [`agents/reviewer.md`](./agents/reviewer.md) – Form-, Frist-, Vollzugs-, Datenschutz- und Berufsrechts-Check (Beurkundung, Long-Stop-Date, § 613a BGB, § 25 Abs. 2 HGB, § 41 GWB)

## Installation

### Claude Code
```bash
# Über Marketplace (empfohlen)
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install m-a-transaktionsrecht
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area m-a-transaktionsrecht --out dist/gemini
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area m-a-transaktionsrecht --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Formprüfung und Closing-Struktur

```
/m-a-transaktionsrecht:share-deal-spa
Erwerb von 100 % der Geschäftsanteile an einer GmbH. Die Parteien haben ein
privatschriftliches "verbindliches Term Sheet" mit Abtretungsverpflichtung
unterzeichnet; der Gesellschaftsvertrag enthält eine Zustimmungsklausel. Der
Zusammenschluss ist anmeldepflichtig. Bitte Formprüfung nach § 15 Abs. 3, 4
GmbHG, Closing-Checkliste und Behandlung der Gesellschafterliste § 40 GmbHG.
```

### Szenario 2 – Garantieverstoß nach Closing

```
/m-a-transaktionsrecht:garantien-freistellungen
14 Monate nach Closing zeigt der erste Jahresabschluss eine nicht bilanzierte
Pensionsverpflichtung von EUR 1,8 Mio. Der Verkäufer verweist auf den
Datenraum. Bitte Prüfung: Rechtsnatur der Garantie, Wirkung des § 442 BGB und
der Anti-Sandbagging-Klausel, Basket als Freibetrag oder Freigrenze, Cap,
vertragliche Verjährung und Deckung unter der W&I-Police.
```

### Szenario 3 – Betriebsübernahme im Asset Deal

```
/m-a-transaktionsrecht:asset-deal-betriebsuebergang
Erwerb eines Produktionsbetriebs einschließlich Betriebshalle, mit
Fortführung der eingeführten Firma und Übernahme nur eines Teils der
Belegschaft. Bitte Prüfung: Formbedürftigkeit § 311b BGB, Bestimmtheit der
Assetliste, § 613a BGB, Enthaftungsvermerk § 25 Abs. 2 HGB, § 75 AO,
§ 1 Abs. 1a UStG und Grunderwerbsteuer.
```

## Rechner

Fristen (Long-Stop-Date, Rüge- und Verjährungsfristen, Widerspruchsfrist § 613a Abs. 6 BGB, Jahresfrist § 75 AO) rechnet der deterministische Fristenrechner:

```bash
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 1 --einheit monate --land BY
```

Er leistet **nur** die Arithmetik der §§ 187–193 BGB. **Fristbeginn und Zugang bleiben rechtliche Eingaben.** Siehe [`../references/rechner.md`](../references/rechner.md).

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Standardkommentare: **Scholz** GmbHG, **Ulmer/Habersack/Löbbe** GmbHG, **Altmeppen** GmbHG, **Baumbach/Hopt** HGB, **Grüneberg** und **MüKoBGB**, **Tipke/Kruse** AO, **Bunjes** UStG, **Boruttau** GrEStG, **Immenga/Mestmäcker** Wettbewerbsrecht. Handbücher: **Beisel/Klumpp**, **Holzapfel/Pöllath**, **Semler/Volhard**.

Unverifizierte Zitate werden mit `[unverifiziert - prüfen]` markiert; `[generiert]` ist im gesamten Repository verboten.

## Hinweise

- **Doppelte Formbedürftigkeit § 15 Abs. 3 und Abs. 4 GmbHG.** Beide Rechtsgeschäfte sind beurkundungsbedürftig; die Heilung nach Abs. 4 S. 2 wirkt erst mit der Abtretung und nur ex nunc.
- **§ 16 Abs. 1 GmbHG.** Vor Aufnahme der Gesellschafterliste im Handelsregister kann der Erwerber gegenüber der Gesellschaft keine Rechte ausüben — Beschlüsse davor sind fehlerhaft, soweit nicht die Rückwirkung nach S. 2 greift.
- **§ 613a BGB ist zwingend.** Der Betriebsübergang lässt sich nicht durch die Gestaltung des Assetkreises vermeiden, wenn die wirtschaftliche Einheit ihre Identität wahrt.
- **§ 25 Abs. 2 HGB.** Der vertragliche Haftungsausschluss wirkt gegenüber Dritten nur bei Registereintragung und Bekanntmachung oder individueller Mitteilung.
- **Vollzugsverbot § 41 GWB / Art. 7 FKVO.** Kein Einfluss auf das operative Geschäft der Zielgesellschaft vor Freigabe; Informationsaustausch zwischen Wettbewerbern nur über ein Clean Team.
- **Mandantengeheimnis (§ 43a Abs. 2 BRAO, § 203 StGB):** Datenraum- und Zielgesellschaftsdaten nur in Werkzeuge mit Auftragsverarbeitungsvertrag. Personaldaten vor dem Upload anonymisieren oder schwärzen.
- **Steuerliche Aussagen** dieses Plugins sind Strukturhinweise, keine Steuerberatung. Bei Zweifeln verbindliche Auskunft nach § 89 Abs. 2 AO einholen und steuerliche Zweitmeinung dokumentieren.
