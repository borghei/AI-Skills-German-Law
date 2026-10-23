---
name: selbstanzeige
description: "Prüfung der strafbefreienden Selbstanzeige bei Steuerhinterziehung – Vollständigkeitsgebot und Zehn-Jahres-Berichtigungsverbund § 371 Abs. 1 AO, Sperrgründe § 371 Abs. 2 AO (Prüfungsanordnung beschränkt auf den angekündigten Prüfungsumfang, Einleitung, Erscheinen, Nachschau, Tatentdeckung, 25.000-EUR-Grenze, besonders schwerer Fall), Teilselbstanzeige bei Voranmeldungen § 371 Abs. 2a, Nachzahlungsfrist § 371 Abs. 3, Dritte § 371 Abs. 4, Hinterziehungszinsen § 235 AO, Zuschlag und Absehen von Verfolgung § 398a AO, Abgrenzung zu § 153 AO und § 378 Abs. 3 AO. Use when eine strafbefreiende Selbstanzeige nach § 371 AO vorbereitet oder auf Wirksamkeit geprüft wird."
language: de
provider_variants:
  - claude
  - gemini
  - openai
test: ./test.md
---

# /steuerrecht:selbstanzeige

> **Rechtsstand: Oktober 2026.** § 371 AO beruht auf der Reform zum 01.01.2015 und wurde seither punktuell geändert: § 371 Abs. 2 S. 1 Nr. 4 AO verweist seit dem Steuerumgehungsbekämpfungsgesetz vom 23.06.2017 auf § 370 Abs. 3 S. 2 Nr. 2 **bis 6** AO (zuvor bis 5), und § 371 Abs. 3 S. 1 AO erfasst seit dem JStG 2022 auch Verzugszinsen nach dem Zollkodex der Union. In den Jahren 2025–2026 ist keine Gesetzesänderung und keine Leitentscheidung bekannt geworden, die den Prüfungsmaßstab verschiebt (vor Abgabe in juris prüfen). Mittelbar relevant ist der Entwurf JStG 2026 (BT-Drs. 21/8283): Die nach § 235 Abs. 4 AO anzurechnenden Zinsen nach § 233a AO sollen ab 01.01.2027 mit 0,3 % statt 0,15 % je Monat bemessen werden; die Hinterziehungszinsen bleiben bei 0,5 % je Monat.

## Zweck

