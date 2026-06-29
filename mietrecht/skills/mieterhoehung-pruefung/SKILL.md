---
name: mieterhoehung-pruefung
description: "Wirksamkeitsprüfung eines empfangenen Mieterhöhungsverlangens auf die ortsübliche Vergleichsmiete – Formprüfung § 558a BGB, 15-Monats-Frist und Kappungsgrenze § 558 Abs. 3 BGB, Begründungsmittel, Abgrenzung zur Modernisierungsmieterhöhung § 559 BGB, Zustimmungsklage § 558b BGB. Use when ein Mieter ein erhaltenes Mieterhöhungsverlangen oder ein Vermieter den eigenen Entwurf auf Wirksamkeit prüft."
language: de
provider_variants:
  - claude
  - gemini
  - openai
test: ./test.md
---

# /mietrecht:mieterhoehung-pruefung

## Zweck

Diese Skill prüft ein **bereits empfangenes** Mieterhöhungsverlangen auf die ortsübliche Vergleichsmiete auf Wirksamkeit — das prüf- und reviewseitige Gegenstück zur gestaltenden Skill `mieterhoehung-558-bgb`. Adressat ist primär der Mieter, der prüft, ob er zustimmen muss; sekundär der Vermieter, der seinen eigenen Entwurf vor Versand kontrolliert.

Ein Mieterhöhungsverlangen löst nur dann eine Zustimmungspflicht aus, wenn es **formwirksam** ist und die materiellen Grenzen wahrt. Ein formfehlerhaftes Verlangen ist unwirksam — der Mieter schuldet keine Zustimmung, und die Überlegungsfrist beginnt nicht zu laufen. Daher steht die Formprüfung am Anfang.

## Eingaben

- Das empfangene **Verlangen** (Wortlaut, Datum des Zugangs, Form: Brief/E-Mail/Textform)
- **Aktuelle Nettokaltmiete** (Ausgangswert für Kappungsgrenze)
- Datum der **letzten Erhöhung** bzw. des Einzugs (für 15-Monats-Frist und Jahressperre)
- **Begründungsmittel**, auf das sich das Verlangen stützt (Mietspiegel, Sachverständigengutachten, drei Vergleichswohnungen, Mietdatenbank)
- **Mietspiegel** der Gemeinde, falls vorhanden (zur Plausibilisierung der geforderten Miete)

## Sub-Agent-Architektur

Die Prüfung läuft in zwei voneinander getrennten Schritten, um die häufigste Fehlerquelle — Vermengung von Form- und Begründetheitsfrage — zu vermeiden. Ein **Form-Prüfer** beurteilt zuerst nur die Wirksamkeit des Verlangens (Textform, Begründungsmittel, Fristen) ohne Blick auf die Höhe. Erst wenn das Verlangen formwirksam ist, bewertet ein **Materiell-Prüfer** die geforderte Miete an ortsüblicher Vergleichsmiete und Kappungsgrenze. Ein **Abgrenzungs-Prüfer** kontrolliert quer, ob das Verlangen in Wahrheit eine Modernisierungsmieterhöhung (§ 559 BGB) ist, die anderen Regeln folgt. Die Architektur ist als Prosa beschrieben; es gibt bewusst keinen `agents`-Block (mietrecht-Konvention).

## Ablauf

### 1. Formprüfung ([§ 558a BGB](https://www.gesetze-im-internet.de/bgb/__558a.html))

Das Mieterhöhungsverlangen ist nach **§ 558a Abs. 1 BGB** in **Textform** zu erklären und zu **begründen**. Die Formprüfung umfasst:

- **Textform** (§ 126b BGB): lesbare Erklärung, Person des Erklärenden genannt. E-Mail genügt; ein bloßer mündlicher Hinweis nicht.
- **Adressierung an alle Mieter**: Bei mehreren Mietern muss das Verlangen von allen Vermietern an alle Mieter gerichtet sein. Ein Verlangen an nur einen von mehreren Mietern ist unwirksam.
- **Begründung mit zulässigem Begründungsmittel**: Das Verlangen muss eines der vier gesetzlichen Begründungsmittel benennen und so konkret bezeichnen, dass der Mieter die geforderte Erhöhung nachprüfen kann.

**Begründungsmittel** (§ 558a Abs. 2 BGB) — eines genügt, muss aber bestimmt sein:

