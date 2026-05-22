---
name: prodhaftg-herstellerhaftung
description: "Parallele Anspruchsprüfung verschuldensunabhängige Herstellerhaftung nach §§ 1, 3 ProdHaftG und Produzentenhaftung § 823 I BGB mit Fehlertypologie (Konstruktion, Fabrikation, Instruktion, Produktbeobachtung) und BGH-Beweislastumkehr „Hühnerpest". Use when ein Verbraucher durch ein fehlerhaftes Produkt geschädigt wurde oder ein Hersteller die Haftungsexposition für einen Schadensfall einschätzen muss."
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

# /produktrecht:prodhaftg-herstellerhaftung

## Zweck

Der Skill prüft Ansprüche aus einem Produktschaden **parallel** auf beiden tragenden Anspruchsgrundlagen: verschuldensunabhängige Gefährdungshaftung des Herstellers nach § 1 ProdHaftG und deliktische Produzentenhaftung nach § 823 I BGB mit der von BGH „Hühnerpest" entwickelten Beweislastumkehr nach Risikosphären. Er ordnet das fehlerhafte Verhalten in die etablierte Fehlertypologie ein und adressiert Haftungsbeschränkungen, Mitverschulden und Verjährung.

## Eingaben

- Schadensbild (Personenschaden, Sachschaden privat / gewerblich, Vermögensschaden)
- Produkt (Bezeichnung, Charge, Inverkehrbringdatum, Zielnutzer)
- Hersteller / Importeur / Quasi-Hersteller (§ 4 ProdHaftG)
- mutmaßlicher Fehlertyp (Konstruktion, Fabrikation, Instruktion, Produktbeobachtung)
- Sachverhalt zur Kausalität (Schadenshergang, Beweislage)
- Position des Mandanten: Geschädigte / Hersteller / Versicherer

## Sub-Agent-Architektur

