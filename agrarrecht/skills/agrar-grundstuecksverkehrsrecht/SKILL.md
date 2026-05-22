---
name: agrar-grundstuecksverkehrsrecht
description: "Prüfung der Genehmigungspflicht eines Verkaufs landwirtschaftlicher Flächen nach GrdstVG, der Versagungsgründe nach § 9 GrdstVG, des siedlungsrechtlichen Vorkaufsrechts nach § 4 RSG und der Anzeige- und Beanstandungspflicht bei Landpachtverträgen nach LPachtVG. Statutory anchors: §§ 2, 6, 9, 22 GrdstVG; §§ 4, 6 RSG; §§ 2, 4 LPachtVG; §§ 463 ff., 581 ff. BGB; LwVG. Use when ein Kaufvertrag über landwirtschaftliche Flächen genehmigt werden soll, das Vorkaufsrecht ausgeübt wurde, ein Landpachtvertrag anzuzeigen ist oder eine Beschwerde gegen einen LwG-Beschluss erwogen wird."
language: de
agents:
  researcher: ../../agents/researcher.md
  drafter: ../../agents/drafter.md
  reviewer: ../../agents/reviewer.md
provider_variants:
  - claude
  - gemini
  - openai
test: ./test.md
---

# /agrarrecht:agrar-grundstuecksverkehrsrecht

## Zweck

Der Skill prüft, ob ein Kaufvertrag über landwirtschaftliche Flächen nach dem **Grundstückverkehrsgesetz (GrdstVG)** genehmigungspflichtig ist und welche **Versagungsgründe** nach § 9 GrdstVG einer Genehmigung entgegenstehen können. Er behandelt das **siedlungsrechtliche Vorkaufsrecht** nach § 4 RSG, das die Genehmigungsbehörde an ein Siedlungsunternehmen ausübt, sowie die **Anzeige- und Beanstandungspflicht** bei Landpachtverträgen nach §§ 2, 4 LPachtVG. Reviewer-Blocker: Ohne GrdstVG-Genehmigung ist die Eigentumsübertragung schwebend unwirksam (§ 2 Abs. 1 GrdstVG).

## Eingaben

- Vertragstyp (Kaufvertrag, Schenkung, Tauschvertrag, Landpachtvertrag) und Vertragsdatum
- Lage und Größe der Fläche (Flurstücksbezeichnung als `[Flurst.-Nr.]`, Hektar)
- Nutzungsart (Acker, Grünland, Wald — Sonderfall, BWaldG/LandesWaldG, idR nicht GrdstVG)
- Bundesland (Schwellenwerte landesspezifisch)
- Status der Parteien (Landwirt iSv § 1 ALG / Nichtlandwirt; Mitbieter aus der Landwirtschaft vorhanden?)
- Verfahrensstand (Notarvertrag geschlossen / Genehmigung beantragt / Versagungsbescheid erlassen / Vorkaufsrecht ausgeübt / Beschwerde erhoben)

## Sub-Agent-Architektur

Researcher liefert §§ 2–9, 22 GrdstVG, §§ 4, 6 RSG, §§ 2, 4 LPachtVG, BGB-Vorkaufs- und Pachtnormen, die landesrechtlichen Ausführungsbestimmungen sowie BGH-Landwirtschaftssenat- und OLG-Linien zu § 9 GrdstVG. Drafter erstellt im Gutachtenstil ein Memo zur Genehmigungsfähigkeit oder eine Beschwerdeschrift nach § 22 GrdstVG iVm § 9 LwVG. Reviewer prüft die Genehmigungsfrist, die Vorkaufsausübungsfrist § 6 RSG, die Anzeigefrist § 2 LPachtVG und die schwebende Unwirksamkeit des Vertrags ohne Genehmigung.

## Ablauf

### 1. Anwendungsbereich GrdstVG

Genehmigungspflichtig nach § 2 Abs. 1 GrdstVG ist die rechtsgeschäftliche Veräußerung von **landwirtschaftlichen oder forstwirtschaftlichen Grundstücken**. Ausgenommen sind nach § 2 Abs. 3 GrdstVG insbesondere Grundstücke unter der landesrechtlich bestimmten Mindestgröße (Schwellenwerte je Bundesland zwischen 0,25 ha und 2 ha; konkrete Schwelle dem jeweiligen Landesgesetz entnehmen `[unverifiziert – aktueller Stand prüfen]`). Forstwirtschaftliche Grundstücke unterliegen idR der landesforstrechtlichen Anzeige- statt Genehmigungspflicht.

