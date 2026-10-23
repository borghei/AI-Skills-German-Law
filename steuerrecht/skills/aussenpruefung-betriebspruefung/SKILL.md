---
name: aussenpruefung-betriebspruefung
description: "Begleitung einer Außenprüfung (Betriebsprüfung) nach §§ 193 ff. AO im reformierten Recht seit 2025 – Prüfungsanordnung § 196, Vorlagefristen und Prüfungsschwerpunkte § 197, Zwischengespräche und Kooperationsvereinbarung § 199 Abs. 2, qualifiziertes Mitwirkungsverlangen mit Mitwirkungsverzögerungsgeld und Zuschlag § 200a, Teilabschlussbescheid § 180 Abs. 1a, Fünf-Jahres-Grenze der Ablaufhemmung § 171 Abs. 4 S. 3 AO, Datenzugriff § 147 Abs. 6 AO, Schätzung § 162 AO, Schlussbesprechung § 201 AO, Außenprüfungsordnung (ApO) 2026. Use when ein Mandant eine Prüfungsanordnung erhalten hat, ein Mitwirkungsverlangen eingeht oder die Schlussbesprechung vorbereitet wird."
language: de
provider_variants: [claude, gemini, openai]
test: ./test.md
---

# /steuerrecht:aussenpruefung-betriebspruefung

> **Rechtsstand: Oktober 2026.** Maßgeblich ist das durch das DAC7-Umsetzungsgesetz vom 20.12.2022 (BGBl. I S. 2730) reformierte Außenprüfungsrecht, das im Kern für **Steuern gilt, die nach dem 31.12.2024 entstehen** (Art. 97 § 37 Abs. 2 EGAO). Einzelne Instrumente greifen auch für ältere Jahre, wenn die Prüfungsanordnung **nach dem 31.12.2024** bekannt gegeben wurde (Art. 97 § 37 Abs. 3 EGAO). Erste Prüfung jedes Mandats: **Welches Recht gilt für welches Prüfungsjahr?**

## Zweck

Die Außenprüfung entscheidet regelmäßig über sechs- bis siebenstellige Mehrergebnisse. Seit der Reform hat die Finanzverwaltung harte Sanktionsinstrumente für verzögerte Mitwirkung (§ 200a AO), zugleich aber eine zeitliche Obergrenze für die Ablaufhemmung (§ 171 Abs. 4 S. 3 AO). Fehler in Mitwirkung und Verfahrensführung führen zu Schätzungen oder Verzögerungsgeldern, deren Bekämpfung im Einspruchs- und Klageverfahren aufwendig ist. Dieser Skill begleitet von der Prüfungsanordnung bis zur Schlussbesprechung und zum Prüfungsbericht.

## Eingaben

- Prüfungsanordnung (Datum der Bekanntgabe, Prüfer, Zeitraum, Steuerarten, angekündigte Prüfungsschwerpunkte, Vorlageverlangen)
- Entstehungsjahre der geprüften Steuern (vor oder nach dem 01.01.2025?)
- Größenklasse und Anschlussprüfung (Großbetrieb / Mittel / Klein)
- Buchführungssystem (DATEV o. a.), GoBD-Verfahrensdokumentation, Tax-Compliance-Management-System
- Vorgeschichte (frühere Prüfungen, offene Punkte, Rahmenvereinbarungen)
- Eingegangene Mitwirkungsverlangen (einfach / qualifiziert nach § 200a AO) mit Fristen

## Sub-Agent-Architektur

Ein **Zeitlich-Anwendungs-Prüfer** ordnet jedes Prüfungsjahr dem alten oder neuen Recht zu. Ein **Verfahrens-Prüfer** führt Fristen (Vorlagefrist, Monatsfrist des § 200a AO, Einspruchsfristen) und Ablaufhemmung. Ein **Sachverhalts-Prüfer** bereitet die Risikofelder vor und plant Datenzugriff und Dokumentation. Ein **Straf-Prüfer** beobachtet laufend, ob ein steuerstrafrechtlicher Anfangsverdacht entsteht (§ 10 der Außenprüfungsordnung, § 397 AO), und stimmt Selbstanzeige- oder Berichtigungsfragen mit der Strafverteidigung ab.

