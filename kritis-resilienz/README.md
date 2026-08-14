# KRITIS-Resilienz (KRITIS-Dachgesetz)

**Production-grade Resilienz-Skills für Claude / Gemini / GPT.** Anwendungsbereich und Registrierung, Resilienzpflichten, Vorfallmeldung und Geschäftsleiterhaftung nach dem Dachgesetz zur Stärkung der physischen Resilienz kritischer Anlagen. Researcher → Drafter → Reviewer.

> **Physisch, nicht Cyber — und beides nebeneinander.** Das [KRITIS-Dachgesetz](https://www.gesetze-im-internet.de/kritisdachg/) setzt die **CER-Richtlinie (EU) 2022/2557** um und regelt die **physische** Resilienz kritischer Anlagen: Sabotage, Naturgefahren, technisches Versagen, Zutritt, Notfallorganisation, Wiederherstellung. Die **Cybersicherheit** bleibt beim BSIG/NIS2. Ein Betreiber kann beiden Regimen unterliegen und muss sich dann **zweimal registrieren** — beim **BSI** und beim **BBK**. Die gemeinsame Registrierungs- und Meldestelle von BSI und BBK ist eine technische Erleichterung, keine Zusammenlegung der Pflichten.

> **Der Ausnahmekatalog des § 4 Abs. 2 ist der wichtigste Filter — und die häufigste Falle.** Er nimmt § 3 Abs. 8, die §§ 9, 10, 12 bis 16, 18, 19 Abs. 2 sowie §§ 20 und 21 Abs. 6 für DORA-Finanzunternehmen, den Sektor IT und Telekommunikation, die Siedlungsabfallentsorgung (ohne § 12) und die Sozialversicherung (ohne § 1) aus. **Die Registrierungspflicht des § 8 steht nicht im Katalog** — wer die Ausnahme auf „das ganze Gesetz" erstreckt, versäumt sie.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `kritis-anwendungsbereich-registrierung` | Sektoren, Bereichsausnahmen, Erheblichkeitsschwellen, Dreimonats-Registrierung, Zuständigkeiten | §§ 2–10, 22, 24 KRITISDachG; RL (EU) 2022/2557; DORA Art. 2; § 1a KWG; § 293 VAG |
| `kritis-resilienzpflichten` | Risikoanalyse, Resilienzplan entlang der vier Ziele, Mindestanforderungen, Nachweise, Audits, Gleichwertigkeit | §§ 11–17, 19, 22, 24 KRITISDachG; §§ 28, 39 VwVfG; §§ 42, 70, 80 VwGO |
| `kritis-vorfallmeldung` | 24-Stunden-Erstmeldung, Aktualisierung, Monatsbericht, Pflichtinhalte, parallele Meldepflichten | § 18 KRITISDachG; BSIG/NIS2; Art. 33 DSGVO; DORA Art. 19; § 121 BGB |
| `kritis-governance-haftung` | Umsetzungs- und Überwachungspflicht, Innenhaftung, Berichtspflichten, Bußgeldstaffel, Verbandsgeldbuße | §§ 20, 21, 24 KRITISDachG; § 43 GmbHG; § 93 AktG; §§ 30, 130 OWiG |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: KRITIS-DachG, Rechtsverordnungen nach §§ 5, 11, 14, 18, CER-Richtlinie, BSIG, DORA, DSGVO, BBK- und BSI-Verlautbarungen
- [`agents/drafter.md`](./agents/drafter.md) – Entwürfe: Betroffenheitsanalyse, Registrierung, Risikoanalyse- und Resilienzplanstruktur, Vorfallmeldung, Governance-Beschlussvorlage, Behördenstellungnahme
- [`agents/reviewer.md`](./agents/reviewer.md) – Regime-, Fristen-, Nachweis- und Sanktionscheck (insbesondere § 4 Abs. 2, die Zuordnung zu den vier Zielen des § 13 Abs. 1 und die stundengenaue 24-Stunden-Frist)

## Installation

### Claude Code
```bash
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install kritis-resilienz
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area kritis-resilienz --out dist/gemini
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area kritis-resilienz --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Betroffenheit und Registrierungsfrist

```
/kritis-resilienz:kritis-anwendungsbereich-registrierung
Kommunaler Versorger mit Wasserwerk, Gasverteilnetz und
Siedlungsabfallverwertungsanlage; Schwellen für Wasser und Gas am
17.04.2026 überschritten. Konzerntochter im Sektor IT/TK, Beteiligung an
einer DORA-pflichtigen Sparkasse. Die Geschäftsführung hält die
NIS2-Registrierung beim BSI für ausreichend. Bitte Betroffenheitsanalyse
und Fristenplan.
```

### Szenario 2 – Nachweisverlangen der Behörde

```
/kritis-resilienz:kritis-resilienzpflichten
Auf das Nachweisverlangen vom 02.06.2026 haben wir ein ISO-27001-Zertifikat
und eine Liste von 40 Maßnahmen vorgelegt. Die Risikoanalyse stammt von
2021 und behandelt nur Sabotage und Cyber. Ein Audit von April 2026 wurde
nicht übermittelt. Perimetersicherung wurde aus Kostengründen gestrichen,
nicht dokumentiert. Bitte Bewertung und Stellungnahme.
```

### Szenario 3 – Vorfall mit paralleler Meldelage

```
/kritis-resilienz:kritis-vorfallmeldung
Am 12.05.2026 um 21:40 Uhr Brandstiftung an zwei Umspannstationen,
gleichzeitig kompromittierte Fernwirktechnik und Datenabfluss aus der
Kundendatenbank; 42.000 Haushalte ohne Wärme, Auswirkungen auf einen
österreichischen Abnehmer möglich. Die IT will die Forensik abwarten.
Bitte Meldelage, Fristen und Entwurf der Erstmeldung.
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Deutsche Normen werden mit gesetze-im-internet.de zitiert, EU-Rechtsakte mit ELI-Fundstelle.

**Schwellenwerte und Mindestanforderungen stehen nicht im Gesetz.** Sie ergeben sich aus den Rechtsverordnungen nach §§ 5 Abs. 1, 11, 14 und 18 KRITISDachG und sind mit Fassungsstand zu zitieren; das Plugin markiert sie mit `[unverifiziert – prüfen]`, solange sie nicht belegt sind.

**Rechtsprechung:** Das KRITIS-Dachgesetz ist erst **2026** in Kraft getreten — **Rechtsprechung existiert nicht**. Die Skills arbeiten deshalb mit Normtext, den Erwägungsgründen der RL (EU) 2022/2557, der Gesetzesbegründung und Verlautbarungen von BBK und BSI. Jede Entscheidung, die ein Modell zu diesem Gesetz nennt, ist als `[unverifiziert – prüfen]` zu behandeln.

## Hinweise

- **Zentrale Anlaufstelle ist das BBK** ([§ 3 Abs. 1](https://www.gesetze-im-internet.de/kritisdachg/__3.html)); **zuständige Behörde** ist je nach kritischer Dienstleistung die Bundesnetzagentur (Strom, Erdgas, Wasserstoff, öffentliche TK-Netze), das BMI, das BMWE (Mineralöl), die Generaldirektion Wasserstraßen und Schifffahrt und weitere Stellen nach § 3 Abs. 2.
- **Die Registrierungsfrist läuft ab dem Geltungszeitpunkt** — drei Monate, nachdem die Anlage als kritische Anlage gilt ([§ 8 Abs. 1](https://www.gesetze-im-internet.de/kritisdachg/__8.html)), nicht ab Kenntnis oder ab einem Behördenschreiben.
- **Der Resilienzplan folgt vier Zielen** ([§ 13 Abs. 1](https://www.gesetze-im-internet.de/kritisdachg/__13.html)): Verhinderung, physischer Schutz, Reaktion und Begrenzung, zügige Wiederherstellung. Jede Maßnahme wird einem Ziel zugeordnet; **unterlassene** Maßnahmen brauchen eine dokumentierte Zweck-Mittel-Relation nach Abs. 2.
- **Cyber-Zertifikate decken den physischen Schutz nicht ab.** § 17 erlaubt die Anerkennung gleichwertiger Nachweise — die Gleichwertigkeit ist je Ziel darzulegen.
- **Meldung: 24 Stunden ab Kenntnis, Bericht binnen eines Monats** ([§ 18 Abs. 1](https://www.gesetze-im-internet.de/kritisdachg/__18.html)). „Unverzüglich" heißt regelmäßig früher; die Erstmeldung enthält nur die verfügbaren Informationen. Meldepflichten nach BSIG, Art. 33 DSGVO und Sektorrecht bleiben nach § 18 Abs. 1 S. 4 **unberührt**.
- **Bußgelder sind gestaffelt** ([§ 24 Abs. 2](https://www.gesetze-im-internet.de/kritisdachg/__24.html)): bis 1.000.000 EUR, 500.000 EUR, 200.000 EUR und 100.000 EUR je nach Tatbestand; Behörde ist nach Abs. 3 das BBK oder die Sektorbehörde.
- **Mandantengeheimnis (§ 43a Abs. 2 BRAO, § 203 StGB):** Standort-, Anlagen- und Sicherheitsdaten sind besonders schutzbedürftig; keine Verarbeitung ohne AVV und Pseudonymisierung (`scripts/pii_redact.py`).
