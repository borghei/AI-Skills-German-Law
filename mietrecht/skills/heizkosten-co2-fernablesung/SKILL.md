---
name: heizkosten-co2-fernablesung
description: "Heizkostenabrechnung, Fernablesung und CO2-Kostenaufteilung im Wohnraummietrecht – Verbrauchserfassung und Verteilung §§ 4–9 HeizkostenV (50–70 % nach Verbrauch), Nachrüstpflicht für fernablesbare Ausstattung bis 31.12.2026 § 5 Abs. 3 HeizkostenV, monatliche Verbrauchsinformation § 6a HeizkostenV, Kürzungsrechte 15 % und 3 % § 12 HeizkostenV, CO2-Stufenmodell §§ 5–7 CO2KostAufG mit 3-%-Kürzung § 7 Abs. 4, Erstattungsanspruch des selbstversorgenden Mieters § 6, hälftige Teilung von Netzentgelten, CO2- und Beimischungskosten bei neuen Gas-/Ölheizungen ab 2028/2029 §§ 5a, 5b CO2KostAufG (GModG v. 23.07.2026), CO2-Preis § 10 BEHG. Rechtsstand: Oktober 2026. Use when eine Heizkostenabrechnung erstellt oder geprüft, die Fernablese-Nachrüstung geplant oder die CO2-Aufteilung berechnet wird."
language: de
provider_variants: [claude, gemini, openai]
test: ./test.md
---

# /mietrecht:heizkosten-co2-fernablesung

## Zweck

Die Heizkostenabrechnung ist der fehleranfälligste Teil der Betriebskostenabrechnung, und sie bekommt Ende 2026 eine harte Frist: Alle nicht fernablesbaren Zähler und Heizkostenverteiler müssen bis zum **31.12.2026** nachgerüstet oder ersetzt sein. Daneben verlangt das CO2KostAufG eine eigene Aufteilungsrechnung, die durch das Gebäudemodernisierungsgesetz (GModG) ab 2028 eine zweite Stufe erhält. Diese Skill prüft die Heizkostenverteilung, rechnet die CO2-Aufteilung, bestimmt die Kürzungsrechte des Mieters und plant die Nachrüstung. Für die allgemeine Betriebskostenabrechnung: `/mietrecht:betriebskostenabrechnung`.

**Rechtsstand: Oktober 2026.**

- **Geltend:** HeizkostenV in der Fassung seit 01.12.2021 (Fernablesbarkeit); CO2KostAufG seit 01.01.2023; §§ 5a, 5b CO2KostAufG durch das Gesetz v. 23.07.2026 (BGBl. 2026 I Nr. 226, in Kraft 29.07.2026) eingefügt, anwendbar ab Abrechnungszeiträumen 2028 bzw. 2029; CO2-Preiskorridor 2026: 55–65 EUR/t.
- **Anhängig, nicht geltend:** Fortgeltung des Preiskorridors für 2027 wegen Verschiebung des EU-ETS2 auf 2028 (BEHG-Änderung, 1. Lesung 24.09.2026) `[unverifiziert – prüfen]`.

## Eingaben

- Heizkostenabrechnung des Messdienstleisters und Betriebskostenabrechnung des Vermieters
- Art der Versorgung: zentrale Heizung, Fernwärme, Gasetagenheizung des Mieters (Selbstversorgung)
- Installierte Ausstattung: Baujahr / Einbaudatum, fernablesbar ja/nein, Smart-Meter-Gateway-fähig
- Verteilungsschlüssel (Verbrauchs- und Grundkostenanteil), Gebäudebaujahr und Dämmung der Leitungen
- Brennstoffrechnung mit CO2-Ausweis (§ 3 CO2KostAufG): Emissionen in kg, CO2-Kosten, Emissionsfaktor
- Wohnfläche des Gebäudes bzw. der Wohnung
- Neue Heizungsanlage nach § 43 GModG (Gas/Öl mit Beimischungspflicht)? Einbaudatum
- Erhaltene monatliche Verbrauchsinformationen (§ 6a HeizkostenV)

## Sub-Agent-Architektur

Die Prüfung wird in Prosa von spezialisierten Schritten getragen; einen `agents`-Block trägt diese Skill bewusst nicht (mietrecht-Konvention).

