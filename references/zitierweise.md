# Zitierweise – BGH/Beck-Standard für `ai-skills-german-law`

This is the **binding** citation style for all skills in this repository. Outputs that violate it should be flagged by the Reviewer sub-agent.

## Grundregel: Jede juristische Aussage wird belegt.

Reihenfolge im Quellenverzeichnis: **Rechtsprechung vor Literatur**, jeweils neueste zuerst.

## Rechtsprechung

### Format

```
[Gericht], [Entscheidungsform] v. [TT.MM.JJJJ] – [Aktenzeichen], [Fundstelle] [Rn. N].
```

### Beispiele

```
BAG, Urt. v. 10.06.2010 – 2 AZR 541/09, NZA 2010, 1227 Rn. 24 ("Emmely").
BGH, Urt. v. 11.10.2023 – VIII ZR 117/22, NJW 2024, 122 Rn. 18.
BVerfG, Beschl. v. 27.01.1998 – 1 BvL 15/87, NJW 1998, 1475.
EuGH, Urt. v. 16.07.2020 – C-311/18, NJW 2020, 2613 ("Schrems II") Rn. 192.
```

### Verification states (mandatory)

| Marker | When |
|---|---|
| **(no marker)** | Citation has been independently verified by a contributor against Beck-Online, juris, openjur.net, or the issuing court's website. Include the URL in the SKILL.md source list. |
| `[unverifiziert – prüfen]` | Citation comes from model knowledge and has NOT been checked. The user must verify before relying on it. |
| `[generiert – kein Fundstellenbeleg]` | Aktenzeichen or page number was invented by the model. **Forbidden** in client-facing outputs. Only acceptable in pedagogical examples that are clearly framed as such. |

## Kommentarliteratur

### Format

```
[Bearbeiter], in: [Kommentar], [Auflage]. Aufl. [Jahr], [Norm] Rn. [N].
```

### Beispiele

```
Preis, in: ErfK, 24. Aufl. 2024, § 626 BGB Rn. 1.
Linck, in: ErfK, 24. Aufl. 2024, § 1 KSchG Rn. 100.
Dörner/Vossen, in: KR, 13. Aufl. 2022, § 1 KSchG Rn. 350.
Becker/Wolff, in: APS, 6. Aufl. 2021, § 102 BetrVG Rn. 12.
Müller-Glöge, in: MüKoBGB, 9. Aufl. 2023, § 622 Rn. 5.
```

Standard German legal commentaries to prefer (alphabetical):

- **APS** – Ascheid/Preis/Schmidt, Kündigungsrecht
- **BeckOK** – Beck'scher Online-Kommentar (zu BGB, GmbHG, MietR, etc.)
- **ErfK** – Erfurter Kommentar zum Arbeitsrecht
- **HWK** – Henssler/Willemsen/Kalb, Arbeitsrecht
- **KR** – Kündigungsrecht-Kommentar (Etzel u.a.)
- **MüKo** – Münchener Kommentar (BGB, GmbHG, etc.)
- **Palandt** (jetzt: Grüneberg) – Beck-Kurz-Kommentar zum BGB
- **Schönke/Schröder** – StGB-Kommentar
- **Schaub** – Arbeitsrechts-Handbuch
- **Staudinger** – Großkommentar BGB

## Aufsätze

### Format

```
[Autor], [Titel], [Zeitschrift] [Jahr], [Anfangsseite], [konkrete Seite].
```

### Beispiele

```
Bauer, Zur Zukunft des Kündigungsschutzrechts, NZA 2024, 1, 8.
Kessler, Aktuelle Entwicklungen zur DSGVO-Auskunft, NJW 2024, 1234, 1238.
```

## Statutes

Statutes get **a verified URL** to [gesetze-im-internet.de](https://www.gesetze-im-internet.de) (or, for EU law, EUR-Lex). No `[unverifiziert]` marker is needed if the URL is included.

### Format

Inline: `§ 1 Abs. 3 KSchG`
On first appearance per skill: link to the official source.

### Examples

- [§ 1 KSchG (Kündigungsschutzgesetz)](https://www.gesetze-im-internet.de/kschg/__1.html)
- [§ 102 BetrVG (Anhörung des Betriebsrats)](https://www.gesetze-im-internet.de/betrvg/__102.html)
- [§ 626 BGB (außerordentliche Kündigung)](https://www.gesetze-im-internet.de/bgb/__626.html)
- [Art. 6 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679#d1e1888-1-1)

## Zeitschriften-Abkürzungen (Auswahl)

- **NJW** – Neue Juristische Wochenschrift
- **NZA** – Neue Zeitschrift für Arbeitsrecht
- **NJW-RR** – NJW-Rechtsprechungs-Report
- **NStZ** – Neue Zeitschrift für Strafrecht
- **NVwZ** – Neue Zeitschrift für Verwaltungsrecht
- **BB** – Betriebs-Berater
- **DB** – Der Betrieb
- **DStR** – Deutsches Steuerrecht
- **GRUR** – Gewerblicher Rechtsschutz und Urheberrecht
- **WM** – Wertpapier-Mitteilungen
- **ZIP** – Zeitschrift für Wirtschaftsrecht
- **ZHR** – Zeitschrift für das gesamte Handels- und Wirtschaftsrecht
- **K&R** – Kommunikation & Recht
- **BeckRS** – Beck Rechtsprechung

## Quellenverzeichnis am Ende eines Memos

```
Quellen

I. Rechtsprechung
   1. BAG, Urt. v. 10.06.2010 – 2 AZR 541/09, NZA 2010, 1227 ("Emmely") [unverifiziert – prüfen].
   2. ...

II. Kommentare
   1. Preis, in: ErfK, 24. Aufl. 2024, § 626 BGB Rn. 1.
   2. ...

III. Aufsätze
   1. Bauer, NZA 2024, 1, 8.

IV. Normen
   - § 1 KSchG  – https://www.gesetze-im-internet.de/kschg/__1.html
   - § 626 BGB  – https://www.gesetze-im-internet.de/bgb/__626.html
```
