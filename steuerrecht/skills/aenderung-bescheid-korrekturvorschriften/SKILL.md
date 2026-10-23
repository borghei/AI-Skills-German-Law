---
name: aenderung-bescheid-korrekturvorschriften
description: "Korrektur bestandskräftiger oder noch offener Steuerbescheide zugunsten oder zulasten des Steuerpflichtigen – offenbare Unrichtigkeit § 129 AO, Vorbehalt der Nachprüfung § 164 AO, vorläufige Festsetzung § 165 AO, schlichter Änderungsantrag § 172 Abs. 1 S. 1 Nr. 2 a AO, neue Tatsachen § 173 AO (grobes Verschulden), Schreib- und Rechenfehler § 173a AO, widerstreitende Festsetzungen § 174 AO, Grundlagenbescheid und rückwirkendes Ereignis § 175 AO, Datenübermittlung § 175b AO, Vertrauensschutz § 176 AO, Mitberichtigung § 177 AO, Festsetzungsverjährung §§ 169–171 AO. Rechtsstand Oktober 2026. Use when die Einspruchsfrist abgelaufen ist oder geprüft wird, ob und auf welcher Grundlage ein Steuerbescheid noch geändert werden kann."
language: de
provider_variants:
  - claude
  - gemini
  - openai
test: ./test.md
---

# /steuerrecht:aenderung-bescheid-korrekturvorschriften

> **Rechtsstand: Oktober 2026.** Die Korrekturvorschriften der §§ 129, 164, 165, 172–177 AO sind 2025–2026 nicht geändert worden. Neu für die Verjährung ist die Fünf-Jahres-Grenze der Ablaufhemmung nach Außenprüfung (§ 171 Abs. 4 S. 3 AO, für nach dem 31.12.2024 entstandene Steuern). Entwurf JStG 2026 (BT-Drs. 21/8283, nicht verabschiedet): Die Gesamtaufrollung im Einspruch soll vom Pflicht- zum Prüfungsrecht werden (§ 367 Abs. 2 S. 1 AO) — damit gewinnt die punktgenaue Korrekturnorm noch an Gewicht.

## Zweck

Nach Ablauf der Einspruchsfrist ist ein Steuerbescheid bestandskräftig. Geändert werden kann er nur, wenn eine **Korrekturnorm** greift und die **Festsetzungsfrist** noch läuft. Umgekehrt muss der Mandant wissen, ob das Finanzamt einen für ihn günstigen Bescheid noch zu seinen Lasten ändern darf. Dieser Skill prüft die Korrekturnormen in der Reihenfolge ihrer praktischen Reichweite, die Festsetzungsfrist und die Mitberichtigung und formuliert Änderungsantrag oder Abwehr.

## Eingaben

- Bescheid (Art, Jahr, Datum, Bekanntgabe), Nebenbestimmungen (Vorbehalt § 164, Vorläufigkeitsvermerk § 165 mit Umfang)
- Ist die Einspruchsfrist abgelaufen? Liegt ein Einspruch vor?
- Fehlerart: Schreib-/Rechenfehler, vergessene Angabe, neue Belege, Rechtsfehler des Finanzamts, geänderter Grundlagenbescheid, rückwirkendes Ereignis, Datenübermittlung Dritter
- Zeitpunkt, zu dem der Mandant / das Finanzamt die Tatsache kannte oder kennen musste
- Abgabedatum der Erklärung, Außenprüfung, Rechtsbehelfe (für die Festsetzungsfrist)

## Sub-Agent-Architektur

Ein **Verjährungs-Prüfer** berechnet zuerst die Festsetzungsfrist mit allen Anlauf- und Ablaufhemmungen — ist sie abgelaufen, endet die Prüfung (§ 169 Abs. 1 S. 1 AO). Ein **Korrekturnorm-Prüfer** durchläuft die Normen nach Reichweite. Ein **Verschuldens-Prüfer** bewertet bei § 173 Abs. 1 Nr. 2 AO das grobe Verschulden. Ein **Saldierungs-Prüfer** prüft, welche gegenläufigen Fehler nach § 177 AO mitzuberichtigen sind.

## Ablauf

### 1. Festsetzungsfrist zuerst ([§ 169 AO](https://www.gesetze-im-internet.de/ao_1977/__169.html), [§ 170 AO](https://www.gesetze-im-internet.de/ao_1977/__170.html), [§ 171 AO](https://www.gesetze-im-internet.de/ao_1977/__171.html))

