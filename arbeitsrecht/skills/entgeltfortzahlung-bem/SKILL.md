---
name: entgeltfortzahlung-bem
description: "Entgeltfortzahlung im Krankheitsfall und Betriebliches Eingliederungsmanagement – Anspruch und Sechs-Wochen-Zeitraum § 3 EFZG mit Wartezeit, Fortsetzungserkrankung und Einheit des Verhinderungsfalls, Entgeltausfallprinzip § 4 EFZG, Anzeige- und Nachweispflicht einschließlich eAU § 5 EFZG, Leistungsverweigerungsrecht § 7 EFZG, Erschütterung des Beweiswerts der Arbeitsunfähigkeitsbescheinigung nach der BAG-Rechtsprechung, BEM § 167 Abs. 2 SGB IX und seine Bedeutung für die krankheitsbedingte Kündigung (Drei-Stufen-Prüfung). Use when Entgeltfortzahlung verweigert oder verlangt, eine AU-Bescheinigung angezweifelt, ein BEM durchgeführt oder eine krankheitsbedingte Kündigung vorbereitet wird."
language: de
agents:
  researcher: ../../agents/researcher.md
  drafter: ../../agents/drafter.md
  reviewer: ../../agents/reviewer.md
provider_variants: [claude, gemini, openai]
test: ./test.md
---

# /arbeitsrecht:entgeltfortzahlung-bem

## Zweck

Krankheit ist der häufigste Anlass arbeitsrechtlicher Auseinandersetzungen unterhalb der Kündigungsschwelle — und der häufigste Grund, warum krankheitsbedingte Kündigungen scheitern. Zwei Fragen stehen im Vordergrund: Muss der Arbeitgeber zahlen (EFZG), und hat er vor einer Kündigung alles getan, was § 167 Abs. 2 SGB IX verlangt? Dieser Skill prüft beide Stränge, bewertet den Beweiswert von Arbeitsunfähigkeitsbescheinigungen nach der verschärften BAG-Linie und dokumentiert das BEM prüffest.

> **Rechtsstand: Oktober 2026.** EFZG und § 167 SGB IX sind 2025/2026 inhaltlich unverändert; die Rechtsprechung zur Erschütterung des Beweiswerts hat sich seit 2021 fortentwickelt.

## Eingaben

- Beginn des Arbeitsverhältnisses (Wartezeit § 3 Abs. 3 EFZG), regelmäßige Arbeitszeit, Vergütungsbestandteile
- AU-Zeiträume der letzten 12 Monate (bzw. drei Jahre für die Prognose) mit Diagnosen, soweit bekannt, und Bescheinigungsart (eAU, Privatarzt, Ausland, Telefon-AU)
- Zeitlicher Zusammenhang mit Kündigung, Urlaubsablehnung, Konflikt, Nebentätigkeit
- Kosten: gezahlte Entgeltfortzahlung je Jahr, Betriebsablaufstörungen
- BEM: Einladung (Datum, Inhalt, Datenschutzhinweis), Reaktion, Gespräche, Maßnahmen
- Betriebsrat, Schwerbehindertenvertretung, schwerbehinderte oder gleichgestellte Person?

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert EFZG- und SGB-IX-Normen mit URL sowie die BAG-Linien zur Fortsetzungserkrankung, zum Beweiswert der AU und zum BEM.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) erstellt Zahlungsverweigerung, BEM-Einladung, BEM-Protokoll oder Kündigungsvermerk.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Zeiträume, Beweislast, Datenschutz und die Kündigungsreife.

## Ablauf

### 1. Anspruch auf Entgeltfortzahlung ([§ 3 EFZG](https://www.gesetze-im-internet.de/entgfg/__3.html))

