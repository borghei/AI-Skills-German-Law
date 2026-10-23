---
name: tod-des-mieters
description: "Tod des Mieters im Wohnraummietrecht – Eintrittsrecht von Ehegatten, Lebenspartnern, Kindern, Familienangehörigen und Haushaltsangehörigen § 563 BGB mit Ablehnungsfrist von einem Monat, Fortsetzung mit überlebenden Mitmietern § 563a BGB, Haftung und Sicherheit § 563b BGB, Fortsetzung mit dem Erben und beiderseitiges außerordentliches Kündigungsrecht mit gesetzlicher Frist § 564 BGB, § 573d BGB ohne berechtigtes Interesse gegenüber dem Erben, Erbenhaftung als Nachlassverbindlichkeit, Gewerberaum § 580 BGB. Rechtsstand: Oktober 2026. Use when ein Mieter verstorben ist und Angehörige, Mitmieter, Erben oder der Vermieter wissen müssen, wer Vertragspartei wird, wie gekündigt werden kann und wer für Miete und Rückgabe haftet."
language: de
provider_variants: [claude, gemini, openai]
test: ./test.md
---

# /mietrecht:tod-des-mieters

## Zweck

Mit dem Tod des Mieters endet das Mietverhältnis nicht. Das Gesetz bestimmt in einer festen Rangfolge, wer in den Vertrag eintritt, wer ihn fortsetzt und wer ihn kündigen kann. Fast alle Rechte hängen an einer **Monatsfrist ab Kenntnis vom Tod**. Verpasst ein Angehöriger die Ablehnung, ist er Mieter. Verpasst der Erbe die Sonderkündigung, haftet der Nachlass für die volle Kündigungsfrist. Diese Skill bestimmt die Rangfolge, rechnet die Fristen und klärt die Haftung zwischen Eingetretenem, Erben und Nachlass.

**Rechtsstand: Oktober 2026.** §§ 563–564, 573d, 580 BGB sind seit 2001 im Kern unverändert; der anhängige Regierungsentwurf BT-Drs. 21/6807 berührt sie nicht. Zuständig beim BGH ist der **VIII. Zivilsenat** (Wohnraum) bzw. der **XII. Zivilsenat** (Gewerberaum).

## Eingaben

- Todestag; wann haben die Beteiligten und der Vermieter **Kenntnis** erlangt?
- **Vertragsparteien:** Wer war Mieter (Alleinmieter / Mitmieter)?
- **Haushalt:** Wer lebte im gemeinsamen Haushalt (Ehegatte, Lebenspartner, Kinder, andere Angehörige, sonstige Personen mit auf Dauer angelegtem gemeinsamem Haushalt)?
- **Erben:** Testament, Erbschein, Ausschlagung (Frist § 1944 BGB: sechs Wochen), Nachlasspflegschaft
- Mietrückstände, Kaution, Zustand der Wohnung, Schönheitsreparaturklausel
- Erklärungen, die bereits abgegeben wurden (Ablehnung, Kündigung, Schlüsselrückgabe)

## Sub-Agent-Architektur

Die Prüfung wird in Prosa von spezialisierten Schritten getragen; einen `agents`-Block trägt diese Skill bewusst nicht (mietrecht-Konvention).

- Ein **Rangfolge-Prüfer** ordnet die Beteiligten den Stufen der §§ 563, 563a, 564 BGB zu.
- Ein **Fristen-Prüfer** berechnet für jeden Beteiligten die Monatsfrist ab Kenntnis.
- Ein **Kündigungs-Prüfer** bestimmt die Kündigungsrechte und deren Fristen.
- Ein **Haftungs-Prüfer** trennt Haftung des Eingetretenen, des Erben und des Nachlasses und prüft die Sicherheit nach § 563b Abs. 3 BGB.

## Ablauf

### 1. Rangfolge — wer wird Mieter?

