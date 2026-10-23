---
name: wettbewerbsverbot-nachvertraglich
description: "Nachvertragliches Wettbewerbsverbot für Arbeitnehmer – Verweisung § 110 GewO auf §§ 74–75f HGB, Form § 74 Abs. 1 HGB (Schriftform und Aushändigung der Urkunde), Karenzentschädigung mindestens 50 % § 74 Abs. 2 HGB, Nichtigkeit bei fehlender Entschädigungszusage gegenüber Unverbindlichkeit mit Wahlrecht bei zu niedriger Entschädigung, berechtigtes geschäftliches Interesse und Höchstdauer zwei Jahre § 74a HGB, Anrechnung anderweitigen Erwerbs § 74c HGB, Lossagung § 75 HGB, Verzicht des Arbeitgebers § 75a HGB, Vertragsstrafe § 75c HGB, Kundenschutzklauseln, bedingte Wettbewerbsverbote, Abgrenzung zum Organmitglied. Use when ein nachvertragliches Wettbewerbsverbot gestaltet, auf Wirksamkeit geprüft, durch Verzicht beseitigt oder Karenzentschädigung geltend gemacht wird."
language: de
agents:
  researcher: ../../agents/researcher.md
  drafter: ../../agents/drafter.md
  reviewer: ../../agents/reviewer.md
provider_variants: [claude, gemini, openai]
test: ./test.md
---

# /arbeitsrecht:wettbewerbsverbot-nachvertraglich

## Zweck

Das nachvertragliche Wettbewerbsverbot ist eine der teuersten Klauseln im Arbeitsvertrag — für den Arbeitgeber, der für bis zu zwei Jahre die Hälfte der letzten Bezüge zahlen muss, und für den Arbeitnehmer, der eine neue Stelle nicht antreten darf. Die Weichen stellen wenige formale Punkte: Entschädigungszusage ja oder nein, Höhe, Form, rechtzeitiger Verzicht. Dieser Skill prüft eine bestehende Klausel, gestaltet eine neue und berechnet die Karenzentschädigung einschließlich Anrechnung.

> **Rechtsstand: Oktober 2026.** §§ 74 ff. HGB sind seit Jahren unverändert; die Klärung der Rechtsfolgen beruht auf der Rspr. des BAG.

## Eingaben

- Wortlaut der Klausel, Vertragsdatum, Unterschriften, Aushändigung der Urkunde
- Räumlicher, sachlicher und zeitlicher Umfang; Kundenschutz- oder Abwerbeverbote
- Zusage der Karenzentschädigung: vorhanden, Höhe, Bemessungsgrundlage (fix, variabel, Sachbezüge, Dienstwagen)
- Beendigung: Datum, Art (ordentliche / außerordentliche Kündigung, Aufhebungsvertrag), Kündigender
- Neue Tätigkeit: Arbeitgeber, Branche, Funktion, Vergütung, Wohnsitzwechsel?
- Vertragsstrafe vereinbart?

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert HGB-Normen mit URL und die BAG-Linien zu Nichtigkeit, Unverbindlichkeit und Anrechnung.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) erstellt Klausel, Verzichtserklärung, Lossagungserklärung oder Zahlungsklage.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Form, Höhe, Fristen des Verzichts und die Berechnung.

## Ablauf

### 1. Anwendbarkeit ([§ 110 GewO](https://www.gesetze-im-internet.de/gewo/__110.html))