- Ein **Ausstattungs-Prüfer** klärt Fernablesbarkeit und Nachrüststatus. Davon hängt das 3-%-Kürzungsrecht der HeizkostenV ab.
- Ein **Verteilungs-Prüfer** kontrolliert den Verbrauchsanteil (50–70 %), die Sonderfälle mit zwingend 70 % und die Warmwassertrennung.
- Ein **CO2-Rechner** bestimmt die Emission pro m², die Stufe und die Aufteilung.
- Ein **GModG-Prüfer** klärt, ob ab 2028/2029 die hälftige Teilung nach §§ 5a, 5b CO2KostAufG greift.
- Ein **Kürzungs-Prüfer** führt alle Kürzungsrechte zusammen und verhindert eine Doppelzählung.

## Ablauf

### 1. Pflicht zur Verbrauchserfassung ([§§ 4, 5 HeizkostenV](https://www.gesetze-im-internet.de/heizkostenv/__5.html))

Der Gebäudeeigentümer hat den anteiligen Verbrauch an Wärme und Warmwasser zu erfassen. Für die Ausstattung gelten zwei Stichtage und eine Frist:

| Zeitraum | Anforderung |
|---|---|
| Einbau nach dem 01.12.2021 | nur **fernablesbare** Geräte (§ 5 Abs. 2 S. 1 HeizkostenV) |
| Einbau ab dem 01.12.2022 | zusätzlich sicher an ein **Smart-Meter-Gateway** anbindbar (BSI-Schutzprofile) und interoperabel (§ 5 Abs. 2, 5 HeizkostenV) |
| Altgeräte (nicht fernablesbar) | **Nachrüstung oder Ersatz bis 31.12.2026** (§ 5 Abs. 3 HeizkostenV), außer bei technischer Unmöglichkeit, unverhältnismäßigem Aufwand oder unbilliger Härte |

Eine Ausnahme gilt für den Ersatz oder die Ergänzung **einzelner** Geräte in einem System, dessen übrige Geräte noch nicht fernablesbar sind. **Handlungsempfehlung für den Vermieter (Stand Oktober 2026):** Aufträge an den Messdienstleister **jetzt** vergeben; die Ausnahmegründe des § 5 Abs. 3 S. 2 HeizkostenV schriftlich dokumentieren, wenn sie in Anspruch genommen werden.

### 2. Monatliche Verbrauchsinformation ([§ 6a HeizkostenV](https://www.gesetze-im-internet.de/heizkostenv/__6a.html))

Sind fernablesbare Geräte installiert, müssen die Nutzer **monatlich** Abrechnungs- oder Verbrauchsinformationen erhalten (Verbrauch, Vergleich zum Vormonat und Vorjahresmonat, Durchschnittsnutzer). Mit der Abrechnung sind zusätzliche Informationen nach § 6a Abs. 3 HeizkostenV mitzuteilen, darunter Brennstoffmix, Steuern und Abgaben sowie Kontaktdaten von Verbraucherorganisationen.

### 3. Verteilung ([§§ 6–9 HeizkostenV](https://www.gesetze-im-internet.de/heizkostenv/__7.html))

- **Heizkosten:** mindestens 50 %, höchstens 70 % nach erfasstem Verbrauch, der Rest nach Wohnfläche oder umbautem Raum (§ 7 Abs. 1 S. 1 HeizkostenV).
- **Zwingend 70 %:** bei Gebäuden, die nicht die Anforderungen der Wärmeschutzverordnung 1994 erfüllen, mit Öl- oder Gasheizung und überwiegend gedämmten freiliegenden Leitungen (§ 7 Abs. 1 S. 2 HeizkostenV).
- **Warmwasser:** gesonderte Erfassung und Verteilung (§§ 8, 9 HeizkostenV); bei verbundenen Anlagen ist die Wärmemenge für Warmwasser mit einem Wärmezähler zu messen (§ 9 Abs. 2 HeizkostenV).
- **Geräteausfall:** Schätzung nach § 9a HeizkostenV, höchstens für 25 % der Fläche bzw. des Verbrauchs; darüber hinaus Verteilung nach Fläche.
- **Ausnahmen:** § 11 HeizkostenV (z. B. Passivhäuser, unverhältnismäßige Kosten).

