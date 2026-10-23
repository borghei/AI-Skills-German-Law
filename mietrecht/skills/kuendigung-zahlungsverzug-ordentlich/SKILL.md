---
name: kuendigung-zahlungsverzug-ordentlich
description: "Ordentliche Kündigung des Wohnraummietverhältnisses wegen Zahlungsrückstands und unpünktlicher Zahlung – schuldhafte, nicht unerhebliche Pflichtverletzung § 573 Abs. 2 Nr. 1 BGB (Rückstand über eine Monatsmiete für mehr als einen Monat), Verschulden und Geldschuld § 286 Abs. 4 BGB, Begründung § 573 Abs. 3 BGB, Schriftform § 568 BGB, Fristen § 573c BGB, Sozialklausel § 574 BGB, Verhältnis zur Schonfristzahlung § 569 Abs. 3 Nr. 2 BGB (BGH-Bestätigung v. 30.09.2026) und § 242-Kontrolle, anhängiger § 573 Abs. 4 BGB-E (BT-Drs. 21/6807). Rechtsstand: Oktober 2026. Use when ein Vermieter wegen Mietrückstands ordentlich (auch hilfsweise) kündigen will oder ein Mieter nach Schonfristzahlung prüft, ob die ordentliche Kündigung fortwirkt."
language: de
provider_variants: [claude, gemini, openai]
test: ./test.md
---

# /mietrecht:kuendigung-zahlungsverzug-ordentlich

## Zweck

Bei Mietrückständen erklärt der Vermieter in der Praxis fast immer zwei Kündigungen: fristlos nach § 543 BGB und hilfsweise ordentlich nach § 573 Abs. 2 Nr. 1 BGB. Der Grund ist, dass die Schonfristzahlung nach geltendem Recht nur die fristlose Kündigung beseitigt. Diese Skill prüft die ordentliche Kündigung eigenständig: Erheblichkeit, Verschulden, Form, Frist und die Frage, ob die Berufung auf sie nach vollständiger Zahlung treuwidrig ist. Sie trennt die gefestigte Rechtsprechung vom anhängigen Regierungsentwurf, der diese Rechtsprechung einmal je Mietverhältnis korrigieren würde. Für die fristlose Kündigung: `/mietrecht:fristlose-kuendigung-543`.

**Rechtsstand: Oktober 2026.**

- **Geltend:** Die Schonfristzahlung heilt die ordentliche Kündigung nicht. Der VIII. Zivilsenat hat das am 30.09.2026 bestätigt (VIII ZR 21/26) und die Gerichte verpflichtet, § 573 BGB eigenständig zu prüfen (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-09-30&Aktenzeichen=VIII%20ZR%2021/26).
- **Anhängig, nicht geltend:** § 573 Abs. 4 BGB-E nach dem Regierungsentwurf BT-Drs. 21/6807 v. 01.07.2026 (Anhörung im Rechtsausschuss am 14.10.2026; Stand 23.10.2026 nicht verabschiedet).

## Eingaben

- **Mietkonto:** Soll, Ist, Fälligkeiten (§ 556b Abs. 1 BGB: bis zum dritten Werktag), Zahlungseingänge
- Höhe der **Monatsmiete** (Bruttomiete einschließlich Vorauszahlungen)
- **Ursache** des Rückstands: Zahlungsunfähigkeit, Jobcenter / Sozialamt, Minderung, Zurückbehaltung, Versehen
- Bisherige Abmahnungen und unpünktliche Zahlungen
- **Kündigungsschreiben** (Wortlaut, Datum, Zugang, Unterschrift)
- Zahlungen nach Zugang der Kündigung, insbesondere innerhalb der Schonfrist
- Mietdauer (für § 573c BGB) und Härtegründe des Mieters (§ 574 BGB)

## Sub-Agent-Architektur

Die Prüfung wird in Prosa von spezialisierten Schritten getragen; einen `agents`-Block trägt diese Skill bewusst nicht (mietrecht-Konvention).

