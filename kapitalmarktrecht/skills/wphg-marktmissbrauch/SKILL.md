---
name: wphg-marktmissbrauch
description: "Prüfung von Insiderhandel und Marktmanipulation nach MAR (VO (EU) 596/2014) iVm WpHG – Insiderinformation Art. 7, Verbote Art. 14/15, Ausnahme Legitimate Behaviour Art. 9, Ad-hoc-Publizität Art. 17 (inkl. Selbstaufschub Abs. 4), Insiderliste Art. 18, Directors' Dealings Art. 19, Sanktionen Art. 30 MAR und §§ 38, 119 WpHG. Use when ein Emittent vor einer transaktions- oder informationsbedingten Marktmissbrauchsfrage steht (M&A, Restrukturierung, vorzeitige Bilanzdaten, Vorstandsgeschäfte)."
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

# /kapitalmarktrecht:wphg-marktmissbrauch

## Zweck

Der Skill prüft die zentralen Marktmissbrauchstatbestände nach der **Marktmissbrauchsverordnung (VO (EU) 596/2014 — MAR)**, insbesondere das Verbot des Insiderhandels (Art. 14 MAR), das Verbot der Marktmanipulation (Art. 15 MAR), die Ad-hoc-Publizitätspflicht (Art. 17 MAR) einschließlich des Selbstaufschubs nach Art. 17 IV, die Pflicht zur Insiderliste (Art. 18 MAR) und die Meldepflicht für Eigengeschäfte von Führungskräften (Directors' Dealings, Art. 19 MAR). Er klärt die Sanktionsfolgen nach Art. 30 MAR sowie §§ 119, 38 WpHG.

## Eingaben

- Emittent (idR börsennotierte AG / SE) und ISIN / Handelsplatz (regulierter Markt iSv § 32 BörsG, Freiverkehr, MTF)
- konkrete Information / Vorhaben (M&A, Restrukturierung, Bilanzkennzahlen, Vorstandswechsel, behördliche Verfahren)
- Stand der Information (Verhandlungsstufe, Term Sheet, LOI, Vertragsschluss, Closing)
- bekannter Personenkreis (Vorstand, Aufsichtsrat, Berater) und ggf. bestehende Insiderliste
- Zweck der Anfrage: präventive Compliance-Beratung, Aufschub-Entscheidung, Reaktion auf BaFin-Verfahren, Verteidigung gegen Anlegerklagen

## Sub-Agent-Architektur

Researcher liefert MAR-Artikel, WpHG-Sanktionsnormen, EuGH-Rspr. (Geltl/Daimler zur "präzisen Information" in mehrstufigen Prozessen, Lafonta zur Kursrelevanz), BGH-Rspr. (IKB, EM.TV) und BaFin-Emittentenleitfaden. Drafter prüft im Gutachtenstil, entwirft ggf. Ad-hoc-Mitteilung und Aufschub-Dokumentation. Reviewer prüft, ob Aufschub Art. 17 IV dokumentiert ist und die Insiderliste angesprochen wurde.

## Ablauf

### 1. Anwendungsbereich (Art. 2 MAR)

MAR gilt für Finanzinstrumente, die zum Handel an einem geregelten Markt (Art. 4 I Nr. 21 MiFID II) zugelassen sind oder für die ein Antrag gestellt wurde, sowie für Finanzinstrumente, die an einem MTF/OTF gehandelt werden (Art. 2 I MAR). Bei reinem Freiverkehr außerhalb MTF (open market in engem Sinne) ist die Anwendung im Einzelfall zu prüfen.

### 2. Insiderinformation (Art. 7 MAR) – vier Kriterien

| Kriterium | Inhalt |
|---|---|
| **Präzise** | Konkreter Umstand, der eingetreten ist oder bei dem mit hinreichender Wahrscheinlichkeit angenommen werden kann, dass er eintreten wird (Art. 7 II MAR; EuGH, **Geltl/Daimler**, Rs. C-19/11 `[unverifiziert]`) |
| **Nicht öffentlich** | Information ist (noch) nicht der allgemeinen Anlegeröffentlichkeit zugänglich |
| **Direkter/indirekter Bezug** | Bezug zu einem oder mehreren Emittenten oder einem oder mehreren Finanzinstrumenten |
| **Kursrelevant** | Geeignet, im Falle des öffentlichen Bekanntwerdens den Kurs erheblich zu beeinflussen ("verständiger Anleger"-Maßstab; EuGH, **Lafonta**, Rs. C-628/13 `[unverifiziert]` — Richtungsangabe nicht erforderlich) |

**Zwischenschritte** in gestreckten Sachverhalten (Verhandlungsstadien einer M&A-Transaktion) können bereits Insiderinformation sein, wenn der einzelne Zwischenschritt selbst die vier Kriterien erfüllt (Geltl-Linie).

### 3. Verbot des Insiderhandels (Art. 14 iVm Art. 8 MAR)

Verboten: (a) Erwerb/Veräußerung unter Verwendung von Insiderinformationen für eigene oder fremde Rechnung; (b) Empfehlung oder Verleitung Dritter; (c) unrechtmäßige Offenlegung (Art. 10 MAR).

**Legitimate Behaviour (Art. 9 MAR):** Bestimmte Verhaltensweisen sind ausdrücklich kein Insidergeschäft, namentlich Geschäfte aufgrund eines vor Erlangen der Insiderinformation gefassten und dokumentierten Plans (Art. 9 III) sowie der **klassische M&A-Erwerbsprozess** (Art. 9 IV: Geschäfte zur Durchführung einer übernahmebezogenen Akquisition, deren Insiderinformation gerade in der Übernahme selbst besteht — sog. Front Running im Rahmen der eigenen Übernahme bleibt erlaubt, soweit Art. 9 IV-Voraussetzungen vorliegen).

### 4. Verbot der Marktmanipulation (Art. 15 iVm Art. 12 MAR)

Drei Haupt-Tatbestände: handelsgestützte Manipulation (Art. 12 I lit. a, b), informationsgestützte Manipulation (Art. 12 I lit. c — falsche oder irreführende Signale), Manipulation durch Benchmarks (Art. 12 I lit. d). Praxis-Beispiele: pump-and-dump, wash trades, spoofing, gezielte Pressemitteilungen ohne sachliche Grundlage.

### 5. Ad-hoc-Publizitätspflicht (Art. 17 MAR)

- **Art. 17 I MAR:** Der Emittent gibt **unverzüglich** Insiderinformationen bekannt, die ihn unmittelbar betreffen. „Unverzüglich" = ohne schuldhaftes Zögern, in der BaFin-Praxis idR innerhalb von Stunden, in komplexen Sachverhalten enger Bearbeitungspuffer.
- **Art. 17 IV MAR (Selbstaufschub):** Aufschub auf eigene Verantwortung zulässig, wenn **kumulativ**:
  1. **Berechtigtes Interesse** des Emittenten (z. B. laufende Verhandlungen, deren Ergebnis durch sofortige Veröffentlichung gefährdet würde — ESMA Guidelines on Delay of Disclosure of Inside Information).
  2. **Aufschub voraussichtlich nicht geeignet, die Öffentlichkeit irrezuführen** (kein Widerspruch zu bereits veröffentlichten Aussagen).
  3. **Vertraulichkeit der Insiderinformation gewährleistet** (Insiderliste, Need-to-know-Verteiler).

  Nach der Veröffentlichung ist die BaFin nach Art. 17 IV UAbs. 3 MAR über den Aufschub und seine Gründe zu informieren.

- **Dokumentation des Aufschubs** ist zwingend (Art. 4 I DurchführungsVO (EU) 2016/1055): Zeitpunkt der Entstehung der Insiderinformation, Zeitpunkt der Aufschub-Entscheidung, verantwortliche Personen, laufende Vertraulichkeitskontrolle.

### 6. Insiderliste (Art. 18 MAR)

Emittent (und in dessen Auftrag handelnde Personen) führt eine Insiderliste mit allen Personen, die Zugang zu Insiderinformationen haben. Format nach DurchführungsVO (EU) 2016/347. Aktualisierung **unverzüglich** bei Personen- oder Statusänderung. Aufbewahrung mindestens 5 Jahre nach Erstellung/Aktualisierung.

### 7. Directors' Dealings (Art. 19 MAR)

Führungskräfte (Vorstand, Aufsichtsrat sowie ihnen "eng verbundene Personen" iSv Art. 3 I Nr. 26 MAR) melden Eigengeschäfte mit Aktien/Schuldverschreibungen des Emittenten oder darauf bezogenen Derivaten **innerhalb von 3 Geschäftstagen** an Emittent und BaFin (Art. 19 I MAR), sobald ein Schwellenwert von 5.000 EUR/Kalenderjahr überschritten ist (Art. 19 VIII MAR; angehoben durch nationale Option in der WpHG-Erleichterungsverordnung möglich). Veröffentlichung durch Emittent unverzüglich.

**Geschlossene Zeiträume (Closed Periods, Art. 19 XI MAR):** 30 Kalendertage vor Veröffentlichung des Halbjahres- bzw. Jahresfinanzberichts dürfen Führungskräfte grundsätzlich keine Eigengeschäfte tätigen — Ausnahmen nach Art. 19 XII MAR (außergewöhnliche Umstände, vorbestimmte Programme).

### 8. Sanktionen

| Norm | Sanktion |
|---|---|
| Art. 30 MAR + § 120 WpHG | Verwaltungssanktion: natP bis 5 Mio. EUR bzw. dreifacher Gewinn; jurP bis 15 Mio. EUR / 15 % Jahresumsatz Konzern |
| § 119 WpHG | Ordnungswidrigkeit (Bußgeld) |
| § 38 WpHG | Strafvorschrift Insiderhandel / Manipulation – Freiheitsstrafe bis 5 Jahre (qualifiziert nach § 38 V WpHG) |
| §§ 826, 823 II BGB iVm § 38 WpHG / Art. 17 MAR | Anlegerschadensersatz – BGH-Linie IKB, EM.TV `[unverifiziert]` |
| BaFin Naming and Shaming, Art. 34 MAR | Veröffentlichung der Sanktion auf bafin.de |

### 9. Strafrechtliche Schwelle § 38 WpHG

Die strafrechtliche Sanktion setzt nach BGH-Rspr. einen wirtschaftlichen Vorteil bzw. ein bedeutendes Umsatzvolumen voraus; bei geringfügigen Verstößen verbleibt es bei der Ordnungswidrigkeit nach § 119 WpHG. Im Mandat: subjektiver Tatbestand (Vorsatz / Leichtfertigkeit) sorgfältig prüfen.

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Unmittelbar anwendbares Unionsrecht

- [VO (EU) 596/2014 (MAR)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596) – Art. 7, 8, 9, 10, 12, 14, 15, 17, 18, 19, 23, 30, 34
- DurchführungsVO (EU) 2016/1055 (Aufschub-Dokumentation)
- DurchführungsVO (EU) 2016/347 (Insiderliste)
- ESMA Guidelines on Delay of Disclosure of Inside Information (MAR/2016/1478)

### Deutsches Recht

- [§§ 33 ff. WpHG](https://www.gesetze-im-internet.de/wphg/__33.html) (Stimmrechtsmeldungen)
- [§ 38 WpHG](https://www.gesetze-im-internet.de/wphg/__38.html) (Strafvorschriften)
- [§ 119 WpHG](https://www.gesetze-im-internet.de/wphg/__119.html) (Bußgeldvorschriften)
- [§ 120 WpHG](https://www.gesetze-im-internet.de/wphg/__120.html) (Bußgeldhöhe)
- BaFin-Emittentenleitfaden Modul C (Marktmissbrauch / Ad-hoc-Publizität)

### Kommentare

- Klöhn, in: Klöhn, MAR, 1. Aufl. 2018, Art. 7 Rn. 1 ff.; Art. 17 Rn. 1 ff.
- Mülbert/Sajnovits, in: Assmann/Schneider/Mülbert, WpHG/MAR, 8. Aufl. 2024, Art. 7 MAR Rn. 1 ff.
- Pawlik, in: KapMRK (Schwark/Zimmer), 5. Aufl. 2020, Art. 17 MAR Rn. 1 ff.
- Just, in: Just/Voß/Ritz/Becker, WpHG, 1. Aufl. 2015, § 38 Rn. 1 ff.

### Rechtsprechung (`[unverifiziert – prüfen in curia.europa.eu / juris / bafin.de]`)

1. EuGH, Urt. v. 28.06.2012 – Rs. C-19/11, ECLI:EU:C:2012:397 (Geltl/Daimler – präzise Information in Zwischenschritten)
2. EuGH, Urt. v. 11.03.2015 – Rs. C-628/13, ECLI:EU:C:2015:162 (Lafonta – Richtungsangabe nicht erforderlich)
3. BGH, Urt. v. 13.12.2011 – XI ZR 51/10, BGHZ 192, 90 (IKB – Anlegerschadensersatz Ad-hoc)
4. BGH, Urt. v. 19.07.2004 – II ZR 217/03, BGHZ 160, 134 (EM.TV)
5. BaFin-Sanktionsentscheidungen – veröffentlicht auf bafin.de (Naming and Shaming Art. 34 MAR)

## Ausgabeformat

```
GUTACHTEN — Marktmissbrauch MAR / WpHG
Emittent: <anonymisiert>  |  Vorgang: <M&A / Restrukturierung / Bilanz / …>

I. Sachverhalt (knapp)
II. Frage(n)
III. Kurzantwort
     – Insiderinformation: [ja / nein / Zwischenschritt]
     – Ad-hoc-Pflicht: [unverzüglich / Aufschub Art. 17 IV zulässig]
     – Empfehlung: [Veröffentlichung / Aufschub mit Doku / Handelsverbot]

IV. Rechtliche Bewertung
    1. Anwendungsbereich MAR (Art. 2)
    2. Insiderinformation (Art. 7) – vier Kriterien
    3. Verbote (Art. 14, 15) – ggf. Legitimate Behaviour (Art. 9)
    4. Ad-hoc-Pflicht (Art. 17 I) und Aufschub (Art. 17 IV)
    5. Insiderliste (Art. 18) – Pflichten Emittent
    6. Directors' Dealings (Art. 19) – Closed Period
    7. Sanktionsrisiko (Art. 30 MAR, §§ 119, 38 WpHG)

V. Fristtabelle
   - Ad-hoc unverzüglich               (Art. 17 I MAR)
   - Aufschub-Doku + BaFin-Mitteilung  (Art. 17 IV MAR + DVO 2016/1055)
   - Directors' Dealings 3 Geschäftstage (Art. 19 I MAR)
   - Insiderliste Aktualisierung unverzüglich (Art. 18)

VI. Risiken / offene Punkte
    🟢 / 🟡 / 🔴 <Einstufung mit Begründung>

VII. Entwurf Ad-hoc-Mitteilung (optional)
     [sachliche Pressemitteilungs-Form, faktentreu, keine Werbung]

VIII. Quellenverzeichnis
```

## Risiken / typische Fehler

- **Aufschub Art. 17 IV ohne Dokumentation** der drei Voraussetzungen — BLOCKER, Verstoß führt zu Bußgeld und Anlegerklagen-Exposition.
- **Insiderliste nicht aktualisiert**, wenn neue Berater eingebunden werden — Verstoß Art. 18 MAR.
- **Closed Period übersehen**, weil Vorstandsmitglied auf "vorbestimmten Plan" verweist, dessen Voraussetzungen nach Art. 19 XII MAR nicht erfüllt sind.
- **Zwischenschritt-Insiderinformation unterschätzt** (Geltl-Linie) — sobald Term Sheet/LOI vorliegt, kann bereits Veröffentlichungspflicht entstehen, wenn der Schritt selbst kursrelevant ist.
- **Marktmanipulations-Risiko bei Pressemitteilungen** ohne ausreichende Tatsachengrundlage — Art. 15 iVm Art. 12 I lit. c MAR.
- **Selbst-Bewertung ohne Insider-Check** in eilbedürftigen Sachverhalten (Vorstandskäufe vor Bilanzveröffentlichung) — BLOCKER.
- **Bankaufsichtsrechtliche Ebene** (KWG-Erlaubnis Wertpapierdienstleistung) nicht hier — Querverweis Plugin `bankrecht`.
