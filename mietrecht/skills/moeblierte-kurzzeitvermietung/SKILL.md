---
name: moeblierte-kurzzeitvermietung
description: "Möblierte Vermietung und Wohnen auf Zeit – Ausnahmen vom Wohnraummietrecht § 549 Abs. 2 Nr. 1 (vorübergehender Gebrauch) und Nr. 2 BGB (möblierter Wohnraum in der Vermieterwohnung), verkürzte Kündigungsfrist § 573c Abs. 3 BGB, Befristung § 575 BGB, Möblierungszuschlag und Mietpreisbremse §§ 556d, 556g BGB, Umgehungsprüfung, Zweckentfremdungsrecht der Länder; anhängige Reform BT-Drs. 21/6807 (Höchstdauer sechs bzw. acht Monate, Möblierungszuschlag-Ausweisung § 556d Abs. 1a, § 556g Abs. 1b BGB-E) mit Übergangsrecht. Rechtsstand: Oktober 2026. Use when eine möblierte oder befristete Wohnung vermietet, ein Möblierungszuschlag geprüft oder eine Kurzzeitvermietung als Umgehung der Mietpreisbremse angegriffen wird."
language: de
provider_variants: [claude, gemini, openai]
test: ./test.md
---

# /mietrecht:moeblierte-kurzzeitvermietung

## Zweck

Möblierte Wohnungen auf Zeit sind in angespannten Märkten zum Hauptweg geworden, die Mietpreisbremse und den Kündigungsschutz zu umgehen. Die Umgehung funktioniert aber nur, wenn tatsächlich ein Ausnahmetatbestand des § 549 Abs. 2 BGB vorliegt. Liegt keiner vor, gilt das volle Wohnraummietrecht, und der Möblierungszuschlag ist Teil der an § 556d BGB zu messenden Miete. Diese Skill prüft die Ausnahmetatbestände, bewertet den Möblierungszuschlag und trennt das geltende Recht vom anhängigen Regierungsentwurf.

**Rechtsstand: Oktober 2026.**

- **Geltend:** § 549 Abs. 2 BGB ohne zeitliche Höchstgrenze; keine gesetzliche Regel zum Möblierungszuschlag; Mietpreisbremse bis 31.12.2029.
- **Anhängig, nicht geltend:** Regierungsentwurf BT-Drs. 21/6807 v. 01.07.2026 (Anhörung im Rechtsausschuss am 14.10.2026; Stand 23.10.2026 nicht verabschiedet) und, parallel, der Gesetzentwurf des Bundesrates BT-Drs. 21/3509 v. 07.01.2026 (ohne bekanntes Ergebnis).

## Eingaben

- **Vertrag** im Wortlaut: Laufzeit, Befristungsgrund, Zweckangabe, Möblierungsliste, ausgewiesener Zuschlag
- **Art der Wohnung:** abgeschlossene Wohnung oder Zimmer in der vom Vermieter selbst bewohnten Wohnung?
- **Bedarf des Mieters:** Projektarbeit, Studium, Übergang, oder dauerhafter Lebensmittelpunkt?
- Tatsächliche Dauer und Verlängerungen
- **Ausstattung:** Möbel, Zeitwert, Anschaffungsjahr
- Lage: Gebiet mit Mietpreisbremse? Zweckentfremdungssatzung / Registrierungspflicht der Gemeinde?
- Ortsübliche Vergleichsmiete für die unmöblierte Wohnung

## Sub-Agent-Architektur

Die Prüfung wird in Prosa von spezialisierten Schritten getragen; einen `agents`-Block trägt diese Skill bewusst nicht (mietrecht-Konvention).

- Ein **Tatbestands-Prüfer** ordnet das Verhältnis einer Fallgruppe des § 549 Abs. 2 BGB zu oder verwirft sie. Davon hängt alles Weitere ab.
- Ein **Umgehungs-Prüfer** vergleicht Vertragsetikett und tatsächliche Durchführung.
- Ein **Zuschlags-Rechner** bestimmt den angemessenen Möblierungszuschlag und spiegelt die Gesamtmiete an § 556d BGB.
- Ein **Beendigungs-Prüfer** bestimmt Kündigungsfrist und Befristungswirksamkeit.
- Ein **Reform-Prüfer** zeigt, was sich nach BT-Drs. 21/6807 ändern würde und ob der Vertrag als Altvertrag geschützt bleibt.

## Ablauf

### 1. Die Ausnahmetatbestände ([§ 549 Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__549.html))

