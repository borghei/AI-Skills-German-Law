---
name: vergabe-eu-schwellenwert-pruefung
description: "Schwellenwert- und Verfahrensprüfung im deutschen Vergaberecht – geschätzter Auftragswert nach § 3 VgV (Vollwertprinzip, Loseregelung § 3 Abs. 7 VgV), Abgleich mit aktuellen EU-Schwellenwerten (VO (EU) – regelmäßig prüfen), Auftraggebereigenschaft § 99 GWB und Empfehlung der Verfahrensart. Use when ein Auftraggeber vor Bekanntmachung klären muss, ob Oberschwellen- (GWB Teil 4 / VgV / SektVO / KonzVgV / VSVgV) oder Unterschwellenbereich (UVgO / VOB/A) gilt."
language: de
agents:
  researcher: ../agents/researcher.md
  drafter: ../agents/drafter.md
  reviewer: ../agents/reviewer.md
provider_variants:
  - claude
  - gemini
  - openai
test: ./test.md
---

# /vergaberecht:vergabe-eu-schwellenwert-pruefung

## Zweck

Vor jeder Beschaffung muss der Auftraggeber prüfen, **welches Vergaberegime gilt**. Dies hängt von drei Variablen ab: Auftraggebereigenschaft (§ 99 GWB), Auftragsgegenstand (Liefer-, Dienst-, Bauleistung, Konzession) und geschätztem Auftragswert (§ 3 VgV) im Verhältnis zum jeweils geltenden EU-Schwellenwert. Dieser Skill führt die Prüfung strukturiert durch und empfiehlt die Verfahrensart.

## Eingaben

- Auftraggeber (Rechtsform, ggf. öffentliche Finanzierung > 50 %, Sektorentätigkeit Anlage I SektVO)
- Auftragsgegenstand (Lieferleistung, Dienstleistung, Bauleistung, Konzession; Beschreibung)
- Geschätzte Vertragslaufzeit (inkl. Verlängerungsoptionen)
- Geschätzter monetärer Wert pro Jahr und Gesamtwert (netto)
- Aufteilung in Lose (geplant, Anzahl, jeweiliger Wert)
- Etwaige verbundene Beschaffungen in den letzten 12 Monaten (§ 3 Abs. 6 VgV)

## Sub-Agent-Architektur

Researcher liefert die einschlägigen Normen (GWB, VgV / SektVO / KonzVgV / VSVgV, UVgO, VOB/A), die aktuelle Schwellenwert-VO und die Rspr. zum Auftraggeberbegriff sowie zur Loseregelung. Drafter führt die dreistufige Prüfung (Auftraggeber → Auftragswert → Verfahrensart) im Gutachtenstil durch. Reviewer prüft, ob die Schwellenwerte korrekt zugeordnet, der Auftragswert nicht künstlich in Lose aufgeteilt (§ 3 Abs. 7 S. 1 VgV) und die Verfahrensart vertretbar empfohlen wurde.

## Ablauf

### 1. Auftraggebereigenschaft § 99 GWB

Dreigliedrige Prüfung:

| Variante | Norm | Inhalt |
|---|---|---|
| Öffentlicher Auftraggeber | § 99 Nr. 1–3 GWB | Gebietskörperschaften, Sondervermögen, juristische Personen des öffentlichen oder privaten Rechts mit Aufgaben im Allgemeininteresse, nichtgewerblich, überwiegend öffentlich finanziert/aufsichtsmäßig kontrolliert |
| Sektorenauftraggeber | § 100 GWB i. V. m. SektVO | Tätigkeit in Anlage I SektVO (Wasser, Energie, Verkehr, Postdienste) |
| Subjektiv-funktionaler Auftraggeber | § 99 Nr. 4 GWB | Private mit überwiegender öffentlicher Bauförderung / Subventionierung |

