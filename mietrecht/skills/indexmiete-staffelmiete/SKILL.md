---
name: indexmiete-staffelmiete
description: "Index- und Staffelmiete im Wohnraummietrecht – Gestaltung und Prüfung der Staffelmietvereinbarung § 557a BGB (Schriftform, betragsmäßige Staffeln, Jahresfrist, Kündigungsverzicht höchstens vier Jahre) und der Indexmietvereinbarung § 557b BGB (Schriftform, Verbraucherpreisindex, Änderungserklärung in Textform, Wirksamwerden ab dem übernächsten Monat), Sperre für §§ 558, 559 BGB (Ausnahme Heizungstausch § 555b Nr. 1a bei Indexmiete), Mietpreisbremse für jede Staffel bzw. die Ausgangsmiete §§ 557a Abs. 4, 557b Abs. 4 BGB, anhängige Indexkappung (BT-Drs. 21/6807). Rechtsstand: Oktober 2026. Use when eine Staffel- oder Indexmiete vereinbart, eine Indexanpassung erklärt oder eine erhaltene Anpassung auf Wirksamkeit und Höhe geprüft wird."
language: de
provider_variants: [claude, gemini, openai]
test: ./test.md
---

# /mietrecht:indexmiete-staffelmiete

## Zweck

Index- und Staffelmiete sind die beiden gesetzlich zugelassenen Alternativen zur Vergleichsmietenerhöhung nach § 558 BGB. Sie nehmen dem Vermieter das Mietspiegelverfahren ab, schließen es dafür aber für die Laufzeit aus. In den Inflationsjahren 2022/2023 hat die Indexmiete Mieten in kurzer Zeit stark erhöht, und deshalb steht sie im Zentrum der anhängigen Reform. Diese Skill prüft die Vereinbarung auf Wirksamkeit, rechnet eine Indexanpassung nach, spiegelt jede Staffel bzw. die Ausgangsmiete an der Mietpreisbremse und trennt geltendes Recht vom Entwurf.

**Rechtsstand: Oktober 2026.**

- **Geltend:** §§ 557a, 557b BGB in der seit 2015 bzw. 2001 bestehenden Fassung; Mietpreisbremse bis 31.12.2029 (§ 556d Abs. 2 BGB).
- **Anhängig, nicht geltend:** Regierungsentwurf eines Gesetzes zur Änderung des Rechts der Wohn- und Geschäftsraummiete (BT-Drs. 21/6807 v. 01.07.2026; Anhörung im Rechtsausschuss am 14.10.2026; Stand 23.10.2026 nicht verabschiedet). Er sieht vor, dass jährliche Indexsteigerungen **über 3 %** nur **zur Hälfte** berücksichtigt werden, und zwar nur in Gebieten, die die Landesregierung bestimmt, für höchstens fünf Jahre (§ 557b Abs. 4 BGB-E). Daneben enthält er Folgeänderungen zu § 559e BGB bei Staffelmiete.

## Eingaben

- **Vertrag** im Wortlaut: Staffel- oder Indexklausel, Datum, Form (schriftlich, § 126 BGB?)
- **Staffelmiete:** Höhe und Fälligkeit jeder Staffel, vereinbarter Kündigungsverzicht
- **Indexmiete:** Ausgangsmiete, Ausgangsindexstand (Monat), Basisjahr, letzte Anpassung (Datum, Wirksamwerden)
- **Anpassungserklärung** im Wortlaut, Zugangsdatum
- Lage: Gebiet mit **Mietpreisbremse** (Landesverordnung am Tag des Vertragsschlusses)?
- Ortsübliche Vergleichsmiete zum Mietbeginn bzw. zur Fälligkeit jeder Staffel
- Modernisierungen während der Laufzeit

## Sub-Agent-Architektur

Die Prüfung wird in Prosa von spezialisierten Schritten getragen; einen `agents`-Block trägt diese Skill bewusst nicht (mietrecht-Konvention).

- Ein **Vereinbarungs-Prüfer** klärt zuerst, ob eine wirksame Staffel- oder Indexvereinbarung vorliegt. Ohne sie gilt allein § 558 BGB.
- Ein **Anpassungs-Rechner** prüft die Indexanpassung arithmetisch und kontrolliert Jahresfrist und Wirksamwerden.
- Ein **Mietpreisbremsen-Prüfer** misst die Ausgangsmiete (Index) bzw. jede einzelne Staffel an § 556d BGB.
- Ein **Sperr-Prüfer** klärt, welche weiteren Erhöhungen (§ 558, § 559, § 559e, § 560 BGB) neben der Vereinbarung möglich bleiben.
- Ein **Reform-Prüfer** markiert, was sich nach BT-Drs. 21/6807 ändern würde und ob der Vertrag als Altvertrag geschützt wäre.

