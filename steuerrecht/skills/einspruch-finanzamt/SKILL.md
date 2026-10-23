---
name: einspruch-finanzamt
description: "Prüfung und Einlegung des Einspruchs gegen einen Steuerbescheid – Statthaftigkeit § 347 AO, Einspruchsfrist von einem Monat § 355 AO, Bekanntgabe per Post (§ 122 Abs. 2 AO, vier Tage) und per Datenabruf (§ 122a Abs. 4 AO, vier Tage nach Bereitstellung), Form und Inhalt § 357 AO, Aussetzung der Vollziehung § 361 AO, Ruhen § 363 AO, Präklusion § 364b AO, Verböserungsgefahr § 367 Abs. 2 AO. Rechtsstand Oktober 2026 inkl. Hinweis auf den Entwurf des JStG 2026. Use when gegen einen Steuerbescheid oder einen anderen Verwaltungsakt der Finanzbehörde Einspruch geprüft oder eingelegt werden soll."
language: de
provider_variants:
  - claude
  - gemini
  - openai
test: ./test.md
---

# /steuerrecht:einspruch-finanzamt

> **Rechtsstand: Oktober 2026.** Geltendes Recht und Entwurfsrecht sind getrennt ausgewiesen. Das Jahressteuergesetz 2026 (Regierungsentwurf, BT-Drs. 21/8283 vom 30.09.2026; Anhörung im Finanzausschuss am 02.11.2026) ist **nicht verabschiedet** — Aussagen dazu sind als „Entwurf" gekennzeichnet.

## Zweck

Der Einspruch ist der zentrale außergerichtliche Rechtsbehelf gegen Verwaltungsakte der Finanzbehörde. Er ist kostenfrei, hemmt die Bestandskraft und den Ablauf der Festsetzungsfrist (§ 171 Abs. 3a AO) und eröffnet eine Überprüfung des ganzen Falls. Wird die einmonatige Frist versäumt, wird der Bescheid bestandskräftig und ist nur noch über die engen Korrekturvorschriften (§§ 129, 164, 165, 172 ff. AO — siehe `/steuerrecht:aenderung-bescheid-korrekturvorschriften`) angreifbar. Dieser Skill prüft Bekanntgabe, Frist, Form, Befugnis und Erfolgsaussichten und formuliert Einspruch und Antrag auf Aussetzung der Vollziehung.

## Eingaben

- Bescheid (Art des Verwaltungsakts, Datum, Steuerart, Streitjahr, Steuernummer)
- **Bekanntgabeweg**: Post (Datum der Aufgabe zur Post) **oder** Bereitstellung zum Datenabruf in ELSTER (Datum der Bereitstellung laut Benachrichtigung)
- Steht ein Antrag auf postalische Bekanntgabe (§ 122a Abs. 2 AO) im Raum?
- Streitpunkt (z. B. nicht anerkannte Werbungskosten, Schätzung, Versagung einer Vergünstigung)
- Vollziehung / Zahlungsfrist (Nachzahlung, Fälligkeit, Vollstreckung)
- Neue Tatsachen oder Beweismittel; ist ein Musterverfahren beim BFH, BVerfG oder EuGH anhängig?

## Sub-Agent-Architektur

Die Bearbeitung verläuft über mehrere gedankliche Rollen. Ein **Fristen-Prüfer** rekonstruiert aus Bekanntgabeweg und Datum den Bekanntgabetag und die Monatsfrist und rechnet deterministisch mit [`scripts/legal_calc/`](../../../scripts/legal_calc/). Ein **Zulässigkeits-Prüfer** klärt Statthaftigkeit, Form und Einspruchsbefugnis. Ein **Vollziehungs-Prüfer** entscheidet über den AdV-Antrag (Details: `/steuerrecht:aussetzung-der-vollziehung`). Ein **Strategie-Prüfer** wägt Erfolgsaussichten gegen die Verböserungsgefahr ab und prüft Ruhen und Hinzuziehung. Die Ergebnisse fließen in das Ausgabeformat.

## Ablauf

### 1. Statthaftigkeit ([§ 347 AO](https://www.gesetze-im-internet.de/ao_1977/__347.html))