Für die folgenden Mietverhältnisse gelten die Vorschriften über die Mieterhöhung (§§ 557–561 BGB), die Mietpreisbremse (§§ 556d–556g BGB) sowie der Kündigungs- und Bestandsschutz (u. a. §§ 568 Abs. 2, 573, 573a, 573d Abs. 1, 574–575, 575a Abs. 1, 577, 577a BGB) **nicht**:

| Nr. | Tatbestand | Kern der Prüfung |
|---|---|---|
| 1 | Wohnraum zu nur **vorübergehendem Gebrauch** | Ein konkreter, zeitlich begrenzter Sonderbedarf (Messe, Projekt, Saison). Die bloße kurze Befristung genügt nicht. |
| 2 | **Möblierter** Wohnraum, der **Teil der vom Vermieter selbst bewohnten Wohnung** ist, überwiegend vom Vermieter auszustatten, nicht zum dauernden Gebrauch einer Familie oder Lebensgemeinschaft überlassen | Bloße Möblierung einer **abgeschlossenen** Wohnung fällt **nicht** darunter. |
| 3 | Wohnraum, den eine juristische Person des öffentlichen Rechts oder ein anerkannter Träger der Wohlfahrtspflege für Personen mit dringendem Wohnungsbedarf angemietet hat | Hinweispflicht bei Vertragsschluss |

Abs. 3 enthält eine Sonderregel für **Studenten- und Jugendwohnheime**.

> **Kernaussage:** „Möbliert" allein ist **kein** Ausnahmetatbestand. Eine möblierte, abgeschlossene Wohnung, die einem Mieter als Lebensmittelpunkt überlassen wird, unterliegt dem vollen Wohnraummietrecht einschließlich der Mietpreisbremse.

### 2. Vorübergehender Gebrauch — Umgehungsprüfung

Maßgeblich ist der **Zweck** der Überlassung, nicht die vereinbarte Laufzeit. Indizien gegen einen vorübergehenden Gebrauch:

- Der Mieter meldet seinen Wohnsitz an und verlagert seinen Lebensmittelpunkt.
- Es gibt keinen konkreten Anlass, der die Befristung erklärt.
- Kettenverträge oder stillschweigende Verlängerungen.
- Ein Standardvertrag, der für alle Mieter des Objekts dieselbe Formel „Wohnen auf Zeit" verwendet.

