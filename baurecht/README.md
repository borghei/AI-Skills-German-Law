# Baurecht

**Production-grade Baurechts-Skills für Claude / Gemini / GPT.** Deutsches Baurecht in beiden Säulen: privates Baurecht (BGB-Werkvertrag, Bauvertragsrecht 2018, VOB/B, HOAI, Architektenrecht) und öffentliches Baurecht (BauGB, BauNVO, Landes-BauO). Researcher → Drafter → Reviewer.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `vob-werkvertrag-mangelpruefung` | Mängelrechte nach Abnahme klären, Vertragsregime einordnen (BGB vs. VOB/B) | §§ 631 ff., 633, 634, 634a, 640, 641 BGB; §§ 650a–u BGB; § 13 VOB/B; §§ 305 ff. BGB |
| `baugenehmigungsverfahren` | Materielle Zulässigkeit + Verfahren von der Bauvoranfrage bis zur Anfechtungs-/Verpflichtungsklage | §§ 29–35, 36 BauGB; BauNVO; LBO; §§ 42, 75 VwGO |
| `nachbarrechtlicher-baustreit` | Drittschutz gegen Baugenehmigung + zivilrechtliche Abwehr | § 1004 iVm § 906 BGB; § 80a VwGO; § 212a BauGB; Rücksichtnahmegebot |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: BGB/VOB/B/BauGB/BauNVO/LBO, BGH VII. ZS, BVerwG 4. Senat, Werner/Pastor, Kniffka/Koeble, Ingenstau/Korbion, Battis/Krautzberger/Löhr, Ernst/Zinkahn/Bielenberg
- [`agents/drafter.md`](./agents/drafter.md) – Erstellung im Gutachten- oder Urteilsstil, Mängelschreiben, Bauantrag-Vorprüfung, Schriftsatz zur Drittanfechtung
- [`agents/reviewer.md`](./agents/reviewer.md) – Frist-Kalender (§ 634a BGB, § 74 VwGO, § 80 III VwGO, § 212a BauGB), VOB/B-„im Ganzen"-Falle, drittschützende Norm

## Installation

### Claude Code
```bash
# Über Marketplace (empfohlen)
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install baurecht

# Oder als ZIP
# Claude Code → Customize Plugins → Install from .zip → baurecht.zip
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area baurecht --out dist/gemini
# Inhalt der erzeugten Dateien in neue Gemini-Gems einfügen
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area baurecht --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Mängel an Einfamilienhaus, Vertragsregime unklar

```
/baurecht:vob-werkvertrag-mangelpruefung
Privater Bauherr hat Generalunternehmer mit Errichtung eines Einfamilienhauses
beauftragt. Vertrag verweist auf die VOB/B, ist aber individuell zwischen
mehreren Klauseln verhandelt. Nach Abnahme treten Risse im Estrich auf. GU
verweigert Nacherfüllung. Bitte prüfen, ob VOB/B „im Ganzen" einbezogen ist
(sonst AGB-Kontrolle §§ 305 ff. BGB) und welche Mängelrechte nach § 634 BGB
in welcher Reihenfolge geltend zu machen sind. Verjährung nach § 634a I Nr. 2
BGB bitte ausrechnen.
```

### Szenario 2 – Baugenehmigung für Erweiterung im Innenbereich

```
/baurecht:baugenehmigungsverfahren
Mandantin will Bestandsgebäude in faktischem Mischgebiet (§ 34 II BauGB
iVm § 6 BauNVO) um Gewerbeeinheit erweitern. Gemeinde verweigert ihr
Einvernehmen nach § 36 BauGB. Bitte materielle Zulässigkeit (§ 34 BauGB,
Einfügen, Maß, Stellplätze nach Landes-BauO), Verfahrensart (vereinfachtes
Verfahren?), und Rechtsbehelfsstrategie (Verpflichtungsklage, ggf. § 75
VwGO Untätigkeit) prüfen.
```

### Szenario 3 – Nachbar wehrt sich gegen Baugenehmigung

```
/baurecht:nachbarrechtlicher-baustreit
Mandant wohnt direkt neben Grundstück, auf dem nach Baugenehmigung eine
fünfgeschossige Wohnanlage entstehen soll. Abstandsflächen der Landes-BauO
nach Mandanteneinschätzung unterschritten, Verschattung erheblich. Bitte
Drittanfechtung der Baugenehmigung (drittschützende Normen, Rücksichtnahme-
gebot), Eilrechtsschutz § 80 V iVm § 80a VwGO trotz § 212a BauGB
(Sofortvollzug kraft Gesetzes) und zivilrechtliche Flanke (§ 1004 iVm § 906
BGB, Landes-Nachbarrechtsgesetz) prüfen.
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Standardkommentare: **Werner/Pastor**, Der Bauprozess; **Kniffka/Koeble**, Kompendium des Baurechts; **Ingenstau/Korbion**, VOB Teile A und B; **Messerschmidt/Voit**, Privates Baurecht; **Battis/Krautzberger/Löhr**, BauGB; **Ernst/Zinkahn/Bielenberg/Krautzberger**, BauGB (Loseblatt); **Jäde/Dirnberger**, BauGB/BauNVO; Landes-BauO-Kommentare (Simon/Busse BayBO; Boeddinghaus/Hahn/Schulte BauO NRW).

Rechtsprechung: BGH VII. Zivilsenat (Bauvertrag), BVerwG 4. Senat (Bauplanungs- und Bauordnungsrecht), OVG der Länder; im Format `BGH, Urt. v. TT.MM.JJJJ – VII ZR NNN/JJ, BGHZ Bd, S.`. Unverifizierte Zitate werden mit `[unverifiziert – prüfen in juris/BeckOnline]` markiert.

## Hinweise

- **VOB/B-Privilegierung nur „im Ganzen".** Ist die VOB/B gegenüber einer Privatperson (Verbraucher) oder mit Abweichungen einbezogen, unterliegt sie der AGB-Inhaltskontrolle nach §§ 305 ff. BGB (st. Rspr. BGH). Falsche Klassifizierung ist Reviewer-Blocker.
- **Sofortvollzug der Baugenehmigung kraft Gesetzes** (§ 212a BauGB). Widerspruch / Anfechtungsklage haben **keine** aufschiebende Wirkung; Drittschutz nur über § 80 V iVm § 80a VwGO.
- **1-Monats-Klagefrist** für Anfechtungs-/Verpflichtungsklage (§ 74 VwGO) ab Bekanntgabe (Nachbarn: § 58 VwGO bei fehlender Rechtsbehelfsbelehrung Jahresfrist).
- **Verjährung der Mängelansprüche am Bauwerk: 5 Jahre** ab Abnahme (§ 634a I Nr. 2 BGB), bei Architekten/Ingenieuren parallel; arglistige Verschweigung: §§ 195, 199 BGB.
- **Drittschützende Norm** ist Voraussetzung der Nachbarklage. Abstandsflächen der LBO sind regelmäßig drittschützend; das bauplanungsrechtliche Rücksichtnahmegebot in §§ 34, 35 BauGB iVm § 15 BauNVO ist drittschützend, wenn der Nachbar individualisiert betroffen ist.
- **Mandatsgeheimnis (§ 43a BRAO, § 203 StGB):** Keine echten Mandatsdaten ohne § 203-konformen Gateway.
