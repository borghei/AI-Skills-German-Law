# Entgelttransparenz (RL (EU) 2023/970 / EntgTranspG)

**Production-grade Entgelttransparenz-Skills für Claude / Gemini / GPT.** Umsetzungsstand, Auskunftsrechte, Berichterstattung und Durchsetzung. Researcher → Drafter → Reviewer.

> **Die Umsetzungsfrist ist abgelaufen — das deutsche Gesetz fehlt.** Art. 34 Abs. 1 der [Richtlinie (EU) 2023/970](https://eur-lex.europa.eu/eli/dir/2023/970/oj) verpflichtete die Mitgliedstaaten, bis zum **7. Juni 2026** umzusetzen. Deutschland hat die Frist **versäumt**. Daraus folgt die zentrale Weichenstellung dieses Plugins: Für **private** Arbeitgeber entfaltet die Richtlinie **keine** horizontale Wirkung — es gelten das [EntgTranspG](https://www.gesetze-im-internet.de/entgtranspg/) von 2017 in richtlinienkonformer Auslegung und **Art. 157 AEUV**, der unmittelbar auch zwischen Privaten gilt. Gegenüber **staatlichen** Arbeitgebern kommt unmittelbare Wirkung in Betracht, soweit die jeweilige Bestimmung unbedingt und hinreichend genau ist. Hinzu tritt die **Staatshaftung** wegen unterbliebener Umsetzung.

> **Prüfen Sie zuerst, ob inzwischen ein Umsetzungsgesetz verkündet wurde.** Jede Skill dieses Plugins beginnt mit dieser Prüfung und markiert den Stand mit `[unverifiziert – prüfen]`, solange er nicht gegen das Bundesgesetzblatt abgeglichen ist.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `entgelttransparenz-umsetzungsstand` | Drei-Ebenen-Analyse, unmittelbare Wirkung je Bestimmung, richtlinienkonforme Auslegung, Staatshaftung | Art. 26, 27, 34 RL (EU) 2023/970; Art. 157, 258, 260 AEUV; EntgTranspG |
| `entgelt-auskunftsanspruch` | Vorvertragliche Transparenz, Auskunftsrecht, Verschwiegenheitsklauseln, geltendes Verfahren der §§ 10 ff. EntgTranspG | Art. 5, 6, 7, 8, 12 RL; §§ 10–16 EntgTranspG; § 80 BetrVG |
| `entgeltberichterstattung` | Sieben Kennzahlen, Schwellen und Stichtage, gemeinsame Entgeltbewertung, Datenmodell und Mitbestimmung | Art. 9, 10, 11, 12, 13 RL; §§ 17–22 EntgTranspG; §§ 80, 87 BetrVG |
| `entgeltdiskriminierung-durchsetzung` | Anspruchsgrundlagen, Beweislastumkehr, Schadensersatz, Verjährung und Ausschlussfristen, Viktimisierung | Art. 14–25 RL; Art. 157 AEUV; §§ 3, 7 EntgTranspG; §§ 15, 16, 22 AGG; § 612a BGB |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: RL (EU) 2023/970, EntgTranspG, Art. 157 AEUV, RL 2006/54/EG, AGG, BetrVG, EuGH- und BAG-Rechtsprechung, Umsetzungsstand
- [`agents/drafter.md`](./agents/drafter.md) – Entwürfe: Umsetzungs- und Betroffenheitsanalyse, Antwort auf Auskunftsverlangen, Berichtsstruktur, Konzept der gemeinsamen Entgeltbewertung, Klage- und Verteidigungsschriftsatz
- [`agents/reviewer.md`](./agents/reviewer.md) – Ebenen-, Fristen- und Beweislastcheck (insbesondere zwei Monate nach Art. 7 Abs. 4 gegen drei Monate nach § 15 Abs. 3 EntgTranspG und die Vollumkehr des Art. 18 Abs. 2)

## Installation

### Claude Code
```bash
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install entgelttransparenz-eu
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area entgelttransparenz-eu --out dist/gemini
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area entgelttransparenz-eu --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Was gilt heute schon?

```
/entgelttransparenz-eu:entgelttransparenz-umsetzungsstand
Zwei Mandanten: ein kommunales Klinikum in GmbH-Form unter Landesaufsicht
und eine private Softwarefirma mit 180 Beschäftigten. Beide fragen Bewerber
nach dem bisherigen Gehalt und verwenden Entgeltverschwiegenheitsklauseln.
Ein Umsetzungsgesetz ist nicht verkündet. Was gilt für wen?
```

### Szenario 2 – Auskunftsverlangen beantworten

```
/entgelttransparenz-eu:entgelt-auskunftsanspruch
Auskunftsverlangen einer Entwicklerin vom 15.07.2026; Arbeitgeber privat
mit 180 Beschäftigten. Vier Kollegen mit gleicher Tätigkeitsbeschreibung,
zwei mit abweichenden Aufgaben, aber vergleichbarer Verantwortung. Der
Arbeitgeber will unter Hinweis auf Betriebsgröße und Datenschutz
vollständig verweigern. Bitte Antwortentwurf.
```

### Szenario 3 – Beweislast im Prozess

```
/entgelttransparenz-eu:entgeltdiskriminierung-durchsetzung
Teamleiterin, privater Arbeitgeber mit 400 Beschäftigten, 900 EUR
Grundgehaltsdifferenz plus Bonus. Auskunftsverlangen vom Juli 2026 nie
beantwortet, kein Entgeltbericht, keine Entgeltbewertung. Nach dem
Verlangen wurde ihr ein Förderprogramm gestrichen. Tarifvertrag mit
dreimonatiger Ausschlussfrist. Bitte Anspruchsprüfung und Beweislastkette.
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). EU-Rechtsakte werden mit ELI-Fundstelle zitiert, deutsche Normen mit gesetze-im-internet.de.

