---
name: bauliche-veraenderung
description: "Einordnung einer baulichen Veränderung im Wohnungseigentum nach der WEMoG-Reform – Beschluss oder Gestattungsbeschluss mit einfacher Mehrheit § 20 Abs. 1 WEG (Beschlusszwang auch in der Zweiergemeinschaft), privilegierter Anspruch auf Barrierefreiheit, E-Mobilität, Einbruchsschutz, Glasfaser und Steckersolargeräte § 20 Abs. 2 WEG (Steckersolar seit 17.10.2024), Gestattungsanspruch bei Einverständnis aller Beeinträchtigten § 20 Abs. 3 WEG, Grenzen § 20 Abs. 4 WEG, Kosten und Nutzungen § 21 Abs. 1–5 WEG, Duldungspflicht von Mietern § 15 WEG. Rechtsstand: Oktober 2026. Use when eine geplante oder bereits ausgeführte bauliche Maßnahme eines Wohnungseigentümers auf Beschlusserfordernis, privilegierten Anspruch, Beseitigung und Kostentragung geprüft wird."
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

# /wohnungseigentumsrecht:bauliche-veraenderung

## Zweck

Mit dem Wohnungseigentumsmodernisierungsgesetz (**WEMoG**, in Kraft seit 01.12.2020) wurde das Recht der baulichen Veränderung grundlegend umgebaut. Unter dem alten § 22 WEG bedurfte eine bauliche Veränderung im Grundsatz der Zustimmung aller beeinträchtigten Eigentümer — faktisch oft Allstimmigkeit. Seit der Reform können bauliche Veränderungen **beschlossen oder einem Eigentümer durch Beschluss gestattet** werden; es genügt die **einfache Mehrheit** der abgegebenen Stimmen ([§ 20 Abs. 1 WEG](https://www.gesetze-im-internet.de/woeigg/__20.html), [§ 25 Abs. 1 WEG](https://www.gesetze-im-internet.de/woeigg/__25.html)).

Daneben bestehen **privilegierte Maßnahmen**, auf die der einzelne Eigentümer einen Anspruch hat ([§ 20 Abs. 2 WEG](https://www.gesetze-im-internet.de/woeigg/__20.html)), sowie ein Gestattungsanspruch, wenn alle Beeinträchtigten einverstanden sind (§ 20 Abs. 3 WEG). Dieser Skill ordnet eine Maßnahme ein, bestimmt den Weg zur Gestattung, prüft Grenzen und Beseitigungsrisiken und klärt Kosten und Nutzungen ([§ 21 WEG](https://www.gesetze-im-internet.de/woeigg/__21.html)).

**Rechtsstand: Oktober 2026.** Letzte Änderung des § 20 WEG durch G v. 10.10.2024 (BGBl. 2024 I Nr. 306): **Steckersolargeräte** als fünfte privilegierte Maßnahme seit **17.10.2024**. Der V. Zivilsenat hat 2024–2026 den **Beschlusszwang** auch für ausgeführte Maßnahmen bekräftigt. Das GModG (seit 29.07.2026) ändert das WEG nicht; die früheren Sonderregeln für Gemeinschaften mit Etagenheizungen (§§ 71l und 71n der früheren GEG-Fassung) sind entfallen, ein Heizungstausch folgt den allgemeinen Regeln der §§ 19–21 WEG.

## Eingaben

- geplante oder bereits ausgeführte Maßnahme (genaue Beschreibung, Ort am Gemeinschafts- oder Sondereigentum, Sichtbarkeit von außen)
- Antragsteller (einzelner Eigentümer / mehrere / Verwalter / Mieter des Eigentümers)
- privilegierte Kategorie (Barrierefreiheit, E-Mobilität, Einbruchsschutz, Glasfaser, Steckersolar)?
- Beeinträchtigung anderer Eigentümer (optisch, baulich, Lärm, Nutzung)
- Kosten und wer sie zu tragen bereit ist
- Gemeinschaftsordnung (Öffnungsklauseln, abweichende Kostenregeln), frühere Beschlüsse
- Anzahl der Einheiten (Zweiergemeinschaft?)

## Sub-Agent-Architektur

Researcher liefert die Normfassung der §§ 20, 21 WEG nach WEMoG und die verifizierte Rechtsprechung des V. Zivilsenats. Drafter erstellt die Einordnung samt Beschlussvorschlag und Kostenfolge. Reviewer prüft Beschlusserfordernis, Grenzen des § 20 Abs. 4 WEG, Beseitigungsrisiko und Schlüssigkeit der Kostenverteilung.

## Ablauf

### 1. Einordnung: Erhaltung oder bauliche Veränderung?

Eine **Erhaltungsmaßnahme** (Instandhaltung/Instandsetzung, [§ 19 Abs. 2 Nr. 2 WEG](https://www.gesetze-im-internet.de/woeigg/__19.html)) ist Gemeinschaftsaufgabe und folgt dem allgemeinen Kostenschlüssel. Eine **bauliche Veränderung** ist jede Maßnahme, die über die ordnungsmäßige Erhaltung des gemeinschaftlichen Eigentums hinausgeht (§ 20 Abs. 1 WEG).

- Auch eine **von außen sichtbare Anlage ohne Substanzeingriff** — etwa ein am Balkongeländer befestigtes Solarmodul — ist eine bauliche Veränderung (BGH, Urt. v. 18.07.2025 – V ZR 29/24, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-07-18&Aktenzeichen=V%20ZR%2029/24)).
- Die GdWE darf die Erhaltung von Bauteilen wie Balkonen beschließen, auch wenn die Teilungserklärung die Erhaltung den einzelnen Eigentümern zuweist; wird sie selbst tätig, **verbleibt es bei der vereinbarten Kostenlast** der einzelnen Eigentümer (BGH, Urt. v. 24.04.2026 – V ZR 102/24, Leitsätze a und b, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-04-24&Aktenzeichen=V%20ZR%20102/24), [Volltext](https://www.rws-verlag.de/fileadmin/Volltexte-4/V_ZR_102-24.pdf)).

### 2. Beschlusszwang und Gestattungsbeschluss (§ 20 Abs. 1 WEG)

Bauliche Veränderungen werden **durch Beschluss** legitimiert — entweder als Maßnahme der Gemeinschaft oder als **Gestattungsbeschluss** zugunsten eines Eigentümers. Es genügt die **einfache Mehrheit** der abgegebenen Stimmen.

- **Beschlusszwang:** Ohne vorherigen Beschluss darf auch der Anspruchsberechtigte nicht bauen. Das gilt auch in der **Zweiergemeinschaft**; der Beschlusszwang ist allerdings durch Vereinbarung abdingbar (BGH, Urt. v. 12.06.2026 – V ZR 68/25, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-06-12&Aktenzeichen=V%20ZR%2068/25)).
- **Eigenmacht rächt sich:** Wer eigenmächtig baut, kann dem Beseitigungsanspruch der GdWE nicht entgegenhalten, er habe einen Anspruch auf Gestattung; ein vermietender Eigentümer haftet für Veränderungen, die sein Mieter mit seiner Erlaubnis oder Duldung vornimmt (BGH, Urt. v. 21.03.2025 – V ZR 1/24, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-03-21&Aktenzeichen=V%20ZR%201/24)).
- **Bestimmtheit bei offener Gestaltung:** Beschließen die Eigentümer eine Fassadengestaltung durch eine namentlich genannte Künstlerin, ist der Beschluss hinreichend bestimmt, wenn er die zu gestaltende **Fläche**, die **Kostentragung** und die **Dauer** des Verbleibs regelt; wie das Werk konkret aussehen wird, muss er nicht beschreiben. Eine Veränderung des optischen Gesamteindrucks ist regelmäßig **keine grundlegende Umgestaltung** i. S. d. § 20 Abs. 4 Alt. 1 WEG (BGH, Urt. v. 25.09.2026 – V ZR 165/25, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-09-25&Aktenzeichen=V%20ZR%20165/25), [Volltext](https://www.rws-verlag.de/fileadmin/Volltexte-4/V_ZR_165-25.pdf)).

### 3. Privilegierter Anspruch (§ 20 Abs. 2 WEG)

Jeder Eigentümer kann **angemessene** bauliche Veränderungen verlangen, die einer der fünf **privilegierte Maßnahmen** dienen:

| Nr. | Privilegierte Maßnahme | Beispiel |
|---|---|---|
| 1 | **Barrierefreiheit** (Gebrauch durch Menschen mit Behinderungen) | Rampe, Treppenlift, Außenaufzug |
| 2 | **E-Mobilität** — Laden elektrisch betriebener Fahrzeuge | Wallbox/Ladepunkt in der Tiefgarage |
| 3 | **Einbruchsschutz** | Sicherheitstür, Gitter, Zusatzschlösser |
| 4 | **Anschluss an ein Telekommunikationsnetz mit sehr hoher Kapazität** | Glasfaser-Hausanschluss |
| 5 | **Steckersolargeräte** (seit 17.10.2024) | Balkonkraftwerk |

- Es besteht ein **Anspruch dem Grunde nach**; die Gemeinschaft kann das „Ob" nicht ablehnen. Über die **Durchführung** (das „Wie") ist im Rahmen ordnungsmäßiger Verwaltung zu beschließen (§ 20 Abs. 2 S. 2 WEG).
- **Barrierefreiheit** hat Gewicht: Barrierereduzierende Maßnahmen sind nach der Reform auch gegen die Mehrheit durchsetzbar; die Angemessenheitsgrenze ist eng auszulegen (BGH, Urt. v. 09.02.2024 – V ZR 244/22, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-02-09&Aktenzeichen=V%20ZR%20244/22)).
- Der Anspruch richtet sich auf einen **Gestattungsbeschluss**; ohne ihn bleibt das Gerät beseitigungspflichtig (BGH V ZR 29/24). Bei Weigerung: Beschlussersetzungsklage (`/wohnungseigentumsrecht:beschlussersetzungsklage`). ([V ZR 29/24](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-07-18&Aktenzeichen=V%20ZR%2029/24))

### 4. Gestattungsanspruch bei Einverständnis aller Beeinträchtigten (§ 20 Abs. 3 WEG)

Jeder Eigentümer kann verlangen, dass ihm eine bauliche Veränderung **gestattet** wird, wenn alle Eigentümer einverstanden sind, deren Rechte durch die Maßnahme über das **bei einem geordneten Zusammenleben unvermeidliche Maß** hinaus beeinträchtigt werden ([§ 20 Abs. 3 WEG](https://www.gesetze-im-internet.de/woeigg/__20.html); Maßstab wie [§ 14 Abs. 1 Nr. 2 WEG](https://www.gesetze-im-internet.de/woeigg/__14.html)).

- Die Befürchtung späterer Störungen (Lärm) spielt bei der Gestattung grundsätzlich keine Rolle; sie ist erst bei der **Grenze des § 20 Abs. 4 Alt. 2 WEG** und dort nur zu berücksichtigen, wenn die unbillige Benachteiligung durch den späteren Gebrauch schon bei der Gestattung evident ist (unten Nr. 5). In diese Linie fügt sich die Entscheidung zum **Split-Klimagerät** auf dem Balkon: Die Gestattung kann grundsätzlich verlangt werden, gegen Lärm kann die Gemeinschaft gesondert vorgehen (BGH, Urt. v. 17.07.2026 – V ZR 162/25, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-07-17&Aktenzeichen=V%20ZR%20162/25)).
- Eine Fassadendurchbohrung oder ein Wanddurchbruch beeinträchtigt die übrigen Eigentümer nicht ohne Weiteres; es kommt auf den Einzelfall an (BGH, Urt. v. 14.02.2025 – V ZR 86/24, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-02-14&Aktenzeichen=V%20ZR%2086/24)).

### 5. Grenzen (§ 20 Abs. 4 WEG)

Bauliche Veränderungen, die die Wohnanlage **grundlegend umgestalten** oder einen Eigentümer **ohne sein Einverständnis** gegenüber anderen **unbillig benachteiligen**, dürfen nicht beschlossen und gestattet werden; sie können auch nicht verlangt werden ([§ 20 Abs. 4 WEG](https://www.gesetze-im-internet.de/woeigg/__20.html)). Die Schranke gilt auch für privilegierte Maßnahmen. Bei der **unbilligen Benachteiligung** (Alt. 2) zählen grundsätzlich nur die **unmittelbar** mit der Maßnahme verbundenen Auswirkungen, nicht die des späteren Gebrauchs (z. B. tieffrequenter Schall einer Klimaanlage), es sei denn, die Benachteiligung durch den Gebrauch ist schon bei der Gestattung evident; die Bestandskraft der Gestattung schließt spätere Abwehransprüche wegen Immissionen nicht aus (BGH, Urt. v. 28.03.2025 – V ZR 105/24, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-03-28&Aktenzeichen=V%20ZR%20105/24), [Volltext](https://www.rws-verlag.de/fileadmin/Volltexte-4/v_zr_105-24.pdf)). Ein Verstoß macht den Beschluss anfechtbar; ob er nichtig macht, ist im Einzelfall zu prüfen `[unverifiziert – prüfen]`.

### 6. Kosten und Nutzungen (§ 21 WEG)

| Fall | Kostenträger und Nutzungen | Norm |
|---|---|---|
| Maßnahme einem Eigentümer **gestattet** oder **auf sein Verlangen nach § 20 Abs. 2** durchgeführt | dieser Eigentümer allein; nur ihm gebühren die Nutzungen | [§ 21 Abs. 1 WEG](https://www.gesetze-im-internet.de/woeigg/__21.html) |
| beschlossen mit **mehr als zwei Dritteln** der abgegebenen Stimmen **und** der Hälfte aller Miteigentumsanteile (außer bei unverhältnismäßigen Kosten) | **alle** nach Miteigentumsanteilen; Nutzungen nach § 16 Abs. 1 WEG | § 21 Abs. 2 S. 1 Nr. 1 WEG |
| Kosten **amortisieren** sich in angemessenem Zeitraum | **alle** nach Miteigentumsanteilen | § 21 Abs. 2 S. 1 Nr. 2 WEG |
| sonstige beschlossene Maßnahmen | nur die **Zustimmenden** nach ihren Anteilen; ihnen gebühren die Nutzungen | § 21 Abs. 3 WEG |
| späterer Mitnutzer | Gestattung gegen angemessenen Ausgleich | § 21 Abs. 4 WEG |
| abweichende Verteilung | durch Beschluss möglich, aber **keine Kosten für Eigentümer, die nach Abs. 1–4 nichts tragen** | § 21 Abs. 5 WEG |

### 7. Mieter und Nutzer

Wer Wohnungseigentum gebraucht, ohne Eigentümer zu sein, hat Erhaltungsmaßnahmen nach rechtzeitiger Ankündigung und sonstige Maßnahmen nach Ankündigung in **Textform drei Monate vor Beginn** zu dulden ([§ 15 WEG](https://www.gesetze-im-internet.de/woeigg/__15.html)). Zur Schnittstelle mit dem Mietrecht (§ 554 BGB): `/wohnungseigentumsrecht:vermietete-eigentumswohnung`.

### 8. Beschlussvorschlag und Ergebnis

Drafter formuliert einen abstimmungsreifen Beschlussantrag: Gegenstand, Ausführung („Wie"), Kostenträger nach § 21 WEG, Nutzungszuordnung, Erhaltungs- und Rückbaupflicht, Haftung. Ergebnis: Einordnung, erforderlicher Beschluss, privilegierter Anspruch ja/nein, Grenzen, Kostenfolge, Beseitigungsrisiko bei Eigenmacht.

## Quellen und Zitierweise

Verbindlich: [`../../references/zitierweise.md`](../../references/zitierweise.md).

### Statute

- [§ 20 WEG](https://www.gesetze-im-internet.de/woeigg/__20.html) (bauliche Veränderungen — Abs. 1 Beschluss/Gestattung, Abs. 2 privilegierte Maßnahmen, Abs. 3 Gestattungsanspruch, Abs. 4 Grenzen)
- [§ 21 WEG](https://www.gesetze-im-internet.de/woeigg/__21.html) (Nutzungen und Kosten bei baulichen Veränderungen)
- [§ 19 WEG](https://www.gesetze-im-internet.de/woeigg/__19.html) (ordnungsmäßige Erhaltung — Abgrenzung), [§ 14 WEG](https://www.gesetze-im-internet.de/woeigg/__14.html) (Maßstab der Beeinträchtigung), [§ 15 WEG](https://www.gesetze-im-internet.de/woeigg/__15.html) (Duldungspflicht von Nutzern)

### Rechtsprechung (V. Zivilsenat)

1. BGH, Urt. v. 25.09.2026 – V ZR 165/25 (Bestimmtheit eines Gestaltungsbeschlusses; optische Veränderung keine grundlegende Umgestaltung), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-09-25&Aktenzeichen=V%20ZR%20165/25), [Volltext](https://www.rws-verlag.de/fileadmin/Volltexte-4/V_ZR_165-25.pdf)
2. BGH, Urt. v. 17.07.2026 – V ZR 162/25 (Split-Klimagerät auf dem Balkon), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-07-17&Aktenzeichen=V%20ZR%20162/25)
3. BGH, Urt. v. 12.06.2026 – V ZR 68/25 (Beschlusszwang in der Zweiergemeinschaft), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-06-12&Aktenzeichen=V%20ZR%2068/25)
4. BGH, Urt. v. 24.04.2026 – V ZR 102/24 (Versäumnisurteil; Beschlusskompetenz und Pflicht der GdWE zur Balkonsanierung, Kostenlast bleibt bei den Eigentümern), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-04-24&Aktenzeichen=V%20ZR%20102/24), [Volltext](https://www.rws-verlag.de/fileadmin/Volltexte-4/V_ZR_102-24.pdf)
5. BGH, Urt. v. 18.07.2025 – V ZR 29/24 (Balkon-Solarmodul als bauliche Veränderung), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-07-18&Aktenzeichen=V%20ZR%2029/24)
6. BGH, Urt. v. 28.03.2025 – V ZR 105/24 (Klimaanlage: für § 20 Abs. 4 Alt. 2 WEG nur unmittelbare Auswirkungen; Bestandskraft der Gestattung schließt Immissionsabwehr nicht aus), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-03-28&Aktenzeichen=V%20ZR%20105/24), [Volltext](https://www.rws-verlag.de/fileadmin/Volltexte-4/v_zr_105-24.pdf)
7. BGH, Urt. v. 21.03.2025 – V ZR 1/24 (kein Gestattungseinwand gegen Beseitigung; Haftung für Mieter), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-03-21&Aktenzeichen=V%20ZR%201/24)
8. BGH, Urt. v. 14.02.2025 – V ZR 86/24 (Fassadendurchbohrung; Vorbefassung), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-02-14&Aktenzeichen=V%20ZR%2086/24)
9. BGH, Urt. v. 09.02.2024 – V ZR 244/22 (Barrierefreiheit, Außenaufzug), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-02-09&Aktenzeichen=V%20ZR%20244/22)

### Kommentare

- Hügel/Elzer, WEG, aktuelle Aufl., § 20 `[unverifiziert – prüfen: Auflage und Rn.]`
- Bärmann/Dötsch, WEG, aktuelle Aufl., §§ 20, 21 `[unverifiziert – prüfen: Auflage und Rn.]`

## Beispiel (Gutachtenstil, verkürzt)

**Sachverhalt.** Eigentümer W will auf eigene Kosten eine Wallbox an seinem Stellplatz in der Tiefgarage installieren. Die Mehrheit lehnt ab, weil die Hauszuleitung „irgendwann" verstärkt werden müsse.

**Anspruch.** Die Wallbox dient dem Laden elektrisch betriebener Fahrzeuge (§ 20 Abs. 2 S. 1 Nr. 2 WEG). W hat einen Anspruch auf Gestattung dem Grunde nach; die Mehrheit kann nur über das „Wie" entscheiden (Leitungsführung, Lastmanagement, Fachbetrieb). Eine grundlegende Umgestaltung (§ 20 Abs. 4 WEG) liegt nicht vor.

**Kosten.** W trägt die Kosten allein, ihm gebühren die Nutzungen (§ 21 Abs. 1 WEG). Wird später ein gemeinschaftliches Lastmanagement beschlossen, kann W sich gegen angemessenen Ausgleich anschließen (§ 21 Abs. 4 WEG).

**Ergebnis.** Ablehnungsbeschluss anfechten und mit der Beschlussersetzungsklage verbinden; bis zum Gestattungsbeschluss **nicht** eigenmächtig installieren (BGH V ZR 1/24). ([V ZR 1/24](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-03-21&Aktenzeichen=V%20ZR%201/24))

## Risiken / typische Fehler

- **Allstimmigkeit angenommen** — veraltet. Seit WEMoG genügt die einfache Mehrheit (§ 20 Abs. 1 WEG).
- **Ohne Beschluss gebaut** — auch bei privilegierter Maßnahme droht Beseitigung; der Gestattungsanspruch ist kein Einwand (BGH V ZR 1/24, V ZR 29/24). Gilt auch in der Zweiergemeinschaft (BGH V ZR 68/25). ([V ZR 1/24](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-03-21&Aktenzeichen=V%20ZR%201/24), [V ZR 29/24](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-07-18&Aktenzeichen=V%20ZR%2029/24), [V ZR 68/25](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-06-12&Aktenzeichen=V%20ZR%2068/25))
- **„Ob" und „Wie" verwechselt** — bei privilegierten Maßnahmen besteht ein Anspruch auf das „Ob"; nur über die Durchführung beschließt die Gemeinschaft.
- **Steckersolargeräte vergessen** — seit 17.10.2024 privilegiert (§ 20 Abs. 2 S. 1 Nr. 5 WEG).
- **Grenze § 20 Abs. 4 WEG übersehen** — auch privilegierte Maßnahmen scheitern an grundlegender Umgestaltung oder unbilliger Benachteiligung.
- **Kostenverteilung falsch** — wer gestattet bekommt, zahlt allein (§ 21 Abs. 1 WEG); sonst tragen nur die Zustimmenden (Abs. 3), alle nur bei Abs. 2. Ein abweichender Beschluss darf Nichtzahlern keine Kosten auferlegen (Abs. 5).
- **Spätere Lärmbefürchtung als Ablehnungsgrund** — für die Gestattung zählen die unmittelbaren Auswirkungen (BGH V ZR 162/25). ([V ZR 162/25](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-07-17&Aktenzeichen=V%20ZR%20162/25))
- **Beschluss zu unbestimmt** — Standort, Ausführung, Kostenträger und Erhaltung regeln, sonst anfechtbar.

## Ausgabeformat

```
EINORDNUNG BAULICHE VERÄNDERUNG (§§ 20, 21 WEG, Rechtsstand Oktober 2026)

1. Maßnahme: <Beschreibung; bereits ausgeführt? ja/nein>
2. Einordnung: [ ] Erhaltung  [ ] bauliche Veränderung
3. Weg zur Legitimation:
   [ ] Beschluss/Gestattung § 20 Abs. 1 (einfache Mehrheit)
   [ ] privilegiert § 20 Abs. 2: [Barrierefreiheit] [E-Mobilität] [Einbruchsschutz]
       [Glasfaser] [Steckersolargeräte]
   [ ] Gestattungsanspruch § 20 Abs. 3 (alle Beeinträchtigten einverstanden)
4. Grenzen § 20 Abs. 4: grundlegende Umgestaltung? / unbillige Benachteiligung?
5. Kosten und Nutzungen § 21: [Abs. 1] [Abs. 2 Nr. 1] [Abs. 2 Nr. 2] [Abs. 3] [Abs. 5]
6. Beseitigungsrisiko bei Eigenmacht: <…>
7. Beschlussvorschlag: <Gegenstand, Ausführung, Kostenträger, Nutzung, Erhaltung>
8. Prozessual: Anfechtung / Beschlussersetzungsklage <Frist § 45 WEG>
```
