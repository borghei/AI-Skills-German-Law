---
name: aufhebungsvertrag
description: "Erstellung und Prüfung eines Aufhebungsvertrags inkl. Sperrzeit § 159 SGB III, Schriftform § 623 BGB und steuerlicher Behandlung der Abfindung § 34 EStG. Use when ein Arbeitsverhältnis einvernehmlich beendet wird oder eine Sperrzeit-Risikobewertung benötigt wird."
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

# /arbeitsrecht:aufhebungsvertrag

## Zweck

Aufhebungsverträge sind das stille Risiko des Arbeitsrechts: technisch ein BGB-Vertrag, praktisch eine Falle, weil **Sperrzeit nach [§ 159 SGB III](https://www.gesetze-im-internet.de/sgb_3/__159.html)** den AN materiell trifft, ohne dass das im Vertragstext steht. Dieser Skill erstellt einen rechtssicheren Entwurf und führt die Sperrzeit-Risikoprüfung **vor** Unterschrift durch.

> **Rechtsstand: Oktober 2026.** Berücksichtigt: Fünftelregelung nur noch in der Veranlagung (seit VZ 2025) und Verzichtsverbot beim Mindesturlaub (BAG 03.06.2025).
## Eingaben

- Beendigungszeitpunkt
- Höhe der Abfindung (BMG × Faktor)
- Beschäftigungsdauer
- Grund der Beendigung (AG-Wunsch / AN-Wunsch / Vergleich nach KSchG-Klage)
- Steuerliche Wünsche (Einmal- vs. Mehrjahresauszahlung)
- Resturlaubs- und Überstundenstatus
- Wettbewerbsverbot?

## Sub-Agent-Architektur

Researcher liefert Statute, Sperrzeit-Rechtsprechung des BSG / BAG, Kommentarstellen. Drafter erstellt den Vertragstext + Sperrzeit-Analyse-Memo. Reviewer prüft Schriftform, Vollständigkeit und Sperrzeit-Mitigation.

## Ablauf

### 1. Schriftform ([§ 623 BGB](https://www.gesetze-im-internet.de/bgb/__623.html))

**Zwingend schriftlich.** Elektronische Form ausgeschlossen. Unterschrift beider Parteien auf demselben Dokument. Verstoß → Nichtigkeit.

### 2. Sperrzeit-Risiko ([§ 159 SGB III](https://www.gesetze-im-internet.de/sgb_3/__159.html))

Sperrzeit von 12 Wochen, wenn AN das Arbeitsverhältnis **gelöst hat** (§ 159 Abs. 1 Nr. 1 SGB III) **ohne wichtigen Grund**.

Wichtiger Grund liegt regelmäßig vor bei:

- konkret drohender, rechtmäßiger betriebsbedingter AG-Kündigung
- Abfindung im Rahmen 0,25–0,5 BMG × Beschäftigungsjahre (Faustformel BA)
- Einhaltung der ordentlichen Kündigungsfrist

Bei Zweifel: Mitteilung an die Bundesagentur für Arbeit nach § 38 SGB III rechtzeitig empfehlen.

**Ruhen des Arbeitslosengeldes** ([§ 158 SGB III](https://www.gesetze-im-internet.de/sgb_3/__158.html)) — getrennt von der Sperrzeit zu prüfen: Endet das Arbeitsverhältnis ohne Einhaltung der ordentlichen Kündigungsfrist des Arbeitgebers und wird eine Abfindung gezahlt, ruht der Anspruch bis zum fiktiven Ende der Kündigungsfrist (höchstens ein Jahr), angerechnet wird ein gestaffelter Teil der Abfindung.

**Sozialversicherung:** Eine echte Abfindung für den Verlust des Arbeitsplatzes ist **beitragsfrei**; als „Abfindung" bezeichnete Nachzahlungen von Arbeitsentgelt (rückständiger Lohn, Urlaubsabgeltung) sind beitragspflichtig.

**Gebot fairen Verhandelns:** Ein Aufhebungsvertrag kann unwirksam sein, wenn er unter Ausnutzung einer psychischen Drucksituation zustande kommt; ein sofortiges Annahmeerfordernis allein genügt dafür nicht (BAG, Urt. v. 24.02.2022 – 6 AZR 333/21 `[unverifiziert – prüfen]`). Ein Widerrufsrecht nach §§ 312 ff. BGB besteht nicht.

**Massenentlassung:** Vom Arbeitgeber veranlasste Aufhebungsverträge zählen bei der Schwelle des § 17 Abs. 1 S. 2 KSchG mit — siehe `/arbeitsrecht:massenentlassungsanzeige`.

### 3. Steuerliche Behandlung ([§ 34 EStG](https://www.gesetze-im-internet.de/estg/__34.html))

„Fünftelregelung" für außerordentliche Einkünfte:

- Abfindung gilt als außerordentliche Einkunft, **wenn** sie in einem Veranlagungszeitraum zufließt.
- Auszahlung über mehrere Jahre zerstört die Fünftelregelung.
- **Seit dem Veranlagungszeitraum 2025** wendet der Arbeitgeber die Fünftelregelung im **Lohnsteuerabzug nicht mehr** an (Wachstumschancengesetz, BGBl. 2024 I Nr. 108); er behält die Lohnsteuer regulär ein. Die Ermäßigung erhält der Arbeitnehmer nur über seine **Einkommensteuerveranlagung** — Liquiditätsnachteil bis zum Bescheid im Folgejahr, daher im Mandantengespräch beziffern.
- Rechtsstand Oktober 2026; eine Pauschalierung der Lohnsteuer für Abfindungen gibt es nicht.

### 4. Klauselkatalog

- Beendigungsdatum + ordentliche Kündigungsfrist eingehalten
- Höhe und Fälligkeit der Abfindung
- Resturlaubs- und Überstundenabgeltung — **Achtung:** Auf den gesetzlichen Mindesturlaub kann im **bestehenden** Arbeitsverhältnis nicht verzichtet werden, auch nicht im gerichtlichen Vergleich und auch nicht bei bereits feststehendem Beendigungsdatum (BAG, Urt. v. 03.06.2025 – 9 AZR 104/24, [bundesarbeitsgericht.de](https://www.bundesarbeitsgericht.de/entscheidung/9-azr-104-24/)). Klauseln „Urlaub ist in natura gewährt" tragen nur, wenn das tatsächlich zutrifft; sonst Urlaub vor Beendigung gewähren oder Abgeltung nach Beendigung regeln.
- Rückgabe von AG-Eigentum (Schlüssel, Hardware, Akten)
- Verschwiegenheitsklausel (häufig wechselseitig)
- Optional: nachvertragliches Wettbewerbsverbot ([§§ 74 ff. HGB](https://www.gesetze-im-internet.de/hgb/__74.html)) — Karenzentschädigung min. 50 % der letzten vertragsmäßigen Leistungen; Fortbestand oder Aufhebung eines bestehenden Verbots **ausdrücklich** regeln (Detail: `/arbeitsrecht:wettbewerbsverbot-nachvertraglich`)
- Optional: Zwischenzeugnis / qualifiziertes Endzeugnis
- Erledigungsklausel (Wirkung auf §§ 138, 779 BGB beachten)

### 5. Erledigungsklausel-Risiken

Pauschalformeln („mit Erfüllung dieses Vertrags sind alle Ansprüche … erledigt") können auch unbekannte Ansprüche aus Bonus, Tantieme, Provision erfassen. Sorgfältige Klauselbestimmung gegen Eigentumsstörung empfohlen ([§ 779 BGB](https://www.gesetze-im-internet.de/bgb/__779.html); Vergleichsanfechtung bei Irrtum).

## Quellen und Zitierweise

Verbindlich: [`../../references/zitierweise.md`](../../references/zitierweise.md).

### Statute

- [§ 623 BGB](https://www.gesetze-im-internet.de/bgb/__623.html), [§ 779 BGB](https://www.gesetze-im-internet.de/bgb/__779.html)
- [§ 159 SGB III](https://www.gesetze-im-internet.de/sgb_3/__159.html)
- [§ 34 EStG](https://www.gesetze-im-internet.de/estg/__34.html)
- [§§ 74 ff. HGB](https://www.gesetze-im-internet.de/hgb/__74.html) (Wettbewerbsverbot)

### Kommentare

- Müller-Glöge, in: MüKoBGB, 9. Aufl. 2023, § 623 Rn. 1 ff.
- Preis, in: ErfK, 24. Aufl. 2024, § 779 BGB Rn. 1 ff.
- Rolfs, in: ErfK, 24. Aufl. 2024, § 159 SGB III Rn. 1 ff.

### Rechtsprechung

- BSG, Urt. v. 17.10.2007 – B 11a/7a AL 52/06 R, NZA 2008, 365 (Sperrzeit Aufhebungsvertrag) `[unverifiziert – prüfen]`
- BSG, Urt. v. 12.07.2006 – B 11a AL 47/05 R (wichtiger Grund bei Aufhebungsvertrag zur Vermeidung einer rechtmäßigen Arbeitgeberkündigung; häufig als Leitentscheidung zitiert — Az. gegen das oben genannte abgleichen) `[unverifiziert – prüfen]`
- BAG, Urt. v. 13.04.2010 – 9 AZR 36/09, NZA 2010, 1308 (Erledigungsklausel) `[unverifiziert – prüfen]`
- BAG, Urt. v. 24.02.2022 – 6 AZR 333/21 (Gebot fairen Verhandelns) `[unverifiziert – prüfen]`
- BAG, Urt. v. 03.06.2025 – 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis, auch nicht im Vergleich), [bundesarbeitsgericht.de](https://www.bundesarbeitsgericht.de/entscheidung/9-azr-104-24/)

## Ausgabeformat

```
AUFHEBUNGSVERTRAG-ENTWURF — <AN-Position> — <Datum>
VERTRAULICH

I.  Sperrzeit-Risikoanalyse
    Risiko: [🟢 niedrig / 🟡 moderat / 🔴 hoch]
    Begründung: <…>
    Mitigations: <…>

II. Vertragstext
    1. Beendigung des Arbeitsverhältnisses
    2. Abfindung (Höhe, Fälligkeit, Steuer)
    3. Urlaubsabgeltung
    4. Rückgabe AG-Eigentum
    5. Verschwiegenheit
    6. Zeugnis
    7. Erledigungsklausel (mit Reichweite)
    8. Schlussbestimmungen

III. Steuerliche Hinweise
     - Fünftelregelung § 34 EStG anwendbar: [ja/nein] — nur in der Veranlagung des AN (seit VZ 2025)
     - Ruhen ALG § 158 SGB III: [ja — bis <Datum> / nein]
     - Steuerlicher Optimierungshinweis: <…>

Offene Fragen:
  - <…>
Empfehlung: <…>
```

## Risiken / typische Fehler

- **Schriftform übersehen** (§ 623 BGB) → Vertrag nichtig.
- **Sperrzeit-Risiko nicht aufgeklärt** → Beratungsfehler-Haftung.
- **Erledigungsklausel zu weit** → unbekannte Ansprüche untergehen.
- **Wettbewerbsverbot ohne Karenzentschädigung** → **nichtig** (§ 74 Abs. 2 HGB); nur eine zu niedrige Karenzentschädigung führt zur Unverbindlichkeit mit Wahlrecht des Arbeitnehmers.
- **Fünftelregelung im Lohnsteuerabzug erwartet** → seit VZ 2025 nur noch über die Veranlagung des Arbeitnehmers.
- **Urlaubsverzicht vereinbart** → unwirksam für den gesetzlichen Mindesturlaub (BAG 03.06.2025).
- **Ruhen nach § 158 SGB III übersehen** → bei verkürzter Kündigungsfrist ruht das Arbeitslosengeld neben einer etwaigen Sperrzeit.
- **Befristete Befreiung von der Arbeitsleistung** ohne ausdrücklichen Hinweis auf Anrechnung anderweitigen Verdienstes.
