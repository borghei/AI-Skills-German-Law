---
name: e-rechnung-vorsteuer
description: "E-Rechnungspflicht im inländischen B2B-Verkehr und Vorsteuerabzug – Begriffe E-Rechnung und sonstige Rechnung § 14 Abs. 1 S. 3–6 UStG (EN 16931: XRechnung, ZUGFeRD), Pflicht nach § 14 Abs. 2 S. 2 Nr. 1 UStG, Übergangsfristen § 27 Abs. 38 UStG (Ausstellungspflicht ab 01.01.2027 bei Vorjahresumsatz über 800.000 EUR, ab 01.01.2028 für alle), Empfangspflicht seit 2025, Ausnahmen (Kleinbetrag, Fahrausweis, Kleinunternehmer, steuerfreie Umsätze), Rechnungsangaben § 14 Abs. 4 UStG, Vorsteuerabzug § 15 Abs. 1 S. 1 Nr. 1 UStG und Rechnungsberichtigung, Gutschrift, Aufbewahrung acht Jahre § 14b UStG / § 147 AO und GoBD, unberechtigter Steuerausweis § 14c UStG, Gastronomie 7 % seit 2026 § 12 Abs. 2 Nr. 15 UStG. BMF-Schreiben vom 15.10.2024, 15.10.2025 und 15.10.2026. Rechtsstand Oktober 2026. Use when ein Unternehmen seine Rechnungsstellung auf 2027 umstellt, eine Eingangsrechnung auf Vorsteuerabzugsfähigkeit prüft oder in der Prüfung Vorsteuer wegen Rechnungsmängeln versagt wird."
language: de
provider_variants:
  - claude
  - gemini
  - openai
test: ./test.md
---

# /steuerrecht:e-rechnung-vorsteuer

