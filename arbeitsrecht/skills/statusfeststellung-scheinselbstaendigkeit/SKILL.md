---
name: statusfeststellung-scheinselbstaendigkeit
description: "Abgrenzung von Beschäftigung und Selbständigkeit und Statusfeststellungsverfahren – Beschäftigungsbegriff § 7 Abs. 1 SGB IV und Arbeitsvertrag § 611a BGB, Gesamtabwägung nach Weisungsgebundenheit, Eingliederung und Unternehmerrisiko, Anfrageverfahren § 7a SGB IV mit Prognose- und Gruppenfeststellung, Haftung für den Gesamtsozialversicherungsbeitrag §§ 28e, 28g SGB IV, Verjährung § 25 SGB IV, Säumniszuschläge § 24 SGB IV, Strafbarkeit § 266a StGB, Lohnsteuerhaftung § 42d EStG, verdeckte Arbeitnehmerüberlassung §§ 9, 10 AÜG, Rentenversicherungspflicht Selbständiger § 2 SGB VI; Ausblick Plattformarbeits-RL (EU) 2024/2831 (Umsetzungsfrist 02.12.2026) und BMAS-Referentenentwurf 2026. Use when Freelancer, Honorarkräfte, Interim-Manager oder Plattformtätige eingesetzt werden oder eine Betriebsprüfung der DRV droht."
language: de
agents:
  researcher: ../../agents/researcher.md
  drafter: ../../agents/drafter.md
  reviewer: ../../agents/reviewer.md
provider_variants: [claude, gemini, openai]
test: ./test.md
---

# /arbeitsrecht:statusfeststellung-scheinselbstaendigkeit

## Zweck

Scheinselbständigkeit ist ein Haftungsthema, kein Etikettenthema: Wird ein „Freelancer" rückwirkend als Beschäftigter eingestuft, schuldet der Auftraggeber die Gesamtsozialversicherungsbeiträge für bis zu vier — bei Vorsatz bis zu 30 — Jahre, regelmäßig ohne Rückgriff auf den Auftragnehmer, zuzüglich Säumniszuschlägen. Dieser Skill prüft den Status anhand der Rspr. von BSG und BAG, entscheidet über ein Statusfeststellungsverfahren nach § 7a SGB IV und sichert laufende Vertragsbeziehungen ab.

> **Rechtsstand: Oktober 2026.** §§ 7, 7a SGB IV in der Fassung seit 01.04.2022. Die Plattformarbeits-RL ist bis 02.12.2026 umzusetzen; ein deutscher Entwurf ist nicht veröffentlicht. Ein BMAS-Referentenentwurf zur Erleichterung der Statusfeststellung (26.03.2026) ist nicht beschlossen `[unverifiziert – prüfen]`.

## Eingaben

- Vertrag (Bezeichnung, Leistungsbeschreibung, Vergütung nach Stunden oder Ergebnis, Laufzeit, Kündigung)
- **Tatsächliche** Durchführung: Weisungen zu Zeit, Ort, Art; Einbindung in Dienstpläne, Teams, Tools, E-Mail-Adresse, Visitenkarte
- Eigene Betriebsmittel, eigene Mitarbeiter, Werbung am Markt, weitere Auftraggeber, Umsatzanteil des Auftraggebers
- Vergütungshöhe im Vergleich zu angestellten Kräften
- Vermittlung über eine Agentur oder Plattform?
- Bisherige Statusentscheidungen, DRV-Betriebsprüfungen, Hinweise von Behörden

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert SGB-IV-, BGB- und AÜG-Normen mit URL sowie die Leitentscheidungen von BSG und BAG zur Abgrenzung.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) erstellt Statusgutachten, Antrag nach § 7a SGB IV, Vertragsanpassung oder Widerspruch gegen einen Beitragsbescheid.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Gesamtabwägung, Haftungsrisiko, Verjährung und strafrechtliche Bezüge.

## Ablauf

### 1. Maßstab ([§ 7 Abs. 1 SGB IV](https://www.gesetze-im-internet.de/sgb_4/__7.html), [§ 611a BGB](https://www.gesetze-im-internet.de/bgb/__611a.html))

- Beschäftigung ist nichtselbständige Arbeit, insbesondere in einem Arbeitsverhältnis; Anhaltspunkte sind **Tätigkeit nach Weisungen** und **Eingliederung** in die Arbeitsorganisation des Weisungsgebers.
- § 611a BGB definiert den Arbeitsvertrag über weisungsgebundene, fremdbestimmte Arbeit in persönlicher Abhängigkeit; maßgeblich ist die **tatsächliche Durchführung**, nicht die Bezeichnung (§ 611a Abs. 1 S. 6 BGB).
- **Gesamtabwägung** aller Indizien; kein Einzelmerkmal ist allein entscheidend.

