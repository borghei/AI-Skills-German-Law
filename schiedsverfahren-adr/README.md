# Schiedsverfahren und ADR

**Production-grade Schiedsrechts-Skills für Claude / Gemini / GPT.** Schiedsvereinbarung, Verfahrensführung, Aufhebung und Vollstreckbarerklärung nach dem Zehnten Buch der ZPO und dem New Yorker Übereinkommen. Researcher → Drafter → Reviewer.

> **Der Schiedsort ist die Weiche, an der dieses Rechtsgebiet steht oder fällt.** Liegt der Ort des schiedsrichterlichen Verfahrens nach [§ 1043 Abs. 1 ZPO](https://www.gesetze-im-internet.de/zpo/__1043.html) in Deutschland, gilt das Zehnte Buch vollständig ([§ 1025 Abs. 1 ZPO](https://www.gesetze-im-internet.de/zpo/__1025.html)) und die Vollstreckbarerklärung richtet sich nach [§ 1060 ZPO](https://www.gesetze-im-internet.de/zpo/__1060.html). Liegt er im Ausland, bleiben nur §§ 1032, 1033, 1050 ZPO anwendbar, und Anerkennung und Vollstreckung folgen [§ 1061 ZPO](https://www.gesetze-im-internet.de/zpo/__1061.html) iVm dem New Yorker Übereinkommen von 1958. Der Schiedsort bestimmt zugleich das zuständige Oberlandesgericht ([§ 1062 ZPO](https://www.gesetze-im-internet.de/zpo/__1062.html)). Jede Skill dieses Plugins macht seine Bestimmung deshalb zu Schritt 1 — und trennt ihn strikt vom Verhandlungsort.

> **Rechtsstand.** Das Zehnte Buch der ZPO ist Gegenstand des Gesetzes vom **20.05.2026 (BGBl. 2026 I Nr. 152)**. Die Änderungen sind auf gesetze-im-internet.de textlich nachgewiesen, dokumentarisch aber **noch nicht abschließend eingearbeitet**. Alle Skills dieses Plugins arbeiten auf der konsolidierten Fassung und weisen darauf hin, dass der Stand vor jeder Verwendung gegen das Bundesgesetzblatt abzugleichen ist `[unverifiziert – prüfen]`.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `schiedsvereinbarung-pruefung` | Wirksamkeit, Reichweite und Durchführbarkeit der Klausel; Schiedseinrede und Feststellungsantrag; Klauselgestaltung; mehrstufige Streitbeilegung | §§ 1025, 1029, 1030, 1031, 1032, 1034 Abs. 2, 1040, 1043, 1062 ZPO; §§ 126a, 203 BGB; MediationsG; § 278a ZPO |
| `schiedsverfahren-fuehrung` | Konstituierung, Ablehnung, rechtliches Gehör, Beweisaufnahme, einstweiliger Rechtsschutz, Schiedsspruch und Kosten | §§ 1033–1058, 1062 ZPO; § 204 Abs. 1 Nr. 11 BGB; DIS-SchiedsO 2018 |
| `aufhebungsantrag-1059` | Abschließender Katalog der Aufhebungsgründe, Dreimonatsfrist, Präklusion, Teilaufhebung, Zurückverweisung | §§ 1058, 1059, 1060 Abs. 2, 1062, 1063, 1065 ZPO; Art. 103 Abs. 1 GG |
| `vollstreckbarerklaerung-schiedsspruch` | Weg zum Titel: inländische und ausländische Schiedssprüche, Art. V und VII NYÜ, Vorlageerfordernisse, Anschlussvollstreckung | §§ 1060, 1061, 1062, 1063, 1064, 1065, 767, 794 Abs. 1 Nr. 4a, 829, 835 ZPO; NYÜ 1958 |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: Zehntes Buch der ZPO, New Yorker Übereinkommen, DIS- und ICC-Schiedsgerichtsordnung, IBA-Regelwerke als soft law, OLG- und BGH-Rechtsprechung
- [`agents/drafter.md`](./agents/drafter.md) – Entwürfe: Klauselprüfung und Ersatzklausel, Schiedsklage und Klagebeantwortung, Ablehnungsgesuch, Aufhebungsantrag, Antrag auf Vollstreckbarerklärung und deren Abwehr
- [`agents/reviewer.md`](./agents/reviewer.md) – Schiedsort-, Fristen-, Präklusions- und Quellencheck (insbesondere §§ 1032 Abs. 1, 1034 Abs. 2, 1037, 1040, 1058, 1059 Abs. 3 ZPO)

## Installation

### Claude Code
```bash
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install schiedsverfahren-adr
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area schiedsverfahren-adr --out dist/gemini
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area schiedsverfahren-adr --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Schiedsklausel gegenüber einem Verbraucher

```
/schiedsverfahren-adr:schiedsvereinbarung-pruefung
In unseren AGB gegenüber privaten Hauseigentümern steht: "Streitigkeiten
aus diesem Vertrag entscheidet ein Schiedsgericht in Frankfurt." Ein Kunde
klagt vor dem Landgericht; die Klageerwiderung steht aus. Frage: Können
wir die Schiedseinrede erheben, und hält die Klausel § 1031 Abs. 5 ZPO stand?
```

### Szenario 2 – Ablehnung eines Schiedsrichters und Gehörsrüge

```
/schiedsverfahren-adr:schiedsverfahren-fuehrung
DIS-Verfahren, Schiedsort München. Der von der Gegenseite benannte
Schiedsrichter berät seit Jahren deren Muttergesellschaft, ohne das je
offengelegt zu haben. Unsere Beweisanträge wurden ohne Begründung
zurückgewiesen. Bitte Ablehnungsgesuch, Fristen und Rügestrategie.
```

### Szenario 3 – Vollstreckung eines ausländischen Schiedsspruchs

```
/schiedsverfahren-adr:vollstreckbarerklaerung-schiedsspruch
ICC-Schiedsspruch, Schiedsort Zürich, 850.000 EUR gegen eine türkische
Gesellschaft ohne deutschen Sitz. Vermögen: Bankguthaben in Berlin,
Warenlager in Hamburg. In der Schweiz läuft eine Aufhebungsklage. Bitte
Zuständigkeit, Antrag, Sicherung und Prüfung der Art.-V-Einwände.
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). ZPO-Normen werden mit gesetze-im-internet.de zitiert. Das **New Yorker Übereinkommen** ist dort **nicht** veröffentlicht; maßgeblich ist der Text im Bundesgesetzblatt (BGBl. 1961 II S. 121).

