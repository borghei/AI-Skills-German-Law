---
name: aussetzung-der-vollziehung
description: "Antrag auf Aussetzung (und Aufhebung) der Vollziehung eines Steuerbescheids bei Finanzamt und Finanzgericht – ernstliche Zweifel und unbillige Härte § 361 Abs. 2 AO, Begrenzung auf die Abschlusszahlung § 361 Abs. 2 S. 4 AO, Folgebescheide § 361 Abs. 3 AO, Sicherheitsleistung, Zugangsvoraussetzung § 69 Abs. 4 FGO, Beschwerde § 128 Abs. 3 FGO, Aussetzungszinsen § 237 AO (anhängige BFH-Vorlage an das BVerfG), Abwägung gegen Säumniszuschläge § 240 AO. Rechtsstand Oktober 2026. Use when nach Einspruch oder Klage die Zahlung einer streitigen Steuer bis zur Entscheidung abgewendet werden soll."
language: de
provider_variants:
  - claude
  - gemini
  - openai
test: ./test.md
---

# /steuerrecht:aussetzung-der-vollziehung

> **Rechtsstand: Oktober 2026.** Geltendes Recht: § 361 AO, § 69 FGO, § 237 AO unverändert. Anhängig: BVerfG – 1 BvL 8/24 zur Höhe der Aussetzungszinsen `[unverifiziert – prüfen]`. Entwurf JStG 2026 (BT-Drs. 21/8283, nicht verabschiedet): Die Begrenzung des § 361 Abs. 2 S. 4 AO soll über § 1 Abs. 2 Nr. 7 AO auch für Gemeinden (Grundsteuer, Gewerbesteuer) gelten.

## Zweck

Einspruch und Klage haben keine aufschiebende Wirkung (§ 361 Abs. 1 AO, § 69 Abs. 1 FGO): Die streitige Steuer bleibt fällig, Säumniszuschläge laufen, die Vollstreckung droht. Die Aussetzung der Vollziehung (AdV) ist deshalb nach jeder Außenprüfung und jedem streitigen Bescheid die erste praktische Frage des Mandanten. Dieser Skill prüft Zulässigkeit, Begründetheit und Umfang eines AdV-Antrags beim Finanzamt und beim Finanzgericht, kalkuliert das Zinsrisiko und formuliert die Anträge.

## Eingaben

- Angefochtener Verwaltungsakt (Art, Datum, Steuerart, Betrag), Stand des Einspruchs- oder Klageverfahrens
- Fälligkeit, bereits gezahlte Beträge, laufende Vollstreckung
- Streitpunkte und ihre Begründung (Rechtsfrage / Tatsachenfrage / Schätzung)
- Anzurechnende Steuerabzugsbeträge und festgesetzte Vorauszahlungen (für § 361 Abs. 2 S. 4 AO)
- Wirtschaftliche Lage (Liquidität, drohende Existenzgefährdung, Sicherheiten)
- Grundlagenbescheid / Folgebescheid-Verhältnis

## Sub-Agent-Architektur

Ein **Zulässigkeits-Prüfer** klärt, ob ein vollziehbarer Verwaltungsakt angefochten ist und welche Stelle zuständig ist. Ein **Zweifels-Prüfer** baut die ernstlichen Zweifel auf (Rechts- und Tatsachenebene). Ein **Umfangs-Prüfer** berechnet den aussetzbaren Betrag nach § 361 Abs. 2 S. 4 AO und prüft Folgebescheide. Ein **Kosten-Prüfer** vergleicht Aussetzungszinsen, Säumniszuschläge und Erstattungszinsen und empfiehlt AdV oder Zahlung unter Vorbehalt.

## Ablauf

### 1. Statthaftigkeit: vollziehbarer, angefochtener Verwaltungsakt

