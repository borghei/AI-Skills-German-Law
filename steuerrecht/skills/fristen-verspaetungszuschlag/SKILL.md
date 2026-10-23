---
name: fristen-verspaetungszuschlag
description: "Steuererklärungsfristen und Verspätungszuschlag – Abgabefristen § 149 Abs. 2, 3 AO (VZ 2025: 31.07.2026 / beraten 01.03.2027; VZ 2026: 02.08.2027 / beraten 29.02.2028), Ende der Corona-Verlängerungen (Art. 97 § 36 EGAO) mit VZ 2024, Vorabanforderung § 149 Abs. 4 AO, Fristverlängerung § 109 AO, Ermessens- und Muss-Zuschlag § 152 Abs. 1, 2 AO (14 Monate; 19 Monate nur bei Land- und Forstwirten mit abweichendem Wirtschaftsjahr), Ausnahmen § 152 Abs. 3, Bemessung § 152 Abs. 5, 6, 10 AO (0,25 %, mind. 25 EUR je Monat, höchstens 25.000 EUR), Zwangsgeld § 329 AO, Schätzung § 162 AO. Rechtsstand Oktober 2026, mit Hinweis auf § 152 Abs. 4 AO im Entwurf JStG 2026. Use when Erklärungsfristen bestimmt, Fristverlängerung beantragt oder ein Verspätungszuschlag angegriffen werden soll."
language: de
provider_variants:
  - claude
  - gemini
  - openai
test: ./test.md
---

# /steuerrecht:fristen-verspaetungszuschlag

> **Rechtsstand: Oktober 2026.** Die coronabedingten Fristverlängerungen (Art. 97 § 36 EGAO) sind mit dem Veranlagungszeitraum 2024 ausgelaufen; ab VZ 2025 gelten wieder die Regelfristen des § 149 AO. Entwurf JStG 2026 (BT-Drs. 21/8283, nicht verabschiedet): Neufassung des § 152 Abs. 4 AO zur Auswahl des Zuschlagsschuldners bei mehreren Erklärungspflichtigen (Vorrang des Steuerschuldners, Zusammenveranlagung). Anhängig: BFH – IX R 35/24 (Ermessen nach § 152 Abs. 1 AO; Verhandlung 10.11.2026) `[unverifiziert – prüfen]`.

## Zweck

Der Verspätungszuschlag ist seit der Reform 2017 in weiten Teilen eine **Muss**-Folge, die automatisiert festgesetzt wird. Die Kunst liegt deshalb vor der Fristversäumnis: Fristen exakt bestimmen, Fristverlängerung rechtzeitig und begründet beantragen, Vorabanforderungen im Blick behalten. Nach der Festsetzung bleibt die Prüfung der Ausnahmen, der Bemessung und — beim Ermessenszuschlag — der Ermessensausübung.

## Eingaben

- Steuerart(en), Veranlagungszeitraum, Erklärungspflicht (§ 149 Abs. 1 AO, Einzelsteuergesetze)
- Beratener Fall? (Steuerberater / Lohnsteuerhilfeverein, § 149 Abs. 3 AO)
- Land- und Forstwirt mit abweichendem Wirtschaftsjahr?
- Vorabanforderung durch das Finanzamt (§ 149 Abs. 4 AO) mit Frist?
- Abgabedatum, festgesetzte Steuer, Vorauszahlungen, Steuerabzugsbeträge
- Gründe der Verspätung (Krankheit, fehlende Unterlagen Dritter, Kanzleiorganisation)

## Sub-Agent-Architektur

Ein **Fristen-Prüfer** bestimmt die maßgebliche Frist je Erklärung und rechnet Wochenend- und Feiertagsverschiebungen nach § 108 Abs. 3 AO deterministisch. Ein **Verlängerungs-Prüfer** prüft Begründung und Erfolgsaussicht eines Antrags nach § 109 AO. Ein **Zuschlags-Prüfer** ordnet den Fall Abs. 1 (Ermessen) oder Abs. 2 (Muss) zu, prüft die Ausnahmen des Abs. 3 und rechnet die Bemessung nach. Ein **Rechtsbehelfs-Prüfer** entscheidet über Einspruch, Billigkeitsantrag und Ruhen.

