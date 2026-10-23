---
name: eigenbedarfskuendigung
description: "Wirksamkeitsprüfung einer Eigenbedarfskündigung im Wohnraummietrecht – berechtigtes Interesse und begünstigter Personenkreis § 573 Abs. 2 Nr. 2 BGB, Begründungspflicht § 573 Abs. 3 BGB, Kündigungssperrfrist nach Umwandlung § 577a BGB, Kündigungsfristen § 573c BGB, Anbietpflicht, Widerspruch und Sozialklausel § 574 BGB, Schadensersatz bei vorgetäuschtem Eigenbedarf. Rechtsstand: Oktober 2026. Use when ein Vermieter eine Eigenbedarfskündigung gestaltet oder ein Mieter eine erhaltene Kündigung auf Wirksamkeit und Härtefall prüft."
language: de
provider_variants:
  - claude
  - gemini
  - openai
test: ./test.md
---

# /mietrecht:eigenbedarfskuendigung

## Zweck

Die Eigenbedarfskündigung ist die praktisch häufigste ordentliche Kündigung des Vermieters, und sie ist zugleich besonders fehleranfällig. Eine ordentliche Kündigung von Wohnraum setzt ein **berechtigtes Interesse** voraus ([§ 573 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__573.html)). Fehlt es oder ist die Begründung unzureichend, ist die Kündigung unwirksam und das Mietverhältnis läuft weiter. Wer Eigenbedarf nur **vortäuscht**, haftet dem Mieter außerdem auf Schadensersatz. Diese Skill prüft die Wirksamkeit aus beiden Perspektiven, rechnet die Sperrfrist nach Umwandlung durch und beziffert das Schadensersatzrisiko.

**Rechtsstand: Oktober 2026.** Neu zu beachten sind die Entscheidungen des VIII. Zivilsenats vom 24.09.2025 (Kontrolle des Nutzungswunsches nur auf Missbrauch, Nr. 1) und vom 21.01.2026 (§ 577a BGB auch nach Einbringung in eine Familien-GbR, Nr. 3). Zuständig ist der **VIII. Zivilsenat**.

## Eingaben

- Kündigungsschreiben (Wortlaut der angegebenen Gründe, Datum, Form, Zugang)
- Begünstigte Person und ihr Verhältnis zum Vermieter (Verwandtschaft, Haushaltszugehörigkeit)
- Konkreter Nutzungswunsch: wer, wofür, ab wann, warum gerade diese Wohnung
- Eigentumsgeschichte: Umwandlung in Wohnungseigentum? Veräußerung nach Überlassung an den Mieter? Erwerb durch eine GbR oder mehrere Erwerber?
- Andere freie oder frei werdende Wohnungen des Vermieters im selben Haus oder derselben Wohnanlage
- Mietdauer und Beginn des Mietverhältnisses (für Kündigungsfrist und Härteabwägung)
- Persönliche Lage des Mieters (Alter, Gesundheit, Verwurzelung — für die Sozialklausel)

## Sub-Agent-Architektur

Die Prüfung wird in Prosa von spezialisierten Schritten getragen, nicht von einem `agents`-Block:

- Ein **Tatbestands-Prüfer** klärt das berechtigte Interesse und den begünstigten Personenkreis.
- Ein **Sperrfrist-Prüfer** rekonstruiert die Eigentumsgeschichte und prüft § 577a BGB.
- Ein **Form-Prüfer** kontrolliert Schriftform, Begründung und Frist.
- Ein **Schutz-Prüfer** bewertet Widerspruch, Sozialklausel und Härtefall.
- Ein **Missbrauchs-Prüfer** untersucht Anzeichen für vorgetäuschten Eigenbedarf, die Anbietpflicht und die Schadensersatzfolge.

Der Ablauf fasst die Einzelergebnisse zu einem Gesamturteil zusammen.

## Ablauf

### 1. Berechtigtes Interesse / konkreter Eigenbedarf ([§ 573 Abs. 1, Abs. 2 Nr. 2 BGB](https://www.gesetze-im-internet.de/bgb/__573.html))

Die ordentliche Kündigung ist nur bei berechtigtem Interesse zulässig (Abs. 1). Eigenbedarf liegt vor, wenn der Vermieter die Wohnung **für sich, seine Familienangehörigen oder Angehörige seines Haushalts benötigt** (Abs. 2 Nr. 2). Erforderlich ist ein **ernsthafter, vernünftiger und nachvollziehbarer** Nutzungswunsch, nicht bloß ein vorgeschobener oder noch ungewisser (Vorratskündigung).

