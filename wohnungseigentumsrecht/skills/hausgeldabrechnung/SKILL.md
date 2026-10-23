---
name: hausgeldabrechnung
description: "Prüfung von Wirtschaftsplan, Jahresabrechnung und Nachschussbeschluss im Wohnungseigentumsrecht nach der WEMoG-Reform – Vorschüsse und Wirtschaftsplan § 28 Abs. 1 WEG, Nachschüsse und Abrechnungsspitze § 28 Abs. 2 WEG (Auslegung eines Beschlusses über die „Jahresabrechnung" als Beschluss über die Abrechnungsspitzen; Anfechtbarkeit nur bei Fehlern mit Auswirkung auf die Spitze), Vermögensbericht § 28 Abs. 4 WEG, Verteilung nach Miteigentumsanteilen § 16 Abs. 2 WEG, Fälligkeit § 28 Abs. 3 WEG, kein Zurückbehaltungsrecht gegenüber Vorschüssen, Entziehung § 17 WEG als ultima ratio. Rechtsstand: Oktober 2026. Use when eine WEG-Jahresabrechnung oder ein Hausgeld-/Nachschussbeschluss auf Plausibilität, Beschlusskompetenz und Anfechtungsaussicht geprüft wird."
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

# /wohnungseigentumsrecht:hausgeldabrechnung

## Zweck

Prüfung einer WEG-Jahresabrechnung auf drei Ebenen: **Beschlussgegenstand** (worüber wurde beschlossen?), **Anfechtungsrelevanz** (welche Fehler schlagen auf den Beschluss durch?) und **Plausibilität** (rechnen die Zahlen, stimmt der Verteilungsschlüssel).

