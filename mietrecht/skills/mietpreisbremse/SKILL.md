---
name: mietpreisbremse
description: "Mietpreisbremse bei Wiedervermietung von Wohnraum – zulässige Miethöhe § 556d BGB (ortsübliche Vergleichsmiete zzgl. 10 %) und Landesverordnung, Ausnahmen für Neubau und umfassende Modernisierung § 556f BGB, Vormiete und modernisierte Wohnung § 556e BGB, vorvertragliche Auskunftspflicht § 556g Abs. 1a BGB, Rüge in Textform und Rückforderung § 556g Abs. 2, 4 BGB (30-Monats-Rückwirkung für Verträge ab 01.04.2020), Unwirksamkeit abweichender Vereinbarungen § 556g Abs. 1 BGB, Verordnungsermächtigung bis 31.12.2029, Rspr. des BGH 2025/2026 und anhängiger Möblierungszuschlag (BT-Drs. 21/6807). Rechtsstand: Oktober 2026. Use when eine Neuvertragsmiete auf Zulässigkeit geprüft, eine Rüge erhoben oder überzahlte Miete zurückgefordert wird."
language: de
provider_variants: [claude, gemini, openai]
test: ./test.md
---

# /mietrecht:mietpreisbremse

## Zweck

Die Mietpreisbremse begrenzt die Miete bei **Wiedervermietung** — nicht die laufende Erhöhung. Sie wirkt nicht automatisch: Der Mieter muss **rügen** (Textform, § 556g Abs. 4 BGB). Für Verträge, die **nach dem 31.03.2020** geschlossen wurden, wirkt eine Rüge, die **binnen 30 Monaten nach Mietbeginn** und während des laufenden Mietverhältnisses zugeht, auf den Mietbeginn zurück; danach nur für die Zukunft (§ 556g Abs. 2 S. 3 BGB). Diese Skill bestimmt die zulässige Miete, prüft die vier Ausnahmetatbestände, ordnet den Vertrag dem richtigen Altrecht/Neurecht zu und formuliert die Rüge.

**Rechtsstand: Oktober 2026.** Geltend: Verordnungsermächtigung bis **31.12.2029** (§ 556d Abs. 2 BGB i.d.F. des Gesetzes v. 17.07.2025, BGBl. 2025 I Nr. 163). Anhängig, **nicht** geltend: Regierungsentwurf eines Gesetzes zur Änderung des Rechts der Wohn- und Geschäftsraummiete (BT-Drs. 21/6807 v. 01.07.2026; Anhörung im Rechtsausschuss 14.10.2026, nicht verabschiedet) mit Regeln zum Möblierungszuschlag (§ 556d Abs. 1a, § 556g Abs. 1b BGB-E).

## Eingaben

- **Mietvertrag**: Datum des Vertragsschlusses, vereinbarte Nettokaltmiete, Wohnfläche, Mietbeginn
- **Belegenheit**: Gilt für den Ort eine **Landesverordnung** nach § 556d Abs. 2 BGB? Seit wann, bis wann?
- **Ortsübliche Vergleichsmiete**: Mietspiegelwert, Feld, Spanne, Fassung
- **Vormiete**: Höhe der zuletzt vor Vertragsschluss geschuldeten Miete und Zeitpunkt
- **Bauzustand**: Erstnutzung nach dem 01.10.2014? Umfassende Modernisierung? Modernisierung in den letzten drei Jahren?
- **Auskunft** des Vermieters nach § 556g Abs. 1a BGB: erteilt, wann, in welcher Form
- Bisher gezahlte Mieten (für die Rückforderung)

## Sub-Agent-Architektur

