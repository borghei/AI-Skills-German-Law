---
name: vermietete-eigentumswohnung
description: "Schnittstelle Wohnungseigentum und Mietrecht bei der vermieteten Eigentumswohnung – Betriebskostenumlage nach dem WEG-Verteilerschlüssel § 556a Abs. 3 BGB und Trennung von WEG-Jahresabrechnung und Betriebskostenabrechnung § 556 Abs. 3 BGB, Duldungspflicht des Mieters gegenüber der Gemeinschaft § 15 WEG, bauliche Veränderungen auf Wunsch des Mieters § 554 BGB und Gestattungsanspruch des Vermieters § 20 Abs. 2 WEG, Haftung des Vermieters für geduldete Veränderungen des Mieters, Mängel am Gemeinschaftseigentum mit Minderung im Mietverhältnis und Schadensersatz gegen die GdWE, Vorkaufsrecht § 577 BGB und Kündigungssperrfrist § 577a BGB nach Umwandlung. Rechtsstand: Oktober 2026. Use when eine Eigentumswohnung vermietet ist und Betriebskosten, Erhaltungsmaßnahmen, bauliche Veränderungen, Mängel oder Kündigung das Verhältnis zwischen Mieter, vermietendem Eigentümer und Gemeinschaft berühren."
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

# /wohnungseigentumsrecht:vermietete-eigentumswohnung

## Zweck

Der vermietende Eigentümer steht in zwei getrennten Rechtsverhältnissen: zur **Gemeinschaft der Wohnungseigentümer** (WEG) und zum **Mieter** (BGB). Beide Regime sind nicht deckungsgleich — Verteilerschlüssel, Fristen und Ansprüche laufen auseinander, und der Eigentümer haftet in beide Richtungen. Dieser Skill ordnet ein Problem dem richtigen Verhältnis zu, gleicht die Regelungen ab und zeigt, wo der Eigentümer Ansprüche weiterreichen kann und wo er das Risiko selbst trägt.

