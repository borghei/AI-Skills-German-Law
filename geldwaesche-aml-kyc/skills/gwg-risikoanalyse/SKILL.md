---
name: gwg-risikoanalyse
description: "Aufbau und Aktualisierung der institutsspezifischen Risikoanalyse nach § 5 GwG – Risikokategorien (Kunde / Produkt / Vertriebsweg / Geografie), Berücksichtigung Supranationale und Nationale Risk Assessment, Risikoklassen und Ableitung des Pflichtenniveaus §§ 10–17 GwG. Use when ein Verpflichteter iSv § 2 GwG die Risikoanalyse erstmals erstellen, jährlich fortschreiben oder anlassbezogen anpassen muss."
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

# /geldwaesche-aml-kyc:gwg-risikoanalyse

## Zweck

Der Skill erzeugt das Grundgerüst einer **dokumentierten** Risikoanalyse nach § 5 GwG, ordnet Risikofaktoren den vier Pflichtkategorien (Kunde, Produkt / Dienstleistung, Vertriebsweg, geografisches Risiko) zu und leitet daraus das Sorgfaltspflichtenniveau (§§ 10, 14, 15 GwG) ab. Er stellt sicher, dass die Analyse die Supranationale Risikoanalyse der EU-Kommission und die Nationale Risikoanalyse des BMF berücksichtigt und mindestens jährlich oder anlassbezogen aktualisiert wird.

## Eingaben

- Verpflichteten-Typ nach § 2 GwG (Kreditinstitut, Finanzdienstleister, Versicherer, Vermögensverwalter, RA / StB / Notar, Güterhändler ab Schwelle, Immobilienmakler, Edelmetall- / Kunsthändler, Glücksspielanbieter, Krypto-Verwahrer)
- Geschäftsmodell (Produktportfolio, Kundengruppen, Vertriebskanäle, geografische Reichweite)
- bestehende Risikoanalyse (falls vorhanden, mit Datum und letzter Aktualisierung)
- aufsichtsrechtlicher Rahmen (BaFin / Zoll / Landesaufsicht)
- besondere Vorfälle seit letzter Analyse (Verdachtsmeldungen, Prüfungsfeststellungen, Sanktionsverfahren)

## Sub-Agent-Architektur

Researcher liefert § 5 GwG mit Bezug zu § 4 (risikobasierter Ansatz) und § 6 (interne Sicherungsmaßnahmen), Supranationale + Nationale Risikoanalyse, BaFin- und FIU-Auslegungshinweise sowie Kommentarstellen. Drafter erstellt das Risikoanalyse-Dokument mit Methodik, Risikofaktoren-Matrix, Risikoklassen und Ableitung des Pflichtenniveaus. Reviewer prüft Vollständigkeit der vier Kategorien, Dokumentationsdichte, Aktualisierungsturnus und Anbindung an § 6 GwG-Sicherungsmaßnahmen.

## Ablauf

### 1. Verpflichteten-Eigenschaft

Vor Beginn klären, **welche** Nummer des § 2 I GwG einschlägig ist — der Pflichtenumfang variiert (z. B. § 2 I Nr. 1: Kreditinstitute; Nr. 10: RA / StB / Notare nur bei Katalogtätigkeiten; Nr. 14: Güterhändler erst ab Bargeldschwelle iSv § 4 V GwG). Bei mehrfacher Einstufung gilt das jeweils strengere Pflichtenregime.

### 2. Methodik der Risikoanalyse (§ 5 GwG)

Die Risikoanalyse muss schriftlich vorliegen, **nachvollziehbar** sein, und die Methodenwahl dokumentieren. Üblich:

- qualitative Bewertung pro Risikofaktor (niedrig / normal / hoch)
- quantitative Gewichtung (z. B. Scorecard)
- aggregierte Risikoklasse je Geschäftsbeziehung / Transaktion

Maßstab und Mindestinhalt: Herzog, GwG, X. Aufl. Jahr, § 5 Rn. 1 ff. `[unverifiziert – Auflage prüfen]`; BaFin, Auslegungs- und Anwendungshinweise zum GwG, Allgemeiner Teil.

### 3. Externe Quellen einbeziehen

- **Supranationale Risikoanalyse** der EU-Kommission (Art. 6 RL (EU) 2015/849, alle zwei Jahre)
- **Nationale Risikoanalyse (NRA)** des BMF (zuletzt aktualisiert; konkrete Ausgabe `[unverifiziert – Stand prüfen]`)
- **Sektorale Risikoanalysen** der zuständigen Aufsicht (BaFin für Banken / Versicherer / FDI; Landes-RAK / StBK / Notarkammer; Zoll-FIU; Glücksspielbehörde)
- **EU-Liste der Hochrisikoländer** (delegierte VO der KOM nach Art. 9 RL 2015/849)
- **FATF-Empfehlungen** und FATF-Länderlisten

