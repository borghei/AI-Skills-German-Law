---
name: mieterhoehung-558-bgb
description: "Mieterhöhung auf die ortsübliche Vergleichsmiete nach § 558 BGB – Wartezeit (Abs. 1), Kappungsgrenze (Abs. 3), Begründungsmittel (§ 558a BGB: Mietspiegel, Sachverständigengutachten, Vergleichswohnungen, Mietdatenbank), Zustimmungsklage. Use when ein Vermieter eine Mieterhöhung gestaltet oder ein Mieter ein Mieterhöhungsverlangen auf Wirksamkeit prüft."
language: de
provider_variants:
  - claude
  - gemini
  - openai
test: ./test.md
---

# /mietrecht:mieterhoehung-558-bgb

## Zweck

Mieterhöhungen nach § 558 BGB sind formstreng. Ein Vermieter, der die Begründungsanforderungen von § 558a BGB verfehlt, hat sechs Monate vergeudet — Zustimmungspflicht der Miete entsteht erst mit korrektem Verlangen.

## Eingaben

- Aktuelle Nettokaltmiete und letzte Mieterhöhung (Datum)
- Wohnungsfläche, Wohnlage, Baujahr, Ausstattungsmerkmale (für Vergleichsmiete)
- Begründungsmittel: Mietspiegel der Gemeinde / Sachverständigengutachten / 3 Vergleichswohnungen / Mietdatenbank
- Mietpreisbremse anwendbar? ([§ 556d BGB](https://www.gesetze-im-internet.de/bgb/__556d.html); landesrechtliche VO)

## Ablauf

### 1. Wartezeit ([§ 558 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__558.html))

Mieterhöhung erst zulässig, wenn die aktuelle Miete **seit 15 Monaten unverändert** ist. Verlangen frühestens 12 Monate nach letzter Erhöhung; Wirksamkeit nach 3-monatiger Überlegungsfrist (§ 558b Abs. 1 BGB).

### 2. Ortsübliche Vergleichsmiete (§ 558 Abs. 2 BGB)

Definition: Mieten, die in der Gemeinde / vergleichbarem Gebiet für nicht preisgebundenen Wohnraum vergleichbarer Art, Größe, Ausstattung, Beschaffenheit und Lage einschließlich energetischer Ausstattung und Beschaffenheit in den letzten **sechs** Jahren vereinbart oder geändert wurden.

### 3. Kappungsgrenze ([§ 558 Abs. 3 BGB](https://www.gesetze-im-internet.de/bgb/__558.html))

Maximale Erhöhung **20 %** innerhalb von 3 Jahren. In Gebieten mit gefährdeter Wohnungsversorgung per landesrechtlicher VO: **15 %**. Kumulierte Erhöhungen werden berücksichtigt.

### 4. Begründungsmittel ([§ 558a BGB](https://www.gesetze-im-internet.de/bgb/__558a.html))

Zur Wahl stehen vier Mittel — eines genügt:

1. **Mietspiegel** der Gemeinde — qualifiziert (§ 558d BGB) oder einfach. Bei qualifiziertem Mietspiegel: Vermutung der ortsüblichen Vergleichsmiete (§ 558d Abs. 3 BGB).
2. **Sachverständigengutachten** — öffentlich bestellter oder anerkannt qualifizierter Sachverständiger.
3. **Drei Vergleichswohnungen** — Lage, Größe, Ausstattung benennen, Vergleichsmieten angeben.
4. **Mietdatenbank** (§ 558e BGB).

### 5. Form des Verlangens (§ 558a Abs. 1 BGB)

- Schriftform (Textform genügt seit 2013)
- Adressiert an alle Mieter
- Klare Bezeichnung der erhöhten Miete + Differenz
- Verweis auf Begründungsmittel

### 6. Zustimmungsfrist und -klage ([§ 558b BGB](https://www.gesetze-im-internet.de/bgb/__558b.html))

Mieter hat bis Ablauf des **zweiten Kalendermonats nach Zugang** Zeit zur Zustimmung. Verweigert er, kann Vermieter **innerhalb von drei Monaten** nach Ablauf der Frist auf Zustimmung klagen.

### 7. Mietpreisbremse-Interaktion

In Gebieten der Mietpreisbremse ([§ 556d BGB](https://www.gesetze-im-internet.de/bgb/__556d.html)) gilt § 558 grundsätzlich weiter — die Kappungsgrenze + Begrenzung auf ortsübliche Vergleichsmiete + 10 % bei Wiedervermietung sind aber zu beachten.

## Quellen

### Statute

- [§ 558 BGB](https://www.gesetze-im-internet.de/bgb/__558.html), [§ 558a BGB](https://www.gesetze-im-internet.de/bgb/__558a.html), [§ 558b BGB](https://www.gesetze-im-internet.de/bgb/__558b.html), [§ 558c BGB](https://www.gesetze-im-internet.de/bgb/__558c.html), [§ 558d BGB](https://www.gesetze-im-internet.de/bgb/__558d.html), [§ 558e BGB](https://www.gesetze-im-internet.de/bgb/__558e.html)
- [§ 556d BGB](https://www.gesetze-im-internet.de/bgb/__556d.html) (Mietpreisbremse)

### Kommentare

- Börstinghaus, in: Schmidt-Futterer, Mietrecht, 15. Aufl. 2023, § 558 BGB Rn. 1 ff.
- Artz, in: MüKoBGB, 9. Aufl. 2023, § 558 Rn. 1 ff.
- Eisenschmid, in: Schmidt-Futterer, § 558a Rn. 1 ff.

### Rechtsprechung

- BGH, Urt. v. 28.01.2004 – VIII ZR 124/02, NJW 2004, 1452 (Begründungstiefe Vergleichswohnungen) `[unverifiziert – prüfen]`
- BGH, Urt. v. 18.11.2020 – VIII ZR 123/20, NJW 2021, 1226 (Mietspiegelvermutung) `[unverifiziert – prüfen]`

## Ausgabeformat

```
MIETERHÖHUNGSVERLANGEN — Prüfung — <Mandat-ID> — <Datum>

I.   Wartezeit (§ 558 Abs. 1)        [✅ / ❌]
II.  Kappungsgrenze (§ 558 Abs. 3)   Aktuelle Miete + Erhöhung = <Wert>
                                     Max. zulässig: <Wert (20 % oder 15 %)>
III. Begründungsmittel               [Mietspiegel / Sachverständige / 3 Vergleichswohnungen / Datenbank]
     Plausibilität:                  [✅ / ⚠️]
IV.  Form (§ 558a)                   [✅ / ⚠️]
V.   Zustimmungsfrist                Ende: <Datum>
VI.  Mietpreisbremse-Check           [N/A / anwendbar]

Empfehlung: <…>
Risiko Zustimmungsklage: [🟢 / 🟡 / 🔴]
```

## Risiken / typische Fehler

- **Wartezeit übersehen** → Verlangen unwirksam, neue 15 Monate Verzögerung.
- **Kappungsgrenze rechnerisch falsch** (kumulative Erhöhungen vergessen) → Verlangen teilweise unwirksam, Restbetrag verfällt nicht, kann erneut verlangt werden.
- **Mietspiegel nicht aktuell** (Zwei-Jahres-Aktualität § 558d Abs. 2 BGB) → keine Vermutungswirkung.
- **Vergleichswohnungen unbestimmt** (keine Adresse / Eckdaten) → unwirksam.
- **Verlangen an nur einen von mehreren Mietern** → unwirksam.
- **Mietpreisbremse als Mieter geltend gemacht?** — Vermieter muss bei Zugang Auskunft erteilen (§ 556g Abs. 1a BGB).