Researcher liefert ProdHaftG-Statute, § 823 BGB, BGH-Leitentscheidungen („Hühnerpest", „Honda", „Pflegebetten") sowie Kommentarstellen (Foerste/Graf von Westphalen, Kullmann, MüKoBGB Wagner). Drafter erstellt parallele Anspruchsprüfung in Gutachtenstil mit Fehlerzuordnung und Schadensbegründung. Reviewer prüft Fristen (§§ 12, 13 ProdHaftG, §§ 195, 199 BGB), Personenschadens-Blocker und Vollständigkeit der Beweislastdiskussion.

## Ablauf

### 1. Anspruch nach § 1 ProdHaftG

Tatbestand:

- **Produkt** iSv § 2 ProdHaftG (jede bewegliche Sache; Strom; nicht: unverarbeitete landwirtschaftliche Erzeugnisse a. F., heute generell erfasst)
- **Fehler** iSv § 3 ProdHaftG: „Sicherheit, die unter Berücksichtigung aller Umstände, insbesondere der Darbietung, des billigerweise zu erwartenden Gebrauchs und des Zeitpunkts des Inverkehrbringens, berechtigterweise erwartet werden kann"
- **Inverkehrbringen** durch Hersteller iSv § 4 ProdHaftG (Endhersteller, Teilhersteller, Quasi-Hersteller durch Markenanbringung, Importeur in den EWR)
- **Personenschaden** oder **privater Sachschaden** (§ 1 I ProdHaftG; gewerbliche Sachschäden ausgeschlossen)
- **Kausalität** Fehler → Schaden
- **Selbstbehalt** § 11: 500 EUR bei Sachschaden
- **Höchstbetrag** § 10: 85 Mio. EUR bei Personenschäden derselben Serie

Haftungsausschlüsse § 1 II ProdHaftG: Inverkehrbringen ohne wirtschaftlichen Zweck, Fehler erst nach Inverkehrbringen entstanden, Stand der Wissenschaft und Technik unerkennbar (Entwicklungsrisiko, § 1 II Nr. 5).

### 2. Anspruch nach § 823 I BGB (Produzentenhaftung)

Verletzung der Verkehrssicherungspflichten des Herstellers; Beweislastumkehr nach Risikosphären (BGH, Urt. v. 26.11.1968 – VI ZR 212/66, **BGHZ 51, 91 „Hühnerpest"** `[unverifiziert – prüfen in juris]`): Steht ein Produktfehler im Bereich der vom Hersteller beherrschbaren Risikosphäre fest, muss der Hersteller darlegen und beweisen, dass ihn kein Verschulden trifft.

Verkehrssicherungspflichten:

1. **Konstruktionspflicht** – fehlerfreie Konzeption der Baureihe nach dem maßgeblichen Stand der Wissenschaft und Technik im Inverkehrbringzeitpunkt
2. **Fabrikationspflicht** – Qualitätssicherung; Verantwortlichkeit auch für „Ausreißer"
3. **Instruktionspflicht** – Warn- und Gebrauchshinweise, abgestuft nach Adressatenkreis (Fachverkehr / Verbraucher / besonders schutzbedürftige Gruppen)
4. **Produktbeobachtungspflicht** – nach Inverkehrbringen Beobachtung des Produkts in der Praxis und Reaktion auf später erkannte Risiken (BGH, **„Pflegebetten"** – Urt. v. 16.12.2008 – VI ZR 170/07 `[unverifiziert – prüfen]`)

Vorteil gegenüber ProdHaftG: kein 500-EUR-Selbstbehalt, kein 85-Mio.-Höchstbetrag, Schmerzensgeld § 253 II BGB, Anspruchsverjährung erst 30 Jahre absolut (§ 199 II BGB bei Verletzung Leben/Körper/Gesundheit), Produktbeobachtungsfehler nur hier erfasst.

### 3. Fehlertypologie

| Typ | Anker | Beweisrichtung |
|---|---|---|
| **Konstruktionsfehler** | gesamte Baureihe; Stand W&T im Inverkehrbringzeitpunkt | Beweislastumkehr greift; Entwicklungsrisiko § 1 II Nr. 5 ProdHaftG als Einrede |
| **Fabrikationsfehler** | einzelner „Ausreißer"; Abweichung von Konstruktion | Beweislastumkehr greift; Hersteller haftet trotz organisatorisch optimaler Qualitätssicherung |
| **Instruktionsfehler** | unzureichende Warn-, Gebrauchs- oder Wartungshinweise | objektive Gefahr für den durchschnittlichen Nutzer; nicht: Selbstverständlichkeiten |
| **Produktbeobachtungsfehler** | nachträgliche Reaktionspflicht | nur § 823 BGB, **nicht** ProdHaftG; Reaktionsstufung (Warnung → Empfehlung → Rückruf) |

### 4. Mitverschulden und Schaden

- **Mitverschulden** § 6 ProdHaftG iVm § 254 BGB (Verbrauchserwartung; unsachgemäßer Gebrauch)
- **Schadensumfang**: § 7 ProdHaftG verweist auf §§ 249 ff. BGB; Schmerzensgeld nach § 253 II BGB seit Schuldrechtsmodernisierung 2002 (vorherige „PHG-Lücke" entfallen, § 8 ProdHaftG a. F.)
- **Gesamtschuld** § 5 ProdHaftG / § 840 BGB bei mehreren Herstellern

### 5. Fristen

- **§ 12 ProdHaftG**: Verjährung **3 Jahre** ab Kenntnis von Schaden, Fehler und Person des Ersatzpflichtigen
- **§ 13 ProdHaftG**: **Erlöschen** der Ansprüche **10 Jahre** ab Inverkehrbringen des konkreten Produkts (absolute Grenze)
- **§§ 195, 199 BGB** für Deliktsansprüche: 3 Jahre ab Jahresende der Kenntnis; Höchstfristen § 199 II BGB (30 Jahre bei Personenschaden), § 199 III BGB (10 Jahre ab Anspruchsentstehung bzw. 30 Jahre ab schädigender Handlung)

### 6. Versicherungsbezug

Bei Personenschaden: **Information des Produkthaftpflichtversicherers** prüfen (Obliegenheit aus dem Versicherungsvertrag; verspätete Anzeige kann Deckung gefährden).

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 1 ProdHaftG](https://www.gesetze-im-internet.de/prodhaftg/__1.html) (Haftung)
- [§ 2 ProdHaftG](https://www.gesetze-im-internet.de/prodhaftg/__2.html) (Produkt)
- [§ 3 ProdHaftG](https://www.gesetze-im-internet.de/prodhaftg/__3.html) (Fehler)
- [§ 4 ProdHaftG](https://www.gesetze-im-internet.de/prodhaftg/__4.html) (Hersteller)
- [§ 6 ProdHaftG](https://www.gesetze-im-internet.de/prodhaftg/__6.html) (Mitverschulden)
- [§ 10 ProdHaftG](https://www.gesetze-im-internet.de/prodhaftg/__10.html) (Höchstbetrag)
- [§ 11 ProdHaftG](https://www.gesetze-im-internet.de/prodhaftg/__11.html) (Selbstbeteiligung)
- [§ 12 ProdHaftG](https://www.gesetze-im-internet.de/prodhaftg/__12.html) (Verjährung)
- [§ 13 ProdHaftG](https://www.gesetze-im-internet.de/prodhaftg/__13.html) (Erlöschen)
- [§ 15 ProdHaftG](https://www.gesetze-im-internet.de/prodhaftg/__15.html) (andere Haftung; Anspruchskonkurrenz)
- [§ 823 BGB](https://www.gesetze-im-internet.de/bgb/__823.html) (Schadensersatzpflicht)
- [§ 253 BGB](https://www.gesetze-im-internet.de/bgb/__253.html) (Schmerzensgeld)
- [§ 254 BGB](https://www.gesetze-im-internet.de/bgb/__254.html) (Mitverschulden)
- [§§ 195, 199 BGB](https://www.gesetze-im-internet.de/bgb/__199.html) (Verjährung)
- [RL 85/374/EWG](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:31985L0374) (Produkthaftungs-RL, Grundlage des ProdHaftG)

### Kommentare

- Foerste, in: Foerste/Graf von Westphalen, Produkthaftungshandbuch, 4. Aufl. 2024, § 24 Rn. 1 ff. (Fehlerbegriff) `[unverifiziert – Aufl./Jahr prüfen]`
- Kullmann, ProdHaftG, 7. Aufl. 2018, § 3 Rn. 1 ff. `[unverifiziert – Aufl. prüfen]`
- Wagner, in: MüKoBGB, 9. Aufl. 2024, § 823 Rn. 800 ff. (Produzentenhaftung)
- Spindler, in: BeckOK BGB, Stand 2024, § 823 Rn. 500 ff. (Produktrisiken)
- Grüneberg/Sprau, in: Palandt/Grüneberg, BGB, 83. Aufl. 2024, § 823 Rn. 167 ff. `[unverifiziert – Aufl. prüfen]`

### Rechtsprechung (`[unverifiziert – prüfen in juris/Beck-Online]`)

1. BGH, Urt. v. 26.11.1968 – VI ZR 212/66, BGHZ 51, 91 („Hühnerpest", Beweislastumkehr nach Risikosphären)
2. BGH, Urt. v. 17.03.1981 – VI ZR 191/79, BGHZ 80, 186 („Honda", Konstruktionsfehler)
3. BGH, Urt. v. 16.12.2008 – VI ZR 170/07, NJW 2009, 1080 („Pflegebetten", Produktbeobachtung und Reaktionsstufung)
4. BGH, Urt. v. 09.05.1995 – VI ZR 158/94, BGHZ 129, 353 (Instruktionspflicht bei Verbraucherprodukten)
5. EuGH, Urt. v. 05.03.2015 – C-503/13, C-504/13, ECLI:EU:C:2015:148 (Boston Scientific, Fehlerbegriff bei Medizinprodukten potenziellen Defekts)

## Ausgabeformat

```
GUTACHTEN — Herstellerhaftung Produktschaden
Mandat: <Geschädigte / Hersteller / Versicherer>
Produkt: <Bezeichnung, Charge, Inverkehrbringdatum>

I. Sachverhalt (knapp)
II. Frage(n)
III. Kurzantwort
     – ProdHaftG: [Anspruch (+/-) / Höhe]
     – § 823 BGB: [Anspruch (+/-) / Höhe + Schmerzensgeld]

IV. Rechtliche Bewertung
    1. Anspruch aus § 1 ProdHaftG
       a) Produkt (§ 2)
       b) Fehler (§ 3) — Fehlertyp:
          ☐ Konstruktion ☐ Fabrikation ☐ Instruktion
       c) Inverkehrbringen durch Hersteller (§ 4)
       d) Schaden und Kausalität
       e) Haftungsbeschränkungen
          – Selbstbehalt § 11 (500 EUR Sachschaden)
          – Höchstbetrag § 10 (85 Mio. EUR Serie)
       f) Mitverschulden § 6 iVm § 254 BGB
    2. Anspruch aus § 823 I BGB (Produzentenhaftung)
       a) Verkehrssicherungspflichten und Pflichtverletzung
          ☐ Konstruktion ☐ Fabrikation ☐ Instruktion ☐ Produktbeobachtung
       b) Beweislastumkehr nach BGH „Hühnerpest"
       c) Schaden inkl. Schmerzensgeld § 253 II BGB
    3. Anspruchskonkurrenz § 15 II ProdHaftG
    4. Fristen
       – § 12 ProdHaftG (3 J ab Kenntnis)
       – § 13 ProdHaftG (10 J Erlöschen ab Inverkehrbringen)
       – §§ 195, 199 BGB (Delikt)

V. Risiken / offene Punkte
    🟢 / 🟡 / 🔴 <Einstufung mit Begründung>
    – Tatsachen offen: <…>
    – Versicherer-Information: <…>

VI. Quellenverzeichnis
```

## Risiken / typische Fehler

- **Anspruchsgrundlagen nur alternativ geprüft.** ProdHaftG und § 823 BGB stehen nebeneinander (§ 15 II ProdHaftG); Verzicht auf § 823 BGB nimmt der Geschädigten Schmerzensgeld und unbegrenzte Haftungssumme.
- **Fehlertyp nicht benannt.** Die Beweisrichtung und der Entwicklungsrisiko-Einwand § 1 II Nr. 5 ProdHaftG hängen vom Fehlertyp ab.
- **Produktbeobachtungspflicht in ProdHaftG verortet.** Sie ist nur § 823 BGB.
- **§ 12 / § 13 ProdHaftG verwechselt.** § 12 ist Verjährung (3 J ab Kenntnis); § 13 ist absolute Erlöschens-Frist (10 J ab Inverkehrbringen) — unabhängig von Kenntnis.
- **Quasi-Hersteller** (§ 4 I 2 ProdHaftG, Markenanbringung) und **Importeur** (§ 4 II ProdHaftG, Einfuhr in den EWR) übersehen — relevant, wenn der Endhersteller außerhalb des EWR sitzt.
- **Schmerzensgeld nur über § 8 ProdHaftG a. F. argumentiert.** Seit 2002 läuft Schmerzensgeld primär über § 253 II BGB.
- **Versicherer-Information vergessen** — Deckungsrisiko aus Produkthaftpflichtversicherung.
