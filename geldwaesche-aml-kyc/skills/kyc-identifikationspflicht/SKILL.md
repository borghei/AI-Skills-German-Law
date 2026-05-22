---
name: kyc-identifikationspflicht
description: "Identifizierung des Vertragspartners (§§ 10, 11 GwG) und des wirtschaftlich Berechtigten (§§ 3 ff. GwG) mit Transparenzregister-Abgleich (§§ 18–26 GwG); Trigger-Schwellen, vereinfachte (§ 14) und verstärkte Sorgfaltspflichten (§ 15), Aufzeichnung § 8 GwG. Use when ein Verpflichteter eine Geschäftsbeziehung aufnimmt, eine Schwellen-Transaktion durchführt oder bei Verdacht KYC nachholt."
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

# /geldwaesche-aml-kyc:kyc-identifikationspflicht

## Zweck

Der Skill strukturiert die KYC-Prüfung („Know your customer") nach §§ 10 ff. GwG: Identifizierung des Vertragspartners, Feststellung des wirtschaftlich Berechtigten, Transparenzregister-Abfrage, Klärung von Zweck und Art der Geschäftsbeziehung sowie kontinuierliche Überwachung. Er trennt zwischen allgemeiner, vereinfachter und verstärkter Sorgfalt und stellt die Aufzeichnungspflicht § 8 GwG (5 Jahre) sicher.

## Eingaben

- Verpflichteten-Typ nach § 2 GwG
- Geschäftsvorgang (Begründung Geschäftsbeziehung / Einzeltransaktion / Verdachtsfall)
- Vertragspartner (natürliche Person / juristische Person / Personengesellschaft / Trust / Stiftung)
- Beteiligungs- und Kontrollstruktur, soweit bekannt
- bei Bargeld / Kunst / Edelmetallen: Transaktionsvolumen (Schwellenwerte)
- Risikoklasse aus der Risikoanalyse (§ 5 GwG, siehe Skill `gwg-risikoanalyse`)
- besondere Indikatoren: PEP-Status, Hochrisikoland-Bezug, ungewöhnliches Konstrukt

## Sub-Agent-Architektur

Researcher liefert §§ 10–17 GwG, §§ 3 ff. GwG, Transparenzregister-Normen §§ 18–26 GwG, BaFin- und FIU-AuA sowie Kommentarstellen (Herzog, Bülte). Drafter erstellt das KYC-Memo mit Identifizierungs-Checkliste, WB-Analyse und Empfehlung zum Pflichtenniveau. Reviewer prüft Vollständigkeit der Identifizierungsdaten, korrekte Anwendung von § 14 / § 15, Transparenzregister-Abgleich, Aufzeichnungspflicht und Hinweis auf Folgepflichten (insb. § 43 GwG).

## Ablauf

### 1. Trigger der Identifizierungspflicht (§ 10 III GwG)

Die Pflicht greift bei:

- **Begründung einer Geschäftsbeziehung** (§ 10 III Nr. 1 GwG) — unabhängig vom Volumen
- **Einzeltransaktion außerhalb einer Geschäftsbeziehung**:
  - Bargeld ≥ 15.000 EUR (oder mehrere kleinere, die augenscheinlich verbunden sind) (§ 10 III Nr. 2 GwG)
  - Güterhändler: Bargeld ≥ 10.000 EUR (§ 4 V GwG); Edelmetallhändler: 2.000 EUR (§ 4 V GwG) `[unverifiziert – aktuellen Schwellenwert prüfen]`
  - Kunsthandel / Kunstvermittler: 10.000 EUR (auch unbar bei bestimmten Konstellationen) `[unverifiziert]`
- **Verdacht** auf Geldwäsche oder Terrorismusfinanzierung (§ 10 III Nr. 3 GwG) — unabhängig von jedem Schwellenwert und unabhängig vom Pflichtenniveau
- **Zweifel an Richtigkeit oder Vollständigkeit** zuvor erhobener Daten (§ 10 III Nr. 4 GwG)

### 2. Identifizierung des Vertragspartners (§ 11 GwG)

**Natürliche Person** (§ 11 IV Nr. 1 GwG): Name (Vor- und Nachname), Geburtsort, Geburtsdatum, Staatsangehörigkeit, Anschrift. Beleg: gültiges Ausweisdokument iSv § 12 I 1 Nr. 1 GwG (Personalausweis, Reisepass, Pass-Ersatz). Erfassung Dokumenten-Nr., ausstellende Behörde, Gültigkeit.

**Juristische Person / Personengesellschaft** (§ 11 IV Nr. 2 GwG): Firma, Name oder Bezeichnung, Rechtsform, Registernummer (sofern vorhanden), Anschrift Sitz / Hauptniederlassung, Mitglieder Vertretungsorgan / gesetzliche Vertreter. Beleg: Auszug aus Handels- / Genossenschafts- / Vereins- / Partnerschafts- / Stiftungsregister oder gleichwertiges amtliches Register.

**Identifizierungsverfahren** (§ 12 I GwG): Vorlage Original / qualifizierte elektronische Signatur / Videoidentifizierung (BaFin-Rundschreiben 3/2017 zur Videoident `[unverifiziert]`) / eID-Funktion / Notar-/Anwalts-Vermittlung (§ 12 I 2 GwG).

### 3. Wirtschaftlich Berechtigter (§ 3 GwG)

**Tatsächlicher WB** (§ 3 II GwG, juristische Person ohne börsenrechtliche Ausnahme):

- jede natürliche Person, die unmittelbar oder mittelbar
  - **mehr als 25 %** der Kapitalanteile hält, oder
  - **mehr als 25 %** der Stimmrechte kontrolliert, oder
  - auf vergleichbare Weise Kontrolle ausübt

**Fiktiver WB** (§ 3 II 5 GwG): Lässt sich nach Ausschöpfung aller Möglichkeiten **kein** tatsächlicher WB ermitteln, gilt der gesetzliche Vertreter, geschäftsführende Gesellschafter oder Partner als WB. Die Fiktion ist zu **begründen** und zu **dokumentieren** — sie ist kein Default.

Bei **Trusts / Treuhand / nicht rechtsfähigen Stiftungen** (§ 3 III GwG): Treugeber, Treuhänder, Protektor, Begünstigte, sowie sonstige natürliche Personen mit beherrschendem Einfluss.

### 4. Transparenzregister-Abgleich (§§ 18–26 GwG)

Seit Umstellung auf Vollregister (Transparenzregister- und Finanzinformationsgesetz, in Kraft seit 01.08.2021) `[unverifiziert – Datum prüfen]` müssen Verpflichtete bei juristischen Personen / Personengesellschaften / Trusts / Stiftungen das Transparenzregister abfragen und mit den selbst erhobenen WB-Daten **abgleichen** (§ 11 V GwG iVm § 23a GwG `[unverifiziert – §-Verweis prüfen]`).

**Unstimmigkeitsmeldung** (§ 23a GwG): Weichen die Registerangaben von den selbst erhobenen Daten ab, ist eine Unstimmigkeit an das registerführende BVA zu melden — dies ist **keine** Verdachtsmeldung nach § 43 GwG und unterliegt nicht dem Tippoff-Verbot des § 47 GwG (str.; herrschend in BaFin-AuA).

### 5. Pflichtenniveau (Risikoanalyse-abhängig)

| Pflichtenniveau | Trigger | Maßnahmen |
|---|---|---|
| **vereinfachte Sorgfalt** § 14 GwG | nachgewiesen niedriges Risiko (z. B. börsennotierte EWR-AG, inländische Behörden) | reduzierter Identifizierungsumfang, lockere Aktualisierung |
| **allgemeine Sorgfalt** § 10 GwG | Standardfall | Identifizierung, WB, Zweck, kontinuierliches Monitoring |
| **verstärkte Sorgfalt** § 15 GwG | PEP § 1 XII; Hochrisikodrittstaat-Bezug § 15 III Nr. 2; komplexe / unübliche Struktur § 15 III Nr. 3; Korrespondenzbankbeziehung außerhalb EWR | Geschäftsleitung-Zustimmung, Herkunft Vermögen / Mittel, verstärkte laufende Überwachung |

### 6. Klärung von Zweck und Art (§ 10 I Nr. 2 GwG)

Plausibilität des Geschäftszwecks dokumentieren. Bei Diskrepanz zwischen erklärtem Zweck und beobachtetem Transaktionsverhalten: Eskalation an GW-Beauftragten, ggf. § 43 GwG-Prüfung.

### 7. Aufzeichnung und Aufbewahrung (§ 8 GwG)

**5 Jahre** ab Ende der Geschäftsbeziehung oder ab Abwicklung der Einzeltransaktion. Aufzeichnungspflicht umfasst Identifizierungsdaten, Kopien der Belege, Risikoeinstufung, Monitoring-Erkenntnisse.

### 8. Folgepflicht: Verdachtsmeldung

KYC-Erkenntnisse können die Meldepflicht nach § 43 GwG auslösen (Skill `verdachtsmeldung-fiu`). Bei Verdacht: **Identifizierung trotzdem durchführen** (§ 10 IX GwG schließt Abbruch nur eng aus), aber **kein Tippoff** und **Stillhaltepflicht** beachten.

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 1 XII GwG](https://www.gesetze-im-internet.de/gwg_2017/__1.html) (PEP-Definition)
- [§ 3 GwG](https://www.gesetze-im-internet.de/gwg_2017/__3.html) (wirtschaftlich Berechtigter)
- [§ 8 GwG](https://www.gesetze-im-internet.de/gwg_2017/__8.html) (Aufzeichnungs- / Aufbewahrungspflicht)
- [§ 10 GwG](https://www.gesetze-im-internet.de/gwg_2017/__10.html) (allgemeine Sorgfaltspflichten, Trigger)
- [§ 11 GwG](https://www.gesetze-im-internet.de/gwg_2017/__11.html) (Identifizierungspflicht)
- [§ 12 GwG](https://www.gesetze-im-internet.de/gwg_2017/__12.html) (Identifizierungsverfahren)
- [§ 14 GwG](https://www.gesetze-im-internet.de/gwg_2017/__14.html) (vereinfachte Sorgfalt)
- [§ 15 GwG](https://www.gesetze-im-internet.de/gwg_2017/__15.html) (verstärkte Sorgfalt; PEP, Hochrisikodrittstaat)
- [§§ 18–26 GwG](https://www.gesetze-im-internet.de/gwg_2017/__18.html) (Transparenzregister)
- [§ 56 GwG](https://www.gesetze-im-internet.de/gwg_2017/__56.html) (Bußgelder)
- [Art. 13, 14, 18, 20 RL (EU) 2015/849](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32015L0849)
- VO (EU) 2024/1624 (AMLR, Kapitel zu CDD) `[unverifiziert – Anwendungsbeginn 2027]`

### Verwaltungsvorschriften

- BaFin, AuA zum GwG, Allgemeiner Teil + Besonderer Teil
- BaFin-Rundschreiben zur Videoidentifizierung `[unverifiziert – aktuelles Rundschreiben prüfen]`
- FIU-AuA für Nichtfinanzsektor

### Kommentare

- Herzog, GwG, X. Aufl. Jahr, §§ 10, 11, 3 (mit Kommentierung WB) `[unverifiziert – Auflage prüfen]`
- Bülte, GwG, §§ 10 ff. `[unverifiziert]`
- Kreitmair, GwG, §§ 3, 11 `[unverifiziert]`

### Rechtsprechung (`[unverifiziert – prüfen in juris]`)

- KG / OLG-Rspr. zu Bußgeldverfahren wegen fehlerhafter KYC `[unverifiziert]`
- BGH zur zivilrechtlichen Haftung von Kreditinstituten bei KYC-Versagen (Bereich Lastschriftrückgabe / Kontoeröffnung) `[unverifiziert]`

## Ausgabeformat

```
KYC-MEMO — §§ 10, 11, 3 GwG
Verpflichteter: <Firma>, § 2 I Nr. <…> GwG
Vorgang: <Geschäftsbeziehung / Einzeltransaktion / Anlass>
Stand: <Datum>

I.   Trigger der Identifizierungspflicht
     - <§ 10 III Nr. 1/2/3/4 GwG, Begründung>

II.  Vertragspartner-Identifizierung § 11 GwG
     - Personendaten / Firma / Register
     - Belegart und -nummer
     - Identifizierungsverfahren § 12 GwG

III. Wirtschaftlich Berechtigter §§ 3 ff. GwG
     - Beteiligungs- / Kontrollkette
     - tatsächlicher WB oder fiktiver WB (Begründung)
     - Transparenzregister-Abgleich (Treffer / Unstimmigkeit?)

IV.  Pflichtenniveau
     - § 14 / § 10 / § 15 GwG (Begründung)
     - PEP-Status, Hochrisikodrittstaat, komplexe Struktur

V.   Zweck und Art der Geschäftsbeziehung
     - Plausibilität, beobachtetes Transaktionsverhalten

VI.  Aufzeichnung § 8 GwG
     - Aufbewahrung 5 Jahre, Speicherort, Verantwortlicher

VII. Folgepflichten
     - Monitoring-Trigger
     - Hinweis auf § 43 GwG (Verdachtsmeldung) — falls einschlägig

VIII. Risiken / offene Punkte
     🟢 / 🟡 / 🔴

IX.  Quellenverzeichnis
```

## Beispiel (Auszug, Gutachtenstil)

> **III. Wirtschaftlich Berechtigter**
>
> Der Vertragspartner ist die A-GmbH (HRB 12345 AG München). Anteilseigner ist nach Gesellschafterliste die B-Holding S.à r.l. (Luxemburg) mit 100 %; deren Anteile werden zu 60 % von einer zypriotischen C-Holding Ltd. und zu 40 % von einer natürlichen Person Y gehalten. C-Holding wird ihrerseits durch einen Jersey-Trust gehalten, dessen Begünstigte nach Trust Deed eine natürliche Person X ist. Damit hält X mittelbar 60 % × 100 % = 60 % der A-GmbH und ist wirtschaftlich Berechtigter iSv § 3 II 1 Nr. 1 GwG; ebenso Y mit 40 %. Beide sind nach §§ 11 V, 23a GwG ins Transparenzregister einzutragen bzw. dort abzugleichen. Die Konstruktion über Jersey-Trust ist ein Risikofaktor iSv § 15 III Nr. 3 GwG (komplexe Struktur), sodass verstärkte Sorgfalt anzuwenden ist (vgl. Herzog, GwG, § 15 Rn. 20 ff. `[unverifiziert]`).

## Risiken / typische Fehler

- **Identifizierung über Kopie ohne Originalvorlage / Videoident / eID** außerhalb der gesetzlich zugelassenen Verfahren — unwirksam, Bußgeld § 56 GwG.
- **Fiktiver WB als Default** ohne dokumentierten Ermittlungsversuch — § 3 II 5 GwG verlangt **vorrangige** Ermittlung des tatsächlichen WB.
- **Transparenzregister-Abgleich unterlassen** oder Unstimmigkeit nicht gemeldet — Verletzung § 23a GwG `[unverifiziert – konkrete Norm prüfen]`.
- **PEP-Status unbeachtet** — § 1 XII GwG erfasst auch Familienangehörige und nahestehende Personen; verstärkte Sorgfalt nach § 15 III Nr. 1 GwG obligatorisch.
- **Hochrisikodrittstaaten-Liste nicht abgefragt** (delegierte VO der KOM) — Risiko § 15 III Nr. 2 GwG übersehen.
- **Aufzeichnung < 5 Jahre / Speicherort nicht zugriffsbereit für Aufsicht** — Verstoß § 8 GwG.
- **Verdachtsindikator übersehen** und KYC-Prüfung als Routine behandelt — Folge: unterlassene § 43-Meldung, ggf. § 261 StGB.