### 4. Vier Risikokategorien (§ 5 I GwG)

| Kategorie | Beispielindikatoren (nicht abschließend) |
|---|---|
| **Kunde** | natürliche / juristische Person; Branche; PEP-Eigenschaft § 1 XII GwG; Nominee-Strukturen; bargeldintensives Geschäft; Bestandskunde vs. Neukunde |
| **Produkt / Dienstleistung** | Produkte mit Anonymitätspotenzial (Inhaberinstrumente, E-Geld, Krypto), grenzüberschreitende Zahlungen, Korrespondenzbank-Beziehungen, Trade Finance |
| **Vertriebsweg** | Präsenz-Onboarding vs. Fernidentifizierung (Videoident, eID); Vermittler / Tippgeber; nicht regulierte Intermediäre |
| **Geografisches Risiko** | EU-Hochrisikoländer-Liste; FATF-Listen; Offshore-Zentren; Sanktionsländer (UN, EU, OFAC); Korruptionsindex (TI CPI) |

### 5. Risikoklassen und Pflichtenniveau

| Risikoklasse | Pflichtenniveau | Norm |
|---|---|---|
| niedrig (mit nachgewiesener Begründung) | vereinfachte Sorgfalt | § 14 GwG |
| normal | allgemeine Sorgfalt | § 10 GwG |
| hoch (PEP, Hochrisikoland, komplexe Struktur, ungewöhnliches Transaktionsverhalten) | verstärkte Sorgfalt | § 15 GwG |

Die Zuordnung darf nicht pauschal sein — jede Klasse ist auf den konkreten Geschäftsvorgang anzuwenden.

### 6. Anbindung an § 6 GwG (interne Sicherungsmaßnahmen)

Die Risikoanalyse muss in konkrete Sicherungsmaßnahmen münden: Verfahren zur Kundenannahme, Monitoring, Mitarbeiterzuverlässigkeit, Schulung, GW-Beauftragter (§ 7 GwG, bei Kreditinstituten + Stellvertreter, MaRisk AT 4.4.3). Ohne diese Anbindung ist die Risikoanalyse formal unvollständig.

### 7. Aktualisierung

Mindestens **jährlich** und **anlassbezogen** (neue Produkte, neue Märkte, geänderte Aufsichtsleitlinien, neue NRA / SNRA, sichtbare Veränderung des Bedrohungsbildes). Aktualisierungen sind zu dokumentieren mit Datum, Anlass und Verantwortlichem.

### 8. Bußgeldrisiko

