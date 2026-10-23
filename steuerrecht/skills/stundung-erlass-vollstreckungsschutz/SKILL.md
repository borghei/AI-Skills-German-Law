---
name: stundung-erlass-vollstreckungsschutz
description: "Zahlungsschwierigkeiten gegenüber dem Finanzamt – Stundung § 222 AO mit Stundungszinsen § 234 AO, Erlass aus sachlichen oder persönlichen Billigkeitsgründen § 227 AO (Erlassbedürftigkeit, Erlasswürdigkeit), Säumniszuschläge § 240 AO (verfassungsgemäß, BFH XI R 18/23) und ihr hälftiger Erlass, Vollstreckungsvoraussetzungen §§ 249, 254 AO, Vollstreckungsaufschub § 258 AO, Kontopfändung §§ 309, 314 AO mit P-Konto-Schutz § 850k ZPO, Vermögensauskunft § 284 AO, Rechtsschutz durch Einspruch und einstweilige Anordnung § 114 FGO, Zahlungsverjährung § 228 AO. Rechtsstand Oktober 2026, mit Hinweis auf die geplante elektronische Kontopfändung (§ 309a, Entwurf JStG 2026). Use when ein Mandant Steuern nicht fristgerecht zahlen kann, Säumniszuschläge angefallen sind oder das Finanzamt vollstreckt."
language: de
provider_variants:
  - claude
  - gemini
  - openai
test: ./test.md
---

# /steuerrecht:stundung-erlass-vollstreckungsschutz