- Ein **Rückstands-Rechner** stellt den Rückstand zum Zeitpunkt des Zugangs der Kündigung fest; Zahlungen werden nach § 366 BGB zugeordnet und berechtigte Minderungen abgezogen.
- Ein **Erheblichkeits-Prüfer** wendet die Schwelle der Rechtsprechung und die Gesamtabwägung an.
- Ein **Verschuldens-Prüfer** prüft § 286 Abs. 4 BGB und die Zurechnung Dritter.
- Ein **Form- und Fristen-Prüfer** kontrolliert Schriftform, Begründung und § 573c BGB.
- Ein **Heilungs-Prüfer** beurteilt die Lage nach Zahlung: kein Wegfall durch Schonfristzahlung, aber Kontrolle nach § 242 BGB; außerdem markiert er den Entwurf.

## Ablauf

### 1. Pflichtverletzung: Rückstand und Erheblichkeit ([§ 573 Abs. 2 Nr. 1 BGB](https://www.gesetze-im-internet.de/bgb/__573.html))

Ein berechtigtes Interesse liegt vor, wenn der Mieter seine vertraglichen Pflichten **schuldhaft nicht unerheblich** verletzt hat. Ein Zahlungsrückstand von **mehr als einer Monatsmiete**, der **länger als einen Monat** besteht, kann die ordentliche Kündigung rechtfertigen. Ob die Pflichtverletzung nicht unerheblich ist, entscheidet das Tatgericht in einer Gesamtabwägung, insbesondere nach Dauer und Höhe des Verzugs (BGH, Urt. v. 10.10.2012 – VIII ZR 107/12, BGHZ 195, 64 = NJW 2013, 159, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2012-10-10&Aktenzeichen=VIII%20ZR%20107/12). Die Schwellen des § 543 Abs. 2 S. 1 Nr. 3 BGB müssen **nicht** erreicht sein.

**Fortdauernd unpünktliche Zahlung** kann ebenfalls eine nicht unerhebliche Pflichtverletzung sein, regelmäßig aber erst nach einer Abmahnung `[unverifiziert – prüfen]`.

### 2. Verschulden ([§ 286 Abs. 4 BGB](https://www.gesetze-im-internet.de/bgb/__286.html), [§ 276 BGB](https://www.gesetze-im-internet.de/bgb/__276.html))

Anders als bei § 543 BGB setzt § 573 Abs. 2 Nr. 1 BGB **Verschulden** voraus. Für Geldschulden gilt: Finanzielle Leistungsunfähigkeit entlastet grundsätzlich nicht. Der Mieter kann sich nur ausnahmsweise auf eine unvorhersehbare wirtschaftliche Notlage berufen und trägt dafür die Darlegungslast (vgl. VIII ZR 107/12). Verzögerungen des **Jobcenters** oder Sozialamts sind dem Mieter nicht nach § 278 BGB als Verschulden eines Erfüllungsgehilfen zuzurechnen; das Jobcenter wird bei der Erfüllung hoheitlicher Aufgaben tätig. Bei der ordentlichen Kündigung kann das Verschulden daher entfallen, wenn der Mieter alles Zumutbare getan hat (BGH, Urt. v. 10.10.2012 – VIII ZR 107/12, BGHZ 195, 64, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2012-10-10&Aktenzeichen=VIII%20ZR%20107/12).

Eine **berechtigte Minderung** (§ 536 BGB) mindert den Rückstand; ein Irrtum des Mieters über die Minderungsquote entlastet nur, wenn er unverschuldet war. Vertiefung: `/mietrecht:mietmangel-minderung`.

### 3. Form, Begründung, Frist