1. **Mietspiegel** der Gemeinde (einfach oder qualifiziert, § 558d BGB). Bei Bezugnahme müssen die einschlägigen Felder/Spannen benannt sein; ein pauschaler Verweis auf „den Mietspiegel" ohne konkrete Einordnung der Wohnung ist unzureichend.
2. **Sachverständigengutachten** eines öffentlich bestellten oder anerkannt qualifizierten Sachverständigen.
3. **Drei Vergleichswohnungen** mit Lage, Größe, Ausstattung und konkreter Vergleichsmiete — so bestimmt, dass sie auffindbar sind.
4. **Mietdatenbank** (§ 558e BGB).

> Fehlt eine zulässige Begründung oder ist sie zu unbestimmt, ist das Verlangen **unwirksam** — die Zustimmungspflicht entsteht nicht.

### 2. Fristen — 15-Monats-Frist und Klagefrist

**15-Monats-Frist / Jahressperre** ([§ 558 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__558.html)): Die erhöhte Miete kann frühestens **15 Monate nach Einzug oder der letzten Mieterhöhung** verlangt werden (Wirksamkeit der Erhöhung). Das Verlangen selbst darf frühestens **12 Monate** nach der letzten Erhöhung zugehen (Jahressperrfrist). Liegt die letzte Erhöhung weniger als ein Jahr zurück, ist das Verlangen verfrüht und unwirksam.