## Ablauf

### 1. Abgrenzung und Form

Staffel- und Indexmiete schließen sich gegenseitig aus. Beide verdrängen für ihre Laufzeit die Vergleichsmietenerhöhung nach § 558 BGB. Beide Vereinbarungen sind **schriftlich** zu treffen (§ 557a Abs. 1, § 557b Abs. 1 BGB), also in **Schriftform** nach [§ 126 BGB](https://www.gesetze-im-internet.de/bgb/__126.html) mit eigenhändiger Unterschrift beider Seiten (bzw. qualifizierter elektronischer Form, § 126a BGB). Eine mündliche oder nur in Textform (E-Mail) getroffene Abrede ist formnichtig (§ 125 BGB), und es bleibt bei der Festmiete mit § 558 BGB. **Textform** ([§ 126b BGB](https://www.gesetze-im-internet.de/bgb/__126b.html)) genügt nur für die **Änderungserklärung** bei der Indexmiete (§ 557b Abs. 3 BGB). Abweichungen zum Nachteil des Mieters sind unwirksam (§ 557a Abs. 5, § 557b Abs. 5 BGB).

### 2. Staffelmiete ([§ 557a BGB](https://www.gesetze-im-internet.de/bgb/__557a.html))

- **Betragsmäßig bestimmt:** Jede Staffel ist als Miete oder als Erhöhungsbetrag in EUR auszuweisen (Abs. 1). Prozentangaben genügen nicht.
- **Mindestens ein Jahr** muss die Miete jeweils unverändert bleiben (Abs. 2 S. 1).
- **Sperre:** Während der Laufzeit ist eine Erhöhung nach §§ 558 bis 559b BGB **ausgeschlossen** (Abs. 2 S. 2). Betriebskostenanpassungen nach § 560 BGB bleiben möglich.
- **Kündigungsverzicht:** Das Kündigungsrecht des Mieters kann höchstens für **vier Jahre** seit Abschluss der Vereinbarung ausgeschlossen werden (Abs. 3). Ein längerer Verzicht ist insoweit unwirksam.
- **Mietpreisbremse:** Die §§ 556d–556g BGB gelten für **jede Staffel**. Maßgeblich ist bei der zweiten und jeder weiteren Staffel die ortsübliche Vergleichsmiete im Zeitpunkt ihrer **Fälligkeit**. Eine in einer früheren Staffel wirksam begründete Miethöhe bleibt erhalten (Abs. 4).

### 3. Indexmiete ([§ 557b BGB](https://www.gesetze-im-internet.de/bgb/__557b.html))

- **Index:** zulässig ist nur der vom Statistischen Bundesamt ermittelte **Verbraucherpreisindex für Deutschland** (Abs. 1). Andere Indizes, etwa ein Baukostenindex, sind für Wohnraum unzulässig.
- **Basisjahr:** Die Klausel muss kein Basisjahr nennen (BGH, Urt. v. 26.05.2021 – VIII ZR 42/20, NZM 2021, 878, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2021-05-26&Aktenzeichen=VIII%20ZR%2042/20). Bei der Berechnung darf aber nicht mit Indexständen verschiedener Basisjahre gerechnet werden. Nach einer Umbasierung durch Destatis sind beide Stände auf derselben Basis zu verwenden.
- **Jahresfrist:** Die Miete muss, von Erhöhungen nach §§ 559 bis 560 BGB abgesehen, jeweils **mindestens ein Jahr unverändert** bleiben (Abs. 2 S. 1).
- **Sperre:** Eine Erhöhung nach § 559 oder § 559e BGB ist nur zulässig, soweit der Vermieter bauliche Maßnahmen aufgrund von Umständen durchgeführt hat, die er **nicht zu vertreten** hat, **es sei denn, es wurde eine Modernisierungsmaßnahme nach § 555b Nr. 1a BGB (Heizungsanlage) durchgeführt**; § 558 BGB ist ausgeschlossen (Abs. 2 S. 2, 3).
- **Änderungserklärung:** Die Änderung tritt nicht automatisch ein. Sie ist durch **Erklärung in Textform** geltend zu machen; dabei sind die eingetretene Änderung des Index sowie die jeweilige Miete oder die Erhöhung in einem Geldbetrag anzugeben (Abs. 3 S. 1, 2). Die geänderte Miete ist **mit Beginn des übernächsten Monats** nach dem Zugang der Erklärung zu zahlen (Abs. 3 S. 3). Eine rückwirkende Anpassung gibt es nicht.
- **Mietpreisbremse:** Die §§ 556d–556g BGB gelten nur für die **Ausgangsmiete** (Abs. 4). Spätere Indexanpassungen werden an § 556d BGB nicht gemessen.
- **Senkung:** Sinkt der Index, kann auch der Mieter die Anpassung nach unten verlangen. Eine Klausel, die nur Erhöhungen zulässt, verstößt gegen § 557b Abs. 5 BGB.

### 4. Indexanpassung nachrechnen

```
Neue Miete = bisherige Nettokaltmiete × (Indexstand neu / Indexstand bei letzter Anpassung)
```

Prüfschritte:

1. Indexstände desselben Basisjahres verwenden.
2. Den Ausgangsmonat der Klausel und den Monat der letzten Anpassung zugrunde legen, nicht den Monat der Erklärung.
3. Wirksamwerden der letzten Anpassung + 12 Monate ≤ Wirksamwerden der neuen Anpassung.
4. Zugang + übernächster Monatsbeginn = Wirksamwerden.

Eine Erklärung ohne Angabe beider Indexstände oder ohne Geldbetrag ist unwirksam.

### 5. Verhältnis zur Modernisierung und zum Heizungstausch

- Bei der **Staffelmiete** sperrt § 557a Abs. 2 S. 2 BGB nach dem Wortlaut Erhöhungen nach §§ 558 bis 559b BGB. Ob auch **§ 559e BGB** gesperrt ist, ist **offen** `[unverifiziert – prüfen]`; der Regierungsentwurf will ihn ausdrücklich in die Sperre aufnehmen (BT-Drs. 21/6807, Folgeänderung zu § 557a BGB).
- Bei der **Indexmiete** sind grundsätzlich nur Maßnahmen umlagefähig, die der Vermieter nicht zu vertreten hat, etwa gesetzliche Pflichten. Für den **Heizungstausch** (§ 555b Nr. 1a BGB) gilt diese Einschränkung nicht: Er ist nach § 559 oder § 559e BGB umlagefähig (§ 557b Abs. 2 S. 2 Hs. 2 BGB); Vertiefung: `/mietrecht:heizungstausch-559e-559f`.

### 6. Anhängige Reform: Indexkappung (BT-Drs. 21/6807)

Der Regierungsentwurf ([BT-Drs. 21/6807](https://dserver.bundestag.de/btd/21/068/2106807.pdf)) sieht vor:

- Übersteigt die Indexsteigerung **3 % pro Jahr**, wird der übersteigende Teil nur **zur Hälfte** berücksichtigt (§ 557b Abs. 4 BGB-E).
- Das gilt nur in Gebieten, die die Landesregierung durch Verordnung bestimmt, für höchstens **fünf Jahre**.
- Die übrigen Teile sollen am Tag nach Verkündung in Kraft treten.

**Handhabung bis zur Verkündung:** Anpassungen sind nach geltendem Recht ohne Kappung zu berechnen. Bei Gestaltung neuer Verträge ist eine Alternativrechnung mit Kappung beizufügen. Die Übergangsvorschrift ist nach Verkündung im Wortlaut zu prüfen.

## Deterministische Berechnung

Die Jahresfrist und das Wirksamwerden sind Fristen nach §§ 187 ff. BGB. Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht **nur die Arithmetik**; das Wirksamwerden der letzten Anpassung und der Zugang bleiben juristische Eingaben.

```bash
# Jahresfrist § 557b Abs. 2 S. 1 BGB: letzte Anpassung wirksam ab 01.03.2025 (Beginnfrist, ohne § 193 BGB)
# → Fristende 28.02.2026; die neue Miete kann ab 01.03.2026 gelten
python -m scripts.legal_calc.cli frist --ereignis 01.03.2025 --menge 12 --einheit monate --art beginn --kein-rollover --land BE

# Kündigungsverzicht § 557a Abs. 3 BGB: Vereinbarung vom 15.06.2023, längstens vier Jahre
python -m scripts.legal_calc.cli frist --ereignis 15.06.2023 --menge 4 --einheit jahre --land BE
```

Das „übernächste Monat"-Wirksamwerden des § 557b Abs. 3 S. 3 BGB ist eine Kalenderregel, keine Fristberechnung. Bei Zugang am 20.10.2026 ist die neue Miete ab dem 01.12.2026 zu zahlen. Das ist von Hand gegen den Wortlaut zu prüfen.

## Quellen

### Statute

- [§ 557 BGB](https://www.gesetze-im-internet.de/bgb/__557.html), [§ 557a BGB](https://www.gesetze-im-internet.de/bgb/__557a.html), [§ 557b BGB](https://www.gesetze-im-internet.de/bgb/__557b.html)
- [§ 556d BGB](https://www.gesetze-im-internet.de/bgb/__556d.html), [§ 556g BGB](https://www.gesetze-im-internet.de/bgb/__556g.html), [§ 558 BGB](https://www.gesetze-im-internet.de/bgb/__558.html), [§ 559 BGB](https://www.gesetze-im-internet.de/bgb/__559.html), [§ 559e BGB](https://www.gesetze-im-internet.de/bgb/__559e.html), [§ 560 BGB](https://www.gesetze-im-internet.de/bgb/__560.html)
- [§ 126b BGB](https://www.gesetze-im-internet.de/bgb/__126b.html) (Textform), [§ 187 BGB](https://www.gesetze-im-internet.de/bgb/__187.html), [§ 188 BGB](https://www.gesetze-im-internet.de/bgb/__188.html)
- [PrKG](https://www.gesetze-im-internet.de/prklg/) (für Gewerberaum; für Wohnraum ist § 557b BGB vorrangig)

### Gesetzgebung

- Regierungsentwurf, BT-Drs. 21/6807 v. 01.07.2026 — https://dserver.bundestag.de/btd/21/068/2106807.pdf (Stand 23.10.2026: nach Anhörung im Rechtsausschuss am 14.10.2026, nicht verabschiedet)

### Kommentare

- Börstinghaus, in: Schmidt-Futterer, Mietrecht, 16. Aufl. 2024, § 557a BGB, § 557b BGB (Rn. vor Zitat prüfen)
- Artz, in: MüKoBGB, 9. Aufl. 2023, § 557b Rn. 1 ff. `[unverifiziert – prüfen]`
- Weidenkaff, in: Grüneberg, BGB, 84. Aufl. 2025, § 557b Rn. 1 ff. (85. Aufl. 2026 auf Erscheinen prüfen)

### Rechtsprechung

- BGH, Urt. v. 26.05.2021 – VIII ZR 42/20, NJW-RR 2021, 1096 = NZM 2021, 878 (Wirksamkeit der Indexmietvereinbarung; Angabe eines Basisjahres nicht erforderlich) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2021-05-26&Aktenzeichen=VIII%20ZR%2042/20
- Zur AGB-Kontrolle von Indexklauseln ohne Obergrenze in Zeiten hoher Inflation ist die instanzgerichtliche Rechtsprechung heranzuziehen `[unverifiziert – prüfen]`.

## Formulierungshilfe — Indexanpassungserklärung (§ 557b Abs. 3 BGB)

```
Sehr geehrte Frau …, sehr geehrter Herr …,

nach § <…> des Mietvertrags vom <Datum> ist die Nettokaltmiete an den vom
Statistischen Bundesamt ermittelten Verbraucherpreisindex für Deutschland
gekoppelt. Ich mache hiermit eine Änderung der Miete geltend.

Die Miete ist seit dem <Datum Wirksamwerden letzte Anpassung> unverändert.
Der Index (Basis <Jahr> = 100) betrug im <Monat/Jahr der letzten Anpassung>
<…> Punkte und beträgt im <Monat/Jahr aktuell> <…> Punkte. Das entspricht
einer Änderung um <…> %.

Die Nettokaltmiete ändert sich damit von <Betrag> EUR auf <Betrag> EUR
monatlich, also um <Betrag> EUR. Die geänderte Miete ist ab dem <Beginn des
übernächsten Monats nach Zugang> zu zahlen.

Mit freundlichen Grüßen
```

## Ausgabeformat

```
INDEX- / STAFFELMIETE — Prüfung — <Mandat-ID> — <Datum>

I.    Vereinbarungstyp                 [Staffel § 557a / Index § 557b / keine → § 558]
      Schriftform § 126 BGB             [✅ / ❌ → Festmiete]
II.   Staffelmiete
      - Staffeln betragsmäßig          [✅ / ❌]
      - Jahresabstand                  [✅ / ❌ Staffel Nr. …]
      - Kündigungsverzicht             <Dauer>  [≤ 4 Jahre / insoweit unwirksam]
      - Mietpreisbremse je Staffel     [N/A / Staffel Nr. … überhöht]
III.  Indexmiete
      - VPI Deutschland                [✅ / anderer Index ❌]
      - Ausgangsmiete § 556d           [N/A / zulässig / überhöht]
      - Letzte Anpassung wirksam ab    <Datum>   Jahresfrist bis <Datum>
      - Indexstände (gleiche Basis)    <alt> → <neu>  (+<…> %)
      - Erklärung Textform + Betrag    [✅ / ❌]
      - Wirksam ab                     <Datum>
      - Rechnerische neue Miete        <Betrag>  [Forderung korrekt / überhöht um …]
IV.   Sperre weiterer Erhöhungen       [§ 558 gesperrt / Index: §§ 559, 559e nur bei Nichtvertretenmüssen oder § 555b Nr. 1a /
                                        Staffel: §§ 558–559b gesperrt, § 559e offen]
V.    Reform BT-Drs. 21/6807           [nicht verabschiedet — Alternativrechnung 3-%-Kappung: <Betrag>]

Ergebnis: <wirksam / teilweise / unwirksam>
Risiko: [🟢 / 🟡 / 🔴]
```

## Beispiel (Gutachtenstil, Kurzform)

Vermieter V erklärt am 20.10.2026 per E-Mail eine Indexanpassung von 1.000 EUR auf 1.080 EUR „ab sofort". Die letzte Anpassung wirkte ab dem 01.12.2025.

Die Erklärung genügt der Textform (§ 126b BGB). Die Jahresfrist des § 557b Abs. 2 S. 1 BGB wäre erst mit Ablauf des 30.11.2026 gewahrt. Nach § 557b Abs. 3 S. 3 BGB ist die geänderte Miete ohnehin erst ab dem übernächsten Monat nach Zugang, also ab dem 01.12.2026, zu zahlen, sodass die Jahresfrist im Ergebnis eingehalten ist. Die Erklärung ist aber unwirksam, wenn sie die Indexstände nicht angibt (Abs. 3 S. 2). Das „ab sofort" ist als Erklärung mit gesetzlichem Wirksamwerden auszulegen.

## Risiken / typische Fehler

- **Indexstände verschiedener Basisjahre gemischt** — die Prozentänderung ist dann falsch; nach Umbasierung beide Werte auf derselben Basis verwenden.
- **Anpassung rückwirkend verlangt** — die geänderte Miete ist erst ab dem übernächsten Monat nach Zugang der Textform-Erklärung geschuldet.
- **Jahresfrist übersehen** — zwischen zwei Anpassungen muss die Miete mindestens ein Jahr unverändert bleiben.
- **Vereinbarung nur per E-Mail getroffen** — §§ 557a, 557b Abs. 1 BGB verlangen Schriftform; ohne sie gilt die Festmiete.
- **Heizungstausch bei Indexmiete für gesperrt gehalten** — § 557b Abs. 2 S. 2 BGB lässt die Erhöhung für Maßnahmen nach § 555b Nr. 1a BGB zu.
- **Staffel in Prozent statt in EUR** — die Staffelvereinbarung ist unwirksam; es gilt § 558 BGB.
- **Mietpreisbremse nur auf die erste Staffel angewendet** — § 557a Abs. 4 BGB verlangt die Prüfung jeder Staffel zum Zeitpunkt ihrer Fälligkeit; bei der Indexmiete nur die Ausgangsmiete.
- **Mieterhöhung nach § 558 BGB neben der Indexmiete verlangt** — gesperrt (§ 557b Abs. 2 S. 3 BGB).
- **Kündigungsverzicht über vier Jahre** — insoweit unwirksam (§ 557a Abs. 3 BGB).
- **Indexkappung des Entwurfs angewendet** — § 557b Abs. 4 BGB-E ist bisher nur Regierungsentwurf (BT-Drs. 21/6807).
