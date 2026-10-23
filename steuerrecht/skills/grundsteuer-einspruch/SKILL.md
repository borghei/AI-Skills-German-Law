---
name: grundsteuer-einspruch
description: "Rechtsschutz gegen die reformierte Grundsteuer (ab 2025) – dreistufiges Verfahren Grundsteuerwertbescheid / Grundsteuermessbescheid (Finanzamt) / Grundsteuerbescheid (Gemeinde), Bindung des Folgebescheids §§ 182, 351 Abs. 2 AO, Einspruch gegen den richtigen Bescheid, Nachweis des niedrigeren gemeinen Werts (40-%-Grenze, § 220 Abs. 2 BewG), Fortschreibung und Fehlerbeseitigung, Bundesmodell §§ 252–257 BewG (BFH II R 25/24) und Landesmodelle (BW, BY, HH, HE, NI), Ruhen § 363 Abs. 2 AO wegen anhängiger Verfassungsbeschwerden, Aussetzung der Vollziehung § 361 Abs. 3 AO. Rechtsstand Oktober 2026. Use when ein Eigentümer Grundsteuerwert, Messbetrag oder Grundsteuer angreifen oder einen niedrigeren Wert nachweisen will."
language: de
provider_variants:
  - claude
  - gemini
  - openai
test: ./test.md
---

# /steuerrecht:grundsteuer-einspruch

> **Rechtsstand: Oktober 2026.** Bundesmodell: vom BFH für verfassungsgemäß gehalten (BFH, Urt. v. 12.11.2025 – II R 25/24, II R 31/24, II R 3/25) `[unverifiziert – prüfen]`; Verfassungsbeschwerden beim BVerfG anhängig (1 BvR 472/26, 1 BvR 551/26) `[unverifiziert – prüfen]`. Landesmodell Baden-Württemberg: vom BFH für verfassungsgemäß gehalten (BFH, Urt. v. 22.04.2026 – II R 26/24, II R 27/24) `[unverifiziert – prüfen]`. Hamburg und Hessen: Verhandlung beim BFH am 11.11.2026 (II R 12/25, II R 15/25); Bayern: II R 33/25 anhängig `[unverifiziert – prüfen]`. Entwurf JStG 2026 (BT-Drs. 21/8283, nicht verabschiedet): § 1 Abs. 2 Nr. 7 AO soll die AdV-Begrenzung des § 361 Abs. 2 S. 4 AO und § 361 Abs. 3 AO auch für die Gemeinden anwendbar machen.

## Zweck

Seit dem 01.01.2025 wird die Grundsteuer auf Grundlage der neuen Grundsteuerwerte (Hauptfeststellung auf den 01.01.2022) erhoben. Die meisten Fehler im Rechtsschutz entstehen dadurch, dass Eigentümer den **falschen Bescheid** angreifen: Einwendungen gegen den Wert müssen gegen den Grundsteuerwertbescheid des Finanzamts erhoben werden, nicht gegen den Grundsteuerbescheid der Gemeinde. Dieser Skill ordnet die Einwendung der richtigen Stufe zu, prüft Fristen, Bewertungsfehler und den Nachweis eines niedrigeren Werts und steuert Ruhen und AdV im Licht der anhängigen Verfassungsverfahren.

## Eingaben

- Bundesland und Belegenheitsgemeinde (Bundesmodell oder Landesmodell?)
- Vorliegende Bescheide mit Datum: Grundsteuerwertbescheid (bzw. Grundsteueräquivalenzbetrags-/Flächenbescheid in Landesmodellen), Grundsteuermessbescheid, Grundsteuerbescheid der Gemeinde
- Stand: Einspruch eingelegt? Bestandskraft? Bereits Fortschreibung beantragt?
- Objektart (Ein-/Zweifamilienhaus, Wohnungseigentum, Mietwohngrundstück, Geschäftsgrundstück, unbebaut), Fläche, Baujahr, Bodenrichtwert
- Anhaltspunkte für einen deutlich niedrigeren Verkehrswert (Kaufpreis, Gutachten, Belastungen, Bauschäden)
- Hebesatz und dessen Entwicklung (ggf. differenzierte Hebesätze)