## Ablauf

### 1. Prüfungsanordnung ([§ 196 AO](https://www.gesetze-im-internet.de/ao_1977/__196.html), [§ 197 AO](https://www.gesetze-im-internet.de/ao_1977/__197.html))

- Schriftlicher oder elektronischer Verwaltungsakt mit Rechtsbehelfsbelehrung: Prüfungszeitraum, Steuerarten, Prüfer, voraussichtlicher Beginn.
- **Neu (§ 197 AO):** Die Anordnung kann mit der Aufforderung verbunden werden, bestimmte Unterlagen innerhalb einer angemessenen Frist vorzulegen; die Behörde kann **Prüfungsschwerpunkte** benennen. Die Vorlage an den Prüfer ist vorbereitend — erst mit ihr laufen Mitwirkungserwartungen konkret an.
- **Rechtsbehelf**: Einspruch (§ 347 AO) und AdV (§ 361 AO). Inhaltliche Angriffe sind nur bei Ermessensfehlern (z. B. Schikane, unverhältnismäßige Erweiterung) erfolgversprechend.
- **Verlegung des Beginns** auf Antrag (§ 197 Abs. 2 AO): Achtung — sie verlängert die Fünf-Jahres-Grenze des § 171 Abs. 4 S. 3 AO um die Dauer des Hinausschiebens (§ 171 Abs. 4 S. 4 AO).
- Die Bekanntgabe der Prüfungsanordnung **sperrt die Selbstanzeige** im sachlichen und zeitlichen Umfang der angekündigten Prüfung (§ 371 Abs. 2 S. 1 Nr. 1 a AO) — vorher prüfen, ob Berichtigungsbedarf besteht.

### 2. Mitwirkungspflichten ([§ 90 AO](https://www.gesetze-im-internet.de/ao_1977/__90.html), [§ 200 AO](https://www.gesetze-im-internet.de/ao_1977/__200.html))