## Ablauf

### 1. Abgabefristen ([§ 149 AO](https://www.gesetze-im-internet.de/ao_1977/__149.html))

| Fall | Regel | VZ 2025 | VZ 2026 |
|---|---|---|---|
| Nicht beraten (§ 149 Abs. 2 S. 1 AO) | sieben Monate nach Ablauf des Kalenderjahres (31.07.) | **31.07.2026** (Freitag) | **02.08.2027** (31.07.2027 ist ein Samstag) |
| Beraten (§ 149 Abs. 3 AO) | letzter Tag des Monats Februar des zweiten Folgejahres | **01.03.2027** (28.02.2027 ist ein Sonntag) | **29.02.2028** (Dienstag, Schaltjahr) |
| Land- und Forstwirte, beraten | 31.07. des zweiten Folgejahres | 31.07.2027 → 02.08.2027 | 31.07.2028 |
| Vorabanforderung (§ 149 Abs. 4 AO) | vom Finanzamt gesetzte Frist (vier Monate nach Bekanntgabe der Anordnung `[unverifiziert – prüfen]`) | — | — |

- Fristverschiebung bei Wochenende/Feiertag: **§ 108 Abs. 3 AO**. Bundeslandspezifische Feiertage beachten.
- **Corona-Fristen**: Art. 97 § 36 EGAO verlängerte die Fristen letztmals für VZ 2024 (beraten: 30.04.2026; Land- und Forstwirte: 30.09.2026) — für VZ 2025 nicht mehr anwenden.
- **Vorabanforderung** (§ 149 Abs. 4 AO) im beratenen Fall z. B. bei verspäteter Abgabe im Vorjahr, nachträglichen Vorauszahlungen, hohen Abschlusszahlungen oder Außenprüfung; sie setzt die Frist für § 152 Abs. 2 Nr. 3 AO.

```bash
# Feiertage des maßgeblichen Bundeslandes für die Verschiebung nach § 108 Abs. 3 AO
python -m scripts.legal_calc.cli feiertage --jahr 2027 --land BY
```

Hinweis: Die gesetzlichen Abgabefristen sind feste Kalenderdaten, keine Ereignisfristen. Der Rechner dient hier nur zur Feiertagsprüfung für § 108 Abs. 3 AO; die Ausgangsdaten stehen in der Tabelle.

### 2. Fristverlängerung ([§ 109 AO](https://www.gesetze-im-internet.de/ao_1977/__109.html))

- Nicht beratene Fälle: Verlängerung auf Antrag, auch rückwirkend, nach Ermessen (§ 109 Abs. 1 AO).
- **Beratene Fälle**: Über die Frist des § 149 Abs. 3 AO hinaus nur **ausnahmsweise**, wenn der Steuerpflichtige ohne Verschulden verhindert ist, die Frist einzuhalten; das Verschulden des Vertreters oder Erfüllungsgehilfen steht dem eigenen gleich (§ 109 Abs. 2 AO). Arbeitsüberlastung der Kanzlei genügt regelmäßig nicht.
- Verlängerung **vor** Fristablauf beantragen; ein rückwirkend verlängerter Fall fällt aus dem Muss-Zuschlag heraus (§ 152 Abs. 3 Nr. 1 AO).
- Die Ablehnung ist ein Verwaltungsakt — Einspruch; vorläufiger Rechtsschutz nur über § 114 FGO.

### 3. Verspätungszuschlag ([§ 152 AO](https://www.gesetze-im-internet.de/ao_1977/__152.html)) — Ermessen oder Muss?