**Institutionenrecht ist kein Gesetzesrecht.** DIS-SchiedsO 2018 und ICC-SchiedsO wirken über § 1042 Abs. 3 ZPO als Parteivereinbarung und verdrängen zwingende Vorschriften nicht. Die IBA Guidelines on Conflicts of Interest und die IBA Rules on the Taking of Evidence sind soft law und werden nur als Orientierung, stets mit Fassungsangabe und Marker, zitiert.

**Rechtsprechung:** Zuständig sind die Oberlandesgerichte (§ 1062 ZPO) und für die Rechtsbeschwerde der BGH (§ 1065 ZPO). Zu Formstrenge, ordre public und Präklusion besteht gefestigte Judikatur; jede konkrete Entscheidung ist vor Verwendung in juris, Beck-Online oder auf bundesgerichtshof.de zu verifizieren. Ohne Beleg gilt sie als `[unverifiziert – prüfen]`.

## Hinweise

- **Verbraucherform § 1031 Abs. 5 ZPO.** Ist ein Verbraucher beteiligt, muss die Schiedsvereinbarung in einer gesonderten, eigenhändig unterzeichneten Urkunde stehen, die keine anderen Vereinbarungen enthält; die Schriftform kann durch die elektronische Form nach § 126a BGB ersetzt werden. Eine Klausel in AGB oder im Hauptvertrag ist unwirksam.
- **Die Dreimonatsfrist des § 1059 Abs. 3 ZPO läuft ab Empfang, nicht ab Erlass.** Wer sie versäumt, verliert die Aufhebungsgründe der Nr. 1 nach § 1060 Abs. 2 S. 3 ZPO auch als Verteidigung im Vollstreckbarerklärungsverfahren.
- **Anordnungen des Schiedsgerichts nach § 1041 ZPO sind nicht unmittelbar vollstreckbar.** Erforderlich ist die Zulassung der Vollziehung durch das OLG (§ 1041 Abs. 2, § 1062 Abs. 1 Nr. 3 ZPO). Der staatliche Eilrechtsschutz nach § 1033 ZPO bleibt daneben offen — auch bei ausländischem Schiedsort.
- **Kein zweiter Rechtszug.** Aufhebungs- und Vollstreckbarerklärungsverfahren kennen keine révision au fond; die Kataloge des § 1059 Abs. 2 ZPO und des Art. V NYÜ sind abschließend.
- **§ 1064 Abs. 1 S. 2 ZPO erlaubt die Beglaubigung des Schiedsspruchs durch den bevollmächtigten Rechtsanwalt** — über Art. VII NYÜ auch bei ausländischen Schiedssprüchen ein spürbarer Vorteil gegenüber Art. IV NYÜ.
- **Mandantengeheimnis und Verfahrensvertraulichkeit (§ 43a Abs. 2 BRAO, § 203 StGB):** Schiedsverfahren sind regelmäßig vertraulich; keine Verarbeitung von Verfahrensinhalten ohne AVV und Pseudonymisierung (`scripts/pii_redact.py`).