- Aufklärung des Sachverhalts, Vorlage von Aufzeichnungen, Büchern, Geschäftspapieren und Urkunden; Auskunftserteilung; Benennung einer Auskunftsperson.
- Erweiterte Mitwirkung und Dokumentation bei Auslandssachverhalten (§ 90 Abs. 2, 3 AO; Transaktionsmatrix und Verrechnungspreisdokumentation auf Anforderung binnen 30 Tagen, § 90 Abs. 4 AO).
- **Zwischengespräche** ([§ 199 Abs. 2 AO](https://www.gesetze-im-internet.de/ao_1977/__199.html)): Der Prüfer soll regelmäßig über Feststellungen unterrichten. Die Beteiligten können einen **Kooperationsrahmen** (Vereinbarung über Mitwirkung, Fristen, Ansprechpartner) vereinbaren; solange er eingehalten wird, ist ein qualifiziertes Mitwirkungsverlangen nach § 200a AO regelmäßig nicht veranlasst. Vereinbarung schriftlich festhalten.

### 3. Qualifiziertes Mitwirkungsverlangen ([§ 200a AO](https://www.gesetze-im-internet.de/ao_1977/__200a.html))

| Element | Regel |
|---|---|
| Zeitpunkt | frühestens **sechs Monate** nach Bekanntgabe der Prüfungsanordnung |
| Form | schriftlich oder elektronisch, mit Rechtsbehelfsbelehrung (anfechtbarer Verwaltungsakt) |
| Frist | Erfüllung binnen **eines Monats** nach Bekanntgabe; Verlängerung in begründeten Einzelfällen |
| Mitwirkungsverzögerungsgeld | **75 EUR je vollem Kalendertag**, höchstens 150 Tage; entfällt bei glaubhaft entschuldbarer Verzögerung (Verschulden von Vertretern und Gehilfen wird zugerechnet) |
| Zuschlag | bis **25.000 EUR je vollem Tag**, höchstens 150 Tage — bei Wiederholung binnen fünf Jahren oder wirtschaftlicher Leistungsfähigkeit; vermutet ab **12 Mio. EUR** Umsatz in einem geprüften Jahr oder **120 Mio. EUR** Konzernumsatz |
| Festsetzungsfrist | **Nur wenn ein Mitwirkungsverzögerungsgeld festgesetzt wurde**, verlängert sich die **Fünf-Jahres-Grenze** des § 171 Abs. 4 S. 3 AO um die Dauer der Verzögerung, mindestens ein Jahr (§ 200a Abs. 4 S. 1 AO). Wurde schon in den fünf Jahren vor Beginn der Verzögerung ein Mitwirkungsverzögerungsgeld festgesetzt, **entfällt die Fünf-Jahres-Grenze ganz** (§ 200a Abs. 4 S. 2 AO). Bei Unmöglichkeit der Mitwirkung gilt das, wenn sie nicht unverzüglich angezeigt wurde (S. 3). Bei Rechtsbehelf gegen Verlangen, Geld oder Zuschlag kein Fristablauf vor einem Jahr nach Unanfechtbarkeit (§ 200a Abs. 5 AO) |
| Ende der Verzögerung | spätestens mit dem Tag der Schlussbesprechung |

**Zeitliche Anwendung:** § 200a Abs. 1–3 und 6 AO gelten auch für Altjahre, wenn die Prüfungsanordnung nach dem 31.12.2024 bekannt gegeben wurde; § 200a Abs. 4 **und 5** AO dagegen nur für nach dem 31.12.2024 entstandene Steuern (Art. 97 § 37 Abs. 2, 3 EGAO — Abs. 3 nennt nur Abs. 1–3 und 6).

**Praxis:** Jedes qualifizierte Verlangen sofort mit Monatsfrist in den Fristenkalender; Unmöglichkeit der Mitwirkung **unverzüglich anzeigen**, sonst greifen die Fristfolgen trotzdem; bei unklaren oder unverhältnismäßigen Verlangen Einspruch und AdV prüfen. Das Verzögerungsgeld nach § 146 Abs. 2c AO betrifft seit 2025 nur noch die unerlaubte Verlagerung der Buchführung ins Ausland.

### 4. Datenzugriff ([§ 147 Abs. 6 AO](https://www.gesetze-im-internet.de/ao_1977/__147.html)) und GoBD

Die **Finanzbehörde wählt** nach pflichtgemäßem Ermessen zwischen:

- **Z1** — Einsicht in die gespeicherten Daten und Nutzung des DV-Systems (unmittelbarer Zugriff),
- **Z2** — maschinelle Auswertung nach ihren Vorgaben durch den Steuerpflichtigen (mittelbarer Zugriff),
- **Z3** — Übertragung der Daten in maschinell auswertbarem Format (Datenträgerüberlassung; in der Praxis der häufigste Weg).

Der Steuerpflichtige kann eine Zugriffsart **anregen**, nicht wählen. Die Kosten trägt er (§ 147 Abs. 6 S. 3 AO). Datenschutz- und Geheimnisschutz durch Datenbeschränkung auf den Prüfungszeitraum sichern; nicht steuerrelevante Daten (z. B. private, mandantenbezogene Berufsgeheimnisse) ausfiltern.

- **Aufbewahrungsfristen** seit 01.01.2025: Bücher und Jahresabschlüsse zehn Jahre, **Buchungsbelege acht Jahre**, sonstige Unterlagen sechs Jahre (§ 147 Abs. 3 S. 1 AO).
- **GoBD** in der Fassung vom 28.11.2019, geändert durch BMF-Schreiben vom 11.03.2024 und vom 14.07.2025 (zweite Änderung: Aufbewahrung von E-Rechnungen — maßgeblich ist der strukturierte Datensatz). Verfahrensdokumentation und internes Kontrollsystem vorlegen können.
- Pending: BFH – IV R 18/24 (löst die bloße Entgegennahme eines Datenträgers durch den Prüfer den Prüfungsbeginn und damit die Ablaufhemmung aus? Verhandlung 12.11.2026) `[unverifiziert – prüfen]`.

### 5. Schätzungen ([§ 162 AO](https://www.gesetze-im-internet.de/ao_1977/__162.html), [§ 158 AO](https://www.gesetze-im-internet.de/ao_1977/__158.html))

- **Schätzungsgrund**: Der Steuerpflichtige kann über seine Angaben keine ausreichenden Aufklärungen geben, verweigert Auskünfte oder Versicherung an Eides statt, verletzt seine Mitwirkungspflicht (§ 162 Abs. 2 S. 1 AO), oder Bücher und Aufzeichnungen können der Besteuerung nicht nach § 158 Abs. 2 AO zugrunde gelegt werden (§ 162 Abs. 2 S. 2 AO). Formelle Mängel tragen eine Verwerfung nur, wenn sie sachlich gewichtig sind.
- **Schätzungsmethoden** (kein Schätzungsgrund!): innerer/äußerer Betriebsvergleich, Richtsatzsammlung, Geldverkehrs- und Vermögenszuwachsrechnung, Zeitreihenvergleich, Ausbeutekalkulation.
- Verrechnungspreise: Schätzungsrahmen und Zuschläge nach § 162 Abs. 3, 4 AO.
- **Verteidigung**: GoBD-Konformität belegen, methodische Fehler der Kalkulation angreifen (Datenbasis, Zeitraum, Branchenwerte), Alternativrechnung vorlegen, Sicherheitszuschläge auf Plausibilität prüfen.

### 6. Teilabschlussbescheid ([§ 180 Abs. 1a AO](https://www.gesetze-im-internet.de/ao_1977/__180.html))

- Im Rahmen einer Außenprüfung können abgrenzbare Besteuerungsgrundlagen auf Antrag gesondert festgestellt werden, wenn ein Interesse besteht (z. B. Rechtssicherheit für eine Transaktion vor Abschluss der Gesamtprüfung).
- Strategisch nutzen, um unstreitige Komplexe abzuschichten; Bindungswirkung beachten.

### 7. Ablaufhemmung ([§ 171 Abs. 4 AO](https://www.gesetze-im-internet.de/ao_1977/__171.html))

- Beginnt die Prüfung vor Ablauf der Festsetzungsfrist, läuft die Frist nicht ab, bevor die Bescheide unanfechtbar sind oder drei Monate nach Mitteilung über eine ergebnislose Prüfung verstrichen sind (§ 171 Abs. 4 S. 1 AO).
- **Neu:** Die Ablaufhemmung endet **spätestens fünf Jahre nach Ablauf des Kalenderjahres, in dem die Prüfungsanordnung bekannt gegeben wurde** (§ 171 Abs. 4 S. 3 AO) — gilt nur für nach dem 31.12.2024 entstandene Steuern. Verlängerung um Zeiten des antragsgemäßen Hinausschiebens/Unterbrechens (S. 4), um zwischenstaatliche Amtshilfe (S. 5, 6, mindestens ein Jahr) und nach § 200a Abs. 4 S. 1 AO; bei wiederholtem Mitwirkungsverzögerungsgeld binnen fünf Jahren entfällt die Grenze (§ 200a Abs. 4 S. 2 AO); daneben Hemmung nach § 200a Abs. 5 AO.
- Unterbrechung unmittelbar nach Beginn für mehr als sechs Monate aus Gründen der Behörde → keine Hemmung (§ 171 Abs. 4 S. 2 AO). „Scheinhandlungen" zum Prüfungsbeginn dokumentieren.

### 8. Schlussbesprechung ([§ 201 AO](https://www.gesetze-im-internet.de/ao_1977/__201.html)) und Prüfungsbericht ([§ 202 AO](https://www.gesetze-im-internet.de/ao_1977/__202.html))

- Über das Ergebnis ist **in der Regel** eine Schlussbesprechung abzuhalten; sie entfällt, wenn sich keine Änderung der Besteuerungsgrundlagen ergibt oder der Steuerpflichtige verzichtet (§ 201 Abs. 1 AO). Hinweis auf mögliche straf- oder bußgeldrechtliche Würdigung (§ 201 Abs. 2 AO).
- Strategisch entscheidend: Hier werden Konzessionen ausgehandelt; tatsächliche Verständigung über schwer ermittelbare Sachverhalte schriftlich fixieren.
- Prüfungsbericht: schriftlich oder elektronisch; der Steuerpflichtige kann **beantragen**, dass ihm der Bericht vor seiner Auswertung übersandt wird, und erhält Gelegenheit zur Stellungnahme (§ 202 Abs. 2 AO). Ergebnislose Prüfung → Mitteilung nach § 202 Abs. 1 S. 3 AO.

### 9. Rechtsbehelf gegen Bescheide nach der Prüfung

- **Einspruch** § 347 AO binnen Monatsfrist (`/steuerrecht:einspruch-finanzamt`), **AdV** § 361 AO (`/steuerrecht:aussetzung-der-vollziehung`), danach **Klage** beim Finanzgericht (`/steuerrecht:finanzgerichtsklage`).
- Änderungssperre: Nach einer Außenprüfung können Bescheide wegen neuer Tatsachen nur bei Steuerhinterziehung oder leichtfertiger Verkürzung geändert werden (§ 173 Abs. 2 AO); der Vorbehalt der Nachprüfung ist aufzuheben (§ 164 Abs. 3 S. 3 AO).

### 10. Verwaltungsvorschriften: Außenprüfungsordnung statt BpO

- Die **Allgemeine Verwaltungsvorschrift für die Außenprüfung (Außenprüfungsordnung — ApO)** ersetzt die BpO 2000; sie regelt u. a. Risikoorientierung, Rahmenvereinbarungen und die Anschlussprüfung und ist auf laufende Prüfungen anzuwenden. Fundstelle und Anwendungsbeginn sind in Sekundärquellen uneinheitlich angegeben (BStBl I 2026, 1061, ab 10.09.2026 bzw. BStBl I 2026, 950, ab 01.08.2026) `[unverifiziert – prüfen]` — vor Zitat im Schriftsatz im BStBl nachschlagen.

### 11. Sonderprobleme

- **Tax Compliance / IKS**: Ein dokumentiertes innerbetriebliches Kontrollsystem kann gegen Vorsatz und Leichtfertigkeit sprechen (AEAO zu § 153 AO).
- **Strafrechtliches Risiko**: Ergibt sich während der Prüfung ein Anfangsverdacht, ist die Prüfung insoweit zu unterbrechen und der Steuerpflichtige zu belehren (§ 10 der Außenprüfungsordnung, § 393 Abs. 1 AO). Eine Selbstanzeige ist im Umfang der Prüfungsanordnung gesperrt; für nicht erfasste Steuerarten und Zeiträume bleibt sie möglich (`/steuerrecht:selbstanzeige`).
- **§ 153 AO**: Erkennt der Mandant während der Prüfung Fehler in nicht geprüften Jahren, besteht Anzeige- und Berichtigungspflicht.

## Ausgabeformat

```
AUSSENPRÜFUNG — Begleitung — <Mandant> — <Datum> — Rechtsstand Oktober 2026

I.    Prüfungsanordnung
      Bekanntgabe:                    <Datum>
      Zeitraum / Steuerarten:         <…>
      Prüfungsschwerpunkte (§ 197):   <…>
      Vorlageverlangen / Frist:       <…>
      Recht je Jahr:                  <Jahr: alt / neu (Art. 97 § 37 EGAO)>
      Einspruch:                      [erwogen / nicht]

II.   Vorbereitung
      GoBD / Verfahrensdokumentation: [✓ / ⚠️]
      Datenzugriff (Z1/Z2/Z3):        [angekündigt: … — Datenfilter: …]
      Risikoschwerpunkte:             <…>
      Kooperationsrahmen § 199 Abs. 2: [vereinbart / angeboten / —]

III.  Mitwirkung
      Mitwirkungspflichten §§ 90, 200: [erfüllt / Lücken: …]
      Qualifiziertes Mitwirkungsverlangen § 200a: [keins / Eingang … — Frist …]
      Verzögerungsgeld-/Zuschlagsrisiko: <EUR je Tag / —>

IV.   Fristen
      Ablaufhemmung § 171 Abs. 4:     <Ende spätestens 31.12.<Jahr+5> / Altrecht>
      Verlängerungen (§ 200a Abs. 4): <…>

V.    Strittige Feststellungen / Schätzung
      <Feststellung — Schätzungsgrund — Methode — Gegenargument>

VI.   Schlussbesprechung-Strategie
      Verhandlungsspielraum / Kompromisspunkte: <…>
      Teilabschlussbescheid § 180 Abs. 1a: [beantragt / nicht]

VII.  Risikoeinschätzung Mehrergebnis: <EUR Bereich>
VIII. Strafrechtliches Risiko / Selbstanzeige: [keines / niedrig / mittel / hoch]

Folgemaßnahmen:                       <Einspruch / AdV / Klage>
```

## Beispiel (Gutachtenstil, verkürzt)

Die Prüfungsanordnung für KSt, GewSt und USt 2022–2024 wurde am 16.03.2026 bekannt gegeben. Fraglich ist, ob das Finanzamt am 20.10.2026 ein qualifiziertes Mitwirkungsverlangen zur Lagerbewertung stellen durfte. Nach § 200a Abs. 1 AO ist dies frühestens sechs Monate nach Bekanntgabe der Prüfungsanordnung zulässig; diese Frist war mit Ablauf des 16.09.2026 verstrichen. Obwohl die geprüften Steuern vor dem 01.01.2025 entstanden sind, gilt § 200a Abs. 1–3 AO, weil die Prüfungsanordnung nach dem 31.12.2024 bekannt gegeben wurde (Art. 97 § 37 Abs. 3 EGAO). § 200a Abs. 4 und 5 AO und die Fünf-Jahres-Grenze des § 171 Abs. 4 S. 3 AO gelten für diese Jahre dagegen nicht. Ergebnis: Das Verlangen ist zulässig; die Unterlagen sind binnen eines Monats vorzulegen, andernfalls droht ein Mitwirkungsverzögerungsgeld von 75 EUR je Tag.

## Risiken / typische Fehler

- **Zeitliche Anwendung verwechselt** — für vor 2025 entstandene Steuern gelten die Fünf-Jahres-Grenze und § 200a Abs. 4, 5 AO nicht; § 200a Abs. 1–3 und 6 AO aber schon bei Prüfungsanordnung ab 2025.
- **Wiederholte Verzögerung** — ein zweites Mitwirkungsverzögerungsgeld binnen fünf Jahren lässt die Fünf-Jahres-Grenze der Ablaufhemmung entfallen (§ 200a Abs. 4 S. 2 AO).
- **Qualifiziertes Mitwirkungsverlangen unterschätzt** — Monatsfrist versäumt → Mitwirkungsverzögerungsgeld (75 EUR/Tag) und ggf. Zuschlag bis 25.000 EUR/Tag; Festsetzungsfrist verlängert sich.
- **Datenzugriff** als Wahlrecht des Mandanten behandelt — die Behörde wählt (§ 147 Abs. 6 AO); Mandant kann nur anregen und Datenumfang begrenzen.
- **Schätzung** provoziert — Mitwirkungsverweigerung als Strategie führt zu Schätzung nach § 162 AO, die schwer zu beklagen ist; Schätzungsgrund und -methode getrennt angreifen.
- **Hinausschieben beantragt, Folgen übersehen** — verlängert die Ablaufhemmung (§ 171 Abs. 4 S. 4 AO).
- **Schlussbesprechung als Formalität** — wichtigster Verhandlungstermin; Berichtsentwurf nach § 202 Abs. 2 AO beantragen.
- **GoBD-Mängel unterschätzt** — gewichtige Mängel erlauben die Verwerfung der Buchführung (§ 158 Abs. 2 AO).
- **Selbstanzeige** nach Bekanntgabe der Prüfungsanordnung im Prüfungsumfang gesperrt — vorher prüfen; außerhalb des Umfangs bleibt sie möglich. Nie ohne Strafverteidiger-Abstimmung.
- **§ 153 AO-Anzeige vergessen** — bei erkannten Fehlern in nicht geprüften Jahren.

## Quellen

### Statute

- [§§ 193–203 AO](https://www.gesetze-im-internet.de/ao_1977/__193.html) (Außenprüfung), insb. [§ 196 AO](https://www.gesetze-im-internet.de/ao_1977/__196.html), [§ 197 AO](https://www.gesetze-im-internet.de/ao_1977/__197.html), [§ 199 AO](https://www.gesetze-im-internet.de/ao_1977/__199.html), [§ 200 AO](https://www.gesetze-im-internet.de/ao_1977/__200.html), [§ 200a AO](https://www.gesetze-im-internet.de/ao_1977/__200a.html), [§ 201 AO](https://www.gesetze-im-internet.de/ao_1977/__201.html), [§ 202 AO](https://www.gesetze-im-internet.de/ao_1977/__202.html)
- [§ 90 AO](https://www.gesetze-im-internet.de/ao_1977/__90.html), [§ 147 AO](https://www.gesetze-im-internet.de/ao_1977/__147.html), [§ 158 AO](https://www.gesetze-im-internet.de/ao_1977/__158.html), [§ 162 AO](https://www.gesetze-im-internet.de/ao_1977/__162.html)
- [§ 171 AO](https://www.gesetze-im-internet.de/ao_1977/__171.html) (Ablaufhemmung), [§ 180 AO](https://www.gesetze-im-internet.de/ao_1977/__180.html) (Teilabschlussbescheid Abs. 1a)
- [§ 173 AO](https://www.gesetze-im-internet.de/ao_1977/__173.html), [§ 164 AO](https://www.gesetze-im-internet.de/ao_1977/__164.html), [§§ 347 ff. AO](https://www.gesetze-im-internet.de/ao_1977/__347.html), [§ 361 AO](https://www.gesetze-im-internet.de/ao_1977/__361.html)
- [§ 153 AO](https://www.gesetze-im-internet.de/ao_1977/__153.html), [§ 371 AO](https://www.gesetze-im-internet.de/ao_1977/__371.html), [§ 393 AO](https://www.gesetze-im-internet.de/ao_1977/__393.html), [§ 397 AO](https://www.gesetze-im-internet.de/ao_1977/__397.html)
- [Art. 97 § 37 EGAO](https://www.gesetze-im-internet.de/aoeg_1977/art_97__37.html) (zeitliche Anwendung der Reform)
- [FGO](https://www.gesetze-im-internet.de/fgo/)

### Verwaltungsanweisungen

- AEAO zu §§ 193–203a AO
- Außenprüfungsordnung (ApO) 2026, ersetzt die BpO 2000 — Fundstelle siehe Schritt 10 `[unverifiziert – prüfen]`
- BMF, GoBD vom 28.11.2019, geändert am 11.03.2024 und 14.07.2025 (IV D 2 - S 0316/00128/005/088) `[unverifiziert – prüfen]`

### Rechtsprechung

- BFH – IV R 18/24 (Ablaufhemmung durch Datenträgerübergabe; anhängig) `[unverifiziert – prüfen]`

### Literatur

- Drüen, in: Tipke/Kruse, AO/FGO, §§ 193 ff., 200a AO — Lieferungsstand prüfen `[unverifiziert – prüfen]`
- Klein, AO, §§ 171, 200a AO — aktuelle Auflage prüfen `[unverifiziert – prüfen]`
- Suchstring juris/Beck-Online: „§ 200a AO qualifiziertes Mitwirkungsverlangen Mitwirkungsverzögerungsgeld"
