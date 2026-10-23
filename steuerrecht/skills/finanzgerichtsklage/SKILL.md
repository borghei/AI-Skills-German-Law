---
name: finanzgerichtsklage
description: "Klage vor dem Finanzgericht nach der FGO – Klagearten §§ 40, 41 FGO, Vorverfahren § 44, Sprungklage § 45, Untätigkeitsklage § 46, Klagefrist von einem Monat § 47 FGO (Jahresfrist nach Allgemeinverfügung § 367 Abs. 2b AO), elektronische Einreichungspflicht § 52d FGO, Muss-Inhalt § 65, Präklusion §§ 65 Abs. 2, 79b FGO und § 76 Abs. 3 FGO, Änderungsbescheid im Prozess § 68, Videoverhandlung (§ 91a a. F. der FGO seit 19.07.2024 aufgehoben), Nichtzulassungsbeschwerde und Revision §§ 115 ff. FGO, Kosten (GKG-Mindeststreitwert 1.500 EUR, KV GKG Nr. 6110). Rechtsstand Oktober 2026. Use when nach einer Einspruchsentscheidung Klage zum Finanzgericht erhoben, vorbereitet oder gegen ein FG-Urteil vorgegangen werden soll."
language: de
provider_variants:
  - claude
  - gemini
  - openai
test: ./test.md
---

# /steuerrecht:finanzgerichtsklage

> **Rechtsstand: Oktober 2026.** Die FGO wurde zuletzt durch das 9. Gesetz zur Änderung des Steuerberatungsrechts vom 29.06.2026 (BGBl. 2026 I Nr. 197) geändert; deren Inhalt für das Klageverfahren ist hier **nicht ausgewertet** `[unverifiziert – prüfen]`. Entwurf JStG 2026 (BT-Drs. 21/8283, nicht verabschiedet): Neufassung der Klagebefugnis bei Feststellungsbescheiden für rechtsfähige Personenvereinigungen (§ 48 Abs. 1 FGO) und Zurückweisung von Masseneinsprüchen per Allgemeinverfügung (§ 367 Abs. 2c AO), die die Jahresklagefrist auslöst.

## Zweck

Das Finanzgericht ist die einzige Tatsacheninstanz der Finanzgerichtsbarkeit; der BFH prüft nur Rechtsfragen. Was vor dem FG nicht vorgetragen und bewiesen wird, ist in der Revision verloren. Dieser Skill prüft Zulässigkeit (Klageart, Vorverfahren, Frist, Form, Klagebefugnis), strukturiert die Klagebegründung entlang Amtsermittlung und Mitwirkungslast und steuert Kosten, Termin und Rechtsmittel.

## Eingaben

- Einspruchsentscheidung (Datum, Bekanntgabeweg, Rechtsbehelfsbelehrung) bzw. Untätigkeit seit Einspruch vom …
- Angefochtene Bescheide (Art, Jahr, Betrag), zwischenzeitliche Änderungsbescheide
- Streitpunkte, Beweismittel (Urkunden, Zeugen, Sachverständige), Präklusionsfristen aus dem Einspruchsverfahren (§ 364b AO)
- Bevollmächtigter (Rechtsanwalt / Steuerberater → beA/beSt-Pflicht)
- Streitwert (Differenz der festgesetzten Steuer zum begehrten Betrag), Kostenrisiko
- Laufende AdV

## Sub-Agent-Architektur

Ein **Zulässigkeits-Prüfer** klärt Klageart, Vorverfahren und Klagebefugnis. Ein **Fristen-Prüfer** berechnet Bekanntgabe und Klagefrist deterministisch und hält alle richterlichen Ausschlussfristen nach. Ein **Begründungs-Prüfer** ordnet den Vortrag nach Tatsachen, Beweisangeboten und Rechtsausführungen und prüft die Feststellungslast. Ein **Kosten-Prüfer** berechnet Streitwert, Gerichts- und Anwaltskosten und die Erstattungsfähigkeit der Vorverfahrenskosten.