- **Schriftform** ([§ 568 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__568.html)): eigenhändig unterschrieben von allen Vermietern, an alle Mieter. E-Mail oder Fax genügen nicht.
- **Begründung** ([§ 573 Abs. 3 BGB](https://www.gesetze-im-internet.de/bgb/__573.html)): Rückstand nach Höhe und Monaten bezeichnen. Später entstandene Rückstände können nachgeschoben werden; frühere, nicht genannte Gründe nicht.
- **Widerspruchshinweis** (§ 568 Abs. 2 BGB).
- **Frist** ([§ 573c Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__573c.html)): drei, sechs oder neun Monate je nach Überlassungsdauer, Zugang spätestens am dritten Werktag eines Monats.
- **Hilfsweise Erklärung:** Die ordentliche Kündigung kann im selben Schreiben hilfsweise neben der fristlosen erklärt werden. Sie soll gerade für den Fall wirken, dass die fristlose durch Schonfristzahlung entfällt (BGH, Urt. v. 19.09.2018 – VIII ZR 231/17, VIII ZR 261/17, BGHZ 220, 1 = NJW 2018, 3517, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2018-09-19&Aktenzeichen=VIII%20ZR%20231/17).

### 4. Schonfristzahlung — geltende Rechtslage ([§ 569 Abs. 3 Nr. 2 BGB](https://www.gesetze-im-internet.de/bgb/__569.html))

Die Zahlung oder die Übernahmeerklärung einer öffentlichen Stelle innerhalb von zwei Monaten nach Rechtshängigkeit der Räumungsklage macht **nur die fristlose** Kündigung unwirksam. Die ordentliche Kündigung bleibt bestehen:

- BGH, Urt. v. 19.09.2018 – VIII ZR 231/17 (Grundsatzentscheidung), https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2018-09-19&Aktenzeichen=VIII%20ZR%20231/17,
- BGH, Urt. v. 13.10.2021 – VIII ZR 91/20 (Bestätigung), https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2021-10-13&Aktenzeichen=VIII%20ZR%2091/20,
- BGH, Urt. v. 30.09.2026 – VIII ZR 21/26 (erneute Bestätigung gegen abweichende Instanzrechtsprechung des LG Berlin), https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-09-30&Aktenzeichen=VIII%20ZR%2021/26.

Nach VIII ZR 21/26 hat das Gericht die Voraussetzungen des § 573 BGB **eigenständig** zu prüfen. Es darf die ordentliche Kündigung also nicht pauschal wegen der Zahlung verwerfen. Es darf sie aber auch nicht ungeprüft durchwinken (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-09-30&Aktenzeichen=VIII%20ZR%2021/26).

### 5. Treuwidrigkeitskontrolle nach Zahlung ([§ 242 BGB](https://www.gesetze-im-internet.de/bgb/__242.html))

Nach vollständigem Ausgleich ist zu prüfen, ob die Berufung auf die ordentliche Kündigung **ausnahmsweise treuwidrig** ist (VIII ZR 231/17, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2018-09-19&Aktenzeichen=VIII%20ZR%20231/17). Abwägungsgesichtspunkte sind:

- Wie kam es zum Rückstand (unverschuldete Notlage, Behördenfehler)?
- Wie schnell und wie vollständig wurde ausgeglichen?
- Gab es frühere Rückstände?
- Wie lange bestand das Mietverhältnis bisher ohne Störung?

Eine Zahlung allein begründet die Treuwidrigkeit nicht.

### 6. Sozialklausel ([§ 574 BGB](https://www.gesetze-im-internet.de/bgb/__574.html))

Gegen die **ordentliche** Kündigung steht dem Mieter der Widerspruch nach §§ 574–574b BGB offen. Er ist nur ausgeschlossen, wenn zugleich ein Grund für eine **fristlose** Kündigung vorliegt (§ 574 Abs. 1 S. 2 BGB). Wurde die fristlose Kündigung durch Schonfristzahlung unwirksam, ist umstritten, ob der Ausschluss noch greift `[unverifiziert – prüfen]`. Vertiefung: `/mietrecht:sozialklausel-widerspruch`.

### 7. Anhängige Reform: § 573 Abs. 4 BGB-E (BT-Drs. 21/6807)

Der Regierungsentwurf ([BT-Drs. 21/6807](https://dserver.bundestag.de/btd/21/068/2106807.pdf)) sieht vor:

- Die Heilungswirkung der Schonfristzahlung erstreckt sich **einmal je Mietverhältnis** auch auf die ordentliche Kündigung wegen Zahlungsverzugs.
- Das gilt auch für Rückstände mit der **Kaution**.
- Inkrafttreten am Tag nach der Verkündung.

**Handhabung bis zur Verkündung:**

- **Vermieter:** Kündigungen weiterhin doppelt (fristlos und hilfsweise ordentlich) erklären. Dokumentieren, ob bereits eine frühere Schonfristzahlung stattgefunden hat; nach dem Entwurf entfiele die Heilung dann.
- **Mieter:** Im laufenden Räumungsprozess die Übergangsregel nach Verkündung genau prüfen; bis dahin trägt nur die § 242-Kontrolle.

## Deterministische Berechnung

```bash
# Verzugszinsen auf den Rückstand (Basiszinssatz ist Pflichteingabe und gegen die Bundesbank zu prüfen)
python -m scripts.legal_calc.cli verzugszinsen --betrag 2400 \
    --verzug-ab 06.03.2026 --bis 23.10.2026 \
    --basiszins 01.01.2026:1.10 --basiszins 01.07.2026:1.10 --schuldner-ist-verbraucher

# Schonfrist: zwei Monate ab Rechtshängigkeit (Zustellung der Räumungsklage am 14.09.2026)
python -m scripts.legal_calc.cli frist --ereignis 14.09.2026 --menge 2 --einheit monate --land NW
```

Die Basiszinssätze im Beispiel sind **Platzhalter**. Der Rechner macht nur die Arithmetik; ob ein Rückstand „nicht unerheblich" ist, bleibt eine juristische Wertung.

## Quellen

### Statute

- [§ 573 BGB](https://www.gesetze-im-internet.de/bgb/__573.html), [§ 573c BGB](https://www.gesetze-im-internet.de/bgb/__573c.html), [§ 568 BGB](https://www.gesetze-im-internet.de/bgb/__568.html), [§ 569 BGB](https://www.gesetze-im-internet.de/bgb/__569.html), [§ 543 BGB](https://www.gesetze-im-internet.de/bgb/__543.html)
- [§ 574 BGB](https://www.gesetze-im-internet.de/bgb/__574.html), [§ 286 BGB](https://www.gesetze-im-internet.de/bgb/__286.html), [§ 276 BGB](https://www.gesetze-im-internet.de/bgb/__276.html), [§ 366 BGB](https://www.gesetze-im-internet.de/bgb/__366.html), [§ 242 BGB](https://www.gesetze-im-internet.de/bgb/__242.html), [§ 556b BGB](https://www.gesetze-im-internet.de/bgb/__556b.html)

### Gesetzgebung

- Regierungsentwurf, BT-Drs. 21/6807 v. 01.07.2026 — https://dserver.bundestag.de/btd/21/068/2106807.pdf (Stand 23.10.2026: nicht verabschiedet)

### Kommentare

- Blank/Börstinghaus, Miete, aktuelle Auflage, § 573 Rn. 1 ff.
- Schmidt-Futterer, Mietrecht, 16. Aufl. 2024, § 573 BGB, § 569 BGB (Bearbeiter und Rn. vor Zitat prüfen)

### Rechtsprechung

- BGH, Urt. v. 30.09.2026 – VIII ZR 21/26 (Schonfristzahlung heilt die ordentliche Kündigung nicht; § 573 BGB eigenständig zu prüfen) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-09-30&Aktenzeichen=VIII%20ZR%2021/26
- BGH, Urt. v. 13.10.2021 – VIII ZR 91/20 — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2021-10-13&Aktenzeichen=VIII%20ZR%2091/20
- BGH, Urt. v. 19.09.2018 – VIII ZR 231/17, VIII ZR 261/17, BGHZ 220, 1 = NJW 2018, 3517 (hilfsweise ordentliche Kündigung; § 242-Kontrolle nach Zahlung) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2018-09-19&Aktenzeichen=VIII%20ZR%20231/17
- BGH, Urt. v. 10.10.2012 – VIII ZR 107/12, BGHZ 195, 64 = NJW 2013, 159 (Erheblichkeitsschwelle: mehr als eine Monatsmiete länger als einen Monat; Gesamtabwägung; Jobcenter nicht Erfüllungsgehilfe des Mieters) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2012-10-10&Aktenzeichen=VIII%20ZR%20107/12
- Zur Abmahnung bei unpünktlicher Zahlung ist die einschlägige BGH-Rechtsprechung heranzuziehen `[unverifiziert – prüfen]`.

## Formulierungshilfe — Fristlose und hilfsweise ordentliche Kündigung

```
Hiermit kündige ich das Mietverhältnis über die Wohnung <Anschrift>
fristlos gemäß § 543 Abs. 2 S. 1 Nr. 3 BGB, hilfsweise ordentlich gemäß
§ 573 Abs. 2 Nr. 1 BGB zum <Datum nach § 573c BGB>.

Begründung: Sie sind mit der Miete für die Monate <…> in Höhe von insgesamt
<Betrag> EUR im Rückstand (Monatsmiete <Betrag> EUR). Der Rückstand besteht
seit dem <Datum> und damit seit mehr als einem Monat. Er übersteigt eine
Monatsmiete.

Die ordentliche Kündigung soll auch dann gelten, wenn die fristlose
Kündigung durch eine Zahlung nach § 569 Abs. 3 Nr. 2 BGB unwirksam wird.

Sie können der ordentlichen Kündigung nach §§ 574 bis 574b BGB schriftlich
bis spätestens zwei Monate vor Beendigung des Mietverhältnisses
widersprechen.

<eigenhändige Unterschrift aller Vermieter>
```

## Ausgabeformat

```
ORDENTLICHE KÜNDIGUNG WEGEN ZAHLUNGSRÜCKSTANDS — <Mandat-ID> — <Datum>

I.    Rückstand bei Zugang              <Betrag> (= <…> Monatsmieten), seit <Datum>
      Schwelle VIII ZR 107/12           [> 1 Monatsmiete > 1 Monat ✅ / ❌]
II.   Verschulden (§ 286 Abs. 4)        [✅ / Entlastung: <…>]
III.  Form § 568 / Begründung § 573 III [✅ / ❌]
IV.   Frist § 573c                      [3 / 6 / 9 Monate] → Ende <Datum>
V.    Schonfristzahlung                 [keine / am <Datum> → nur fristlose entfallen]
VI.   § 242-Kontrolle nach Zahlung      [keine Treuwidrigkeit / Treuwidrigkeit wegen <…>]
VII.  Sozialklausel § 574               [N/A / Widerspruch erhoben / Härte: <…>]
VIII. Entwurf § 573 Abs. 4 BGB-E        [nicht verabschiedet — wäre: erste / zweite Heilung]

Ergebnis: <Mietverhältnis endet am … / besteht fort>
Risiko: [🟢 / 🟡 / 🔴]
```

## Risiken / typische Fehler

- **Ordentliche Kündigung nicht hilfsweise erklärt** — nach einer Schonfristzahlung ist das Verfahren dann verloren.
- **Schonfristzahlung als Heilung der ordentlichen Kündigung behandelt** — widerspricht VIII ZR 231/17, VIII ZR 91/20 und VIII ZR 21/26 (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2018-09-19&Aktenzeichen=VIII%20ZR%20231/17).
- **Verschulden nicht geprüft** — § 573 Abs. 2 Nr. 1 BGB verlangt es, anders als § 543 BGB.
- **Minderung im Rückstand nicht berücksichtigt** — der kündigungsrelevante Rückstand ist zu hoch angesetzt.
- **Treuwidrigkeitskontrolle übersprungen** — nach vollständigem Ausgleich ist § 242 BGB zu prüfen.
- **Kündigung per E-Mail** — Schriftform des § 568 Abs. 1 BGB verfehlt.
- **Entwurf § 573 Abs. 4 BGB-E angewendet** — bisher nur Regierungsentwurf (BT-Drs. 21/6807).
