---
name: mindestlohn-minijob-aktivrente
description: "Mindestlohn, Minijob/Midijob und Beschäftigung nach Erreichen der Regelaltersgrenze – Mindestlohn 13,90 EUR ab 01.01.2026 und 14,60 EUR ab 01.01.2027 (Fünfte Mindestlohnanpassungsverordnung), Unabdingbarkeit und Fälligkeit §§ 2, 3 MiLoG, Arbeitszeitkonto § 2 Abs. 2 MiLoG, Aufzeichnungspflicht § 17 MiLoG, Ausnahmen § 22 MiLoG, dynamische Geringfügigkeitsgrenze § 8 Abs. 1a SGB IV (603 EUR 2026 / 633 EUR 2027), Übergangsbereich § 20 Abs. 2 SGB IV, Arbeit auf Abruf § 12 TzBfG, Aktivrente § 3 Nr. 21 EStG und erleichterte Befristung nach der Regelaltersgrenze § 41 Abs. 2 SGB VI (seit 01.01.2026). Use when Vergütungsmodelle, Minijobs oder Weiterbeschäftigung von Rentnern auf die Werte 2026/2027 geprüft werden."
language: de
agents:
  researcher: ../../agents/researcher.md
  drafter: ../../agents/drafter.md
  reviewer: ../../agents/reviewer.md
provider_variants: [claude, gemini, openai]
test: ./test.md
---

# /arbeitsrecht:mindestlohn-minijob-aktivrente

## Zweck

Zum 01.01.2026 und zum 01.01.2027 steigen der Mindestlohn und mit ihm automatisch die Minijob-Grenze. Verträge mit festen Monatsbeträgen oder Stundenkontingenten „rutschen" dadurch aus der Geringfügigkeit oder unter den Mindestlohn, ohne dass jemand den Vertrag ändert. Gleichzeitig hat der Gesetzgeber zum 01.01.2026 die Weiterbeschäftigung nach der Regelaltersgrenze steuerlich (Aktivrente) und befristungsrechtlich (§ 41 Abs. 2 SGB VI) erleichtert. Dieser Skill prüft Vergütungsmodelle gegen die aktuellen Werte und gestaltet die Beschäftigung von Rentnern.

> **Rechtsstand: Oktober 2026.** Werte für 2027 sind bereits verordnet. Die Mindestlohnkommission entscheidet über die Folgejahre erst wieder 2027.

## Eingaben

- Stundenlohn bzw. Monatsentgelt, vereinbarte Wochen-/Monatsstunden, Arbeit auf Abruf?
- Zulagen, Einmalzahlungen, Sachbezüge, Arbeitszeitkonto
- Art der Beschäftigung: Minijob, Midijob, Werkstudent, Praktikum, Auszubildende(r), Saison
- Mehrfachbeschäftigung?
- Bei Rentnern: Geburtsdatum, Regelaltersgrenze, Bezug einer Vollrente, bisherige Beschäftigung beim selben Arbeitgeber, Vertragskette nach Erreichen der Regelaltersgrenze

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert MiLoG, MiLoV5, SGB IV, SGB VI, § 3 Nr. 21 EStG und die aktuellen Rechengrößen.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) erstellt Vertragsanpassung, Minijob-Vertrag, Befristungsvereinbarung nach § 41 SGB VI oder Mandanteninformation.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) rechnet nach, prüft Grenzwerte, Befristungsform und Dokumentationspflichten.

## Ablauf

### 1. Mindestlohn ([§ 1 MiLoG](https://www.gesetze-im-internet.de/milog/__1.html))

| Zeitraum | Mindestlohn brutto je Zeitstunde |
|---|---|
| ab 01.01.2025 | 12,82 EUR |
| **ab 01.01.2026** | **13,90 EUR** |
| **ab 01.01.2027** | **14,60 EUR** |