| Stufe | Konstellation | Norm | Rechtsfolge |
|---|---|---|---|
| 1 | Verstorbener war **Mitmieter**; Mitmieter lebten im gemeinsamen Haushalt | [§ 563a BGB](https://www.gesetze-im-internet.de/bgb/__563a.html) | Fortsetzung mit den überlebenden Mitmietern |
| 2 | Verstorbener war **Alleinmieter**; Ehegatte oder Lebenspartner im gemeinsamen Haushalt | [§ 563 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__563.html) | Eintritt des Ehegatten / Lebenspartners |
| 3 | Kinder im gemeinsamen Haushalt | § 563 Abs. 2 S. 1 BGB | Eintritt, wenn nicht der Ehegatte oder Lebenspartner eintritt |
| 4 | Andere Familienangehörige und Personen, die mit dem Mieter einen **auf Dauer angelegten gemeinsamen Haushalt** führten | § 563 Abs. 2 S. 2, 3 BGB | Eintritt, wenn nicht der Ehegatte oder der Lebenspartner eintritt |
| 5 | Niemand tritt ein oder setzt fort | [§ 564 BGB](https://www.gesetze-im-internet.de/bgb/__564.html) | Fortsetzung mit dem **Erben** |

Der Eintritt geschieht **kraft Gesetzes** mit dem Tod. Es bedarf keiner Erklärung und keiner Zustimmung des Vermieters.

### 2. Ablehnung des Eintritts ([§ 563 Abs. 3 BGB](https://www.gesetze-im-internet.de/bgb/__563.html))

Ein Eintrittsberechtigter kann innerhalb **eines Monats**, nachdem er vom Tod Kenntnis erlangt hat, dem Vermieter gegenüber **erklären**, dass er das Mietverhältnis nicht fortsetzen will. Dann gilt der Eintritt als nicht erfolgt. Bei mehreren Eintrittsberechtigten kann jeder die Erklärung für sich abgeben. Für geschäftsunfähige oder in der Geschäftsfähigkeit beschränkte Personen gilt § 210 BGB entsprechend (§ 563 Abs. 3 S. 2 BGB): Fehlt ein gesetzlicher Vertreter, endet die Frist nicht vor Ablauf eines Monats, nachdem die Person unbeschränkt geschäftsfähig geworden ist oder der Mangel der Vertretung behoben ist (Ablaufhemmung). Eine Form ist gesetzlich nicht vorgeschrieben, aus Beweisgründen ist Textform mit Zugangsnachweis zu wählen.

### 3. Kündigung durch den Vermieter gegenüber dem Eingetretenen ([§ 563 Abs. 4 BGB](https://www.gesetze-im-internet.de/bgb/__563.html))

Der Vermieter kann das Mietverhältnis innerhalb eines Monats, nachdem er vom endgültigen Eintritt Kenntnis erlangt hat, **außerordentlich mit der gesetzlichen Frist** kündigen, wenn in der Person des Eingetretenen ein **wichtiger Grund** vorliegt. Beispiele sind eine erhebliche Störung des Hausfriedens oder eine offensichtlich fehlende Zahlungsfähigkeit. Die Kündigung bedarf eines berechtigten Interesses (§ 573d Abs. 1 BGB), und die Sozialklausel ist anwendbar.

### 4. Fortsetzung mit überlebenden Mitmietern ([§ 563a BGB](https://www.gesetze-im-internet.de/bgb/__563a.html))

Die überlebenden Mitmieter können das Mietverhältnis innerhalb eines Monats nach Kenntnis vom Tod **außerordentlich mit der gesetzlichen Frist** kündigen (§ 563a Abs. 2 BGB). Ein Kündigungsrecht des Vermieters aus diesem Anlass besteht nicht.

### 5. Haftung und Sicherheit ([§ 563b BGB](https://www.gesetze-im-internet.de/bgb/__563b.html))

- Für die bis zum Tod entstandenen Verbindlichkeiten haften die Eingetretenen bzw. Fortsetzenden **neben dem Erben als Gesamtschuldner**. Im Innenverhältnis haftet allein der Erbe, soweit nichts anderes bestimmt ist (Abs. 1).
- Hat der Verstorbene Miete im Voraus entrichtet, schulden die Eingetretenen dem Erben den ersparten Betrag (Abs. 2).
- Der Vermieter kann von den Eingetretenen eine **Sicherheit** nach § 551 BGB verlangen, wenn der Verstorbene keine geleistet hatte (Abs. 3).

### 6. Fortsetzung mit dem Erben ([§ 564 BGB](https://www.gesetze-im-internet.de/bgb/__564.html), [§ 573d BGB](https://www.gesetze-im-internet.de/bgb/__573d.html))

Tritt niemand ein und wird das Mietverhältnis nicht nach § 563a BGB fortgesetzt, wird es mit dem Erben fortgesetzt (§ 564 S. 1 BGB). **Erbe und Vermieter** können dann innerhalb **eines Monats**, nachdem sie vom Tod **und** davon Kenntnis erlangt haben, dass ein Eintritt oder eine Fortsetzung nicht erfolgt ist, **außerordentlich mit der gesetzlichen Frist** kündigen (§ 564 S. 2 BGB).

- **Gesetzliche Frist:** § 573d Abs. 2 BGB — spätestens am dritten Werktag eines Kalendermonats zum Ablauf des übernächsten Monats (rund drei Monate).
- **Kein berechtigtes Interesse:** Die Kündigung des Vermieters **gegenüber dem Erben** nach § 564 BGB bedarf keines berechtigten Interesses; § 573d Abs. 1 BGB nimmt diesen Fall ausdrücklich aus.
- **Form:** Schriftform (§ 568 Abs. 1 BGB), gerichtet an **alle** Erben; bei unbekannten Erben über einen Nachlasspfleger (§ 1961 BGB).
- **Verpasste Frist:** Danach gelten die allgemeinen Regeln; für den Erben die ordentliche Kündigung nach § 573c BGB, für den Vermieter nur noch mit berechtigtem Interesse.

### 7. Erbenhaftung

Verbindlichkeiten aus dem nach § 564 BGB fortgesetzten Mietverhältnis, die nach dem Erbfall bis zur Beendigung fällig werden, sind jedenfalls dann **reine Nachlassverbindlichkeiten**, wenn der Erbe fristgerecht nach § 564 S. 2 BGB kündigt. Der Erbe kann seine Haftung deshalb auf den Nachlass beschränken, etwa mit der Dürftigkeitseinrede nach § 1990 BGB (BGH, Urt. v. 23.01.2013 – VIII ZR 68/12, NJW 2013, 933, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2013-01-23&Aktenzeichen=VIII%20ZR%2068/12). Ob der Erbe persönlich haftet, wenn er die Wohnung nach dem Erbfall selbst nutzt oder nicht kündigt, ist gesondert zu prüfen. Eine **Ausschlagung** der Erbschaft (§§ 1942 ff. BGB) beseitigt die Erbenstellung rückwirkend; bei überschuldetem Nachlass ist sie vorrangig zu prüfen.

Rückgabe, Räumung und Schönheitsreparaturen sind Pflichten des jeweiligen Mieters bzw. des Erben. Die sechsmonatige Verjährung nach § 548 BGB beginnt mit dem **Rückerhalt**. Vertiefung: `/mietrecht:schoenheitsreparaturen-rueckgabe`, `/mietrecht:kaution-mietsicherheit`.

### 8. Gewerberaum ([§ 580 BGB](https://www.gesetze-im-internet.de/bgb/__580.html))

Bei anderen Mietverhältnissen als über Wohnraum können **Erbe und Vermieter** innerhalb eines Monats nach Kenntnis vom Tod außerordentlich mit der gesetzlichen Frist (§ 580a Abs. 4 BGB) kündigen. Ein Eintrittsrecht von Angehörigen besteht nicht.

## Deterministische Berechnung

```bash
# Monatsfrist § 563 Abs. 3 / § 564 S. 2 BGB: Kenntnis vom Tod am 12.10.2026
python -m scripts.legal_calc.cli frist --ereignis 12.10.2026 --menge 1 --einheit monate --land SN

# Ausschlagungsfrist § 1944 BGB: sechs Wochen ab Kenntnis vom Anfall und Berufungsgrund
python -m scripts.legal_calc.cli frist --ereignis 12.10.2026 --menge 6 --einheit wochen --land SN
```

Die Kenntnis ist für jeden Beteiligten gesondert festzustellen und bleibt eine juristische Eingabe. Die gesetzliche Kündigungsfrist des § 573d Abs. 2 BGB ist eine Kalenderregel (dritter Werktag, Ablauf des übernächsten Monats) und von Hand gegen den Wortlaut zu prüfen.

## Quellen

### Statute

- [§ 563 BGB](https://www.gesetze-im-internet.de/bgb/__563.html), [§ 563a BGB](https://www.gesetze-im-internet.de/bgb/__563a.html), [§ 563b BGB](https://www.gesetze-im-internet.de/bgb/__563b.html), [§ 564 BGB](https://www.gesetze-im-internet.de/bgb/__564.html)
- [§ 573d BGB](https://www.gesetze-im-internet.de/bgb/__573d.html), [§ 568 BGB](https://www.gesetze-im-internet.de/bgb/__568.html), [§ 551 BGB](https://www.gesetze-im-internet.de/bgb/__551.html), [§ 580 BGB](https://www.gesetze-im-internet.de/bgb/__580.html), [§ 580a BGB](https://www.gesetze-im-internet.de/bgb/__580a.html)
- [§ 1922 BGB](https://www.gesetze-im-internet.de/bgb/__1922.html), [§ 1944 BGB](https://www.gesetze-im-internet.de/bgb/__1944.html), [§ 1961 BGB](https://www.gesetze-im-internet.de/bgb/__1961.html), [§ 1990 BGB](https://www.gesetze-im-internet.de/bgb/__1990.html)

### Kommentare

- Streyl, in: Schmidt-Futterer, Mietrecht, 16. Aufl. 2024, §§ 563–564 BGB `[unverifiziert – prüfen]` (Bearbeiter vor Zitat prüfen)
- Blank/Börstinghaus, Miete, aktuelle Auflage, § 563 Rn. 1 ff.

### Rechtsprechung

- BGH, Urt. v. 23.01.2013 – VIII ZR 68/12, NJW 2013, 933 = NZM 2013, 185 (nach dem Erbfall fällig werdende Forderungen als reine Nachlassverbindlichkeiten; Haftungsbeschränkung des Erben) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2013-01-23&Aktenzeichen=VIII%20ZR%2068/12
- Zum „auf Dauer angelegten gemeinsamen Haushalt" i.S.d. § 563 Abs. 2 S. 3 BGB und zum wichtigen Grund i.S.d. § 563 Abs. 4 BGB ist die einschlägige Rechtsprechung heranzuziehen `[unverifiziert – prüfen]`.

## Formulierungshilfe — Sonderkündigung des Erben (§ 564 S. 2 BGB)

```
Sehr geehrte Damen und Herren,

Ihre Mieterin, Frau <Name>, ist am <Datum> verstorben. Ich bin ihr
<alleiniger / Mit->Erbe (Erbschein / Testament anbei in Kopie). Ein Eintritt
nach § 563 BGB oder eine Fortsetzung nach § 563a BGB ist nicht erfolgt;
im Haushalt der Verstorbenen lebte niemand.

Hiermit kündige ich das Mietverhältnis über die Wohnung <Anschrift>
außerordentlich mit der gesetzlichen Frist gemäß §§ 564 S. 2, 573d Abs. 2 BGB
zum <Datum>.

Ich weise darauf hin, dass ich für Verbindlichkeiten aus dem Mietverhältnis
nur mit dem Nachlass hafte.

<eigenhändige Unterschrift aller Erben>
```

## Ausgabeformat

```
TOD DES MIETERS — Prüfung — <Mandat-ID> — <Datum>

I.    Todestag / Kenntnis               <Datum> / je Beteiligtem: <…>
II.   Rangfolge
      - Mitmieter (§ 563a)              [ja: <Namen> / nein]
      - Ehegatte / Lebenspartner (§ 563 Abs. 1) [ja / nein]
      - Kinder / Angehörige / Haushalt (§ 563 Abs. 2) [<Namen> / nein]
      - Erbe (§ 564)                    [<Namen> / unbekannt → Nachlasspfleger]
III.  Fristen (1 Monat ab Kenntnis)
      - Ablehnung § 563 Abs. 3          bis <Datum>  [erklärt / offen / versäumt]
      - Kündigung Mitmieter § 563a Abs. 2 bis <Datum>
      - Kündigung Erbe / Vermieter § 564 S. 2 bis <Datum>
      - Kündigung Vermieter § 563 Abs. 4 bis <Datum>
IV.   Beendigung (§ 573d Abs. 2)        zum <Datum>
V.    Haftung
      - bis Tod: Gesamtschuld (§ 563b Abs. 1)
      - danach: Nachlassverbindlichkeit (VIII ZR 68/12) [Beschränkung möglich / persönliche Haftung]
      - Sicherheit § 563b Abs. 3        [verlangt / N/A]
VI.   Ausschlagung (§ 1944)             bis <Datum>  [geprüft / offen]

Ergebnis: <…>
Risiko: [🟢 / 🟡 / 🔴]
```

## Risiken / typische Fehler

- **Ablehnungsfrist verpasst** — wer im Haushalt lebte und nicht binnen eines Monats ablehnt, ist Mieter mit allen Pflichten.
- **Erbe statt Eintrittsberechtigtem als Vertragspartei behandelt** — vorrangig sind Mitmieter, Ehegatte, Lebenspartner und Haushaltsangehörige.
- **Sonderkündigungsfrist des § 564 S. 2 BGB versäumt** — danach bleibt dem Erben nur die ordentliche Kündigung.
- **Kündigung nicht an alle Erben gerichtet** — die Kündigung ist dann unwirksam; bei unbekannten Erben ist ein Nachlasspfleger zu bestellen.
- **Berechtigtes Interesse bei Kündigung gegenüber dem Erben verlangt** — § 573d Abs. 1 BGB nimmt die Kündigung nach § 564 BGB aus.
- **Haftungsbeschränkung übersehen** — Forderungen nach dem Erbfall sind Nachlassverbindlichkeiten; bei überschuldetem Nachlass Ausschlagung oder Dürftigkeitseinrede prüfen.
