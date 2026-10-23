---
name: eigentuemerversammlung-beschlussfassung
description: "Vorbereitung, Durchführung und Kontrolle der Eigentümerversammlung nach WEG – Einberufung in Textform mit Drei-Wochen-Frist und Einberufungsverlangen von mehr als einem Viertel § 24 WEG, Ankündigung des Gegenstands § 23 Abs. 2 WEG, Online-Teilnahme (Hybridversammlung) § 23 Abs. 1 S. 2 WEG, virtuelle Eigentümerversammlung § 23 Abs. 1a WEG (Drei-Viertel-Beschluss, höchstens drei Jahre, jährliche Präsenzversammlung bis 2028 nach § 48 Abs. 6 WEG), Umlaufbeschluss § 23 Abs. 3 WEG, Mehrheit, Kopfprinzip, Vollmacht in Textform und Stimmverbot § 25 WEG, Niederschrift und Beschluss-Sammlung § 24 Abs. 6–8 WEG, Verwaltungsbeirat § 29 WEG. Rechtsstand: Oktober 2026. Use when eine Eigentümerversammlung einberufen, als hybride oder virtuelle Versammlung organisiert, ein Umlaufbeschluss vorbereitet oder die formelle Ordnungsmäßigkeit einer Beschlussfassung geprüft werden soll."
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

# /wohnungseigentumsrecht:eigentuemerversammlung-beschlussfassung

## Zweck

Fast jede erfolgreiche Beschlussanfechtung beginnt mit einem Formfehler: falsche Einladung, nicht angekündigter Tagesordnungspunkt, unzulässige Vollmacht, Abstimmung im falschen Format. Dieser Skill führt durch Einberufung, Versammlungsformat (Präsenz, hybrid, virtuell), Umlaufverfahren und Abstimmung und liefert eine Checkliste, mit der Verwalter und Beirat anfechtungsfeste Beschlüsse vorbereiten — und mit der ein Eigentümer die formelle Angreifbarkeit eines Beschlusses prüft.