## Sub-Agent-Architektur

Ein **Stufen-Prüfer** ordnet jede Einwendung dem richtigen Bescheid zu. Ein **Fristen-Prüfer** rechnet Einspruchs- und Widerspruchsfristen und prüft bei Bestandskraft die Fortschreibungswege. Ein **Bewertungs-Prüfer** rechnet den Grundsteuerwert nach und bewertet die Nachweismöglichkeit des niedrigeren gemeinen Werts. Ein **Verfassungs-Prüfer** entscheidet über Ruhen, AdV und den Umgang mit den anhängigen BFH- und BVerfG-Verfahren.

## Ablauf

### 1. Drei Stufen, drei Bescheide

| Stufe | Bescheid | Behörde | Rechtsbehelf | Einwendungen |
|---|---|---|---|---|
| 1 | **Grundsteuerwertbescheid** (Feststellung, § 219 BewG) | Finanzamt | Einspruch (§ 347 AO), dann FG | Wert, Grundstücksart, Zurechnung, Verfassungsmäßigkeit des Bewertungsrechts |
| 2 | **Grundsteuermessbescheid** (§ 184 AO) | Finanzamt | Einspruch, dann FG | Messzahl, Steuerbefreiung, Steuerpflicht |
| 3 | **Grundsteuerbescheid** | Gemeinde (in Stadtstaaten teils Finanzamt) | nach Landesrecht Widerspruch oder unmittelbar Klage zum **Verwaltungsgericht** | nur Hebesatz und Berechnung |