Die Gerichte haben die Lebensplanung des Vermieters zu respektieren. Sie dürfen den Nutzungswunsch nur auf **Rechtsmissbrauch** kontrollieren, etwa bei weit überhöhtem Wohnbedarf oder fehlender Eignung der Wohnung. Das gilt auch dann, wenn der Vermieter die Bedarfslage selbst herbeigeführt hat (BGH, Urt. v. 24.09.2025 – VIII ZR 289/23, NZM 2025, 870, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-09-24&Aktenzeichen=VIII%20ZR%20289/23).

Zu prüfen ist also:

- Wer soll einziehen?
- Zu welchem Zweck?
- Ab wann?
- Ist der Wunsch ernsthaft, oder dient er etwa nur dem Verkauf?

### 2. Begünstigter Personenkreis ([§ 573 Abs. 2 Nr. 2 BGB](https://www.gesetze-im-internet.de/bgb/__573.html))

Der **begünstigter Personenkreis** ist auf den Vermieter selbst, seine Familienangehörigen und die Angehörigen seines Haushalts begrenzt. Privilegierte Familienangehörige sind insbesondere Kinder, Eltern, Geschwister und Enkel. Bei entfernteren Verwandten ist eine konkrete soziale Bindung darzulegen. Eine **Tochter** zählt unproblematisch zum privilegierten Kreis. Personen außerhalb dieses Kreises tragen keinen Eigenbedarf.

Eine (Außen-)GbR als Vermieterin kann Eigenbedarf für einen Gesellschafter oder dessen Angehörige geltend machen (BGH, Urt. v. 14.12.2016 – VIII ZR 232/15 `[unverifiziert – prüfen]`). Eine juristische Person kann dagegen keinen Eigenbedarf geltend machen; für sie kommt allenfalls § 573 Abs. 1 BGB in Betracht.

### 3. Kündigungssperrfrist nach Umwandlung ([§ 577a BGB](https://www.gesetze-im-internet.de/bgb/__577a.html))

Ist an vermieteten Wohnräumen **nach der Überlassung an den Mieter Wohnungseigentum begründet und veräußert** worden, kann sich der Erwerber erst nach Ablauf von **drei Jahren** seit der Veräußerung auf Eigenbedarf (oder Verwertung) berufen (Abs. 1). In Gebieten, die die Landesregierung durch Verordnung bestimmt, beträgt die Frist **bis zu zehn Jahre** (Abs. 2); in Berlin sind es zehn Jahre. Die Sperre greift nach Abs. 1a auch, wenn das Grundstück nach der Überlassung an eine Personengesellschaft oder an mehrere Erwerber veräußert wird.

**Neu:** Die Sperrfrist gilt auch dann, wenn die Wohnung nach der Überlassung in eine **Familien-GbR** eingebracht wurde. Eine gleichwohl erklärte Eigenbedarfskündigung ist unwirksam (BGH, Urt. v. 21.01.2026 – VIII ZR 247/24, NZM 2026, 269, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-01-21&Aktenzeichen=VIII%20ZR%20247/24). Die Länge der Frist im entschiedenen Fall ergibt sich aus der Landesverordnung und ist im Einzelfall nachzuprüfen.

> Die Sperrfrist ist eine **Zulässigkeitsschranke** vor jeder inhaltlichen Prüfung. Sie wird regelmäßig übersehen, wenn der Vermieter die Wohnung erst vor wenigen Jahren erworben hat.

### 4. Form und Begründung ([§ 573 Abs. 3 BGB](https://www.gesetze-im-internet.de/bgb/__573.html), [§ 568 BGB](https://www.gesetze-im-internet.de/bgb/__568.html))

Die Kündigung bedarf der **Schriftform** (§ 568 Abs. 1 BGB). Textform genügt bei Wohnraum nicht: Eine E-Mail oder ein Fax ist unwirksam. Die Gründe des berechtigten Interesses sind nach **§ 573 Abs. 3 BGB im Kündigungsschreiben anzugeben**. Die **Begründung** muss die begünstigte Person und das Nutzungsinteresse so konkret bezeichnen, dass der Mieter sie auf Plausibilität prüfen kann. Das bloße Stichwort „Eigenbedarf" ohne nähere Angaben genügt **nicht** und macht die Kündigung formell unwirksam. Gründe, die nicht im Schreiben stehen, werden nur berücksichtigt, soweit sie nachträglich entstanden sind (§ 573 Abs. 3 S. 2 BGB).

Der Hinweis auf das Widerspruchsrecht nach §§ 574–574b BGB soll rechtzeitig erteilt werden (§ 568 Abs. 2 BGB). Fehlt er, verlängert sich die Widerspruchsfrist (§ 574b Abs. 2 S. 2 BGB).