- **Voraussetzungen:** Arbeitsunfähigkeit infolge Krankheit, **Monokausalität** (Krankheit ist die alleinige Ursache des Arbeitsausfalls), kein Verschulden des Arbeitnehmers (grobes Verschulden gegen sich selbst).
- **Wartezeit:** Anspruch erst nach **vierwöchiger** ununterbrochener Dauer des Arbeitsverhältnisses (§ 3 Abs. 3 EFZG).
- **Dauer:** bis zu **sechs Wochen** je Krankheit.
- **Einheit des Verhinderungsfalls:** Tritt während einer AU eine neue Krankheit hinzu, entsteht kein neuer Sechs-Wochen-Zeitraum. Der Arbeitnehmer muss bei unmittelbar aneinander anschließenden Bescheinigungen darlegen und beweisen, dass die erste AU geendet hatte `[unverifiziert – prüfen]`.
- **Fortsetzungserkrankung** (§ 3 Abs. 1 S. 2 EFZG): Bei erneuter AU wegen **derselben** Krankheit neuer Anspruch nur, wenn der Arbeitnehmer vorher **sechs Monate** nicht wegen dieser Krankheit arbeitsunfähig war oder seit Beginn der ersten AU **zwölf Monate** abgelaufen sind. Der Arbeitgeber kann über die Krankenkasse Auskunft verlangen ([§ 69 Abs. 4 SGB X](https://www.gesetze-im-internet.de/sgb_10/__69.html)).

### 2. Höhe ([§ 4 EFZG](https://www.gesetze-im-internet.de/entgfg/__4.html))

- **Entgeltausfallprinzip:** 100 % des Entgelts, das bei Arbeit angefallen wäre.
- Nicht erfasst: Überstundenvergütung (§ 4 Abs. 1a EFZG) und Aufwendungsersatz.
- Tarifliche Abweichungen in der Bemessungsgrundlage zulässig (§ 4 Abs. 4 EFZG).
- Nach sechs Wochen: Krankengeld der Krankenkasse ([§ 44 SGB V](https://www.gesetze-im-internet.de/sgb_5/__44.html)); Erstattung für Kleinbetriebe über die U1-Umlage nach dem AAG.

### 3. Anzeige und Nachweis ([§ 5 EFZG](https://www.gesetze-im-internet.de/entgfg/__5.html))

- **Anzeigepflicht:** unverzüglich, unabhängig von der Dauer.
- **Nachweispflicht:** bei AU von mehr als **drei Kalendertagen** spätestens am folgenden Arbeitstag; der Arbeitgeber kann die Vorlage **früher** verlangen (§ 5 Abs. 1 S. 3 EFZG) — auch ab dem ersten Tag, ohne Begründung.
- **eAU** (§ 5 Abs. 1a EFZG): Gesetzlich Versicherte müssen die AU ärztlich feststellen lassen; der Arbeitgeber **ruft die Daten bei der Krankenkasse ab**. Keine eAU bei Privatversicherten, Privatärzten und Auslandsbescheinigungen — dort bleibt die Vorlagepflicht.
- **Leistungsverweigerungsrecht** ([§ 7 EFZG](https://www.gesetze-im-internet.de/entgfg/__7.html)): solange der Nachweis nicht erbracht ist — vorläufig, nicht endgültig.

### 4. Beweiswert der AU-Bescheinigung

Die AU-Bescheinigung hat einen **hohen Beweiswert**. Der Arbeitgeber kann ihn nur durch **tatsächliche Umstände** erschüttern, die ernsthafte Zweifel begründen; dann muss der Arbeitnehmer die AU voll beweisen (Entbindung des Arztes von der Schweigepflicht, Zeugnis).

Anerkannte Fallgruppen:

| Fallgruppe | Leitlinie |
|---|---|
| AU deckt **passgenau** die Kündigungsfrist ab | BAG, Urt. v. 08.09.2021 – 5 AZR 149/21 (Eigenkündigung, AU taggleich bis Fristende), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BAG&Datum=2021-09-08&Aktenzeichen=5%20AZR%20149/21) |
| Folgebescheinigungen bis Fristende nach Arbeitgeberkündigung | BAG, Urt. v. 13.12.2023 – 5 AZR 137/23 `[unverifiziert – prüfen]` |
| Passgenaue AU auch bei vorheriger Krankheitsgeschichte | BAG, Urt. v. 21.08.2024 – 5 AZR 248/23; BAG, Urt. v. 18.09.2024 – 5 AZR 29/24 `[unverifiziert – prüfen]` |
| Ausländische AU mit auffälligen Umständen (lange AU, Rückflug am Folgetag gebucht) | BAG, Urt. v. 15.01.2025 – 5 AZR 284/24 `[unverifiziert – prüfen]` |
| Angekündigte Krankheit, Freizeitaktivitäten, Nebentätigkeit während AU | st. Rspr. `[unverifiziert – prüfen]` |

**Vorgehen:** Zweifel dokumentieren, Begutachtung durch den Medizinischen Dienst über die Krankenkasse anregen ([§ 275 Abs. 1a SGB V](https://www.gesetze-im-internet.de/sgb_5/__275.html)), Zahlung unter Hinweis auf die erschütterte Beweiswirkung zurückhalten. Detektiveinsatz nur bei konkretem Verdacht und mit Verhältnismäßigkeitsprüfung (§ 26 BDSG).

### 5. Betriebliches Eingliederungsmanagement ([§ 167 Abs. 2 SGB IX](https://www.gesetze-im-internet.de/sgb_9_2018/__167.html))

- **Auslöser:** innerhalb eines Jahres länger als **sechs Wochen** ununterbrochen **oder wiederholt** arbeitsunfähig — für **alle** Beschäftigten, nicht nur schwerbehinderte Menschen. Maßgeblich sind die letzten zwölf Monate, nicht das Kalenderjahr.
- **Einladung:** Hinweis auf Ziele des BEM, Freiwilligkeit, Art und Umfang der erhobenen Daten; Beteiligung von Betriebsrat und ggf. SBV nur mit Zustimmung der betroffenen Person.
- **Ablauf:** offener, ergebnisoffener Suchprozess; keine Pflicht zu einer bestimmten Form, aber zu den gesetzlichen Mindeststandards.
- **Wiederholung:** Ist der Arbeitnehmer nach Abschluss eines BEM erneut mehr als sechs Wochen innerhalb eines Jahres arbeitsunfähig, ist grundsätzlich **ein neues BEM** anzubieten (BAG, Urt. v. 18.11.2021 – 2 AZR 138/21 `[unverifiziert – prüfen]`).
- **Mitbestimmung:** Ausgestaltung des Verfahrens nach § 87 Abs. 1 Nr. 1, 6, 7 BetrVG.

### 6. Krankheitsbedingte Kündigung — Drei-Stufen-Prüfung

1. **Negative Gesundheitsprognose** — in der Regel indiziert durch erhebliche Fehlzeiten der letzten drei Jahre (Kurzerkrankungen) bzw. Ungewissheit der Wiederherstellung (Langzeiterkrankung).
2. **Erhebliche Beeinträchtigung betrieblicher Interessen** — Entgeltfortzahlungskosten von mehr als sechs Wochen jährlich oder Betriebsablaufstörungen.
3. **Interessenabwägung** — Betriebszugehörigkeit, Ursache (Arbeitsunfall?), Alter, Unterhaltspflichten.

**Bedeutung des BEM:** Das BEM ist keine formelle Wirksamkeitsvoraussetzung, konkretisiert aber den **Verhältnismäßigkeitsgrundsatz**. Hat der Arbeitgeber kein ordnungsgemäßes BEM angeboten, trägt er die **erweiterte Darlegungslast**, dass auch ein BEM keine Weiterbeschäftigungsmöglichkeit (leidensgerechter Arbeitsplatz, Reha, Arbeitszeitreduzierung) ergeben hätte (BAG, Urt. v. 20.11.2014 – 2 AZR 755/13 `[unverifiziert – prüfen]`). Für die Kündigung selbst: `/arbeitsrecht:kuendigungs-pruefung`.

## Quellen

### Statute

- [§ 3 EFZG](https://www.gesetze-im-internet.de/entgfg/__3.html), [§ 4 EFZG](https://www.gesetze-im-internet.de/entgfg/__4.html), [§ 5 EFZG](https://www.gesetze-im-internet.de/entgfg/__5.html), [§ 7 EFZG](https://www.gesetze-im-internet.de/entgfg/__7.html), [§ 8 EFZG](https://www.gesetze-im-internet.de/entgfg/__8.html)
- [§ 167 SGB IX](https://www.gesetze-im-internet.de/sgb_9_2018/__167.html)
- [§ 44 SGB V](https://www.gesetze-im-internet.de/sgb_5/__44.html), [§ 275 SGB V](https://www.gesetze-im-internet.de/sgb_5/__275.html), [§ 69 SGB X](https://www.gesetze-im-internet.de/sgb_10/__69.html)
- [§ 1 KSchG](https://www.gesetze-im-internet.de/kschg/__1.html), [§ 87 BetrVG](https://www.gesetze-im-internet.de/betrvg/__87.html), [§ 26 BDSG](https://www.gesetze-im-internet.de/bdsg_2018/__26.html)

### Kommentare

- Reinhard, in: ErfK, 26. Aufl. 2026, § 3 EFZG Rn. 1 ff. `[unverifiziert – prüfen]` (Auflage prüfen)
- Schmitt, EFZG, 9. Aufl., § 5 Rn. 1 ff. `[unverifiziert – prüfen]`

### Rechtsprechung

- BAG, Urt. v. 08.09.2021 – 5 AZR 149/21 (Erschütterung des Beweiswerts bei passgenauer AU nach Eigenkündigung), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BAG&Datum=2021-09-08&Aktenzeichen=5%20AZR%20149/21)
- BAG, Urt. v. 13.12.2023 – 5 AZR 137/23 (Folgebescheinigungen nach Arbeitgeberkündigung) `[unverifiziert – prüfen]`
- BAG, Urt. v. 21.08.2024 – 5 AZR 248/23 und Urt. v. 18.09.2024 – 5 AZR 29/24 (passgenaue AU) `[unverifiziert – prüfen]`
- BAG, Urt. v. 15.01.2025 – 5 AZR 284/24 (ausländische AU-Bescheinigung) `[unverifiziert – prüfen]`
- BAG, Urt. v. 18.11.2021 – 2 AZR 138/21 (erneutes BEM) `[unverifiziert – prüfen]`
- BAG, Urt. v. 20.11.2014 – 2 AZR 755/13 (Darlegungslast ohne BEM) `[unverifiziert – prüfen]`

## Ausgabeformat

```
ENTGELTFORTZAHLUNG / BEM — <Mandat-ID> — <Datum>
Rechtsstand: Oktober 2026

I.    Anspruch § 3 EFZG
      Wartezeit (4 Wochen):           [erfüllt / nicht erfüllt]
      AU-Zeitraum / Diagnose:         <…>
      Fortsetzungserkrankung:         [ja — 6/12-Monats-Regel: … / nein]
      Einheit des Verhinderungsfalls: [ja / nein]
      Sechs-Wochen-Zeitraum endet:    <Datum>
II.   Höhe § 4 EFZG                   <Entgelt, ohne Überstunden>
III.  Nachweis § 5 EFZG               [eAU abgerufen / Papier / Ausland]
IV.   Beweiswert der AU               [unerschüttert / erschüttert — Umstände: …]
      Maßnahmen:                      <MD-Begutachtung, Zahlungsvorbehalt>
V.    BEM § 167 Abs. 2 SGB IX
      Auslöser (> 6 Wochen / 12 Mon.): [ja / nein]
      Einladung ordnungsgemäß:        [ja / nein — Mangel: …]
      Ergebnis / Maßnahmen:           <…>
VI.   Kündigungsreife (Drei-Stufen-Prüfung)
      Prognose / Beeinträchtigung / Abwägung: <…>
VII.  Empfehlung und nächste Schritte
```

## Beispiel (Gutachtenstil, verkürzt)

**Sachverhalt.** Lagermitarbeiter, seit 2017 beschäftigt, kündigt am 02.09.2026 zum 30.09.2026 und legt am 03.09.2026 eine AU-Bescheinigung bis exakt 30.09.2026 vor.

**Frage: Muss der Arbeitgeber Entgeltfortzahlung leisten?** Ein Anspruch aus § 3 Abs. 1 EFZG setzt krankheitsbedingte Arbeitsunfähigkeit voraus, die der Arbeitnehmer grundsätzlich durch die AU-Bescheinigung beweist. Deren hoher Beweiswert kann erschüttert werden, wenn tatsächliche Umstände ernsthafte Zweifel begründen. Hier deckt die Bescheinigung passgenau die Restlaufzeit nach der Eigenkündigung ab. Das ist die Fallgruppe, in der das BAG 2021 die Erschütterung bejaht hat (BAG 2021, oben Nr. 4). Die Beweiswirkung ist damit erschüttert; der Arbeitnehmer muss die Arbeitsunfähigkeit nun voll beweisen, etwa durch Vernehmung des behandelnden Arztes nach Entbindung von der Schweigepflicht.

**Ergebnis.** Der Arbeitgeber kann die Zahlung zurückhalten und die Begutachtung durch den Medizinischen Dienst anregen; er sollte den Arbeitnehmer unter Hinweis auf die zeitliche Deckung zur Darlegung auffordern. Plant der Arbeitgeber später eine krankheitsbedingte Kündigung und war der Mitarbeiter innerhalb eines Jahres länger als sechs Wochen arbeitsunfähig, ist zuvor ein ordnungsgemäßes BEM anzubieten; ohne BEM trägt der Arbeitgeber die erweiterte Darlegungslast.

## Risiken / typische Fehler

- **Fortsetzungserkrankung nicht geprüft** — bei derselben Krankheit entsteht ein neuer Sechs-Wochen-Zeitraum nur nach der 6/12-Monats-Regel; Auskunft der Krankenkasse einholen.
- **Beweiswert der AU ohne Tatsachen bestritten** — pauschales Bestreiten genügt nicht; erforderlich sind konkrete Umstände wie passgenaue Deckung der Kündigungsfrist.
- **Zahlung endgültig verweigert statt zurückbehalten** — § 7 EFZG gibt nur ein vorläufiges Leistungsverweigerungsrecht.
- **eAU bei Privatversicherten erwartet** — dort bleibt es bei der Vorlage der Papierbescheinigung.
- **BEM nur schwerbehinderten Beschäftigten angeboten** — § 167 Abs. 2 SGB IX gilt für alle Beschäftigten.
- **BEM-Einladung ohne Datenschutzhinweis** — eine Einladung ohne Hinweis auf Ziele und erhobene Daten ist nicht ordnungsgemäß.
- **Kein erneutes BEM nach neuer Sechs-Wochen-Phase** — ein früheres BEM verbraucht die Pflicht nicht.
- **Krankheitsbedingte Kündigung ohne BEM** — trägt die erweiterte Darlegungslast und scheitert regelmäßig an der Verhältnismäßigkeit.
- **Detektiv ohne konkreten Verdacht** — Verwertungsverbot und Schadensersatzrisiko nach DSGVO.
