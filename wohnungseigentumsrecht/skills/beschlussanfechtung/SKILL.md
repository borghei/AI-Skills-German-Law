---
name: beschlussanfechtung
description: "Prüfung der Erfolgsaussicht einer WEG-Beschlussanfechtung nach der WEMoG-Reform – Anfechtungs- und Nichtigkeitsklage § 44 Abs. 1 WEG gegen die Gemeinschaft der Wohnungseigentümer § 44 Abs. 2 WEG, Klage- und Begründungsfrist § 45 S. 1 WEG mit Wiedereinsetzung § 45 S. 2 WEG, Zustellung demnächst, Nichtigkeit und Anfechtbarkeit § 23 Abs. 4 WEG, Einberufung und Ankündigung §§ 23 Abs. 2, 24 Abs. 4 WEG, ordnungsmäßige Verwaltung §§ 18 Abs. 2, 19 WEG, Teilanfechtung, Zuständigkeit § 43 Abs. 2 WEG, Streitwert § 49 GKG, Kostenlast des obsiegenden Klägers. Rechtsstand: Oktober 2026. Use when ein Wohnungseigentümer einen Beschluss der Eigentümerversammlung anfechten will oder die Erfolgsaussicht einer Anfechtungsklage geprüft werden soll."
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

# /wohnungseigentumsrecht:beschlussanfechtung

## Zweck