### 5. Kündigungsfrist ([§ 573c BGB](https://www.gesetze-im-internet.de/bgb/__573c.html))

Es gelten die gesetzlichen Fristen des **§ 573c BGB**. Die Grundfrist beträgt **drei Monate**; sie verlängert sich auf **sechs Monate nach fünf Jahren** und auf **neun Monate nach acht Jahren** Überlassungsdauer. Die Kündigung muss spätestens am dritten Werktag eines Kalendermonats zugehen und wirkt dann zum Ablauf des übernächsten Monats (bei der Grundfrist). Für eine langjährige Mieterin ist regelmäßig die Neun-Monats-Frist einschlägig. Der Zugang sollte mit Puffer geplant werden: Ob der Samstag als Werktag zählt, ist bei einer knappen Zustellung ein vermeidbares Risiko.

### 6. Anbietpflicht

Wird während der Kündigungsfrist im selben Haus oder in derselben Wohnanlage eine **vergleichbare Wohnung** des Vermieters frei, muss er sie dem Mieter anbieten. Ein Verstoß macht die Kündigung nach neuerer Rechtsprechung nicht unwirksam. Er begründet aber einen **Schadensersatzanspruch** (BGH, Urt. v. 14.12.2016 – VIII ZR 232/15 `[unverifiziert – prüfen]`).

### 7. Widerspruch und Sozialklausel ([§ 574 BGB](https://www.gesetze-im-internet.de/bgb/__574.html))

Auch eine formell wirksame Kündigung kann am **Widerspruch** des Mieters scheitern. Die **Sozialklausel** des **§ 574 BGB** gibt dem Mieter das Recht, der Kündigung zu widersprechen und die **Fortsetzung des Mietverhältnisses** zu verlangen. Voraussetzung ist, dass die Beendigung für ihn, seine Familie oder einen Haushaltsangehörigen eine **Härte** bedeutet, die auch unter Würdigung der berechtigten Interessen des Vermieters nicht zu rechtfertigen ist.