Pflichtverletzung iSv § 5 GwG ist Ordnungswidrigkeit nach § 56 I Nr. 6 GwG `[unverifiziert – konkrete Nr. prüfen]`. Bußgeldrahmen bei vorsätzlichen Verstößen bis 1 Mio. EUR bzw. 10 % des jährlichen Gesamtumsatzes (§ 56 III GwG).

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 4 GwG](https://www.gesetze-im-internet.de/gwg_2017/__4.html) (risikobasierter Ansatz)
- [§ 5 GwG](https://www.gesetze-im-internet.de/gwg_2017/__5.html) (Risikoanalyse)
- [§ 6 GwG](https://www.gesetze-im-internet.de/gwg_2017/__6.html) (interne Sicherungsmaßnahmen)
- [§ 7 GwG](https://www.gesetze-im-internet.de/gwg_2017/__7.html) (Geldwäschebeauftragter)
- [§§ 10, 14, 15 GwG](https://www.gesetze-im-internet.de/gwg_2017/__10.html) (Pflichtenniveau)
- [§ 56 GwG](https://www.gesetze-im-internet.de/gwg_2017/__56.html) (Bußgelder)
- [Art. 6, 7, 8 RL (EU) 2015/849](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32015L0849) (Risikobewertungspflichten)
- VO (EU) 2024/1624 (AMLR, Art. 9–11 Risikobewertung) `[unverifiziert – Anwendungsbeginn 2027]`

### Verwaltungsvorschriften

- BaFin, Auslegungs- und Anwendungshinweise zum GwG, Allgemeiner Teil und Besonderer Teil Kreditinstitute
- FIU-Auslegungs- und Anwendungshinweise (für Nichtfinanzsektor)
- BMF, Nationale Risikoanalyse `[unverifiziert – aktuellen Stand prüfen]`
- EU-Kommission, Supranational Risk Assessment, COM(2022) 554 final `[unverifiziert – aktuelle Ausgabe prüfen]`
- MaRisk (AT 4.4.3 Compliance-Funktion, BT 5 GW-Prävention)

### Kommentare

- Herzog, GwG, X. Aufl. Jahr, § 5 Rn. 1 ff. `[unverifiziert – Auflage prüfen]`
- Bülte, GwG, § 5 Rn. 1 ff. `[unverifiziert]`
- Kreitmair, GwG, § 5 Rn. 1 ff. `[unverifiziert]`
- Quedenfeld, Handbuch Bekämpfung Geldwäsche und Wirtschaftskriminalität, X. Aufl., Kap. zu Risikomanagement `[unverifiziert]`

### Rechtsprechung (`[unverifiziert – prüfen in juris]`)

- Bußgeld-Rspr. zu § 56 GwG (Aufsichts- und Verwaltungsgerichte, vereinzelt KG / OLG) — konkrete Aktenzeichen sind im Modellwissen nicht zuverlässig erinnerbar; in juris mit Suchstring „GwG Risikoanalyse Bußgeld" recherchieren.

## Ausgabeformat

```
RISIKOANALYSE — § 5 GwG
Verpflichteter: <Firma / Kanzlei>, § 2 I Nr. <…> GwG
Stand: <Datum>   Verantwortlich: <Name GW-Beauftragter>
Letzte Aktualisierung: <Datum>   Nächste Wiedervorlage: <Datum + 12 Monate>

I.   Methodik
     - Bewertungslogik (qualitativ / quantitativ / Scorecard)
     - Berücksichtigte externe Quellen (SNRA, NRA, BaFin-AuA, FATF)

II.  Risikofaktoren
     1. Kunde
        - <Faktor> → Bewertung (niedrig / normal / hoch) → Begründung
     2. Produkt / Dienstleistung
     3. Vertriebsweg
     4. Geografisches Risiko

III. Risikoklassen und Pflichtenniveau
     - niedrig → § 14 GwG (vereinfachte Sorgfalt)
     - normal → § 10 GwG
     - hoch   → § 15 GwG (verstärkte Sorgfalt)

IV.  Interne Sicherungsmaßnahmen § 6 GwG
     - Kundenannahme, Monitoring, Mitarbeiterschulung, GW-Beauftragter

V.   Aktualisierungsregime
     - jährlich + anlassbezogen

VI.  Risiken / offene Punkte
     🟢 / 🟡 / 🔴 <Einstufung mit Begründung>

VII. Quellenverzeichnis
```

## Beispiel (Auszug, Gutachtenstil)

> **III. Risikoklassen und Pflichtenniveau**
>
> Die Geschäftsbeziehung zu einer in Deutschland ansässigen mittelständischen GmbH ohne PEP-Bezug und ohne Hochrisikoland-Bezug fällt nach den unter II. zusammengetragenen Indikatoren in die Risikoklasse „normal". Anwendbar ist daher § 10 I GwG (allgemeine Sorgfaltspflichten: Identifizierung des Vertragspartners, Abklärung des wirtschaftlich Berechtigten gem. §§ 10 I Nr. 2, 11 V GwG, Klärung von Zweck und angestrebter Art der Geschäftsbeziehung, kontinuierliche Überwachung). Eine vereinfachte Sorgfalt nach § 14 GwG kommt nicht in Betracht, weil eine nachgewiesen niedrige Risikolage iSd § 14 I GwG nicht belegt ist; das pauschale Argument „inländischer Mittelstand" trägt nicht (vgl. Herzog, GwG, § 14 Rn. 12 ff. `[unverifiziert]`).

## Risiken / typische Fehler

- **Risikoanalyse als „Schubladendokument"** ohne Anbindung an konkrete Sicherungsmaßnahmen (§ 6 GwG) — formaler Verstoß, Bußgeldrisiko nach § 56 GwG.
- **Pauschale Einstufung „niedriges Risiko"** ohne Begründung der vereinfachten Sorgfalt § 14 GwG — Aufsicht und FIU-AuA verlangen Einzelfallbegründung.
- **PEP-Status unbeachtet** — § 1 XII GwG erfasst auch ausländische und nationale Amtsträger sowie Angehörige; ohne strukturierte PEP-Abfrage ist § 15 III GwG verletzt.
- **Keine Aktualisierung** seit > 12 Monaten oder trotz neuer NRA / EU-Hochrisikoliste — verletzt § 5 II GwG.
- **GW-Beauftragter ohne Stellvertreter** bei Verpflichteten mit entsprechender Pflicht (§ 7 GwG iVm Branchenspezifik) — MaRisk-Verstoß bei Kreditinstituten.
- **AMLR / AMLA-Übergang ignoriert** — ab Anwendungsbeginn `[unverifiziert – 2027]` greifen vollharmonisierte Pflichten; Risikoanalyse sollte schon jetzt darauf vorbereitet sein.