### 2. Genehmigungsverfahren

Der Notar reicht den Vertrag bei der Genehmigungsbehörde (idR Landkreis / Landwirtschaftsbehörde) ein. Die Behörde entscheidet binnen **1 Monat** ab Eingang (§ 6 Abs. 1 S. 1 GrdstVG); Verlängerung auf bis zu **2 Monate** ist möglich (§ 6 Abs. 1 S. 2). Bei Untätigkeit nach Fristablauf gilt die Genehmigung als erteilt — **Genehmigungsfiktion** § 6 Abs. 2 GrdstVG `[unverifiziert – Wortlaut im aktuellen Stand prüfen]`.

Rechtsfolge des Genehmigungserfordernisses: **schwebende Unwirksamkeit** der Eigentumsübertragung; Auflassung (§ 925 BGB) und Eintragung im Grundbuch werden erst mit Erteilung der Genehmigung (oder Eintritt der Genehmigungsfiktion) wirksam.

### 3. Versagungsgründe § 9 GrdstVG

Die Genehmigung **ist zu versagen** (gebundene Entscheidung), wenn einer der Gründe des § 9 Abs. 1 GrdstVG vorliegt:

| Nr. | Versagungsgrund |
|---|---|
| 1 | **Ungesunde Verteilung des Grund und Bodens** — insb. wenn ein Nichtlandwirt landwirtschaftliche Flächen erwirbt, obwohl ein aufstockungsbedürftiger Landwirt zum Verkehrswert kaufbereit ist (Erwerb durch Nichtlandwirt) |
| 2 | **Unwirtschaftliche Verkleinerung oder Aufteilung** eines lebensfähigen landwirtschaftlichen Betriebs |
| 3 | **Grobes Missverhältnis** zwischen vereinbartem Kaufpreis und Verkehrswert (idR > 50 % über Verkehrswert) |

Maßstab: BGH-BLw-Senat, Linie zu § 9 Abs. 1 Nr. 1 GrdstVG (aufstockungsbedürftiger Landwirt, Kaufbereitschaft zum Verkehrswert) `[unverifiziert – prüfen in juris/openjur]`; ferner BVerfG zum Eingriff in Art. 14 GG durch die Genehmigungsverweigerung `[unverifiziert]`.

### 4. Siedlungsrechtliches Vorkaufsrecht § 4 RSG

Statt zu versagen kann die Genehmigungsbehörde dem **Siedlungsunternehmen** (gemeinnützig anerkannt nach RSG) das Vorkaufsrecht **mitteilen**; dieses kann binnen **2 Monaten ab Mitteilung** ausgeübt werden (§ 6 Abs. 1 RSG i.V.m. § 469 Abs. 2 BGB). Die Ausübungserklärung erfolgt formgebunden gegenüber dem Verkäufer.

Folgen:

- Mit Ausübung kommt der Kaufvertrag zwischen Verkäufer und Siedlungsunternehmen zu denselben Bedingungen zustande (§ 464 Abs. 2 BGB).
- Der ursprüngliche Käufer verliert seine Stellung; ggf. Rückabwicklung zwischen Verkäufer und Erstkäufer nach allgemeinen Regeln (§§ 280 ff., 311a BGB).
- Praxisrelevant: Das Siedlungsunternehmen reicht die Fläche idR weiter an einen aufstockungsbedürftigen Landwirt vor Ort.

Konkurrenz zu anderen Vorkaufsrechten (gemeindliches Vorkaufsrecht § 24 BauGB, Vorkaufsrechte aus BGB-Verträgen) ist gesondert zu prüfen.

### 5. Landpachtverkehrsrecht (LPachtVG)

Landpachtverträge unterliegen idR nicht der Genehmigung, sondern der **Anzeigepflicht** § 2 Abs. 1 LPachtVG: Innerhalb von **1 Monat** nach Vertragsabschluss ist der Vertrag der zuständigen Behörde (Landwirtschaftsamt) anzuzeigen.