- **Ermessenszuschlag** (§ 152 Abs. 1 AO): bei nicht oder nicht fristgemäßer Abgabe; entfällt, wenn die Versäumnis **entschuldbar** erscheint (Verschulden des Vertreters wird zugerechnet). Die Ermessenserwägungen (Dauer, Höhe des Zahlungsanspruchs, Vorteile aus der Verspätung, Verschulden, Leistungsfähigkeit) müssen erkennbar sein.
- **Muss-Zuschlag** (§ 152 Abs. 2 AO) bei Jahres- und Stichtagserklärungen, die abgegeben wurden
  1. nicht binnen **14 Monaten** nach Ablauf des Kalenderjahres bzw. Besteuerungszeitpunkts — das ist der Regelfall auch für **beratene** Steuerpflichtige: Die 14-Monats-Frist endet am letzten Tag des Februar des zweiten Folgejahres und fällt damit mit der Abgabefrist des § 149 Abs. 3 AO zusammen; jede Abgabe nach Ablauf der Beraterfrist löst den Muss-Zuschlag aus,
  2. nur in den Fällen des § 149 Abs. 2 S. 2 AO (**Land- und Forstwirte mit abweichendem Wirtschaftsjahr**) nicht binnen **19 Monaten**, oder
  3. bei Vorabanforderung nicht bis zur gesetzten Frist.
- **Ausnahmen vom Muss-Zuschlag** (§ 152 Abs. 3 AO): Fristverlängerung nach § 109 AO (auch rückwirkend); Steuer auf **null oder negativ** festgesetzt; festgesetzte Steuer übersteigt die Summe aus Vorauszahlungen und Abzugsbeträgen nicht; bestimmte Jahresanmeldungen (Lohnsteuer, USt-Sondervorauszahlung u. a.). In diesen Fällen bleibt der Ermessenszuschlag nach Abs. 1 möglich.

### 4. Bemessung

| Erklärung | Bemessung je angefangenem Monat der Verspätung |
|---|---|
| Jahres-/Stichtagserklärung (§ 152 Abs. 5 S. 2 AO) | **0,25 %** der um Vorauszahlungen und anzurechnende Steuerabzugsbeträge verminderten festgesetzten Steuer, **mindestens 25 EUR** |
| sonstige Erklärungen (§ 152 Abs. 5 S. 1 AO) | 0,25 % der festgesetzten Steuer, mindestens 10 EUR |
| Feststellungs-, Gewerbesteuermessbetrags-, Zerlegungserklärungen (§ 152 Abs. 6 AO) | **25 EUR** |

- Erstmalige Aufforderung nach Ablauf der gesetzlichen Frist bei Personen, die nicht mit einer Erklärungspflicht rechnen mussten: Berechnung erst ab Ablauf der in der Aufforderung gesetzten Frist (§ 152 Abs. 5 S. 3 AO).
- **Höchstbetrag 25.000 EUR**, Abrundung auf volle Euro (§ 152 Abs. 10 AO).
- Der Zuschlag ist eine steuerliche Nebenleistung (§ 3 Abs. 4 AO); er wird regelmäßig mit dem Steuerbescheid verbunden und ist bei dessen Änderung anzupassen.

### 5. Mehrere Erklärungspflichtige ([§ 152 Abs. 4 AO](https://www.gesetze-im-internet.de/ao_1977/__152.html))

- **Geltendes Recht**: Festsetzung gegen einen, mehrere oder alle Pflichtigen nach Ermessen (§ 152 Abs. 4 S. 1 AO); bei Festsetzung gegen mehrere oder alle sind diese **Gesamtschuldner** (S. 2); bei gesonderter und einheitlicher Feststellung (§ 180 Abs. 1 S. 1 Nr. 2 a AO) vorrangig gegen die rechtsfähige Personenvereinigung bzw. bei nicht rechtsfähigen gegen die nach § 181 Abs. 2 S. 2 Nr. 4 AO Erklärungspflichtigen (S. 3).
- **Entwurf JStG 2026** (Art. 18 Nr. 12): zusätzlich **Vorrang** gegen die Person, gegen die die Steuer oder der Steuermessbetrag festgesetzt wird bzw. die die Steuer als Steuer- oder Entrichtungsschuldner anzumelden hat (auch bei Zerlegung), und bei **Zusammenveranlagung** zwingend Festsetzung gegen alle Erklärungspflichtigen.

### 6. Folgen über den Zuschlag hinaus

