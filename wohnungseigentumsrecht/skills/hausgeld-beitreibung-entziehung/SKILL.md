---
name: hausgeld-beitreibung-entziehung
description: "Beitreibung rückständigen Hausgelds durch die Gemeinschaft der Wohnungseigentümer und Entziehung des Wohnungseigentums – Anspruchsgrundlage Vorschuss- und Nachschussbeschlüsse § 28 Abs. 1–3 WEG, Verzug und Verzugszinsen §§ 286, 288, 247 BGB, kein Zurückbehaltungsrecht gegenüber Vorschüssen, Mahnbescheid und Zahlungsklage vor dem Amtsgericht § 43 Abs. 2 Nr. 2 WEG, Vertretung durch den Verwalter § 9b WEG, Verjährung §§ 195, 199 BGB (Hausgeld 2023 verjährt mit Ablauf des 31.12.2026), Zwangsversteigerung mit Vorrang § 10 Abs. 1 Nr. 2 ZVG (Jahr der Beschlagnahme und zwei Vorjahre, höchstens 5 % des Verkehrswerts, Titel nach § 10 Abs. 3 ZVG), Sicherungshypothek § 866 ZPO, Insolvenz des Eigentümers, Entziehung § 17 WEG mit Abmahnung und Veräußerungsurteil, Stimmverbot § 25 Abs. 4 WEG. Rechtsstand: Oktober 2026. Use when ein Wohnungseigentümer Hausgeld, Nachschüsse oder Sonderumlagen nicht zahlt und die Gemeinschaft Beitreibung, Vollstreckung oder Entziehung prüft."
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

# /wohnungseigentumsrecht:hausgeld-beitreibung-entziehung

## Zweck