**Rechtsstand: Oktober 2026.** Seit dem **17.10.2024** können die Eigentümer die **virtuelle Eigentümerversammlung** beschließen ([§ 23 Abs. 1a WEG](https://www.gesetze-im-internet.de/woeigg/__23.html); G v. 10.10.2024, BGBl. 2024 I Nr. 306). Für Beschlüsse, die vor dem 01.01.2028 gefasst werden, gilt eine **Präsenzpflicht einmal jährlich bis einschließlich 2028** ([§ 48 Abs. 6 WEG](https://www.gesetze-im-internet.de/woeigg/__48.html)). Ein Beschlussfähigkeitsquorum gibt es seit dem WEMoG nicht mehr. Das BMJV befragt derzeit die Eigentümer (bis 12.11.2026) zur Vorbereitung der für **2027** geplanten Evaluation des WEG; ein Änderungsentwurf liegt nicht vor.

## Eingaben

- Gemeinschaftsordnung (Einberufungsregeln, Stimmrecht, Vertretungsbeschränkungen, Öffnungsklauseln)
- bestehende Beschlüsse zu Online-Teilnahme (§ 23 Abs. 1 S. 2 WEG) oder virtueller Versammlung (§ 23 Abs. 1a WEG)
- Einladung: Datum des Versands, Form, Tagesordnung, Beschlussanträge
- Teilnehmerliste, Vollmachten, Stimmverhältnisse, Protokoll
- Anzahl der Einheiten und Eigentümer (Kopfprinzip; Mitberechtigte)

## Sub-Agent-Architektur

- **Researcher** liefert §§ 23–25, 29, 48 WEG und die verifizierte Rechtsprechung zu Hybridversammlung, Umlaufbeschluss und Stimmrecht.
- **Drafter** erstellt Einladung, Tagesordnung mit bestimmten Beschlussanträgen, Beschluss über das Versammlungsformat oder die Prüfung eines gefassten Beschlusses.
- **Reviewer** prüft Fristen, Formate, Stimmrechte und die Kausalität etwaiger Fehler.

## Ablauf

### 1. Wer beruft ein? (§ 24 Abs. 1–3 WEG)

- Der **Verwalter** beruft mindestens einmal jährlich ein ([§ 24 Abs. 1 WEG](https://www.gesetze-im-internet.de/woeigg/__24.html)).
- Er **muss** einberufen, wenn **mehr als ein Viertel** der Eigentümer dies in **Textform** unter Angabe von Zweck und Gründen verlangt (§ 24 Abs. 2 WEG).
- Fehlt ein Verwalter oder weigert er sich pflichtwidrig: Einberufung durch den **Beiratsvorsitzenden**, seinen Vertreter oder einen **durch Beschluss ermächtigten Eigentümer** (§ 24 Abs. 3 WEG). Eine Einberufung durch einen Unbefugten macht die gefassten Beschlüsse anfechtbar.

### 2. Form, Frist, Tagesordnung (§ 24 Abs. 4, § 23 Abs. 2 WEG)

- **Textform** (§ 126b BGB) genügt; E-Mail ist ausreichend, wenn die Adresse dem Verwalter vom Eigentümer mitgeteilt wurde `[unverifiziert – prüfen: Zugangsfragen bei E-Mail-Einladung]`.
- **Frist:** mindestens **drei Wochen**, außer bei besonderer Dringlichkeit (Soll-Vorschrift, § 24 Abs. 4 S. 2 WEG). Eine Unterschreitung macht Beschlüsse nur anfechtbar, wenn nicht auszuschließen ist, dass sie sich auf das Ergebnis ausgewirkt hat `[unverifiziert – prüfen]`.
- **Tagesordnung:** Jeder Beschlussgegenstand muss **bei der Einberufung bezeichnet** sein ([§ 23 Abs. 2 WEG](https://www.gesetze-im-internet.de/woeigg/__23.html)). „Verschiedenes" trägt keinen Beschluss von Gewicht.
- **Fristbeginn ist der Zugang**, nicht der Versand. Zwischen Zugang und Versammlung müssen **drei volle Wochen** liegen; frühester Versammlungstag ist der **Tag nach Fristende**.
- **Rechenbeispiel:** Postversand am 02.11.2026, Zugang am 04.11.2026 → Fristende 25.11.2026 → frühester Versammlungstag **26.11.2026**:

```bash
python -m scripts.legal_calc.cli frist --ereignis 04.11.2026 --menge 3 --einheit wochen --kein-rollover
# Fristende 25.11.2026 (Mittwoch) -> Versammlung frühestens am 26.11.2026
```

Bei E-Mail-Einladung ist der Zugang regelmäßig am Versandtag anzunehmen, wenn die Nachricht zu üblichen Geschäftszeiten eingeht; bei Postversand zwei bis drei Tage Puffer einplanen.

### 3. Versammlungsformat wählen (§ 23 Abs. 1, 1a WEG)

| Format | Grundlage | Mehrheit | Besonderheiten |
|---|---|---|---|
| **Präsenz** | Gesetzlicher Regelfall | — | Ort zumutbar, Zeit nicht zur Unzeit |
| **Hybrid** (Präsenz + Online-Teilnahme) | Beschluss nach § 23 Abs. 1 S. 2 WEG | einfache Mehrheit | Wer online teilnehmen will, muss das **verlangen**; der Verwalter muss die Online-Teilnahme nicht von sich aus anbieten (BGH, Urt. v. 20.09.2024 – V ZR 123/23, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-09-20&Aktenzeichen=V%20ZR%20123/23)) |
| **Virtuell** (ohne physische Präsenz) | Beschluss nach **§ 23 Abs. 1a WEG** | mindestens **drei Viertel der abgegebenen Stimmen** | Geltung höchstens **drei Jahre** ab Beschlussfassung; Teilnahme und Rechteausübung müssen mit einer Präsenzversammlung **vergleichbar** sein |

**Präsenzpflicht bis 2028:** Wird vor dem 01.01.2028 ein Beschluss nach § 23 Abs. 1a WEG gefasst, ist bis einschließlich 2028 mindestens einmal im Jahr eine Präsenzversammlung durchzuführen, sofern die Eigentümer nicht **einstimmig** verzichten. Ein Verstoß führt **nicht** zur Nichtigkeit oder Anfechtbarkeit der virtuell gefassten Beschlüsse ([§ 48 Abs. 6 WEG](https://www.gesetze-im-internet.de/woeigg/__48.html)).

**Vergleichbarkeit:** Ton- und Bildübertragung, Rede- und Antragsrecht, geheime Abstimmung wo erforderlich, technische Unterstützung. Technische Ausfälle, die Eigentümer von der Teilnahme ausschließen, sind formelle Fehler.

### 4. Umlaufbeschluss (§ 23 Abs. 3 WEG)

- Ohne Versammlung ist ein Beschluss gültig, wenn **alle** Eigentümer ihre Zustimmung in **Textform** erklären (§ 23 Abs. 3 S. 1 WEG).
- Die Eigentümer können in einer Versammlung beschließen, dass für einen **einzelnen Gegenstand** im Umlaufverfahren die **Mehrheit** der abgegebenen Stimmen genügt (§ 23 Abs. 3 S. 2 WEG).
- Dieser **Absenkungsbeschluss** kann Gegenstand einer Beschlussmängelklage sein. Seine Ungültigerklärung oder Nichtigkeit macht einen anschließend im Umlaufverfahren mit einfacher Mehrheit gefassten Beschluss **nur anfechtbar**, nicht nichtig. Die Klage gegen den Absenkungsbeschluss wird unzulässig, sobald der Umlaufbeschluss bestandskräftig ist (BGH, Urt. v. 17.07.2026 – V ZR 190/25, Leitsätze a–c, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-07-17&Aktenzeichen=V%20ZR%20190/25), [Volltext](https://www.rws-verlag.de/fileadmin/Volltexte-4/V_ZR_190-25.pdf)). Praxis: den Umlaufbeschluss **selbst fristgerecht** anfechten.

### 5. Abstimmung (§ 25 WEG)

- **Mehrheit der abgegebenen Stimmen**; Enthaltungen zählen nicht ([§ 25 Abs. 1 WEG](https://www.gesetze-im-internet.de/woeigg/__25.html)).
- **Kopfprinzip:** Jeder Eigentümer hat eine Stimme; Mitberechtigte stimmen einheitlich ab (§ 25 Abs. 2 WEG). Abweichende Stimmrechtsregeln (Objekt- oder Wertprinzip) nur durch Vereinbarung.
- **Stimmrechtsbeschränkungen** in der Gemeinschaftsordnung sind möglich, wenn sie klar formuliert sind; ein Ausschluss vom Stimmrecht bei der Verwalterbestellung, dem Wirtschaftsplan und der Jahresabrechnung ist jedoch unwirksam (BGH, Urt. v. 27.02.2026 – V ZR 189/24, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-02-27&Aktenzeichen=V%20ZR%20189/24)).
- **Vollmachten** bedürfen der **Textform** (§ 25 Abs. 3 WEG); Vertretungsbeschränkungen der Gemeinschaftsordnung beachten.
- **Stimmverbot** bei Rechtsgeschäften mit dem Eigentümer, Rechtsstreit gegen ihn und nach rechtskräftiger Verurteilung nach § 17 WEG (§ 25 Abs. 4 WEG). Ein Verwalter, der zugleich Eigentümer ist, darf über seine eigene Abberufung aus wichtigem Grund nicht mitstimmen `[unverifiziert – prüfen]`.

### 6. Verkündung, Niederschrift, Beschluss-Sammlung (§ 24 Abs. 5–8 WEG)

- Den **Vorsitz** führt der Verwalter, sofern nichts anderes beschlossen wird (§ 24 Abs. 5 WEG). Ein Beschluss entsteht erst mit der **Verkündung** des Ergebnisses durch den Versammlungsleiter.
- **Niederschrift** unverzüglich; zu unterschreiben vom Vorsitzenden, einem Eigentümer und ggf. dem Beiratsvorsitzenden (§ 24 Abs. 6 WEG).
- **Beschluss-Sammlung** fortlaufend und unverzüglich führen; Anfechtung und Aufhebung vermerken (§ 24 Abs. 7, 8 WEG). Jeder Eigentümer hat ein Einsichtsrecht.

### 7. Verwaltungsbeirat (§ 29 WEG)

Beiratsmitglieder werden durch Beschluss bestellt; auch **juristische Personen** können Mitglied sein (BGH, Urt. v. 04.07.2025 – V ZR 225/24, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-07-04&Aktenzeichen=V%20ZR%20225/24)). Der Beirat soll Wirtschaftsplan und Jahresabrechnung vor der Beschlussfassung prüfen ([§ 29 Abs. 2 S. 2 WEG](https://www.gesetze-im-internet.de/woeigg/__29.html)); unentgeltlich tätige Mitglieder haften nur für Vorsatz und grobe Fahrlässigkeit (§ 29 Abs. 3 WEG).

### 8. Ergebnis

Checkliste mit Ampel je Prüfpunkt; bei bereits gefassten Beschlüssen: Fehler, Kausalität, Rechtsfolge (nichtig / anfechtbar / unbeachtlich), Klagefrist nach [§ 45 WEG](https://www.gesetze-im-internet.de/woeigg/__45.html).

## Quellen und Zitierweise

Verbindlich: [`../../references/zitierweise.md`](../../references/zitierweise.md).

### Statute

- [§ 23 WEG](https://www.gesetze-im-internet.de/woeigg/__23.html) (Versammlung, Online-Teilnahme, virtuelle Versammlung, Ankündigung, Umlaufbeschluss, Nichtigkeit)
- [§ 24 WEG](https://www.gesetze-im-internet.de/woeigg/__24.html) (Einberufung, Vorsitz, Niederschrift, Beschluss-Sammlung)
- [§ 25 WEG](https://www.gesetze-im-internet.de/woeigg/__25.html) (Mehrheit, Kopfprinzip, Vollmacht, Stimmverbot)
- [§ 29 WEG](https://www.gesetze-im-internet.de/woeigg/__29.html) (Verwaltungsbeirat), [§ 48 WEG](https://www.gesetze-im-internet.de/woeigg/__48.html) (Übergangsvorschriften, Abs. 6 Präsenzpflicht)

### Rechtsprechung (V. Zivilsenat)

1. BGH, Urt. v. 17.07.2026 – V ZR 190/25 (Absenkungsbeschluss; Folgen für den Umlaufbeschluss), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-07-17&Aktenzeichen=V%20ZR%20190/25), [Volltext](https://www.rws-verlag.de/fileadmin/Volltexte-4/V_ZR_190-25.pdf)
2. BGH, Urt. v. 27.02.2026 – V ZR 189/24 (Stimmrechtsbeschränkungen; Ausschluss bei Verwalterbestellung, Wirtschaftsplan, Jahresabrechnung unwirksam), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-02-27&Aktenzeichen=V%20ZR%20189/24)
3. BGH, Urt. v. 04.07.2025 – V ZR 225/24 (juristische Person im Verwaltungsbeirat), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-07-04&Aktenzeichen=V%20ZR%20225/24)
4. BGH, Urt. v. 20.09.2024 – V ZR 123/23 (Online-Teilnahme nur auf Verlangen), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-09-20&Aktenzeichen=V%20ZR%20123/23)

### Kommentare

- Bärmann/Merle, WEG, aktuelle Aufl., §§ 23–25 `[unverifiziert – prüfen: Auflage und Rn.]`
- Hügel/Elzer, WEG, aktuelle Aufl., § 23 Rn. zu Abs. 1a `[unverifiziert – prüfen: Auflage und Rn.]`

## Beispiel (Urteilsstil, verkürzt)

**Sachverhalt.** Gemeinschaft mit 24 Einheiten. Die Versammlung vom 12.03.2026 beschloss mit 15 Ja- und 6 Nein-Stimmen bei 3 Enthaltungen, die Versammlungen „künftig nur noch online" abzuhalten. Die Einladung zur Versammlung am 26.10.2026 erging per E-Mail am 08.10.2026 und enthielt den Punkt „Fassadensanierung".

**Bewertung.** Der Beschluss vom 12.03.2026 verfehlte die Drei-Viertel-Mehrheit der abgegebenen Stimmen: 15 von 21 sind 71,4 %. Er ist anfechtbar, aber wohl nicht nichtig, weil § 23 Abs. 1a WEG die Beschlusskompetenz gewährt und nur das Quorum verfehlt ist `[unverifiziert – prüfen]`. Er ist zudem unbefristet, obwohl das Gesetz höchstens drei Jahre zulässt. Nach Ablauf der Anfechtungsfrist ist er bestandskräftig. Die E-Mail-Einladung ging am 08.10.2026 zu; die Drei-Wochen-Frist endete erst am 29.10.2026, die Versammlung am 26.10.2026 liegt davor; ein Fall besonderer Dringlichkeit ist nicht ersichtlich.

**Ergebnis.** Die Versammlung vom 26.10.2026 sollte verlegt und mit voller Frist neu einberufen werden. Für 2026 ist zudem eine Präsenzversammlung durchzuführen (§ 48 Abs. 6 WEG), weil kein einstimmiger Verzicht vorliegt.

## Risiken / typische Fehler

- **Gegenstand nicht angekündigt** → Beschluss anfechtbar (§ 23 Abs. 2 WEG); „Verschiedenes" trägt keine Sachbeschlüsse.
- **Drei-Wochen-Frist unterschritten** → Anfechtungsrisiko, wenn Kausalität nicht ausgeschlossen werden kann.
- **Virtuelle Versammlung mit einfacher Mehrheit beschlossen** → § 23 Abs. 1a WEG verlangt drei Viertel der abgegebenen Stimmen und höchstens drei Jahre.
- **Präsenzpflicht bis 2028 übersehen** → nach § 48 Abs. 6 WEG einmal jährlich Präsenz, aber kein Anfechtungsgrund für virtuell gefasste Beschlüsse.
- **Online-Teilnahme ohne Beschluss gewährt oder verweigert** → Grundlage ist ein Beschluss nach § 23 Abs. 1 S. 2 WEG; ohne Verlangen besteht kein Anspruch (BGH V ZR 123/23). ([V ZR 123/23](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-09-20&Aktenzeichen=V%20ZR%20123/23))
- **Umlaufbeschluss mit Mehrheit ohne Absenkungsbeschluss** → ohne wirksamen Absenkungsbeschluss trägt nur Allstimmigkeit in Textform (§ 23 Abs. 3 S. 1 WEG). Ist der Absenkungsbeschluss mangelhaft, ist der Mehrheits-Umlaufbeschluss nach BGH V ZR 190/25 nur anfechtbar — ihn daher selbst fristgerecht anfechten ([dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-07-17&Aktenzeichen=V%20ZR%20190/25)).
- **Stimmrechtsausschluss aus der Gemeinschaftsordnung angewandt** → bei Verwalterbestellung, Wirtschaftsplan und Jahresabrechnung unwirksam (BGH V ZR 189/24). ([V ZR 189/24](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-02-27&Aktenzeichen=V%20ZR%20189/24))
- **Vollmacht mündlich** → unwirksam; Textform erforderlich (§ 25 Abs. 3 WEG).

## Ausgabeformat

```
EIGENTÜMERVERSAMMLUNG — CHECKLISTE (Rechtsstand Oktober 2026)

1. Einberufung
   - Einberufender: <Verwalter / Beirat / ermächtigter Eigentümer>   [🟢/🔴]
   - Form: Textform ✓ | Versand: <Datum> | Zugang: <Datum>
   - Frist (§ 24 Abs. 4 WEG): <Tage> — 3 Wochen gewahrt? [🟢/🟡]
   - Tagesordnung: jeder Beschlussgegenstand bezeichnet? [🟢/🔴]

2. Format
   [ ] Präsenz  [ ] hybrid (Beschluss Nr. …)  [ ] virtuell (Beschluss Nr. …, ¾, bis …)
   - Präsenzpflicht § 48 Abs. 6 WEG erfüllt / Verzicht einstimmig: <…>

3. Abstimmung (§ 25 WEG)
   - Ja / Nein / Enthaltung: <…> → Mehrheit: <einfach / ¾ erreicht?>
   - Vollmachten Textform ✓ | Stimmverbote: <…>

4. Umlaufverfahren (§ 23 Abs. 3 WEG): <Allstimmigkeit / Absenkungsbeschluss Nr. …>

5. Niederschrift / Beschluss-Sammlung (§ 24 Abs. 6–8 WEG): <…>

6. Ergebnis: <anfechtungsfest / Fehler + Kausalität + Rechtsfolge>
   Klagefrist § 45 WEG: <Datum>
```