> **Rechtsstand: Oktober 2026.** §§ 222, 227, 234, 240, 249 ff., 258, 309 AO sind 2025–2026 unverändert. Der BFH hat die Höhe der Säumniszuschläge auch für Zeiträume nach 2018 bestätigt ([BFH, Urt. v. 19.02.2025 – XI R 18/23](https://www.bundesfinanzhof.de/en/entscheidungen/entscheidungen-online/decision-detail/STRE202520150/)). Entwurf JStG 2026 (BT-Drs. 21/8283, nicht verabschiedet): elektronische Pfändung bei Kreditinstituten über einen neuen § 309a — anwendbar erst ab einer gesonderten Bekanntmachung des BMF im BGBl.

## Zweck

Wer die festgesetzte Steuer nicht zahlen kann, hat vier Hebel: Stundung vor Fälligkeit, Vollstreckungsaufschub nach Fälligkeit, Erlass bei Unbilligkeit und den Rechtsschutz gegen einzelne Vollstreckungsmaßnahmen. Dazu kommen Säumniszuschläge von 1 % je Monat, die schnell zum eigentlichen Problem werden. Dieser Skill ordnet die Lage des Mandanten dem richtigen Instrument zu, bereitet den Antrag mit Liquiditätsnachweis vor und sichert gegen Kontopfändung und Insolvenzantrag ab.

## Eingaben

- Rückstände (Steuerart, Betrag, Fälligkeit), bereits angefallene Säumniszuschläge, Vollstreckungsmaßnahmen (Pfändungs- und Einziehungsverfügung, Vollziehungsbeamter, Ladung zur Vermögensauskunft, Insolvenzantrag angekündigt?)
- Liquiditätsstatus und Liquiditätsplanung (Einnahmen, Ausgaben, Kredite, Sicherheiten), Gründe der Zahlungsschwierigkeit
- Steuerliches Verhalten in der Vergangenheit (pünktliche Erklärungen und Zahlungen?)
- Ist der Bescheid selbst streitig? (dann AdV vorrangig — `/steuerrecht:aussetzung-der-vollziehung`)
- Bei Unternehmen: Insolvenzreife (Zahlungsunfähigkeit, Überschuldung), Geschäftsführerhaftung (`/steuerrecht:haftungsbescheid`)

## Sub-Agent-Architektur

Ein **Lage-Prüfer** trennt streitige von unstreitigen Rückständen und ordnet nach Fälligkeit. Ein **Instrumenten-Prüfer** wählt zwischen Stundung, Vollstreckungsaufschub, Erlass und AdV. Ein **Liquiditäts-Prüfer** baut den Zahlungsplan und die Glaubhaftmachung. Ein **Vollstreckungs-Prüfer** prüft jede Maßnahme auf Rechtmäßigkeit, Pfändungsschutz und Rechtsbehelf.

## Ablauf

### 1. Instrument wählen

| Lage | Instrument | Norm |
|---|---|---|
| Bescheid streitig | Aussetzung der Vollziehung | § 361 AO, § 69 FGO |
| Steuer unstreitig, **vor** Fälligkeit, vorübergehender Engpass | **Stundung** | § 222 AO |
| Steuer unstreitig, **nach** Fälligkeit, Vollstreckung droht | **Vollstreckungsaufschub** / einstweilige Einstellung | § 258 AO |
| Einziehung wäre unbillig | **Erlass** | § 227 AO |
| Nur Säumniszuschläge belastend | Teil-/Vollerlass Säumniszuschläge | § 227 AO i. V. m. § 240 AO |
| Erlass/Stundung abgelehnt, Vollstreckung läuft | Einspruch + **einstweilige Anordnung** | § 347 AO, § 114 FGO |

### 2. Stundung ([§ 222 AO](https://www.gesetze-im-internet.de/ao_1977/__222.html))

- Voraussetzungen: Einziehung bei Fälligkeit wäre eine **erhebliche Härte** für den Schuldner, und der Anspruch erscheint durch die Stundung **nicht gefährdet**. Ermessen.
- **Stundungsbedürftigkeit**: vorübergehende Zahlungsschwierigkeiten, die nicht vom Steuerpflichtigen zu vertreten sind; Kreditaufnahme oder Vermögensverwertung zumutbar? **Stundungswürdigkeit**: Verhalten des Steuerpflichtigen.
- In der Regel nur gegen **Sicherheitsleistung** (§ 222 S. 2 AO); Ratenstundung mit Widerrufsvorbehalt üblich.
- **Nicht** stundbar: Steuerabzugsbeträge (Lohnsteuer, Kapitalertragsteuer) gegenüber dem Entrichtungspflichtigen (§ 222 S. 3, 4 AO).
- **Stundungszinsen** 0,5 % je Monat ([§ 234 AO](https://www.gesetze-im-internet.de/ao_1977/__234.html)); Verzicht möglich, wenn die Erhebung unbillig wäre (§ 234 Abs. 2 AO). Säumniszuschläge entfallen für den Stundungszeitraum.
- Antrag **vor Fälligkeit** stellen und Liquiditätsplan beifügen; ein Antrag allein hemmt weder Fälligkeit noch Säumniszuschläge.

### 3. Vollstreckungsaufschub ([§ 258 AO](https://www.gesetze-im-internet.de/ao_1977/__258.html))

- Soweit die Vollstreckung **im Einzelfall unbillig** ist, kann die Vollstreckungsbehörde sie einstweilen einstellen, beschränken oder Maßnahmen aufheben.
- Unbillig ist die Vollstreckung, wenn sie dem Schuldner einen unangemessenen Nachteil bringt, der durch kurzfristiges Zuwarten vermieden werden kann — typisch: konkret absehbarer Zahlungseingang, Ratenplan.
- Anders als die Stundung **lässt der Aufschub Säumniszuschläge weiterlaufen**; in der Praxis „Vollstreckungsaufschub gegen Raten".

### 4. Erlass ([§ 227 AO](https://www.gesetze-im-internet.de/ao_1977/__227.html))

- **Sachliche Unbilligkeit**: Die Einziehung widerspricht im Einzelfall dem Gesetzeszweck (vom Gesetzgeber nicht bedachte Härte); keine Korrektur bestandskräftiger, nur „falscher" Bescheide über den Erlass.
- **Persönliche Unbilligkeit**: **Erlassbedürftigkeit** (Existenzgefährdung, Unmöglichkeit, die Steuer aus Vermögen/Einkommen zu zahlen) und **Erlasswürdigkeit** (der Steuerpflichtige hat die mangelnde Leistungsfähigkeit nicht selbst herbeigeführt und nicht gegen die Interessen der Allgemeinheit verstoßen). Erlass scheidet aus, wenn er nur anderen Gläubigern zugutekäme.
- Rechtsschutz: Einspruch, dann **Verpflichtungsklage**; das FG prüft nur Ermessensfehler ([§ 102 FGO](https://www.gesetze-im-internet.de/fgo/__102.html)).
- Bei Billigkeitsfragen, die die Festsetzung betreffen, parallel abweichende Festsetzung nach § 163 AO beantragen (Grundlagenentscheidung für den Erlass).

### 5. Säumniszuschläge ([§ 240 AO](https://www.gesetze-im-internet.de/ao_1977/__240.html))

- **1 %** des auf 50 EUR abgerundeten rückständigen Betrags für **jeden angefangenen Monat** der Säumnis; entstehen kraft Gesetzes.
- **Schonfrist** drei Tage bei Überweisung (§ 240 Abs. 3 AO); nicht bei Bar- oder Scheckzahlung. Zahlungstag bei Überweisung: Gutschrift auf dem Konto der Finanzbehörde, bei SEPA-Lastschrift der Fälligkeitstag (§ 224 Abs. 2 AO).
- Verfassungsmäßigkeit: Der BFH hat ernstliche Zweifel verneint; Säumniszuschläge sind Druckmittel und Gegenleistung, nicht Zins (BFH, Urt. v. 19.02.2025 – XI R 18/23, s. o.).
- **Erlass zur Hälfte**: Bei **Überschuldung und Zahlungsunfähigkeit** verliert der Säumniszuschlag seine Druckfunktion; nach st. Rspr. ist er dann regelmäßig zur Hälfte zu erlassen (der Zinsanteil bleibt) `[unverifiziert – prüfen]`.
- **Voll-Erlass**: Wurde ein Bescheid später aufgehoben, bleiben verwirkte Zuschläge bestehen (§ 240 Abs. 1 S. 4 AO) — Erlass aus sachlichen Gründen nur, wenn AdV hätte gewährt werden müssen und der Steuerpflichtige alles Zumutbare getan hat, sie zu erlangen `[unverifiziert – prüfen]`.

### 6. Vollstreckung durch das Finanzamt ([§§ 249 ff. AO](https://www.gesetze-im-internet.de/ao_1977/__249.html))

- **Voraussetzungen** ([§ 254 AO](https://www.gesetze-im-internet.de/ao_1977/__254.html)): Leistungsgebot, Fälligkeit, Ablauf **einer Woche** seit Bekanntgabe des Leistungsgebots; Mahnung soll in der Regel vorausgehen (§ 259 AO). Selbstberechnete Steuern (Anmeldungen) bedürfen keines Leistungsgebots.
- **Kontopfändung**: Pfändungs- und Einziehungsverfügung ([§ 309 AO](https://www.gesetze-im-internet.de/ao_1977/__309.html), [§ 314 AO](https://www.gesetze-im-internet.de/ao_1977/__314.html)) — die Behörde ist ihr eigener Vollstreckungstitel.
- **Pfändungsschutz**: Über § 309 Abs. 3 und § 319 AO gelten die Schutzvorschriften der ZPO; **Pfändungsschutzkonto** ([§ 850k ZPO](https://www.gesetze-im-internet.de/zpo/__850k.html)) einrichten (Umwandlung binnen eines Monats wirkt zurück); Freibetragserhöhung über Bescheinigung (§ 903 ZPO) oder Antrag an die Vollstreckungsstelle (§ 850l ZPO entsprechend, bei Unpfändbarkeit).
- **Vermögensauskunft** ([§ 284 AO](https://www.gesetze-im-internet.de/ao_1977/__284.html)): Folge ist Eintragung ins Schuldnerverzeichnis — mit Zahlungsplan abwenden.
- **Insolvenzantrag** des Finanzamts (§ 14 InsO) als Druckmittel: frühzeitige Kommunikation mit der Vollstreckungsstelle; bei Unternehmen Insolvenzantragspflicht (§ 15a InsO) eigenständig prüfen.
- **Entwurf JStG 2026 — elektronische Kontopfändung**: Pfändung bei Kreditinstituten nach amtlichem Datensatz über sichere Übermittlungswege, Zustellung an ein elektronisches Postfach der Bank; anwendbar erst ab Bekanntmachung des BMF über die technischen Voraussetzungen. Für den Mandanten: kürzere Reaktionszeit zwischen Verfügung und Kontosperre einkalkulieren.

### 7. Rechtsschutz in der Vollstreckung

- **Einspruch** gegen jede Vollstreckungsmaßnahme (§ 347 AO); Einwendungen gegen den zugrunde liegenden Steuerbescheid sind hier ausgeschlossen (§ 256 AO).
- **AdV** einer Pfändungsverfügung möglich (§ 361 AO, § 69 FGO); gegen die **Ablehnung** von Stundung, Erlass oder Vollstreckungsaufschub nur **einstweilige Anordnung** ([§ 114 FGO](https://www.gesetze-im-internet.de/fgo/__114.html)) — Anordnungsanspruch und -grund glaubhaft machen.
- **Zahlungsverjährung** ([§ 228 AO](https://www.gesetze-im-internet.de/ao_1977/__228.html)): fünf Jahre, zehn Jahre bei Hinterziehung; Unterbrechung u. a. durch Stundung, Vollstreckungsmaßnahmen, schriftliche Geltendmachung (§ 231 AO).

## Ausgabeformat

```
ZAHLUNGSSCHWIERIGKEITEN / VOLLSTRECKUNG — <Mandant> — <Datum> — Rechtsstand Oktober 2026

I.    Rückstände
      <Steuerart — Betrag — Fälligkeit — streitig ja/nein>
      Säumniszuschläge bisher (§ 240): <EUR>

II.   Instrument
      [AdV / Stundung § 222 / Vollstreckungsaufschub § 258 / Erlass § 227 / einstweilige Anordnung § 114 FGO]
      Begründung:                     <…>

III.  Antrag
      Erhebliche Härte / Unbilligkeit: <…>
      Liquiditätsplan / Raten:        <…>
      Sicherheiten:                   <…>
      Stundungszinsen (§ 234) / Verzicht: <EUR / beantragt>

IV.   Säumniszuschläge
      Hälftiger Erlass (Überschuldung + Zahlungsunfähigkeit): [✓ / ✗]
      Voll-Erlass (AdV wäre zu gewähren gewesen): [✓ / ✗]

V.    Vollstreckung
      Maßnahme / Datum:               <Pfändungs- und Einziehungsverfügung vom …>
      Voraussetzungen § 254:          [✓ / Mangel: …]
      Pfändungsschutz (P-Konto § 850k ZPO): [eingerichtet / einzurichten]
      Rechtsbehelf:                   [Einspruch + AdV / einstweilige Anordnung]

VI.   Zahlungsverjährung (§ 228):     <Ende …>
```

## Beispiel (Gutachtenstil, verkürzt)

Die Einzelunternehmerin U schuldet ESt-Nachzahlung 2024 von 18.000 EUR, fällig am 16.11.2026; ein Großkunde zahlt 25.000 EUR erst im Februar 2027, der Eingang ist vertraglich belegt. Fraglich ist eine Stundung nach § 222 AO. Eine erhebliche Härte liegt vor, weil die Zahlung bei Fälligkeit nur durch Aufnahme eines kurzfristigen Kredits zu Konditionen möglich wäre, die über den Stundungszinsen liegen, und der Engpass vorübergehend ist. Der Anspruch ist nicht gefährdet: Die Forderung gegen den Kunden kann zur Sicherheit abgetreten werden. U hat ihre Steuern bisher pünktlich gezahlt (Stundungswürdigkeit). Ergebnis: Stundung bis 28.02.2027 gegen Abtretung ist zu beantragen, und zwar **vor** dem 16.11.2026; die Stundungszinsen (0,5 % je Monat, § 234 AO) sind einzukalkulieren.

## Risiken / typische Fehler

- **Stundung nach Fälligkeit beantragt** — Säumniszuschläge sind bereits verwirkt; dann nur noch Vollstreckungsaufschub, unter dem Säumniszuschläge weiterlaufen.
- **Kein Liquiditätsnachweis** — Anträge ohne Zahlungsplan und Belege werden abgelehnt.
- **Lohnsteuer gestundet erwartet** — Abzugsbeträge sind nicht stundbar; Haftungsrisiko des Geschäftsführers (§ 69 AO).
- **Falscher Rechtsschutz** — gegen abgelehnte Stundung oder Erlass keine AdV, sondern einstweilige Anordnung nach § 114 FGO.
- **Säumniszuschläge** unkritisch hingenommen — hälftiger Erlass bei Überschuldung und Zahlungsunfähigkeit prüfen.
- **P-Konto zu spät** — ohne Pfändungsschutzkonto ist das Guthaben blockiert; Umwandlung sofort beantragen.
- **Einwendungen gegen den Bescheid im Vollstreckungsverfahren** — ausgeschlossen (§ 256 AO); dafür Einspruch/Korrektur gegen den Bescheid.
- **Insolvenzreife ignoriert** — Zahlungen an das Finanzamt in der Krise können anfechtbar sein (§§ 130 ff. InsO); Antragspflicht § 15a InsO.

## Quellen

### Statute

- [§ 222 AO](https://www.gesetze-im-internet.de/ao_1977/__222.html), [§ 224 AO](https://www.gesetze-im-internet.de/ao_1977/__224.html), [§ 227 AO](https://www.gesetze-im-internet.de/ao_1977/__227.html), [§ 228 AO](https://www.gesetze-im-internet.de/ao_1977/__228.html), [§ 231 AO](https://www.gesetze-im-internet.de/ao_1977/__231.html), [§ 234 AO](https://www.gesetze-im-internet.de/ao_1977/__234.html), [§ 240 AO](https://www.gesetze-im-internet.de/ao_1977/__240.html), [§ 163 AO](https://www.gesetze-im-internet.de/ao_1977/__163.html)
- [§ 249 AO](https://www.gesetze-im-internet.de/ao_1977/__249.html), [§ 254 AO](https://www.gesetze-im-internet.de/ao_1977/__254.html), [§ 256 AO](https://www.gesetze-im-internet.de/ao_1977/__256.html), [§ 258 AO](https://www.gesetze-im-internet.de/ao_1977/__258.html), [§ 259 AO](https://www.gesetze-im-internet.de/ao_1977/__259.html), [§ 284 AO](https://www.gesetze-im-internet.de/ao_1977/__284.html), [§ 309 AO](https://www.gesetze-im-internet.de/ao_1977/__309.html), [§ 314 AO](https://www.gesetze-im-internet.de/ao_1977/__314.html), [§ 319 AO](https://www.gesetze-im-internet.de/ao_1977/__319.html)
- [§ 850k ZPO](https://www.gesetze-im-internet.de/zpo/__850k.html), [§ 903 ZPO](https://www.gesetze-im-internet.de/zpo/__903.html)
- [§ 102 FGO](https://www.gesetze-im-internet.de/fgo/__102.html), [§ 114 FGO](https://www.gesetze-im-internet.de/fgo/__114.html)
- [§ 14 InsO](https://www.gesetze-im-internet.de/inso/__14.html), [§ 15a InsO](https://www.gesetze-im-internet.de/inso/__15a.html)

### Gesetzgebung (nicht in Kraft)

- Regierungsentwurf JStG 2026, BT-Drs. 21/8283, Art. 18 Nr. 15 (elektronische Pfändung bei einem Kreditinstitut), Art. 20 Nr. 2 (Anwendung erst nach BMF-Bekanntmachung)

### Verwaltungsanweisungen

- AEAO zu §§ 222, 227, 240, 258 AO; Vollstreckungsanweisung (VollzA) `[unverifiziert – prüfen]`

### Rechtsprechung

- [BFH, Urt. v. 19.02.2025 – XI R 18/23](https://www.bundesfinanzhof.de/en/entscheidungen/entscheidungen-online/decision-detail/STRE202520150/) (Säumniszuschläge verfassungsgemäß)
- BFH-Linie zum hälftigen Erlass von Säumniszuschlägen bei Überschuldung und Zahlungsunfähigkeit — Az. in juris ermitteln `[unverifiziert – prüfen]`

### Literatur

- Loose, in: Tipke/Kruse, AO/FGO, §§ 222, 227 AO `[unverifiziert – prüfen]`
- Suchstring juris: „§ 258 AO Vollstreckungsaufschub einstweilige Anordnung § 114 FGO"