### 4. Kürzungsrechte des Mieters ([§ 12 HeizkostenV](https://www.gesetze-im-internet.de/heizkostenv/__12.html))

| Grund | Kürzung | Norm |
|---|---|---|
| Keine verbrauchsabhängige Abrechnung entgegen der HeizkostenV | **15 %** des Kostenanteils | § 12 S. 1 HeizkostenV |
| Keine fernablesbare Ausstattung entgegen § 5 Abs. 2 oder 3 HeizkostenV | **3 %** | § 12 S. 2 HeizkostenV |
| Monatliche Information nach § 6a HeizkostenV fehlt ganz oder teilweise | **3 %** | § 12 S. 3 HeizkostenV |
| CO2-Anteil nicht ermittelt oder Angaben nach § 7 Abs. 3 CO2KostAufG fehlen | **3 %** der Heizkosten | § 7 Abs. 4 CO2KostAufG |

Die Kürzungsrechte gelten nicht im Verhältnis zwischen Wohnungseigentümer und Gemeinschaft (§ 12 S. 4 HeizkostenV). **Ab Abrechnungszeiträumen 2027** werden nicht nachgerüstete Altgeräte regelmäßig die 3-%-Kürzung nach § 12 S. 2 HeizkostenV auslösen.

### 5. CO2-Kostenaufteilung ([CO2KostAufG](https://www.gesetze-im-internet.de/co2kostaufg/))

1. **Lieferantenangaben** (§ 3 CO2KostAufG): Brennstoffmenge, Emissionen, CO2-Kosten.
2. **Spezifische Emission** des Gebäudes in kg CO2 je m² Wohnfläche und Jahr, auf eine Nachkommastelle gerundet (§ 5 Abs. 1 CO2KostAufG). Versorgt der Vermieter eine Wohnung gesondert, gilt die Rechnung für diese Wohnung.
3. **Stufe** nach der Anlage zum CO2KostAufG: unter 12 kg trägt der Mieter 100 %, ab 52 kg der Vermieter 95 %; dazwischen acht Stufen in 5-kg-Schritten.
4. **Abzug** des Vermieteranteils und Verteilung des Mieteranteils nach dem Heizkostenschlüssel (§ 7 Abs. 1 CO2KostAufG).
5. **Ausweis** in der Abrechnung (§ 7 Abs. 3 CO2KostAufG): Mieteranteil, Einstufung und Berechnungsgrundlagen. Fehlt der Ausweis, darf der Mieter um 3 % kürzen (§ 7 Abs. 4 CO2KostAufG).

**Selbstversorgende Mieter** (Gasetagenheizung): Der Mieter rechnet die Stufe selbst und hat gegen den Vermieter einen **Erstattungsanspruch** nach § 6 CO2KostAufG, der innerhalb von **zwölf Monaten** ab der Abrechnung des Lieferanten gegenüber dem Mieter in Textform geltend zu machen ist (§ 6 Abs. 2 S. 3 CO2KostAufG); ohne Verrechnung muss der Vermieter spätestens zwölf Monate nach der Anzeige erstatten (S. 5). Der Vermieter kann ihn mit der nächsten Betriebskostenabrechnung verrechnen.

**Nichtwohngebäude:** hälftige Teilung (§ 8 CO2KostAufG). **Beschränkungen** der energetischen Sanierung (Denkmal-, Milieuschutz) ermäßigen den Vermieteranteil (§ 9 CO2KostAufG).

### 6. Neu durch das GModG: hälftige Teilung bei neuen Gas-/Ölheizungen (§§ 5a, 5b CO2KostAufG)

Wird in einem Bestandsgebäude (§ 5a) oder Neubau (§ 5b) eine Heizungsanlage nach **§ 43 GModG** eingebaut und betrieben, tragen Vermieter und Mieter **jeweils die Hälfte**:

