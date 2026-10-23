---
name: verwalter-bestellung-abberufung
description: "Bestellung, Abberufung und Pflichten des WEG-Verwalters nach der WEMoG-Reform – Bestellung durch Beschluss mit Höchstdauer fünf Jahre (erste Bestellung drei Jahre) und Wiederbestellung frühestens ein Jahr vor Ablauf § 26 Abs. 1, 2 WEG, jederzeitige Abberufung ohne wichtigen Grund und Ende des Verwaltervertrags spätestens sechs Monate danach § 26 Abs. 3 WEG, Unabdingbarkeit § 26 Abs. 5 WEG, Anspruch auf zertifizierten Verwalter § 19 Abs. 2 Nr. 6, § 26a WEG mit ZertVerwV (seit 01.12.2023; Übergangsschutz für Altverwalter bis 01.06.2024 abgelaufen), Aufgaben und Befugnisse § 27 WEG, Vertretung der GdWE § 9b WEG, Haftung gegenüber der GdWE. Rechtsstand: Oktober 2026. Use when ein Verwalter bestellt, wiederbestellt oder abberufen werden soll, ein Eigentümer einen zertifizierten Verwalter verlangt oder Pflichtverletzungen und Haftung des Verwalters geprüft werden."
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

# /wohnungseigentumsrecht:verwalter-bestellung-abberufung

## Zweck

