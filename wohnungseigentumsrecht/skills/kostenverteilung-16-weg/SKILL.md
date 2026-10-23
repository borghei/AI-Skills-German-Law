---
name: kostenverteilung-16-weg
description: "Änderung des Kostenverteilungsschlüssels im Wohnungseigentum durch Beschluss – gesetzlicher Schlüssel nach Miteigentumsanteilen § 16 Abs. 2 S. 1 WEG, Beschlusskompetenz für einzelne Kosten oder bestimmte Arten von Kosten auch abweichend von einer Vereinbarung § 16 Abs. 2 S. 2 WEG, erstmalige Belastung und vollständige Befreiung einzelner Eigentümer, Änderung für eine einzelne Erhaltungsmaßnahme, Grenzen der ordnungsmäßigen Verwaltung bei objektbezogener Kostentrennung und beim Wechsel zum Objektprinzip bei unterschiedlich großen Einheiten, Bindung der Folgebeschlüsse, Abgrenzung zu § 21 WEG und zum Anpassungsanspruch § 10 Abs. 2 WEG, Wirkung gegenüber Sondernachfolgern § 10 Abs. 3, § 48 Abs. 1 WEG. Rechtsstand: Oktober 2026. Use when eine Gemeinschaft den Verteilerschlüssel für Erhaltungs-, Betriebs- oder Verwaltungskosten ändern will oder ein Eigentümer einen Kostenverteilungsbeschluss angreifen möchte."
language: de
agents:
  researcher: ../../agents/researcher.md
  drafter: ../../agents/drafter.md
  reviewer: ../../agents/reviewer.md
provider_variants:
  - claude
  - gemini
  - openai
test: ./test.md
---

# /wohnungseigentumsrecht:kostenverteilung-16-weg

## Zweck