Dieser Skill prüft die **Erfolgsaussicht** einer Beschlussanfechtung nach dem Wohnungseigentumsmodernisierungsgesetz (**WEMoG**, in Kraft seit 01.12.2020). Die Reform hat das Beschlussklagerecht grundlegend umgestaltet: Beschlussklagen sind nach [§ 44 Abs. 2 WEG](https://www.gesetze-im-internet.de/woeigg/__44.html) **gegen die Gemeinschaft der Wohnungseigentümer** zu richten — nicht mehr gegen die übrigen Eigentümer. Geprüft werden Klageart, Fristen, Nichtigkeit und Anfechtbarkeit, formelle und materielle Fehler sowie das Kostenrisiko.

**Rechtsstand: Oktober 2026.** §§ 43–45 WEG sind seit dem WEMoG unverändert. Neu seit 17.10.2024 ist die **virtuelle Eigentümerversammlung** ([§ 23 Abs. 1a WEG](https://www.gesetze-im-internet.de/woeigg/__23.html)), deren Einberufung und Durchführung eigene Anfechtungsgründe erzeugen kann. Die Rechtsprechung des V. Zivilsenats hat 2024–2026 Zustellung, Kostenlast und Teilanfechtung geklärt.

## Eingaben

- der angefochtene **Beschluss** (Wortlaut, Beschlussart, Verkündung)
- das **Versammlungsprotokoll** (Beschlussfassung, Stimmverhältnis, Teilnehmer, Vollmachten)
- die **Einladung** (Datum, Form, Tagesordnung, Versammlungsart: Präsenz / hybrid / virtuell)
- das **Beschlussdatum** (für die Fristberechnung)
- Gemeinschaftsordnung (Öffnungsklauseln, Stimmrecht), frühere Beschlüsse
- Interesse des Klägers und Verkehrswert seiner Einheit (Streitwert)

## Sub-Agent-Architektur

- **Researcher** (`../../agents/researcher.md`) liefert die WEG-Normen in der **post-WEMoG-Fassung** und die verifizierte Rechtsprechung des V. Zivilsenats.
- **Drafter** (`../../agents/drafter.md`) erstellt das Prüfungsergebnis und — bei Erfolgsaussicht — den Entwurf der Anfechtungsklage gegen die GdWE.
- **Reviewer** (`../../agents/reviewer.md`) kontrolliert Fristwahrung, richtigen Beklagten, Trennung von Nichtigkeit und Anfechtbarkeit sowie das Kostenrisiko.

## Ablauf

### 1. Beschluss und Klageart erfassen

Wortlaut und Gegenstand festhalten, Beschlussart bestimmen (Sonderumlage, Nachschüsse, Verwalterbestellung, bauliche Maßnahme, Kostenverteilung). [§ 44 Abs. 1 WEG](https://www.gesetze-im-internet.de/woeigg/__44.html) kennt drei Beschlussklagen:

| Klage | Ziel |
|---|---|
| **Anfechtungsklage** | Ungültigerklärung eines anfechtbaren Beschlusses |
| **Nichtigkeitsklage** | Feststellung der Nichtigkeit |
| **Beschlussersetzungsklage** | Gericht fasst einen unterbliebenen notwendigen Beschluss (`/wohnungseigentumsrecht:beschlussersetzungsklage`) |

Anfechtungs- und Nichtigkeitsklage haben denselben Streitgegenstand; der Antrag sollte die Nichtigkeitsfeststellung hilfsweise einschließen.

### 2. Nichtigkeit oder Anfechtbarkeit (§ 23 Abs. 4 WEG)

Erste Weichenstellung nach [§ 23 Abs. 4 WEG](https://www.gesetze-im-internet.de/woeigg/__23.html):

| Kategorie | Voraussetzung | Folge |
|---|---|---|
| **Nichtigkeit** | Verstoß gegen eine Rechtsvorschrift, auf deren Einhaltung nicht verzichtet werden kann (Satz 1) — insbesondere **fehlende Beschlusskompetenz** | von Anfang an unwirksam — **fristunabhängig** geltend zu machen |
| **Anfechtbarkeit** | jeder sonstige Rechtsverstoß (Satz 2) | wirksam, bis er auf fristgerechte Klage rechtskräftig für ungültig erklärt ist |

Ein nur **anfechtbarer** Beschluss erwächst nach Fristablauf in Bestandskraft.

### 3. Fristen (§ 45 WEG)

[§ 45 WEG](https://www.gesetze-im-internet.de/woeigg/__45.html) enthält **zwei materielle Ausschlussfristen**:

- **Klagefrist:** Erhebung **binnen eines Monats** nach Beschlussfassung.
- **Begründungsfrist:** Begründung **binnen zweier Monate** nach Beschlussfassung.
- **Fristbeginn** ist die Beschlussfassung (Verkündung), nicht der Zugang des Protokolls; bei Umlaufbeschlüssen die Mitteilung des Beschlussergebnisses.
- **Wiedereinsetzung** bei unverschuldeter Versäumung: §§ 233–238 ZPO gelten entsprechend (§ 45 S. 2 WEG).
- **Zustellung demnächst** (§ 167 ZPO): Verzögert sich die Zustellung der rechtzeitig eingereichten Klage, muss sich der Kläger spätestens binnen eines Jahres nach Ablauf der Anfechtungsfrist beim Gericht nach dem Sachstand erkundigen; sonst ist die Zustellung nicht mehr „demnächst" (BGH, Urt. v. 24.10.2024 – V ZR 17/24 `[unverifiziert – prüfen: Datum in den Quellen uneinheitlich (24./25.10.2024)]`). Gerichtskostenvorschuss sofort zahlen.

Fristberechnung (Beispiel: Beschluss am 14.09.2026):

```bash
python -m scripts.legal_calc.cli frist --ereignis 14.09.2026 --menge 1 --einheit monate
python -m scripts.legal_calc.cli frist --ereignis 14.09.2026 --menge 2 --einheit monate
```

### 4. Beklagte, Zuständigkeit, Streitwert

- **Beklagte:** die **Gemeinschaft der Wohnungseigentümer** ([§ 44 Abs. 2 S. 1 WEG](https://www.gesetze-im-internet.de/woeigg/__44.html)), vertreten durch den Verwalter ([§ 9b Abs. 1 WEG](https://www.gesetze-im-internet.de/woeigg/__9b.html)). Das gilt auch, wenn der angefochtene Beschluss den Verwalter selbst betrifft; § 9b Abs. 2 WEG regelt nur die Vertretung **gegenüber dem Verwalter**, nicht im Beschlussprozess. Fehlt ein Verwalter, vertreten alle Eigentümer die GdWE gemeinschaftlich (§ 9b Abs. 1 S. 2 WEG). Eine Klage gegen die übrigen Eigentümer ist gegen den falschen Beklagten gerichtet.
- **Zuständigkeit:** ausschließlich das Amtsgericht der belegenen Sache, unabhängig vom Streitwert ([§ 43 Abs. 2 Nr. 4 WEG](https://www.gesetze-im-internet.de/woeigg/__43.html); § 23 Nr. 2 Buchst. c GVG). Berufung zum Landgericht am Sitz des Oberlandesgerichts ([§ 72 Abs. 2 GVG](https://www.gesetze-im-internet.de/gvg/__72.html)).
- **Urteilswirkung** für und gegen alle Eigentümer ([§ 44 Abs. 3 WEG](https://www.gesetze-im-internet.de/woeigg/__44.html)); der Verwalter macht die Klage bekannt (§ 44 Abs. 2 S. 2 WEG). Kosten einer Nebenintervention sind nur erstattungsfähig, wenn sie geboten war (§ 44 Abs. 4 WEG).
- **Streitwert:** Interesse aller Eigentümer, höchstens das 7,5-fache Interesse des Klägers und der Verkehrswert seines Wohnungseigentums ([§ 49 GKG](https://www.gesetze-im-internet.de/gkg_2004/__49.html)).

### 5. Formelle Anfechtungsgründe

- **Einberufung** in **Textform**, Frist mindestens **drei Wochen** (Soll-Vorschrift, außer bei besonderer Dringlichkeit), durch den Verwalter oder hilfsweise die in [§ 24 Abs. 3 WEG](https://www.gesetze-im-internet.de/woeigg/__24.html) Genannten ([§ 24 Abs. 4 WEG](https://www.gesetze-im-internet.de/woeigg/__24.html)).
- **Ankündigung:** Ein Beschluss ist nur gültig, wenn der **Gegenstand bei der Einberufung bezeichnet** war ([§ 23 Abs. 2 WEG](https://www.gesetze-im-internet.de/woeigg/__23.html)). Ein nicht angekündigter Tagesordnungspunkt führt regelmäßig zur **Anfechtbarkeit**.
- **Kausalität:** Formelle Fehler führen nur dann zur Ungültigerklärung, wenn nicht feststeht, dass der Beschluss bei ordnungsgemäßem Vorgehen ebenso gefasst worden wäre `[unverifiziert – prüfen: Kausalitätsrechtsprechung post-WEMoG im Volltext]`. Bei Einberufungsfehlern, die Eigentümer von der Teilnahme abhalten, ist die Kausalität regelmäßig nicht auszuschließen.
- **Stimmrecht:** Kopfprinzip, einheitliche Stimmabgabe bei Mitberechtigten, Vollmachten in Textform, Stimmverbote ([§ 25 WEG](https://www.gesetze-im-internet.de/woeigg/__25.html)).
- **Virtuelle / hybride Versammlung:** Grundlage nach § 23 Abs. 1 S. 2 oder Abs. 1a WEG vorhanden? Vergleichbarkeit der Teilnahme und Rechteausübung gewahrt? Dazu `/wohnungseigentumsrecht:eigentuemerversammlung-beschlussfassung`.

### 6. Materielle Prüfung — ordnungsmäßige Verwaltung (§§ 18, 19 WEG)

Maßstab ist die **ordnungsmäßige Verwaltung** ([§ 18 Abs. 2](https://www.gesetze-im-internet.de/woeigg/__18.html), [§ 19 WEG](https://www.gesetze-im-internet.de/woeigg/__19.html)): dem Interesse der Gesamtheit der Eigentümer nach billigem Ermessen entsprechend. Den Eigentümern steht ein **Beurteilungs- und Ermessensspielraum** zu. Beispiele aus der jüngeren Rechtsprechung:

- Vor Erhaltungsmaßnahmen müssen **nicht generell Vergleichsangebote** eingeholt werden; ein Beschluss ist nicht allein deshalb für ungültig zu erklären (BGH, Urt. v. 27.03.2026 – V ZR 7/25, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-03-27&Aktenzeichen=V%20ZR%207/25)).
- Unverhältnismäßige Sonderumlage, sachfremde Erwägungen, Verstoß gegen den Gleichbehandlungsgrundsatz bleiben klassische Anfechtungsgründe.

### 7. Teilanfechtung

Ein Beschluss kann **in Teilen** angefochten werden, wenn der angegriffene Teil abtrennbar ist und die Eigentümer den Rest auch so beschlossen hätten. Das gilt insbesondere für den Nachschussbeschluss nach § 28 Abs. 2 WEG (BGH, Urt. v. 11.04.2025 – V ZR 96/24, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-04-11&Aktenzeichen=V%20ZR%2096/24)).

### 8. Kostenrisiko

Die Prozesskosten der GdWE sind Kosten der Verwaltung, die nach § 16 Abs. 2 WEG verteilt werden. Auch der **obsiegende Anfechtungskläger** trägt sie anteilig mit, soweit nichts anderes vereinbart oder beschlossen ist (BGH, Urt. v. 19.07.2024 – V ZR 139/23, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-07-19&Aktenzeichen=V%20ZR%20139/23)). Das in den Kostenhinweis aufnehmen.

### 9. Ergebnis

Erfolgsaussicht zusammenfassen: Klageart, Nichtigkeit oder Anfechtbarkeit, Fristwahrung, richtige Beklagte, durchgreifender Anfechtungsgrund, Reichweite (Voll- oder Teilanfechtung), Kostenrisiko.

## Quellen und Zitierweise

Verbindlich: [`../../references/zitierweise.md`](../../references/zitierweise.md).

### Statute (post-WEMoG)

- [§ 44 WEG](https://www.gesetze-im-internet.de/woeigg/__44.html) (Beschlussklagen; Abs. 2: Klage gegen die Gemeinschaft der Wohnungseigentümer)
- [§ 45 WEG](https://www.gesetze-im-internet.de/woeigg/__45.html) (Anfechtungsfrist — ein Monat Klagefrist, zwei Monate Begründungsfrist, Wiedereinsetzung)
- [§ 23 WEG](https://www.gesetze-im-internet.de/woeigg/__23.html) (Abs. 1a virtuelle Versammlung, Abs. 2 Ankündigung, Abs. 4 Nichtigkeit/Anfechtbarkeit)
- [§ 24 WEG](https://www.gesetze-im-internet.de/woeigg/__24.html) (Einberufung), [§ 25 WEG](https://www.gesetze-im-internet.de/woeigg/__25.html) (Beschlussfassung, Stimmrecht)
- [§ 18 WEG](https://www.gesetze-im-internet.de/woeigg/__18.html), [§ 19 WEG](https://www.gesetze-im-internet.de/woeigg/__19.html) (Maßstab der ordnungsmäßigen Verwaltung)
- [§ 43 WEG](https://www.gesetze-im-internet.de/woeigg/__43.html) (Zuständigkeit), [§ 72 GVG](https://www.gesetze-im-internet.de/gvg/__72.html) (Berufungsgericht), [§ 49 GKG](https://www.gesetze-im-internet.de/gkg_2004/__49.html) (Streitwert)

### Rechtsprechung (V. Zivilsenat)

1. BGH, Urt. v. 27.03.2026 – V ZR 7/25 (keine generelle Pflicht zu Vergleichsangeboten), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-03-27&Aktenzeichen=V%20ZR%207/25)
2. BGH, Urt. v. 11.04.2025 – V ZR 96/24 (Teilanfechtung des Nachschussbeschlusses), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-04-11&Aktenzeichen=V%20ZR%2096/24)
3. BGH, Urt. v. 24.10.2024 – V ZR 17/24 (Zustellung demnächst; Nachfragepflicht des Klägers) `[unverifiziert – prüfen: Datum in den Quellen uneinheitlich (24./25.10.2024)]`
4. BGH, Urt. v. 19.07.2024 – V ZR 139/23 (Kostenbeteiligung des obsiegenden Anfechtungsklägers), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-07-19&Aktenzeichen=V%20ZR%20139/23)

### Kommentare

- Bärmann/Göbel, WEG, aktuelle Aufl., §§ 44, 45 `[unverifiziert – prüfen: Auflage und Rn.]`
- Hügel/Elzer, WEG, aktuelle Aufl., § 45 `[unverifiziert – prüfen: Auflage und Rn.]`

## Beispiel (Gutachtenstil, verkürzt)

**Sachverhalt.** Versammlung am 14.09.2026 (Präsenz). Unter „Verschiedenes" wird eine Sonderumlage von 80.000 EUR beschlossen; in der Einladung war der Punkt nicht angekündigt. Eigentümer K stimmte dagegen.

**Frist.** Die Klagefrist endet am 14.10.2026, die Begründungsfrist am 16.11.2026 (14.11.2026 ist ein Samstag; Rechner, § 222 Abs. 2 ZPO). **Beklagte** ist die GdWE (§ 44 Abs. 2 S. 1 WEG), zuständig das Amtsgericht der belegenen Sache.

**Anfechtungsgrund.** Der Gegenstand war bei der Einberufung nicht bezeichnet (§ 23 Abs. 2 WEG). Der Beschluss ist nicht nichtig, sondern anfechtbar (§ 23 Abs. 4 S. 2 WEG). Dass er bei ordnungsgemäßer Ankündigung ebenso gefasst worden wäre, ist nicht festzustellen, weil abwesende Eigentümer sich auf die Tagesordnung verlassen durften.

**Ergebnis.** Hohe Erfolgsaussicht. Kostenhinweis: K trägt die Prozesskosten der GdWE anteilig mit, auch wenn er gewinnt (BGH V ZR 139/23); Streitwert nach § 49 GKG. ([V ZR 139/23](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-07-19&Aktenzeichen=V%20ZR%20139/23))

## Risiken / typische Fehler

- **Versäumte Anfechtungsfrist** → materielle Ausschlussfrist; der anfechtbare Beschluss wird bestandskräftig. Wiedereinsetzung nur bei fehlendem Verschulden (§ 45 S. 2 WEG).
- **Zustellung nicht überwacht** → bei steckender Zustellung binnen eines Jahres nachfragen (BGH V ZR 17/24); Vorschuss sofort zahlen. `[unverifiziert – prüfen: Datum in den Quellen uneinheitlich (24./25.10.2024)]`
- **falscher Beklagter** → Klage gegen die übrigen Eigentümer statt gegen die Gemeinschaft der Wohnungseigentümer (§ 44 Abs. 2 WEG, WEMoG-Änderung).
- **Nichtigkeit mit Anfechtbarkeit verwechselt** → fehlende Beschlusskompetenz führt zur Nichtigkeit; ein bloß anfechtbarer Beschluss wird nach Fristablauf bestandskräftig.
- **Alte Rechtslage angewandt** → Vor-WEMoG-Numerierung und Beklagtenstellung nicht mehr verwenden; durchgängig die post-WEMoG-Fassung prüfen.
- **Vollanfechtung statt Teilanfechtung** → bei abtrennbaren Positionen genügt die Teilanfechtung (BGH V ZR 96/24). ([V ZR 96/24](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-04-11&Aktenzeichen=V%20ZR%2096/24))
- **Kostenrisiko verschwiegen** → auch der obsiegende Kläger trägt anteilig die Kosten der GdWE (BGH V ZR 139/23). ([V ZR 139/23](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-07-19&Aktenzeichen=V%20ZR%20139/23))
- **Fehlende Vergleichsangebote als Selbstläufer** → trägt allein keine Anfechtung (BGH V ZR 7/25). ([V ZR 7/25](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-03-27&Aktenzeichen=V%20ZR%207/25))

## Ausgabeformat

```
ERFOLGSAUSSICHT — WEG-BESCHLUSSANFECHTUNG (Rechtsstand Oktober 2026)

1. Beschluss
   - Gegenstand / Beschlussart: <…>
   - Beschlussdatum / Versammlungsart: <…>

2. Klageart (§ 44 Abs. 1 WEG): [Anfechtung] [Nichtigkeit hilfsweise] [Beschlussersetzung]

3. Nichtigkeit vs. Anfechtbarkeit (§ 23 Abs. 4 WEG)
   - Beschlusskompetenz: <Grundlage / fehlt → nichtig>
   - Einordnung: [ ] nichtig  [ ] anfechtbar

4. Fristen (§ 45 WEG)
   - Klagefrist: <Datum> | Begründungsfrist: <Datum> | Wiedereinsetzung: <…>

5. Beklagte / Gericht / Streitwert
   - GdWE, vertreten durch <Verwalter / Beirat>
   - AG <Ort> (§ 43 Abs. 2 Nr. 4 WEG) | Streitwert § 49 GKG: <…>

6. Formelle Gründe (§§ 23 Abs. 2, 24, 25 WEG): <…>
7. Materielle Prüfung (§§ 18, 19 WEG): <…>
8. Teilanfechtung: <abtrennbar? Reichweite>
9. Kostenrisiko: <inkl. Anteil an den Kosten der GdWE>
10. Ergebnis: <hoch / offen / gering> — <Begründung>
```