Seit der **WEMoG**-Reform (in Kraft seit 01.12.2020) beschließen die Eigentümer nach [§ 28 Abs. 2 WEG](https://www.gesetze-im-internet.de/woeigg/__28.html) nicht mehr über „die Jahresabrechnung", sondern über die **Einforderung von Nachschüssen oder die Anpassung der beschlossenen Vorschüsse** — die **Abrechnungsspitze**. Die Jahresabrechnung ist nur noch Berechnungsgrundlage. Der BGH zieht daraus zwei praxisentscheidende Folgerungen: Ein Beschluss über die „Genehmigung der Jahresabrechnung" ist **nicht kompetenzwidrig**, sondern im Zweifel als Beschluss über die Abrechnungsspitzen auszulegen; und anfechtbar macht ihn nur ein Fehler, der sich **auf die Abrechnungsspitze auswirkt**.

**Rechtsstand: Oktober 2026.** § 28 WEG ist seit dem WEMoG unverändert. Die Rechtsprechung des V. Zivilsenats 2024–2026 hat die Lesart des § 28 WEG weitgehend geklärt (Nachweise unten).

## Eingaben

- **Wirtschaftsplan** des Abrechnungsjahres und der Beschluss über die Vorschüsse
- **Jahresabrechnung** (Gesamtabrechnung) und **Einzelabrechnung** des Eigentümers
- der gefasste Beschluss im **Wortlaut** (Beschluss-Sammlung, Protokoll)
- **Verteilungsschlüssel** laut Gemeinschaftsordnung und etwaige Änderungsbeschlüsse nach § 16 Abs. 2 S. 2 WEG
- **Vermögensbericht** des Verwalters
- Datum der Beschlussfassung (für die Anfechtungsfrist des § 45 WEG)

## Sub-Agent-Architektur

- **Researcher** liefert §§ 16, 17, 28 WEG in der post-WEMoG-Fassung und die verifizierte Rechtsprechung des V. Zivilsenats zu § 28 WEG.
- **Drafter** erstellt die Prüfung und ggf. die Anfechtungsbegründung, beschränkt auf die angreifbaren Positionen.
- **Reviewer** prüft Beschlussauslegung, Auswirkung jedes gerügten Fehlers auf die Spitze, Verteilungsschlüssel und Frist.

## Ablauf

### 1. Wirtschaftsplan und Vorschüsse (§ 28 Abs. 1 WEG)

Die Wohnungseigentümer beschließen über die **Vorschüsse** zur Kostentragung und zu den Rücklagen; der Verwalter stellt dazu für jedes Kalenderjahr einen **Wirtschaftsplan** auf ([§ 28 Abs. 1 WEG](https://www.gesetze-im-internet.de/woeigg/__28.html)). Die Festsetzung der Vorschüsse gehört zur ordnungsmäßigen Verwaltung ([§ 19 Abs. 2 Nr. 5 WEG](https://www.gesetze-im-internet.de/woeigg/__19.html)).

- Die Eigentümer haben bei der Höhe der Vorschüsse einen **weiten Ermessensspielraum**; anfechtbar ist der Beschluss erst, wenn die Ansätze offensichtlich unangemessen sind (BGH, Urt. v. 26.09.2025 – V ZR 108/24, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-09-26&Aktenzeichen=V%20ZR%20108/24)).
- **Zweitbeschlüsse** über Vorschüsse sind zulässig, auch nach Ablauf des Wirtschaftsjahres (BGH, Urt. v. 20.09.2024 – V ZR 235/23, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-09-20&Aktenzeichen=V%20ZR%20235/23)).
- Der beschlossene Wirtschaftsplan ist der Maßstab, an dem die spätere Abrechnungsspitze gemessen wird.

### 2. Beschlussgegenstand: die Abrechnungsspitze (§ 28 Abs. 2 WEG)

Nach Ablauf des Kalenderjahres beschließen die Eigentümer über die **Einforderung von Nachschüssen** oder die **Anpassung der beschlossenen Vorschüsse**; Grundlage ist die vom Verwalter aufgestellte Jahresabrechnung ([§ 28 Abs. 2 WEG](https://www.gesetze-im-internet.de/woeigg/__28.html)).

```
Abrechnungsspitze = auf den Eigentümer entfallende Kosten laut Einzelabrechnung
                    − beschlossene Vorschüsse (Soll laut Wirtschaftsplan)
   positive Spitze → Nachschuss
   negative Spitze → Anpassung der Vorschüsse (Guthaben)
```

**Auslegung des Beschlusswortlauts.** Ein nach dem 30.11.2020 gefasster Beschluss, durch den „die Gesamtabrechnung und die daraus resultierenden Einzelabrechnungen" **genehmigt** werden, ist nächstliegend dahin auszulegen, dass die Eigentümer nur die Höhe der Nachschüsse bzw. die Anpassung der Vorschüsse festlegen wollen (BGH, Urt. v. 19.07.2024 – V ZR 102/23, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-07-19&Aktenzeichen=V%20ZR%20102/23)). Ein solcher Beschluss ist also **weder nichtig noch wegen fehlender Beschlusskompetenz anfechtbar**. Wer nur den Wortlaut „Jahresabrechnung" rügt, verliert.

**Verwalterwechsel.** Zur Erstellung der Jahresabrechnung ist die **GdWE** verpflichtet; der jeweils **amtierende** Verwalter erstellt sie als ihr Organ, auch für Rückstände aus Vorjahren. Die Pflicht entsteht am **1. Januar des Folgejahres**. Ein Verwalter, der zum 31.12. oder im Laufe des Jahres ausscheidet, schuldet die Jahresabrechnung für das bei seinem Ausscheiden laufende Jahr daher **nicht**; er schuldet sie nur, wenn der Verwaltervertrag es bestimmt und die Pflicht der GdWE noch in seiner Amtszeit entstanden ist. Er hat aber Rechnung zu legen und die Unterlagen herauszugeben (BGH, Urt. v. 26.09.2025 – V ZR 206/24, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-09-26&Aktenzeichen=V%20ZR%20206/24)).

### 3. Anfechtungsrelevanz: nur Fehler mit Auswirkung auf die Spitze

- Anfechtbar ist der Nachschussbeschluss nur wegen Fehlern, die sich **auf die Abrechnungsspitze auswirken** (BGH, Urt. v. 20.09.2024 – V ZR 195/23, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-09-20&Aktenzeichen=V%20ZR%20195/23)). Fehler in Positionen, die die Spitze nicht verändern (z. B. bloße Darstellungsmängel der Gesamtabrechnung), tragen die Anfechtung nicht.
- **Teilanfechtung / Teilungültigerklärung:** Ist eine fehlerhafte Position abtrennbar und hätten die Eigentümer den Beschluss im Übrigen auch so gefasst, wird der Beschluss nur insoweit für ungültig erklärt (BGH, Urt. v. 11.04.2025 – V ZR 96/24, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-04-11&Aktenzeichen=V%20ZR%2096/24)).
- **Praxisfolge:** Für jeden gerügten Fehler den Betrag ausweisen, um den sich die Spitze des Mandanten ändert. Ohne diesen Nachweis ist die Anfechtung unschlüssig.

