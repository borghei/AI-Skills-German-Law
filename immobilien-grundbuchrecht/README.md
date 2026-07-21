# Immobilien- und Grundbuchrecht

**Production-grade Immobilienrechts-Skills für Claude / Gemini / GPT.** Grundstückskaufvertrag, Grundbuchverfahren nach der GBO, Grundschuld als Kreditsicherheit und die Begründung von Wohnungseigentum — aus notarieller und anwaltlicher Praxisperspektive. Researcher → Drafter → Reviewer.

> Abgrenzung: Der **laufende Betrieb** einer Wohnungseigentümergemeinschaft (Beschlussanfechtung, Hausgeldabrechnung, bauliche Veränderung) liegt im Plugin [`wohnungseigentumsrecht`](../wohnungseigentumsrecht/). Mietverhältnisse liegen in [`mietrecht`](../mietrecht/), das Bauvertragsrecht in [`baurecht`](../baurecht/), die Verwertung des Grundstücks in [`zwangsvollstreckung`](../zwangsvollstreckung/). Dieses Plugin geht **in die Tiefe** für Erwerb, Eintragung, Besicherung und Aufteilung von Grundbesitz.

## Skills

| Skill | Funktion | Anker |
|---|---|---|
| `grundstueckskaufvertrag` | Entwurf und Prüfung des Kaufvertrags von der Beurkundung bis zur Fälligkeitskaskade, einschließlich der Grenzen des Gewährleistungsausschlusses | § 311b Abs. 1 BGB; § 17 BeurkG; §§ 873, 925 BGB; §§ 883, 885 BGB; §§ 434, 442, 444, 446, 103, 566 BGB; § 28 BauGB |
| `grundbuchverfahren` | Eintragungsreifer Antrag, Formalprüfung des Grundbuchamts und Rechtsbehelfe — mit der MoPeG-Falle der nicht registrierten GbR | §§ 13, 18, 19, 20, 22, 29, 39, 40, 47 Abs. 2, 53, 71, 75 GBO; §§ 874, 879–881, 892, 899 BGB; § 707 BGB |
| `grundschuld-sicherungsrecht` | Bestellung, Sicherungsabrede, Vollstreckungsunterwerfung, Abtretung und Rückgewähr der Grundschuld | §§ 1191, 1192 (Abs. 1a), 1154, 1157, 1168, 1113, 1116 BGB; §§ 726, 727, 732, 767, 794 Abs. 1 Nr. 5, 797, 800 ZPO; §§ 305c, 307 BGB |
| `wohnungseigentum-teilungserklaerung` | Begründung von Wohnungseigentum, Zuordnung von Sonder- und Gemeinschaftseigentum, Sondernutzungsrechte, Gemeinschaftsordnung und ihre Änderung | §§ 1, 3, 5, 7, 8, 10, 16, 20 WEG (WEMoG); §§ 13, 19, 29 GBO |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: BGB-Sachenrecht, GBO, BeurkG, WEG, ZPO-Vollstreckungsrecht, BGH V. und XI. Zivilsenat, OLG als Grundbuchbeschwerdegerichte, Standardkommentare
- [`agents/drafter.md`](./agents/drafter.md) – Erstellung in Gutachten-, Urteils- oder Urkundenstil; Vertragsentwürfe, Teilungserklärungen, Grundbuchanträge, Beschwerdeschriften
- [`agents/reviewer.md`](./agents/reviewer.md) – Vollzugs-, Frist- und Berufsrechts-Check (Form § 29 GBO, Voreintragung, eGbR-Sperre, Fälligkeitskaskade, Zwischenverfügungsfristen)

## Installation