Das WEMoG hat der Mehrheit eine weitreichende Kompetenz gegeben: Die Eigentümer können **für einzelne Kosten oder bestimmte Arten von Kosten** eine vom Gesetz **oder von einer Vereinbarung** abweichende Verteilung **beschließen** ([§ 16 Abs. 2 S. 2 WEG](https://www.gesetze-im-internet.de/woeigg/__16.html)). Der BGH hat 2024–2026 geklärt, wie weit diese Kompetenz reicht und wo die ordnungsmäßige Verwaltung sie begrenzt. Dieser Skill prüft, ob ein Kostenverteilungsbeschluss **von der Kompetenz gedeckt** ist (sonst nichtig) und ob er **ordnungsmäßiger Verwaltung** entspricht (sonst anfechtbar), und formuliert anfechtungsfeste Beschlüsse.

**Rechtsstand: Oktober 2026.** § 16 WEG ist seit dem WEMoG unverändert. Seit **01.01.2026** wirken Altbeschlüsse, die auf einer **Öffnungsklausel** beruhen, gegen Sondernachfolger nur noch nach Eintragung im Grundbuch; die Übergangsfrist des § 48 Abs. 1 S. 2 WEG ist am 31.12.2025 abgelaufen.

## Eingaben

- geltender Schlüssel: Gesetz (Miteigentumsanteile), Gemeinschaftsordnung (Wohnfläche, Einheiten, Untergemeinschaften, objektbezogene Kostentrennung), frühere Änderungsbeschlüsse
- Wortlaut des beabsichtigten oder gefassten Beschlusses
- betroffene Kostenart (Erhaltung eines Bauteils, Betriebskosten, Verwaltervergütung, Aufzug, Tiefgarage)
- Größe der Einheiten, Miteigentumsanteile, Nutzungsmöglichkeiten (wer profitiert?)
- finanzielle Auswirkung je Einheit (Mehr- oder Minderbelastung in Prozent)
- Datum der Beschlussfassung (Frist § 45 WEG)

## Sub-Agent-Architektur

- **Researcher** liefert § 16 WEG, §§ 10, 21, 48 WEG und die Leitentscheidungen des V. Zivilsenats zu § 16 Abs. 2 S. 2 WEG.
- **Drafter** rechnet die Belastungsverschiebung je Einheit aus und formuliert den Beschluss (Kostenart, Schlüssel, Geltungsbeginn, Begründung des sachlichen Grundes).
- **Reviewer** trennt Kompetenzfrage und Ermessensfrage und prüft die Folgebeschlüsse.

## Ablauf

### 1. Ausgangsschlüssel bestimmen

- **Gesetz:** Kosten nach dem Verhältnis der **Miteigentumsanteile** laut Grundbuch ([§ 16 Abs. 2 S. 1, Abs. 1 S. 2 WEG](https://www.gesetze-im-internet.de/woeigg/__16.html)).
- **Vereinbarung:** abweichender Schlüssel der Gemeinschaftsordnung (z. B. Wohnfläche, Einheiten, getrennte Kostenkreise für Gebäudeteile).
- **Bauliche Veränderungen:** nicht § 16, sondern § 21 WEG (§ 16 Abs. 3 WEG); dazu `/wohnungseigentumsrecht:bauliche-veraenderung`.

### 2. Beschlusskompetenz (§ 16 Abs. 2 S. 2 WEG)

- Gegenstand: **einzelne Kosten** oder **bestimmte Arten von Kosten**. Ein Beschluss, der den Schlüssel für **sämtliche** Kosten der Gemeinschaft umstellt, ist von der Kompetenz nicht gedeckt `[unverifiziert – prüfen: Grenzziehung im Volltext der Senatsrechtsprechung]`.
- Die Kompetenz umfasst auch, einzelne Eigentümer **erstmals zu belasten** oder **vollständig zu befreien** (BGH, Urt. v. 22.03.2024 – V ZR 81/23, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-03-22&Aktenzeichen=V%20ZR%2081/23)).
- Eine Änderung für eine **einzelne Erhaltungsmaßnahme** ist zulässig; es muss nicht zugleich eine Regelung für alle künftigen gleich gelagerten Fälle beschlossen werden (BGH, Urt. v. 22.03.2024 – V ZR 87/23, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-03-22&Aktenzeichen=V%20ZR%2087/23)).
- Fehlt die Kompetenz, ist der Beschluss **nichtig** ([§ 23 Abs. 4 S. 1 WEG](https://www.gesetze-im-internet.de/woeigg/__23.html)).

### 3. Ordnungsmäßige Verwaltung — die eigentliche Hürde

Die Eigentümer haben ein **weites Ermessen**, dürfen aber nicht willkürlich verteilen. Maßstäbe aus der Rechtsprechung:

| Konstellation | Maßstab | Entscheidung |
|---|---|---|
| Kosten auf die Eigentümer verlagern, die den **größten Nutzen** haben | in der Regel ordnungsmäßig | BGH V ZR 81/23, V ZR 87/23 ([V ZR 81/23](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-03-22&Aktenzeichen=V%20ZR%2081/23), [V ZR 87/23](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-03-22&Aktenzeichen=V%20ZR%2087/23)) |
| Gemeinschaftsordnung sieht **objektbezogene Kostentrennung** vor (z. B. Tiefgarage nur für Stellplatzeigentümer) und alle Eigentümer sollen beteiligt werden | widerspricht in der Regel ordnungsmäßiger Verwaltung, außer bei **sachlichem Grund** | BGH, Urt. v. 14.02.2025 – V ZR 236/23, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-02-14&Aktenzeichen=V%20ZR%20236/23) |
| Wechsel von Wohnfläche/MEA zum **Objektprinzip** (gleiche Kosten je Einheit) für Erhaltungskosten bei **unterschiedlich großen** Einheiten | widerspricht in der Regel ordnungsmäßiger Verwaltung; schon eine Mehrbelastung der kleineren Einheiten von rund **5 %** kann genügen | BGH, Urt. v. 24.04.2026 – V ZR 50/25, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-04-24&Aktenzeichen=V%20ZR%2050/25) |

Die 5-%-Schwelle stammt aus der Berichterstattung über V ZR 50/25 `[unverifiziert – prüfen: Wortlaut der Gründe]`. Für die Praxis: **Belastungsverschiebung je Einheit in Prozent ausrechnen** und im Beschluss den sachlichen Grund (Nutzen, Verursachung, Gebrauchsmöglichkeit) benennen.

### 4. Folgebeschlüsse und Bestandskraft

- Ein **wirksam geänderter** Schlüssel ist in Wirtschaftsplan, Jahresabrechnung und Sonderumlage **anzuwenden**; die Anfechtung der Folgebeschlüsse mit dem Argument, der Schlüssel sei unbillig, scheitert (BGH, Urt. v. 15.11.2024 – V ZR 239/23, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-11-15&Aktenzeichen=V%20ZR%20239/23)).
- Konsequenz: Der Änderungsbeschluss selbst ist **binnen eines Monats** anzufechten ([§ 45 WEG](https://www.gesetze-im-internet.de/woeigg/__45.html)). Wer erst die nächste Jahresabrechnung angreift, ist zu spät.

### 5. Wirkung gegenüber Sondernachfolgern

- Beschlüsse auf **gesetzlicher** Grundlage (§ 16 Abs. 2 S. 2 WEG) wirken ohne Grundbucheintragung gegen Sondernachfolger; sie sind in die Beschluss-Sammlung einzutragen ([§ 24 Abs. 7 WEG](https://www.gesetze-im-internet.de/woeigg/__24.html)).
- Beschlüsse aufgrund einer **Öffnungsklausel** wirken gegen Sondernachfolger nur bei Eintragung als Inhalt des Sondereigentums ([§ 10 Abs. 3 WEG](https://www.gesetze-im-internet.de/woeigg/__10.html)). Für Altbeschlüsse galt bis 31.12.2025 die Übergangsregel des [§ 48 Abs. 1 S. 2 WEG](https://www.gesetze-im-internet.de/woeigg/__48.html); seit 01.01.2026 nicht mehr.

### 6. Anspruch auf Änderung (§ 10 Abs. 2 WEG, § 18 Abs. 2 WEG)

- Ein Eigentümer kann eine **Änderung der Vereinbarung** verlangen, wenn das Festhalten aus **schwerwiegenden Gründen** unbillig erscheint ([§ 10 Abs. 2 WEG](https://www.gesetze-im-internet.de/woeigg/__10.html)).
- Daneben kann er einen **Kostenverteilungsbeschluss** nach § 16 Abs. 2 S. 2 WEG verlangen, wenn nur dieser ordnungsmäßiger Verwaltung entspricht; durchsetzbar mit der Beschlussersetzungsklage (`/wohnungseigentumsrecht:beschlussersetzungsklage`).

### 7. Ergebnis

Kompetenz (ja/nein → nichtig), Ermessen (sachlicher Grund, Belastungsverschiebung), Folgebeschlüsse, Sondernachfolger, Handlungsempfehlung (Beschlussvorschlag oder Anfechtung).

## Quellen und Zitierweise

Verbindlich: [`../../references/zitierweise.md`](../../references/zitierweise.md).

### Statute

- [§ 16 WEG](https://www.gesetze-im-internet.de/woeigg/__16.html) (Nutzungen und Kosten), [§ 21 WEG](https://www.gesetze-im-internet.de/woeigg/__21.html) (bauliche Veränderungen)
- [§ 10 WEG](https://www.gesetze-im-internet.de/woeigg/__10.html) (Anpassungsanspruch, Sondernachfolger), [§ 48 WEG](https://www.gesetze-im-internet.de/woeigg/__48.html) (Übergang)
- [§ 23 WEG](https://www.gesetze-im-internet.de/woeigg/__23.html), [§ 45 WEG](https://www.gesetze-im-internet.de/woeigg/__45.html)

### Rechtsprechung (V. Zivilsenat)

1. BGH, Urt. v. 24.04.2026 – V ZR 50/25 (Objektprinzip bei unterschiedlich großen Einheiten), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-04-24&Aktenzeichen=V%20ZR%2050/25)
2. BGH, Urt. v. 14.02.2025 – V ZR 236/23 (objektbezogene Kostentrennung; sachlicher Grund), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-02-14&Aktenzeichen=V%20ZR%20236/23)
3. BGH, Urt. v. 14.02.2025 – V ZR 128/23 (Ordnungsmäßigkeit einer Änderung der Kostenverteilung) `[unverifiziert – prüfen: Leitsatz im Volltext]`
4. BGH, Urt. v. 15.11.2024 – V ZR 239/23 (geänderter Schlüssel in Folgebeschlüssen), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-11-15&Aktenzeichen=V%20ZR%20239/23)
5. BGH, Urt. v. 22.03.2024 – V ZR 87/23 (Änderung für einzelne Erhaltungsmaßnahme), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-03-22&Aktenzeichen=V%20ZR%2087/23)
6. BGH, Urt. v. 22.03.2024 – V ZR 81/23 (erstmalige Belastung und Befreiung), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-03-22&Aktenzeichen=V%20ZR%2081/23)

### Kommentare

- Bärmann/Becker, WEG, aktuelle Aufl., § 16 `[unverifiziert – prüfen: Auflage und Rn.]`
- Hügel/Elzer, WEG, aktuelle Aufl., § 16 `[unverifiziert – prüfen: Auflage und Rn.]`

## Beispiel (Gutachtenstil, verkürzt)

**Sachverhalt.** 12 Einheiten zwischen 38 und 120 m²; die Gemeinschaftsordnung verteilt Erhaltungskosten nach Wohnfläche. Die Mehrheit beschließt am 10.06.2026, die Kosten der anstehenden Dachsanierung (240.000 EUR) „gerecht nach Einheiten" zu verteilen. Eigentümer K (38 m², Gesamtfläche 900 m²) zahlt danach 20.000 EUR statt 10.133 EUR.

**Kompetenz.** Die Dachsanierung ist eine einzelne Erhaltungsmaßnahme; der Beschluss ist von § 16 Abs. 2 S. 2 WEG gedeckt (V ZR 87/23) und daher nicht nichtig. ([V ZR 87/23](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-03-22&Aktenzeichen=V%20ZR%2087/23))

**Ermessen.** Die Einheiten sind sehr unterschiedlich groß; die Belastung des K steigt um 97 %. Der Wechsel zum Objektprinzip widerspricht bei solchen Größenunterschieden in der Regel ordnungsmäßiger Verwaltung (V ZR 50/25). Ein sachlicher Grund, etwa ein höherer Nutzen der kleinen Einheiten, ist nicht ersichtlich. ([V ZR 50/25](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-04-24&Aktenzeichen=V%20ZR%2050/25))

**Ergebnis.** Anfechtungsklage gegen die GdWE bis 10.07.2026 (Monatsfrist), Begründung bis 10.08.2026; Folgebeschlüsse (Sonderumlage) vorsorglich mit anfechten.

## Risiken / typische Fehler

- **Kompetenz und Ermessen vermischt** → fehlende Kompetenz macht nichtig, Ermessensfehler nur anfechtbar.
- **Erstmalige Belastung für unzulässig gehalten** → seit BGH V ZR 81/23 von der Kompetenz gedeckt; die Prüfung verlagert sich ins Ermessen. ([V ZR 81/23](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-03-22&Aktenzeichen=V%20ZR%2081/23))
- **Objektprinzip bei ungleichen Einheiten** → regelmäßig nicht ordnungsmäßig (BGH V ZR 50/25); Belastungsverschiebung in Prozent ausrechnen. ([V ZR 50/25](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-04-24&Aktenzeichen=V%20ZR%2050/25))
- **Objektbezogene Kostentrennung ohne sachlichen Grund aufgehoben** → anfechtbar (BGH V ZR 236/23). ([V ZR 236/23](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-02-14&Aktenzeichen=V%20ZR%20236/23))
- **Nur die Jahresabrechnung angegriffen** → nach bestandskräftiger Schlüsseländerung zu spät (BGH V ZR 239/23). ([V ZR 239/23](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-11-15&Aktenzeichen=V%20ZR%20239/23))
- **§ 16 statt § 21 WEG angewandt** → Kosten baulicher Veränderungen folgen § 21 WEG (§ 16 Abs. 3 WEG).
- **Öffnungsklausel-Altbeschluss gegenüber Erwerber angewandt** → seit 01.01.2026 nur bei Grundbucheintragung (§ 10 Abs. 3, § 48 Abs. 1 WEG).

## Ausgabeformat

```
KOSTENVERTEILUNG § 16 WEG — PRÜFUNG (Rechtsstand Oktober 2026)

1. Ausgangsschlüssel: [Gesetz/MEA] [GO: …] [früherer Beschluss Nr. …]
2. Beschluss: Kostenart <…> | neuer Schlüssel <…> | ab <…>
3. Kompetenz (§ 16 Abs. 2 S. 2 WEG):
   - einzelne Kosten / bestimmte Kostenart? <ja/nein>  → sonst nichtig
4. Ermessen (ordnungsmäßige Verwaltung):
   | Einheit | m² / MEA | alt EUR | neu EUR | Δ % |
   - sachlicher Grund: <Nutzen / Verursachung / keiner>
   - objektbezogene Kostentrennung berührt? <…>
5. Folgebeschlüsse (Wirtschaftsplan, Sonderumlage): <…>
6. Sondernachfolger (§ 10 Abs. 3, § 48 Abs. 1 WEG): <…>
7. Ergebnis: <Beschlussvorschlag / Anfechtung bis …>
```
