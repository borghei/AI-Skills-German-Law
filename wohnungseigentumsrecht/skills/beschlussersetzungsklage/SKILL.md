---
name: beschlussersetzungsklage
description: "Durchsetzung eines Anspruchs auf ordnungsmäßige Verwaltung durch die Beschlussersetzungsklage nach WEG – Anspruch des Eigentümers gegen die Gemeinschaft der Wohnungseigentümer § 18 Abs. 2 WEG mit Katalog § 19 Abs. 2 WEG, Beschlussersetzungsklage § 44 Abs. 1 S. 2 WEG gegen die GdWE § 44 Abs. 2 WEG, Vorbefassung der Eigentümerversammlung als Rechtsschutzbedürfnis, Verbindung mit der Anfechtung des Negativbeschlusses und Monatsfrist § 45 WEG, Ermessen des Gerichts, typische Klageziele (Erhaltung, Herstellung, zertifizierter Verwalter, Gestattung nach § 20 Abs. 2 und 3 WEG, Kostenverteilung, Jahresabrechnung), einstweiliger Rechtsschutz, Zuständigkeit § 43 Abs. 2 WEG, Streitwert § 49 GKG. Rechtsstand: Oktober 2026. Use when die Eigentümerversammlung einen notwendigen Beschluss ablehnt oder nicht fasst und ein Eigentümer ihn gerichtlich ersetzen lassen will."
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

# /wohnungseigentumsrecht:beschlussersetzungsklage

## Zweck