- Dauer: **vier Jahre** (Regel), **fünf Jahre** bei leichtfertiger Verkürzung, **zehn Jahre** bei Hinterziehung (§ 169 Abs. 2 AO).
- Beginn: mit Ablauf des Jahres der Steuerentstehung; bei Erklärungspflicht **Anlaufhemmung** bis zum Ablauf des Jahres der Abgabe, längstens drei Jahre (§ 170 Abs. 2 S. 1 Nr. 1 AO).
- Wichtige **Ablaufhemmungen**: Antrag auf Änderung vor Fristablauf (§ 171 Abs. 3 AO), Einspruch/Klage (Abs. 3a), Außenprüfung (Abs. 4 — mit Fünf-Jahres-Grenze für Steuern ab 2025), Steuerfahndung (Abs. 5), Grundlagenbescheid: zwei Jahre nach dessen Bekanntgabe (Abs. 10), Datenübermittlung Dritter (Abs. 10a).
- Fristwahrung durch das Finanzamt: Der Bescheid muss den Bereich der Behörde vor Fristablauf verlassen haben bzw. bei Datenabruf bereitgestellt sein (§ 169 Abs. 1 S. 3 AO).

### 2. Offenbare Unrichtigkeit ([§ 129 AO](https://www.gesetze-im-internet.de/ao_1977/__129.html))

- Schreibfehler, Rechenfehler und **ähnliche offenbare Unrichtigkeiten** beim Erlass des Verwaltungsakts — mechanische Versehen, nicht Fehler in der Rechtsanwendung oder Sachverhaltsermittlung.
- Auch die Übernahme offenbarer Fehler aus der Erklärung durch das Finanzamt kann erfasst sein, wenn das Finanzamt sie als eigene übernimmt; jede ernsthafte Möglichkeit eines Rechts- oder Ermittlungsfehlers schließt § 129 AO aus (st. Rspr. `[unverifiziert – prüfen]`).
- Berichtigung jederzeit innerhalb der Festsetzungsfrist; Ablaufhemmung: Die Festsetzungsfrist endet insoweit nicht vor Ablauf eines Jahres nach Bekanntgabe des fehlerhaften Bescheids (§ 171 Abs. 2 S. 1 AO; ebenso für § 173a AO, § 171 Abs. 2 S. 2 AO). Zugunsten wie zulasten.

### 3. Vorbehalt der Nachprüfung ([§ 164 AO](https://www.gesetze-im-internet.de/ao_1977/__164.html)) und Vorläufigkeit ([§ 165 AO](https://www.gesetze-im-internet.de/ao_1977/__165.html))

- **Vorbehalt**: Solange er besteht, ist der Bescheid **in vollem Umfang** änderbar — auf Antrag des Steuerpflichtigen jederzeit (§ 164 Abs. 2 AO); er entfällt mit Ablauf der Festsetzungsfrist (§ 164 Abs. 4 AO) und ist nach einer Außenprüfung aufzuheben (§ 164 Abs. 3 S. 3 AO). Typisch bei Steueranmeldungen (USt-Voranmeldung, LSt-Anmeldung: § 168 AO).
- **Vorläufigkeit**: nur **im Umfang des Vorläufigkeitsvermerks** (z. B. Verfassungsmäßigkeit einer Norm nach Musterverfahren); Änderung, sobald die Ungewissheit beseitigt ist; Ablaufhemmung ein Jahr nach Kenntnis der Behörde von der Beseitigung der Ungewissheit (§ 171 Abs. 8 AO). Vermerk genau lesen — er deckt nicht den Streitpunkt des Mandanten, wenn dieser anders gelagert ist.

### 4. Schlichter Änderungsantrag ([§ 172 Abs. 1 S. 1 Nr. 2 a AO](https://www.gesetze-im-internet.de/ao_1977/__172.html))

- Änderung **zugunsten** des Steuerpflichtigen nur, wenn er **vor Ablauf der Einspruchsfrist** zugestimmt oder den Antrag gestellt hat; zulasten jederzeit mit Zustimmung.
- Vorteil: keine Gesamtaufrollung, kein Verböserungsrisiko. Nachteil: Der Antrag muss das Änderungsbegehren konkret bezeichnen; Nachschieben neuer Punkte nach Ablauf der Einspruchsfrist ist ausgeschlossen. Keine AdV.
- **Faustregel**: Bei unklarer Lage und knapper Zeit Einspruch statt schlichten Antrag — der Einspruch erlaubt Nachbesserung.
- § 172 Abs. 1 S. 1 Nr. 2 c AO: Rücknahme bei unlauteren Mitteln (Täuschung, Drohung, Bestechung) des Steuerpflichtigen.