| Für Beschäftigung | Für Selbständigkeit |
|---|---|
| Einbindung in Dienstpläne, feste Arbeitszeiten | freie Zeiteinteilung |
| Arbeit mit Betriebsmitteln des Auftraggebers | eigene, nennenswerte Betriebsmittel |
| Vergütung nach Zeit ohne Verlustrisiko | **Unternehmerrisiko** mit Chance und Risiko |
| Einbindung in Teams, Vertretungsregeln | eigene Mitarbeiter, Recht zur Delegation |
| ein Auftraggeber, dauerhaft | Marktauftritt, mehrere Auftraggeber |

Eine Vergütung **deutlich über** dem Arbeitnehmerniveau ist ein Indiz für Selbständigkeit, überwiegt aber nicht die übrigen Merkmale (BSG, Urt. v. 04.06.2019 – B 12 R 11/18 R, Honorarärzte, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BSG&Datum=2019-06-04&Aktenzeichen=B%2012%20R%2011/18%20R)). Für Lehrkräfte hat das BSG die Eingliederung in den Lehrbetrieb in den Vordergrund gestellt (BSG, Urt. v. 28.06.2022 – B 12 R 3/20 R, *Herrenberg*, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BSG&Datum=2022-06-28&Aktenzeichen=B%2012%20R%203/20%20R)); für Lehrkräfte gilt eine gesetzliche Übergangsregelung bis 31.12.2026 `[unverifiziert – prüfen]`.

### 2. Statusfeststellungsverfahren ([§ 7a SGB IV](https://www.gesetze-im-internet.de/sgb_4/__7a.html))

- **Antrag** bei der Clearingstelle der DRV Bund durch Auftraggeber oder Auftragnehmer, sofern nicht bereits ein Verfahren (Betriebsprüfung, Einzugsstelle) eingeleitet ist.
- Seit 01.04.2022: Feststellung des **Erwerbsstatus** (nicht mehr der Versicherungspflicht in jedem Zweig), **Prognoseentscheidung** vor Aufnahme der Tätigkeit, **Gruppenfeststellung** für gleichartige Vertragsverhältnisse, mündliche Anhörung im Widerspruchsverfahren. Befristung einzelner Elemente bis 30.06.2027 prüfen `[unverifiziert – prüfen]`.
- **Rückwirkungsschutz:** Bei Antrag binnen **eines Monats** nach Aufnahme der Tätigkeit und Zustimmung des Beschäftigten tritt Versicherungspflicht erst mit Bekanntgabe der Entscheidung ein, wenn der Beschäftigte für Krankheit und Alter abgesichert ist (§ 7a SGB IV).
- **Taktik:** Ein Antrag macht den Fall aktenkundig. Er ist bei objektiv klarer Selbständigkeit oder als Absicherung bei langfristigen Einsätzen sinnvoll, bei gemischtem Bild erst nach Vertragsanpassung **und** tatsächlicher Umstellung.

### 3. Rechtsfolgen der Fehlklassifizierung