Rechtsgrundlage: [Fünfte Mindestlohnanpassungsverordnung (MiLoV5) v. 05.11.2025, BGBl. 2025 I Nr. 268, ber. Nr. 312](https://www.gesetze-im-internet.de/milov5/BJNR10C0A0025.html).

- **Unabdingbarkeit** ([§ 3 MiLoG](https://www.gesetze-im-internet.de/milog/__3.html)): Vereinbarungen, die den Anspruch unterschreiten oder ausschließen, sind insoweit unwirksam; Verzicht nur durch **gerichtlichen Vergleich**. Ausschlussfristen müssen den Mindestlohn ausnehmen.
- **Fälligkeit** ([§ 2 MiLoG](https://www.gesetze-im-internet.de/milog/__2.html)): spätestens am letzten Bankarbeitstag des Folgemonats.
- **Arbeitszeitkonto** (§ 2 Abs. 2 MiLoG): monatlich höchstens 50 % der vereinbarten Arbeitszeit, Ausgleich binnen zwölf Monaten.
- **Anrechenbarkeit:** Zahlungen mit Entgeltcharakter für die Normalleistung zählen; Aufwendungsersatz und Zahlungen für besondere Leistungen nur nach der Rspr. des BAG `[unverifiziert – prüfen]`.
- **Ausnahmen** ([§ 22 MiLoG](https://www.gesetze-im-internet.de/milog/__22.html)): Pflichtpraktika, Orientierungspraktika bis drei Monate, Minderjährige ohne Berufsabschluss, Langzeitarbeitslose in den ersten sechs Monaten, Auszubildende (für sie gilt die Mindestausbildungsvergütung nach [§ 17 BBiG](https://www.gesetze-im-internet.de/bbig_2005/__17.html)).
- **Aufzeichnung** ([§ 17 MiLoG](https://www.gesetze-im-internet.de/milog/__17.html)): Beginn, Ende und Dauer für Minijobber und in den Branchen des § 2a SchwarzArbG, spätestens bis zum siebten Tag nach der Arbeitsleistung, zwei Jahre aufbewahren.
- **Sanktionen** ([§ 21 MiLoG](https://www.gesetze-im-internet.de/milog/__21.html)): Bußgeld bis 500.000 EUR; Ausschluss von öffentlichen Aufträgen ([§ 19 MiLoG](https://www.gesetze-im-internet.de/milog/__19.html)); Auftraggeberhaftung ([§ 13 MiLoG](https://www.gesetze-im-internet.de/milog/__13.html)).

### 2. Minijob ([§ 8 SGB IV](https://www.gesetze-im-internet.de/sgb_4/__8.html))

Die **Geringfügigkeitsgrenze** ist dynamisch (§ 8 Abs. 1a SGB IV): Mindestlohn × 130 ÷ 3, aufgerundet auf volle Euro.

```
2026: 13,90 × 130 ÷ 3 = 602,33 → 603 EUR monatlich
2027: 14,60 × 130 ÷ 3 = 632,67 → 633 EUR monatlich
```

- **Gelegentliches unvorhersehbares Überschreiten** (§ 8 Abs. 1b SGB IV): unschädlich in bis zu zwei Kalendermonaten innerhalb eines Zeitjahres, höchstens bis zum Doppelten der Grenze.
- **Abgaben:** Pauschalbeiträge zur KV (13 %) und RV (15 %), pauschale Lohnsteuer 2 % ([§ 40a Abs. 2 EStG](https://www.gesetze-im-internet.de/estg/__40a.html)); RV-Pflicht mit Befreiungsmöglichkeit ([§ 6 Abs. 1b SGB VI](https://www.gesetze-im-internet.de/sgb_6/__6.html)).
- **Gleichbehandlung:** Minijobber sind Teilzeitbeschäftigte ([§ 4 TzBfG](https://www.gesetze-im-internet.de/tzbfg/__4.html)) mit Anspruch auf Urlaub, Entgeltfortzahlung und Feiertagsvergütung.

**Übergangsbereich (Midijob)** ([§ 20 Abs. 2 SGB IV](https://www.gesetze-im-internet.de/sgb_4/__20.html)): von 603,01 EUR (2026) bis 2.000 EUR; reduzierte Arbeitnehmerbeiträge.

### 3. Die Drift-Falle: feste Beträge, steigender Mindestlohn

| Vertragsmodell | Folge der Erhöhung |
|---|---|
| fester Monatsbetrag 603 EUR, „ca. 45 Std./Monat" | 45 × 13,90 = 625,50 EUR → Mindestlohn unterschritten **oder** Grenze überschritten |
| feste Stunden, Lohn an Mindestlohn gekoppelt | 2027: Stunden prüfen, damit 633 EUR nicht überschritten werden |
| **Arbeit auf Abruf ohne Stundenzahl** ([§ 12 TzBfG](https://www.gesetze-im-internet.de/tzbfg/__12.html)) | gesetzliche Fiktion von **20 Wochenstunden** → ca. 1.204 EUR monatlich (2026) → kein Minijob mehr, Beitragsnachforderung |

Folge eines unerkannten Überschreitens: Versicherungspflicht in allen Zweigen ab dem Monat des Überschreitens; Nachforderung durch die Prüfung der DRV ([§ 28p SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28p.html)), Säumniszuschläge.

### 4. Aktivrente ([§ 3 Nr. 21 EStG](https://www.gesetze-im-internet.de/estg/__3.html))

- Seit **01.01.2026** steuerfrei: Arbeitslohn aus einem **Beschäftigungsverhältnis** bis **2.000 EUR monatlich** (24.000 EUR jährlich), ab dem Monat nach Erreichen der **Regelaltersgrenze**.
- Nicht erfasst nach berichteter Gesetzeslage: Selbständige, pauschal besteuerte Minijobs `[unverifiziert – prüfen]`; Wirkung auf Progressionsvorbehalt und Sozialversicherung vor Beratung am Gesetzestext prüfen.
- **Sozialversicherung:** Beschäftigte mit Vollrente nach Erreichen der Regelaltersgrenze sind in der RV versicherungsfrei ([§ 5 Abs. 4 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__5.html)), können aber verzichten; der Arbeitgeberanteil bleibt zu zahlen ([§ 172 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__172.html)). In der Arbeitslosenversicherung ist der Arbeitnehmer ab dem Folgemonat des Erreichens der Regelaltersgrenze versicherungsfrei; der **Arbeitgeberanteil bleibt** ([§ 346 Abs. 3 SGB III](https://www.gesetze-im-internet.de/sgb_3/__346.html)). KV und PV bleiben.

### 5. Befristung nach Erreichen der Regelaltersgrenze ([§ 41 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__41.html))

- **Seit 01.01.2026 (§ 41 Abs. 2 SGB VI):** Für Arbeitnehmer, die die Regelaltersgrenze erreicht haben, gilt das **Vorbeschäftigungsverbot** des § 14 Abs. 2 S. 2 TzBfG **nicht**. Sachgrundlose Befristung also auch beim bisherigen Arbeitgeber — mit Obergrenzen von insgesamt **acht Jahren** und **zwölf Verträgen**. Ob die Regel gerade den Wiedereinstieg beim früheren Arbeitgeber erfassen soll, ist umstritten `[unverifiziert – prüfen]`.
- Die übrigen Grenzen des § 14 Abs. 2 S. 1 TzBfG und die **Schriftform** des § 14 Abs. 4 TzBfG für die neue Befristung bleiben zu beachten — siehe `/arbeitsrecht:befristungskontrolle`.
- **Beendigung zur Regelaltersgrenze** (§ 41 Abs. 3 SGB VI, seit 01.01.2025): Die Vereinbarung, dass das Arbeitsverhältnis mit Erreichen der Regelaltersgrenze endet, bedarf nur der **Textform**; § 14 Abs. 4 TzBfG gilt insoweit nicht.
- **Hinausschieben** des Beendigungszeitpunkts während des Arbeitsverhältnisses bleibt möglich (§ 41 SGB VI) — vor Erreichen der Grenze vereinbaren.

## Quellen

### Statute

- [§ 1 MiLoG](https://www.gesetze-im-internet.de/milog/__1.html), [§ 2 MiLoG](https://www.gesetze-im-internet.de/milog/__2.html), [§ 3 MiLoG](https://www.gesetze-im-internet.de/milog/__3.html), [§ 13 MiLoG](https://www.gesetze-im-internet.de/milog/__13.html), [§ 17 MiLoG](https://www.gesetze-im-internet.de/milog/__17.html), [§ 21 MiLoG](https://www.gesetze-im-internet.de/milog/__21.html), [§ 22 MiLoG](https://www.gesetze-im-internet.de/milog/__22.html)
- [Fünfte Mindestlohnanpassungsverordnung (MiLoV5)](https://www.gesetze-im-internet.de/milov5/BJNR10C0A0025.html)
- [§ 8 SGB IV](https://www.gesetze-im-internet.de/sgb_4/__8.html), [§ 20 SGB IV](https://www.gesetze-im-internet.de/sgb_4/__20.html), [§ 28p SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28p.html)
- [§ 5 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__5.html), [§ 6 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__6.html), [§ 41 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__41.html), [§ 172 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__172.html)
- [§ 3 Nr. 21 EStG](https://www.gesetze-im-internet.de/estg/__3.html) (Aktivrentengesetz v. 22.12.2025, BGBl. 2025 I Nr. 361), [§ 40a EStG](https://www.gesetze-im-internet.de/estg/__40a.html)
- [§ 4 TzBfG](https://www.gesetze-im-internet.de/tzbfg/__4.html), [§ 12 TzBfG](https://www.gesetze-im-internet.de/tzbfg/__12.html), [§ 14 TzBfG](https://www.gesetze-im-internet.de/tzbfg/__14.html), [§ 17 BBiG](https://www.gesetze-im-internet.de/bbig_2005/__17.html)

### Rechengrößen 2026

- Beitragsbemessungsgrenze RV/ALV 8.450 EUR monatlich; KV/PV 69.750 EUR jährlich; Versicherungspflichtgrenze 77.400 EUR jährlich (SV-Rechengrößenverordnung 2026)

### Kommentare

- Franzen, in: ErfK, 26. Aufl. 2026, § 1 MiLoG Rn. 1 ff. `[unverifiziert – prüfen]` (Auflage prüfen)
- Rolfs, in: ErfK, 26. Aufl. 2026, § 41 SGB VI Rn. 1 ff. `[unverifiziert – prüfen]`

## Ausgabeformat

```
MINDESTLOHN / MINIJOB / AKTIVRENTE — <Mandat-ID> — <Datum>
Rechtsstand: Oktober 2026

I.    Mindestlohnprüfung
      Stundenlohn effektiv:           <EUR> vs. 13,90 (2026) / 14,60 (2027)
      Anrechenbare Bestandteile:      <…>
      Ausschlussfrist mit Mindestlohn-Ausnahme: [ja / nein]
II.   Geringfügigkeitsgrenze
      Monatsentgelt 2026 / 2027:      <EUR> vs. 603 / 633 EUR
      Abrufarbeit § 12 TzBfG:         [Stunden vereinbart / Fiktion 20 Std.]
      Status:                         [Minijob / Midijob / voll versicherungspflichtig]
III.  Aufzeichnung § 17 MiLoG         [erfüllt / Lücken]
IV.   Rentnerbeschäftigung
      Regelaltersgrenze erreicht am:  <Datum>
      Aktivrente § 3 Nr. 21 EStG:     [anwendbar ab <Monat> / nicht anwendbar]
      Befristung § 41 Abs. 2 SGB VI:  Verträge <N>/12, Dauer <J>/8 Jahre
      Schriftform § 14 Abs. 4 TzBfG:  [✓ / ✗]
V.    Handlungsbedarf zum 01.01.2027  <Vertragsanpassungen>
```

## Beispiel (Urteilsstil, verkürzt)

**Sachverhalt.** Minijobber mit 603 EUR monatlich bei „ca. 45 Stunden"; zwei Aushilfen auf Abruf ohne Stundenzahl; ein Verkäufer erreicht im Dezember 2026 die Regelaltersgrenze und soll zwei Jahre befristet weiterarbeiten.

**Bewertung.** Die Minijob-Verträge unterschreiten den Mindestlohn: 45 Stunden × 13,90 EUR ergeben 625,50 EUR, gezahlt werden 603 EUR. Eine Anpassung des Entgelts überschreitet die Geringfügigkeitsgrenze des § 8 Abs. 1a SGB IV; zulässig sind 2026 höchstens 43 Stunden (43 × 13,90 = 597,70 EUR), 2027 höchstens 43 Stunden (43 × 14,60 = 627,80 EUR). Die Abrufverträge ohne Stundenzahl gelten nach § 12 Abs. 1 S. 3 TzBfG als 20-Stunden-Verträge und sind kein Minijob mehr; es drohen Beitragsnachforderungen nach § 28p SGB IV. Den Verkäufer kann die Mandantin nach Erreichen der Regelaltersgrenze sachgrundlos befristet weiterbeschäftigen, weil § 41 Abs. 2 SGB VI das Vorbeschäftigungsverbot ausschließt; der Vertrag ist vor Arbeitsaufnahme schriftlich zu schließen (§ 14 Abs. 4 TzBfG). Sein Arbeitslohn ist bis 2.000 EUR monatlich nach § 3 Nr. 21 EStG steuerfrei.

**Empfehlung.** Stundenkontingente auf 43 Stunden begrenzen und schriftlich fixieren, Abrufverträge mit Wochenstunden versehen, Altfälle mit der Lohnbuchhaltung bereinigen.

## Risiken / typische Fehler

- **Minijob-Grenze nicht mitgezogen** — feste Stundenzahlen führen 2026/2027 entweder zur Mindestlohnunterschreitung oder zum Überschreiten von 603 / 633 EUR.
- **Arbeit auf Abruf ohne Stundenzahl** — die gesetzliche Fiktion von 20 Wochenstunden beendet den Minijob-Status und löst Beitragsnachforderungen aus.
- **Ausschlussfrist ohne Mindestlohn-Ausnahme** — die Klausel ist insoweit unwirksam; bei Neuverträgen droht die Gesamtunwirksamkeit nach § 307 BGB.
- **Aufzeichnungspflicht § 17 MiLoG übersehen** — Bußgeldrisiko auch ohne Unterzahlung.
- **Aktivrente auf Selbständige oder Minijobs angewandt** — die Steuerbefreiung betrifft nach berichteter Gesetzeslage nur Arbeitslohn aus regulärer Beschäftigung; am Gesetzestext prüfen.
- **§ 41 Abs. 2 SGB VI als Freibrief verstanden** — Schriftform, Höchstdauer von acht Jahren und zwölf Verträge bleiben Grenzen.
- **Beendigung zur Regelaltersgrenze nur mündlich** — Textform genügt, Mündlichkeit nicht.
- **Werte 2027 nicht eingeplant** — die Anpassung zum 01.01.2027 steht bereits fest.