## Ablauf

### 1. Klageart ([§ 40 FGO](https://www.gesetze-im-internet.de/fgo/__40.html), [§ 41 FGO](https://www.gesetze-im-internet.de/fgo/__41.html))

- **Anfechtungsklage**: Aufhebung oder Änderung eines Verwaltungsakts (Steuer-, Haftungs-, Feststellungsbescheid); Änderung eines Geldbetrags nach § 100 Abs. 2 FGO.
- **Verpflichtungsklage**: Erlass eines abgelehnten oder unterlassenen Verwaltungsakts (Erlass, Stundung, Billigkeitsmaßnahme, verbindliche Auskunft); bei Ermessen nur Bescheidung (§ 101 FGO) und eingeschränkte Kontrolle nach [§ 102 FGO](https://www.gesetze-im-internet.de/fgo/__102.html).
- **Sonstige Leistungsklage**: z. B. Akteneinsicht, Unterlassung.
- **Feststellungsklage** (§ 41 FGO): subsidiär; Nichtigkeit eines Verwaltungsakts.
- **Klagebefugnis**: Geltendmachung einer Rechtsverletzung (§ 40 Abs. 2 FGO); bei Feststellungsbescheiden Sonderregel [§ 48 FGO](https://www.gesetze-im-internet.de/fgo/__48.html).

### 2. Vorverfahren, Sprungklage, Untätigkeitsklage

- **Vorverfahren** ([§ 44 FGO](https://www.gesetze-im-internet.de/fgo/__44.html)): Klage grundsätzlich erst nach ganz oder teilweise erfolglosem Einspruch.
- **Sprungklage** ([§ 45 FGO](https://www.gesetze-im-internet.de/fgo/__45.html)): ohne Einspruch, wenn die Behörde innerhalb **eines Monats** nach Zustellung der Klageschrift **zustimmt**; ohne Zustimmung wird die Klage als Einspruch behandelt. Sinnvoll bei reinen Rechtsfragen.
- **Untätigkeitsklage** ([§ 46 FGO](https://www.gesetze-im-internet.de/fgo/__46.html)): wenn über den Einspruch ohne Mitteilung eines zureichenden Grundes in angemessener Frist nicht entschieden wurde; grundsätzlich **nicht vor Ablauf von sechs Monaten** seit Einlegung. Das Gericht kann das Verfahren aussetzen und der Behörde eine Frist setzen.

### 3. Klagefrist ([§ 47 FGO](https://www.gesetze-im-internet.de/fgo/__47.html))

- **Ein Monat** nach Bekanntgabe der Einspruchsentscheidung (§ 47 Abs. 1 FGO); bei Sprungklage ab Bekanntgabe des Verwaltungsakts.
- Bekanntgabe: Post vier Tage nach Aufgabe (§ 122 Abs. 2 AO), Datenabruf vier Tage nach Bereitstellung (§ 122a Abs. 4 AO); Einspruchsentscheidungen werden in der Praxis häufig förmlich zugestellt — dann gilt das Zustellungsdatum.
- Fristwahrend auch die Anbringung bei der Behörde, die den Verwaltungsakt erlassen hat (§ 47 Abs. 2 FGO).
- Fristberechnung: § 54 Abs. 2 FGO i. V. m. § 222 ZPO, §§ 187 ff. BGB; Fristende am Wochenende/Feiertag → nächster Werktag.
- **Allgemeinverfügung** (§ 367 Abs. 2b AO): Klagefrist **ein Jahr** nach Bekanntgabe der Allgemeinverfügung (§ 367 Abs. 2b S. 5 AO). Entwurf JStG 2026: gleiche Folge für Zurückweisungen nach dem geplanten § 367 Abs. 2c AO.
- Fehlende/unrichtige Rechtsbehelfsbelehrung → Jahresfrist (§ 55 Abs. 2 FGO). Wiedereinsetzung: § 56 FGO (zwei Wochen nach Wegfall des Hindernisses).

```bash
# Einspruchsentscheidung zugestellt am 06.10.2026 → Klagefrist (1 Monat, § 54 FGO, § 222 ZPO)
python -m scripts.legal_calc.cli frist --ereignis 06.10.2026 --menge 1 --einheit monate --land BY
```

### 4. Form und Inhalt

- **Schriftlich** oder zur Niederschrift (§ 64 FGO); für Rechtsanwälte, Behörden und vertretungsberechtigte Personen mit sicherem Übermittlungsweg (Steuerberater: beSt) **elektronische Einreichung Pflicht** ([§ 52d FGO](https://www.gesetze-im-internet.de/fgo/__52d.html)); Papierklage ist dann unwirksam, außer bei vorübergehender technischer Unmöglichkeit mit unverzüglicher Glaubhaftmachung.
- **Muss-Inhalt** ([§ 65 Abs. 1 S. 1 FGO](https://www.gesetze-im-internet.de/fgo/__65.html)): Kläger, Beklagter (Finanzamt), Gegenstand des Klagebegehrens; bei Anfechtungsklage auch Verwaltungsakt und Einspruchsentscheidung. **Soll-Inhalt**: bestimmter Antrag, Tatsachen und Beweismittel.
- Fehlt Muss-Inhalt, setzt der Vorsitzende eine Frist **mit ausschließender Wirkung** (§ 65 Abs. 2 S. 2 FGO) — Versäumung führt zur Unzulässigkeit.
- Vertretungszwang besteht vor dem FG nicht, wohl aber vor dem **BFH** ([§ 62 Abs. 4 FGO](https://www.gesetze-im-internet.de/fgo/__62.html)).

### 5. Verfahren vor dem FG

- **Amtsermittlung** ([§ 76 FGO](https://www.gesetze-im-internet.de/fgo/__76.html)) bei Mitwirkungspflicht der Beteiligten; Verletzung der Mitwirkungspflicht reduziert die Ermittlungspflicht des Gerichts. Präklusion aus dem Einspruch (§ 364b AO) kann übernommen werden (§ 76 Abs. 3 FGO).
- **Ausschlussfrist** nach [§ 79b FGO](https://www.gesetze-im-internet.de/fgo/__79b.html) für Tatsachen und Beweismittel — Fristen strikt einhalten; verspäteter Vortrag kann zurückgewiesen werden.
- **Änderungsbescheid im Prozess** ([§ 68 FGO](https://www.gesetze-im-internet.de/fgo/__68.html)): wird automatisch Gegenstand des Verfahrens; kein neuer Einspruch nötig (und nicht zulässig).
- **Erörterungstermin** (§ 79 Abs. 1 S. 2 Nr. 1 FGO): Gelegenheit zur tatsächlichen Verständigung oder Abhilfezusage.
- **Mündliche Verhandlung**, auch per Bild- und Tonübertragung: Der frühere § 91a der FGO ist durch das Gesetz zur Förderung des Einsatzes von Videokonferenztechnik (Art. 12, in Kraft 19.07.2024) **aufgehoben**; für den Erörterungstermin verweist § 79 Abs. 1 S. 2 Nr. 1 FGO nun auf § 128a ZPO, für die mündliche Verhandlung gilt § 128a ZPO über § 155 FGO `[unverifiziert – prüfen]`. Alte Kommentarstellen zu § 91a a. F. nicht mehr zitieren; Verzicht (§ 90 Abs. 2 FGO); **Gerichtsbescheid** (§ 90a FGO) — binnen eines Monats Antrag auf mündliche Verhandlung, sonst wirkt er als Urteil.
- **Feststellungslast**: Steuerbegründende Tatsachen trägt das Finanzamt, steuermindernde der Kläger.
- **AdV** parallel nach § 69 Abs. 3 FGO (`/steuerrecht:aussetzung-der-vollziehung`).

### 6. Urteil und Rechtsmittel

- Urteil auf Aufhebung/Änderung ([§ 100 FGO](https://www.gesetze-im-internet.de/fgo/__100.html)); bei aufwendiger Berechnung überlässt das Gericht die Berechnung dem Finanzamt (§ 100 Abs. 2 S. 2 FGO).
- **Revision** nur bei Zulassung ([§ 115 FGO](https://www.gesetze-im-internet.de/fgo/__115.html)): grundsätzliche Bedeutung, Fortbildung des Rechts / Sicherung einheitlicher Rspr., Verfahrensmangel.
- **Nichtzulassungsbeschwerde** ([§ 116 FGO](https://www.gesetze-im-internet.de/fgo/__116.html)): Einlegung beim BFH binnen **eines Monats**, Begründung binnen **zwei Monaten** nach Zustellung des Urteils (Verlängerung um einen Monat möglich). Darlegungsanforderungen hoch; Vertretungszwang.
- **Revision** ([§ 120 FGO](https://www.gesetze-im-internet.de/fgo/__120.html)): ein Monat Einlegung, zwei Monate Begründung nach Zustellung des Urteils bzw. des Zulassungsbeschlusses.

### 7. Kosten

- **Streitwert**: Differenz zwischen festgesetzter und begehrter Steuer ([§ 52 GKG](https://www.gesetze-im-internet.de/gkg_2004/__52.html)); **Mindeststreitwert 1.500 EUR** (§ 52 Abs. 4 Nr. 1 GKG; nicht in Kindergeldsachen); vorläufige Gebühr nach dem Mindestwert (§ 52 Abs. 5 GKG).
- **Gerichtsgebühr**: Verfahren im Allgemeinen 4,0 (KV GKG Nr. 6110); Ermäßigung auf 2,0 bei Rücknahme oder Erledigung vor Schluss der mündlichen Verhandlung (KV GKG Nr. 6111).
- **Anwaltsgebühren**: Verfahrensgebühr 1,6 (VV RVG Nr. 3200), Terminsgebühr 1,2 (VV RVG Nr. 3202) — das FG-Verfahren wird gebührenrechtlich wie ein Berufungsverfahren behandelt (Vorbem. 3.2.1 VV RVG).
- **Vorverfahrenskosten** erstattungsfähig nur, wenn das Gericht die Zuziehung eines Bevollmächtigten für das Vorverfahren für notwendig erklärt (§ 139 Abs. 3 S. 3 FGO) — Antrag stellen.

```bash
# Gerichtsgebühr (4,0) bei Streitwert 20.000 EUR — der Rechner beschriftet den Faktor generisch; maßgeblich ist KV GKG Nr. 6110
python -m scripts.legal_calc.cli gkg --wert 20000 --faktor 4.0
python -m scripts.legal_calc.cli rvg --wert 20000 --posten verfahren termin
```

Hinweis: Die `rvg`-Posten des Rechners bilden die erstinstanzlichen Sätze (1,3/1,2) ab; für das FG-Verfahren die Verfahrensgebühr mit 1,6 von Hand ansetzen.

## Ausgabeformat

```
FINANZGERICHTSKLAGE — <Mandant> ./. FA <…> — <Datum> — Rechtsstand Oktober 2026

I.    Zulässigkeit
      Klageart (§§ 40, 41 FGO):       [Anfechtung / Verpflichtung / …]
      Vorverfahren (§ 44 FGO):        [Einspruchsentscheidung vom … / Sprungklage § 45 / Untätigkeit § 46]
      Klagebefugnis:                  [✓ / § 48 FGO]
      Klagefrist (§ 47 FGO):          <Bekanntgabe/Zustellung — Fristende (Rechner)>
      Form (§§ 52d, 64, 65 FGO):      [elektronisch über beA/beSt]

II.   Anträge
      <Bescheid vom … in Gestalt der Einspruchsentscheidung vom … dahin ändern, dass …>
      <Zuziehung eines Bevollmächtigten für das Vorverfahren für notwendig erklären>
      <hilfsweise Revision zulassen>

III.  Begründung
      Sachverhalt / Beweisangebote:   <…>
      Rechtliche Würdigung:           <…>
      Feststellungslast:              <…>
      Präklusionsrisiken (§§ 65, 79b FGO, § 364b AO): <…>

IV.   Parallel: AdV (§ 69 Abs. 3 FGO): [beantragt / nicht erforderlich]

V.    Kosten
      Streitwert:                     <EUR (mind. 1.500)>
      Gerichtsgebühr KV 6110 (4,0):   <EUR (Rechner)>
      RVG (1,6 + 1,2):                <EUR>

VI.   Rechtsmittelplanung:            <NZB / Revision — Fristen>
```

## Beispiel (Urteilsstil, Klagezulässigkeit)

Die Einspruchsentscheidung zur ESt 2024 wurde am Dienstag, 06.10.2026, förmlich zugestellt. Die Klagefrist von einem Monat (§ 47 Abs. 1 FGO) endet mit Ablauf des 06.11.2026, einem Freitag (§ 54 Abs. 2 FGO i. V. m. § 222 Abs. 1 ZPO, § 188 Abs. 2 BGB; Rechner). Die Klage wird durch die Steuerberaterin erhoben; sie ist nach § 52d FGO als elektronisches Dokument über das beSt einzureichen. Streitig sind nicht anerkannte Werbungskosten von 12.000 EUR; bei einem Grenzsteuersatz von 42 % liegt der Streitwert bei rund 5.040 EUR zuzüglich Solidaritätszuschlag, also über dem Mindeststreitwert von 1.500 EUR. Zugleich ist zu beantragen, die Zuziehung der Bevollmächtigten für das Vorverfahren für notwendig zu erklären (§ 139 Abs. 3 S. 3 FGO).

## Risiken / typische Fehler

- **Klagefrist versäumt** — ein Monat ab Bekanntgabe/Zustellung; Wiedereinsetzung nur binnen zwei Wochen und bei fehlendem Verschulden (§ 56 FGO), Beraterverschulden wird zugerechnet.
- **Elektronische Einreichungspflicht missachtet** — Papier- oder Faxklage eines Rechtsanwalts oder Steuerberaters ist unwirksam (§ 52d FGO).
- **Ausschlussfrist nach § 65 Abs. 2 oder § 79b FGO versäumt** — Unzulässigkeit oder Zurückweisung des Vortrags; Fristen sofort notieren.
- **Neuer Einspruch gegen Änderungsbescheid im Prozess** — unzulässig; der Änderungsbescheid wird nach § 68 FGO Verfahrensgegenstand.
- **Untätigkeitsklage zu früh** — vor Ablauf von sechs Monaten nur bei besonderen Umständen.
- **Vortrag für die Revision aufgespart** — der BFH ist an die Tatsachenfeststellungen des FG gebunden (§ 118 Abs. 2 FGO).
- **NZB-Begründung unzureichend** — Zulassungsgründe müssen dargelegt, nicht nur behauptet werden; Vertretungszwang beim BFH.
- **Vorverfahrenskosten verschenkt** — Antrag nach § 139 Abs. 3 S. 3 FGO vergessen.
- **Allgemeinverfügung übersehen** — die Jahresfrist läuft auch, wenn der Mandant nichts davon erfährt.

## Quellen

### Statute

- [§ 40 FGO](https://www.gesetze-im-internet.de/fgo/__40.html), [§ 41 FGO](https://www.gesetze-im-internet.de/fgo/__41.html), [§ 44 FGO](https://www.gesetze-im-internet.de/fgo/__44.html), [§ 45 FGO](https://www.gesetze-im-internet.de/fgo/__45.html), [§ 46 FGO](https://www.gesetze-im-internet.de/fgo/__46.html), [§ 47 FGO](https://www.gesetze-im-internet.de/fgo/__47.html), [§ 48 FGO](https://www.gesetze-im-internet.de/fgo/__48.html)
- [§ 52d FGO](https://www.gesetze-im-internet.de/fgo/__52d.html), [§ 54 FGO](https://www.gesetze-im-internet.de/fgo/__54.html), [§ 55 FGO](https://www.gesetze-im-internet.de/fgo/__55.html), [§ 56 FGO](https://www.gesetze-im-internet.de/fgo/__56.html), [§ 62 FGO](https://www.gesetze-im-internet.de/fgo/__62.html), [§ 64 FGO](https://www.gesetze-im-internet.de/fgo/__64.html), [§ 65 FGO](https://www.gesetze-im-internet.de/fgo/__65.html)
- [§ 68 FGO](https://www.gesetze-im-internet.de/fgo/__68.html), [§ 76 FGO](https://www.gesetze-im-internet.de/fgo/__76.html), [§ 79b FGO](https://www.gesetze-im-internet.de/fgo/__79b.html), [§ 79 FGO](https://www.gesetze-im-internet.de/fgo/__79.html), [§ 90a FGO](https://www.gesetze-im-internet.de/fgo/__90a.html), [§ 155 FGO](https://www.gesetze-im-internet.de/fgo/__155.html), [§ 128a ZPO](https://www.gesetze-im-internet.de/zpo/__128a.html)
- [§ 100 FGO](https://www.gesetze-im-internet.de/fgo/__100.html), [§ 102 FGO](https://www.gesetze-im-internet.de/fgo/__102.html), [§ 115 FGO](https://www.gesetze-im-internet.de/fgo/__115.html), [§ 116 FGO](https://www.gesetze-im-internet.de/fgo/__116.html), [§ 118 FGO](https://www.gesetze-im-internet.de/fgo/__118.html), [§ 120 FGO](https://www.gesetze-im-internet.de/fgo/__120.html), [§ 139 FGO](https://www.gesetze-im-internet.de/fgo/__139.html)
- [§ 367 AO](https://www.gesetze-im-internet.de/ao_1977/__367.html) (Allgemeinverfügung Abs. 2b), [§ 122 AO](https://www.gesetze-im-internet.de/ao_1977/__122.html), [§ 122a AO](https://www.gesetze-im-internet.de/ao_1977/__122a.html)
- [§ 52 GKG](https://www.gesetze-im-internet.de/gkg_2004/__52.html), [§ 222 ZPO](https://www.gesetze-im-internet.de/zpo/__222.html)

### Gesetzgebung

- 9. Gesetz zur Änderung des Steuerberatungsrechts sowie im Steuerrecht vom 29.06.2026, BGBl. 2026 I Nr. 197 (ändert u. a. die FGO; Inhalt prüfen) `[unverifiziert – prüfen]`
- Regierungsentwurf JStG 2026, BT-Drs. 21/8283, Art. 23 (§ 48 Abs. 1 FGO) und Art. 18 Nr. 18 (§ 367 Abs. 2c AO) — nicht in Kraft

### Rechtsprechung

- Zur Darlegung der Zulassungsgründe in der NZB und zur Wirkung des § 52d FGO: Az. vor Zitat in juris ermitteln (Suchstring: „§ 52d FGO Steuerberater beSt Formunwirksamkeit") `[unverifiziert – prüfen]`

### Literatur

- Gräber, FGO, 10. Aufl. 2024 `[unverifiziert – prüfen]` (Auflage prüfen)
- Seer, in: Tipke/Kruse, AO/FGO, §§ 40 ff. FGO `[unverifiziert – prüfen]`