Liegt kein vorübergehender Gebrauch vor, ist die Befristung nur nach [§ 575 BGB](https://www.gesetze-im-internet.de/bgb/__575.html) wirksam (Eigennutzung, Baumaßnahme, Werkwohnung, Grund schriftlich bei Vertragsschluss mitgeteilt). Andernfalls gilt der Vertrag als auf **unbestimmte Zeit** geschlossen (§ 575 Abs. 1 S. 2 BGB).

### 3. Möblierungszuschlag nach geltendem Recht

- Der Möblierungszuschlag ist **Teil der Miete**. In einem Gebiet mit Mietpreisbremse ist die **Gesamtmiete** an § 556d BGB zu messen: ortsübliche Vergleichsmiete der unmöblierten Wohnung zuzüglich 10 % zuzüglich eines **angemessenen** Möblierungszuschlags.
- Eine gesetzliche Bemessungsregel gibt es nach geltendem Recht **nicht**. In der instanzgerichtlichen Praxis wird der Zuschlag aus dem Zeitwert der Möbel über eine Abschreibung und eine Verzinsung abgeleitet `[unverifiziert – prüfen]`. Pauschale Zuschläge von 30–50 % der Nettokaltmiete sind regelmäßig nicht zu rechtfertigen.
- Der Vermieter muss den Zuschlag nach geltendem Recht **nicht gesondert ausweisen**. Fehlt der Ausweis, erschwert das aber seine Darlegung im Rügeverfahren nach § 556g BGB.
- Rüge und Rückforderung richten sich nach § 556g BGB; Vertiefung: `/mietrecht:mietpreisbremse`.

### 4. Kündigung und Beendigung

- **§ 549 Abs. 2 Nr. 2 BGB (möbliertes Zimmer in der Vermieterwohnung):** Die Kündigung ist spätestens am **15.** eines Monats zum Ablauf **dieses** Monats zulässig ([§ 573c Abs. 3 BGB](https://www.gesetze-im-internet.de/bgb/__573c.html)). Ein berechtigtes Interesse ist nicht erforderlich.
- **§ 549 Abs. 2 Nr. 1 BGB:** Das Verhältnis endet mit Zeitablauf; ein Kündigungsschutz nach § 573 BGB besteht nicht.
- **Kein Ausnahmetatbestand:** Es gilt das volle Recht: § 573 BGB, § 573c Abs. 1 BGB, Sozialklausel §§ 574 ff. BGB, Schriftform § 568 BGB.

### 5. Zweckentfremdung und Registrierung

Wiederholte Kurzzeitvermietung an wechselnde Gäste kann eine **genehmigungspflichtige Zweckentfremdung** nach Landesrecht sein (z. B. Zweckentfremdungsverbotsgesetze und -satzungen in Berlin, Hamburg, München). Verbreitet sind Registriernummern-, Anzeige- und Höchsttagepflichten mit Bußgeldern. Seit dem 20.05.2026 gilt außerdem die EU-Verordnung über Daten zur kurzfristigen Vermietung von Unterkünften (VO (EU) 2024/1028) mit Registrierungs- und Plattformpflichten `[unverifiziert – prüfen]`. Das Orts- und Landesrecht ist gesondert zu prüfen; für die Untervermietung durch einen Mieter: `/mietrecht:untervermietung`.

### 6. Anhängige Reform (BT-Drs. 21/6807) — Altrecht / Neurecht

Der Regierungsentwurf ([BT-Drs. 21/6807](https://dserver.bundestag.de/btd/21/068/2106807.pdf)) sieht vor:

| Regelung | Inhalt des Entwurfs |
|---|---|
| § 549 Abs. 2 Nr. 1 BGB-E | „Vorübergehender Gebrauch" nur bei besonderem vorübergehendem Bedarf, **höchstens sechs Monate**, verlängerbar auf **acht Monate** |
| § 556d Abs. 1a BGB-E | Möblierungszuschlag höchstens **1 % des Zeitwerts** der Möbel monatlich; bei Vollmöblierung bis **10 %** der Nettokaltmiete als angemessen vermutet |
| § 556g Abs. 1b BGB-E | Weist der Vermieter den Zuschlag nicht gesondert aus, gilt die Wohnung als **unmöbliert**, bis zwei Jahre nach Nachholung der Ausweisung |

**Inkrafttreten:** Für §§ 549, 556d, 556g BGB-E am ersten Tag des vierten Monats nach Verkündung. **Übergang:** Für **Altverträge** bleibt es beim bisherigen Recht. **Handhabung bis zur Verkündung:** Prüfung nach geltendem Recht; bei Neuabschlüssen Laufzeit, Bedarfsbegründung und Zuschlagsausweisung schon jetzt am Entwurf ausrichten, weil das Vertragsdatum über die anwendbare Fassung entscheidet.

## Deterministische Berechnung

```bash
# Kündigung möbliertes Zimmer § 573c Abs. 3 BGB: Zugang spätestens 15.11.2026 → Ende 30.11.2026 (Kalenderregel, von Hand prüfen)
python -m scripts.legal_calc.cli feiertage --jahr 2026 --land BE

# Entwurf: Höchstdauer sechs Monate ab Mietbeginn 01.11.2026 (nur Planungsrechnung)
python -m scripts.legal_calc.cli frist --ereignis 01.11.2026 --menge 6 --einheit monate --art beginn --land BE
```

Der Rechner macht nur die Arithmetik. Ob ein vorübergehender Bedarf vorliegt, ist eine juristische Wertung.

## Quellen

### Statute

- [§ 549 BGB](https://www.gesetze-im-internet.de/bgb/__549.html), [§ 573c BGB](https://www.gesetze-im-internet.de/bgb/__573c.html), [§ 575 BGB](https://www.gesetze-im-internet.de/bgb/__575.html), [§ 568 BGB](https://www.gesetze-im-internet.de/bgb/__568.html)
- [§ 556d BGB](https://www.gesetze-im-internet.de/bgb/__556d.html), [§ 556g BGB](https://www.gesetze-im-internet.de/bgb/__556g.html), [§ 558 BGB](https://www.gesetze-im-internet.de/bgb/__558.html)
- Landesrecht: Zweckentfremdungsverbotsgesetze und -satzungen der Länder und Gemeinden (gesondert ermitteln)

### Gesetzgebung

- Regierungsentwurf, BT-Drs. 21/6807 v. 01.07.2026 — https://dserver.bundestag.de/btd/21/068/2106807.pdf
- Gesetzentwurf des Bundesrates, BT-Drs. 21/3509 v. 07.01.2026 (möblierte und kurzfristige Vermietung) `[unverifiziert – prüfen]`

### Kommentare

- Blank/Börstinghaus, Miete, aktuelle Auflage, § 549 Rn. 1 ff.
- Schmidt-Futterer, Mietrecht, 16. Aufl. 2024, § 549 BGB (Bearbeiter und Rn. vor Zitat prüfen)

### Rechtsprechung

- BVerfG, Beschl. v. 18.07.2019 – 1 BvL 1/18 u.a. (Mietpreisbremse verfassungsgemäß; Bedeutung für Umgehungskonstruktionen) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=2019-07-18&Aktenzeichen=1%20BvL%201/18
- Zur Bemessung des Möblierungszuschlags und zum „vorübergehenden Gebrauch" bei Wohnen auf Zeit ist die instanzgerichtliche Rechtsprechung (insbesondere LG Berlin) heranzuziehen `[unverifiziert – prüfen]`. Eine Leitentscheidung des VIII. Zivilsenats zur Höhe des Zuschlags ist hier nicht verifiziert.

## Formulierungshilfe — Rüge bei möblierter Wohnung (§ 556g BGB)

```
Sehr geehrte Damen und Herren,

ich rüge einen Verstoß gegen die §§ 556d ff. BGB. Die Wohnung <Anschrift>
ist eine abgeschlossene Wohnung, die mir seit <Datum> als
Lebensmittelpunkt überlassen ist. Ein Fall des § 549 Abs. 2 BGB liegt
nicht vor: Ein besonderer vorübergehender Bedarf bestand nicht; ich bin
unter dieser Anschrift gemeldet.

Die vereinbarte Gesamtmiete von <Betrag> EUR übersteigt die zulässige
Miete. Die ortsübliche Vergleichsmiete der unmöblierten Wohnung beträgt
<…> EUR, zuzüglich 10 % also <…> EUR. Ein angemessener Möblierungszuschlag
für die vorhandene Ausstattung (Zeitwert ca. <…> EUR) liegt allenfalls bei
<…> EUR monatlich.

Ich bitte um Auskunft nach § 556g Abs. 3 BGB und um Herabsetzung der Miete.

Mit freundlichen Grüßen
```

## Ausgabeformat

```
MÖBLIERT / WOHNEN AUF ZEIT — Prüfung — <Mandat-ID> — <Datum>

I.    Ausnahmetatbestand § 549 Abs. 2 BGB  [Nr. 1 / Nr. 2 / Nr. 3 / keiner]
      Umgehungsindizien                    <Aufzählung>
II.   Befristung                           [§ 549 Abs. 2 Nr. 1 / § 575 wirksam / unbefristet]
III.  Mietpreisbremse anwendbar            [ja / nein]
      Vergleichsmiete unmöbliert + 10 %    <Betrag>
      Möblierungszuschlag angemessen       <Betrag>  (Zeitwert <…>)
      Zulässige Gesamtmiete                <Betrag>  vereinbart: <Betrag>
IV.   Kündigung                            [§ 573c Abs. 3 / Zeitablauf / volles Recht]
V.    Zweckentfremdung / Registrierung     [N/A / Genehmigung erforderlich / Verstoß]
VI.   Reform BT-Drs. 21/6807               [nicht verabschiedet — Altvertrag geschützt / Neuvertrag nach Inkrafttreten]

Ergebnis: <…>
Risiko: [🟢 / 🟡 / 🔴]
```

## Risiken / typische Fehler

- **Möblierung als Ausnahme behandelt** — eine möblierte, abgeschlossene Wohnung fällt nicht unter § 549 Abs. 2 Nr. 2 BGB; es gilt volles Wohnraummietrecht.
- **Vorübergehenden Gebrauch aus der Laufzeit abgeleitet** — maßgeblich ist der konkrete Sonderbedarf, nicht die vereinbarte Befristung.
- **Befristung ohne § 575-Grund** — der Vertrag gilt als unbefristet.
- **Möblierungszuschlag pauschal bemessen** — er muss sich aus Zeitwert und Ausstattung herleiten lassen.
- **Entwurfsregeln als geltendes Recht angewendet** — die Sechs-/Acht-Monats-Grenze und die Ausweisungspflicht sind bisher nur Regierungsentwurf (BT-Drs. 21/6807); Altverträge bleiben beim bisherigen Recht.
- **Zweckentfremdungsrecht übersehen** — Kurzzeitvermietung an Gäste kann genehmigungspflichtig und bußgeldbewehrt sein.