Beanstandungsgründe § 4 LPachtVG:

1. Ungesunde Verteilung der Bodennutzung
2. Unwirtschaftliche Aufteilung
3. Pacht in **grobem Missverhältnis** zum Ertrag (idR > 150 % der ortsüblichen Pacht)

Bei großen Pachtflächen oder ungewöhnlich langen Pachtzeiten greift teilweise eine Genehmigungspflicht (§ 5 LPachtVG bzw. landesrechtliche Erweiterung `[unverifiziert]`).

Behörde kann binnen Beanstandungsfrist (idR 1 Monat ab Anzeige) den Vertrag beanstanden; bei Beanstandung Verfahren vor dem Landwirtschaftsgericht.

### 6. Rechtsschutz

- **Beschwerde** gegen den Versagungsbescheid bzw. die Beanstandung beim **OLG-Landwirtschaftssenat** nach §§ 22 ff. GrdstVG iVm § 9 LwVG, Frist regelmäßig **1 Monat** ab Zustellung `[unverifiziert – konkrete Frist prüfen]`.
- **Beschwerde gegen LwG-Beschluss** beim BGH-Landwirtschaftssenat nach Maßgabe der LwVG- und FamFG-Vorschriften (zulassungsabhängig).
- Verfassungsbeschwerde Art. 14 GG bei willkürlicher Versagung möglich; hohe Schwelle.

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 2 GrdstVG](https://www.gesetze-im-internet.de/grdstvg/__2.html) (Genehmigungspflicht)
- [§ 6 GrdstVG](https://www.gesetze-im-internet.de/grdstvg/__6.html) (Genehmigungsfrist, Genehmigungsfiktion)
- [§ 9 GrdstVG](https://www.gesetze-im-internet.de/grdstvg/__9.html) (Versagungsgründe)
- [§ 22 GrdstVG](https://www.gesetze-im-internet.de/grdstvg/__22.html) (Beschwerde)
- [§ 4 RSG](https://www.gesetze-im-internet.de/rsiedlg/__4.html) (Vorkaufsrecht Siedlungsunternehmen)
- [§ 6 RSG](https://www.gesetze-im-internet.de/rsiedlg/__6.html) (Ausübungsfrist)
- [§ 2 LPachtVG](https://www.gesetze-im-internet.de/lpachtvg/__2.html) (Anzeigepflicht)
- [§ 4 LPachtVG](https://www.gesetze-im-internet.de/lpachtvg/__4.html) (Beanstandungsgründe)
- [§§ 463–473 BGB](https://www.gesetze-im-internet.de/bgb/__463.html) (Vorkaufsrecht)
- [§§ 581 ff. BGB](https://www.gesetze-im-internet.de/bgb/__581.html) (Landpacht)
- [LwVG](https://www.gesetze-im-internet.de/lwvg/) (Verfahren in Landwirtschaftssachen)

### Kommentare

- Lange, GrdstVG, 9. Aufl. `[unverifiziert]`
- Netz, Landpachtrecht, Stand `[unverifiziert]`
- Wöhrmann, Landwirtschaftsrecht, Stand `[unverifiziert]`
- Bearbeiter, in: Düsing/Martinez, Agrarrecht, Stand 2024, GrdstVG/RSG/LPachtVG `[unverifiziert]`

### Rechtsprechung (`[unverifiziert – prüfen in juris/openjur]`)

1. BGH-BLw-Senat zur „ungesunden Verteilung" § 9 Abs. 1 Nr. 1 GrdstVG bei Nichtlandwirt-Erwerb und Vorhandensein aufstockungsbedürftiger Landwirte.
2. BGH-BLw-Senat zur Ausübung des Siedlungs-Vorkaufsrechts und zur Frist § 6 RSG.
3. BVerfG zur Verhältnismäßigkeit der GrdstVG-Versagung im Lichte des Art. 14 GG.
4. OLG-Landwirtschaftssenate (Hamm, Celle, Rostock, München) zur Verkehrswertfeststellung und zum „groben Missverhältnis" § 9 Abs. 1 Nr. 3.

## Ausgabeformat

```
GUTACHTEN — Grundstücksverkehrsrechtliche Prüfung
Vertrag: <Notarurkunde Nr., Datum>
Fläche: [Flurst.-Nr.], <ha>, <Nutzung>, <Bundesland>

I. Sachverhalt (knapp)
II. Frage(n)
III. Kurzantwort
     – Genehmigungspflichtig: ja / nein
     – Genehmigungsfähig: ja / nein / fraglich
     – Vorkaufsrecht-Risiko: ja / nein
     – Empfehlung: <Antrag / Beschwerde / Vergleich>

IV. Rechtliche Bewertung
    1. Anwendungsbereich GrdstVG (§ 2; Schwellenwerte landesspez.)
    2. Genehmigungsverfahren (§ 6; Frist 1 Monat / 2 Monate;
       Genehmigungsfiktion)
    3. Versagungsgründe § 9 GrdstVG
       a) Ungesunde Verteilung (Nichtlandwirt; aufstockungsbedürftig)
       b) Unwirtschaftliche Aufteilung
       c) Grobes Missverhältnis Kaufpreis/Verkehrswert
    4. Siedlungs-Vorkaufsrecht § 4 RSG
       (Frist 2 Monate; Ausübungserklärung; Konkurrenz Vorkaufsrechte)
    5. Schwebende Unwirksamkeit ohne Genehmigung
       (§ 2 Abs. 1 GrdstVG; Auflassung & Eintragung)
    6. Rechtsschutz
       (Beschwerde § 22 GrdstVG / § 9 LwVG; Frist)

V. Antrag / Empfehlung

VI. Risiken / offene Punkte
    🟢 / 🟡 / 🔴 <Einstufung mit Begründung>

VII. Frist-Tabelle
     <übernommen vom Researcher>

VIII. Quellenverzeichnis
```

## Beispiel (Auszug, Gutachtenstil)

> **III. Versagungsgrund § 9 Abs. 1 Nr. 1 GrdstVG.** Der Mandant ist Nichtlandwirt iSd § 1 ALG; der konkurrierende Erwerbsinteressent (Landwirt mit Hofstelle 1,8 km entfernt) hat im Genehmigungsverfahren Aufstockungsbedarf belegt und Kaufbereitschaft zum Verkehrswert von 28.500 EUR/ha erklärt `[unverifiziert – konkreter Verkehrswert dem regionalen Bodenrichtwert entnehmen]`. Nach ständiger Linie des BGH-Landwirtschaftssenats `[unverifiziert – prüfen in juris]` führt diese Konstellation zur Versagung wegen ungesunder Verteilung des Grund und Bodens. Eine Genehmigung ist daher nicht zu erwarten. **Alternativ** kann die Behörde nach § 4 RSG dem Siedlungsunternehmen das Vorkaufsrecht mitteilen; die Ausübungsfrist beträgt 2 Monate ab Mitteilung (§ 6 Abs. 1 RSG). **Bis zur Genehmigung oder zum Eintritt der Genehmigungsfiktion (§ 6 Abs. 2 GrdstVG) bleibt die Eigentumsübertragung schwebend unwirksam (§ 2 Abs. 1 GrdstVG); eine Eintragung des Mandanten als Eigentümer ist daher derzeit unmöglich.**

## Risiken / typische Fehler

- **GrdstVG-Genehmigung nicht beantragt** → schwebende Unwirksamkeit; Notar muss den Vertrag der Behörde vorlegen. (🔴 BLOCKER bei Übersehen.)
- **Schwellenwert** des Bundeslands falsch eingeschätzt — die landesrechtliche Mindestgröße variiert.
- **Siedlungs-Vorkaufsrecht** in der Vertragsgestaltung nicht antizipiert; auflösende Bedingung im Kaufvertrag fehlt.
- **Beschwerdefrist § 22 GrdstVG / § 9 LwVG** versäumt; danach Bestandskraft der Versagung.
- **„Grobes Missverhältnis" § 9 Abs. 1 Nr. 3** ohne Verkehrswertgutachten gerügt oder verteidigt.
- **LPachtVG-Anzeige § 2 vergessen** — Beanstandungsrisiko § 4 LPachtVG.
- **Verwechslung der Zuständigkeiten**: Landwirtschaftsgericht (LwVG) für GrdstVG-/LPachtVG-/LwAnpG-Streitigkeiten; **nicht** ordentliche Zivilkammer.