Maßstab EuGH zur "Funktion im Allgemeininteresse, nichtgewerblicher Art": EuGH, Urt. v. 10.11.1998 – Rs. C-360/96, BFI Holding (https://curia.europa.eu/juris/liste.jsf?language=en&num=C-360/96); EuGH, Urt. v. 22.05.2003 – Rs. C-18/01, Korhonen (https://curia.europa.eu/juris/liste.jsf?language=en&num=C-18/01).

### 2. Auftragswertschätzung § 3 VgV

**Grundsatz Vollwertprinzip** (§ 3 Abs. 1 VgV): Gesamter Auftragswert über die volle Laufzeit, netto, inklusive Optionen und Verlängerungen.

| Konstellation | Norm | Berechnung |
|---|---|---|
| Befristete Verträge ≤ 48 Monate | § 3 Abs. 11 Nr. 1 VgV | Wert der gesamten Laufzeit |
| Unbefristete oder > 48 Monate | § 3 Abs. 11 Nr. 2 VgV | 48-fache Monatsrate |
| Lieferleistungen Leasing | § 3 Abs. 10 VgV | Gesamter Schätzwert |
| Rahmenvereinbarung | § 3 Abs. 12 VgV | Geschätzter Gesamtwert aller Abrufe |
| Lose | § 3 Abs. 7 VgV | Gesamtwert aller Lose; **kein** künstliches Splitting |
| Bagatellklausel Lose | § 3 Abs. 9 VgV | 20 %-Quote / 80 %-Wert: kleine Lose < 80.000 EUR (Liefer/Dienst) bzw. < 1 Mio. EUR (Bau) dürfen unterschwellig vergeben werden, soweit ≤ 20 % des Gesamtwerts |

**Verbot der Aufteilung in Umgehungsabsicht** § 3 Abs. 7 S. 1 VgV. Maßstab Funktionalitätsprüfung (gleicher Beschaffungsgegenstand, sachlich-zeitlicher Zusammenhang): vgl. BGH, Beschl. v. 18.06.2012 – X ZB 9/11, NZBau 2012, 715 `[unverifiziert – prüfen]`.

### 3. Abgleich mit EU-Schwellenwert

Schwellenwerte werden alle zwei Jahre durch delegierte VO der Kommission angepasst (Stand 2024/2025: **VO (EU) 2023/2497**) `[unverifiziert – aktuelle Folge-VO prüfen]`.

Indikative Schwellenwerte 2024/2025 (netto, **prüfen**):

| Auftragstyp | Schwelle |
|---|---|
| Bauaufträge (klassisch, Sektoren, Konzessionen) | 5.538.000 EUR `[unverifiziert]` |
| Liefer-/Dienstleistungen oberste Bundesbehörden | 143.000 EUR `[unverifiziert]` |
| Liefer-/Dienstleistungen sonstige öffentliche AG | 221.000 EUR `[unverifiziert]` |
| Liefer-/Dienstleistungen Sektorenauftraggeber | 443.000 EUR `[unverifiziert]` |
| Soziale und besondere Dienstleistungen Anh. XIV RL 2014/24/EU | 750.000 EUR `[unverifiziert]` |
| Konzessionen | 5.538.000 EUR `[unverifiziert]` |

**Pflicht**: aktuellen Stand bei Anwendung der Skill prüfen.

### 4. Verfahrensartwahl

#### Oberschwellenbereich (≥ Schwelle)

Anwendbares Regelwerk:

- **VgV** für klassische Aufträge öffentlicher Auftraggeber
- **SektVO** für Sektorentätigkeit (Anlage I SektVO)
- **KonzVgV** für Konzessionen
- **VSVgV** für Verteidigung/Sicherheit

Verfahrensarten § 14 VgV:

| Verfahren | Norm | Voraussetzung |
|---|---|---|
| Offenes Verfahren | § 15 VgV | jederzeit |
| Nicht offenes Verfahren mit Teilnahmewettbewerb | § 16 VgV | jederzeit |
| Verhandlungsverfahren mit Teilnahmewettbewerb | § 17 VgV | Tatbestände § 14 Abs. 3 VgV |
| Wettbewerblicher Dialog | § 18 VgV | Tatbestände § 14 Abs. 3 VgV |
| Innovationspartnerschaft | § 19 VgV | innovative Leistung am Markt nicht verfügbar |
| Verhandlungsvergabe ohne Teilnahmewettbewerb | § 14 Abs. 4 VgV | enge Ausnahmen (z. B. Dringlichkeit, ausschließliche Rechte) |

#### Unterschwellenbereich (< Schwelle)

- **UVgO** für Liefer- und Dienstleistungen, soweit durch Land/Bund eingeführt — Landesvergabegesetze beachten
- **VOB/A Abschnitt 1** für Bauaufträge
- Grundsatz: öffentliche Ausschreibung als Regelverfahren, beschränkte Ausschreibung und Verhandlungsvergabe nur bei Vorliegen der Tatbestände der UVgO bzw. VOB/A

### 5. Dokumentation

Vergabevermerk § 8 VgV / § 6 UVgO mit Begründung der Verfahrenswahl, Wertschätzung und Losentscheidung (§ 97 Abs. 4 GWB).

## Quellen und Zitierweise

Verbindlich: [`../../references/zitierweise.md`](../../references/zitierweise.md).

### Statute

- [§ 99 GWB](https://www.gesetze-im-internet.de/gwb/__99.html) (Öffentlicher Auftraggeber)
- [§ 100 GWB](https://www.gesetze-im-internet.de/gwb/__100.html) (Sektorenauftraggeber)
- [§ 106 GWB](https://www.gesetze-im-internet.de/gwb/__106.html) (Schwellenwerte)
- [§ 107 GWB](https://www.gesetze-im-internet.de/gwb/__107.html) (Ausnahmen, In-house § 108 GWB)
- [§ 3 VgV](https://www.gesetze-im-internet.de/vgv_2016/__3.html) (Auftragswertschätzung)
- [§ 14 VgV](https://www.gesetze-im-internet.de/vgv_2016/__14.html) (Verfahrensarten)
- [Art. 4 RL 2014/24/EU](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014L0024) (Schwellenwerte EU)
- VO (EU) 2023/2497 – delegierte Verordnung zur Anpassung der Schwellenwerte `[unverifiziert – Folge-VO prüfen]`

### Kommentare

- Burgi, Vergaberecht, 4. Aufl. 2022, § 13 Rn. 1 ff. (Auftraggeber), § 17 Rn. 1 ff. (Auftragswert)
- Eßer, in: Pünder/Schellenberg, Vergaberecht, 4. Aufl. 2022, § 99 GWB Rn. 10 ff.
- Ziekow, in: Ziekow/Völlink, Vergaberecht, 5. Aufl. 2024, § 3 VgV Rn. 1 ff.
- Müller-Wrede (Hrsg.), Beck'scher Vergaberechtskommentar, § 99 GWB

### Rechtsprechung (`[unverifiziert – prüfen in Beck-Online/juris/eur-lex]`)

1. EuGH, Urt. v. 10.11.1998 – Rs. C-360/96, BFI Holding (Allgemeininteresse, nichtgewerblich)
2. EuGH, Urt. v. 22.05.2003 – Rs. C-18/01, Korhonen (subjektiv-funktional)
3. BGH, Beschl. v. 18.06.2012 – X ZB 9/11, NZBau 2012, 715 (Auftragswert, Splittingverbot)
4. OLG Düsseldorf, Beschl. v. 11.07.2018 – Verg 1/18, NZBau 2018, 638 (Loseregelung) `[unverifiziert]`

## Ausgabeformat

```
SCHWELLENWERT- UND VERFAHRENSPRÜFUNG
Mandat: <…>
Auftraggeber: <…>
Vergabegegenstand: <…>
Stand: <Datum>

I. Sachverhalt
   - Auftraggeber: <…>
   - Beschaffungsgegenstand: <…>
   - Geschätzter Wert (netto, gesamte Laufzeit inkl. Optionen): <EUR>
   - Laufzeit: <Monate>
   - Lose: <…>

II. Auftraggebereigenschaft (§ 99 GWB)
    Subsumtion: <…>
    Ergebnis: <öffentlicher AG / Sektor / subjektiv-funktional / keiner>

III. Auftragswertschätzung (§ 3 VgV)
     Berechnung: <…>
     Lose-Test § 3 Abs. 7 VgV: <Splitting? Bagatellquote § 3 Abs. 9?>
     Ergebnis: geschätzter Gesamtwert <EUR netto>

IV. Anwendbare Schwelle
    Bezug: VO (EU) <…> [unverifiziert – aktuelle VO prüfen]
    Einschlägige Schwelle: <EUR>
    Ergebnis: Ober-/Unterschwellenbereich

V. Empfohlene Verfahrensart
   Begründung: <§ 14 VgV / UVgO / VOB/A>
   Verfahren: <offen / nicht offen / Verhandlungsverfahren / …>

VI. Risiken / offene Punkte
    🟢/🟡/🔴
    - <Lossplitting-Risiko>
    - <Auftraggeberbegriff strittig>
    - <Schwellenwert-Stand>

VII. Quellenverzeichnis
     <gem. references/zitierweise.md>
```

## Beispiele

### Beispiel — IT-Dienstleistung, Kommune, 4 Jahre Laufzeit

> **Sachverhalt:** Stadtverwaltung (öffentlicher AG § 99 Nr. 1 GWB) plant Lizenz + Wartung Fachsoftware, 4 Jahre Laufzeit, jährlich 70.000 EUR netto.
>
> **Auftragswertschätzung:** § 3 Abs. 11 Nr. 1 VgV — 4 × 70.000 = 280.000 EUR netto.
>
> **Schwelle:** 221.000 EUR (sonstige öffentliche AG, Dienstleistung, Stand 2024/2025) `[unverifiziert]`. Auftragswert > Schwelle → Oberschwellenbereich, VgV anwendbar.
>
> **Verfahrensart:** Regelverfahren offenes Verfahren § 15 VgV. Verhandlungsverfahren § 17 VgV nur bei Tatbestand § 14 Abs. 3 VgV (z. B. konzeptionelle Dienstleistung mit Vorab-Unklarheit). Empfehlung: offenes Verfahren, sofern Leistungsbeschreibung eindeutig spezifizierbar.

## Risiken / typische Fehler

- **Lossplitting in Umgehungsabsicht** § 3 Abs. 7 S. 1 VgV → Nachprüfungsantrag durch übergangene Bieter wahrscheinlich.
- **Veraltete Schwellenwerte** zitiert → fehlerhafte Verfahrenswahl → Aufhebung durch Vergabekammer.
- **Verlängerungsoptionen vergessen** in der Schätzung → tatsächlicher Auftragswert überschreitet Schwelle, Vergabe unterhalb der Bekanntmachungspflicht.
- **Auftraggebereigenschaft verneint**, obwohl überwiegende öffentliche Finanzierung > 50 % gegeben — § 99 Nr. 2 GWB zu eng ausgelegt.
- **Verhandlungsverfahren ohne Teilnahmewettbewerb § 14 Abs. 4 VgV** ohne tragfähige Begründung — strenger Ausnahmecharakter.