- **Zwangsgeld** zur Durchsetzung der Abgabe (§ 328, § 329 AO: bis 25.000 EUR), vorher Androhung.
- **Schätzung** der Besteuerungsgrundlagen (§ 162 AO), regelmäßig unter Vorbehalt der Nachprüfung; Einspruch nur mit Nachreichung der Erklärung erfolgversprechend.
- **Anlaufhemmung** der Festsetzungsfrist (§ 170 Abs. 2 S. 1 Nr. 1 AO) und steuerstrafrechtliches Risiko bei Nichtabgabe (§ 370 Abs. 1 Nr. 2 AO) — bei Unternehmen insbesondere USt-Jahreserklärung.

### 7. Rechtsbehelf gegen den Zuschlag

- **Einspruch** gegen die Festsetzung des Verspätungszuschlags (gesonderter Verwaltungsakt, auch wenn mit dem Steuerbescheid verbunden).
- Prüfprogramm: Fristberechnung korrekt? Ausnahme nach Abs. 3? Ermessen beim Abs.-1-Zuschlag ausgeübt und begründet? Bemessungsgrundlage (Vorauszahlungen abgezogen?) richtig? Höchstbetrag?
- Bei Muss-Zuschlägen bleibt Spielraum nur über Fristverlängerung (rückwirkend!) oder Billigkeit (§ 227 AO).

## Ausgabeformat

```
ERKLÄRUNGSFRISTEN / VERSPÄTUNGSZUSCHLAG — <Mandant> — <Datum> — Rechtsstand Oktober 2026

I.    Erklärung
      Steuerart / VZ:                 <ESt 2025 / …>
      Beraten (§ 149 Abs. 3 AO):      [ja / nein]
      Vorabanforderung (§ 149 Abs. 4): [nein / ja, Frist …]
      Maßgebliche Frist:              <Datum, ggf. § 108 Abs. 3 AO>

II.   Fristverlängerung (§ 109 AO)
      Antrag:                         [gestellt am … / zu stellen]
      Begründung (ohne Verschulden):  <…>

III.  Verspätungszuschlag (§ 152 AO)
      Grundlage:                      [Abs. 1 Ermessen / Abs. 2 Nr. 1, 2, 3 Muss]
      Ausnahme Abs. 3:                [Nr. … / keine]
      Verspätung (angefangene Monate): <…>
      Bemessung:                      <0,25 % × … EUR / mind. 25 EUR × … Monate>
      Festgesetzt / richtig:          <EUR / EUR>

IV.   Weitere Folgen
      Zwangsgeld / Schätzung:         <…>
      Strafrechtliches Risiko:        [keines / prüfen]

V.    Empfehlung
      <Einspruch / Antrag auf rückwirkende Fristverlängerung / Billigkeitsantrag>
```

## Beispiel (Urteilsstil, Kurzvermerk)

Die ESt-Erklärung 2025 des beratenen Mandanten wird am 15.04.2027 abgegeben; Fristverlängerung wurde nicht beantragt. Die Frist des § 149 Abs. 3 AO endete am Montag, 01.03.2027, weil der 28.02.2027 ein Sonntag ist (§ 108 Abs. 3 AO). Die Erklärung bezieht sich auf ein Kalenderjahr und wurde nicht binnen 14 Monaten nach Ablauf des Kalenderjahres abgegeben, denn diese Frist endete ebenfalls mit Ablauf des 01.03.2027. Die 19-Monats-Frist des § 152 Abs. 2 Nr. 2 AO gilt nur für Land- und Forstwirte mit abweichendem Wirtschaftsjahr und ist hier nicht einschlägig. Eine Ausnahme nach § 152 Abs. 3 AO liegt nicht vor, weil eine Abschlusszahlung von 4.000 EUR festgesetzt wird. Der Verspätungszuschlag ist daher nach § 152 Abs. 2 Nr. 1 AO **zwingend** festzusetzen; ein Einspruch mit der Rüge fehlender Ermessenserwägungen geht ins Leere. Bemessung nach § 152 Abs. 5 S. 2 AO: zwei angefangene Monate, 0,25 % × 4.000 EUR = 10 EUR je Monat, mindestens aber 25 EUR je Monat, insgesamt 50 EUR. Angreifbar bleibt nur die Grundlage: Konnte der Mandant die Frist **ohne Verschulden** (auch des Beraters) nicht einhalten, ist rückwirkende Fristverlängerung nach § 109 Abs. 2 AO zu beantragen; sie beseitigt den Muss-Zuschlag (§ 152 Abs. 3 Nr. 1 AO).

