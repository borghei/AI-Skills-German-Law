---
name: haftungsbescheid
description: "Abwehr und Prüfung eines Haftungsbescheids des Finanzamts – Haftung der Geschäftsführer und Vertreter §§ 34, 35, 69 AO (Grundsatz anteiliger Tilgung, Sonderfall Lohnsteuer), Haftung des Steuerhinterziehers § 71 AO, Betriebsübernehmer § 75 AO, Organschaft § 73 AO, Arbeitgeberhaftung § 42d EStG, Haftungsbescheid und Ermessen § 191 AO, Festsetzungsfrist § 191 Abs. 3 AO, Akzessorietät § 191 Abs. 5 AO, Subsidiarität der Zahlungsaufforderung § 219 AO, Drittwirkung § 166 AO, Insolvenzlage und § 15b Abs. 8 InsO, Ressortaufteilung. Rechtsstand Oktober 2026. Use when ein Geschäftsführer, Vorstand, Liquidator oder Erwerber für Steuerschulden einer Gesellschaft oder eines Dritten in Anspruch genommen wird oder dies droht."
language: de
provider_variants:
  - claude
  - gemini
  - openai
test: ./test.md
---

# /steuerrecht:haftungsbescheid

> **Rechtsstand: Oktober 2026.** §§ 69 ff., 191, 219 AO und § 15b InsO sind 2025–2026 unverändert. Entwurf JStG 2026 (BT-Drs. 21/8283, nicht verabschiedet): Zuständigkeitsregeln bei Gesellschaften in Liquidation und „faktischer Liquidation" (§ 26 S. 3 Nr. 3, 4 AO-Entwurfsfassung; § 28 AO) — relevant für die Frage, welches Finanzamt den Haftungsbescheid erlassen darf.

## Zweck

Wird eine GmbH zahlungsunfähig, greift das Finanzamt auf die Geschäftsführer zu — mit einem eigenen Verwaltungsakt, dem Haftungsbescheid. Er ist ermessensgebunden, akzessorisch zur Steuerschuld und nur unter engen Voraussetzungen vollstreckbar. Dieser Skill prüft Haftungstatbestand, Verschulden, Kausalität und Ermessen, berechnet die Haftungsquote und bereitet Einspruch und AdV vor. Er dient zugleich der Prävention: Geschäftsführer in der Krise sollen wissen, welche Steuern sie vorrangig abführen müssen.

## Eingaben

- Haftungsbescheid (Datum, Haftungsschuldner, Haftungsnorm, Steuerarten, Zeiträume, Betrag) oder Anhörungsschreiben
- Rolle des Haftungsschuldners (Geschäftsführer, faktischer Geschäftsführer, Liquidator, Vorstand, Vermögensverwalter, Erwerber, Arbeitgeber) und Zeitraum der Organstellung
- Ressortverteilung in der Geschäftsführung (schriftlich? wann?)
- Liquiditätsentwicklung der Gesellschaft: Fälligkeiten, gezahlte Verbindlichkeiten, Lohnzahlungen, Insolvenzantrag (Datum), Insolvenzeröffnung
- Steuerfestsetzungen gegenüber der Gesellschaft (bestandskräftig? angefochten? vom Haftungsschuldner als Vertreter angefochten?)
- Strafverfahren (§ 370 AO, § 266a StGB)

## Sub-Agent-Architektur

Ein **Tatbestands-Prüfer** bestimmt die Haftungsnorm und die Pflichtenstellung. Ein **Quoten-Prüfer** berechnet die Haftung nach dem Grundsatz anteiliger Tilgung (Ausnahme Lohnsteuer). Ein **Ermessens-Prüfer** prüft Entschließungs- und Auswahlermessen und deren Begründung. Ein **Verfahrens-Prüfer** prüft Festsetzungsfrist, Akzessorietät, Drittwirkung, Subsidiarität und Zuständigkeit und bereitet Einspruch und AdV vor.

## Ablauf

### 1. Haftungsnorm bestimmen