### 5. Neue Tatsachen oder Beweismittel ([§ 173 AO](https://www.gesetze-im-internet.de/ao_1977/__173.html))

- **Tatsache**: Lebenssachverhalt (auch innere Tatsachen, Hilfstatsachen), nicht rechtliche Würdigung oder Schlussfolgerung.
- **Neu**: nachträglich bekannt geworden — maßgeblich ist der Kenntnisstand der zuständigen Veranlagungsstelle bei abschließender Zeichnung bzw. Freigabe des Bescheids. Verletzung der Ermittlungspflicht durch das Finanzamt kann einer Änderung zulasten nach Treu und Glauben entgegenstehen, wenn der Steuerpflichtige seine Mitwirkungspflichten erfüllt hat `[unverifiziert – prüfen]`.
- **Zulasten** (Nr. 1): ohne Verschuldensprüfung.
- **Zugunsten** (Nr. 2): nur, wenn den Steuerpflichtigen **kein grobes Verschulden** daran trifft, dass die Tatsache erst nachträglich bekannt wird — es sei denn, sie steht in unmittelbarem oder mittelbarem Zusammenhang mit einer Tatsache nach Nr. 1. Grobes Verschulden: Vorsatz und grobe Fahrlässigkeit, auch des Beraters; bei elektronischen Erklärungen ist das Übergehen ausdrücklicher Erklärungsfelder regelmäßig grob fahrlässig, das Übersehen unklarer Felder nicht ohne Weiteres `[unverifiziert – prüfen]`. Rechtsirrtum ist kein Verschulden in Bezug auf Tatsachen, kann aber zur Unkenntnis der Erheblichkeit führen.
- **Änderungssperre nach Außenprüfung** (§ 173 Abs. 2 AO): nur bei Hinterziehung oder leichtfertiger Verkürzung.

### 6. Schreib- und Rechenfehler des Steuerpflichtigen ([§ 173a AO](https://www.gesetze-im-internet.de/ao_1977/__173a.html))

- Änderung, soweit dem Steuerpflichtigen bei Erstellung der Erklärung **Schreib- oder Rechenfehler** unterlaufen sind und er deshalb der Behörde rechtserhebliche Tatsachen unzutreffend mitgeteilt hat — unabhängig von grobem Verschulden. Abgrenzung zum (nicht erfassten) Rechtsanwendungs- oder Übertragungsfehler mit Wertung.

### 7. Widerstreitende Festsetzung, Grundlagenbescheid, rückwirkendes Ereignis