Hausgeld ist die Liquidität der Gemeinschaft. Zahlt ein Eigentümer nicht, müssen die übrigen vorfinanzieren. Dieser Skill führt von der Forderungsfeststellung über Mahnung, Mahnverfahren und Klage bis zur Vollstreckung in das Wohnungseigentum — wo das Hausgeld in der Zwangsversteigerung **vor den Grundpfandrechten** befriedigt wird — und prüft als letztes Mittel die **Entziehung** nach [§ 17 WEG](https://www.gesetze-im-internet.de/woeigg/__17.html).

**Rechtsstand: Oktober 2026.** §§ 17, 28 WEG und § 10 ZVG sind seit dem WEMoG unverändert; die frühere Mindestschwelle für die Vollstreckung im Vorrang ist entfallen. **Fristwarnung:** Hausgeldforderungen, die im Jahr **2023** fällig wurden, verjähren mit Ablauf des **31.12.2026**. Klage oder Mahnbescheid müssen vorher zugestellt bzw. „demnächst" zugestellt werden.

## Eingaben

- Beschlüsse über Wirtschaftsplan (Vorschüsse), Nachschüsse/Abrechnungsspitze, Sonderumlagen — Datum, Fälligkeitsregelung
- Kontoauszug des Eigentümers: Soll, Zahlungen, Rückstand je Monat
- Mahnungen, Zahlungsvereinbarungen, Einwände des Eigentümers (Aufrechnung, Zurückbehaltung, Minderung)
- Grundbuchauszug (Belastungen, Rang), Verkehrswert, laufende Zwangsversteigerung oder Insolvenz
- frühere Pflichtverletzungen und Abmahnungen (für § 17 WEG)

## Sub-Agent-Architektur

- **Researcher** liefert §§ 9b, 17, 25, 28, 43 WEG, §§ 286, 288, 195, 199 BGB, § 10 ZVG, §§ 866, 867 ZPO und die Rechtsprechung zur Zurückbehaltung.
- **Drafter** erstellt Forderungsaufstellung, Mahnung, Mahnantrag oder Klageschrift, Antrag auf Zwangsversteigerung, Beschlussvorlage zur Entziehungsklage.
- **Reviewer** prüft Anspruchsgrundlage je Monat, Verjährung, Vorrangfähigkeit und Abmahnung.

## Ablauf

### 1. Anspruchsgrundlage: der Beschluss, nicht die Abrechnung

- Die Zahlungspflicht entsteht durch den **Beschluss** über Vorschüsse ([§ 28 Abs. 1 WEG](https://www.gesetze-im-internet.de/woeigg/__28.html)), Nachschüsse bzw. Anpassung der Vorschüsse (§ 28 Abs. 2 WEG) oder eine Sonderumlage. Gläubigerin ist die **Gemeinschaft der Wohnungseigentümer** (GdWE).
- **Fälligkeit** nach dem Beschluss (§ 28 Abs. 3 WEG), sonst sofort.
- Für jede Monatsrate die Beschlussgrundlage und Fälligkeit aufstellen. Ein bestandskräftiger Beschluss ist auch dann Grundlage, wenn er rechtswidrig war.

### 2. Einwände des Eigentümers

- **Kein Zurückbehaltungsrecht** gegenüber beschlossenen Vorschüssen — auch nicht wegen anerkannter oder rechtskräftig zuerkannter Gegenforderungen gegen die GdWE (BGH, Urt. v. 14.11.2025 – V ZR 190/24, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-11-14&Aktenzeichen=V%20ZR%20190/24)).
- **Aufrechnung** ist grundsätzlich ausgeschlossen und nur ausnahmsweise mit **anerkannten oder rechtskräftig festgestellten** Gegenforderungen zulässig (BGH, Urt. v. 14.11.2025 – V ZR 190/24 Rn. 17, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-11-14&Aktenzeichen=V%20ZR%20190/24), [Volltext](https://www.rws-verlag.de/fileadmin/Volltexte-4/v_zr_190-24.pdf)).
- **Anfechtung** des zugrunde liegenden Beschlusses hemmt die Zahlungspflicht nicht; bis zur rechtskräftigen Ungültigerklärung bleibt er wirksam ([§ 23 Abs. 4 S. 2 WEG](https://www.gesetze-im-internet.de/woeigg/__23.html)).
- **Mietminderung** des Mieters ist kein Einwand gegen das Hausgeld.

### 3. Verzug und Zinsen (§§ 286, 288 BGB)

- Verzug mit kalendermäßig bestimmter Fälligkeit ohne Mahnung (§ 286 Abs. 2 Nr. 1 BGB), sonst nach Mahnung.
- Hausgeld ist **keine Entgeltforderung**; Zinssatz **5 Prozentpunkte** über dem Basiszinssatz ([§ 288 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__288.html)). Basiszinssatz: 1,27 % ab 01.01.2026, **1,52 % ab 01.07.2026** (Deutsche Bundesbank).

```bash
# je Monatsrate getrennt rechnen: Verzug ab dem Tag nach Fälligkeit (hier 3. Werktag)
python -m scripts.legal_calc.cli verzugszinsen --betrag 600 --verzug-ab 05.02.2026 --bis 23.10.2026 \
    --basiszins 01.01.2026:1.27 --basiszins 01.07.2026:1.52 --schuldner-ist-verbraucher
# -> 27,27 EUR für die Februarrate; die neun Raten Februar bis Oktober 2026 ergeben zusammen 132,75 EUR
```

### 4. Verjährung (§§ 195, 199 BGB)

- Regelverjährung **drei Jahre** ab Schluss des Jahres der Fälligkeit ([§ 195](https://www.gesetze-im-internet.de/bgb/__195.html), [§ 199 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__199.html)).
- Hemmung durch Zustellung von Klage oder Mahnbescheid (§ 204 Abs. 1 Nr. 1, 3 BGB); Rückwirkung bei Zustellung „demnächst" (§ 167 ZPO).

```bash
python -m scripts.legal_calc.cli verjaehrung --entstehung 05.06.2023 --kenntnis 05.06.2023
# -> Verjährung mit Ablauf des 31.12.2026
```

### 5. Gerichtliche Durchsetzung

- **Klägerin** ist die GdWE, vertreten durch den Verwalter ([§ 9b Abs. 1 WEG](https://www.gesetze-im-internet.de/woeigg/__9b.html)); für Aktivprozesse ist kein gesonderter Beschluss erforderlich, wenn die Beitreibung dem Verwalter übertragen ist oder es sich um eine Maßnahme nach § 27 Abs. 1 Nr. 2 WEG handelt `[unverifiziert – prüfen: Reichweite der Verwalterbefugnis ohne Ermächtigungsbeschluss]`.
- **Zuständigkeit:** ausschließlich das Amtsgericht der belegenen Sache ([§ 43 Abs. 2 Nr. 2 WEG](https://www.gesetze-im-internet.de/woeigg/__43.html)); im Mahnverfahren als Streitgericht anzugeben.
- **Titel** so fassen, dass Art, Bezugszeitraum und Fälligkeit des Anspruchs erkennbar sind — das ist Voraussetzung für die Vollstreckung im Vorrang ([§ 10 Abs. 3 ZVG](https://www.gesetze-im-internet.de/zvg/__10.html)). Sonst ist Glaubhaftmachung nötig.

### 6. Vollstreckung in das Wohnungseigentum

| Instrument | Wirkung | Norm |
|---|---|---|
| **Zwangsversteigerung** im Rang des § 10 Abs. 1 Nr. 2 ZVG | Befriedigung **vor** den Grundpfandrechten für laufende Beträge und Rückstände aus dem **Jahr der Beschlagnahme und den letzten zwei Jahren**, begrenzt auf **5 % des festgesetzten Verkehrswerts** einschließlich Nebenleistungen; Anmeldung durch die GdWE | [§ 10 Abs. 1 Nr. 2 ZVG](https://www.gesetze-im-internet.de/zvg/__10.html) |
| **Beitritt** zu einer laufenden Versteigerung | eigener Antrag; das Gericht lässt den Beitritt zu, der Gläubiger erhält die Rechte eines betreibenden Gläubigers | [§ 27 ZVG](https://www.gesetze-im-internet.de/zvg/__27.html) |
| **Anmeldung** in fremder Versteigerung | Vorrang der Rangklasse 2 ohne eigenen Antrag; Anmeldung durch die GdWE | § 10 Abs. 1 Nr. 2 S. 4 ZVG |
| **Zwangsverwaltung** | Mieteinnahmen decken laufendes Hausgeld | §§ 146 ff. ZVG |
| **Sicherungshypothek** | Sicherung ohne sofortige Verwertung; Mindestbetrag über 750 EUR | [§ 866 Abs. 3 ZPO](https://www.gesetze-im-internet.de/zpo/__866.html) |

Ältere Rückstände (außerhalb des Zwei-Jahres-Fensters) fallen in den Rang des betreibenden Gläubigers; frühzeitig vollstrecken.

### 7. Eigentümerwechsel und Insolvenz

- **Erwerber** haftet nicht für Hausgeldschulden des Veräußerers, die vor dem Eigentumsübergang fällig wurden; für danach fällige Beträge — auch eine nach dem Übergang beschlossene Abrechnungsspitze — haftet der neue Eigentümer `[unverifiziert – prüfen: Fortgeltung der Fälligkeitstheorie nach WEMoG]`.
- **Insolvenz** des Eigentümers: Rückstände vor Eröffnung sind Insolvenzforderungen; das Vorrecht des § 10 Abs. 1 Nr. 2 ZVG begründet ein Absonderungsrecht (§ 49 InsO) `[unverifiziert – prüfen]`. Nach Eröffnung fällig werdendes Hausgeld ist Masseverbindlichkeit (§ 55 Abs. 1 Nr. 1 InsO) `[unverifiziert – prüfen]`.

### 8. Entziehung (§ 17 WEG) — ultima ratio

- Hat sich ein Eigentümer einer so **schweren Pflichtverletzung** schuldig gemacht, dass den anderen die Fortsetzung der Gemeinschaft nicht mehr zuzumuten ist, kann die **GdWE** die **Veräußerung** verlangen ([§ 17 Abs. 1 WEG](https://www.gesetze-im-internet.de/woeigg/__17.html)).
- Regelbeispiel: **trotz Abmahnung wiederholt gröblicher Verstoß** gegen die Pflichten aus § 14 Abs. 1 und 2 WEG (§ 17 Abs. 2 WEG). Der frühere Sondertatbestand des Hausgeldverzugs (§ 18 Abs. 2 Nr. 2 WEG a. F.) ist entfallen; anhaltende erhebliche Zahlungsrückstände sind am allgemeinen Maßstab des Abs. 1 zu messen.
- **Verfahren:** Beschluss der Eigentümer über die Klageerhebung (einfache Mehrheit), **Abmahnung** mit konkreter Fristsetzung, Klage der GdWE auf Veräußerung; das Urteil wird nach dem ZVG vollstreckt (§ 17 Abs. 4 WEG). Der Anspruch ist durch Vereinbarung nicht einschränkbar (§ 17 Abs. 3 WEG).
- Nach **rechtskräftiger Verurteilung** ist der Eigentümer nicht stimmberechtigt ([§ 25 Abs. 4 WEG](https://www.gesetze-im-internet.de/woeigg/__25.html)).
- **Verhältnismäßigkeit:** Vorrangig Beitreibung und Zwangsversteigerung; die Entziehung kommt in Betracht, wenn die Vollstreckung dauerhaft ins Leere läuft oder neben dem Zahlungsverzug weitere schwere Störungen treten.

### 9. Ergebnis

Forderungsaufstellung mit Beschlussgrundlage, Verjährungsampel je Jahr, empfohlener Weg (Mahnbescheid / Klage / Versteigerung / Beitritt), Vorrangbetrag, Entziehung ja/nein mit Abmahnungsstand.

## Quellen und Zitierweise

Verbindlich: [`../../references/zitierweise.md`](../../references/zitierweise.md).

### Statute

- [§ 28 WEG](https://www.gesetze-im-internet.de/woeigg/__28.html), [§ 17 WEG](https://www.gesetze-im-internet.de/woeigg/__17.html), [§ 25 WEG](https://www.gesetze-im-internet.de/woeigg/__25.html), [§ 43 WEG](https://www.gesetze-im-internet.de/woeigg/__43.html), [§ 9b WEG](https://www.gesetze-im-internet.de/woeigg/__9b.html)
- [§ 288 BGB](https://www.gesetze-im-internet.de/bgb/__288.html), [§ 286 BGB](https://www.gesetze-im-internet.de/bgb/__286.html), [§ 195 BGB](https://www.gesetze-im-internet.de/bgb/__195.html), [§ 199 BGB](https://www.gesetze-im-internet.de/bgb/__199.html)
- [§ 10 ZVG](https://www.gesetze-im-internet.de/zvg/__10.html) (Rangklasse 2, Titelanforderungen Abs. 3), [§ 866 ZPO](https://www.gesetze-im-internet.de/zpo/__866.html)

### Rechtsprechung (V. Zivilsenat)

1. BGH, Urt. v. 14.11.2025 – V ZR 190/24 (kein Zurückbehaltungsrecht gegenüber Vorschüssen), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-11-14&Aktenzeichen=V%20ZR%20190/24)
2. BGH, Urt. v. 26.09.2025 – V ZR 108/24 (Ermessen bei der Höhe der Vorschüsse), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-09-26&Aktenzeichen=V%20ZR%20108/24)

### Kommentare

- Bärmann/Suilmann, WEG, aktuelle Aufl., § 17 `[unverifiziert – prüfen: Auflage und Rn.]`
- Stöber, ZVG, aktuelle Aufl., § 10 Rn. zu Nr. 2 `[unverifiziert – prüfen: Auflage und Rn.]`

## Beispiel (Urteilsstil, verkürzt)

**Sachverhalt.** Eigentümer S zahlt seit Februar 2026 kein Hausgeld (600 EUR monatlich, fällig am 3. Werktag); Rückstand am 23.10.2026: 5.400 EUR (neun Monatsraten Februar bis Oktober; erste Fälligkeit 04.02.2026, Verzug ab 05.02.2026). Aus 2023 ist eine Abrechnungsspitze von 1.150 EUR offen (fällig 05.06.2023). S hält das Geld zurück, weil die GdWE seinen Wasserschaden nicht reguliere. Das Wohnungseigentum ist mit einer Grundschuld voll belastet; Verkehrswert 260.000 EUR.

**Bewertung.** Die Forderungen beruhen auf bestandskräftigen Beschlüssen. Ein Zurückbehaltungsrecht besteht nicht (V ZR 190/24). Die Spitze 2023 verjährt mit Ablauf des 31.12.2026 und ist sofort gerichtlich geltend zu machen. Verzugszinsen auf die neun Raten, je Rate ab dem Tag nach ihrer Fälligkeit gerechnet: 132,75 EUR bis 23.10.2026 (Rechner); Zinsen auf die Spitze 2023 gesondert. In der Zwangsversteigerung ist der Vorrang auf 5 % von 260.000 EUR = 13.000 EUR begrenzt. Bei einer Beschlagnahme im Jahr 2026 erfasst er die Rückstände aus 2026, 2025 und 2024 — die **Spitze 2023 fällt aus dem Zeitfenster** und geht nur im Rang des betreibenden Gläubigers mit. ([V ZR 190/24](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-11-14&Aktenzeichen=V%20ZR%20190/24))

**Ergebnis.** Mahnbescheid bzw. Klage über 6.550 EUR (5.400 EUR + 1.150 EUR) nebst Zinsen sofort, mit Titel nach § 10 Abs. 3 ZVG (Art, Zeitraum, Fälligkeit je Rate); danach Antrag auf Zwangsversteigerung im Rang 2. Für eine Entziehung fehlen bislang Abmahnung und eine über den Zahlungsverzug hinausgehende Schwere.

## Risiken / typische Fehler

- **Verjährung zum Jahresende übersehen** → Hausgeld 2023 verjährt mit Ablauf des 31.12.2026; Zustellung „demnächst" sicherstellen.
- **Zurückbehaltung akzeptiert** → gegenüber Vorschüssen ausgeschlossen (BGH V ZR 190/24). ([V ZR 190/24](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-11-14&Aktenzeichen=V%20ZR%20190/24))
- **Titel ohne Zeitraum und Fälligkeit** → Vorrang nach § 10 Abs. 1 Nr. 2 ZVG nur mit Glaubhaftmachung erreichbar (§ 10 Abs. 3 ZVG).
- **Vorrangfenster verpasst** → nur Jahr der Beschlagnahme und zwei Vorjahre, höchstens 5 % des Verkehrswerts.
- **Zinssatz 9 Prozentpunkte** angesetzt → Hausgeld ist keine Entgeltforderung; 5 Prozentpunkte (§ 288 Abs. 1 BGB).
- **Falsche Klägerin** → Gläubigerin ist die GdWE, nicht der Verwalter und nicht die übrigen Eigentümer.
- **Entziehung § 17 WEG ohne Abmahnung** oder als Druckmittel → Klage scheitert; ultima ratio nach erfolgloser Vollstreckung.
- **Alter Sondertatbestand Hausgeldverzug** (§ 18 Abs. 2 Nr. 2 WEG a. F.) zitiert → seit WEMoG entfallen.

## Ausgabeformat

```
HAUSGELDBEITREIBUNG — <Einheit> — Stand <Datum> (Rechtsstand Oktober 2026)

1. Forderungsaufstellung
   | Zeitraum | Beschluss Nr./Datum | Fälligkeit | Betrag | verjährt am |
   Summe: <EUR>

2. Einwände: Zurückbehaltung [ausgeschlossen] | Aufrechnung [anerkannt/rechtskräftig?]

3. Zinsen (§ 288 Abs. 1 BGB, Rechner): <EUR> bis <Datum>

4. Verjährungsampel: 🔴 <Forderungen mit Ablauf 31.12.2026> | 🟢 <übrige>

5. Weg: [Mahnbescheid] [Klage AG <Ort>, § 43 Abs. 2 Nr. 2 WEG]
   Titel mit Art / Zeitraum / Fälligkeit (§ 10 Abs. 3 ZVG): <✓>

6. Vollstreckung: Versteigerung Rang 2 — Vorrang max. <5 % Verkehrswert = EUR>
   | Zwangsverwaltung | Sicherungshypothek (> 750 EUR)

7. Entziehung § 17 WEG: Abmahnung <Datum/fehlt> | Schwere <…> | Empfehlung <…>
```