| Norm | Haftender | Kern |
|---|---|---|
| [§ 69 AO](https://www.gesetze-im-internet.de/ao_1977/__69.html) i. V. m. [§ 34 AO](https://www.gesetze-im-internet.de/ao_1977/__34.html), [§ 35 AO](https://www.gesetze-im-internet.de/ao_1977/__35.html) | gesetzliche Vertreter, Geschäftsführer, Liquidatoren, Vermögensverwalter, Verfügungsberechtigte | vorsätzliche oder grob fahrlässige Pflichtverletzung → Steuer nicht oder nicht rechtzeitig festgesetzt oder erfüllt |
| [§ 71 AO](https://www.gesetze-im-internet.de/ao_1977/__71.html) | Täter und Teilnehmer einer Steuerhinterziehung / Steuerhehlerei | verkürzte Steuern und Hinterziehungszinsen |
| [§ 73 AO](https://www.gesetze-im-internet.de/ao_1977/__73.html) | Organgesellschaft | Steuern des Organträgers, für die die Organschaft zwischen ihnen steuerlich von Bedeutung ist |
| [§ 74 AO](https://www.gesetze-im-internet.de/ao_1977/__74.html) | wesentlich Beteiligter (> 25 %) als Eigentümer überlassener Gegenstände | betriebliche Steuern, beschränkt auf diese Gegenstände |
| [§ 75 AO](https://www.gesetze-im-internet.de/ao_1977/__75.html) | Betriebsübernehmer | betriebliche Steuern des letzten Jahres vor Übereignung, beschränkt auf das übernommene Vermögen; nicht bei Erwerb aus Insolvenzmasse |
| [§ 42d EStG](https://www.gesetze-im-internet.de/estg/__42d.html) | Arbeitgeber | nicht einbehaltene / nicht abgeführte Lohnsteuer |

### 2. Haftung des Geschäftsführers nach § 69 AO

- **Pflichtenstellung**: Der Geschäftsführer hat die steuerlichen Pflichten der GmbH zu erfüllen und insbesondere die Steuern aus den verwalteten Mitteln zu entrichten (§ 34 Abs. 1 AO). Auch der **faktische Geschäftsführer** haftet (§ 35 AO).
- **Pflichtverletzung**: Nichtzahlung fälliger Steuern, Nichtabgabe von Erklärungen und Anmeldungen, verspätete Anmeldungen.
- **Verschulden**: Vorsatz oder **grobe Fahrlässigkeit**. Unkenntnis der steuerlichen Pflichten entlastet nicht; der „Strohmann" haftet regelmäßig, weil er seine Überwachungspflicht verletzt.
- **Ressortaufteilung**: Eine klare, im Voraus **schriftlich** getroffene Geschäftsverteilung kann die Verantwortung der nicht zuständigen Geschäftsführer begrenzen; sie entfällt in der Krise, wenn die Zahlungsfähigkeit insgesamt betroffen ist (Gesamtverantwortung) `[unverifiziert – prüfen]`.
- **Kausalität**: Der Schaden muss auf der Pflichtverletzung beruhen; bei verspäteter Anmeldung kommt es darauf an, ob bei rechtzeitiger Anmeldung hätte gezahlt werden können.

### 3. Haftungsumfang: Grundsatz anteiliger Tilgung

- Reichen die Mittel nicht für alle Gläubiger, darf der Geschäftsführer das Finanzamt nicht schlechter stellen als andere Gläubiger. Er haftet nur für den Betrag, um den die Steuern **in geringerem Umfang getilgt** wurden als die übrigen Verbindlichkeiten (**Haftungsquote**: Verhältnis der Gesamtzahlungen zu den Gesamtverbindlichkeiten im Haftungszeitraum, angewandt auf die Steuerschulden) `[unverifiziert – prüfen]`.
- **Ausnahme Lohnsteuer**: Lohnsteuer ist ein treuhänderisch einbehaltener Betrag. Reichen die Mittel nicht für Lohn und Lohnsteuer, sind die **Löhne zu kürzen** und die auf den gekürzten Lohn entfallende Lohnsteuer abzuführen; werden Nettolöhne voll ausgezahlt und die Lohnsteuer nicht abgeführt, haftet der Geschäftsführer regelmäßig **in voller Höhe** `[unverifiziert – prüfen]`.
- Umsatzsteuer, Körperschaft- und Gewerbesteuer: anteilige Tilgung. Säumniszuschläge und Zinsen sind von der Haftung umfasst (§ 69 S. 2 AO).
- Darlegung: Der Geschäftsführer muss die Liquiditätsverhältnisse im Haftungszeitraum mitwirkend darlegen; fehlt die Darlegung, darf das Finanzamt schätzen.

### 4. Insolvenzlage ([§ 15b InsO](https://www.gesetze-im-internet.de/inso/__15b.html))

- Nach Eintritt der Zahlungsunfähigkeit oder Überschuldung gilt das **Zahlungsverbot** des § 15b Abs. 1 InsO. Die Kollision mit der steuerlichen Zahlungspflicht löst **§ 15b Abs. 8 InsO**: Eine Verletzung steuerlicher Zahlungspflichten liegt nicht vor, wenn zwischen Eintritt der Insolvenzreife und der Entscheidung des Insolvenzgerichts Steuern nicht oder nicht rechtzeitig gezahlt werden, **sofern** die Antragspflichtigen ihre Pflichten nach § 15a InsO erfüllen; bei verspätetem Antrag entfällt der Schutz (Einzelheiten zum Umfang in § 15b Abs. 8 S. 2, 3 InsO nachlesen).
- Folge für die Haftung: Wer den Insolvenzantrag rechtzeitig (binnen drei Wochen bei Zahlungsunfähigkeit, sechs Wochen bei Überschuldung, § 15a Abs. 1 InsO) stellt, haftet für die in dieser Zeit nicht gezahlten Steuern regelmäßig nicht nach § 69 AO. Wer zu spät stellt, verliert den Schutz.
- Anfechtbarkeit von Steuerzahlungen in der Krise (§§ 129 ff. InsO): Nach der BFH-Linie entfällt die Kausalität nicht ohne Weiteres, weil die Zahlung später angefochten werden könnte `[unverifiziert – prüfen]`.

### 5. Haftungsbescheid ([§ 191 AO](https://www.gesetze-im-internet.de/ao_1977/__191.html))

- **Ermessen**: Entschließungsermessen (ob überhaupt Haftung) und Auswahlermessen (welcher von mehreren Haftenden, in welcher Höhe). Bei mehreren Geschäftsführern ist die Auswahl zu begründen; ein Verweis auf Vorsatz kann das Auswahlermessen vorprägen. Ermessensfehler sind im Einspruch vollständig, im Klageverfahren nur nach [§ 102 FGO](https://www.gesetze-im-internet.de/fgo/__102.html) überprüfbar. Im Klageverfahren kann die Behörde ihre Ermessenserwägungen bis zum Abschluss der Tatsacheninstanz nur **ergänzen**, nicht erstmals anstellen (§ 102 S. 2 FGO).
- **Anhörung** vor Erlass (§ 91 AO); bei Rechtsanwälten, Steuerberatern, Notaren in Ausübung ihres Berufs: vorherige Unterrichtung der Berufskammer (§ 191 Abs. 2 AO).
- **Festsetzungsfrist** für den Haftungsbescheid (§ 191 Abs. 3 AO): **vier Jahre**, bei § 71 AO **zehn Jahre**, bei § 70 AO in Fällen des § 370 AO zehn und des § 378 AO fünf Jahre; Beginn mit Ablauf des Jahres, in dem der Haftungstatbestand verwirklicht wurde; Ist die Steuer, für die gehaftet wird, **noch nicht festgesetzt**, endet die Frist nicht vor Ablauf der für die Steuerfestsetzung geltenden Festsetzungsfrist; ist sie festgesetzt, gilt **§ 171 Abs. 10 AO sinngemäß** (zwei Jahre nach Bekanntgabe des Steuerbescheids) (§ 191 Abs. 3 S. 4 AO). Bei §§ 73, 74 AO endet die Frist nicht vor Zahlungsverjährung der Steuer (§ 191 Abs. 3 S. 5 AO).
- **Akzessorietät** (§ 191 Abs. 5 AO): Kein Haftungsbescheid, soweit die Steuer gegenüber dem Steuerschuldner nicht mehr festgesetzt werden kann, festgesetzte Steuer verjährt oder erlassen ist — außer bei Hinterziehung oder Hehlerei durch den Haftenden.

### 6. Drittwirkung und Einwendungen ([§ 166 AO](https://www.gesetze-im-internet.de/ao_1977/__166.html))

- Ist die Steuer gegenüber der Gesellschaft **unanfechtbar** festgesetzt, muss der Haftende sie gegen sich gelten lassen, **soweit er als Vertreter in der Lage gewesen wäre, die Festsetzung anzufechten** — typisch für den amtierenden Geschäftsführer.
- Ausgeschiedene Geschäftsführer oder solche ohne Anfechtungsmöglichkeit können Einwendungen gegen die Steuer im Haftungsverfahren vorbringen.
- Bei Steueranmeldungen der GmbH (USt-Voranmeldung, Lohnsteueranmeldung) wirkt die Anmeldung als Festsetzung unter Vorbehalt — Drittwirkung entsprechend.

### 7. Zahlungsaufforderung und Vollstreckung ([§ 219 AO](https://www.gesetze-im-internet.de/ao_1977/__219.html))

- Der Haftungsschuldner darf **auf Zahlung** nur in Anspruch genommen werden, soweit die Vollstreckung in das bewegliche Vermögen des Steuerschuldners **erfolglos** war oder aussichtslos wäre (**Subsidiarität**).
- **Ausnahmen** (§ 219 S. 2 AO): Haftung wegen Hinterziehung/Hehlerei und Haftung für einbehaltene und abzuführende Steuern (Lohnsteuer, Kapitalertragsteuer) — dann sofortige Zahlungsaufforderung möglich.
- Zahlungsaufforderung ist ein eigenständiger Verwaltungsakt, regelmäßig mit dem Haftungsbescheid verbunden.

### 8. Rechtsschutz

- **Einspruch** binnen eines Monats (§ 355 AO) gegen Haftungsbescheid und Zahlungsaufforderung; **AdV** (§ 361 AO) — ernstliche Zweifel an Pflichtverletzung, Verschulden, Quote oder Ermessen.
- Die Begrenzung des § 361 Abs. 2 S. 4 AO betrifft nur Steuerbescheide, **nicht** Haftungsbescheide.
- Parallel: Strafverfahren (§ 370 AO, § 266a StGB) koordinieren; Einlassungen im Haftungsverfahren können strafrechtlich verwertet werden.

## Ausgabeformat

```
HAFTUNGSBESCHEID — Prüfung — <Haftungsschuldner> — <Datum> — Rechtsstand Oktober 2026

I.    Bescheid
      Datum / Bekanntgabe:            <…>
      Haftungsnorm:                   [§ 69 AO / § 71 AO / § 75 AO / § 42d EStG / …]
      Steuerarten / Zeiträume / Betrag: <…>

II.   Tatbestand
      Pflichtenstellung (§§ 34, 35):  <Organstellung von … bis …>
      Pflichtverletzung:              <…>
      Verschulden (Vorsatz / grobe Fahrlässigkeit): <…>
      Ressortaufteilung:              [schriftlich vom … / keine]
      Kausalität:                     <…>

III.  Umfang
      Haftungsquote (anteilige Tilgung): <Zahlungen / Verbindlichkeiten = …%>
      Lohnsteuer (volle Haftung?):    <…>
      § 15b Abs. 8 InsO:              [Antrag rechtzeitig am … → Schutz / verspätet]

IV.   Verfahren
      Anhörung (§ 91):                [✓ / ✗]
      Ermessen (Entschließung / Auswahl): [begründet / fehlerhaft: …]
      Festsetzungsfrist (§ 191 Abs. 3): <Ende …>
      Akzessorietät (§ 191 Abs. 5):   <…>
      Drittwirkung (§ 166):           [greift / greift nicht — Einwendungen gegen die Steuer zulässig]
      Subsidiarität (§ 219):          [Vollstreckung gegen GmbH erfolglos? / Ausnahme S. 2]

V.    Rechtsbehelf
      Einspruch bis:                  <Datum>
      AdV:                            [beantragt — Gründe …]

VI.   Strafrechtliche Bezüge:         <…>
```

## Beispiel (Gutachtenstil, verkürzt)

G war bis zum Insolvenzantrag vom 14.08.2026 alleiniger Geschäftsführer der X-GmbH. Das Finanzamt nimmt ihn für USt Mai–Juli 2026 (60.000 EUR) und Lohnsteuer Juli 2026 (12.000 EUR) in Haftung. Die GmbH war seit Ende Juni 2026 zahlungsunfähig. Fraglich ist zunächst die USt. Für Mai 2026 ist nach dem Grundsatz anteiliger Tilgung nur die Quote geschuldet, die sich aus dem Verhältnis der Zahlungen an andere Gläubiger zu den Gesamtverbindlichkeiten ergibt. Für Juni und Juli 2026 kommt eine Entlastung nach § 15b Abs. 8 InsO in Betracht. Sie setzt voraus, dass G seine Antragspflicht nach § 15a InsO erfüllt hat. Bei Zahlungsunfähigkeit Ende Juni 2026 lief die Drei-Wochen-Frist Mitte Juli ab; der Antrag vom 14.08.2026 war verspätet, sodass der Schutz für den Zeitraum der Verspätung entfällt. Für die Lohnsteuer Juli 2026 haftet G regelmäßig voll, wenn er die Nettolöhne ungekürzt ausgezahlt hat. Ergebnis: Einspruch mit Quotenberechnung für die USt; zur Lohnsteuer allenfalls Ermessens- und Kausalitätseinwände.

## Risiken / typische Fehler

- **Lohnsteuer wie andere Steuern behandelt** — volle Haftung, wenn Nettolöhne ausgezahlt und Lohnsteuer nicht abgeführt wurde; keine Subsidiarität (§ 219 S. 2 AO).
- **Haftungsquote nicht dargelegt** — ohne Liquiditätsaufstellung darf das Finanzamt schätzen.
- **§ 15b Abs. 8 InsO überschätzt** — Schutz nur bei rechtzeitigem Insolvenzantrag.
- **Ressortaufteilung ohne Schriftform** — schützt nicht; in der Krise Gesamtverantwortung.
- **Drittwirkung (§ 166 AO) verkannt** — der amtierende Geschäftsführer kann Einwendungen gegen bestandskräftige Steuern meist nicht mehr vorbringen.
- **Ermessensfehler nicht gerügt** — fehlende Auswahlbegründung bei mehreren Geschäftsführern; Ermessen kann im Klageverfahren nur ergänzt, nicht nachgeholt werden.
- **Festsetzungsfrist und Akzessorietät** (§ 191 Abs. 3, 5 AO) nicht geprüft.
- **Strafverfahren ausgeblendet** — Einlassungen im Haftungsverfahren mit der Verteidigung abstimmen.

## Quellen

### Statute

- [§ 34 AO](https://www.gesetze-im-internet.de/ao_1977/__34.html), [§ 35 AO](https://www.gesetze-im-internet.de/ao_1977/__35.html), [§ 69 AO](https://www.gesetze-im-internet.de/ao_1977/__69.html), [§ 70 AO](https://www.gesetze-im-internet.de/ao_1977/__70.html), [§ 71 AO](https://www.gesetze-im-internet.de/ao_1977/__71.html), [§ 73 AO](https://www.gesetze-im-internet.de/ao_1977/__73.html), [§ 74 AO](https://www.gesetze-im-internet.de/ao_1977/__74.html), [§ 75 AO](https://www.gesetze-im-internet.de/ao_1977/__75.html)
- [§ 91 AO](https://www.gesetze-im-internet.de/ao_1977/__91.html), [§ 166 AO](https://www.gesetze-im-internet.de/ao_1977/__166.html), [§ 191 AO](https://www.gesetze-im-internet.de/ao_1977/__191.html), [§ 219 AO](https://www.gesetze-im-internet.de/ao_1977/__219.html), [§ 355 AO](https://www.gesetze-im-internet.de/ao_1977/__355.html), [§ 361 AO](https://www.gesetze-im-internet.de/ao_1977/__361.html)
- [§ 42d EStG](https://www.gesetze-im-internet.de/estg/__42d.html)
- [§ 15a InsO](https://www.gesetze-im-internet.de/inso/__15a.html), [§ 15b InsO](https://www.gesetze-im-internet.de/inso/__15b.html)
- [§ 102 FGO](https://www.gesetze-im-internet.de/fgo/__102.html)

### Gesetzgebung (nicht in Kraft)

- Regierungsentwurf JStG 2026, BT-Drs. 21/8283, Art. 18 Nr. 3, 4 (§§ 26, 28 AO)

### Verwaltungsanweisungen

- AEAO zu §§ 69, 191, 219 AO

### Rechtsprechung (alle `[unverifiziert – prüfen]`)

- BFH-Linie zum Grundsatz anteiliger Tilgung und zur vollen Lohnsteuerhaftung — Az. in juris ermitteln (Suchstring: „§ 69 AO Grundsatz anteiliger Tilgung Lohnsteuer Kürzung der Löhne")
- BFH-Linie zur Ressortaufteilung in der Krise — Suchstring: „§ 69 AO Geschäftsverteilung schriftlich Gesamtverantwortung Krise"
- BFH-Linie zu § 15b Abs. 8 InsO — Suchstring: „§ 15b Abs. 8 InsO Haftung § 69 AO Antragsfrist"

### Literatur

- Loose, in: Tipke/Kruse, AO/FGO, § 69 AO `[unverifiziert – prüfen]`
- Jatzke, in: Gosch, AO/FGO, § 191 AO `[unverifiziert – prüfen]`