- **Bindungswirkung**: Der Grundsteuerwertbescheid ist Grundlagenbescheid für den Messbescheid, dieser für den Grundsteuerbescheid ([§ 182 AO](https://www.gesetze-im-internet.de/ao_1977/__182.html)). Einwendungen gegen eine Grundlage können **nur** gegen den Grundlagenbescheid erhoben werden ([§ 351 Abs. 2 AO](https://www.gesetze-im-internet.de/ao_1977/__351.html)).
- **Landesmodelle** mit eigenen Bescheidtypen: Baden-Württemberg (modifiziertes Bodenwertmodell), Bayern (wertunabhängiges Flächenmodell), Hamburg (Wohnlagemodell), Hessen (Flächen-Faktor-Verfahren), Niedersachsen (Flächen-Lage-Modell). Die übrigen Länder wenden das **Bundesmodell** an (Saarland und Sachsen mit abweichenden Steuermesszahlen). Einzelheiten und Nachweisregeln stehen im jeweiligen Landesgrundsteuergesetz — vor Beratung Landesrecht prüfen.

### 2. Fristen und Bestandskraft

- Einspruch: **ein Monat** nach Bekanntgabe ([§ 355 AO](https://www.gesetze-im-internet.de/ao_1977/__355.html)); Bekanntgabe per Post am vierten Tag nach Aufgabe (§ 122 Abs. 2 AO).
- Viele Grundsteuerwertbescheide aus 2022/2023 sind **bestandskräftig**. Dann verbleiben:
  - **Wertfortschreibung** (§ 222 Abs. 1 BewG), wenn der auf volle 100 EUR abgerundete Wert zu Beginn eines Kalenderjahres um **mehr als 15.000 EUR** vom zuletzt festgestellten Wert abweicht,
  - **Fehlerbeseitigung** (§ 222 Abs. 3 BewG) — Beseitigung eines Fehlers der letzten Feststellung im Wege der Fortschreibung; Fortschreibungszeitpunkt ist der Beginn des Kalenderjahres, in dem das Finanzamt den Fehler feststellt (§ 222 Abs. 4 BewG) — der Antrag sollte deshalb vor Jahresende gestellt werden; Vertrauensschutz nach § 176 AO gilt entsprechend,
  - Antrag auf Ansatz des niedrigeren gemeinen Werts im Fortschreibungsverfahren (Schritt 4).
- Gegen den Grundsteuerbescheid der Gemeinde gelten landesrechtliche Widerspruchs- und Klagefristen (in der Regel ein Monat, § 70 bzw. § 74 VwGO).

### 3. Bewertung prüfen — Bundesmodell

- **Ertragswertverfahren** für Ein- und Zweifamilienhäuser, Mietwohngrundstücke und Wohnungseigentum (§§ 252–257 BewG): typisierte Nettokaltmiete nach Mietniveaustufe, Bewirtschaftungskosten, Vervielfältiger, abgezinster Bodenwert.
- **Sachwertverfahren** für Geschäfts- und gemischt genutzte Grundstücke (§§ 258–260 BewG).
- Prüfpunkte: Wohnfläche (Abgrenzung Nutzfläche, Keller, Garagen), Baujahr bzw. Kernsanierung, Grundstücksart, Bodenrichtwert und Grundstücksfläche, wirtschaftliche Einheit (mehrere Flurstücke), Zurechnung bei Erbbaurecht.
- Häufigste Fehler: falsche Flächen aus der Erklärung (Eigenfehler!), Doppelerfassung von Garagen, falsches Baujahr.

### 4. Nachweis des niedrigeren gemeinen Werts (§ 220 Abs. 2 BewG)

- Der niedrigere gemeine Wert ist als Grundsteuerwert anzusetzen, wenn der Steuerpflichtige nachweist, dass der Grundsteuerwert **erheblich** vom gemeinen Wert abweicht; davon ist auszugehen, wenn der Grundsteuerwert den nachgewiesenen gemeinen Wert **um mindestens 40 %** übersteigt ([§ 220 BewG, Volltext](https://www.gesetze-im-internet.de/bewg/__220.html)).
- **Maßgeblicher Stichtag**: Auch der niedrigere gemeine Wert ist nach den **Wertverhältnissen am Hauptfeststellungszeitpunkt 01.01.2022** zu ermitteln; § 227 BewG bleibt ausdrücklich unberührt (§ 220 Abs. 2 S. 6 BewG). Ein späterer Preisverfall (z. B. Zinswende 2023–2026) beweist deshalb nichts.
- **Nachweismittel**:
  - **Gutachten** des örtlichen Gutachterausschusses oder eines Sachverständigen für die Bewertung von Grundstücken, **bezogen auf den 01.01.2022** (§ 220 Abs. 2 S. 3 BewG verweist auf § 198 Abs. 1 S. 2, Abs. 2 BewG);
  - **Kaufpreis** über die wirtschaftliche Einheit, der im gewöhnlichen Geschäftsverkehr **innerhalb eines Jahres vor oder nach dem Hauptfeststellungszeitpunkt** (also zwischen 01.01.2021 und 01.01.2023) zustande gekommen ist, wenn die maßgeblichen Verhältnisse gegenüber dem 01.01.2022 unverändert sind (§ 220 Abs. 2 S. 4 BewG).
- Nutzungsrechte und grundstücksbezogene Belastungen zählen nur, soweit sie nach Inhalt und Entstehung mit der Beschaffenheit der Einheit zusammenhängen (§ 220 Abs. 2 S. 5 BewG) — ein privat bestelltes Wohnrecht senkt den Wert nicht ohne Weiteres.
- Gleich lautende Ländererlasse vom 30.04.2025 regeln Einzelheiten `[unverifiziert – prüfen]`.
- **Landesmodelle** haben eigene Öffnungsklauseln, z. B. Baden-Württemberg nach § 38 Abs. 4 des Landesgrundsteuergesetzes `[unverifiziert – prüfen]`; Hamburg und Niedersachsen weichen ebenfalls ab.
- Kosten-Nutzen: Ein Gutachten lohnt nur, wenn die 40-%-Schwelle realistisch erreichbar ist und die jährliche Ersparnis die Kosten in überschaubarer Zeit trägt.

### 5. Verfassungsrechtliche Einwände: Ruhen statt Klage

- **Bundesmodell**: Der BFH hat die Bewertungsregeln für Wohnungseigentum (§§ 252–257 BewG) für verfassungsgemäß gehalten und nicht vorgelegt; der Gesetzgeber habe seine Spielräume nicht ausgeschöpft, ohne dass dies zur Verfassungswidrigkeit führe (BFH, Urt. v. 12.11.2025 – II R 25/24) `[unverifiziert – prüfen]`.
- Gegen die Urteile sind **Verfassungsbeschwerden** anhängig (1 BvR 472/26, 1 BvR 551/26) `[unverifiziert – prüfen]`. Ein Einspruch, der sich darauf stützt, **ruht kraft Gesetzes** ([§ 363 Abs. 2 S. 2 AO](https://www.gesetze-im-internet.de/ao_1977/__363.html)) — Aktenzeichen im Einspruch ausdrücklich benennen.
- **Allgemeinverfügung**: Nach Abschluss der Musterverfahren kann die Verwaltung anhängige Masseneinsprüche per Allgemeinverfügung zurückweisen (§ 367 Abs. 2b AO; Entwurf JStG 2026: § 367 Abs. 2c AO). Wer individuelle Bewertungsfehler hat, muss sie gesondert vortragen, damit der Einspruch nicht mit der Verfassungsfrage untergeht.
- **Landesmodelle**: Verfahrensstand je Land beobachten (BW entschieden, HH/HE Verhandlung 11.11.2026, BY anhängig).

### 6. Aussetzung der Vollziehung

- AdV des **Grundsteuerwertbescheids** führt nach [§ 361 Abs. 3 AO](https://www.gesetze-im-internet.de/ao_1977/__361.html) zur AdV der Folgebescheide; die Gemeinde muss den Grundsteuerbescheid aussetzen.
- Ernstliche Zweifel bei **individuellen** Bewertungsfehlern oder konkret belegtem Überbewertungsnachweis; wegen der Verfassungsfrage allein ist AdV nach der BFH-Entscheidung zum Bundesmodell schwer zu erreichen. Frühere AdV-Beschlüsse des BFH (2024) zur fehlenden Nachweismöglichkeit `[unverifiziert – prüfen]` sind durch § 220 Abs. 2 BewG teilweise überholt.
- Siehe `/steuerrecht:aussetzung-der-vollziehung`.

### 7. Hebesatz und Gemeinde

- Den Hebesatz bestimmt die Gemeinde durch Satzung (§ 25 des Grundsteuergesetzes); einzelne Länder erlauben **differenzierte Hebesätze** für Wohn- und Nichtwohngrundstücke (z. B. Nordrhein-Westfalen) `[unverifiziert – prüfen]`.
- Einwendungen gegen den Hebesatz (z. B. fehlende Aufkommensneutralität) richten sich gegen den Grundsteuerbescheid der Gemeinde — Verwaltungsrechtsweg; Erfolgsaussichten gering, da Aufkommensneutralität rechtlich nicht bindend ist.
- **Mieter**: Die Grundsteuer ist umlagefähig (§ 2 Nr. 1 BetrKV); Mieter haben keine Einspruchsbefugnis gegen die Bescheide des Eigentümers.

## Ausgabeformat

```
GRUNDSTEUER — Rechtsschutzprüfung — <Eigentümer> — <Objekt> — <Datum> — Rechtsstand Oktober 2026

I.    Land / Modell:                  <Land — Bundesmodell / Landesmodell …>

II.   Bescheide
      Grundsteuerwertbescheid:        <Datum — Wert — Bestandskraft ja/nein>
      Grundsteuermessbescheid:        <Datum — Messbetrag>
      Grundsteuerbescheid Gemeinde:   <Datum — Hebesatz — Betrag>

III.  Einwendungen → richtige Stufe
      <Einwendung — Stufe 1 / 2 / 3 — Rechtsbehelf — Frist>

IV.   Bewertung
      Nachrechnung:                   <Abweichungen: Fläche / Baujahr / Bodenwert …>
      Niedrigerer gemeiner Wert (40 %): [erreichbar / nicht — Nachweismittel …]

V.    Bei Bestandskraft
      Fortschreibung / Fehlerbeseitigung: <…>

VI.   Verfassungsfrage
      Ruhen (§ 363 Abs. 2 S. 2 AO):   [1 BvR 472/26 / Landesverfahren …]
      Individueller Vortrag gesichert: [✓ / ✗]

VII.  AdV (§ 361 Abs. 3 AO):          [beantragt gegen Grundsteuerwertbescheid / nicht]

VIII. Empfehlung:                     <…>
```

## Beispiel (Gutachtenstil, verkürzt)

E, Eigentümerin einer Eigentumswohnung in Köln (Bundesmodell), erhält im Oktober 2026 einen geänderten Grundsteuerbescheid der Stadt mit höherem Hebesatz und will „gegen die Grundsteuer" vorgehen, weil der Grundsteuerwert von 310.000 EUR viel zu hoch sei. Gegen den Grundsteuerwertbescheid hat sie 2023 Einspruch eingelegt, der wegen der Verfassungsfrage ruht. E hat die Wohnung im März 2022 von einem fremden Dritten für 200.000 EUR gekauft; seither ist nichts verändert worden. Der Einwand betrifft den Wert, also die Stufe 1; gegen den Grundsteuerbescheid der Gemeinde kann E ihn nicht vorbringen (§ 351 Abs. 2 AO). Im noch offenen Einspruch gegen den Grundsteuerwertbescheid kann E den niedrigeren gemeinen Wert nachweisen. Der Kaufpreis ist ein taugliches Nachweismittel, weil er im gewöhnlichen Geschäftsverkehr innerhalb eines Jahres nach dem Hauptfeststellungszeitpunkt 01.01.2022 zustande kam und die Verhältnisse unverändert sind (§ 220 Abs. 2 S. 4 BewG). Der Grundsteuerwert übersteigt ihn um 55 % und damit um mindestens 40 % (§ 220 Abs. 2 S. 2 BewG). Ergebnis: Den Kaufvertrag im Einspruch vorlegen und den Ansatz von 200.000 EUR beantragen; die Gemeinde muss den Grundsteuerbescheid nach Änderung des Grundlagenbescheids anpassen. Abwandlung: Hätte E die Wohnung erst im Mai 2026 für 200.000 EUR verkauft, wäre dieser Preis kein Nachweis — er liegt außerhalb des Jahresfensters und spiegelt nicht die Wertverhältnisse vom 01.01.2022 (§ 220 Abs. 2 S. 6 BewG i. V. m. § 227 BewG); nötig wäre ein Gutachten auf den 01.01.2022.

## Risiken / typische Fehler

- **Falscher Bescheid angegriffen** — Wert-Einwände gegen den Grundsteuerbescheid der Gemeinde sind ausgeschlossen (§ 351 Abs. 2 AO); Einspruch gegen den Grundsteuerwertbescheid beim Finanzamt.
- **Bestandskraft übersehen** — dann nur Fortschreibung oder Fehlerbeseitigung; Wirkung erst für künftige Jahre.
- **40-%-Schwelle** ohne belastbaren Nachweis behauptet — Gutachten auf den 01.01.2022 oder Kaufpreis aus dem Jahresfenster um den Hauptfeststellungszeitpunkt erforderlich; aktuelle Verkaufspreise beweisen nichts; Kosten-Nutzen prüfen.
- **Landesmodell mit Bundesrecht geprüft** — Bayern, Baden-Württemberg, Hamburg, Hessen und Niedersachsen haben eigene Regeln und Bescheide.
- **Ruhen nicht beantragt** — anhängige Verfassungsbeschwerden konkret benennen; sonst droht Zurückweisung.
- **Masseneinspruch ohne individuellen Vortrag** — geht bei einer Allgemeinverfügung mit unter.
- **Eigene Erklärungsfehler** (Fläche, Baujahr) nicht korrigiert — Fehlerbeseitigung beantragen.
- **AdV gegen den Grundsteuerbescheid der Gemeinde beantragt** — AdV gehört an den Grundlagenbescheid; Folgewirkung über § 361 Abs. 3 AO.

## Quellen

### Statute

- [§ 182 AO](https://www.gesetze-im-internet.de/ao_1977/__182.html), [§ 184 AO](https://www.gesetze-im-internet.de/ao_1977/__184.html), [§ 351 AO](https://www.gesetze-im-internet.de/ao_1977/__351.html), [§ 355 AO](https://www.gesetze-im-internet.de/ao_1977/__355.html), [§ 361 AO](https://www.gesetze-im-internet.de/ao_1977/__361.html), [§ 363 AO](https://www.gesetze-im-internet.de/ao_1977/__363.html), [§ 367 AO](https://www.gesetze-im-internet.de/ao_1977/__367.html), [§ 1 AO](https://www.gesetze-im-internet.de/ao_1977/__1.html)
- Bewertungsgesetz: [§ 219](https://www.gesetze-im-internet.de/bewg/__219.html), [§ 220](https://www.gesetze-im-internet.de/bewg/__220.html), [§ 222](https://www.gesetze-im-internet.de/bewg/__222.html), [§§ 252–257](https://www.gesetze-im-internet.de/bewg/__252.html), [§§ 258–260](https://www.gesetze-im-internet.de/bewg/__258.html)
- Grundsteuergesetz: [§ 25](https://www.gesetze-im-internet.de/grstg_1973/__25.html) (Hebesatz)
- [§ 2 BetrKV](https://www.gesetze-im-internet.de/betrkv/__2.html) (Umlage), [§ 70 VwGO](https://www.gesetze-im-internet.de/vwgo/__70.html), [§ 74 VwGO](https://www.gesetze-im-internet.de/vwgo/__74.html)
- Landesgrundsteuergesetze BW, BY, HH, HE, NI (Landesrecht, nicht auf gesetze-im-internet.de)

### Gesetzgebung (nicht in Kraft)

- Regierungsentwurf JStG 2026, BT-Drs. 21/8283, Art. 18 Nr. 2 (§ 1 Abs. 2 Nr. 7 AO)

### Verwaltungsanweisungen

- AEAO zu §§ 182, 351 AO
- Gleich lautende Erlasse der obersten Finanzbehörden der Länder vom 30.04.2025 zum Nachweis des niedrigeren gemeinen Werts `[unverifiziert – prüfen]`

### Rechtsprechung (alle `[unverifiziert – prüfen]`)

- BFH, Urt. v. 12.11.2025 – II R 25/24 (Bundesmodell verfassungsgemäß); ebenso II R 31/24, II R 3/25 — Volltext auf bundesfinanzhof.de prüfen
- BFH, Urt. v. 22.04.2026 – II R 26/24, II R 27/24 (Landesgrundsteuergesetz BW verfassungsgemäß)
- BFH – II R 12/25, II R 15/25 (HH, HE; Verhandlung 11.11.2026); II R 33/25 (BY)
- BVerfG – 1 BvR 472/26, 1 BvR 551/26 (Verfassungsbeschwerden, anhängig)

### Literatur

- Suchstring juris: „§ 220 Abs. 2 BewG niedrigerer gemeiner Wert 40 Prozent Nachweis Gutachten"