### Claude Code
```bash
# Über Marketplace (empfohlen)
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install immobilien-grundbuchrecht

# Oder als ZIP
# Claude Code → Customize Plugins → Install from .zip → immobilien-grundbuchrecht.zip
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area immobilien-grundbuchrecht --out dist/gemini
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area immobilien-grundbuchrecht --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Käuferprüfung eines Notarentwurfs

```
/immobilien-grundbuchrecht:grundstueckskaufvertrag
Mandanten kaufen ein Reihenhaus für 450.000 EUR. Der Entwurf kam erst
am Vortag der Beurkundung. Küche und eine zugesagte Dachsanierung sind
nur per E-Mail vereinbart. Bitte Prüfung von Beurkundungsvollständigkeit,
Fälligkeitskaskade, Vormerkungsschutz und Reichweite der Klausel
"gekauft wie besichtigt".
```

### Szenario 2 – Grundbuchvollzug mit GbR

```
/immobilien-grundbuchrecht:grundbuchverfahren
Eine 2011 gegründete Grundstücks-GbR will verkaufen; sie ist nicht im
Gesellschaftsregister eingetragen. Ein Gesellschafter ist verstorben.
Das Grundbuchamt hat eine Zwischenverfügung erlassen. Bitte
Vollzugsplan, § 47 Abs. 2 GBO, Voreintragung, Fristenkalender.
```

### Szenario 3 – Verteidigung gegen Grundschuldvollstreckung

```
/immobilien-grundbuchrecht:grundschuld-sicherungsrecht
Eltern haben eine Grundschuld über 180.000 EUR für das Darlehen ihres
Sohnes bestellt, mit weitem Sicherungszweck und persönlicher
Schuldübernahme. Die Bank hat abgetreten; die Erwerberin vollstreckt,
obwohl zwei Drittel getilgt sind. Bitte Verteidigungslinien
(§ 1192 Abs. 1a BGB, §§ 732, 767, 797 Abs. 4 ZPO) und Rückgewähr.
```

### Szenario 4 – Teilungserklärung prüfen

```
/immobilien-grundbuchrecht:wohnungseigentum-teilungserklaerung
Bauträgeraufteilung nach § 8 WEG. Fenster und Dachterrasse sollen
Sondereigentum sein, Gartenflächen nur im Kaufvertrag zugewiesen,
keine Öffnungsklausel, zwei Kellerräume weichen vom Aufteilungsplan ab.
Was gehört den Erwerbern tatsächlich, und was ist zu korrigieren?
```

## Deterministische Rechner

Die Skills binden `scripts/legal_calc/` ein: Fristen (§§ 187–193 BGB) für Zwischenverfügungen und die Zwei-Wochen-Frist des § 17 Abs. 2a BeurkG, Verzugszinsen (§§ 288, 247 BGB) auf gesicherte Forderungen, RVG/GKG dort, wo ein Geschäftswert die Gebühren treibt. Der Rechner macht **nur die Arithmetik**; Zugang, Zustellung und Fristbeginn bleiben juristische Eingaben. Ein **GNotKG-Modul ist nicht implementiert** — Notar- und Grundbuchkosten sind gegen KV GNotKG von Hand zu ermitteln. Details: [`../references/rechner.md`](../references/rechner.md).

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Standardkommentare: **Demharter** GBO, **Schöner/Stöber** Grundbuchrecht, **Bauer/Schaub** GBO, **Winkler** BeurkG, **Bärmann** / **Hügel/Elzer** / **Jennißen** WEG, **Clemente** Recht der Sicherungsgrundschuld, **Grüneberg** und **MüKoBGB** für das materielle Recht.

Rechtsprechung: BGH V. Zivilsenat (Grundstücks- und WEG-Recht), XI. Zivilsenat (Kreditsicherheiten), OLG als Grundbuchbeschwerdegerichte. Format: `BGH, Urt. v. TT.MM.JJJJ – V ZR NN/JJ, NJW Jahr, Seite Rn. N`. Verifikation über dejure.org; unverifizierte Zitate tragen `[unverifiziert - prüfen]`.

## Hinweise

- **MoPeG seit 01.01.2024.** § 47 Abs. 2 GBO sperrt jede Grundbucheintragung für eine GbR, die nicht im Gesellschaftsregister eingetragen ist. Das ist die häufigste Ursache geplatzter Beurkundungstermine — vor Terminierung klären.
- **Kein Kaufpreis ohne Vormerkung.** Die Auflassungsvormerkung (§ 883 BGB) ist der einzige wirksame Schutz des Käufers gegen Zwischenverfügungen und die Insolvenz des Verkäufers.
- **Die Grundschuld ist nicht akzessorisch.** Tilgung des Darlehens beendet die Grundschuld nicht; der Rückgewähranspruch ist gesondert geltend zu machen und wirtschaftlich meist als Abtretung, nicht als Löschung.
- **Zwingendes Gemeinschaftseigentum** (§ 5 Abs. 2 WEG) lässt sich nicht durch Teilungserklärung zum Sondereigentum machen — die Zuweisung ist unwirksam, die daran hängende Kostenregelung läuft leer.
- **Notarielle Unparteilichkeit.** Der Notar berät keine Seite (§ 17 BeurkG, § 14 BNotO). Die Interessenwahrnehmung für Käufer oder Verkäufer ist Anwaltsaufgabe; dieses Plugin ersetzt weder Beurkundung noch Belehrung.
- **Mandantengeheimnis (§ 43a BRAO, § 203 StGB):** Keine echten Grundbuchauszüge, Kaufpreise oder Beteiligtennamen ohne § 203-konformen Gateway.
- **Steuern.** Grunderwerbsteuer, Spekulationsfrist § 23 EStG und die steuerliche Behandlung mitverkauften Inventars sind nicht Gegenstand dieses Plugins; hierzu ist steuerliche Beratung einzuholen (Querverweis: [`steuerrecht`](../steuerrecht/)).