> **Rechtsstand: Oktober 2026.** Die Empfangspflicht gilt seit 01.01.2025; die **Ausstellungspflicht beginnt am 01.01.2027** für Unternehmer mit einem Gesamtumsatz 2026 über 800.000 EUR und am 01.01.2028 für alle übrigen ([§ 27 Abs. 38 UStG](https://www.gesetze-im-internet.de/ustg_1980/__27.html)). Die Verwaltung hat ihre Auffassung in drei BMF-Schreiben niedergelegt (15.10.2024, 15.10.2025 und **15.10.2026**). Das Schreiben vom 15.10.2026 (III C 5 – S 7287-a/00019/021/017) ändert u. a. Abschn. 14.1, 14.11 und 15.11 UStAE; Geschäftszeichen, Rz. 27 und 28 sowie Abschn. 14.11 Abs. 2 S. 7 UStAE sind in einem Review gegen den Volltext abgeglichen; übrige Einzelheiten sind als `[unverifiziert – prüfen]` gekennzeichnet.

## Zweck

Ab 2027 ist eine Papier- oder PDF-Rechnung zwischen inländischen Unternehmern für viele Leistende **keine ordnungsgemäße Rechnung** mehr. Für den Leistungsempfänger steht damit der Vorsteuerabzug auf dem Spiel, für den Leistenden die Ordnungsmäßigkeit seiner Buchführung. Dieser Skill bestimmt, ob und ab wann ein Unternehmen E-Rechnungen ausstellen muss, prüft Eingangsrechnungen auf Format und Pflichtangaben und verteidigt den Vorsteuerabzug bei formellen Mängeln.

## Eingaben

- Unternehmen: Sitz (Inland?), Gesamtumsatz 2026 (§ 19 Abs. 2 UStG), Kleinunternehmer?, Branche, steuerfreie Umsätze
- Leistungsbeziehungen: B2B inländisch / B2C / grenzüberschreitend / öffentliche Auftraggeber
- Rechnungsformat und -kanal (XRechnung, ZUGFeRD-Profil, PDF, EDI, Portal), ERP-/Buchhaltungssystem
- Streitige Eingangsrechnung: Format, Angaben, Zeitpunkt, ggf. Berichtigung
- Prüfungssituation: Versagung der Vorsteuer? Für welche Zeiträume?

## Sub-Agent-Architektur

Ein **Pflicht-Prüfer** bestimmt für jeden Leistungstyp, ob E-Rechnungspflicht besteht und ab wann. Ein **Format-Prüfer** klassifiziert die Rechnung (E-Rechnung / sonstige Rechnung) und prüft die Pflichtangaben. Ein **Vorsteuer-Prüfer** bewertet Abzugsfähigkeit, Berichtigungsmöglichkeit und Rückwirkung. Ein **Archiv-Prüfer** prüft Aufbewahrung, GoBD und Datenzugriff.

## Ablauf

### 1. Begriffe ([§ 14 Abs. 1 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html))

- **E-Rechnung**: in einem **strukturierten elektronischen Format** ausgestellt, übermittelt und empfangen, das eine elektronische Verarbeitung ermöglicht (§ 14 Abs. 1 S. 3 UStG). Das Format muss der **europäischen Norm EN 16931** und ihrer Syntaxliste entsprechen (XRechnung; ZUGFeRD ab Profil EN 16931, nicht MINIMUM/BASIC-WL) oder zwischen den Parteien vereinbart sein, sofern die vollständige Extraktion der Pflichtangaben im Normformat möglich ist (§ 14 Abs. 1 S. 6 UStG).
- **Sonstige Rechnung**: Papier oder anderes elektronisches Format (PDF, Bild, E-Mail-Text) (§ 14 Abs. 1 S. 4 UStG).
- **Hybridformat** (ZUGFeRD): Maßgeblich ist der **strukturierte Teil**; Abweichungen zur Bilddarstellung gehen zulasten der Bilddarstellung (BMF) `[unverifiziert – prüfen]`.
- Zustimmung des Empfängers ist nur erforderlich, soweit keine Pflicht zur E-Rechnung besteht (§ 14 Abs. 1 S. 5 UStG) — **Empfangspflicht** im B2B seit 01.01.2025; ein E-Mail-Postfach genügt.

### 2. Pflicht und Ausnahmen ([§ 14 Abs. 2 S. 2 Nr. 1 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html))

- **Pflicht**: Leistung an einen anderen Unternehmer für dessen Unternehmen, wenn **leistender Unternehmer und Leistungsempfänger im Inland** (oder in Gebieten nach § 1 Abs. 3 UStG) **ansässig** sind.
- **Keine Pflicht**: Leistungen an Verbraucher (B2C), grenzüberschreitende Leistungen; steuerfreie Umsätze nach § 4 Nr. 8–29 UStG `[unverifiziert – prüfen]`; **Kleinbetragsrechnungen** bis 250 EUR (§ 33 UStDV) und **Fahrausweise** (§ 34 UStDV); **Kleinunternehmer** nach § 19 UStG (Rechnungsinhalt § 34a UStDV; Befreiung von der Ausstellungspflicht `[unverifiziert – prüfen]`) — sie müssen aber E-Rechnungen empfangen können.
- **Öffentliche Auftraggeber (B2G)**: eigene Pflichten nach E-Rechnungsverordnungen des Bundes und der Länder (XRechnung, Portale) — unabhängig von § 14 UStG.

### 3. Übergangsfristen ([§ 27 Abs. 38 UStG](https://www.gesetze-im-internet.de/ustg_1980/__27.html))

| Umsatz ausgeführt | Sonstige Rechnung (Papier/PDF) zulässig? |
|---|---|
| 2025 und 2026 | **ja** (Papier; andere elektronische Formate nur mit Zustimmung des Empfängers) — Rechnung bis 31.12.2026 |
| 2027 | nur, wenn der **Gesamtumsatz 2026 nicht über 800.000 EUR** lag; außerdem EDI-Verfahren mit Zustimmung (auch ohne Umsatzgrenze) — Rechnung bis 31.12.2027 |
| ab 2028 | **nein** — nur noch E-Rechnung |

- Der Gesamtumsatz bemisst sich nach § 19 Abs. 2 UStG; bei Organschaft auf Ebene des Organträgers `[unverifiziert – prüfen]`.
- **Praxis Oktober 2026**: Für Unternehmen über 800.000 EUR Umsatz bleiben rund zehn Wochen; Ausgangsrechnungsprozess, Stammdaten (Leitweg-ID, Bestellnummern) und Gutschriftenverfahren jetzt umstellen.

### 4. Pflichtangaben ([§ 14 Abs. 4 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html))

- Name/Anschrift beider Parteien, Steuernummer oder USt-IdNr., Ausstellungsdatum, fortlaufende Rechnungsnummer, Menge und Art der Lieferung bzw. Umfang und Art der Leistung, Leistungszeitpunkt, Entgelt nach Steuersätzen, Steuersatz und Steuerbetrag bzw. Hinweis auf Steuerbefreiung, ggf. Hinweis auf Steuerschuldnerschaft des Leistungsempfängers (§ 14a UStG).
- **Gastronomie**: Restaurant- und Verpflegungsdienstleistungen (ohne Getränke) unterliegen seit 01.01.2026 **dauerhaft 7 %** ([§ 12 Abs. 2 Nr. 15 UStG](https://www.gesetze-im-internet.de/ustg_1980/__12.html)) — Getränke 19 %; Aufteilung in der Rechnung, Pauschalangebote nach Verwaltungsvereinfachung aufteilen `[unverifiziert – prüfen]`.
- **Gutschrift** (§ 14 Abs. 2 S. 2 UStG): ebenfalls als E-Rechnung, wenn die Pflicht besteht; Bezeichnung „Gutschrift"; Widerspruch des Empfängers nimmt ihr die Rechnungswirkung. **Korrektur durch Gutschrift**: Nach Abschn. 14.11 Abs. 2 S. 7 UStAE i. d. F. des BMF-Schreibens vom 15.10.2026 kann eine E-Rechnung des Leistenden auch durch eine Gutschrift des Leistungsempfängers berichtigt werden, wenn dies **vorher vereinbart** ist und die Gutschrift eindeutig auf die zu berichtigende Rechnung Bezug nimmt.

### 5. Vorsteuerabzug ([§ 15 Abs. 1 S. 1 Nr. 1 UStG](https://www.gesetze-im-internet.de/ustg_1980/__15.html))

- Voraussetzung ist der Besitz einer Rechnung nach §§ 14, 14a UStG. Ab Geltung der Pflicht ist eine **sonstige Rechnung, wo eine E-Rechnung geschuldet ist, keine ordnungsgemäße Rechnung**.
- **Berichtigung**: Eine Rechnung, die die Mindestangaben enthält (Aussteller, Empfänger, Leistungsbeschreibung, Entgelt, gesondert ausgewiesene Steuer), kann berichtigt werden; die Berichtigung wirkt **auf den Zeitpunkt der ursprünglichen Rechnung zurück** (EuGH, Urt. v. 15.09.2016 – C-518/14 *Senatex* `[unverifiziert – prüfen]`). Die Übersendung einer E-Rechnung als Ersatz für eine im falschen Format ausgestellte Rechnung ist nach Verwaltungsauffassung als Berichtigung möglich `[unverifiziert – prüfen]`.
- **Materielle Voraussetzungen** können nach EuGH-Rspr. auch anders als durch eine ordnungsgemäße Rechnung nachgewiesen werden; darauf darf sich die Beratung nicht verlassen, wohl aber die Verteidigung in der Prüfung.
- **Unvollständige Rechnungen** nach dem BMF-Schreiben vom 15.10.2026: Abzug trotz einzelner fehlender Angaben unter bestimmten Bedingungen; nicht beanstandet werden bis 31.12.2026 ausgestellte E-Rechnungen, die den früheren Schreiben entsprechen `[unverifiziert – prüfen]`. Kein Bußgeld nach § 26a UStG allein wegen des Formats (Rz. 28).
- **Öffentlich-rechtliche Gebührenbescheide**, die zugleich Rechnung sind, dürfen bis **30.06.2030** als sonstige Rechnung erteilt werden (BMF-Schreiben vom 15.10.2026, Rz. 27).

### 6. Aufbewahrung und GoBD

- **Acht Jahre** für Rechnungen ([§ 14b UStG](https://www.gesetze-im-internet.de/ustg_1980/__14b.html)) und Buchungsbelege ([§ 147 Abs. 3 AO](https://www.gesetze-im-internet.de/ao_1977/__147.html)) seit 01.01.2025.
- E-Rechnung: im **Originalformat** (strukturierter Datensatz) aufbewahren; die zweite GoBD-Änderung (BMF vom 14.07.2025) lässt den strukturierten Teil genügen, eine zusätzliche Bilddatei nur, wenn sie zusätzliche buchungsrelevante Informationen enthält `[unverifiziert – prüfen]`. Unveränderbarkeit, Maschinenauswertbarkeit und Datenzugriff (§ 147 Abs. 6 AO) sicherstellen.

### 7. Risiken auf Ausstellerseite

- **Unberechtigter oder unrichtiger Steuerausweis** ([§ 14c UStG](https://www.gesetze-im-internet.de/ustg_1980/__14c.html)): Doppelversand (PDF und E-Rechnung mit identischem Inhalt) ist unschädlich, wenn es sich um dieselbe Rechnung handelt; bei abweichendem Inhalt droht Steuerschuld nach § 14c UStG `[unverifiziert – prüfen]`.
- Bußgeld bei Verstoß gegen die Rechnungsausstellungspflicht ([§ 26a UStG](https://www.gesetze-im-internet.de/ustg_1980/__26a.html)).
- Kundenbeziehungen: Leistungsempfänger werden ab 2027 Rechnungen im falschen Format zurückweisen und Zahlungen zurückhalten.

## Ausgabeformat

```
E-RECHNUNG / VORSTEUER — <Unternehmen> — <Datum> — Rechtsstand Oktober 2026

I.    Ausstellungspflicht
      Sitz / Ansässigkeit:            <Inland / …>
      Gesamtumsatz 2026 (§ 19 Abs. 2): <EUR — über / unter 800.000>
      Pflicht ab:                     [01.01.2027 / 01.01.2028 / keine (Ausnahme …)]
      Leistungsarten mit Ausnahme:    <B2C / Kleinbetrag / Fahrausweis / steuerfrei …>

II.   Format
      Ausgangsrechnungen:             [XRechnung / ZUGFeRD EN 16931 / PDF → umstellen]
      Gutschriftenverfahren:          <…>
      Empfang:                        [eingerichtet / Lücke]

III.  Eingangsrechnung (Einzelprüfung)
      Klassifikation:                 [E-Rechnung / sonstige Rechnung]
      Pflichtangaben § 14 Abs. 4:     [✓ / fehlt: …]
      Vorsteuerabzug § 15:            [✓ / gefährdet — Berichtigung anfordern]
      Rückwirkung der Berichtigung:   [✓ Mindestangaben vorhanden / ✗]

IV.   Aufbewahrung
      8 Jahre (§ 14b UStG, § 147 AO): [✓]
      GoBD / Datensatz im Original:   [✓ / ⚠️]

V.    Maßnahmen bis 31.12.2026:       <…>
```

## Beispiel (Gutachtenstil, verkürzt)

Die inländische B-GmbH (Gesamtumsatz 2026: 2,1 Mio. EUR) liefert im Januar 2027 Ware an die inländische K-KG und schickt eine PDF-Rechnung per E-Mail. Fraglich ist, ob K daraus die Vorsteuer abziehen kann. Leistender und Empfänger sind im Inland ansässige Unternehmer, die Leistung erfolgt für das Unternehmen der K; die Rechnung ist daher als E-Rechnung auszustellen (§ 14 Abs. 2 S. 2 Nr. 1 UStG). Die Übergangsregel des § 27 Abs. 38 Nr. 2 UStG greift nicht, weil der Gesamtumsatz der B im Vorjahr 800.000 EUR überstieg. Die PDF-Rechnung ist eine sonstige Rechnung und keine ordnungsgemäße Rechnung im Sinne des § 15 Abs. 1 S. 1 Nr. 1 UStG. Sie enthält aber die Mindestangaben und kann durch Übermittlung einer E-Rechnung mit Rückwirkung berichtigt werden. Ergebnis: K sollte die PDF zurückweisen und eine E-Rechnung anfordern; bis dahin ist der Vorsteuerabzug gefährdet.

## Risiken / typische Fehler

- **Übergangsfrist falsch angewendet** — für 2027 nur bei Vorjahresumsatz bis 800.000 EUR; maßgeblich ist der Gesamtumsatz 2026.
- **PDF als E-Rechnung behandelt** — eine PDF ist eine sonstige Rechnung; ZUGFeRD nur ab Profil EN 16931.
- **Vorsteuerabzug** aus formwidriger Rechnung geltend gemacht — ab Geltung der Pflicht Berichtigung einfordern; Rückwirkung nur bei Mindestangaben.
- **Gutschriften** nicht umgestellt — auch Gutschriften unterliegen der E-Rechnungspflicht; Rechnungsberichtigung per Gutschrift nur mit vorheriger Vereinbarung und eindeutiger Bezugnahme.
- **Ausnahmen überdehnt** — Kleinbetrag (250 EUR) und Fahrausweise ja, „Barverkauf an Unternehmer" über 250 EUR nein.
- **Gastronomie-Steuersatz** — 7 % nur für Speisen, Getränke 19 %; Mischrechnungen aufteilen.
- **Aufbewahrung nur als PDF-Ausdruck** — der strukturierte Datensatz ist das Original.
- **BMF-Schreiben vom 15.10.2026 ungeprüft zitiert** — Einzelheiten vor Beratung im Volltext prüfen.

## Quellen

### Statute

- [§ 12 UStG](https://www.gesetze-im-internet.de/ustg_1980/__12.html), [§ 14 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html), [§ 14a UStG](https://www.gesetze-im-internet.de/ustg_1980/__14a.html), [§ 14b UStG](https://www.gesetze-im-internet.de/ustg_1980/__14b.html), [§ 14c UStG](https://www.gesetze-im-internet.de/ustg_1980/__14c.html), [§ 15 UStG](https://www.gesetze-im-internet.de/ustg_1980/__15.html), [§ 19 UStG](https://www.gesetze-im-internet.de/ustg_1980/__19.html), [§ 26a UStG](https://www.gesetze-im-internet.de/ustg_1980/__26a.html), [§ 27 UStG](https://www.gesetze-im-internet.de/ustg_1980/__27.html)
- Umsatzsteuer-Durchführungsverordnung: [§ 33](https://www.gesetze-im-internet.de/ustdv_1980/__33.html), [§ 34](https://www.gesetze-im-internet.de/ustdv_1980/__34.html), [§ 34a](https://www.gesetze-im-internet.de/ustdv_1980/__34a.html)
- [§ 147 AO](https://www.gesetze-im-internet.de/ao_1977/__147.html)

### Verwaltungsanweisungen

- BMF-Schreiben vom 15.10.2024 und 15.10.2025 zur obligatorischen E-Rechnung `[unverifiziert – prüfen]` (GZ im BStBl nachschlagen)
- BMF-Schreiben vom 15.10.2026, III C 5 – S 7287-a/00019/021/017: https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/Umsatzsteuer-Anwendungserlass/2026-10-15-obligatorische-elektronische-rechnung.pdf
- BMF, GoBD, zweite Änderung vom 14.07.2025 `[unverifiziert – prüfen]`; UStAE Abschn. 14.1–14.11, 15.2a, 15.11

### Rechtsprechung

- EuGH, Urt. v. 15.09.2016 – C-518/14 (Senatex; Rückwirkung der Rechnungsberichtigung) `[unverifiziert – prüfen]`

### Literatur

- Suchstring juris/Beck-Online: „E-Rechnung § 27 Abs. 38 UStG Vorsteuerabzug sonstige Rechnung Berichtigung"