Seit dem WEMoG ist der Verwalter **Organ der Gemeinschaft der Wohnungseigentümer (GdWE)**: Er vertritt sie nach außen ([§ 9b WEG](https://www.gesetze-im-internet.de/woeigg/__9b.html)) und ist ihr gegenüber zur ordnungsmäßigen Verwaltung verpflichtet ([§ 27 WEG](https://www.gesetze-im-internet.de/woeigg/__27.html)). Die Eigentümer können ihn **jederzeit ohne wichtigen Grund abberufen** ([§ 26 Abs. 3 WEG](https://www.gesetze-im-internet.de/woeigg/__26.html)), und jeder Eigentümer kann einen **zertifizierten Verwalter** verlangen ([§ 19 Abs. 2 Nr. 6 WEG](https://www.gesetze-im-internet.de/woeigg/__19.html)). Dieser Skill führt durch Bestellung, Wiederbestellung, Abberufung, Vertragsende, Zertifizierung und Haftung.

**Rechtsstand: Oktober 2026.** §§ 26, 26a, 27 WEG sind seit dem WEMoG unverändert. Der Anspruch auf einen zertifizierten Verwalter gilt seit **01.12.2023**; die Fiktion, dass ein am 01.12.2020 amtierender Verwalter als zertifiziert gilt, ist am **01.06.2024 ausgelaufen** ([§ 48 Abs. 4 WEG](https://www.gesetze-im-internet.de/woeigg/__48.html)). Ein Altverwalter ohne Zertifikat oder Befreiung erfüllt den Anspruch heute nicht mehr.

## Eingaben

- Bestellungsbeschluss (Datum, Laufzeit), Verwaltervertrag (Laufzeit, Vergütung, Kündigungsregeln)
- erste Bestellung nach Begründung des Wohnungseigentums? (Höchstdauer drei Jahre)
- Zertifikat nach § 26a WEG / Befreiungstatbestand nach der ZertVerwV
- Anzahl der Sondereigentumsrechte; ist ein Eigentümer Verwalter?
- Pflichtverletzungen (fehlende Jahresabrechnung, fehlender Vermögensbericht, Untätigkeit, eigenmächtige Zahlungen)
- Wer soll handeln: Eigentümermehrheit, einzelner Eigentümer, Verwaltungsbeirat?

## Sub-Agent-Architektur

- **Researcher** liefert §§ 9b, 19, 26, 26a, 27, 48 WEG, die ZertVerwV und die Rechtsprechung zur Verwalterhaftung.
- **Drafter** erstellt Beschlussanträge (Bestellung, Abberufung, Vertragsabschluss, Ermächtigung des Beirats), Kündigungsschreiben und ggf. die Beschlussersetzungsklage.
- **Reviewer** prüft Laufzeitgrenzen, Vertragsende, Vertretung beim Vertragsschluss und den Zertifizierungsstatus.

## Ablauf

### 1. Bestellung (§ 26 Abs. 1, 2 WEG)

- Über die **Bestellung** beschließen die Eigentümer mit einfacher Mehrheit ([§ 26 Abs. 1 WEG](https://www.gesetze-im-internet.de/woeigg/__26.html)).
- **Höchstdauer** fünf Jahre; bei der **ersten Bestellung nach Begründung** des Wohnungseigentums höchstens **drei Jahre** (§ 26 Abs. 2 S. 1 WEG).
- **Wiederbestellung** zulässig, aber nur durch erneuten Beschluss, der **frühestens ein Jahr vor Ablauf** der Bestellungszeit gefasst werden kann (§ 26 Abs. 2 S. 2 WEG).
- Abweichungen von Abs. 1–3 sind **nicht zulässig** (§ 26 Abs. 5 WEG) — auch nicht durch die Gemeinschaftsordnung.
- **Stimmrecht:** Ein Ausschluss von Eigentümern vom Stimmrecht bei der Verwalterbestellung durch die Gemeinschaftsordnung ist unwirksam (BGH, Urt. v. 27.02.2026 – V ZR 189/24, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-02-27&Aktenzeichen=V%20ZR%20189/24)).
- **Nachweis** gegenüber dem Grundbuchamt: Niederschrift über den Bestellungsbeschluss mit öffentlich beglaubigten Unterschriften der in § 24 Abs. 6 WEG genannten Personen (§ 26 Abs. 4 WEG).

### 2. Zertifizierter Verwalter (§ 19 Abs. 2 Nr. 6, § 26a WEG)

- Zur ordnungsmäßigen Verwaltung gehört die Bestellung eines **zertifizierten Verwalters** ([§ 19 Abs. 2 Nr. 6 WEG](https://www.gesetze-im-internet.de/woeigg/__19.html)). Jeder Eigentümer kann das verlangen ([§ 18 Abs. 2 WEG](https://www.gesetze-im-internet.de/woeigg/__18.html)).
- **Ausnahme** (alle drei Voraussetzungen kumulativ): weniger als **neun Sondereigentumsrechte**, ein **Eigentümer** ist Verwalter, und weniger als **ein Drittel** der Eigentümer verlangt einen zertifizierten Verwalter.
- **Zertifiziert** ist, wer die Prüfung vor einer **IHK** bestanden hat ([§ 26a Abs. 1 WEG](https://www.gesetze-im-internet.de/woeigg/__26a.html)); Einzelheiten und **Befreiungen** (u. a. Befähigung zum Richteramt, Immobilienkaufmann/-frau, Hochschulabschluss mit immobilienwirtschaftlichem Schwerpunkt) regelt die Zertifizierter-Verwalter-Prüfungsverordnung ([ZertVerwV](https://www.gesetze-im-internet.de/zertverwv/)) `[unverifiziert – prüfen: abschließender Befreiungskatalog (§ 7) der Verordnung im Volltext]`.
- **Übergang:** anwendbar seit 01.12.2023; der Altverwalterschutz endete am 01.06.2024 (§ 48 Abs. 4 WEG).
- Folge: Ein Beschluss, der einen nicht zertifizierten Verwalter bestellt, entspricht nicht ordnungsmäßiger Verwaltung und ist **anfechtbar**, wenn keine Ausnahme greift.

### 3. Verwaltervertrag und Vertretung

- Den Vertrag schließt die **GdWE** mit dem Verwalter. Gegenüber dem Verwalter vertritt der **Vorsitzende des Verwaltungsbeirats** oder ein durch Beschluss ermächtigter Eigentümer die GdWE ([§ 9b Abs. 2 WEG](https://www.gesetze-im-internet.de/woeigg/__9b.html)).
- Der Verwaltervertrag entfaltet nach der Reform **keine Schutzwirkung zugunsten der einzelnen Eigentümer**; Ansprüche wegen Pflichtverletzung stehen der GdWE zu (BGH, Urt. v. 05.07.2024 – V ZR 34/24, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-07-05&Aktenzeichen=V%20ZR%2034/24)).
- Laufzeit des Vertrags nicht länger als die Bestellung; Vergütungsregeln (Grund- und Sondervergütung) AGB-rechtlich prüfen.

### 4. Aufgaben und Befugnisse (§ 27 WEG)

- Der Verwalter trifft eigenständig Maßnahmen ordnungsmäßiger Verwaltung, die **untergeordnete Bedeutung** haben und nicht zu erheblichen Verpflichtungen führen oder zur **Wahrung einer Frist** oder **Abwendung eines Nachteils** erforderlich sind ([§ 27 Abs. 1 WEG](https://www.gesetze-im-internet.de/woeigg/__27.html)).
- Die Eigentümer können diese Befugnisse durch Beschluss **einschränken oder erweitern** (§ 27 Abs. 2 WEG), etwa durch Wertgrenzen. Haben sie über das „Ob" einer Erhaltungsmaßnahme entschieden, können sie die Durchführung dem Verwalter übertragen (BGH, Urt. v. 05.07.2024 – V ZR 241/23, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-07-05&Aktenzeichen=V%20ZR%20241/23)); ein verbindlicher Entscheidungsmaßstab muss im Delegationsbeschluss nicht vorgegeben werden.
- Pflichtaufgaben aus dem Gesetz: Einberufung (§ 24 WEG), Beschluss-Sammlung, Wirtschaftsplan, Jahresabrechnung und Vermögensbericht (§ 28 WEG). Die Jahresabrechnung schuldet die **GdWE**; der **amtierende** Verwalter erstellt sie als Organ — auch für Vorjahre, die sein Vorgänger nicht abgerechnet hat. Die Pflicht entsteht am 1. Januar des Folgejahres; ein zum 31.12. oder unterjährig ausgeschiedener Verwalter schuldet die Abrechnung für dieses Jahr nur, wenn sein Vertrag es vorsieht und die Pflicht in seiner Amtszeit entstanden ist (BGH, Urt. v. 26.09.2025 – V ZR 206/24, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-09-26&Aktenzeichen=V%20ZR%20206/24)). Beim Wechsel Rechnungslegung und Herausgabe der Unterlagen vom Vorgänger verlangen.

### 5. Abberufung und Vertragsende (§ 26 Abs. 3 WEG)

- Der Verwalter kann **jederzeit abberufen** werden — ein **wichtiger Grund ist nicht erforderlich** (§ 26 Abs. 3 S. 1 WEG). Vereinbarungen, die die Abberufung erschweren, sind unwirksam (§ 26 Abs. 5 WEG).
- Der **Verwaltervertrag endet spätestens sechs Monate nach der Abberufung** (§ 26 Abs. 3 S. 2 WEG). Bis dahin läuft die Vergütung grundsätzlich weiter; eine außerordentliche Kündigung aus wichtigem Grund (§ 626 BGB) beendet ihn früher.
- **Anspruch des einzelnen Eigentümers auf Abberufung:** Lehnt die Mehrheit die Abberufung ab, kann ein Eigentümer die Abberufung im Wege der **Beschlussersetzungsklage** nur durchsetzen, wenn ein Festhalten am Verwalter nicht mehr ordnungsmäßiger Verwaltung entspricht — praktisch bei schweren Pflichtverletzungen (`/wohnungseigentumsrecht:beschlussersetzungsklage`).
- **Herausgabe:** Verwaltungsunterlagen, Bankzugänge, Schlüssel und Beschluss-Sammlung sind herauszugeben; der Anspruch steht der GdWE zu.

### 6. Haftung

- Der Verwalter haftet der **GdWE** nach Vertrag (§ 280 BGB); einzelne Eigentümer können ihn nicht aus dem Vertrag in Anspruch nehmen (BGH V ZR 34/24). ([V ZR 34/24](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-07-05&Aktenzeichen=V%20ZR%2034/24))
- Auch ein **faktischer Verwalter** — wer die Verwaltung ohne wirksame Bestellung tatsächlich ausübt — hat die Pflichten eines bestellten Verwalters und muss der GdWE ungerechtfertigte Zahlungen erstatten (BGH, Urt. v. 30.01.2026 – V ZR 76/25, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-01-30&Aktenzeichen=V%20ZR%2076/25)).
- Gegenüber den Eigentümern kann die **GdWE** haften, wenn sie eine erforderliche Maßnahme am Gemeinschaftseigentum schuldhaft unterlässt — ab dem Zeitpunkt, zu dem eine ordnungsmäßig handelnde GdWE sie beschlossen und durchgeführt hätte (BGH, Urt. v. 27.02.2026 – V ZR 18/25, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-02-27&Aktenzeichen=V%20ZR%2018/25); Einzelheiten `[unverifiziert – prüfen]`); Regress der GdWE beim Verwalter prüfen.

### 7. Ergebnis

Status des Verwalters (bestellt bis …, zertifiziert ja/nein), Handlungsoptionen (Abberufung, Neubestellung, Kündigung des Vertrags, Herausgabe- und Schadensersatzansprüche der GdWE), Beschlussvorschläge, Fristen.

## Quellen und Zitierweise

Verbindlich: [`../../references/zitierweise.md`](../../references/zitierweise.md).

### Statute

- [§ 26 WEG](https://www.gesetze-im-internet.de/woeigg/__26.html) (Bestellung und Abberufung), [§ 26a WEG](https://www.gesetze-im-internet.de/woeigg/__26a.html) (zertifizierter Verwalter)
- [§ 27 WEG](https://www.gesetze-im-internet.de/woeigg/__27.html) (Aufgaben und Befugnisse), [§ 9b WEG](https://www.gesetze-im-internet.de/woeigg/__9b.html) (Vertretung)
- [§ 19 WEG](https://www.gesetze-im-internet.de/woeigg/__19.html) (Abs. 2 Nr. 6), [§ 18 WEG](https://www.gesetze-im-internet.de/woeigg/__18.html), [§ 48 WEG](https://www.gesetze-im-internet.de/woeigg/__48.html) (Abs. 4 Übergang)
- [ZertVerwV](https://www.gesetze-im-internet.de/zertverwv/) (Prüfung und Befreiungen)

### Rechtsprechung (V. Zivilsenat)

1. BGH, Urt. v. 27.02.2026 – V ZR 189/24 (Stimmrechtsausschluss bei Verwalterbestellung unwirksam), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-02-27&Aktenzeichen=V%20ZR%20189/24)
2. BGH, Urt. v. 27.02.2026 – V ZR 18/25 (Haftung der GdWE für unterlassene Erhaltung), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-02-27&Aktenzeichen=V%20ZR%2018/25)
3. BGH, Urt. v. 30.01.2026 – V ZR 76/25 (Pflichten und Haftung des faktischen Verwalters), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-01-30&Aktenzeichen=V%20ZR%2076/25)
4. BGH, Urt. v. 26.09.2025 – V ZR 206/24 (Jahresabrechnung als Pflicht der GdWE; ausgeschiedener Verwalter nur nach Vertrag), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-09-26&Aktenzeichen=V%20ZR%20206/24)
5. BGH, Urt. v. 05.07.2024 – V ZR 34/24 (keine Schutzwirkung des Verwaltervertrags für Eigentümer), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-07-05&Aktenzeichen=V%20ZR%2034/24)
6. BGH, Urt. v. 05.07.2024 – V ZR 241/23 (Delegation von Entscheidungen auf den Verwalter; bei Erhaltung nach Grundentscheidung der Eigentümer regelmäßig ordnungsmäßig), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-07-05&Aktenzeichen=V%20ZR%20241/23), [Volltext](https://www.rws-verlag.de/fileadmin/Volltexte-4/v_zr_241-23.pdf)

### Kommentare

- Bärmann/Becker, WEG, aktuelle Aufl., §§ 26, 26a `[unverifiziert – prüfen: Auflage und Rn.]`
- Jennißen, WEG, aktuelle Aufl., § 26 `[unverifiziert – prüfen: Auflage und Rn.]`

## Beispiel (Gutachtenstil, verkürzt)

**Sachverhalt.** Gemeinschaft mit 14 Einheiten. Verwalter V (kein Eigentümer) amtiert seit 2018, ohne IHK-Zertifikat und ohne Befreiung; Vertrag bis 31.12.2027. Die Jahresabrechnung 2025 fehlt im Oktober 2026 noch. Eigentümerin E will einen neuen Verwalter.

**Zertifizierung.** Die Ausnahme des § 19 Abs. 2 Nr. 6 WEG greift nicht (14 Einheiten, V ist kein Eigentümer). Der Altverwalterschutz ist seit 01.06.2024 abgelaufen. E kann die Bestellung eines zertifizierten Verwalters verlangen.

**Abberufung.** Die Eigentümer können V jederzeit ohne wichtigen Grund abberufen (§ 26 Abs. 3 S. 1 WEG). Der Vertrag endet dann spätestens sechs Monate danach (S. 2); bei fortgesetzter Abrechnungsverweigerung kommt eine außerordentliche Kündigung in Betracht.

**Ergebnis.** Tagesordnung: (1) Abberufung V, (2) Bestellung eines zertifizierten Verwalters für drei bis fünf Jahre, (3) Ermächtigung des Beiratsvorsitzenden zum Vertragsschluss (§ 9b Abs. 2 WEG), (4) Herausgabe der Unterlagen. Lehnt die Mehrheit ab: Beschlussersetzungsklage gestützt auf § 19 Abs. 2 Nr. 6 WEG.

## Risiken / typische Fehler

- **Bestellung über fünf Jahre** (bzw. drei Jahre bei erster Bestellung) → insoweit unwirksam (§ 26 Abs. 2 WEG).
- **Wiederbestellung zu früh** beschlossen (mehr als ein Jahr vor Ablauf) → unzulässig (§ 26 Abs. 2 S. 2 WEG).
- **Abberufung an wichtigen Grund geknüpft** → überholt; seit WEMoG jederzeit möglich, Erschwerungen unwirksam (§ 26 Abs. 3, 5 WEG).
- **Vertragslaufzeit nach Abberufung übersehen** → der Vertrag endet spätestens nach sechs Monaten; Vergütungsrisiko einplanen.
- **Altverwalter als zertifiziert behandelt** → Schutz endete am 01.06.2024 (§ 48 Abs. 4 WEG).
- **Eigentümer verklagt Verwalter aus dem Vertrag** → keine Schutzwirkung; Anspruchsinhaberin ist die GdWE (BGH V ZR 34/24). ([V ZR 34/24](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-07-05&Aktenzeichen=V%20ZR%2034/24))
- **Vertrag vom Verwalter selbst unterschrieben** → die GdWE wird gegenüber dem Verwalter vom Beiratsvorsitzenden oder einem ermächtigten Eigentümer vertreten (§ 9b Abs. 2 WEG).

## Ausgabeformat

```
VERWALTER — STATUS UND HANDLUNGSOPTIONEN (Rechtsstand Oktober 2026)

1. Bestellung: Beschluss <Datum> | Laufzeit bis <Datum> | Höchstdauer gewahrt? [🟢/🔴]
2. Zertifizierung (§ 19 Abs. 2 Nr. 6, § 26a WEG):
   - Zertifikat / Befreiung: <…>
   - Ausnahme (< 9 Einheiten + Eigentümer-Verwalter + < ⅓ Verlangen)? <ja/nein>
3. Vertrag: Laufzeit <…> | Vergütung <…> | Vertretung GdWE (§ 9b Abs. 2): <…>
4. Pflichtverletzungen: <Abrechnung / Vermögensbericht / Einberufung / Zahlungen>
5. Optionen:
   - Abberufung (§ 26 Abs. 3 S. 1) → Vertragsende spätestens <Datum + 6 Monate>
   - außerordentliche Kündigung (§ 626 BGB): <…>
   - Ansprüche der GdWE (Herausgabe, Schadensersatz): <…>
6. Beschlussvorschläge: <…>
7. Prozessual: Anfechtung / Beschlussersetzung, Frist § 45 WEG <Datum>
```