**Rechtsstand: Oktober 2026.** Seit dem WEMoG ist der Mieter unmittelbar der Gemeinschaft gegenüber duldungspflichtig ([§ 15 WEG](https://www.gesetze-im-internet.de/woeigg/__15.html)), und der Betriebskostenschlüssel folgt mangels Vereinbarung dem WEG-Schlüssel ([§ 556a Abs. 3 BGB](https://www.gesetze-im-internet.de/bgb/__556a.html)). Der anhängige Regierungsentwurf zum Mietrecht (BT-Drs. 21/6807, nicht verabschiedet) würde § 566 BGB auf Veräußerungen an Miteigentümer erstrecken; für die Schnittstellen dieses Skills ändert er sonst nichts. Für das Mietrecht im Übrigen: `/mietrecht:*`.

## Eingaben

- Mietvertrag (Betriebskostenvereinbarung, Umlageschlüssel, Klauseln zu baulichen Veränderungen, Hausordnung)
- Gemeinschaftsordnung und Beschlüsse (Kostenschlüssel, Hausordnung, Gebrauchsregelungen)
- WEG-Jahresabrechnung und Einzelabrechnung, Wirtschaftsplan
- Ankündigungen der GdWE zu Erhaltungs- und Modernisierungsmaßnahmen
- Mängelanzeigen des Mieters, Minderungsbeträge
- Eigentumsgeschichte (Umwandlung nach Überlassung? Veräußerung wann?)

## Sub-Agent-Architektur

- **Researcher** liefert §§ 15, 16, 20, 28 WEG und §§ 554, 556, 556a, 536, 577, 577a BGB sowie die Rechtsprechung des V. (WEG) und VIII. Zivilsenats (Wohnraummiete).
- **Drafter** erstellt die Betriebskostenabrechnung aus der WEG-Abrechnung, Duldungsaufforderungen, Antrag auf Gestattung bei der GdWE oder Schadensersatzanspruch gegen die GdWE.
- **Reviewer** prüft, ob jede Position dem richtigen Rechtsverhältnis zugeordnet und die Mietrechtsfrist eingehalten ist.

## Ablauf

### 1. Betriebskosten: zwei Abrechnungen, ein Schlüssel

- Ist Wohnungseigentum vermietet und **nichts anderes vereinbart**, sind die Betriebskosten nach dem **für die Verteilung zwischen den Wohnungseigentümern geltenden Maßstab** umzulegen; widerspricht dieser billigem Ermessen, nach Wohnfläche ([§ 556a Abs. 3 BGB](https://www.gesetze-im-internet.de/bgb/__556a.html)).
- Die **WEG-Einzelabrechnung ist keine Betriebskostenabrechnung**. Herauszunehmen sind insbesondere Verwaltervergütung, Zuführung zur Erhaltungsrücklage, Erhaltungs- und Reparaturkosten, Bankgebühren der GdWE. Umlagefähig sind nur Kosten nach der BetrKV, soweit vereinbart ([§ 556 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__556.html)).
- **Grundsteuer** wird dem Eigentümer direkt von der Gemeinde berechnet und ist gesondert anzusetzen.
- **Frist:** Abrechnung an den Mieter binnen **zwölf Monaten** nach Ende des Abrechnungszeitraums ([§ 556 Abs. 3 S. 2 BGB](https://www.gesetze-im-internet.de/bgb/__556.html)). Die Frist läuft unabhängig davon, wann die GdWE ihre Jahresabrechnung beschließt. Ob eine verspätete WEG-Abrechnung die Verspätung entschuldigt, ist eine Frage des Vertretenmüssens (§ 556 Abs. 3 S. 3 BGB) `[unverifiziert – prüfen: VIII. ZS-Rechtsprechung zur Abhängigkeit von der WEG-Abrechnung]`.
- Mietrechtliche Detailprüfung: `/mietrecht:betriebskostenabrechnung`, Heizkosten: `/mietrecht:heizkosten-co2-fernablesung`.

### 2. Erhaltung und Modernisierung durch die GdWE

- Der Mieter hat **gegenüber der GdWE und den anderen Eigentümern** zu dulden: Erhaltungsmaßnahmen, die ihm **rechtzeitig angekündigt** wurden (§ 555a Abs. 2 BGB gilt entsprechend), und darüber hinausgehende Maßnahmen, die **spätestens drei Monate vor Beginn in Textform** angekündigt wurden ([§ 15 WEG](https://www.gesetze-im-internet.de/woeigg/__15.html); § 555c Abs. 1 S. 2 Nr. 1, 2, Abs. 2–4 und § 555d Abs. 2–5 BGB entsprechend).
- Die GdWE kann die Duldung **unmittelbar** vom Mieter verlangen; der Härteeinwand des Mieters (§ 555d Abs. 2 BGB) gilt entsprechend.
- Ob der Eigentümer im Mietverhältnis die **Miete nach § 559 BGB erhöhen** darf, richtet sich allein nach Mietrecht (`/mietrecht:modernisierung-559-bgb`, `/mietrecht:heizungstausch-559e-559f`). Die Modernisierungsankündigung nach § 555c BGB gibt der vermietende Eigentümer ab, nicht die GdWE.

### 3. Bauliche Veränderungen auf Wunsch des Mieters

- Der **Mieter** kann vom Vermieter die Erlaubnis baulicher Veränderungen verlangen, die der **Barrierefreiheit**, dem **Laden von E-Fahrzeugen**, dem **Einbruchsschutz** oder **Steckersolargeräten** dienen ([§ 554 BGB](https://www.gesetze-im-internet.de/bgb/__554.html)); Glasfaser ist — anders als in § 20 Abs. 2 WEG — nicht genannt.
- Betrifft die Maßnahme Gemeinschaftseigentum, braucht der **Eigentümer** zusätzlich einen **Gestattungsbeschluss** der GdWE; auf ihn hat er bei privilegierten Maßnahmen einen Anspruch ([§ 20 Abs. 2 WEG](https://www.gesetze-im-internet.de/woeigg/__20.html)). Reihenfolge: erst Gestattung durch die GdWE, dann Erlaubnis an den Mieter.
- Erlaubt oder duldet der Eigentümer eine Veränderung seines Mieters am Gemeinschaftseigentum ohne Gestattung, **haftet er** gegenüber der GdWE auf Beseitigung (BGH, Urt. v. 21.03.2025 – V ZR 1/24, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-03-21&Aktenzeichen=V%20ZR%201/24)). Auch ein sichtbares Balkon-Solarmodul ist eine bauliche Veränderung (BGH, Urt. v. 18.07.2025 – V ZR 29/24, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-07-18&Aktenzeichen=V%20ZR%2029/24)).

### 4. Mängel am Gemeinschaftseigentum

- Gegenüber dem Mieter haftet der **Vermieter** für jeden Mangel der Mietsache — auch wenn er im Gemeinschaftseigentum liegt (Minderung § 536 BGB, Schadensersatz § 536a BGB). Er kann sich nicht auf die Untätigkeit der GdWE berufen.
- Gegenüber der **GdWE** hat der Eigentümer einen Anspruch auf ordnungsmäßige Erhaltung ([§ 18 Abs. 2, § 19 Abs. 2 Nr. 2 WEG](https://www.gesetze-im-internet.de/woeigg/__19.html)); durchsetzbar mit der Beschlussersetzungsklage (`/wohnungseigentumsrecht:beschlussersetzungsklage`).
- Unterlässt die GdWE eine erforderliche Maßnahme schuldhaft, kann sie dem Eigentümer auf **Schadensersatz** haften (BGH, Urt. v. 27.02.2026 – V ZR 18/25, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-02-27&Aktenzeichen=V%20ZR%2018/25)). Das ist keine verschuldensunabhängige Haftung: Ersatzfähig ist nur der Schaden ab dem Zeitpunkt, zu dem eine ordnungsmäßig handelnde GdWE die Maßnahme beschlossen und durchgeführt hätte; für Mietausfall gelten weitere Voraussetzungen `[unverifiziert – prüfen: Einzelheiten im Volltext]`. Mängelanzeige des Mieters daher unverzüglich an den Verwalter weiterleiten und dokumentieren.

### 5. Gebrauchsregelungen und Hausordnung

- Hausordnung und Gebrauchsregelungen der GdWE binden den Mieter **nicht automatisch**; im Mietvertrag ist eine dynamische Bezugnahme auf die jeweils geltende Hausordnung zu vereinbaren `[unverifiziert – prüfen: Reichweite dynamischer Verweisungsklauseln]`.
- Verstößt der Mieter gegen die Gemeinschaftsordnung (z. B. zweckwidrige Nutzung von Teileigentum), kann die GdWE vom **Eigentümer** verlangen, auf den Mieter einzuwirken, und ggf. unmittelbar gegen den Mieter auf Unterlassung vorgehen (§ 1004 BGB) `[unverifiziert – prüfen]`.

### 6. Verkauf und Kündigung nach Umwandlung

- **Vorkaufsrecht:** Werden vermietete Wohnräume verkauft, an denen **nach Überlassung** an den Mieter Wohnungseigentum begründet wurde, ist der Mieter zum Vorkauf berechtigt; Ausübung durch schriftliche Erklärung gegenüber dem Verkäufer ([§ 577 BGB](https://www.gesetze-im-internet.de/bgb/__577.html)).
- **Kündigungssperrfrist:** Der Erwerber kann sich auf Eigenbedarf oder Verwertungsinteresse erst **drei Jahre** nach der Veräußerung berufen, in Gebieten mit Landesverordnung bis zu **zehn Jahre** ([§ 577a BGB](https://www.gesetze-im-internet.de/bgb/__577a.html)); Einzelheiten `/mietrecht:eigenbedarfskuendigung`.

### 7. Ergebnis

Zuordnung jedes Punkts (WEG / Mietrecht / beides), Handlungsschritte in beide Richtungen, Fristen (§ 556 Abs. 3 BGB, § 45 WEG, § 15 WEG), Haftungsrisiken des Eigentümers.

## Quellen und Zitierweise

Verbindlich: [`../../references/zitierweise.md`](../../references/zitierweise.md).

### Statute

- [§ 15 WEG](https://www.gesetze-im-internet.de/woeigg/__15.html) (Pflichten Dritter), [§ 20 WEG](https://www.gesetze-im-internet.de/woeigg/__20.html), [§ 18 WEG](https://www.gesetze-im-internet.de/woeigg/__18.html), [§ 19 WEG](https://www.gesetze-im-internet.de/woeigg/__19.html)
- [§ 556 BGB](https://www.gesetze-im-internet.de/bgb/__556.html), [§ 556a BGB](https://www.gesetze-im-internet.de/bgb/__556a.html) (Abs. 3: vermietetes Wohnungseigentum), [§ 554 BGB](https://www.gesetze-im-internet.de/bgb/__554.html)
- [§ 536 BGB](https://www.gesetze-im-internet.de/bgb/__536.html), [§ 577 BGB](https://www.gesetze-im-internet.de/bgb/__577.html), [§ 577a BGB](https://www.gesetze-im-internet.de/bgb/__577a.html)

### Rechtsprechung

1. BGH, Urt. v. 27.02.2026 – V ZR 18/25 (Haftung der GdWE für unterlassene Maßnahmen), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-02-27&Aktenzeichen=V%20ZR%2018/25)
2. BGH, Urt. v. 18.07.2025 – V ZR 29/24 (Balkon-Solarmodul als bauliche Veränderung), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-07-18&Aktenzeichen=V%20ZR%2029/24)
3. BGH, Urt. v. 21.03.2025 – V ZR 1/24 (Haftung des Vermieters für geduldete Veränderungen des Mieters), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-03-21&Aktenzeichen=V%20ZR%201/24)

### Kommentare

- Schmidt-Futterer/Lehmann-Richter, Mietrecht, 16. Aufl. 2024, § 556a BGB `[unverifiziert – prüfen: Bearbeiter und Rn.]`
- Bärmann/Dötsch, WEG, aktuelle Aufl., § 15 `[unverifiziert – prüfen: Auflage und Rn.]`

## Beispiel (Gutachtenstil, verkürzt)

**Sachverhalt.** Eigentümer V vermietet seine Wohnung seit 2019; der Mietvertrag regelt keinen Umlageschlüssel. Die WEG-Einzelabrechnung 2025 (beschlossen im Mai 2026) weist 3.400 EUR aus, darunter Verwaltervergütung 420 EUR, Rücklagenzuführung 600 EUR und eine Dachreparatur 380 EUR. Mieterin M hat Ende September 2026 ein Balkonkraftwerk montiert, das V „in Ordnung" fand. Seit März 2026 dringt über das Gemeinschaftsdach Wasser ein; M mindert um 10 %.

**Betriebskosten.** Mangels Vereinbarung gilt der WEG-Schlüssel (§ 556a Abs. 3 BGB). Herauszunehmen sind Verwaltervergütung, Rücklage und Reparatur (1.400 EUR); umlagefähig bleiben 2.000 EUR zuzüglich der Grundsteuer. Abrechnungsfrist gegenüber M: 31.12.2026.

**Balkonkraftwerk.** M hat einen Anspruch auf Erlaubnis (§ 554 BGB), V seinerseits auf Gestattung durch die GdWE (§ 20 Abs. 2 S. 1 Nr. 5 WEG). Ohne Gestattungsbeschluss droht V der Beseitigungsanspruch der GdWE (V ZR 29/24, V ZR 1/24). V muss die Gestattung sofort beantragen. ([V ZR 29/24](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-07-18&Aktenzeichen=V%20ZR%2029/24), [V ZR 1/24](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-03-21&Aktenzeichen=V%20ZR%201/24))

**Dach.** Gegenüber M ist die Minderung berechtigt. V verlangt von der GdWE die Sanierung. Schadensersatz für den Mietausfall kommt nicht ab März 2026 in Betracht, sondern erst ab dem Zeitpunkt, zu dem eine ordnungsmäßig handelnde GdWE nach der Anzeige über die Sanierung beschlossen und sie durchgeführt hätte; dieser Zeitraum ist zu dokumentieren (V ZR 18/25, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-02-27&Aktenzeichen=V%20ZR%2018/25)).

## Risiken / typische Fehler

- **WEG-Einzelabrechnung an den Mieter weitergereicht** → enthält nicht umlagefähige Positionen; Abrechnung ist materiell fehlerhaft.
- **Auf die WEG-Abrechnung gewartet** → die Zwölf-Monats-Frist des § 556 Abs. 3 BGB läuft unabhängig davon.
- **Mieter-Umbau ohne Gestattungsbeschluss erlaubt** → der Eigentümer haftet der GdWE auf Beseitigung (BGH V ZR 1/24). ([V ZR 1/24](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-03-21&Aktenzeichen=V%20ZR%201/24))
- **Minderung an die GdWE „durchgereicht"** → gegenüber dem Mieter haftet allein der Vermieter; Rückgriff nur über Schadensersatz gegen die GdWE bei Verschulden und erst ab dem Zeitpunkt, zu dem ordnungsmäßig gehandelt worden wäre (BGH V ZR 18/25). ([V ZR 18/25](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-02-27&Aktenzeichen=V%20ZR%2018/25))
- **Duldung ohne Ankündigung verlangt** → § 15 WEG verlangt rechtzeitige Ankündigung, bei Modernisierungen drei Monate vorher in Textform.
- **Glasfaser über § 554 BGB verlangt** → nicht erfasst; nur im WEG privilegiert.
- **§ 577a BGB übersehen** → Eigenbedarfskündigung nach Umwandlung innerhalb der Sperrfrist unwirksam.

## Ausgabeformat

```
VERMIETETE EIGENTUMSWOHNUNG — SCHNITTSTELLENPRÜFUNG (Rechtsstand Oktober 2026)

| Thema | WEG (Eigentümer ↔ GdWE) | Mietrecht (Vermieter ↔ Mieter) | Handlung / Frist |
|---|---|---|---|
| Betriebskosten | Einzelabrechnung <Jahr> | § 556a Abs. 3 BGB Schlüssel; umlagefähig <EUR> | Abrechnung bis <Datum> |
| Erhaltung/Modernisierung | Beschluss <Nr.> | Duldung § 15 WEG; § 559 BGB? | Ankündigung <Datum> |
| bauliche Veränderung | Gestattung § 20 Abs. 2 WEG | Erlaubnis § 554 BGB | Antrag GdWE <Datum> |
| Mangel Gemeinschaftseigentum | Anspruch § 19 Abs. 2 Nr. 2 / Schadensersatz | Minderung § 536 BGB | Anzeige an Verwalter <Datum> |
| Verkauf/Kündigung | — | §§ 577, 577a BGB | Sperrfrist bis <Datum> |

Haftungsrisiken des Eigentümers: <…>
```