- **§ 174 AO** ([Link](https://www.gesetze-im-internet.de/ao_1977/__174.html)): Ein Sachverhalt wurde mehrfach (Abs. 1) oder zu Unrecht gar nicht bzw. im falschen Jahr (Abs. 3, 4) berücksichtigt. Abs. 4: Wird ein Bescheid auf Rechtsbehelf oder Antrag zugunsten geändert, können die richtigen Folgerungen auch in anderen Jahren gezogen werden — **Risiko** bei Periodenverschiebungen.
- **§ 175 Abs. 1 S. 1 Nr. 1 AO** ([Link](https://www.gesetze-im-internet.de/ao_1977/__175.html)): Anpassung an einen erlassenen, geänderten oder aufgehobenen **Grundlagenbescheid** — Einwendungen gegen die Grundlage nur dort (§ 351 Abs. 2 AO).
- **§ 175 Abs. 1 S. 1 Nr. 2 AO**: **rückwirkendes Ereignis** mit steuerlicher Wirkung für die Vergangenheit (z. B. Ausfall einer Kaufpreisforderung bei § 17 EStG); Beginn der Festsetzungsfrist mit Ablauf des Jahres des Ereignisses.
- **§ 175b AO**: Änderung bei nachträglicher oder korrigierter Datenübermittlung Dritter (§ 93c AO), zugunsten und zulasten.

### 8. Vertrauensschutz ([§ 176 AO](https://www.gesetze-im-internet.de/ao_1977/__176.html)) und Mitberichtigung ([§ 177 AO](https://www.gesetze-im-internet.de/ao_1977/__177.html))

- § 176 AO: Bei Änderung darf zuungunsten nicht berücksichtigt werden, dass das BVerfG ein Gesetz für nichtig erklärt, ein oberster Gerichtshof eine Norm nicht anwendet oder seine Rspr. ändert, oder eine Verwaltungsvorschrift für nicht mit geltendem Recht vereinbar erklärt wird.
- § 177 AO: Bei jeder Änderung sind **materielle Fehler**, die nicht selbst Anlass der Änderung sind, **innerhalb des Änderungsrahmens** mitzuberichtigen — zugunsten wie zulasten. Vor jedem Antrag prüfen, welche gegenläufigen Fehler im Bescheid stecken.

### 9. Korrekturnormen-Kaskade (Prüfreihenfolge)

1. Einspruchsfrist offen? → **Einspruch** (`/steuerrecht:einspruch-finanzamt`), ggf. schlichter Antrag nach § 172 Abs. 1 S. 1 Nr. 2 a AO.
2. Vorbehalt der Nachprüfung? → **§ 164 Abs. 2 AO** (Vollrevision).
3. Vorläufigkeitsvermerk deckt den Punkt? → **§ 165 Abs. 2 AO**.
4. Mechanischer Fehler des Finanzamts? → **§ 129 AO**; des Steuerpflichtigen? → **§ 173a AO**.
5. Neue Tatsache? → **§ 173 Abs. 1 Nr. 2 AO** (grobes Verschulden prüfen).
6. Grundlagenbescheid / rückwirkendes Ereignis / Drittdaten? → **§§ 175, 175b AO**.
7. Doppel- oder Nichtberücksichtigung? → **§ 174 AO**.
8. Ergänzend: Rücknahme sonstiger Verwaltungsakte (§§ 130, 131 AO — nicht für Steuerbescheide, § 172 Abs. 1 S. 1 Nr. 2 d AO); Billigkeitserlass nach § 227 AO bei sachlicher Unbilligkeit (`/steuerrecht:stundung-erlass-vollstreckungsschutz`).

## Ausgabeformat

```
KORREKTURPRÜFUNG — <Mandant> — <Steuerart / Jahr> — <Datum> — Rechtsstand Oktober 2026

I.    Bescheid
      Datum / Bekanntgabe:            <…>
      Einspruchsfrist:                [offen bis … / abgelaufen]
      Nebenbestimmungen:              [Vorbehalt § 164 / Vorläufig § 165 (Umfang: …) / keine]

II.   Festsetzungsfrist
      Dauer (§ 169):                  <4 / 5 / 10 Jahre>
      Anlaufhemmung (§ 170):          <Abgabe am … → Beginn 31.12.…>
      Ablaufhemmungen (§ 171):        <…>
      Fristende:                      <…>

III.  Korrekturnorm
      § 129 / § 164 / § 165 / § 172 / § 173 / § 173a / § 174 / § 175 / § 175b: <einschlägig: … — Begründung>
      Grobes Verschulden (§ 173 Abs. 1 Nr. 2): [nein / ja / Zusammenhang Nr. 1]

IV.   Mitberichtigung (§ 177)
      Gegenläufige Fehler:            <… EUR>
      Saldo:                          <…>

V.    Vertrauensschutz (§ 176):       [relevant / —]

VI.   Empfehlung
      <Änderungsantrag nach § … / Abwehr der Änderung / Einspruch gegen Änderungsbescheid>
```

## Beispiel (Gutachtenstil, verkürzt)

M hat in der ESt-Erklärung 2022 (abgegeben 10.05.2023) Handwerkerleistungen von 6.000 EUR nicht angegeben, weil die Rechnung verlegt war; der Bescheid vom 14.07.2023 ist bestandskräftig und enthält keinen Vorbehalt. Die Rechnung taucht im Oktober 2026 auf. Die Festsetzungsfrist begann wegen der Anlaufhemmung mit Ablauf des 31.12.2023 und endet am 31.12.2027 (§§ 169 Abs. 2 S. 1 Nr. 2, 170 Abs. 2 S. 1 Nr. 1 AO). In Betracht kommt § 173 Abs. 1 Nr. 2 AO. Die Aufwendungen sind eine nachträglich bekannt gewordene Tatsache, die zu einer niedrigeren Steuer führt. Fraglich ist das grobe Verschulden: M wusste von den Aufwendungen und hat das ausdrücklich vorgesehene Erklärungsfeld nicht ausgefüllt. Das spricht für grobe Fahrlässigkeit; dass der Beleg verlegt war, entschuldigt nicht, weil die Angabe auch ohne Beleg möglich gewesen wäre. Ergebnis: Eine Änderung nach § 173 Abs. 1 Nr. 2 AO scheidet voraussichtlich aus; zu prüfen bleibt, ob § 129 oder § 173a AO greifen (nicht ersichtlich).

## Risiken / typische Fehler

- **Festsetzungsfrist nicht zuerst geprüft** — nach Fristablauf ist jede Korrektur ausgeschlossen; Anlaufhemmung und Ablaufhemmungen genau rechnen.
- **Schlichter Änderungsantrag zu spät oder zu unbestimmt** — zugunsten nur, wenn vor Ablauf der Einspruchsfrist gestellt; spätere Erweiterung ausgeschlossen.
- **Grobes Verschulden unterschätzt** — bei § 173 Abs. 1 Nr. 2 AO wird das Verschulden des Beraters zugerechnet; Erklärungsfelder in ELSTER sind Prüfmaßstab.
- **Vorläufigkeitsvermerk überschätzt** — er reicht nur so weit wie sein Wortlaut.
- **Mitberichtigung nach § 177 AO übersehen** — ein Änderungsantrag kann durch gegenläufige Fehler neutralisiert werden.
- **§ 174 Abs. 4 AO** — erfolgreiche Periodenverschiebung kann Folgeänderungen in anderen Jahren auslösen.
- **Grundlagen-Einwand am falschen Bescheid** — nur gegen den Grundlagenbescheid (§ 351 Abs. 2 AO, § 175 AO).
- **Änderungssperre nach Außenprüfung** (§ 173 Abs. 2 AO) übersehen — auch zugunsten des Finanzamts relevant.

## Quellen

### Statute

- [§ 129 AO](https://www.gesetze-im-internet.de/ao_1977/__129.html), [§ 164 AO](https://www.gesetze-im-internet.de/ao_1977/__164.html), [§ 165 AO](https://www.gesetze-im-internet.de/ao_1977/__165.html), [§ 168 AO](https://www.gesetze-im-internet.de/ao_1977/__168.html)
- [§ 172 AO](https://www.gesetze-im-internet.de/ao_1977/__172.html), [§ 173 AO](https://www.gesetze-im-internet.de/ao_1977/__173.html), [§ 173a AO](https://www.gesetze-im-internet.de/ao_1977/__173a.html), [§ 174 AO](https://www.gesetze-im-internet.de/ao_1977/__174.html), [§ 175 AO](https://www.gesetze-im-internet.de/ao_1977/__175.html), [§ 175b AO](https://www.gesetze-im-internet.de/ao_1977/__175b.html), [§ 176 AO](https://www.gesetze-im-internet.de/ao_1977/__176.html), [§ 177 AO](https://www.gesetze-im-internet.de/ao_1977/__177.html)
- [§ 169 AO](https://www.gesetze-im-internet.de/ao_1977/__169.html), [§ 170 AO](https://www.gesetze-im-internet.de/ao_1977/__170.html), [§ 171 AO](https://www.gesetze-im-internet.de/ao_1977/__171.html)
- [§ 351 AO](https://www.gesetze-im-internet.de/ao_1977/__351.html), [§ 367 AO](https://www.gesetze-im-internet.de/ao_1977/__367.html)

### Verwaltungsanweisungen

- AEAO zu §§ 129, 164, 165, 172–177 AO; BMF-Schreiben zum Vorläufigkeitskatalog (jeweils aktuelle Fassung) `[unverifiziert – prüfen]`

### Rechtsprechung (alle `[unverifiziert – prüfen]`)

- BFH-Linie zur „ähnlichen offenbaren Unrichtigkeit" bei Übernahme von Erklärungsfehlern — Az. in juris ermitteln (Suchstring: „§ 129 AO Übernahme offenbare Unrichtigkeit Steuererklärung")
- BFH-Linie zum groben Verschulden bei elektronisch abgegebenen Erklärungen — Suchstring: „§ 173 Abs. 1 Nr. 2 AO grobes Verschulden ELSTER Erklärungsfeld"

### Literatur

- von Wedelstädt, in: Gosch, AO/FGO, §§ 172 ff. AO `[unverifiziert – prüfen]`
- Loose, in: Tipke/Kruse, AO/FGO, § 173 AO `[unverifiziert – prüfen]`