- **Beitragsschuld des Arbeitgebers** ([§ 28e SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28e.html)): Gesamtsozialversicherungsbeitrag einschließlich Arbeitnehmeranteil.
- **Rückgriff auf den Beschäftigten** nur durch Lohnabzug und nur bei den **drei nächsten** Lohn- oder Gehaltszahlungen; danach nur, wenn der Abzug ohne Verschulden des Arbeitgebers unterblieben ist ([§ 28g SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28g.html)) — praktisch meist ausgeschlossen.
- **Verjährung** ([§ 25 SGB IV](https://www.gesetze-im-internet.de/sgb_4/__25.html)): vier Jahre nach Ablauf des Kalenderjahres der Fälligkeit; **30 Jahre** bei Vorsatz — bedingter Vorsatz genügt.
- **Säumniszuschläge** ([§ 24 SGB IV](https://www.gesetze-im-internet.de/sgb_4/__24.html)): 1 % je angefangenen Monat; Entlastung nur bei unverschuldeter Unkenntnis.
- **Strafbarkeit** ([§ 266a StGB](https://www.gesetze-im-internet.de/stgb/__266a.html)): Vorenthalten von Arbeitnehmerbeiträgen; persönliche Haftung der Geschäftsführung über § 823 Abs. 2 BGB.
- **Lohnsteuer** ([§ 42d EStG](https://www.gesetze-im-internet.de/estg/__42d.html)): Haftung für nicht einbehaltene Lohnsteuer; Umsatzsteuer aus den Honorarrechnungen kann entfallen (Vorsteuerkorrektur).
- **Arbeitsrecht:** Bestehen eines Arbeitsverhältnisses mit Kündigungsschutz, Urlaub, Entgeltfortzahlung; Klage auf Feststellung vor dem Arbeitsgericht.

### 4. Dreieckskonstellationen — verdeckte Arbeitnehmerüberlassung

Wird der Auftragnehmer über eine Agentur eingesetzt und tatsächlich in den Betrieb des Kunden eingegliedert, liegt Arbeitnehmerüberlassung vor. Fehlt die Erlaubnis oder die Offenlegung und Konkretisierung als Überlassung ([§ 1 AÜG](https://www.gesetze-im-internet.de/a_g/__1.html)), ist der Vertrag unwirksam und es wird ein **Arbeitsverhältnis zum Entleiher** fingiert ([§ 9 AÜG](https://www.gesetze-im-internet.de/a_g/__9.html), [§ 10 AÜG](https://www.gesetze-im-internet.de/a_g/__10.html)). Eine vorsorgliche Überlassungserlaubnis („Fallschirm") schützt nicht mehr.

### 5. Selbständige mit Rentenversicherungspflicht

Auch echte Selbständige können rentenversicherungspflichtig sein, insbesondere Lehrer, Pflegepersonen und Selbständige mit im Wesentlichen nur **einem** Auftraggeber ohne eigene versicherungspflichtige Arbeitnehmer ([§ 2 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__2.html)).

### 6. Ausblick — nicht geltendes Recht

- **Plattformarbeits-RL (EU) 2024/2831:** widerlegliche **Vermutung** eines Arbeitsverhältnisses bei Kontrolle und Steuerung durch die Plattform (Art. 5), algorithmisches Management, Umsetzungsfrist **02.12.2026**. Nach BT-Drs. 21/5454 (14.04.2026) erarbeitet das BMAS einen Referentenentwurf; eine Umsetzung bis zur Frist ist nicht absehbar `[unverifiziert – prüfen]`. Nach Fristablauf: unionsrechtskonforme Auslegung, gegenüber staatlichen Stellen ggf. unmittelbare Wirkung.
- **BMAS-Referentenentwurf vom 26.03.2026** zur Erleichterung der Feststellung des Erwerbsstatus — Inhalt nicht verifiziert `[unverifiziert – prüfen]`.

## Quellen

### Statute

- [§ 7 SGB IV](https://www.gesetze-im-internet.de/sgb_4/__7.html), [§ 7a SGB IV](https://www.gesetze-im-internet.de/sgb_4/__7a.html), [§ 24 SGB IV](https://www.gesetze-im-internet.de/sgb_4/__24.html), [§ 25 SGB IV](https://www.gesetze-im-internet.de/sgb_4/__25.html), [§ 28e SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28e.html), [§ 28g SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28g.html)
- [§ 611a BGB](https://www.gesetze-im-internet.de/bgb/__611a.html), [§ 2 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__2.html), [§ 266a StGB](https://www.gesetze-im-internet.de/stgb/__266a.html), [§ 42d EStG](https://www.gesetze-im-internet.de/estg/__42d.html)
- [§ 1 AÜG](https://www.gesetze-im-internet.de/a_g/__1.html), [§ 9 AÜG](https://www.gesetze-im-internet.de/a_g/__9.html), [§ 10 AÜG](https://www.gesetze-im-internet.de/a_g/__10.html)
- Richtlinie (EU) 2024/2831 zur Verbesserung der Arbeitsbedingungen in der Plattformarbeit, Art. 4, 5, 29 (über EUR-Lex)

### Kommentare

- Rittweger, in: BeckOK Sozialrecht, § 7 SGB IV Rn. 1 ff. `[unverifiziert – prüfen]`
- Preis, in: ErfK, 26. Aufl. 2026, § 611a BGB Rn. 1 ff. `[unverifiziert – prüfen]` (Auflage prüfen)

### Rechtsprechung

- BSG, Urt. v. 04.06.2019 – B 12 R 11/18 R (Honorarärzte; Honorarhöhe nur Indiz), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BSG&Datum=2019-06-04&Aktenzeichen=B%2012%20R%2011/18%20R)
- BSG, Urt. v. 28.06.2022 – B 12 R 3/20 R, *Herrenberg* (Musikschullehrkraft; Eingliederung), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BSG&Datum=2022-06-28&Aktenzeichen=B%2012%20R%203/20%20R)
- BAG, Urt. v. 01.12.2020 – 9 AZR 102/20 (Crowdworker als Arbeitnehmer) `[unverifiziert – prüfen]`

## Ausgabeformat

```
STATUSPRÜFUNG — <Auftragnehmer> — <Mandat-ID> — <Datum>
Rechtsstand: Oktober 2026

Gesamtbefund: [🟢 Selbständigkeit tragfähig / 🟡 gemischt / 🔴 Beschäftigung]

I.    Vertrag vs. tatsächliche Durchführung   <Abweichungen>
II.   Indizien (Gesamtabwägung)
      Weisungen / Eingliederung:      <…>
      Unternehmerrisiko / Betriebsmittel: <…>
      Marktauftritt / Auftraggeber:   <…>
      Vergütungsniveau:               <…>
III.  Dreieck / AÜG                   [nein / ja — Erlaubnis? Offenlegung?]
IV.   Haftungsrisiko
      Beitragszeitraum (§ 25 SGB IV): <4 / 30 Jahre>
      Geschätzte Nachforderung:       <EUR> + Säumniszuschläge
      § 266a StGB-Risiko:             <…>
V.    Statusfeststellungsverfahren § 7a SGB IV
      Empfehlung:                     [Antrag jetzt / nach Umstellung / kein Antrag]
      Rückwirkungsschutz (1 Monat):   [möglich / verpasst]
VI.   Ausblick Plattform-RL / RefE    <Relevanz>
VII.  Maßnahmen                       <Vertrag, Durchführung, Dokumentation>
```

## Beispiel (Gutachtenstil, verkürzt)

**Sachverhalt.** Zwölf „freie" Disponenten arbeiten seit drei Jahren in festen Schichten im Dispositionssystem der Mandantin, mit Firmen-E-Mail und Stundenhonorar von 65 EUR. Die DRV kündigt eine Betriebsprüfung an.

**Frage: Liegt Beschäftigung vor?** Beschäftigung ist nach § 7 Abs. 1 SGB IV nichtselbständige Arbeit mit Weisungsgebundenheit und Eingliederung. Feste Schichten, Arbeit im System des Auftraggebers und die Außendarstellung über eine Firmenadresse sprechen deutlich für Eingliederung. Ein Unternehmerrisiko fehlt: Vergütet wird die Zeit, eigene Betriebsmittel von Gewicht sind nicht ersichtlich. Das hohe Honorar ist nach der BSG-Rechtsprechung nur ein Indiz und kann die übrigen Merkmale nicht aufwiegen. In der Gesamtabwägung liegt Beschäftigung vor.

**Haftung.** Die Mandantin schuldet den Gesamtsozialversicherungsbeitrag (§ 28e SGB IV) für den gesamten Zeitraum, ohne nennenswerten Rückgriff (§ 28g SGB IV), zuzüglich Säumniszuschlägen. Bei bedingtem Vorsatz verjähren die Beiträge erst nach 30 Jahren (§ 25 Abs. 1 S. 2 SGB IV). Für die zwei über eine Agentur eingesetzten Disponenten ist zusätzlich die verdeckte Arbeitnehmerüberlassung zu prüfen (§§ 9, 10 AÜG).

**Ergebnis.** Ein Statusfeststellungsantrag ist unzulässig, sobald der Rentenversicherungsträger ein Verfahren zur Feststellung eingeleitet hat (§ 7a Abs. 1 S. 1 SGB IV); ob die bloße Prüfankündigung schon genügt, ist vor Antragstellung zu klären `[unverifiziert – prüfen]`. Praktisch kommt der Antrag hier zu spät. Empfehlung: Überführung in Arbeitsverhältnisse, Beitragsschätzung, Prüfung einer Korrekturmeldung zur Begrenzung des Vorsatzvorwurfs, steuerliche Haftung nach § 42d EStG einbeziehen.

## Risiken / typische Fehler

- **Vertragsbezeichnung statt tatsächlicher Durchführung geprüft** — maßgeblich ist, wie das Verhältnis gelebt wird (§ 611a Abs. 1 S. 6 BGB).
- **Hohes Honorar als Freibrief gewertet** — es ist nur ein Indiz unter mehreren.
- **Verjährung mit vier Jahren angesetzt** — bei bedingtem Vorsatz gilt die 30-jährige Frist; Kenntnis der Problematik genügt oft.
- **Rückgriff auf den Auftragnehmer eingeplant** — § 28g SGB IV erlaubt den unterbliebenen Abzug nur bei den **drei nächsten** Lohn- oder Gehaltszahlungen, danach nur bei fehlendem Verschulden des Arbeitgebers.
- **Statusfeststellungsantrag ohne vorherige Umstellung gestellt** — macht ein gemischtes Bild aktenkundig.
- **Verdeckte Arbeitnehmerüberlassung übersehen** — Fiktion eines Arbeitsverhältnisses zum Kunden nach §§ 9, 10 AÜG.
- **Plattform-RL als bereits umgesetzt behandelt** — Stand Oktober 2026 gibt es kein deutsches Umsetzungsgesetz.
- **Rentenversicherungspflicht echter Selbständiger vergessen** — § 2 SGB VI erfasst u. a. Selbständige mit nur einem Auftraggeber.