**Rechtsprechung:** Zu Art. 157 AEUV, zur Vergleichbarkeit von Tätigkeiten, zur Darlegungslast nach § 22 AGG sowie zu unmittelbarer Richtlinienwirkung, weitem Staatsbegriff und unionsrechtlicher Staatshaftung besteht **gefestigte** Rechtsprechung von EuGH und BAG. Zur **RL (EU) 2023/970 selbst liegt noch keine Judikatur vor**. Die Skills benennen deshalb die Streitfelder, behaupten aber keine Aktenzeichen; jede genannte Entscheidung ist als `[unverifiziert – prüfen]` zu behandeln, bis sie in curia.europa.eu, juris oder Beck-Online belegt ist.

## Hinweise

- **Zwei Fristen, die nie zu vermischen sind:** Das Auskunftsrecht nach **Art. 7 Abs. 4** der Richtlinie ist binnen **zwei Monaten** zu erfüllen, das Verfahren nach **§ 15 Abs. 3 EntgTranspG** binnen **drei Monaten**.
- **Die Richtlinie kennt keinen Schwellenwert für das Auskunftsrecht.** Die **200**-Beschäftigten-Schwelle und die **Sechs-Personen-Vergleichsgruppe** stehen im EntgTranspG, nicht in Art. 7.
- **Berichtsstichtage:** ab **250** Beschäftigten jährlich ab dem **07.06.2027**, **150–249** dreijährlich ab dem 07.06.2027, **100–149** dreijährlich ab dem **07.06.2031** — jeweils über das **vorangehende Kalenderjahr**. Wer 2027 berichtet, braucht die Daten aus 2026.
- **Die gemeinsame Entgeltbewertung nach Art. 10** wird ausgelöst, wenn in **einer** Arbeitnehmergruppe ein Unterschied von mindestens **5 Prozent** besteht, der weder gerechtfertigt noch binnen **sechs Monaten** korrigiert wurde. Das Halbjahr ist das eigentliche Steuerungsfenster.
- **Art. 18 Abs. 2 ist der schärfste Hebel:** Hat der Arbeitgeber die Transparenzpflichten der Art. 5, 6, 7, 9 und 10 verletzt, muss **er** beweisen, dass keine Diskriminierung vorliegt — es sei denn, der Verstoß war **offensichtlich unbeabsichtigt und geringfügig**, was er selbst nachzuweisen hat.
- **Art. 21 Abs. 3 lässt Erlöschensvorschriften unberührt.** Tarifliche und vertragliche **Ausschlussfristen** sind deshalb neben der Verjährung stets gesondert zu prüfen — ebenso die Zweimonatsfrist des § 15 Abs. 4 AGG.
- **Mandantengeheimnis (§ 43a Abs. 2 BRAO, § 203 StGB):** Entgeltdaten sind besonders sensibel; Art. 12 der Richtlinie und die DSGVO begrenzen Verwendung und Veröffentlichungstiefe. Keine Verarbeitung ohne AVV und Pseudonymisierung (`scripts/pii_redact.py`).