- AdV setzt einen **angefochtenen** Verwaltungsakt voraus: Einspruch oder Klage muss eingelegt sein bzw. gleichzeitig eingelegt werden (§ 361 Abs. 1 AO, § 69 Abs. 2 FGO).
- **Vollziehbar** sind belastende, auf Leistung gerichtete Verwaltungsakte: Steuer-, Haftungs-, Zins-, Feststellungsbescheide (mittelbar über Folgebescheide), Prüfungsanordnungen.
- **Nicht** aussetzbar sind Ablehnungen begünstigender Verwaltungsakte (z. B. abgelehnte Stundung, abgelehnter Erlass, abgelehnte Erstattung) — hier ist die **einstweilige Anordnung** nach [§ 114 FGO](https://www.gesetze-im-internet.de/fgo/__114.html) der richtige Weg. Ausnahme: negative Feststellungsbescheide und Bescheide, die eine Erstattung mindern, nach der Rspr. teilweise aussetzbar `[unverifiziert – prüfen]`.

### 2. Zuständigkeit und Zugang zum Gericht

- **Finanzamt**: die Behörde, die den Verwaltungsakt erlassen hat (§ 361 Abs. 2 S. 1 AO, § 69 Abs. 2 FGO). Auch während des Klageverfahrens bleibt das Finanzamt zuständig.
- **Finanzgericht**: Antrag beim Gericht der Hauptsache ([§ 69 Abs. 3 FGO](https://www.gesetze-im-internet.de/fgo/__69.html)); auch schon vor Klageerhebung.
- **Zugangsvoraussetzung** (§ 69 Abs. 4 FGO): Der gerichtliche Antrag ist nur zulässig, wenn die Behörde einen AdV-Antrag ganz oder teilweise **abgelehnt** hat — es sei denn, sie hat ohne Mitteilung eines zureichenden Grundes **nicht in angemessener Frist** entschieden oder eine **Vollstreckung droht** (konkrete Vollstreckungsmaßnahmen angekündigt oder eingeleitet). Ein fehlender Vorantrag ist nicht nachholbar; der Antrag wird unzulässig verworfen.
- Gegen den Beschluss des FG: **Beschwerde** zum BFH nur, wenn sie zugelassen wurde ([§ 128 Abs. 3 FGO](https://www.gesetze-im-internet.de/fgo/__128.html)). Änderungsantrag nach § 69 Abs. 6 S. 2 FGO bei veränderten Umständen.

### 3. Begründetheit ([§ 361 Abs. 2 S. 2 AO](https://www.gesetze-im-internet.de/ao_1977/__361.html))

Die AdV **soll** auf Antrag gewährt werden, wenn

1. **ernstliche Zweifel** an der Rechtmäßigkeit bestehen — d. h. bei summarischer Prüfung neben für die Rechtmäßigkeit sprechenden Umständen gewichtige gegen sie sprechende Gründe zutage treten, die Unentschiedenheit oder Unsicherheit in der Beurteilung von Rechtsfragen oder Unklarheit in der Beurteilung von Tatfragen bewirken; Erfolgsaussichten über 50 % sind **nicht** erforderlich (st. Rspr. seit BFH, Beschl. v. 10.02.1967 – III B 9/66 `[unverifiziert – prüfen]`), **oder**
2. die Vollziehung eine **unbillige**, nicht durch überwiegende öffentliche Interessen gebotene **Härte** zur Folge hätte (wirtschaftliche Nachteile, die über die Zahlung hinausgehen und nicht oder schwer wiedergutzumachen sind, z. B. Existenzgefährdung) — bei offensichtlicher Rechtmäßigkeit scheidet auch die Härte-AdV aus.

**Typische Zweifelsgründe:**

- Rechtsfrage höchstrichterlich ungeklärt, divergierende FG-Rspr., anhängiges Revisionsverfahren beim BFH.
- Schätzung methodisch angreifbar (Schätzungsgrund zweifelhaft, Kalkulationsfehler) — siehe `/steuerrecht:aussenpruefung-betriebspruefung`.
- Verfahrensfehler mit Rechtswidrigkeitsfolge (fehlende Bekanntgabe, Festsetzungsverjährung).
- **Verfassungsrechtliche Zweifel**: Nach der BFH-Linie ist AdV hier zusätzlich von einem **besonderen berechtigten Aussetzungsinteresse** abhängig, das gegen das öffentliche Interesse am Gesetzesvollzug abzuwägen ist `[unverifiziert – prüfen]`. Hilfsweise Ruhen nach § 363 Abs. 2 S. 2 AO.

### 4. Umfang ([§ 361 Abs. 2 S. 3, 4 AO](https://www.gesetze-im-internet.de/ao_1977/__361.html))

- **Aufhebung der Vollziehung**: Ist der Bescheid schon vollzogen (gezahlt oder vollstreckt), tritt an die Stelle der Aussetzung die Aufhebung der Vollziehung — gezahlte Beträge werden erstattet (§ 361 Abs. 2 S. 3 AO).
- **Begrenzung bei Steuerbescheiden**: AdV und Aufhebung sind auf die festgesetzte Steuer, **vermindert um anzurechnende Steuerabzugsbeträge, anzurechnende Körperschaftsteuer und festgesetzte Vorauszahlungen**, beschränkt — praktisch auf die **Abschlusszahlung**. Ausnahme: wenn die Aussetzung zur Abwendung **wesentlicher Nachteile** nötig erscheint (§ 361 Abs. 2 S. 4 AO; inhaltsgleich § 69 Abs. 2 FGO). Die Ausnahme wird von der Rspr. eng ausgelegt (Existenzgefährdung) `[unverifiziert – prüfen]`.
- **Sicherheitsleistung** (§ 361 Abs. 2 S. 5 AO): Ermessen; regelmäßig nicht, wenn die Rechtswidrigkeit offensichtlich ist oder der Steuerpflichtige die Sicherheit nicht leisten kann; bei Gefährdung des Steueranspruchs (z. B. Wegzug, Vermögensverlagerung) üblich.
- **Folgebescheide** (§ 361 Abs. 3 AO): Wird ein Grundlagenbescheid (Feststellungs-, Messbescheid) ausgesetzt, ist auch der Folgebescheid **von Amts wegen** auszusetzen. Daher AdV gegen den **Grundlagenbescheid** beantragen, nicht gegen den Folgebescheid (§ 351 Abs. 2 AO).
- **Entwurf JStG 2026**: § 1 Abs. 2 Nr. 7 AO soll für die Gemeinden auch auf § 361 Abs. 2 S. 4 und Abs. 3 AO verweisen — wirkt sich bei Grund- und Gewerbesteuer aus.

### 5. Zinsen und Kosten: AdV oder zahlen?

| Variante | Kosten bei Unterliegen | Ertrag bei Obsiegen |
|---|---|---|
| AdV | **Aussetzungszinsen** [§ 237 AO](https://www.gesetze-im-internet.de/ao_1977/__237.html): 0,5 % je vollem Monat ([§ 238 Abs. 1 AO](https://www.gesetze-im-internet.de/ao_1977/__238.html)) | keine Zinsen |
| Zahlen | keine | **Prozesszinsen** [§ 236 AO](https://www.gesetze-im-internet.de/ao_1977/__236.html) (0,5 % je Monat ab Rechtshängigkeit) bzw. Erstattungszinsen § 233a AO (0,15 % je Monat, Entwurf: 0,3 % ab 2027) |
| Weder AdV noch Zahlung | **Säumniszuschläge** [§ 240 AO](https://www.gesetze-im-internet.de/ao_1977/__240.html): 1 % je angefangenem Monat — nach BFH auch für Zeiträume nach 2018 verfassungsgemäß ([BFH, Urt. v. 19.02.2025 – XI R 18/23](https://www.bundesfinanzhof.de/en/entscheidungen/entscheidungen-online/decision-detail/STRE202520150/)); Vollstreckung | — |

- **Aussetzungszinsen verfassungswidrig?** Der BFH hält den Zinssatz von 0,5 % je Monat jedenfalls für einen Teilzeitraum ab 2019 für verfassungswidrig und hat dem BVerfG vorgelegt (BFH, Beschl. v. 08.05.2024 – VIII R 9/23; BVerfG – 1 BvL 8/24) `[unverifiziert – prüfen]`. Gegen jeden Aussetzungszinsbescheid **Einspruch** einlegen und Zwangsruhe nach § 363 Abs. 2 S. 2 AO geltend machen.
- Wird AdV ab Fälligkeit gewährt, entstehen keine Säumniszuschläge. Bereits verwirkte Säumniszuschläge bleiben dagegen auch bei späterer Aufhebung oder Änderung der Steuerfestsetzung bestehen (§ 240 Abs. 1 S. 4 AO); ein Erlass ist möglich, wenn der Bescheid später aufgehoben wird und AdV hätte gewährt werden müssen, der Steuerpflichtige aber alles getan hat, sie zu erlangen (`/steuerrecht:stundung-erlass-vollstreckungsschutz`).

### 6. Antragsformulierung

- Antrag, die Vollziehung des Bescheids vom … über … EUR in Höhe von … EUR **ohne Sicherheitsleistung** bis einen Monat nach Bekanntgabe der Einspruchsentscheidung auszusetzen (bzw. bereits geleistete Beträge aufzuheben).
- Begründung: Darstellung der ernstlichen Zweifel, mit Belegen; Berechnung des aussetzbaren Betrags nach § 361 Abs. 2 S. 4 AO; ggf. Darlegung wesentlicher Nachteile.
- Beim FG: Darlegung der Zugangsvoraussetzung (Ablehnung vom … / Nichtentscheidung seit … / drohende Vollstreckung durch Ankündigung vom …).

## Ausgabeformat

```
AUSSETZUNG DER VOLLZIEHUNG — <Mandant> — <Datum> — Rechtsstand Oktober 2026

I.    Verwaltungsakt
      Bescheid / Datum / Betrag:      <…>
      Rechtsbehelf eingelegt:         [Einspruch vom … / Klage vom …]
      Vollziehbar / aussetzbar:       [✓ / ✗ → einstweilige Anordnung § 114 FGO]

II.   Zuständigkeit
      Finanzamt (§ 361 AO):           [Antrag vom … / zu stellen]
      Finanzgericht (§ 69 Abs. 3 FGO): [Zugangsvoraussetzung § 69 Abs. 4: Ablehnung / Untätigkeit / Vollstreckung droht]

III.  Begründetheit
      Ernstliche Zweifel:             <Gründe>
      Unbillige Härte:                <Gründe / —>

IV.   Umfang
      Festgesetzte Steuer:            <EUR>
      ./. Abzugsbeträge, Vorauszahlungen: <EUR>
      Aussetzbarer Betrag (§ 361 Abs. 2 S. 4): <EUR>
      Aufhebung der Vollziehung:      <EUR bereits gezahlt / —>
      Sicherheitsleistung:            [nicht erforderlich / … EUR]
      Folgebescheide (§ 361 Abs. 3):  <…>

V.    Zinsen / Kosten
      Aussetzungszinsen-Risiko (§ 237): <EUR je Monat>
      Alternative Zahlung + § 236:    <…>
      Säumniszuschläge bisher:        <EUR — Erlass prüfen>

VI.   Anträge
      <AdV-Antrag / Antrag beim FG / Einspruch gegen Zinsbescheid>
```

## Beispiel (Urteilsstil, Kurzvermerk)

Nach einer Betriebsprüfung setzte das Finanzamt die ESt 2023 auf 84.000 EUR fest; Vorauszahlungen von 30.000 EUR und Kapitalertragsteuer von 4.000 EUR sind anzurechnen. Die Hinzuschätzung beruht auf einer Zeitreihe ohne Berücksichtigung einer Betriebsumstellung. Ernstliche Zweifel bestehen, weil der Schätzungsgrund fraglich und die Methode für den Betrieb ungeeignet ist (§ 361 Abs. 2 S. 2 AO). Auszusetzen ist nach § 361 Abs. 2 S. 4 AO höchstens die Abschlusszahlung von 50.000 EUR (84.000 EUR ./. 30.000 EUR ./. 4.000 EUR); wesentliche Nachteile, die eine darüber hinausgehende Aussetzung rechtfertigen, sind nicht dargelegt. Lehnt das Finanzamt ab, ist der Antrag beim Finanzgericht nach § 69 Abs. 3, 4 FGO zulässig.

## Risiken / typische Fehler

- **Kein Vorantrag beim Finanzamt** — gerichtlicher Antrag unzulässig (§ 69 Abs. 4 FGO), sofern nicht Untätigkeit oder drohende Vollstreckung dargelegt wird.
- **Falscher Rechtsbehelf** — Ablehnung von Stundung/Erlass ist nicht aussetzbar; einstweilige Anordnung nach § 114 FGO.
- **AdV gegen den Folgebescheid statt gegen den Grundlagenbescheid** — Einwendungen ausgeschlossen (§ 351 Abs. 2 AO); AdV des Grundlagenbescheids wirkt nach § 361 Abs. 3 AO auf den Folgebescheid.
- **Begrenzung auf die Abschlusszahlung übersehen** — Vorauszahlungen und Abzugsbeträge sind nicht aussetzbar, außer bei wesentlichen Nachteilen.
- **Aussetzungszinsen nicht einkalkuliert** — 0,5 % je Monat bei Unterliegen; Einspruch gegen Zinsbescheide wegen der anhängigen Vorlage (1 BvL 8/24 `[unverifiziert – prüfen]`) nicht vergessen.
- **Säumniszuschläge** — wird AdV **ab Fälligkeit** gewährt, entstehen keine; deshalb AdV ausdrücklich ab Fälligkeit beantragen. Wird der Antrag abgelehnt oder AdV erst ab einem späteren Zeitpunkt gewährt, sind die bis dahin verwirkten Zuschläge geschuldet — bis zur Entscheidung Vollstreckungsaufschub erbitten.
- **Beschwerde nicht zugelassen** — gegen FG-Beschlüsse keine Beschwerde ohne Zulassung; stattdessen Änderungsantrag bei neuen Umständen.

## Quellen

### Statute

- [§ 361 AO](https://www.gesetze-im-internet.de/ao_1977/__361.html) (Aussetzung der Vollziehung), [§ 351 AO](https://www.gesetze-im-internet.de/ao_1977/__351.html), [§ 363 AO](https://www.gesetze-im-internet.de/ao_1977/__363.html)
- [§ 69 FGO](https://www.gesetze-im-internet.de/fgo/__69.html), [§ 114 FGO](https://www.gesetze-im-internet.de/fgo/__114.html), [§ 128 FGO](https://www.gesetze-im-internet.de/fgo/__128.html)
- [§ 236 AO](https://www.gesetze-im-internet.de/ao_1977/__236.html), [§ 237 AO](https://www.gesetze-im-internet.de/ao_1977/__237.html), [§ 238 AO](https://www.gesetze-im-internet.de/ao_1977/__238.html), [§ 240 AO](https://www.gesetze-im-internet.de/ao_1977/__240.html)
- [§ 1 AO](https://www.gesetze-im-internet.de/ao_1977/__1.html) (Anwendung auf Realsteuern)

### Gesetzgebung (nicht in Kraft)

- Regierungsentwurf JStG 2026, BT-Drs. 21/8283, Art. 18 Nr. 2 (§ 1 Abs. 2 Nr. 7 AO)

### Verwaltungsanweisungen

- AEAO zu § 361 AO (insb. Begrenzung nach § 361 Abs. 2 S. 4 AO, Sicherheitsleistung)

### Rechtsprechung

- [BFH, Urt. v. 19.02.2025 – XI R 18/23](https://www.bundesfinanzhof.de/en/entscheidungen/entscheidungen-online/decision-detail/STRE202520150/) (Säumniszuschläge verfassungsgemäß)
- BFH, Beschl. v. 08.05.2024 – VIII R 9/23 (Vorlage Aussetzungszinsen); BVerfG – 1 BvL 8/24 (anhängig) `[unverifiziert – prüfen]`
- BFH, Beschl. v. 10.02.1967 – III B 9/66 (Begriff der ernstlichen Zweifel) `[unverifiziert – prüfen]`

### Literatur

- Seer, in: Tipke/Kruse, AO/FGO, § 69 FGO, § 361 AO — Lieferungsstand prüfen `[unverifiziert – prüfen]`
- Gosch, in: Gosch, AO/FGO, § 69 FGO `[unverifiziert – prüfen]`
- Suchstring juris: „§ 69 Abs. 4 FGO Zugangsvoraussetzung Vollstreckung droht"