- der **Gasnetzentgelte** (Netzentgeltbestandteil der Gasrechnung nach dem EnWG, vgl. https://www.gesetze-im-internet.de/enwg_2005/__40.html) für Abrechnungszeiträume ab dem **01.01.2028**,
- der **CO2-Kosten**, abweichend vom Stufenmodell, ab dem **01.01.2028**,
- der Mehrkosten der **anteilig zu nutzenden Brennstoffe** (Beimischung) ab dem **01.01.2029**, begrenzt auf höchstens 30 % des insgesamt verbrauchten Brennstoffs.

Für Ersatzbeschaffungen nach einem irreparablen Ausfall gelten befristete Ausnahmen (§ 5a Abs. 4 CO2KostAufG); eine Härtefallregel enthält § 5d CO2KostAufG. Der Ausweis richtet sich nach § 7 Abs. 5 CO2KostAufG, einschließlich des 3-%-Kürzungsrechts. Vertiefung zur Mieterhöhung nach dem Heizungstausch: `/mietrecht:heizungstausch-559e-559f`.

### 7. Abrechnungsfristen

Es gelten die Fristen des [§ 556 Abs. 3 BGB](https://www.gesetze-im-internet.de/bgb/__556.html): Abrechnung binnen zwölf Monaten nach Ende des Abrechnungszeitraums, Einwendungen binnen zwölf Monaten nach Zugang. Die Kürzungsrechte sind **Einwendungen** und unterliegen der Einwendungsfrist.

## Deterministische Berechnung

```bash
# Abrechnungsfrist § 556 Abs. 3 S. 2 BGB für Abrechnungsjahr 2026
python -m scripts.legal_calc.cli frist --ereignis 31.12.2026 --menge 12 --einheit monate --land HE

# Einwendungsfrist § 556 Abs. 3 S. 5 BGB: Ablauf des zwölften Monats nach Zugang (Monatsendregel).
# Zugang am 15.06.2027 → Ereignis = Monatsende 30.06.2027 → Fristende 30.06.2028
python -m scripts.legal_calc.cli frist --ereignis 30.06.2027 --menge 12 --einheit monate --land HE
```

**CO2-Rechenweg** (von Hand, gegen die Anlage zum CO2KostAufG zu prüfen):

```
Emission (kg) / Wohnfläche Gebäude (m²) = kg CO2/m²·a  → Stufe laut Anlage
CO2-Kosten gesamt × Vermieteranteil (%) = Vermieteranteil EUR
CO2-Kosten gesamt − Vermieteranteil     = Mieteranteil → Verteilung nach HeizkostenV-Schlüssel
```

## Quellen

### Statute

- [HeizkostenV](https://www.gesetze-im-internet.de/heizkostenv/) — [§ 5 HeizkostenV](https://www.gesetze-im-internet.de/heizkostenv/__5.html), [§ 6a HeizkostenV](https://www.gesetze-im-internet.de/heizkostenv/__6a.html), [§ 7 HeizkostenV](https://www.gesetze-im-internet.de/heizkostenv/__7.html), [§ 9a HeizkostenV](https://www.gesetze-im-internet.de/heizkostenv/__9a.html), [§ 12 HeizkostenV](https://www.gesetze-im-internet.de/heizkostenv/__12.html)
- [CO2KostAufG](https://www.gesetze-im-internet.de/co2kostaufg/) — [§ 5](https://www.gesetze-im-internet.de/co2kostaufg/__5.html), [§ 5a](https://www.gesetze-im-internet.de/co2kostaufg/__5a.html), [§ 7](https://www.gesetze-im-internet.de/co2kostaufg/__7.html) (Kohlendioxidkostenaufteilungsgesetz)
- [§ 556 BGB](https://www.gesetze-im-internet.de/bgb/__556.html), [§ 556a BGB](https://www.gesetze-im-internet.de/bgb/__556a.html)
- [BEHG](https://www.gesetze-im-internet.de/behg/) (Preiskorridor § 10), Gesetz v. 23.07.2026, BGBl. 2026 I Nr. 226 (GModG)

### Kommentare

- Lammel, Heizkostenverordnung, aktuelle Auflage `[unverifiziert – prüfen]`
- Schmidt-Futterer, Mietrecht, 16. Aufl. 2024, HeizkostenV (Bearbeiter und Rn. vor Zitat prüfen)

### Rechtsprechung

- BGH, Urt. v. 20.01.2016 – VIII ZR 93/15 (formelle Anforderungen an die Betriebskostenabrechnung; gilt auch für die Heizkostenabrechnung als ihr Bestandteil) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2016-01-20&Aktenzeichen=VIII%20ZR%2093/15
- Zur Anwendung des CO2KostAufG und zu § 5 Abs. 3 HeizkostenV liegt nach dem Kenntnisstand dieser Skill (Oktober 2026) **keine** verifizierte BGH-Rechtsprechung vor.

## Formulierungshilfe — Einwendung gegen die Heizkostenabrechnung

```
Sehr geehrte Damen und Herren,

gegen die Heizkostenabrechnung für <Zeitraum>, zugegangen am <Datum>,
erhebe ich folgende Einwendungen:

1. Die Heizkosten wurden zu <…> % nach Verbrauch verteilt. Das unterschreitet
   die Mindestquote des § 7 Abs. 1 HeizkostenV; ich kürze meinen Anteil nach
   § 12 S. 1 HeizkostenV um 15 %.
2. Die Heizkostenverteiler sind nicht fernablesbar. Ich kürze nach § 12 S. 2
   HeizkostenV um weitere 3 %.
3. Die Abrechnung weist die Einstufung des Gebäudes nach dem CO2KostAufG und
   die Berechnungsgrundlagen nicht aus. Ich kürze nach § 7 Abs. 4
   CO2KostAufG um 3 %.

Den sich ergebenden Betrag von <…> EUR zahle ich unter Vorbehalt bzw.
rechne ihn mit dem Guthaben auf.

Mit freundlichen Grüßen
```

## Ausgabeformat

```
HEIZKOSTEN / CO2 — Prüfung — <Mandat-ID> — <Datum>

I.    Ausstattung
      - fernablesbar                     [✅ / ❌ — Nachrüstung bis 31.12.2026]
      - Smart-Meter-Gateway / Interop.   [✅ / ❌ / N/A]
      - monatliche Info § 6a             [✅ / ❌]
II.   Verteilung (§ 7 HeizkostenV)       Verbrauch <…> %  [50–70 / 70 zwingend / Verstoß]
      Warmwasser getrennt (§§ 8, 9)      [✅ / ❌]
III.  CO2KostAufG
      - Emission                         <…> kg CO2/m²·a → Stufe <…>
      - Vermieter / Mieter               <…> % / <…> %
      - Ausweis § 7 Abs. 3               [✅ / ❌]
      - §§ 5a/5b (GModG) ab 2028/2029    [N/A / greift ab <Jahr>]
IV.   Kürzungen
      - § 12 S. 1 (15 %)                 [—/✓]
      - § 12 S. 2, 3 (3 %)               [—/✓]
      - § 7 Abs. 4 CO2KostAufG (3 %)     [—/✓]
V.    Fristen § 556 Abs. 3               Abrechnung bis <Datum> / Einwendung bis <Datum>

Ergebnis: <Nachzahlung / Guthaben nach Kürzungen>
Risiko: [🟢 / 🟡 / 🔴]
```

## Risiken / typische Fehler

- **Nachrüstfrist 31.12.2026 verpasst** — ab den Abrechnungszeiträumen 2027 droht das 3-%-Kürzungsrecht nach § 12 S. 2 HeizkostenV in jeder Abrechnung.
- **Monatliche Verbrauchsinformation unterlassen** — eigenständiges 3-%-Kürzungsrecht (§ 12 S. 3 HeizkostenV).
- **Stufenmodell mit falscher Fläche gerechnet** — maßgeblich ist die Wohnfläche des Gebäudes bzw. der gesondert versorgten Wohnung.
- **CO2-Ausweis fehlt** — 3 % Kürzung nach § 7 Abs. 4 CO2KostAufG.
- **GModG-Teilung zu früh angewendet** — die hälftige Teilung nach § 5a CO2KostAufG gilt erst für Abrechnungszeiträume ab 2028 (Beimischung ab 2029).
- **Preiskorridor 2027 als feststehend behandelt** — die BEHG-Änderung ist noch nicht verabschiedet.
- **Kürzungsrechte außerhalb der Einwendungsfrist geltend gemacht** — die Zwölfmonatsfrist des § 556 Abs. 3 S. 5 BGB gilt auch für sie.