## Risiken / typische Fehler

- **Corona-Fristen weiter angewendet** — Art. 97 § 36 EGAO gilt letztmals für VZ 2024; VZ 2025 beraten endet am 01.03.2027.
- **Wochenend-Verschiebung falsch** — § 108 Abs. 3 AO auf das gesetzliche Fristende anwenden (VZ 2026 nicht beraten: 02.08.2027).
- **Vorabanforderung übersehen** — die angeordnete Frist löst den Muss-Zuschlag nach § 152 Abs. 2 Nr. 3 AO aus.
- **Fristverlängerung zu spät oder unbegründet** — im beratenen Fall nur ohne Verschulden; Kanzleiüberlastung reicht nicht (§ 109 Abs. 2 AO).
- **Ermessen beim Abs.-1-Zuschlag nicht gerügt** — formelhafte Festsetzung ohne Abwägung ist angreifbar; beim Muss-Zuschlag nach Abs. 2 gibt es dagegen kein Ermessen.
- **19-Monats-Frist auf beratene Fälle angewendet** — sie gilt nur für Land- und Forstwirte mit abweichendem Wirtschaftsjahr (§ 152 Abs. 2 Nr. 2 i. V. m. § 149 Abs. 2 S. 2 AO); beratene Fälle fallen unter die 14 Monate.
- **Bemessung ohne Abzug der Vorauszahlungen** — bei Jahreserklärungen ist die Abschlusszahlung maßgeblich (§ 152 Abs. 5 S. 2 AO).
- **Entwurf JStG 2026 als geltendes Recht behandelt** — die Neufassung des § 152 Abs. 4 AO ist nicht verabschiedet.
- **Nichtabgabe als bloßes Fristproblem behandelt** — bei Unternehmen Strafbarkeitsrisiko (§ 370 Abs. 1 Nr. 2 AO).

## Quellen

### Statute

- [§ 149 AO](https://www.gesetze-im-internet.de/ao_1977/__149.html), [§ 109 AO](https://www.gesetze-im-internet.de/ao_1977/__109.html), [§ 108 AO](https://www.gesetze-im-internet.de/ao_1977/__108.html), [§ 152 AO](https://www.gesetze-im-internet.de/ao_1977/__152.html), [§ 3 AO](https://www.gesetze-im-internet.de/ao_1977/__3.html)
- [§ 162 AO](https://www.gesetze-im-internet.de/ao_1977/__162.html), [§ 170 AO](https://www.gesetze-im-internet.de/ao_1977/__170.html), [§ 328 AO](https://www.gesetze-im-internet.de/ao_1977/__328.html), [§ 329 AO](https://www.gesetze-im-internet.de/ao_1977/__329.html), [§ 370 AO](https://www.gesetze-im-internet.de/ao_1977/__370.html), [§ 227 AO](https://www.gesetze-im-internet.de/ao_1977/__227.html)
- [Art. 97 § 36 EGAO](https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html) (Corona-Fristen, letztmals VZ 2024)
- [§ 114 FGO](https://www.gesetze-im-internet.de/fgo/__114.html)

### Gesetzgebung (nicht in Kraft)

- Regierungsentwurf JStG 2026, BT-Drs. 21/8283, Art. 18 Nr. 12 (§ 152 Abs. 4 AO)

### Verwaltungsanweisungen

- AEAO zu §§ 109, 149, 152 AO; jährliche gleich lautende Ländererlasse zu den Steuererklärungsfristen `[unverifiziert – prüfen]`

### Rechtsprechung

- BFH – IX R 35/24 (Ermessen beim Verspätungszuschlag; anhängig, Verhandlung 10.11.2026) `[unverifiziert – prüfen]`

### Literatur

- Rätke, in: Klein, AO, § 152 — aktuelle Auflage prüfen `[unverifiziert – prüfen]`
- Suchstring juris: „§ 152 Abs. 2 AO Verspätungszuschlag 14 Monate Ermessen Vorabanforderung"