**Überlegungs- und Klagefrist** ([§ 558b BGB](https://www.gesetze-im-internet.de/bgb/__558b.html)): Der Mieter hat bis zum **Ablauf des zweiten Kalendermonats nach Zugang** Zeit, der Erhöhung zuzustimmen (Überlegungsfrist). Stimmt er zu, schuldet er die erhöhte Miete **ab Beginn des dritten Kalendermonats** nach Zugang des Verlangens. Verweigert oder schweigt der Mieter, kann der Vermieter **innerhalb von drei weiteren Monaten** auf Zustimmung klagen (siehe Schritt 6).

### 3. Ortsübliche Vergleichsmiete ermitteln

Die geforderte Miete darf die **ortsübliche Vergleichsmiete** nicht überschreiten (§ 558 Abs. 1, Abs. 2 BGB). Maßgeblich sind die Mieten für nicht preisgebundenen Wohnraum vergleichbarer Art, Größe, Ausstattung, Beschaffenheit und Lage einschließlich energetischer Ausstattung, die in den letzten sechs Jahren vereinbart oder geändert wurden. Praktisch wird die geforderte Miete gegen den einschlägigen Mietspiegelwert (richtige Felder, gültige Fassung — Aktualität § 558d Abs. 2 BGB) plausibilisiert. Liegt die Forderung oberhalb der Spanne, ist sie der Höhe nach unbegründet, soweit sie die ortsübliche Vergleichsmiete übersteigt.

### 4. Kappungsgrenze ([§ 558 Abs. 3 BGB](https://www.gesetze-im-internet.de/bgb/__558.html))

Unabhängig von der ortsüblichen Vergleichsmiete darf die Miete **innerhalb von drei Jahren um höchstens 20 %** steigen. In Gebieten mit gefährdeter Wohnungsversorgung gilt per landesrechtlicher Verordnung eine abgesenkte Kappungsgrenze von **15 %**. Berechnung: Ausgangswert ist die Miete vor drei Jahren; zwischenzeitliche Erhöhungen werden kumuliert angerechnet. Übersteigt die Forderung die Kappungsgrenze, ist sie nur **bis zur Grenze** wirksam; der überschießende Teil entfällt.

### 5. Abgrenzung zur Modernisierungsmieterhöhung ([§ 559 BGB](https://www.gesetze-im-internet.de/bgb/__559.html))

Eine Erhöhung nach **§ 559 BGB** (Modernisierungsmieterhöhung) folgt einem **anderen Regime**: Sie stützt sich auf durchgeführte Modernisierungsmaßnahmen, erfordert keine Zustimmung des Mieters (einseitige Erklärung), kennt eine eigene Kappung und ist nicht an die ortsübliche Vergleichsmiete gebunden. Prüfe, ob das empfangene Schreiben tatsächlich ein Verlangen nach § 558 BGB ist oder verdeckt eine Modernisierungsmieterhöhung. Eine Vermischung beider Wege im selben Schreiben oder das Anrechnen modernisierungsbedingter Beträge in einem § 558-Verlangen ist fehlerhaft und gesondert zu rügen.

### 6. Zustimmung und Zustimmungsklage ([§ 558b BGB](https://www.gesetze-im-internet.de/bgb/__558b.html))

Ist das Verlangen formwirksam und der Höhe nach begründet, schuldet der Mieter **Zustimmung** (nicht Zahlung kraft Gesetzes). Stimmt er nicht fristgerecht zu, ist der Vermieter auf die **Zustimmungsklage** verwiesen, die er innerhalb der Frist des § 558b Abs. 2 BGB erheben muss. Ist das Verlangen nur **teilweise** begründet (z. B. wegen Kappungsgrenze), sollte der Mieter in Höhe des wirksamen Teils zustimmen, um insoweit eine Klage zu vermeiden.

### 7. Zulässiger Erhöhungsbetrag

Abschließend wird der **tatsächlich zulässige Erhöhungsbetrag** bestimmt: das **Minimum** aus (a) ortsüblicher Vergleichsmiete und (b) Ausgangsmiete zuzüglich Kappungsgrenze. Die Forderung wird gegen diesen Wert gespiegelt; die Differenz ist der unbegründete Teil.

## Risiken / typische Fehler

- **Form vor Höhe verwechselt** — ein formunwirksames Verlangen ist insgesamt unwirksam; die Höhe ist dann gar nicht zu prüfen.
- **15-Monats-Frist / Jahressperre übersehen** — verfrühtes Verlangen unwirksam, neue Wartezeit.
- **Begründungsmittel zu unbestimmt** — pauschaler Verweis auf „den Mietspiegel" ohne Einordnung der Wohnung genügt nicht.
- **Kappungsgrenze falsch berechnet** — Drei-Jahres-Zeitraum oder kumulierte Vorerhöhungen falsch angesetzt; abgesenkte 15-%-Grenze übersehen.
- **Modernisierung als Vergleichsmieterhöhung getarnt** — § 559 BGB folgt eigenen Regeln; Vermischung rügen.
- **Teilzustimmung verpasst** — bei nur teilweiser Begründetheit Zustimmung in wirksamer Höhe versäumt, dadurch unnötiges Klagerisiko.

## Quellen

### Statute

- [§ 558 BGB](https://www.gesetze-im-internet.de/bgb/__558.html), [§ 558a BGB](https://www.gesetze-im-internet.de/bgb/__558a.html), [§ 558b BGB](https://www.gesetze-im-internet.de/bgb/__558b.html), [§ 558d BGB](https://www.gesetze-im-internet.de/bgb/__558d.html), [§ 558e BGB](https://www.gesetze-im-internet.de/bgb/__558e.html)
- [§ 559 BGB](https://www.gesetze-im-internet.de/bgb/__559.html) (Modernisierungsmieterhöhung)
- [§ 126b BGB](https://www.gesetze-im-internet.de/bgb/__126b.html) (Textform)

### Kommentare

- Börstinghaus, in: Schmidt-Futterer, Mietrecht, 15. Aufl. 2023, § 558a BGB Rn. 1 ff.
- Artz, in: MüKoBGB, 9. Aufl. 2023, § 558a Rn. 1 ff.

### Rechtsprechung

- Zur Begründungstiefe und Bestimmtheit des Verlangens ist die einschlägige BGH-Rechtsprechung heranzuziehen `[unverifiziert - prüfen]`. Kein Aktenzeichen ohne eigene Verifikation übernehmen.

## Ausgabeformat

```
MIETERHÖHUNGSVERLANGEN — Wirksamkeitsprüfung — <Mandat-ID> — <Datum>

I.   Formprüfung (§ 558a)            [✅ / ❌]
     - Textform                      [✅ / ❌]
     - Adressierung alle Mieter      [✅ / ❌]
     - Begründungsmittel benannt     [Mietspiegel / Gutachten / 3 Wohnungen / Datenbank]
       Bestimmtheit                  [✅ / ⚠️]
II.  Fristen
     - 15-Monats-Frist / Jahressperre [✅ / ❌]
     - Überlegungsfrist Ende         <Datum>
     - Klagefrist Vermieter Ende     <Datum>
III. Ortsübliche Vergleichsmiete     Mietspiegelwert: <Wert>
                                     Forderung: <Wert>   [innerhalb / darüber]
IV.  Kappungsgrenze (§ 558 Abs. 3)   Ausgang + max <20 % / 15 %> = <Wert>
                                     Forderung: <Wert>   [✅ / überschießend <Differenz>]
V.   Abgrenzung § 559 (Modernisierung) [N/A / Verdacht — gesondert prüfen]
VI.  Zulässiger Erhöhungsbetrag      <Min(Vergleichsmiete, Kappungsgrenze)>
     Empfehlung Zustimmung           [voll / teilweise <Wert> / verweigern]

Ergebnis: <Verlangen wirksam / teilweise / unwirksam>
Risiko Zustimmungsklage: [🟢 / 🟡 / 🔴]
```