Lehnt die Mehrheit einen Beschluss ab, den ordnungsmäßige Verwaltung verlangt, hilft die Anfechtung allein nicht: Sie beseitigt den Negativbeschluss, schafft aber keinen positiven. Dafür gibt es seit dem WEMoG die **Beschlussersetzungsklage**: Unterbleibt eine notwendige Beschlussfassung, kann das Gericht auf Klage eines Eigentümers **den Beschluss fassen** ([§ 44 Abs. 1 S. 2 WEG](https://www.gesetze-im-internet.de/woeigg/__44.html)). Dieser Skill prüft Anspruch, Vorbefassung, Antragsfassung, Kombination mit der Anfechtung und Kostenrisiko.

**Rechtsstand: Oktober 2026.** § 44 WEG ist seit dem WEMoG unverändert. Der V. Zivilsenat hat die **Vorbefassung** 2025 präzisiert (BGH V ZR 86/24) und die Ansprüche auf Erhaltung und Haftung der GdWE 2026 gestärkt (V ZR 102/24, V ZR 18/25). ([V ZR 86/24](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-02-14&Aktenzeichen=V%20ZR%2086/24), [V ZR 102/24](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-04-24&Aktenzeichen=V%20ZR%20102/24), [V ZR 18/25](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-02-27&Aktenzeichen=V%20ZR%2018/25))

## Eingaben

- begehrter Beschluss (konkreter Inhalt: Maßnahme, Umfang, Kosten, Finanzierung, Ausführende)
- Protokoll der Versammlung, in der der Antrag gestellt wurde: Antragstext, Abstimmungsergebnis (Negativbeschluss?) oder Nichtbefassung
- Beschlussdatum (Monatsfrist für die Anfechtung des Negativbeschlusses)
- Unterlagen zur Notwendigkeit (Gutachten, Angebote, Schadensbilder)
- Eilbedürftigkeit (drohender Schaden, Fristablauf)

## Sub-Agent-Architektur

- **Researcher** liefert §§ 18, 19, 20, 44, 45 WEG und die Rechtsprechung zu Vorbefassung und Klagezielen.
- **Drafter** formuliert den Beschlussantrag für die Versammlung und die Klageanträge (Anfechtung + Ersetzung, Haupt- und Hilfsanträge).
- **Reviewer** prüft Vorbefassung, Bestimmtheit des Antrags, Frist und Kostenrisiko.

## Ablauf

### 1. Anspruch auf ordnungsmäßige Verwaltung (§ 18 Abs. 2, § 19 WEG)

- Jeder Eigentümer kann von der **GdWE** eine Verwaltung und Benutzung verlangen, die dem Interesse der Gesamtheit nach billigem Ermessen sowie Gesetz, Vereinbarungen und Beschlüssen entspricht ([§ 18 Abs. 2 WEG](https://www.gesetze-im-internet.de/woeigg/__18.html)).
- Zur ordnungsmäßigen Verwaltung gehören insbesondere Hausordnung, ordnungsmäßige **Erhaltung**, Versicherung, angemessene **Erhaltungsrücklage**, Vorschüsse und die Bestellung eines **zertifizierten Verwalters** ([§ 19 Abs. 2 WEG](https://www.gesetze-im-internet.de/woeigg/__19.html)).
- Bei Ermessensspielräumen setzt die Ersetzung voraus, dass **nur ein bestimmter Beschluss** ordnungsmäßig ist (Ermessensreduzierung) oder dass das Gericht das Ermessen anstelle der Eigentümer ausübt; im zweiten Fall ist ein Rahmenantrag zulässig `[unverifiziert – prüfen: Reichweite des gerichtlichen Ermessens nach § 44 Abs. 1 S. 2 WEG]`.

### 2. Vorbefassung — Zulässigkeitsvoraussetzung

- Der Kläger muss die Angelegenheit **zuerst der Eigentümerversammlung** vorlegen; sonst fehlt das Rechtsschutzbedürfnis.
- Es genügt, dass er in der Versammlung **die Beschlussfassung verlangt** hat, **so wie er sie anschließend gerichtlich ersetzt haben will**; die Zulässigkeit hängt nicht davon ab, dass er weitere Informationen oder Unterlagen vorgelegt hat (BGH, Urt. v. 14.02.2025 – V ZR 86/24, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-02-14&Aktenzeichen=V%20ZR%2086/24)).
- Praxis: Antrag **wortgleich** zur Tagesordnung anmelden (Einberufungsverlangen nach [§ 24 Abs. 2 WEG](https://www.gesetze-im-internet.de/woeigg/__24.html) bei Verweigerung), Abstimmung protokollieren lassen. Für die Begründetheit sind Unterlagen gleichwohl nützlich.
- **Entbehrlich** ist die Vorbefassung, wenn sie sicher erfolglos wäre oder unzumutbar ist (z. B. Mehrheitseigentümer hat bereits endgültig abgelehnt) `[unverifiziert – prüfen]`.

### 3. Negativbeschluss mit anfechten

- Hat die Versammlung den Antrag **abgelehnt**, liegt ein (Negativ-)Beschluss vor. Ihn **binnen eines Monats** mit der Anfechtungsklage angreifen und die Beschlussersetzung im selben Verfahren beantragen ([§ 45 WEG](https://www.gesetze-im-internet.de/woeigg/__45.html)).
- Ob ein bestandskräftiger Negativbeschluss eine spätere Ersetzungsklage sperrt, ist nicht abschließend geklärt `[unverifiziert – prüfen]`; die Kombination vermeidet das Risiko.
- Die Beschlussersetzungsklage selbst ist **nicht fristgebunden**.

```bash
python -m scripts.legal_calc.cli frist --ereignis 22.10.2026 --menge 1 --einheit monate
python -m scripts.legal_calc.cli frist --ereignis 22.10.2026 --menge 2 --einheit monate
```

### 4. Typische Klageziele

| Ziel | Grundlage | Hinweis |
|---|---|---|
| **Erhaltungsmaßnahme** (Dach, Balkone, Leitungen) | § 19 Abs. 2 Nr. 2 WEG | Die GdWE darf und muss jedenfalls bei mehreren sanierungsbedürftigen Balkonen selbst tätig werden, auch wenn die Teilungserklärung die Erhaltung den Eigentümern zuweist; die **vereinbarte Kostenlast** der einzelnen Eigentümer bleibt bestehen (BGH, Urt. v. 24.04.2026 – V ZR 102/24, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-04-24&Aktenzeichen=V%20ZR%20102/24)) |
| **Herstellung** des plangerechten Zustands | § 18 Abs. 2 WEG | Anspruch auf erstmalige Errichtung grundsätzlich gegeben; Grenze Treu und Glauben, wenn die Erfüllung den übrigen nicht zuzumuten ist; § 22 WEG nicht analog (BGH, Urt. v. 20.12.2024 – V ZR 243/23, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-12-20&Aktenzeichen=V%20ZR%20243/23)) |
| **Zertifizierter Verwalter** | § 19 Abs. 2 Nr. 6 WEG | `/wohnungseigentumsrecht:verwalter-bestellung-abberufung` |
| **Gestattung** einer baulichen Veränderung | § 20 Abs. 2, 3 WEG | `/wohnungseigentumsrecht:bauliche-veraenderung` |
| **Kostenverteilung** | § 16 Abs. 2 S. 2 WEG | nur wenn allein der begehrte Schlüssel ordnungsmäßig ist |
| **Jahresabrechnung** / Vermögensbericht | § 28 WEG | Der Anspruch auf Erstellung der Jahresabrechnung richtet sich gegen die GdWE, nicht gegen den Verwalter (BGH, Urt. v. 19.04.2024 – V ZR 167/23, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-04-19&Aktenzeichen=V%20ZR%20167/23)) |

### 5. Prozessuales

- **Beklagte:** GdWE ([§ 44 Abs. 2 WEG](https://www.gesetze-im-internet.de/woeigg/__44.html)); Zuständigkeit Amtsgericht der belegenen Sache ([§ 43 Abs. 2 Nr. 4 WEG](https://www.gesetze-im-internet.de/woeigg/__43.html)).
- **Antrag:** „Das Gericht fasst anstelle der Wohnungseigentümer folgenden Beschluss: …" — bestimmt, vollziehbar, mit Kosten und Finanzierung; hilfsweise Rahmenanträge.
- **Wirkung:** Das rechtskräftige Urteil ersetzt den Beschluss und wirkt für und gegen alle Eigentümer (§ 44 Abs. 3 WEG).
- **Eilfälle:** einstweilige Verfügung auf Durchführung einer Notmaßnahme; daneben das Notgeschäftsführungsrecht jedes Eigentümers bei unmittelbar drohendem Schaden ([§ 18 Abs. 3 WEG](https://www.gesetze-im-internet.de/woeigg/__18.html)).
- **Streitwert:** [§ 49 GKG](https://www.gesetze-im-internet.de/gkg_2004/__49.html); Kosten der GdWE trägt der Kläger auch im Obsiegen anteilig mit (BGH, Urt. v. 19.07.2024 – V ZR 139/23, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-07-19&Aktenzeichen=V%20ZR%20139/23)).

### 6. Schadensersatz bei Verzögerung

Unterlässt die GdWE eine erforderliche Maßnahme am Gemeinschaftseigentum schuldhaft, kann sie dem geschädigten Eigentümer auf Schadensersatz haften (BGH, Urt. v. 27.02.2026 – V ZR 18/25, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-02-27&Aktenzeichen=V%20ZR%2018/25)). Die Haftung ist **keine Gefährdungshaftung**: Sie setzt erst ab dem Zeitpunkt ein, zu dem eine ordnungsmäßig handelnde GdWE die Maßnahme beschlossen und durchgeführt hätte; für Mietausfall gelten weitere Voraussetzungen `[unverifiziert – prüfen: Einzelheiten im Volltext von V ZR 18/25]`. Ablehnende Abstimmungen und Mängelanzeigen dokumentieren — sie belegen den Zeitpunkt und das Verschulden.

### 7. Ergebnis

Anspruch (ja/nein, Ermessensreduzierung), Vorbefassung (erfolgt / nachzuholen), Antragsfassung, Fristen, Eilbedürftigkeit, Kosten.

## Quellen und Zitierweise

Verbindlich: [`../../references/zitierweise.md`](../../references/zitierweise.md).

### Statute

- [§ 44 WEG](https://www.gesetze-im-internet.de/woeigg/__44.html) (Beschlussklagen, Abs. 1 S. 2 Beschlussersetzung), [§ 45 WEG](https://www.gesetze-im-internet.de/woeigg/__45.html)
- [§ 18 WEG](https://www.gesetze-im-internet.de/woeigg/__18.html), [§ 19 WEG](https://www.gesetze-im-internet.de/woeigg/__19.html) (Anspruch und Maßstab), [§ 24 WEG](https://www.gesetze-im-internet.de/woeigg/__24.html) (Einberufungsverlangen)
- [§ 43 WEG](https://www.gesetze-im-internet.de/woeigg/__43.html), [§ 49 GKG](https://www.gesetze-im-internet.de/gkg_2004/__49.html)

### Rechtsprechung (V. Zivilsenat)

1. BGH, Urt. v. 24.04.2026 – V ZR 102/24 (Pflicht der GdWE zur Balkonsanierung; vereinbarte Kostenlast bleibt), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-04-24&Aktenzeichen=V%20ZR%20102/24), [Volltext](https://www.rws-verlag.de/fileadmin/Volltexte-4/V_ZR_102-24.pdf)
2. BGH, Urt. v. 27.02.2026 – V ZR 18/25 (Haftung der GdWE für unterlassene Maßnahmen), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-02-27&Aktenzeichen=V%20ZR%2018/25)
3. BGH, Urt. v. 14.02.2025 – V ZR 86/24 (Vorbefassung), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-02-14&Aktenzeichen=V%20ZR%2086/24)
4. BGH, Urt. v. 20.12.2024 – V ZR 243/23 (Anspruch auf erstmalige Errichtung; Grenze § 242 BGB), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-12-20&Aktenzeichen=V%20ZR%20243/23), [Volltext](https://www.rws-verlag.de/fileadmin/Volltexte-4/V_ZR_243-23.pdf)
5. BGH, Urt. v. 19.07.2024 – V ZR 139/23 (Kostenbeteiligung des obsiegenden Klägers), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-07-19&Aktenzeichen=V%20ZR%20139/23)
6. BGH, Urt. v. 19.04.2024 – V ZR 167/23 (Anspruch auf Jahresabrechnung gegen die GdWE), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2024-04-19&Aktenzeichen=V%20ZR%20167/23)

### Kommentare

- Bärmann/Göbel, WEG, aktuelle Aufl., § 44 Rn. zur Beschlussersetzungsklage `[unverifiziert – prüfen: Auflage und Rn.]`
- Hügel/Elzer, WEG, aktuelle Aufl., § 44 `[unverifiziert – prüfen: Auflage und Rn.]`

## Beispiel (Gutachtenstil, verkürzt)

**Sachverhalt.** Seit zwei Wintern dringt über das undichte Flachdach Wasser in die Dachgeschosswohnung von D ein. Ein Gutachten beziffert die Sanierung auf 95.000 EUR; die Erhaltungsrücklage beträgt 110.000 EUR. In der Versammlung vom 22.10.2026 beantragt D wortgleich: „Das Flachdach wird nach dem Angebot X saniert; Finanzierung aus der Erhaltungsrücklage." Der Antrag wird mehrheitlich abgelehnt.

**Zulässigkeit.** Die Vorbefassung ist erfolgt: D hat genau den Beschluss verlangt, den er ersetzen lassen will (V ZR 86/24). ([V ZR 86/24](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-02-14&Aktenzeichen=V%20ZR%2086/24))

**Begründetheit.** Die Sanierung ist ordnungsmäßige Erhaltung (§ 19 Abs. 2 Nr. 2 WEG); angesichts fortlaufender Durchfeuchtung ist allein die Sanierung ordnungsmäßig. Die Finanzierung aus der Rücklage ist gedeckt.

**Ergebnis.** Klage gegen die GdWE bis **23.11.2026** (22.11.2026 ist ein Sonntag): (1) Ungültigerklärung des Negativbeschlusses, (2) Beschlussersetzung mit dem Antragstext, hilfsweise Rahmenbeschluss; Begründung bis 22.12.2026. Parallel Schadensersatz gegen die GdWE prüfen — für den Zeitraum ab dem Zeitpunkt, zu dem eine ordnungsmäßig handelnde GdWE saniert hätte (V ZR 18/25). ([V ZR 18/25](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2026-02-27&Aktenzeichen=V%20ZR%2018/25))

## Risiken / typische Fehler

- **Ohne Vorbefassung geklagt** → unzulässig; der Antrag muss in der Versammlung so gestellt worden sein, wie er ersetzt werden soll (BGH V ZR 86/24). ([V ZR 86/24](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-02-14&Aktenzeichen=V%20ZR%2086/24))
- **Negativbeschluss nicht angefochten** → Bestandskraftrisiko; Anfechtung binnen eines Monats verbinden.
- **Antrag unbestimmt** → das Gericht kann keinen vollziehbaren Beschluss fassen; Maßnahme, Kosten, Finanzierung angeben.
- **Ermessensspielraum übersehen** → wo mehrere Lösungen ordnungsmäßig sind, nur Rahmenantrag oder Hilfsanträge.
- **Klage gegen die übrigen Eigentümer oder den Verwalter** → Beklagte ist die GdWE (§ 44 Abs. 2 WEG).
- **Eilfall im Hauptsacheverfahren** → einstweilige Verfügung oder Notmaßnahme (§ 18 Abs. 3 WEG) prüfen.

## Ausgabeformat

```
BESCHLUSSERSETZUNGSKLAGE — PRÜFUNG (Rechtsstand Oktober 2026)

1. Begehrter Beschluss: <Wortlaut, Kosten, Finanzierung>
2. Anspruch (§ 18 Abs. 2, § 19 Abs. 2 WEG): <Grundlage> | Ermessen reduziert? <ja/nein>
3. Vorbefassung: Versammlung <Datum>, TOP <…>, Antrag wortgleich? [🟢/🔴]
4. Negativbeschluss: <ja/nein> → Anfechtung bis <Datum>, Begründung bis <Datum>
5. Anträge:
   (1) Ungültigerklärung des Beschlusses zu TOP <…>
   (2) „Das Gericht fasst anstelle der Wohnungseigentümer folgenden Beschluss: …"
   (3) hilfsweise: <Rahmenantrag>
6. Eilrechtsschutz / Notmaßnahme § 18 Abs. 3 WEG: <…>
7. Kosten: Streitwert § 49 GKG <…> | Kostenbeteiligung des obsiegenden Klägers
8. Flankierend: Schadensersatz gegen die GdWE: <…>
```