Die strafbefreiende Selbstanzeige nach [§ 371 AO](https://www.gesetze-im-internet.de/ao_1977/__371.html) ist der einzige Weg, nach vollendeter Steuerhinterziehung ([§ 370 AO](https://www.gesetze-im-internet.de/ao_1977/__370.html)) noch Straffreiheit zu erlangen. Sie ist ein „Alles-oder-Nichts"-Instrument: Wirkt sie nicht vollständig, entfaltet sie keine Sperrwirkung gegen die Strafverfolgung und liefert der Behörde zugleich ein Geständnis. Dieser Skill prüft die Wirksamkeitsvoraussetzungen, identifiziert Sperrgründe und steuert die fristgerechte Nachzahlung. Für die Strafverteidigung im eingeleiteten Verfahren siehe das Gebiet `wirtschafts-steuerstrafrecht`.

## Eingaben

- Betroffene Steuerarten und Veranlagungs-/Voranmeldungszeiträume (ESt, KSt, USt, LSt, ErbSt)
- Hinterziehungsvolumen **je Tat** (je Steuerart und Zeitraum), Anhaltspunkte für einen besonders schweren Fall
- Laufende Prüfung (Prüfungsanordnung mit Umfang), Nachschau, Ermittlung oder bekannt gegebene Einleitung
- Datenlage der Behörde (Kontrollmitteilungen, CRS-/DAC-Meldungen, Datenankäufe, Presseberichte)
- Vollständigkeit und Belegbarkeit der nachzuerklärenden Angaben
- Beteiligte (Steuerpflichtiger, Mittäter, Gehilfen, Begünstigte, Erben)
- Liquidität zur fristgerechten Nachzahlung von Steuer, Zinsen und ggf. Zuschlag

## Sub-Agent-Architektur

Ein **Tatbestands-Prüfer** klärt, ob vorsätzliche Steuerhinterziehung, leichtfertige Verkürzung (§ 378 AO) oder eine schlichte Berichtigung nach § 153 AO vorliegt. Ein **Wirksamkeits-Prüfer** rekonstruiert das Vollständigkeitsgebot, durchmustert sämtliche Sperrgründe je Tat und bestimmt das noch offene Zeitfenster. Ein **Folgen-Prüfer** berechnet Nachzahlung, Hinterziehungszinsen und Zuschlag nach § 398a AO und plant die Liquidität. Die Rollen arbeiten streng sequentiell, weil jede Stufe die nächste sperren kann; das Ergebnis wird mit der Strafverteidigung abgestimmt.

## Ablauf

### 1. Abgrenzung: § 370 AO, § 378 AO, § 153 AO

- [§ 370 AO](https://www.gesetze-im-internet.de/ao_1977/__370.html) setzt **Vorsatz** voraus (auch bedingter Vorsatz genügt).
- [§ 378 AO](https://www.gesetze-im-internet.de/ao_1977/__378.html): Leichtfertige Steuerverkürzung → bußgeldbefreiende Selbstanzeige nach § 378 Abs. 3 AO; kein Vollständigkeitsgebot in der strengen Form, Sperre nur durch bekannt gegebene Einleitung eines Straf- oder Bußgeldverfahrens.
- [§ 153 AO](https://www.gesetze-im-internet.de/ao_1977/__153.html): Nachträgliches Erkennen einer Unrichtigkeit ohne ursprünglichen Vorsatz → **Berichtigungspflicht** „unverzüglich"; ihre Verletzung ist selbst Hinterziehung durch Unterlassen.
- **Praxis**: Im Zweifel die Erklärung so formulieren, dass sie die Anforderungen des § 371 AO erfüllt und zugleich als Berichtigung nach § 153 AO trägt — ohne ein Vorsatzgeständnis zu formulieren.

### 2. Vollständigkeitsgebot ([§ 371 Abs. 1 AO](https://www.gesetze-im-internet.de/ao_1977/__371.html))

Das **Vollständigkeitsgebot** verlangt die Berichtigung, Ergänzung oder Nachholung der Angaben zu **allen unverjährten Steuerstraftaten einer Steuerart**, mindestens aber zu allen Steuerstraftaten dieser Steuerart **innerhalb der letzten zehn Kalenderjahre** (§ 371 Abs. 1 S. 2 AO).

- Keine „Teilselbstanzeige" (Ausnahme: Voranmeldungen, Schritt 4): Wird auch nur ein Sachverhalt derselben Steuerart bewusst ausgespart, ist die gesamte Selbstanzeige unwirksam. Auslöser der Rechtslage war BGH, Beschl. v. 20.05.2010 – 1 StR 577/09 `[unverifiziert – prüfen]`.
- Materielle Vollständigkeit: Die Angaben müssen der Behörde eine Veranlagung ohne weitere Ermittlungen ermöglichen; belastbare Schätzungen mit Sicherheitszuschlag sind zulässig. Geringfügige, unbewusste Abweichungen sind nach h. M. unschädlich `[unverifiziert – prüfen]`.
- Zehn-Jahres-Berichtigungsverbund gilt auch für strafrechtlich verjährte, aber in den Verbund fallende Jahre; bei besonders schweren Fällen gilt die verlängerte Strafverfolgungsverjährung von 15 Jahren (§ 376 Abs. 1 AO).

### 3. Sperrgründe ([§ 371 Abs. 2 S. 1 AO](https://www.gesetze-im-internet.de/ao_1977/__371.html))

Liegt ein **Sperrgrund** vor, tritt keine Straffreiheit ein. Jeder Sperrgrund ist **je Tat** zu prüfen:

| Nr. | Sperrgrund | Reichweite |
|---|---|---|
| 1 a | **Prüfungsanordnung** nach § 196 AO bekannt gegeben (an Täter, Teilnehmer, Begünstigten oder deren Vertreter) | **beschränkt auf den sachlichen und zeitlichen Umfang der angekündigten Außenprüfung** |
| 1 b | **Bekanntgabe der Einleitung** eines Straf- oder Bußgeldverfahrens | die Tat, wegen der eingeleitet wurde |
| 1 c | **Erscheinen des Prüfers** zur steuerlichen Prüfung | beschränkt auf den Umfang der Außenprüfung |
| 1 d | Erscheinen eines Amtsträgers zur Ermittlung einer Steuerstraftat/-ordnungswidrigkeit | die Tat |
| 1 e | Erscheinen zu einer **Umsatzsteuer-, Lohnsteuer- oder sonstigen Nachschau** (z. B. Kassen-Nachschau § 146b AO), wenn sich der Amtsträger **ausgewiesen** hat | Gegenstand der Nachschau |
| 2 | **Tatentdeckung**: Die Tat war ganz oder teilweise entdeckt und der Täter wusste dies oder musste bei verständiger Würdigung damit rechnen | die entdeckte Tat |
| 3 | verkürzte Steuer oder nicht gerechtfertigter Vorteil **über 25.000 EUR je Tat** | → nur § 398a AO |
| 4 | **besonders schwerer Fall** nach § 370 Abs. 3 S. 2 Nr. 2–6 AO | → nur § 398a AO |

- Nach § 371 Abs. 2 S. 2 AO hindern die Sperren nach Nr. 1 a und c nicht die Selbstanzeige zu Steuerarten, die **nicht** Gegenstand der angekündigten Prüfung sind — das Zeitfenster für andere Steuerarten oder Jahre bleibt offen.
- **Tatentdeckung** heute besonders durch automatischen Informationsaustausch (CRS, DAC6/DAC7, Kontenabruf) und Datenankäufe: Kenntnis der Behörde allein genügt nicht, wohl aber ein Abgleich, der die Tat wahrscheinlich macht `[unverifiziert – prüfen]`.

### 4. Voranmeldungen: Teilselbstanzeige zulässig ([§ 371 Abs. 2a AO](https://www.gesetze-im-internet.de/ao_1977/__371.html))

- Bei **Umsatzsteuervoranmeldungen und Lohnsteueranmeldungen** tritt Straffreiheit in dem Umfang ein, in dem korrekt berichtigt wird — abweichend vom Vollständigkeitsgebot und von der 25.000-EUR-Grenze.
- Die Tatentdeckungssperre (Nr. 2) greift nicht, wenn die Entdeckung auf der berichtigten oder nachgeholten Voranmeldung selbst beruht.
- **Nicht** für Jahresanmeldungen (USt-Jahreserklärung, Jahreslohnsteueranmeldung): hier gilt wieder das volle Vollständigkeitsgebot.
- Die fristgerechte Zahlung der Zinsen ist in diesen Fällen unerheblich (§ 371 Abs. 3 S. 2 AO).

### 5. Fristgerechte Nachzahlung ([§ 371 Abs. 3 AO](https://www.gesetze-im-internet.de/ao_1977/__371.html))

Ist die Steuerverkürzung eingetreten, tritt Straffreiheit nur ein, wenn der Täter die zu seinen Gunsten hinterzogenen Steuern **sowie** die Zinsen innerhalb der ihm bestimmten angemessenen Frist **nachzahlt**:

- **Hinterziehungszinsen** nach [§ 235 AO](https://www.gesetze-im-internet.de/ao_1977/__235.html): 0,5 % je vollem Monat ([§ 238 AO](https://www.gesetze-im-internet.de/ao_1977/__238.html)); Zinsen nach [§ 233a AO](https://www.gesetze-im-internet.de/ao_1977/__233a.html) werden angerechnet (§ 235 Abs. 4 AO) und sind ebenfalls fristgerecht zu entrichten.
- Die **Nachzahlungsfrist** wird im Strafverfahren (Bußgeld- und Strafsachenstelle bzw. Staatsanwaltschaft) gesetzt. Sie ist von der **Stundung** der Steuer durch die Erhebungsstelle (§ 222 AO) zu unterscheiden: Eine steuerliche Stundung oder ein Vollstreckungsaufschub verlängert die strafrechtliche Zahlungsfrist **nicht** `[unverifiziert – prüfen]`. Fristverlängerung bei der Straf- und Bußgeldsachenstelle **vor** Fristablauf beantragen.
- Liquiditätsprüfung vorab: Reicht das Vermögen nicht, wird die Selbstanzeige gleichwohl strafmildernd berücksichtigt, die Straffreiheit ist aber gefährdet.
- **Dritte** ([§ 371 Abs. 4 AO](https://www.gesetze-im-internet.de/ao_1977/__371.html)): Erstattet ein Dritter (z. B. Erbe) die Anzeige nach § 153 AO rechtzeitig und ordnungsgemäß, wird der Dritte, der die Erklärung unterlassen oder unrichtig abgegeben hat, nicht verfolgt — es sei denn, ihm oder seinem Vertreter war zuvor die Einleitung bekannt gegeben; hat er zum eigenen Vorteil gehandelt, gilt Abs. 3 entsprechend.

### 6. Zuschlag und Absehen von Verfolgung ([§ 398a AO](https://www.gesetze-im-internet.de/ao_1977/__398a.html))

Tritt Straffreiheit nur wegen § 371 Abs. 2 S. 1 Nr. 3 oder Nr. 4 AO nicht ein, wird von der Verfolgung abgesehen, wenn der Täter innerhalb angemessener Frist die Steuern und Zinsen entrichtet **und** einen **Zuschlag** zahlt:

- **10 %** der hinterzogenen Steuer bis 100.000 EUR,
- **15 %** über 100.000 EUR bis 1.000.000 EUR,
- **20 %** über 1.000.000 EUR.

Der **Zuschlag** wird je Tat berechnet; das Kompensationsverbot des § 370 Abs. 4 S. 3 AO gilt für die Bemessung (§ 398a Abs. 2 AO). Er wird nicht erstattet, wenn die Rechtsfolge nicht eintritt, kann aber auf eine spätere Geldstrafe angerechnet werden (§ 398a Abs. 4 AO). Bei späterer Unrichtigkeit oder Unvollständigkeit wird das Verfahren wieder aufgenommen (§ 398a Abs. 3 AO). § 398a AO ist ein Verfolgungshindernis, kein Freispruch.

### 7. Berater- und Berufsrechtsrisiken

- **Eigene Strafbarkeit des Beraters** (Beihilfe zu § 370 AO, § 27 StGB) bei Mitwirkung an der ursprünglichen Erklärung gesondert prüfen; ggf. Mandatsniederlegung und eigene Anzeige nach § 371 AO.
- **Mandatsannahme**: Selbstanzeige nur nach klarer schriftlicher Beauftragung; Interessenkonflikte bei mehreren Beteiligten (§ 43a Abs. 4 BRAO, § 57 StBerG).
- **Dokumentation**: Vollständigkeit der erhaltenen Unterlagen aktenkundig machen.
- **Verschwiegenheit**: keine Offenbarung für Dritte ohne Mandatsdeckung (§ 203 StGB).

### 8. Ergebnis

- Wirksamkeit je Tat: wirksam / unwirksam / nur über § 398a AO.
- Offene Sperrgründe und verbleibendes Zeitfenster (je Steuerart und Jahr).
- Bezifferte Nachzahlung: Steuer + Hinterziehungszinsen (+ Zuschlag), Zahlungsplan.
- Empfehlung: sofortige Abgabe (ggf. gestufte Selbstanzeige mit Schätzung und Nachreichung) / Nachschärfung / Abstimmung mit Strafverteidiger.

## Ausgabeformat

```
SELBSTANZEIGE — Wirksamkeitsprüfung — <Mandant> — <Datum> — Rechtsstand Oktober 2026

I.    Tatbestand
      Steuerhinterziehung § 370 (Vorsatz):   [ja / nein → § 378 Abs. 3 / § 153 AO]
      Betroffene Steuerarten / Jahre:        <…>
      Hinterziehungsvolumen je Tat:          <EUR>

II.   Vollständigkeitsgebot § 371 Abs. 1
      Alle Taten einer Steuerart erfasst:    [✓ / ⚠️ Lücke: …]
      Zeitraum (mind. 10 Kalenderjahre):     <…>
      Materielle Vollständigkeit/Schätzung:  [✓ / nachschärfen]
      Voranmeldungen (Abs. 2a):              [Teilberichtigung zulässig / —]

III.  Sperrgründe § 371 Abs. 2
      Prüfungsanordnung (Umfang):            [nein / ja: Steuerarten …, Jahre …]
      Bekanntgabe Einleitung:                [nein / ja]
      Erscheinen Prüfer / Ermittler:         [nein / ja]
      Nachschau (Nr. 1 e):                   [nein / ja]
      Tatentdeckung:                         [nein / ja / Risiko]
      Betrag > 25.000 EUR / bes. schwerer Fall: [nein / ja → § 398a]

IV.   Nachzahlung § 371 Abs. 3
      Hinterzogene Steuer:                   <EUR>
      Hinterziehungszinsen § 235:            <EUR>
      Zuschlag § 398a (10/15/20 %):          <EUR / —>
      Nachzahlungsfrist / Liquidität:        <…>

V.    Beraterrisiken:                        <…>

Ergebnis:  [wirksam / unwirksam / nur über § 398a]
Folgemaßnahmen:  <sofort abgeben / nachschärfen / Strafverteidiger>
```

## Beispiel (Gutachtenstil, verkürzt)

M hat Kapitalerträge aus einem Schweizer Depot für 2016–2024 nicht erklärt; die verkürzte ESt beträgt je Jahr 4.000–9.000 EUR. Eine Prüfungsanordnung liegt nur für die USt 2022–2024 seines Einzelunternehmens vor. Fraglich ist, ob eine Selbstanzeige zur ESt gesperrt ist. Die Sperre nach § 371 Abs. 2 S. 1 Nr. 1 a AO ist auf den sachlichen und zeitlichen Umfang der angekündigten Außenprüfung beschränkt; die ESt ist nicht Prüfungsgegenstand. Die Betragsgrenze von 25.000 EUR je Tat ist nicht überschritten. Eine Tatentdeckung ist nicht ersichtlich, solange keine Anhaltspunkte für einen bereits erfolgten CRS-Abgleich vorliegen. Ergebnis: Die Selbstanzeige zur ESt ist möglich; sie muss nach dem Vollständigkeitsgebot alle unverjährten Taten, mindestens die Jahre der letzten zehn Kalenderjahre, umfassen. Die Steuer nebst Hinterziehungszinsen ist innerhalb der gesetzten Frist nachzuzahlen.

## Risiken / typische Fehler

- **Teilselbstanzeige** — Aussparen eines Sachverhalts derselben Steuerart macht die gesamte Anzeige unwirksam (Vollständigkeitsgebot); Ausnahme nur bei Voranmeldungen (§ 371 Abs. 2a AO), nicht bei Jahreserklärungen.
- **Sperrgrund Prüfungsanordnung falsch abgegrenzt** — zu weit verstanden (Selbstanzeige zu nicht geprüften Steuerarten unterlassen) oder zu eng (geprüfte Jahre doch einbezogen).
- **Nachschau übersehen** — Erscheinen zur USt-, LSt- oder Kassen-Nachschau mit Ausweis sperrt (§ 371 Abs. 2 S. 1 Nr. 1 e AO).
- **Wettlauf mit der Tatentdeckung** — verzögerte Abgabe lässt einen Sperrgrund reifen; automatischer Informationsaustausch beschleunigt die Entdeckung.
- **Zu knappe Schätzung** — materielle Unvollständigkeit; stets Sicherheitszuschlag ansetzen.
- **Nachzahlungsfrist mit Stundung verwechselt** — steuerliche Stundung verlängert die strafrechtliche Frist nicht; Hinterziehungszinsen § 235 AO bzw. Zuschlag § 398a AO fristgerecht zahlen.
- **Betragsgrenze 25.000 EUR oder besonders schwerer Fall verkannt** — § 371 AO gesperrt, Weg führt nur über § 398a AO.
- **§ 153 AO mit § 371 AO verwechselt** — bei fehlendem Vorsatz genügt die Berichtigung; eine „Selbstanzeige" wäre ein überschießendes Geständnis.
- **Selbstanzeige ohne Strafverteidiger-Abstimmung** — Eigenbelastung von Mandant und Berater riskiert.

## Quellen

### Statute

- [§ 371 AO](https://www.gesetze-im-internet.de/ao_1977/__371.html) (Selbstanzeige; Abs. 1 Vollständigkeit, Abs. 2 Sperrgründe, Abs. 2a Voranmeldungen, Abs. 3 Nachzahlung, Abs. 4 Dritte)
- [§ 398a AO](https://www.gesetze-im-internet.de/ao_1977/__398a.html) (Absehen von Verfolgung — Zuschlag)
- [§ 370 AO](https://www.gesetze-im-internet.de/ao_1977/__370.html) (Steuerhinterziehung), [§ 376 AO](https://www.gesetze-im-internet.de/ao_1977/__376.html) (Verfolgungsverjährung), [§ 378 AO](https://www.gesetze-im-internet.de/ao_1977/__378.html) (leichtfertige Steuerverkürzung)
- [§ 153 AO](https://www.gesetze-im-internet.de/ao_1977/__153.html) (Anzeige- und Berichtigungspflicht), [§ 146b AO](https://www.gesetze-im-internet.de/ao_1977/__146b.html) (Kassen-Nachschau)
- [§ 235 AO](https://www.gesetze-im-internet.de/ao_1977/__235.html) (Hinterziehungszinsen), [§ 233a AO](https://www.gesetze-im-internet.de/ao_1977/__233a.html), [§ 238 AO](https://www.gesetze-im-internet.de/ao_1977/__238.html) (Zinshöhe)
- [§ 222 AO](https://www.gesetze-im-internet.de/ao_1977/__222.html) (Stundung — Abgrenzung)

### Gesetzgebung (nicht in Kraft)

- Regierungsentwurf JStG 2026, BT-Drs. 21/8283, Art. 18 Nr. 14 (§ 238 Abs. 1a AO: 0,3 % für § 233a-Zinsen ab 01.01.2027)

### Verwaltungsanweisungen

- AEAO zu § 153 AO (Abgrenzung Berichtigung / Selbstanzeige; Tax-Compliance-System)
- Anweisungen für das Straf- und Bußgeldverfahren (Steuer) — AStBV (St), jeweils aktuelle Fassung `[unverifiziert – prüfen]`

### Rechtsprechung (alle `[unverifiziert – prüfen]`)

- BGH, Beschl. v. 20.05.2010 – 1 StR 577/09 (Unwirksamkeit der Teilselbstanzeige nach altem Recht; historischer Hintergrund der Reform 2011)
- BGH-Rechtsprechung zur Tatentdeckung und zur Nachschau-Sperre — vor Zitat Az. in juris ermitteln (Suchstring: „§ 371 Abs. 2 Nr. 2 AO Tatentdeckung Kontrollmitteilung")

### Literatur

- Klein, AO, § 371, § 398a — aktuelle Auflage prüfen `[unverifiziert – prüfen]`
- Joecks/Jäger/Randt, Steuerstrafrecht, 9. Aufl. 2023, § 371 AO `[unverifiziert – prüfen]`
- Schwarz/Pahlke/Keß, AO/FGO, § 371, § 398a `[unverifiziert – prüfen]`