Die Prüfung wird in Prosa von spezialisierten Schritten getragen; einen `agents`-Block trägt diese Skill bewusst nicht (mietrecht-Konvention). Ein **Anwendungsbereichs-Prüfer** klärt zuerst, ob überhaupt eine wirksame Landesverordnung für den Ort und den Vertragszeitraum gilt — daran scheitern in der Praxis die meisten Fälle. Ein **Ausnahme-Prüfer** arbeitet die Tatbestände der §§ 556e, 556f BGB ab, weil sie die zulässige Miete vollständig verschieben. Ein **Rechen-Prüfer** ermittelt die zulässige Miete und den Überzahlungsbetrag. Ein **Rüge-Prüfer** ordnet den Vertrag zeitlich ein (Vertragsschluss bis/nach 31.03.2020), formuliert die Rüge und bestimmt den Beginn des Rückforderungszeitraums.

## Ablauf

### 1. Anwendungsbereich ([§ 556d BGB](https://www.gesetze-im-internet.de/bgb/__556d.html))

Wird ein Mietvertrag über Wohnraum abgeschlossen, der in einem durch **Rechtsverordnung der Landesregierung** bestimmten Gebiet mit **angespanntem Wohnungsmarkt** liegt, darf die Miete zu Beginn des Mietverhältnisses die **ortsübliche Vergleichsmiete höchstens um 10 %** übersteigen. Zu prüfen ist:

- Existiert für den Ort eine **wirksame Verordnung**? Sie muss begründet sein und muss nach § 556d Abs. 2 BGB **spätestens mit Ablauf des 31.12.2029** außer Kraft treten (Verlängerung durch Gesetz v. 17.07.2025, BGBl. 2025 I Nr. 163, https://www.recht.bund.de/bgbl/1/2025/163/VO.html). Mehrere Landesverordnungen sind wegen fehlender Begründung für unwirksam erklärt worden; viele Länder haben 2025/2026 **neue** Verordnungen erlassen (z. B. Berlin mit Wirkung ab 01.01.2026). Die Fassung, die am Tag des **Vertragsschlusses** galt, ist im Landesgesetzblatt zu ermitteln.
- Fällt der **Vertragsschluss** in den Geltungszeitraum? Maßgeblich ist der Vertragsschluss, nicht der Mietbeginn.
- Handelt es sich um **Wohnraum**? Gewerberaum, Wohnraum zum vorübergehenden Gebrauch, möblierter Wohnraum in der Vermieterwohnung und Werkmietwohnungen sind ausgenommen (§ 549 Abs. 2 BGB).

Die Verfassungsmäßigkeit der Regelung ist geklärt: BVerfG, Beschl. v. 18.07.2019 – 1 BvL 1/18 u.a., https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=2019-07-18&Aktenzeichen=1%20BvL%201/18.

### 2. Ortsübliche Vergleichsmiete als Bezugsgröße

Die ortsübliche Vergleichsmiete bestimmt sich nach **§ 558 Abs. 2 BGB**: Entgelte für nicht preisgebundenen Wohnraum vergleichbarer Art, Größe, Ausstattung, Beschaffenheit und Lage einschließlich der energetischen Ausstattung, vereinbart oder geändert in den letzten **sechs Jahren**. Praktisch wird der **Mietspiegel** herangezogen; die Wohnung ist konkret in Feld und Spanne einzuordnen. Die zulässige Miete beträgt diesen Wert **zuzüglich 10 %**. Vertiefung zur Ermittlung: `/mietrecht:mieterhoehung-558-bgb`.

### 3. Vormiete und vorangegangene Modernisierung ([§ 556e BGB](https://www.gesetze-im-internet.de/bgb/__556e.html))

**Abs. 1 — Vormiete:** War die zuletzt geschuldete Miete (**Vormiete**) höher als die nach § 556d Abs. 1 BGB zulässige Miete, darf eine Miete bis zur Höhe der Vormiete vereinbart werden. Unberücksichtigt bleiben Mietminderungen sowie Erhöhungen, die innerhalb des letzten Jahres vor Beendigung des Vormietverhältnisses vereinbart wurden.

**Abs. 2 — Modernisierung in den letzten drei Jahren:** Hat der Vermieter in den letzten drei Jahren vor Beginn des Mietverhältnisses **modernisiert** (§ 555b BGB), darf er die zulässige Miete um den Betrag erhöhen, der sich bei einer Modernisierungsmieterhöhung nach §§ 559–559b BGB ergäbe. Vertiefung: `/mietrecht:modernisierung-559-bgb`.

### 4. Ausnahmen ([§ 556f BGB](https://www.gesetze-im-internet.de/bgb/__556f.html))

Die Mietpreisbremse gilt **nicht**

- für Wohnraum, der **nach dem 01.10.2014 erstmals genutzt und vermietet** wird (**Neubauprivileg**, S. 1) — und zwar dauerhaft, auch für jede spätere Wiedervermietung;
- für die **erste Vermietung nach umfassender Modernisierung** (S. 2). „Umfassend" verlangt einen Aufwand von etwa **einem Drittel** des für einen vergleichbaren Neubau erforderlichen Betrags und eine Qualität, die einem Neubau nahekommt; bloße Renovierung genügt nicht.

**Neubau durch Umbau:** Das Neubauprivileg des S. 1 erfasst auch Flächen, die erst durch Baumaßnahmen mit einem Aufwand von rund einem Drittel vergleichbarer Neubaukosten zu Wohnraum geworden sind (BGH, Urt. v. 01.07.2026 – VIII ZR 50/23, NZM 2026, 685, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-07-01&Aktenzeichen=VIII%20ZR%2050/23). Bei der Umwandlung von Gewerbe- in Wohnraum ist die Ausnahme **eng** auszulegen: Die Räume dürfen im früheren Zustand objektiv nicht als Wohnung nutzbar gewesen sein (eigenständige Haushaltsführung mit WC, Bad, Küche bzw. Kochgelegenheit und Anschlüssen); die Wohnnutzung muss erst durch Baumaßnahmen mit wesentlichem Bauaufwand (rund ein Drittel vergleichbarer Neubaukosten ohne Grundstück, Schätzung nach § 287 ZPO) möglich geworden sein; **bloße Instandsetzung**, die einen früheren Zustand wiederherstellt, zählt **nicht**; Darlegungs- und Beweislast beim Vermieter (BGH, 19.08.2026 – VIII ZR 104/25, Entscheidungsart in der Quelle nicht ausgewiesen, wohl Urteil; https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-08-19&Aktenzeichen=VIII%20ZR%20104/25). **Grenze:** Hat der Vermieter den unbewohnbaren Zustand bewusst herbeigeführt (etwa durch Entkernung einer zuvor bewohnbaren Wohnung), kann er sich nach überwiegender Auffassung nicht auf das Neubauprivileg berufen; das ist den hier zugänglichen Auszügen der Entscheidungen nicht zu entnehmen `[unverifiziert – prüfen]`.

Die Darlegungs- und Beweislast für die Ausnahmen trägt der **Vermieter**.

### 5. Vorvertragliche Auskunftspflicht ([§ 556g Abs. 1a BGB](https://www.gesetze-im-internet.de/bgb/__556g.html))

Der Vermieter hat den Mieter **unaufgefordert und in Textform vor Abgabe von dessen Vertragserklärung** darüber zu informieren, wenn er sich auf eine der folgenden Konstellationen berufen will:

1. **Vormiete** (§ 556e Abs. 1 BGB) — Höhe der Vormiete,
2. **Modernisierung in den letzten drei Jahren** (§ 556e Abs. 2 BGB),
3. **Neubau** nach dem 01.10.2014 (§ 556f S. 1 BGB),
4. **umfassende Modernisierung** (§ 556f S. 2 BGB).

**Sanktion:** Erteilt der Vermieter die Auskunft nicht, kann er sich auf die betreffende Ausnahme **nicht berufen**. Holt er sie nach, kann er sich erst **zwei Jahre nach Nachholung** darauf berufen (Abs. 1a S. 2, 3). Das macht die Auskunftspflicht zum wirksamsten Hebel des Mieters.

### 6. Rüge und Rückforderung ([§ 556g Abs. 1, Abs. 2, Abs. 4 BGB](https://www.gesetze-im-internet.de/bgb/__556g.html))

Eine zum Nachteil des Mieters abweichende Vereinbarung ist **unwirksam** (Abs. 1 S. 1); zu viel gezahlte Miete ist nach den Vorschriften über die **ungerechtfertigte Bereicherung** herauszugeben (Abs. 1 S. 3). Voraussetzung der Rückforderung ist eine **Rüge** (Abs. 2 S. 1) in **Textform** (Abs. 4).

**Inhalt der Rüge.** Eine **qualifizierte Rüge** mit Darlegung der Tatsachen, auf denen die Beanstandung beruht, verlangt das Gesetz seit dem **01.01.2019** (MietAnpG) **nicht mehr**. Es genügt die erkennbare Beanstandung, die Miete verstoße gegen §§ 556d ff. BGB. Hat der Vermieter eine Auskunft nach Abs. 1a erteilt, muss sich die Rüge **auf diese Auskunft beziehen** (Abs. 2 S. 2). Nur für Altverträge vor 2019 ist die qualifizierte Rüge noch maßgeblich.

**Rückwirkung — zeitliche Einordnung zwingend:**

| Vertragsschluss | Wirkung der Rüge |
|---|---|
| bis einschließlich 31.03.2020 (Art. 229 § 51 EGBGB: § 556g BGB a.F.) | nur für die **nach Zugang** der Rüge fällig werdende Miete (ex nunc) |
| ab 01.04.2020 — Rüge **binnen 30 Monaten** nach Mietbeginn, Mietverhältnis noch nicht beendet | Rückforderung **ab Mietbeginn** |
| ab 01.04.2020 — Rüge **nach** 30 Monaten oder nach Beendigung | nur für die nach Zugang fällig werdende Miete (Abs. 2 S. 3) |

Ergänzend besteht ein **Auskunftsanspruch** nach Abs. 3 über die für die zulässige Miethöhe maßgeblichen Tatsachen; das Rechtsschutzinteresse daran entfällt nicht dadurch, dass dem Vermieter bereits die Sanktion des Abs. 1a droht (BGH, Urt. v. 01.07.2026 – VIII ZR 211/23, NZM 2026, 689, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-07-01&Aktenzeichen=VIII%20ZR%20211/23). Eine **während** des Mietverhältnisses vereinbarte Mietsenkung fällt nicht unter §§ 556d ff. BGB; insoweit besteht auch kein Auskunftsanspruch nach § 556g BGB (BGH, Urt. v. 17.12.2025 – VIII ZR 56/25, NZM 2026, 139, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-12-17&Aktenzeichen=VIII%20ZR%2056/25). Zur Vormiete, die ihrerseits gegen § 556g Abs. 1a BGB verstieß, und zu Schadensersatz nach § 241 Abs. 2 BGB bei Verlangen einer teilnichtigen Miete: BGH, Urt. v. 01.07.2026 – VIII ZR 125/23, NZM 2026, 716, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-07-01&Aktenzeichen=VIII%20ZR%20125/23 — die Entscheidung ist differenziert; vor Verwendung im Volltext lesen.

### 7. Durchsetzung und Abtretung

Der Rückforderungsanspruch kann an **registrierte Inkassodienstleister** abgetreten werden; deren Geschäftsmodell ist mit dem RDG vereinbar (BGH, Urt. v. 27.11.2019 – VIII ZR 285/18, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2019-11-27&Aktenzeichen=VIII%20ZR%20285/18). Die Verjährung richtet sich nach den §§ 195, 199 BGB (drei Jahre ab Schluss des Jahres der Entstehung und Kenntnis). Die Rüge sollte daher früh und beweisbar zugehen. **Keine Kündigungsgefahr:** Die Rüge ist Rechtsausübung; eine darauf gestützte Kündigung wäre unwirksam und begründete Schadensersatzansprüche.

### 8. Anhängig: Möblierungszuschlag und Kurzzeitvermietung (BT-Drs. 21/6807)

Nach geltendem Recht gilt die Mietpreisbremse auch für möblierte Wohnungen, sofern kein Ausnahmetatbestand des § 549 Abs. 2 BGB vorliegt; der Möblierungszuschlag ist Teil der Miete und an § 556d BGB zu messen. Der **Regierungsentwurf** (BT-Drs. 21/6807, https://dserver.bundestag.de/btd/21/068/2106807.pdf) sieht vor: Zuschlag höchstens 1 % des Zeitwerts der Möbel monatlich, bei Vollmöblierung bis 10 % der Nettokaltmiete als angemessen vermutet (§ 556d Abs. 1a BGB-E); ohne gesonderte Ausweisung gilt die Wohnung bis zwei Jahre nach Nachholung als unmöbliert (§ 556g Abs. 1b BGB-E). Inkrafttreten am ersten Tag des vierten Monats nach Verkündung; **Altverträge** bleiben beim bisherigen Recht. Stand 23.10.2026: nicht verabschiedet. Vertiefung: `/mietrecht:moeblierte-kurzzeitvermietung`.

## Quellen

### Statute

- [§ 556d BGB](https://www.gesetze-im-internet.de/bgb/__556d.html), [§ 556e BGB](https://www.gesetze-im-internet.de/bgb/__556e.html), [§ 556f BGB](https://www.gesetze-im-internet.de/bgb/__556f.html), [§ 556g BGB](https://www.gesetze-im-internet.de/bgb/__556g.html)
- [§ 558 BGB](https://www.gesetze-im-internet.de/bgb/__558.html) (ortsübliche Vergleichsmiete), [§ 559 BGB](https://www.gesetze-im-internet.de/bgb/__559.html), [§ 555b BGB](https://www.gesetze-im-internet.de/bgb/__555b.html)
- [§ 549 BGB](https://www.gesetze-im-internet.de/bgb/__549.html) (Ausnahmen vom Wohnraummietrecht), [§ 812 BGB](https://www.gesetze-im-internet.de/bgb/__812.html), [§ 195 BGB](https://www.gesetze-im-internet.de/bgb/__195.html), [§ 199 BGB](https://www.gesetze-im-internet.de/bgb/__199.html)

### Kommentare

- Börstinghaus, in: Schmidt-Futterer, Mietrecht, 16. Aufl. 2024, § 556d BGB Rn. 1 ff.; § 556g BGB Rn. 1 ff.
- Artz, in: MüKoBGB, 9. Aufl. 2023, § 556d Rn. 1 ff.; § 556f Rn. 1 ff.
- Weidenkaff, in: Grüneberg, BGB, 84. Aufl. 2025, § 556d Rn. 1 ff.

### Rechtsprechung

- BVerfG, Beschl. v. 18.07.2019 – 1 BvL 1/18 u.a. (Mietpreisbremse verfassungsgemäß) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=2019-07-18&Aktenzeichen=1%20BvL%201/18
- BGH, Urt. v. 27.11.2019 – VIII ZR 285/18 (Abtretung an registrierten Inkassodienstleister; Vereinbarkeit mit dem RDG) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2019-11-27&Aktenzeichen=VIII%20ZR%20285/18
- BGH, Urt. v. 01.07.2026 – VIII ZR 50/23, NZM 2026, 685 (§ 556f S. 1 BGB: Neubau durch Umbau, Drittel-Schwelle wesentlichen Bauaufwands) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-07-01&Aktenzeichen=VIII%20ZR%2050/23
- BGH, 19.08.2026 – VIII ZR 104/25 (Entscheidungsart nicht ausgewiesen; Umwandlung Gewerbe in Wohnraum; enge Auslegung von § 556f BGB; Instandsetzungskosten zählen nicht zur Drittel-Schwelle) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-08-19&Aktenzeichen=VIII%20ZR%20104/25
- BGH, Urt. v. 01.07.2026 – VIII ZR 211/23, NZM 2026, 689 (Auskunftsanspruch § 556g Abs. 3 BGB) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-07-01&Aktenzeichen=VIII%20ZR%20211/23
- BGH, Urt. v. 01.07.2026 – VIII ZR 125/23, NZM 2026, 716 (Vormiete, § 241 Abs. 2 BGB) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-07-01&Aktenzeichen=VIII%20ZR%20125/23
- BGH, Urt. v. 17.12.2025 – VIII ZR 56/25, NZM 2026, 139 (Mietsenkung während des Mietverhältnisses) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-12-17&Aktenzeichen=VIII%20ZR%2056/25
- Zur Frage, wann eine Modernisierung „umfassend" i.S.v. § 556f S. 2 BGB ist (Qualitätskriterium neben der Kostenschwelle), ist die einschlägige Rechtsprechung heranzuziehen `[unverifiziert – prüfen]`.

## Formulierungshilfe — Rüge (§ 556g Abs. 2, 4 BGB)

```
Sehr geehrte Damen und Herren,

hiermit rüge ich gemäß § 556g Abs. 2 BGB einen Verstoß gegen die
Vorschriften über die zulässige Miethöhe bei Mietbeginn (§§ 556d ff. BGB).
Tatsachen muss die Rüge seit 2019 nicht enthalten; zur Klarstellung
und um eine schnelle Einigung zu ermöglichen, weise ich auf Folgendes hin:

1. Die Wohnung <Anschrift, Lage im Haus> liegt im Geltungsbereich der
   <Bezeichnung der Landesverordnung> vom <Datum>, in Kraft seit <Datum>.
   Der Mietvertrag wurde am <Datum> geschlossen und damit im
   Geltungszeitraum.
2. Die vereinbarte Nettokaltmiete beträgt <Betrag> EUR für <…> m², mithin
   <…> EUR/m².
3. Nach dem Mietspiegel der Stadt <Ort> (Fassung <Datum>) ist die Wohnung
   in das Feld <…> einzuordnen (Baujahr <…>, Ausstattung <…>, Lage <…>).
   Der einschlägige Wert beträgt <…> EUR/m². Zuzüglich 10 % ergibt sich
   eine zulässige Miete von <…> EUR/m², mithin <Betrag> EUR monatlich.
4. Die vereinbarte Miete übersteigt die zulässige Miete damit um
   <Betrag> EUR monatlich.
5. Eine Auskunft nach § 556g Abs. 1a BGB haben Sie vor meiner
   Vertragserklärung nicht erteilt. Auf die Ausnahmen der §§ 556e, 556f BGB
   können Sie sich daher nicht berufen.

Ich fordere Sie auf, die Miete ab dem <Datum> auf <Betrag> EUR zu
reduzieren und die überzahlten Beträge nach § 556g Abs. 1 S. 3 BGB
zurückzuzahlen — seit Mietbeginn, da diese Rüge binnen 30 Monaten nach
Mietbeginn zugeht <bei Vertragsschluss ab 01.04.2020; sonst: ab Zugang>. Ferner verlange ich Auskunft nach
§ 556g Abs. 3 BGB über die für die zulässige Miethöhe maßgeblichen
Tatsachen.

Frist: <Datum>

Mit freundlichen Grüßen
```

## Ausgabeformat

```
MIETPREISBREMSE §§ 556d ff. BGB — Prüfung — <Mandat-ID> — <Datum>

I.    Anwendungsbereich
      - Landesverordnung                 <Bezeichnung, Geltung von–bis>  [wirksam / zweifelhaft]
      - Vertragsschluss im Zeitraum      [✅ / ❌]
      - Wohnraum (§ 549 BGB)             [✅ / Ausnahme]
II.   Zulässige Miete (§ 556d Abs. 1)    Vergleichsmiete: <…> EUR/m²
                                         + 10 % = <…> EUR/m² → <Betrag> EUR
III.  Vereinbarte Miete                  <Betrag> EUR    Differenz: <Betrag> EUR
IV.   Ausnahmen
      - Vormiete (§ 556e Abs. 1)         [N/A / <Betrag>]
      - Modernisierung 3 Jahre (§ 556e Abs. 2) [N/A / Zuschlag <Betrag>]
      - Neubau ab 01.10.2014 (§ 556f S. 1)     [N/A / greift → Prüfung endet]
      - Umfassende Modernisierung (§ 556f S. 2) [N/A / greift / streitig]
V.    Auskunft (§ 556g Abs. 1a)          [erteilt am <Datum> / nicht erteilt]
      Folge                              [Berufung auf Ausnahme möglich /
                                          ausgeschlossen / erst ab <Datum +2 J.>]
VI.   Rüge (§ 556g Abs. 2)               [erhoben am <Datum> / zu erheben]
      Textform / Bezug auf Auskunft      [✅ / ⚠️]
      Vertragsschluss ≤ / > 31.03.2020    [ex nunc / Rückwirkung 30 Monate]
VII.  Rückforderung                      ab <Datum>: <Betrag> EUR
      Verjährung §§ 195, 199 BGB         Ende: <Datum>
VIII. Auskunftsanspruch (§ 556g Abs. 3)  [geltend gemacht / offen]

Ergebnis: <Miete überhöht um … / zulässig>
Risiko: [🟢 / 🟡 / 🔴]
```

## Risiken / typische Fehler

- **Landesverordnung nicht geprüft** — mehrere Verordnungen sind wegen fehlender oder verspäteter Begründung für unwirksam erklärt worden; ohne wirksame Verordnung greift die Mietpreisbremse nicht.
- **Rüge nicht auf erteilte Auskunft bezogen** — hat der Vermieter eine Auskunft nach Abs. 1a erteilt, muss sich die Rüge darauf beziehen (Abs. 2 S. 2); umgekehrt ist es falsch, nach heutigem Recht noch eine qualifizierte Rüge mit Tatsachendarlegung zu verlangen (Altrecht bis 31.12.2018).
- **Rückwirkung überschätzt** oder unterschätzt — volle Rückwirkung auf den Mietbeginn nur bei Vertragsschluss ab 01.04.2020, Rüge binnen 30 Monaten und laufendem Mietverhältnis; sonst ex nunc. Die 30-Monats-Frist ist ab Mietbeginn zu notieren.
- **Möblierungszuschlag nach künftigem Recht beurteilt** — § 556d Abs. 1a, § 556g Abs. 1b BGB-E sind Entwurf (BT-Drs. 21/6807) und gelten nicht für Altverträge.
- **Neubauprivileg übersehen** — für Wohnraum mit erstmaliger Nutzung und Vermietung nach dem 01.10.2014 gilt die Mietpreisbremse dauerhaft nicht, auch bei späteren Wiedervermietungen.
- **Vormiete falsch angesetzt** — Erhöhungen im letzten Jahr vor Beendigung des Vormietverhältnisses und Minderungen bleiben außer Betracht.
- **Mietpreisbremse mit § 558 BGB verwechselt** — sie begrenzt die Miete bei Wiedervermietung, nicht die laufende Erhöhung auf die ortsübliche Vergleichsmiete.
- **Verjährung übersehen** — der Bereicherungsanspruch verjährt in drei Jahren nach §§ 195, 199 BGB.