Für alle Arbeitnehmer gelten die §§ 74–75f HGB entsprechend. **Nicht** erfasst sind Organmitglieder (GmbH-Geschäftsführer, Vorstände); für sie gelten § 138 BGB und Art. 12 GG, eine Karenzentschädigung ist nicht zwingend `[unverifiziert – prüfen]`. Auszubildende: Wettbewerbsverbote sind weitgehend nichtig ([§ 12 BBiG](https://www.gesetze-im-internet.de/bbig_2005/__12.html)).

### 2. Form ([§ 74 Abs. 1 HGB](https://www.gesetze-im-internet.de/hgb/__74.html))

- **Schriftform** (§ 126 BGB) — Textform genügt nicht; die BEG-IV-Erleichterungen für den Nachweis der Arbeitsbedingungen ändern daran nichts.
- **Aushändigung** einer vom Arbeitgeber unterzeichneten Urkunde mit den vereinbarten Bestimmungen. Fehlt sie, kann der Arbeitnehmer sich auf das Verbot berufen, der Arbeitgeber nicht `[unverifiziert – prüfen]`.

### 3. Karenzentschädigung ([§ 74 Abs. 2 HGB](https://www.gesetze-im-internet.de/hgb/__74.html)) — die zentrale Weiche

| Konstellation | Rechtsfolge |
|---|---|
| **Keine** Zusage einer Karenzentschädigung | Verbot **nichtig**; keine Partei kann Rechte daraus herleiten; eine salvatorische Klausel rettet es nicht (BAG, Urt. v. 22.03.2017 – 10 AZR 448/15 `[unverifiziert – prüfen]`) |
| Zusage, aber **unter 50 %** der zuletzt bezogenen vertragsmäßigen Leistungen | Verbot **unverbindlich**: **Wahlrecht** des Arbeitnehmers — Wettbewerb oder Einhaltung gegen die zugesagte Entschädigung; Ausübung zu Beginn der Karenzzeit |
| Zusage von mindestens 50 % | wirksam, soweit § 74a HGB nicht entgegensteht |
| **Bedingtes** Verbot („Arbeitgeber kann bei Beendigung entscheiden, ob…") | unverbindlich, Wahlrecht des Arbeitnehmers `[unverifiziert – prüfen]` |

**Bemessung:** alle vertragsmäßigen Leistungen der letzten Zeit — Fixum, variable Vergütung (Durchschnitt der letzten drei Jahre, [§ 74b Abs. 2 HGB](https://www.gesetze-im-internet.de/hgb/__74b.html)), Sachbezüge wie die Privatnutzung des Dienstwagens. Zahlung **am Schluss jedes Monats** (§ 74b Abs. 1 HGB).

### 4. Inhaltliche Grenzen ([§ 74a HGB](https://www.gesetze-im-internet.de/hgb/__74a.html))

- **Berechtigtes geschäftliches Interesse** des Arbeitgebers (Schutz von Kundenbeziehungen oder Know-how), keine reine Konkurrenzabwehr. Soweit es fehlt oder das Fortkommen unbillig erschwert wird, ist das Verbot **insoweit unverbindlich** (geltungserhaltende Reduktion im Rahmen von § 74a HGB).
- **Höchstdauer zwei Jahre** ab Beendigung.
- Nichtig gegenüber Minderjährigen und bei Ehrenwort-Versprechen (§ 74a Abs. 2 HGB).
- **Kundenschutzklauseln** und Abwerbeverbote sind Wettbewerbsverbote im Sinne der §§ 74 ff. HGB und brauchen ebenfalls eine Karenzentschädigung.

### 5. Anrechnung ([§ 74c HGB](https://www.gesetze-im-internet.de/hgb/__74c.html))

Anderweitiger Erwerb (oder böswillig unterlassener Erwerb) wird angerechnet, soweit Entschädigung und neuer Verdienst zusammen **110 %** der letzten Bezüge übersteigen — **125 %**, wenn der Arbeitnehmer wegen des Verbots den **Wohnsitz verlegen** musste. Auskunftspflicht des Arbeitnehmers (§ 74c Abs. 2 HGB). Ob Arbeitslosengeld anzurechnen ist, verneint das BAG `[unverifiziert – prüfen]`.

```
Letzte Bezüge (12 Mon.):        120.000 EUR → 10.000 EUR/Monat
Karenzentschädigung 50 %:         5.000 EUR/Monat
Neuer Verdienst:                  7.000 EUR/Monat
Summe:                           12.000 EUR → Grenze 110 % = 11.000 EUR
Anrechnung:                       1.000 EUR → Zahlung 4.000 EUR/Monat
```

### 6. Beseitigung des Verbots

- **Verzicht des Arbeitgebers** ([§ 75a HGB](https://www.gesetze-im-internet.de/hgb/__75a.html)): nur **vor** Beendigung des Arbeitsverhältnisses, **schriftlich**; der Arbeitnehmer ist sofort frei, die Entschädigungspflicht endet aber erst **ein Jahr** nach der Erklärung. Ein Verzicht nach Beendigung oder im Aufhebungsvertrag ohne Einigung über die Entschädigung entlastet nicht.
- **Lossagung** ([§ 75 HGB](https://www.gesetze-im-internet.de/hgb/__75.html)): bei außerordentlicher Kündigung wegen vertragswidrigen Verhaltens der anderen Seite durch schriftliche Erklärung **binnen eines Monats**; bei ordentlicher Arbeitgeberkündigung ohne erheblichen Anlass in der Person des Arbeitnehmers kann dieser sich lossagen, es sei denn, der Arbeitgeber zahlt die vollen Bezüge (§ 75 Abs. 2 HGB).
- **Aufhebungsvertrag:** ausdrücklich regeln, ob das Verbot fortbesteht; allgemeine Erledigungsklauseln erfassen es nur bei klarer Formulierung.
- **Rücktritt** bei Nichtzahlung der Entschädigung nach § 323 BGB (BAG, Urt. v. 31.01.2018 – 10 AZR 392/17 `[unverifiziert – prüfen]`).

### 7. Sanktionen

Unterlassungsanspruch (einstweilige Verfügung), Wegfall der Entschädigung für die Dauer des Verstoßes, Schadensersatz; **Vertragsstrafe** ([§ 75c HGB](https://www.gesetze-im-internet.de/hgb/__75c.html)) mit AGB-Kontrolle der Höhe (§ 307 BGB). Steuerlich ist die Karenzentschädigung Arbeitslohn bzw. Entschädigung (§ 24 Nr. 1 EStG), sozialversicherungsrechtlich regelmäßig beitragsfrei `[unverifiziert – prüfen]`.

## Quellen

### Statute

- [§ 110 GewO](https://www.gesetze-im-internet.de/gewo/__110.html)
- [§ 74 HGB](https://www.gesetze-im-internet.de/hgb/__74.html), [§ 74a HGB](https://www.gesetze-im-internet.de/hgb/__74a.html), [§ 74b HGB](https://www.gesetze-im-internet.de/hgb/__74b.html), [§ 74c HGB](https://www.gesetze-im-internet.de/hgb/__74c.html), [§ 75 HGB](https://www.gesetze-im-internet.de/hgb/__75.html), [§ 75a HGB](https://www.gesetze-im-internet.de/hgb/__75a.html), [§ 75c HGB](https://www.gesetze-im-internet.de/hgb/__75c.html), [§ 75d HGB](https://www.gesetze-im-internet.de/hgb/__75d.html)
- [§ 126 BGB](https://www.gesetze-im-internet.de/bgb/__126.html), [§ 307 BGB](https://www.gesetze-im-internet.de/bgb/__307.html), [§ 323 BGB](https://www.gesetze-im-internet.de/bgb/__323.html), [§ 12 BBiG](https://www.gesetze-im-internet.de/bbig_2005/__12.html)

### Kommentare

- Oetker, in: ErfK, 26. Aufl. 2026, § 74 HGB Rn. 1 ff. `[unverifiziert – prüfen]` (Auflage prüfen)
- Bauer / Diller, Wettbewerbsverbote, 9. Aufl., Rn. 1 ff. `[unverifiziert – prüfen]`

### Rechtsprechung

- BAG, Urt. v. 22.03.2017 – 10 AZR 448/15 (fehlende Entschädigungszusage → Nichtigkeit; salvatorische Klausel unbeachtlich) `[unverifiziert – prüfen]`
- BAG, Urt. v. 31.01.2018 – 10 AZR 392/17 (Rücktritt vom Wettbewerbsverbot) `[unverifiziert – prüfen]`

## Ausgabeformat

```
WETTBEWERBSVERBOT — <Mandat-ID> — <Datum>
Rechtsstand: Oktober 2026

Gesamtbefund: [🟢 wirksam / 🟡 unverbindlich — Wahlrecht / 🔴 nichtig]

I.    Klausel                         <Umfang räumlich/sachlich/zeitlich>
II.   Form § 74 Abs. 1 HGB            Schriftform [✓/✗]; Aushändigung [✓/✗]
III.  Karenzentschädigung § 74 Abs. 2 HGB
      Zusage:                         [fehlt → nichtig / < 50 % / ≥ 50 %]
      Bemessungsgrundlage:            <Fixum + Ø variabel + Sachbezüge>
IV.   § 74a HGB                       Interesse <…>; Dauer <≤ 2 Jahre>
V.    Wahlrecht des AN                [besteht — ausüben bis <Datum> / entfällt]
VI.   Anrechnung § 74c HGB            110 % / 125 %: <Berechnung>
VII.  Verzicht § 75a / Lossagung § 75 [möglich bis <Datum> / Entschädigung bis <Datum>]
VIII. Vertragsstrafe § 75c HGB        <Höhe, AGB-Kontrolle>
IX.   Empfehlung
```

## Beispiel (Gutachtenstil, verkürzt)

**Sachverhalt.** Vertriebsleiter mit Fixum 96.000 EUR, Bonus durchschnittlich 24.000 EUR und Dienstwagen kündigt zum 31.12.2026. Vereinbart ist ein zweijähriges Wettbewerbsverbot gegen „50 % des zuletzt bezogenen Fixgehalts".

**Frage 1: Ist das Verbot verbindlich?** Nach § 74 Abs. 2 HGB muss die Entschädigung mindestens die Hälfte der zuletzt bezogenen **vertragsmäßigen Leistungen** erreichen. Dazu gehören neben dem Fixum der Durchschnitt der variablen Vergütung (§ 74b Abs. 2 HGB) und der Sachbezug des Dienstwagens. 50 % des Fixums allein (48.000 EUR) bleiben unter der Hälfte der Gesamtbezüge (mindestens 60.000 EUR zuzüglich Sachbezug). Eine Entschädigung ist also zugesagt, aber zu niedrig. Das Verbot ist deshalb nicht nichtig, sondern **unverbindlich**. Der Arbeitnehmer hat ein Wahlrecht: Er kann den Wettbewerb aufnehmen oder sich an das Verbot halten und die zugesagte Entschädigung verlangen.

**Frage 2: Verzicht im Januar 2027?** Ein Verzicht nach § 75a HGB ist nur **vor** Beendigung des Arbeitsverhältnisses möglich. Ein Verzicht im Januar 2027 geht ins Leere. Ein Verzicht noch im Dezember 2026 hätte die Entschädigungspflicht erst ein Jahr nach der Erklärung enden lassen.

**Ergebnis.** Der Arbeitnehmer kann zum Wettbewerber wechseln; die Vertragsstrafe greift mangels verbindlichen Verbots nicht.

## Risiken / typische Fehler

- **Fehlende Entschädigungszusage mit Unverbindlichkeit verwechselt** — ohne Zusage ist das Verbot nichtig, kein Wahlrecht, keine Entschädigung.
- **Verzicht nach Beendigung erklärt** — § 75a HGB verlangt den Verzicht vor dem Ende des Arbeitsverhältnisses; danach bleibt die Entschädigungspflicht.
- **Ein-Jahres-Nachwirkung des Verzichts übersehen** — der Arbeitgeber zahlt noch zwölf Monate ab Erklärung.
- **Variable Vergütung und Dienstwagen nicht eingerechnet** — die 50 %-Grenze bezieht sich auf alle vertragsmäßigen Leistungen.
- **Wahlrecht nicht rechtzeitig ausgeübt** — der Arbeitnehmer muss sich zu Beginn der Karenzzeit entscheiden.
- **Kundenschutzklausel ohne Entschädigung** — sie ist ein Wettbewerbsverbot und teilt dessen Schicksal.
- **Textform statt Schriftform** — § 74 Abs. 1 HGB verlangt Schriftform und Aushändigung.
- **Aufhebungsvertrag ohne Regelung zum Verbot** — das Verbot gilt fort, mit Entschädigungspflicht.
- **Geschäftsführer nach §§ 74 ff. HGB beurteilt** — für Organmitglieder gelten andere Maßstäbe.