Der Widerspruch ist form- und fristgebunden ([§ 574b BGB](https://www.gesetze-im-internet.de/bgb/__574b.html)): schriftlich, spätestens zwei Monate vor Beendigung. Ein **Härtefall** kommt namentlich bei hohem Alter, Krankheit, Gebrechlichkeit, langer Mietdauer oder fehlendem angemessenen Ersatzwohnraum in Betracht. Eine 80-jährige, verwurzelte Mieterin ist ein typischer Anwendungsfall. Alter allein ist aber kein Automatismus: Bei behaupteten gesundheitlichen Folgen ist regelmäßig ein Sachverständigengutachten einzuholen (BGH, Urt. v. 22.05.2019 – VIII ZR 180/18 `[unverifiziert – prüfen]`). Rechtsfolge ist die Fortsetzung auf bestimmte oder unbestimmte Zeit (§ 574a BGB). Vertiefung: `/mietrecht:sozialklausel-widerspruch`.

### 8. Rechtsmissbrauch / vorgetäuschter Eigenbedarf + Schadensersatz

Die Kündigung ist rechtsmissbräuchlich und unwirksam, wenn der Eigenbedarf nur vorgeschoben ist. Stellt sich nach dem Auszug heraus, dass der behauptete Bedarf nie bestand, liegt ein **vorgetäuschter Eigenbedarf** vor. Der Vermieter haftet dann auf **Schadensersatz** nach § 280 Abs. 1 BGB (Umzugs-, Makler- und Mietmehrkosten). Ein Räumungsvergleich schließt diesen Anspruch nicht ohne Weiteres aus (BGH, Urt. v. 10.06.2015 – VIII ZR 99/14, NJW 2015, 2324, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2015-06-10&Aktenzeichen=VIII%20ZR%2099/14).

Verwirklicht der Vermieter den Eigenbedarf nach dem Auszug nicht, trifft ihn eine **sekundäre Darlegungslast**: Er muss substantiiert und plausibel darlegen, warum der Bedarf nachträglich entfallen sein soll. Diese Linie stammt aus der Rechtsprechung zum vorgeschobenen Bedarf, u. a. BGH, Urt. v. 29.03.2017 – VIII ZR 44/16 (dort für einen Betriebsbedarf) `[unverifiziert – prüfen]`.

**Wegfall des Bedarfs vor Ablauf der Kündigungsfrist:** Der Vermieter muss den Mieter darauf hinweisen, solange die Frist läuft. Unterlässt er das, haftet er ebenfalls (BGH, Urt. v. 09.11.2005 – VIII ZR 339/04 `[unverifiziert – prüfen]`).

Indizien für Vortäuschung sind ein fehlender tatsächlicher Einzug, eine alsbaldige Weitervermietung oder ein Verkauf und wechselnde Begründungen.

### 9. Ergebnis

Zusammenführung, Stufe für Stufe:

- Ist die Sperrfrist abgelaufen?
- Liegt ein ernsthafter Eigenbedarf für eine privilegierte Person vor?
- Ist die Schriftform gewahrt, die Begründung konkret und die Frist eingehalten?
- Greift kein durchgreifender Härtefall?

Erst wenn alle Stufen bestehen, ist die Kündigung wirksam und durchsetzbar. Zur Durchsetzung: `/mietrecht:raeumungsklage`.

## Formulierungshilfe — Begründung der Eigenbedarfskündigung

```
Ich kündige das Mietverhältnis über die Wohnung <Anschrift, Lage> ordentlich
zum <Datum, § 573c BGB>.

Ich benötige die Wohnung für meine Tochter <Name>, <Alter>. Sie wohnt derzeit
in <Ort> zur Miete in einer <…> m² großen Wohnung und tritt zum <Datum> eine
Stelle in <Ort der Wohnung> an. Sie beabsichtigt, mit ihrem Partner <Name>
einen gemeinsamen Hausstand zu begründen. Die Wohnung ist mit <…> Zimmern und
<…> m² dafür geeignet und liegt <…> km vom Arbeitsplatz entfernt.

Eine Sperrfrist nach § 577a BGB besteht nicht: Ich bin seit <Datum> Eigentümer;
Wohnungseigentum wurde <nicht / vor Ihrem Einzug am …> begründet.

Sie können der Kündigung nach §§ 574 bis 574b BGB widersprechen und die
Fortsetzung des Mietverhältnisses verlangen, wenn die Beendigung für Sie eine
nicht zu rechtfertigende Härte bedeuten würde. Der Widerspruch ist schriftlich
und spätestens zwei Monate vor Beendigung des Mietverhältnisses zu erklären.

<eigenhändige Unterschrift aller Vermieter>
```

## Beispiel (Gutachtenstil, Kurzform)

Der Vermieter V kündigt der seit 22 Jahren in der Wohnung lebenden 80-jährigen Mieterin M mit dem Satz „wegen Eigenbedarfs". Fraglich ist, ob die Kündigung das Mietverhältnis beendet.

Die Kündigung bedarf eines berechtigten Interesses (§ 573 Abs. 1 BGB), dessen Gründe im Kündigungsschreiben anzugeben sind (§ 573 Abs. 3 BGB). Das bloße Stichwort „Eigenbedarf" lässt weder die Bedarfsperson noch das Nutzungsinteresse erkennen, sodass M die Kündigung nicht auf Plausibilität prüfen kann. Die Kündigung ist bereits formell unwirksam.

Hilfsweise: Selbst eine ordnungsgemäß begründete Kündigung (Frist § 573c BGB: neun Monate) müsste sich am Widerspruch nach § 574 BGB messen lassen. Alter, lange Mietdauer und Verwurzelung sprechen für eine Härte; deren Gewicht ist gegebenenfalls durch Gutachten zu klären.

Ergebnis: Das Mietverhältnis besteht fort.

## Quellen

### Statute

- [§ 573 BGB](https://www.gesetze-im-internet.de/bgb/__573.html), [§ 573c BGB](https://www.gesetze-im-internet.de/bgb/__573c.html), [§ 574 BGB](https://www.gesetze-im-internet.de/bgb/__574.html), [§ 574a BGB](https://www.gesetze-im-internet.de/bgb/__574a.html), [§ 574b BGB](https://www.gesetze-im-internet.de/bgb/__574b.html)
- [§ 577a BGB](https://www.gesetze-im-internet.de/bgb/__577a.html) (Kündigungsbeschränkung bei Wohnungsumwandlung), [§ 568 BGB](https://www.gesetze-im-internet.de/bgb/__568.html) (Form), [§ 280 BGB](https://www.gesetze-im-internet.de/bgb/__280.html) (Schadensersatz)

### Kommentare

- Häublein, in: MüKoBGB, 9. Aufl. 2023, § 573 Rn. 1 ff. `[unverifiziert – prüfen]` (Bearbeiter und Auflage vor Zitat prüfen)
- Blank/Börstinghaus, Miete, aktuelle Auflage, § 573 Rn. 1 ff.
- Schmidt-Futterer, Mietrecht, 16. Aufl. 2024, § 573 BGB, § 577a BGB (Bearbeiter vor Zitat prüfen)

### Rechtsprechung

- BGH, Urt. v. 21.01.2026 – VIII ZR 247/24, NZM 2026, 269 (§ 577a BGB auch nach Einbringung in eine Familien-GbR) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-01-21&Aktenzeichen=VIII%20ZR%20247/24
- BGH, Urt. v. 24.09.2025 – VIII ZR 289/23, NZM 2025, 870 (Nutzungswunsch nur auf Missbrauch kontrollierbar, auch bei selbst geschaffener Bedarfslage) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-09-24&Aktenzeichen=VIII%20ZR%20289/23
- BGH, Urt. v. 10.06.2015 – VIII ZR 99/14, NJW 2015, 2324 = NZM 2015, 532 (Schadensersatz bei vorgetäuschtem Eigenbedarf, § 280 Abs. 1 BGB; Räumungsvergleich) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2015-06-10&Aktenzeichen=VIII%20ZR%2099/14
- BGH, Urt. v. 29.03.2017 – VIII ZR 44/16 (Betriebsbedarf; sekundäre Darlegungslast bei nicht verwirklichtem Bedarf) `[unverifiziert – prüfen]`
- BGH, Urt. v. 14.12.2016 – VIII ZR 232/15 (Eigenbedarf der GbR; Verletzung der Anbietpflicht nur Schadensersatz) `[unverifiziert – prüfen]`
- BGH, Urt. v. 22.05.2019 – VIII ZR 180/18 (Härteprüfung, Sachverständigengutachten) `[unverifiziert – prüfen]`
- BGH, Urt. v. 09.11.2005 – VIII ZR 339/04 (Hinweispflicht bei Wegfall des Eigenbedarfs während der Kündigungsfrist) `[unverifiziert – prüfen]`

## Ausgabeformat

```
EIGENBEDARFSKÜNDIGUNG — Prüfung — <Mandat-ID> — <Datum>

I.    Sperrfrist (§ 577a BGB)                                   [keine / läuft bis <Datum> → unwirksam]
II.   Berechtigtes Interesse / Eigenbedarf (§ 573 Abs. 2 Nr. 2)  [✅ / ❌]
      Missbrauchskontrolle (VIII ZR 289/23)                      [kein Anhalt / überhöhter Bedarf]
III.  Begünstigter Personenkreis                                 [privilegiert / nein]
IV.   Form + Begründung (§ 568 Abs. 1, § 573 Abs. 3)             [✅ / ⚠️ / ❌]
V.    Kündigungsfrist (§ 573c)                                   [3 / 6 / 9 Monate] → Ende <Datum>
VI.   Anbietpflicht                                              [N/A / verletzt → Schadensersatz]
VII.  Widerspruch / Sozialklausel / Härtefall (§ 574)            [kein / möglich / durchgreifend]
VIII. Rechtsmissbrauch / vorgetäuschter Eigenbedarf              [kein Anhalt / Indizien]
      Schadensersatzrisiko (§ 280, VIII ZR 99/14)                [🟢 / 🟡 / 🔴]

Ergebnis: <wirksam / unwirksam / schwebend>
Empfehlung: <…>
```

## Risiken

- **Begründung zu pauschal** (nur Stichwort „Eigenbedarf") → formell unwirksam, § 573 Abs. 3 BGB.
- **Sperrfrist nach § 577a BGB übersehen** → Kündigung unwirksam, auch bei Umweg über eine Familien-GbR (BGH VIII ZR 247/24, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-01-21&Aktenzeichen=VIII%20ZR%20247/24).
- **Begünstigte Person außerhalb des privilegierten Kreises** → kein Eigenbedarf.
- **Kündigung per E-Mail oder ohne Unterschrift aller Vermieter** → Schriftform des § 568 Abs. 1 BGB verfehlt.
- **Kündigungsfrist nach § 573c BGB falsch berechnet** (Staffelung 3/6/9 Monate übersehen) → Beendigung erst zum späteren Termin.
- **Härtefall / Sozialklausel unterschätzt** → Mieter erzwingt Fortsetzung nach § 574 BGB.
- **Vorgetäuschter Eigenbedarf** → Unwirksamkeit *und* Schadensersatz (BGH, Urt. v. 10.06.2015 – VIII ZR 99/14, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2015-06-10&Aktenzeichen=VIII%20ZR%2099/14).
- **Wegfall des Eigenbedarfs während der Frist nicht mitgeteilt** → Schadensersatzrisiko.
- **Anbietpflicht verletzt** → Schadensersatz, auch wenn die Kündigung wirksam bleibt.
