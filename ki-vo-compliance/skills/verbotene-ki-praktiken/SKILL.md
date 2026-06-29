---
name: verbotene-ki-praktiken
description: "Prüfung der verbotenen KI-Praktiken nach Art. 5 KI-VO – manipulative und ausnutzende Systeme, Social Scoring, biometrische Echtzeit-Fernidentifizierung, Ausnahmen und Bußgeldrisiko Art. 99 KI-VO. Use when ein Unternehmen oder eine Behörde prüfen muss, ob ein geplantes oder eingesetztes KI-System unter die Verbotstatbestände der KI-VO fällt."
language: de
provider_variants: [claude, gemini, openai]
test: ./test.md
---

# /ki-vo-compliance:verbotene-ki-praktiken

## Zweck

**Art. 5 KI-VO** ([VO (EU) 2024/1689](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1689)) listet die KI-Praktiken, die als mit den europäischen Grundrechten unvereinbar **vollständig verboten** sind. Diese Verbote gelten seit dem 2. Februar 2025. Verstöße bilden die höchste Bußgeldstufe der Verordnung. Dieser Skill prüft, ob ein System einen Verbotstatbestand erfüllt und ob eine eng auszulegende Ausnahme greift.

## Eingaben

- Funktion und Zweck des KI-Systems
- Adressatenkreis (allgemeine Öffentlichkeit, Beschäftigte, vulnerable Gruppen)
- Einsatzkontext (öffentlich zugänglicher Raum, Strafverfolgung, privat, behördlich)
- Verwendete Techniken (Manipulation, biometrische Erfassung, Bewertung von Sozialverhalten)
- Rolle des Mandanten (Anbieter, Betreiber)

## Sub-Agent-Architektur

Drei gedankliche Rollen prüfen das System. Ein **Tatbestands-Prüfer** ordnet die Funktion den acht Verbotskategorien des Art. 5 KI-VO zu und arbeitet die jeweiligen Tatbestandsmerkmale heraus. Ein **Ausnahme-Analyst** prüft spiegelbildlich die eng gefassten Ausnahmen, insbesondere bei der biometrischen Echtzeit-Fernidentifizierung zu Strafverfolgungszwecken. Ein **Sanktions-Bewerter** beziffert das Bußgeldrisiko nach Art. 99 KI-VO und grenzt zur Hochrisiko-Einstufung ab. Der Tatbestands-Prüfer übergibt jeden bejahten Verbotstatbestand an den Ausnahme-Analysten, bevor das Endergebnis steht.

## Ablauf

### 1. Verbotskategorien (Art. 5 Abs. 1 KI-VO)

a) **Unterschwellige/manipulative Beeinflussung**, die das Verhalten wesentlich verändert und Schaden verursacht
b) **Ausnutzung von Vulnerabilität** (Alter, Behinderung, soziale/wirtschaftliche Lage) mit Schadensfolge
c) **Social Scoring** — Bewertung/Klassifizierung anhand sozialen Verhaltens oder persönlicher Merkmale mit ungerechtfertigter Schlechterstellung in nicht zusammenhängenden Kontexten
d) **Prädiktive Strafverfolgung** allein auf Profiling/Persönlichkeitsmerkmalen
e) **Ungezieltes Scraping** von Gesichtsbildern zum Aufbau von Gesichtserkennungsdatenbanken
f) **Emotionserkennung** am Arbeitsplatz und in Bildungseinrichtungen (außer medizinisch/sicherheitsbezogen)
g) **Biometrische Kategorisierung** zur Ableitung sensibler Merkmale (z. B. ethnische Herkunft, politische Meinung, sexuelle Orientierung)
h) **Biometrische Echtzeit-Fernidentifizierung** in öffentlich zugänglichen Räumen zu Strafverfolgungszwecken

### 2. Ausnahmen bei biometrischer Echtzeit-Fernidentifizierung (Art. 5 Abs. 1 lit. h KI-VO)

Nur **drei** eng begrenzte Zwecke kommen in Betracht:

- gezielte Suche nach Opfern von Entführung, Menschenhandel, sexueller Ausbeutung sowie vermissten Personen
- Abwendung einer konkreten, erheblichen und unmittelbaren Gefahr für Leib/Leben oder eines Terroranschlags
- Lokalisierung/Identifizierung eines einer schweren Straftat Verdächtigen

Voraussetzung: vorherige **richterliche oder behördliche Genehmigung** (Art. 5 Abs. 3 KI-VO), Verhältnismäßigkeit, nationale Ermächtigungsgrundlage.

### 3. Abgrenzung zur Hochrisiko-Einstufung

Greift kein Verbot, ist die Hochrisiko-Prüfung nach Art. 6 i.V.m. Anhang III KI-VO der nächste Schritt — ein System kann zulässig, aber hochreguliert sein.

### 4. Sanktionen (Art. 99 KI-VO)

Verstöße gegen die Verbote nach Art. 5 KI-VO werden mit Geldbußen bis **35 Mio. EUR oder 7 % des weltweiten Jahresumsatzes** geahndet — die höchste Stufe.

## Risiken

- **Manipulation** — vermeintlich harmlose Personalisierung kann als unterschwellige Beeinflussung nach Art. 5 KI-VO verboten sein.
- **Social Scoring** durch die Hintertür — übergreifende Reputations- oder Bonitätssysteme können den Verbotstatbestand erfüllen.
- **Scheinausnahme** — die Ausnahmen zur biometrischen Echtzeit-Fernidentifizierung sind eng; eine fehlende Genehmigung nach Art. 5 Abs. 3 KI-VO macht den Einsatz verboten.
- **Bußgeldrisiko** — bis 35 Mio. EUR / 7 % nach Art. 99 KI-VO; Verbote gelten bereits seit Februar 2025.

## Ausgabeformat

```
VERBOTENE KI-PRAKTIKEN — PRÜFUNG — <System> — <Datum>

I.   Funktion / Zweck                          [Beschreibung]
II.  Einschlägige Kategorie (Art. 5 KI-VO)     [lit. a–h / keine]
     Tatbestandsmerkmale                       [erfüllt? <…>]
III. Ausnahme (Art. 5 Abs. 1 lit. h / Abs. 3 KI-VO)  [greift? / Genehmigung?]
IV.  Ergebnis                                  [VERBOTEN / nicht verboten]
V.   Falls nicht verboten: Hochrisiko-Check (Art. 6, Anhang III)  [erforderlich?]
VI.  Bußgeldrisiko (Art. 99 KI-VO)             [bis 35 Mio. EUR / 7 %]

Empfehlung: <…>
Nächste Schritte: <…>
```

## Quellen

### Statute

- [VO (EU) 2024/1689 (KI-VO / EU AI Act)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1689) — Volltext mit Anhängen
- Art. 5 KI-VO (verbotene Praktiken), Art. 6 KI-VO und Anhang III (Hochrisiko), Art. 99 KI-VO (Sanktionen)

### Leitlinien

- EU-Kommission, Leitlinien zur Anwendung der Verbote gemäß Art. 5 KI-VO (Februar 2025)

### Sekundärliteratur

- Hilgendorf/Roth-Isigkeit, KI-VO, 1. Aufl. 2024
- BeckOK KI-VO (Online)