### 4. Vermögensbericht (§ 28 Abs. 4 WEG)

Der Verwalter hat nach Ablauf eines Kalenderjahres einen **Vermögensbericht** zu erstellen, der den Stand der Rücklagen und eine Aufstellung des wesentlichen Gemeinschaftsvermögens enthält, und ihn jedem Eigentümer zur Verfügung zu stellen ([§ 28 Abs. 4 WEG](https://www.gesetze-im-internet.de/woeigg/__28.html)).

- Der Vermögensbericht ist **nicht Gegenstand** des Nachschussbeschlusses. Sein Fehlen macht den Beschluss über die Abrechnungsspitze daher nicht ohne Weiteres anfechtbar; es ist eine eigenständige Pflichtverletzung des Verwalters.
- Reaktion: Vorlage verlangen, ggf. über die GdWE durchsetzen; bei Verweigerung Abberufungsgrund prüfen (`/wohnungseigentumsrecht:verwalter-bestellung-abberufung`).
- Der Verwaltungsbeirat soll Wirtschaftsplan und Jahresabrechnung vor der Beschlussfassung prüfen ([§ 29 Abs. 2 S. 2 WEG](https://www.gesetze-im-internet.de/woeigg/__29.html)).

### 5. Verteilungsschlüssel / Miteigentumsanteile (§ 16 Abs. 2 WEG)

Die Kosten trägt jeder Eigentümer nach dem Verhältnis seines **Miteigentumsanteils** ([§ 16 Abs. 2 S. 1 WEG](https://www.gesetze-im-internet.de/woeigg/__16.html)), soweit nicht eine Vereinbarung oder ein Beschluss nach § 16 Abs. 2 S. 2 WEG einen anderen Schlüssel vorsieht.

- Ein wirksam geänderter Schlüssel ist **in Wirtschaftsplan, Jahresabrechnung und Sonderumlage anzuwenden**; die Anfechtung der Folgebeschlüsse mit dem Argument, der Schlüssel sei unbillig, scheitert (BGH, Urt. v. 15.11.2024 – V ZR 239/23, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-11-15&Aktenzeichen=V%20ZR%20239/23)). Der Angriff gehört gegen den Änderungsbeschluss selbst (`/wohnungseigentumsrecht:kostenverteilung-16-weg`).
- Verbrauchsabhängige Kosten (Heizung, Warmwasser) nach HeizkostenV gesondert verteilt?
- Summieren sich die Einzelabrechnungen exakt auf die Gesamtabrechnung (Schlüssigkeitskontrolle)?

### 6. Fälligkeit, Zurückbehaltung und Beitreibung (§ 28 Abs. 3, § 17 WEG)

- Über Fälligkeit und Art der Zahlung beschließen die Eigentümer ([§ 28 Abs. 3 WEG](https://www.gesetze-im-internet.de/woeigg/__28.html)).
- Gegenüber beschlossenen **Vorschüssen** steht dem Eigentümer **kein Zurückbehaltungsrecht** zu (BGH, Urt. v. 14.11.2025 – V ZR 190/24, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-11-14&Aktenzeichen=V%20ZR%20190/24)) — auch dann nicht, wenn es auf anerkannte oder rechtskräftig zuerkannte Ansprüche gestützt wird. Eine **Aufrechnung** ist dagegen ausnahmsweise mit **anerkannten oder rechtskräftig festgestellten** Gegenforderungen zulässig (V ZR 190/24 Rn. 17, [Volltext](https://www.rws-verlag.de/fileadmin/Volltexte-4/v_zr_190-24.pdf)).
- Beitreibung, Vorrang in der Zwangsversteigerung (§ 10 Abs. 1 Nr. 2 ZVG) und — als **ultima ratio** — die **Entziehung** nach [§ 17 WEG](https://www.gesetze-im-internet.de/woeigg/__17.html) behandelt `/wohnungseigentumsrecht:hausgeld-beitreibung-entziehung`.

### 7. Ergebnis

Zusammenfassende Bewertung: (a) Beschlussgegenstand nach Auslegung, (b) gerügte Fehler mit Auswirkung auf die Spitze (Betrag je Fehler), (c) Verteilungsschlüssel und Schlüssigkeit, (d) Vermögensbericht, (e) Empfehlung — bestätigen, Nachbesserung durch Zweitbeschluss oder fristgerechte (Teil-)Anfechtung binnen eines Monats ([§ 45 WEG](https://www.gesetze-im-internet.de/woeigg/__45.html)).

## Quellen und Zitierweise

Verbindlich: [`../../references/zitierweise.md`](../../references/zitierweise.md).

### Statute (post-WEMoG)

- [§ 28 WEG](https://www.gesetze-im-internet.de/woeigg/__28.html) (Wirtschaftsplan, Jahresabrechnung, Vermögensbericht)
- [§ 16 WEG](https://www.gesetze-im-internet.de/woeigg/__16.html) (Kostenverteilung), [§ 19 WEG](https://www.gesetze-im-internet.de/woeigg/__19.html) (ordnungsmäßige Verwaltung), [§ 29 WEG](https://www.gesetze-im-internet.de/woeigg/__29.html) (Verwaltungsbeirat)
- [§ 17 WEG](https://www.gesetze-im-internet.de/woeigg/__17.html) (Entziehung), [§ 45 WEG](https://www.gesetze-im-internet.de/woeigg/__45.html) (Anfechtungsfrist)

### Rechtsprechung (V. Zivilsenat)

1. BGH, Urt. v. 14.11.2025 – V ZR 190/24 (kein Zurückbehaltungsrecht gegenüber Vorschüssen), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-11-14&Aktenzeichen=V%20ZR%20190/24)
2. BGH, Urt. v. 26.09.2025 – V ZR 108/24 (weites Ermessen bei Vorschüssen), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-09-26&Aktenzeichen=V%20ZR%20108/24)
3. BGH, Urt. v. 26.09.2025 – V ZR 206/24 (Abrechnungspflicht der GdWE; amtierender Verwalter als Organ; ausgeschiedener Verwalter nur nach Vertrag), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-09-26&Aktenzeichen=V%20ZR%20206/24)
4. BGH, Urt. v. 11.04.2025 – V ZR 96/24 (Teilungültigerklärung des Nachschussbeschlusses), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-04-11&Aktenzeichen=V%20ZR%2096/24)
5. BGH, Urt. v. 15.11.2024 – V ZR 239/23 (geänderter Schlüssel in Folgebeschlüssen anzuwenden), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-11-15&Aktenzeichen=V%20ZR%20239/23)
6. BGH, Urt. v. 20.09.2024 – V ZR 195/23 (nur Fehler mit Auswirkung auf die Spitze), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-09-20&Aktenzeichen=V%20ZR%20195/23)
7. BGH, Urt. v. 20.09.2024 – V ZR 235/23 (Zweitbeschluss über Vorschüsse), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-09-20&Aktenzeichen=V%20ZR%20235/23)
8. BGH, Urt. v. 19.07.2024 – V ZR 102/23 (Auslegung des „Genehmigungs"-Beschlusses als Beschluss über die Abrechnungsspitzen), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-07-19&Aktenzeichen=V%20ZR%20102/23)

### Kommentare

- Bärmann/Becker, WEG, aktuelle Aufl., § 28 `[unverifiziert – prüfen: Auflage und Rn.]`
- Hügel/Elzer, WEG, aktuelle Aufl., § 28 `[unverifiziert – prüfen: Auflage und Rn.]`

## Beispiel (Urteilsstil, verkürzt)

**Sachverhalt.** Die Versammlung vom 14.05.2026 beschließt: „Die Jahresabrechnung 2025 wird genehmigt." Eigentümerin E erhält eine Nachzahlung von 412 EUR. Die Gesamtabrechnung weist die Gebäudeversicherung doppelt aus; auf E entfallen davon 58 EUR. Ein Vermögensbericht liegt nicht vor.

**Bewertung.** Der Beschluss ist nach BGH V ZR 102/23 als Festsetzung der Abrechnungsspitzen auszulegen und daher von der Beschlusskompetenz des § 28 Abs. 2 WEG gedeckt. Die doppelt erfasste Versicherung erhöht die Spitze der E um 58 EUR; insoweit ist der Beschluss fehlerhaft (V ZR 195/23). Die Position ist abtrennbar, sodass nur eine Teilungültigerklärung in Höhe der Mehrbelastung in Betracht kommt (V ZR 96/24). Das Fehlen des Vermögensberichts trägt die Anfechtung nicht; E kann ihn gesondert verlangen. ([V ZR 102/23](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-07-19&Aktenzeichen=V%20ZR%20102/23), [V ZR 195/23](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-09-20&Aktenzeichen=V%20ZR%20195/23), [V ZR 96/24](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-04-11&Aktenzeichen=V%20ZR%2096/24))

**Ergebnis.** Teilanfechtungsklage gegen die GdWE bis **15.06.2026** erheben (Monatsfrist ab 14.05.2026; 14.06.2026 ist ein Sonntag, § 222 Abs. 2 ZPO), Begründung bis 14.07.2026:

```bash
python -m scripts.legal_calc.cli frist --ereignis 14.05.2026 --menge 1 --einheit monate
python -m scripts.legal_calc.cli frist --ereignis 14.05.2026 --menge 2 --einheit monate
```

## Risiken / typische Fehler

- **Wortlaut „Jahresabrechnung" als Kompetenzüberschreitung gerügt** → trägt nicht; der Beschluss ist als Beschluss über die **Abrechnungsspitze** auszulegen (BGH V ZR 102/23). Die **Beschlusskompetenz** ist gewahrt. ([V ZR 102/23](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-07-19&Aktenzeichen=V%20ZR%20102/23))
- **Fehler ohne Auswirkung auf die Spitze angegriffen** → Anfechtung unbegründet (BGH V ZR 195/23); je Fehler die Differenz beziffern. ([V ZR 195/23](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-09-20&Aktenzeichen=V%20ZR%20195/23))
- **Vollanfechtung statt Teilanfechtung** → bei abtrennbarer Position genügt die Teilanfechtung; die Vollanfechtung erhöht das Kostenrisiko (BGH V ZR 96/24). ([V ZR 96/24](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-04-11&Aktenzeichen=V%20ZR%2096/24))
- **Fehlender Vermögensbericht** als Anfechtungsgrund gegen den Nachschussbeschluss → falscher Hebel; gesondert vom Verwalter verlangen (§ 28 Abs. 4 WEG).
- **Schlüssel im Folgebeschluss angegriffen** → nach wirksamer Änderung ist der Angriff verspätet (BGH V ZR 239/23). ([V ZR 239/23](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-11-15&Aktenzeichen=V%20ZR%20239/23))
- **Vorschüsse zurückbehalten** → kein Zurückbehaltungsrecht (BGH V ZR 190/24); Verzug und Beitreibung drohen. ([V ZR 190/24](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-11-14&Aktenzeichen=V%20ZR%20190/24))
- **Anfechtungsfrist versäumt** → Monatsfrist des § 45 WEG ab Beschlussfassung, nicht ab Zugang des Protokolls.
- **Vor-WEMoG-Recht angewandt** → Genehmigung „der Jahresabrechnung" als Beschlussgegenstand ist seit dem WEMoG überholt; Gesamtabrechnung ist nur Rechengrundlage.
- **Entziehung § 17 WEG vorschnell** angedroht → ultima ratio, nicht Druckmittel im laufenden Hausgeldstreit.

## Ausgabeformat

```
PRÜFUNG JAHRESABRECHNUNG / HAUSGELD — WEG (Rechtsstand Oktober 2026)

I.    Beschlussgegenstand (§ 28 Abs. 2 WEG)
      - Wortlaut: <…>
      - Auslegung: Abrechnungsspitze / anderer Inhalt: <…>

II.   Wirtschaftsplan & Vorschüsse (§ 28 Abs. 1 WEG)
      - Vorschuss-Soll: <…> | Zweitbeschluss: <ja/nein>

III.  Abrechnungsspitze / Nachschuss
      - Kosten lt. Einzelabrechnung − Vorschüsse = Spitze: <Betrag>

IV.   Gerügte Fehler
      | Fehler | Auswirkung auf Spitze (EUR) | abtrennbar? |

V.    Verteilungsschlüssel (§ 16 Abs. 2 WEG)
      - angewandter Schlüssel / Grundlage: <GO / Beschluss Nr. …>
      - Einzelabrechnungen = Gesamtabrechnung: <ja/nein>

VI.   Vermögensbericht (§ 28 Abs. 4 WEG): <vorhanden / fehlt → gesondert verlangen>

VII.  Fälligkeit (§ 28 Abs. 3 WEG) / Zahlungsstand

VIII. Ergebnis & Empfehlung: <bestätigen / Zweitbeschluss / Teilanfechtung>
      Klagefrist: <Datum> | Begründungsfrist: <Datum> (§ 45 WEG)
```