- Statthaft gegen Verwaltungsakte in Abgabenangelegenheiten, auf die die AO Anwendung findet (§ 347 Abs. 1 AO): Steuer-, Feststellungs-, Haftungs-, Zins-, Ablehnungsbescheide und sonstige Verwaltungsakte der Finanzbehörde.
- Auch bei **Untätigkeit** der Behörde statthaft (§ 347 Abs. 1 S. 2 AO).
- Abgrenzung: gegen Einspruchsentscheidungen nur Klage (§ 348 Nr. 1 AO); gegen Grundsteuerbescheide der Gemeinde gilt Landes- bzw. Kommunalabgabenrecht (siehe `/steuerrecht:grundsteuer-einspruch`).

### 2. Bekanntgabe — zwei Wege, jeweils vier Tage

**a) Post ([§ 122 AO](https://www.gesetze-im-internet.de/ao_1977/__122.html))**

- Ein im Inland per Post übermittelter Verwaltungsakt gilt am **vierten Tag nach Aufgabe zur Post** als bekannt gegeben (§ 122 Abs. 2 Nr. 1 AO; seit 01.01.2025 vier statt drei Tage).
- Fällt der vierte Tag auf Samstag, Sonntag oder Feiertag, verschiebt sich die Bekanntgabe nach § 108 Abs. 3 AO auf den nächsten Werktag.
- Die Fiktion gilt nicht, wenn der Bescheid nicht oder später zugegangen ist; im Zweifel muss die Behörde den Zugang nachweisen (§ 122 Abs. 2 letzter Halbs. AO). Bei strukturellen Zustellmängeln innerhalb der Frist kann die Vermutung erschüttert sein (BFH, Urt. v. 29.07.2025 – VI R 6/23 `[unverifiziert – prüfen]`).

**b) Bereitstellung zum Datenabruf ([§ 122a AO](https://www.gesetze-im-internet.de/ao_1977/__122a.html))**

- Ein zum Abruf bereitgestellter Verwaltungsakt gilt am **vierten Tag nach der Bereitstellung** als bekannt gegeben (§ 122a Abs. 4 S. 1 AO). Ob und wann der Mandant ihn tatsächlich abruft, ist **unerheblich**; die E-Mail-Benachrichtigung ist nur Hinweis. Im Zweifel muss die Behörde den Zeitpunkt der Bereitstellung nachweisen (§ 122a Abs. 4 S. 2 AO).
- **Regelfall ohne Einwilligung — zeitlich gestaffelt:** § 122a Abs. 1 S. 2 AO (Bereitstellung „soll" erfolgen, wenn der Bescheid auf einer elektronisch übermittelten Erklärung beruht) ist nach Art. 97 § 28 Abs. 2 S. 2 EGAO erst auf Verwaltungsakte anzuwenden, die **nach dem 31.12.2026** erlassen werden ([Volltext](https://www.gesetze-im-internet.de/aoeg_1977/art_97__28.html)). Für 2026 erlassene Bescheide bleibt es bei der Bereitstellung nur mit Einwilligung des Beteiligten.
- **Antrag auf postalische Bekanntgabe** (§ 122a Abs. 2 AO): einmalig oder dauerhaft möglich; wirkt — wie sein Widerruf — **nur für die Zukunft** und erst ab Zugang bei der Behörde.
- **Entwurf JStG 2026 (ab 01.01.2027 geplant):** Bereitstellung an jeden Beteiligten mit aktivem Nutzerkonto bzw. an Bevollmächtigte mit elektronisch angezeigter Empfangsvollmacht; der Antrag auf Papierbescheid soll **nur noch elektronisch** über die amtlichen Schnittstellen gestellt werden können, und bisherige formlose Anträge sollen für ab 2027 bekanntzugebende Verwaltungsakte unbeachtlich werden. Außerdem soll ein Verstoß gegen den gewählten Bekanntgabeweg die Bekanntgabe nicht unwirksam machen (§ 124 Abs. 1 AO-Entwurfsfassung; § 125 Abs. 3 Nr. 5, 6 AO-Entwurfsfassung). Vor jeder Beratung ab Dezember 2026 Verabschiedung prüfen.

### 3. Einspruchsfrist ([§ 355 AO](https://www.gesetze-im-internet.de/ao_1977/__355.html))

- Der Einspruch ist **innerhalb eines Monats** nach Bekanntgabe einzulegen (§ 355 Abs. 1 S. 1 AO). Diese **Monatsfrist** ist die maßgebliche **Einspruchsfrist**; sie ist nicht verlängerbar.
- Fristberechnung nach § 108 Abs. 1 AO i. V. m. §§ 187 ff. BGB; Fristende am Wochenende/Feiertag → nächster Werktag (§ 108 Abs. 3 AO).
- Deterministisch rechnen — erst die Bekanntgabefiktion, dann die Monatsfrist:

```bash
# Bekanntgabe: Aufgabe zur Post bzw. Bereitstellung am 19.10.2026 (+ 4 Tage, § 108 Abs. 3 AO)
python -m scripts.legal_calc.cli frist --ereignis 19.10.2026 --menge 4 --einheit tage --land NW
# Einspruchsfrist: 1 Monat ab dem ermittelten Bekanntgabetag
python -m scripts.legal_calc.cli frist --ereignis 23.10.2026 --menge 1 --einheit monate --land NW
```

- Fehlende oder unrichtige Rechtsbehelfsbelehrung → Jahresfrist (§ 356 Abs. 2 AO).
- Versäumte Frist: Wiedereinsetzung nach [§ 110 AO](https://www.gesetze-im-internet.de/ao_1977/__110.html) (Antrag binnen eines Monats nach Wegfall des Hindernisses; Verschulden des Beraters wird zugerechnet).

### 4. Form und Inhalt ([§ 357 AO](https://www.gesetze-im-internet.de/ao_1977/__357.html))

- **Form**: schriftlich, elektronisch (auch über ELSTER) oder zur Niederschrift (§ 357 Abs. 1 S. 1 AO). Unrichtige Bezeichnung schadet nicht (§ 357 Abs. 1 S. 3 AO).
- Der Einspruch **soll** den angefochtenen Verwaltungsakt bezeichnen, angeben, inwieweit er angefochten und seine Aufhebung beantragt wird, und Tatsachen und Beweismittel anführen (§ 357 Abs. 3 AO) — eine Soll-Vorschrift, keine Zulässigkeitsvoraussetzung.
- **Adressat**: die Behörde, deren Verwaltungsakt angefochten wird. Einlegung bei einer anderen Behörde wahrt die Frist nur, wenn der Einspruch der zuständigen Behörde **vor Fristablauf** übermittelt wird (§ 357 Abs. 2 S. 4 AO).
- Begründung ist nicht Zulässigkeitsvoraussetzung, aber strategisch geboten; Achtung auf eine Ausschlussfrist nach § 364b AO (Schritt 7).

### 5. Einspruchsbefugnis ([§ 350 AO](https://www.gesetze-im-internet.de/ao_1977/__350.html)) und Beschwer

- **Einspruchsbefugnis** hat nur, wer geltend macht, durch den Verwaltungsakt beschwert zu sein.
- Null-Bescheide: regelmäßig keine Beschwer; Ausnahme bei bindenden Besteuerungsgrundlagen.
- Feststellungsbescheide: Sonderregelung § 352 AO. **Entwurf JStG 2026**: Neufassung des § 352 Abs. 1 AO für rechtsfähige Personenvereinigungen (Folge des MoPeG).
- Bindung an Grundlagenbescheide: Einwendungen gegen Feststellungen sind nur gegen den Grundlagenbescheid zu erheben (§ 351 Abs. 2 AO).

### 6. Aussetzung der Vollziehung ([§ 361 AO](https://www.gesetze-im-internet.de/ao_1977/__361.html))

- Der Einspruch hat **keine** aufschiebende Wirkung (§ 361 Abs. 1 AO).
- Auf Antrag soll die **Aussetzung der Vollziehung** erfolgen bei ernstlichen Zweifeln oder unbilliger Härte (§ 361 Abs. 2 S. 2 AO); bei Steuerbescheiden begrenzt auf die festgesetzte Steuer abzüglich Steuerabzugsbeträgen und Vorauszahlungen (§ 361 Abs. 2 S. 4 AO).
- Gerichtliche AdV erst nach Ablehnung durch die Behörde (§ 69 Abs. 4 FGO).
- **Aussetzungszinsen** (§ 237 AO, 0,5 % je Monat): Der BFH hält den Zinssatz für einen Teilzeitraum für verfassungswidrig und hat vorgelegt (BFH, Beschl. v. 08.05.2024 – VIII R 9/23; BVerfG – 1 BvL 8/24 anhängig `[unverifiziert – prüfen]`). Gegen Zinsbescheide Einspruch einlegen und Ruhen beantragen.
- Vollständiges Prüfprogramm: `/steuerrecht:aussetzung-der-vollziehung`.

### 7. Verfahren im Einspruch: Ruhen, Präklusion, Hinzuziehung

- **Ruhen** ([§ 363 AO](https://www.gesetze-im-internet.de/ao_1977/__363.html)): Zwangsruhe kraft Gesetzes, wenn wegen der Verfassungsmäßigkeit einer Norm oder einer Rechtsfrage ein Verfahren beim EuGH, BVerfG oder einem obersten Bundesgericht anhängig ist und der Einspruch darauf gestützt wird (§ 363 Abs. 2 S. 2 AO). Musterverfahren mit Aktenzeichen benennen. Ruhen mit Zustimmung (§ 363 Abs. 2 S. 1 AO) aus Zweckmäßigkeit.
- **Präklusion** ([§ 364b AO](https://www.gesetze-im-internet.de/ao_1977/__364b.html)): Setzt die Behörde eine Frist zur Angabe von Tatsachen oder Vorlage von Beweismitteln, sind verspätete Erklärungen ausgeschlossen — und können nach § 76 Abs. 3 FGO auch im Klageverfahren zurückgewiesen werden. Fristen notieren, Fristverlängerung rechtzeitig beantragen.
- **Hinzuziehung** ([§ 360 AO](https://www.gesetze-im-internet.de/ao_1977/__360.html)): bei Zusammenveranlagung, Feststellungen, Haftung — notwendige Hinzuziehung beachten.
- **Teileinspruchsentscheidung und Allgemeinverfügung** (§ 367 Abs. 2a, 2b AO): Bei Massenrechtsbehelfen kann über Teile entschieden bzw. per Allgemeinverfügung zurückgewiesen werden; die Klagefrist gegen eine Allgemeinverfügung beträgt ein Jahr (§ 367 Abs. 2b S. 5 AO).

### 8. Verböserungsgefahr ([§ 367 Abs. 2 AO](https://www.gesetze-im-internet.de/ao_1977/__367.html)) und Rücknahme ([§ 362 AO](https://www.gesetze-im-internet.de/ao_1977/__362.html))

- **Geltendes Recht:** Die Behörde „hat die Sache in vollem Umfang erneut zu prüfen" (§ 367 Abs. 2 S. 1 AO) — Gesamtaufrollung.
- Daraus folgt die Gefahr einer **Verböserung**: Änderung zum Nachteil ist zulässig, aber nur nach vorherigem **Verböserungshinweis** mit Gelegenheit zur Äußerung (§ 367 Abs. 2 S. 2 AO).
- Reaktion: **Rücknahme** nach § 362 AO bis zur Bekanntgabe der Einspruchsentscheidung; der ursprüngliche Bescheid wird bestandskräftig. Einen Verböserungshinweis stets mit Frist im Fristenkalender führen.
- **Entwurf JStG 2026:** § 367 Abs. 2 S. 1 AO soll in ein bloßes Prüfungs**recht** umgewandelt werden; ein neuer § 367 Abs. 2c AO soll erlauben, anhängige Einsprüche, die ausschließlich bereits vom EuGH, BVerfG oder BFH entschiedene Rechtsfragen betreffen, per **Allgemeinverfügung** zurückzuweisen — auch für vor Inkrafttreten eingelegte Einsprüche. Für Masseneinsprüche bedeutet das: Begründung individualisieren, wenn der Einspruch mehr als die Musterfrage betrifft.

### 9. Ergebnis und Antragsformulierung

- Zusammenführung von Bekanntgabe, Frist, Form, Befugnis und Erfolgsaussicht zu einer Empfehlung.
- Einspruch mit Bezeichnung des Verwaltungsakts, Umfang der Anfechtung, Antrag und Begründung (oder Ankündigung der Begründung mit Fristvorschlag).
- Gesonderter AdV-Antrag; ggf. Antrag auf Ruhen; Antrag auf Akteneinsicht (im Einspruchsverfahren kein Anspruch, aber Ermessen; Art. 15 DSGVO als Auskunftsweg).

## Ausgabeformat

```
EINSPRUCH — Prüfung — <Mandant> — <Datum> — Rechtsstand Oktober 2026

I.    Angefochtener Verwaltungsakt
      Art / Steuerart / Jahr:         <ESt-Bescheid 2025 / …>
      Bescheiddatum:                  <…>
      Bekanntgabeweg:                 [Post / Datenabruf § 122a AO]
      Aufgabe zur Post / Bereitstellung: <Datum>
      Bekanntgabe (Fiktion 4 Tage):   <Datum, ggf. § 108 Abs. 3 AO>

II.   Frist
      Einspruchsfrist (§ 355 AO):     <Monatsfrist — Fristende (Rechner)>
      Rechtsbehelfsbelehrung:         [ordnungsgemäß / fehlerhaft → 1 Jahr]
      Status:                         [offen / abgelaufen → § 110 AO]

III.  Zulässigkeit
      Statthaftigkeit (§ 347 AO):     [✓]
      Form (§ 357 AO):                [schriftlich / elektronisch / Niederschrift]
      Einspruchsbefugnis (§ 350 AO):  [Beschwer ✓ / fraglich]

IV.   Vollziehung
      Nachzahlung / Fälligkeit:       <EUR / Datum>
      Aussetzung der Vollziehung:     [beantragt — ernstliche Zweifel: …]

V.    Verfahren
      Ruhen (§ 363 AO):               [Musterverfahren Az … / —]
      Präklusionsfrist (§ 364b AO):   [keine / bis …]

VI.   Erfolgsaussicht / Strategie
      Streitpunkt:                    <…>
      Verböserungsrisiko (§ 367 AO):  [keines / niedrig / mittel / hoch]
      Rücknahmeoption (§ 362 AO):     <…>

VII.  Antrag
      <Einspruch + Begründung + ggf. AdV- und Ruhensantrag>
```

## Beispiel (Urteilsstil, Kurzvermerk)

Der ESt-Bescheid 2025 wurde am Montag, 19.10.2026, zum Datenabruf bereitgestellt; der Mandant hatte in die elektronische Bekanntgabe eingewilligt. Er gilt am vierten Tag nach der Bereitstellung, Freitag, 23.10.2026, als bekannt gegeben (§ 122a Abs. 4 S. 1 AO); dass der Mandant ihn erst am 05.11.2026 abgerufen hat, ist unerheblich. Die Einspruchsfrist endet mit Ablauf des 23.11.2026 (§ 355 Abs. 1 AO, § 108 Abs. 1 AO i. V. m. § 188 Abs. 2 BGB; Rechner). Der Einspruch ist statthaft (§ 347 AO), der Mandant ist durch die Nichtberücksichtigung von Werbungskosten beschwert (§ 350 AO). Da die Nachzahlung am 23.11.2026 fällig wird, ist zugleich Aussetzung der Vollziehung nach § 361 Abs. 2 S. 2 AO zu beantragen. Ein Verböserungsrisiko besteht, weil im selben Bescheid ein großzügig geschätzter Arbeitszimmeranteil anerkannt wurde; es ist dem Mandanten vor Einlegung schriftlich zu erläutern.

## Risiken / typische Fehler

- **Einspruchsfrist verpasst** — die Monatsfrist ist nicht verlängerbar; ohne Wiedereinsetzung (§ 110 AO) wird der Bescheid bestandskräftig.
- **Bekanntgabe falsch berechnet** — vier Tage bei Post **und** bei Datenabruf; maßgeblich ist die Bereitstellung, nicht der tatsächliche Abruf; Verschiebung nach § 108 Abs. 3 AO übersehen.
- **Bekanntgabeweg verwechselt** — für 2026 erlassene Bescheide gilt die Bereitstellung ohne Einwilligung noch nicht; ein Antrag auf Papierbescheid wirkt nur für die Zukunft (§ 122a Abs. 2 AO). Den Entwurf JStG 2026 (nur noch elektronischer Antrag ab 2027) nicht als geltendes Recht darstellen.
- **Aussetzung der Vollziehung nicht beantragt** — trotz Einspruch droht Vollstreckung; AdV ist gesondert zu beantragen.
- **Verböserung unterschätzt** — Gesamtaufrollung nach § 367 Abs. 2 AO kann zu höherer Steuer führen; Rücknahme nach § 362 AO nur bis zur Einspruchsentscheidung.
- **Präklusionsfrist nach § 364b AO ignoriert** — verspäteter Vortrag ist auch vor dem FG verloren.
- **Ruhen nicht beantragt** — bei anhängigen Musterverfahren (z. B. Aussetzungszinsen 1 BvL 8/24 `[unverifiziert – prüfen]`) bleibt die Sache sonst offen für Zurückweisung.
- **Einspruchsbefugnis fehlt** — mangelnde Beschwer (Null-Bescheid) macht den Einspruch unzulässig; Grundlagen-Einwände gegen den Folgebescheid scheitern an § 351 Abs. 2 AO.
- **Form verfehlt** — Einspruch bei unzuständiger Stelle wahrt die Frist nur bei rechtzeitiger Weiterleitung (§ 357 Abs. 2 S. 4 AO).

## Quellen

### Statute

- [§ 347 AO](https://www.gesetze-im-internet.de/ao_1977/__347.html) (Statthaftigkeit), [§ 350 AO](https://www.gesetze-im-internet.de/ao_1977/__350.html) (Beschwer), [§ 351 AO](https://www.gesetze-im-internet.de/ao_1977/__351.html) (Bindungswirkung)
- [§ 355 AO](https://www.gesetze-im-internet.de/ao_1977/__355.html) (Einspruchsfrist), [§ 356 AO](https://www.gesetze-im-internet.de/ao_1977/__356.html) (Rechtsbehelfsbelehrung)
- [§ 357 AO](https://www.gesetze-im-internet.de/ao_1977/__357.html) (Einlegung), [§ 360 AO](https://www.gesetze-im-internet.de/ao_1977/__360.html) (Hinzuziehung)
- [§ 361 AO](https://www.gesetze-im-internet.de/ao_1977/__361.html) (Aussetzung der Vollziehung), [§ 237 AO](https://www.gesetze-im-internet.de/ao_1977/__237.html) (Aussetzungszinsen)
- [§ 362 AO](https://www.gesetze-im-internet.de/ao_1977/__362.html) (Rücknahme), [§ 363 AO](https://www.gesetze-im-internet.de/ao_1977/__363.html) (Ruhen), [§ 364b AO](https://www.gesetze-im-internet.de/ao_1977/__364b.html) (Präklusion), [§ 367 AO](https://www.gesetze-im-internet.de/ao_1977/__367.html) (Entscheidung, Gesamtaufrollung)
- [§ 122 AO](https://www.gesetze-im-internet.de/ao_1977/__122.html) (Bekanntgabe), [§ 122a AO](https://www.gesetze-im-internet.de/ao_1977/__122a.html) (Bereitstellung zum Datenabruf), [§ 108 AO](https://www.gesetze-im-internet.de/ao_1977/__108.html) (Fristen), [§ 110 AO](https://www.gesetze-im-internet.de/ao_1977/__110.html) (Wiedereinsetzung)
- [Art. 97 § 28 EGAO (EGAO)](https://www.gesetze-im-internet.de/aoeg_1977/art_97__28.html) (zeitliche Anwendung des § 122a AO)
- [§ 69 FGO](https://www.gesetze-im-internet.de/fgo/__69.html) (AdV beim Finanzgericht), [§ 76 FGO](https://www.gesetze-im-internet.de/fgo/__76.html) (Präklusion im Klageverfahren)

### Gesetzgebung (nicht in Kraft)

- Regierungsentwurf JStG 2026, BT-Drs. 21/8283 vom 30.09.2026 — Art. 18 (§ 367 Abs. 2 S. 1, Abs. 2c AO) und Art. 19, 21 (Bekanntgabe ab 01.01.2027): https://dserver.bundestag.de/btd/21/082/2108283.pdf

### Verwaltungsanweisungen

- AEAO zu §§ 122, 122a, 347 ff. AO
- BMF-Schreiben zur Bekanntgabe durch Bereitstellung zum Datenabruf vom 13.08.2026 `[unverifiziert – prüfen]` (Datum aus Sekundärquellen; GZ und BStBl-Fundstelle prüfen)

### Rechtsprechung

- BFH, Urt. v. 29.07.2025 – VI R 6/23 (Erschütterung der Bekanntgabevermutung) `[unverifiziert – prüfen]`
- BFH, Beschl. v. 08.05.2024 – VIII R 9/23 (Vorlage Aussetzungszinsen); BVerfG – 1 BvL 8/24 (anhängig) `[unverifiziert – prüfen]`

### Literatur

- Seer, in: Tipke/Kruse, AO/FGO, § 367 AO (Gesamtaufrollung, Verböserung) — Lieferungsstand prüfen `[unverifiziert – prüfen]`
- Klein, AO, 18. Aufl. 2024, §§ 122a, 355, 357 AO `[unverifiziert – prüfen]` (Auflage prüfen)
- Suchstring juris/Beck-Online: „§ 122a Abs. 4 AO Bereitstellung Bekanntgabe Einspruchsfrist"
