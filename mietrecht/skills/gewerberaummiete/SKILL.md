---
name: gewerberaummiete
description: "Gewerberaummiete – Form langfristiger Mietverträge §§ 550, 578 Abs. 1 S. 2 BGB (seit BEG IV Textform; Übergang Art. 229 § 70 EGBGB) und die Unwirksamkeit von Schriftformheilungsklauseln, Index- und Staffelmiete §§ 557a, 557b BGB, vertragsimmanenter Konkurrenzschutz und Sortimentsbindung, Betriebspflicht und Offenhaltungsklausel, AGB-Kontrolle §§ 305 ff. BGB, Störung der Geschäftsgrundlage § 313 BGB und Art. 240 § 7 EGBGB, Kündigungsfristen § 580a BGB, Vermieterpfandrecht § 562 BGB. Use when ein Gewerberaummietvertrag gestaltet, geprüft, beendet oder eine Anpassung wegen veränderter Umstände verlangt wird."
language: de
provider_variants: [claude, gemini, openai]
test: ./test.md
---

# /mietrecht:gewerberaummiete

## Zweck

Die Gewerberaummiete kennt keinen sozialen Bestandsschutz — dafür ein anderes zentrales Risiko: **§ 550 BGB**. Ein Schriftformmangel macht den auf zehn Jahre geschlossenen Vertrag ordentlich kündbar, und die dagegen üblichen Heilungsklauseln tragen nicht. Diese Skill prüft Schriftform, Wertsicherung, Konkurrenzschutz und Betriebspflicht, kontrolliert die AGB und behandelt die Anpassung wegen Störung der Geschäftsgrundlage.

**Rechtsstand: Oktober 2026.** Seit dem Vierten Bürokratieentlastungsgesetz (BEG IV) genügt für Gewerberaummietverträge die **Textform** (§ 578 Abs. 1 S. 2 BGB); für Altverträge galt die Schriftform nach Art. 229 § 70 Abs. 1 EGBGB nur noch bis einschließlich 01.01.2026. Für **Wohnraum** bleibt § 550 BGB bei der Schriftform. Zuständig beim BGH ist der **XII. Zivilsenat**.

## Eingaben

- **Mietvertrag** mit allen Anlagen, Nachträgen und Nebenabreden — vollständig, mit Datumsangaben
- **Laufzeit**, Verlängerungsoptionen, vereinbarte Kündigungsfristen
- **Mietstruktur**: Festmiete, Staffel, Index, Umsatzmiete; Wertsicherungsklausel im Wortlaut
- **Mietzweck / Sortimentsbeschreibung**, Konkurrenzschutz- und Betriebspflichtklauseln
- **Mitbewerber** im Objekt (bei Einkaufszentren: Mieterstruktur, Centermanagement)
- Bei Anpassungsverlangen: Umsatzentwicklung, staatliche Maßnahmen, Hilfen, Versicherungsleistungen
- Ob Verbraucher- oder Unternehmereigenschaft, AGB oder Individualvereinbarung

## Sub-Agent-Architektur

Die Prüfung wird in Prosa von spezialisierten Schritten getragen; einen `agents`-Block trägt diese Skill bewusst nicht (mietrecht-Konvention). Ein **Schriftform-Prüfer** arbeitet den gesamten Vertrag samt Nachträgen auf § 550 BGB durch — dieser Schritt entscheidet über die Laufzeitsicherheit und steht deshalb am Anfang. Ein **Entgelt-Prüfer** kontrolliert Wertsicherung, Staffel und Umsatzmiete. Ein **Nutzungs-Prüfer** klärt Mietzweck, Konkurrenzschutz und Betriebspflicht. Ein **AGB-Prüfer** unterzieht die Klauseln der Inhaltskontrolle nach §§ 305 ff. BGB im unternehmerischen Verkehr. Ein **Anpassungs-Prüfer** bewertet § 313 BGB und Art. 240 § 7 EGBGB.

## Ablauf

### 1. Abgrenzung und anwendbares Recht

Auf die Gewerberaummiete finden die **allgemeinen Mietvorschriften** (§§ 535–548 BGB) sowie die Vorschriften über Mietverhältnisse über Räume Anwendung; die **Schutzvorschriften des Wohnraummietrechts** (§§ 549 ff. BGB — Mietpreisbremse, § 558 BGB, Kündigungsschutz §§ 573 ff. BGB, Sozialklausel §§ 574 ff. BGB) gelten **nicht**. Die Vertragsfreiheit ist entsprechend weit; ihre Grenze bildet die **AGB-Kontrolle** nach §§ 305 ff. BGB, die auch zwischen Unternehmern gilt — allerdings ohne die Klauselverbote der §§ 308, 309 BGB in unmittelbarer Anwendung (§ 310 Abs. 1 BGB), die aber Indizwirkung im Rahmen des § 307 BGB entfalten.

### 2. Form langfristiger Verträge ([§ 550 BGB](https://www.gesetze-im-internet.de/bgb/__550.html), [§ 578 BGB](https://www.gesetze-im-internet.de/bgb/__578.html), [Art. 229 § 70 EGBGB](https://www.gesetze-im-internet.de/bgbeg/art_229__70.html))

Wird der Mietvertrag für **länger als ein Jahr** nicht in der gesetzlichen Form geschlossen, gilt er als **für unbestimmte Zeit geschlossen**; die Kündigung ist frühestens zum Ablauf eines Jahres nach Überlassung zulässig. Ein Formmangel macht aus einem zehnjährigen Vertrag einen ordentlich kündbaren.

**Welche Form gilt? — zuerst zeitlich einordnen:**

| Konstellation | Maßgebliche Form |
|---|---|
| Vertrag geschlossen ab 01.01.2025 | **Textform** (§ 578 Abs. 1 S. 2 BGB, § 126b BGB) |
| Altvertrag (Mietverhältnis vor 01.01.2025 entstanden), Nachtrag ab 01.01.2025 | Textform ab dem Zeitpunkt der Änderungsvereinbarung (Art. 229 § 70 Abs. 1 EGBGB) |
| Altvertrag ohne Nachtrag | Schriftform bis einschließlich 01.01.2026, seither Textform |
| Kündigung wegen Formmangels, die bis 01.01.2026 zuging | wohl nach altem Recht (Schriftform) zu beurteilen — Auslegung des Art. 229 § 70 EGBGB, Rspr. steht aus |

**Textform** (§ 126b BGB) verlangt eine lesbare Erklärung auf einem dauerhaften Datenträger, in der die Person des Erklärenden genannt ist — keine Unterschrift. Ein E-Mail-Wechsel, ein PDF ohne Unterschrift oder eine Vertragsplattform genügen. Unverändert bleibt der **Kern**: Alle **wesentlichen Vertragsbedingungen** — Parteien, Mietobjekt, Miete, Mietzeit — müssen sich aus den in Textform vorliegenden Erklärungen beider Seiten ergeben. Damit entfallen die meisten Unterschrifts-, Vertretungszusatz- und Heftungsfehler; bestehen bleiben die inhaltlichen Mängel:

- **Nachträge** zu wesentlichen Punkten, die nur **mündlich** oder telefonisch vereinbart wurden,
- **Anlagen** (Grundriss, Flächenaufstellung), auf die nicht eindeutig Bezug genommen wird,
- **Parteiwechsel** (Verkauf, Umwandlung) ohne formwahrende Dokumentation,
- **mündliche Nebenabreden** zu wesentlichen Punkten,
- Erklärungen, aus denen die **Annahme** des Angebots in Textform nicht hervorgeht.

**Schriftformheilungsklauseln** — Klauseln, die die Parteien verpflichten, den Formmangel zu heilen und bis dahin nicht ordentlich zu kündigen — sind **unwirksam**; ein Erwerber wird durch sie nicht gebunden (BGH, Urt. v. 27.09.2017 – XII ZR 114/16, BGHZ 216, 68 = NJW 2017, 3772, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2017-09-27&Aktenzeichen=XII%20ZR%20114/16). Die Entscheidung bleibt für Textformmängel übertragbar. Die Berufung auf den Formmangel kann nur ausnahmsweise treuwidrig sein (§ 242 BGB). Konsequenz für die Praxis: **Formaudit** vor jedem Nachtrag und vor jeder Transaktion — nicht auf Heilungsklauseln vertrauen. Bei Altverträgen ist zu dokumentieren, wann zuletzt ein Nachtrag geschlossen wurde, weil davon die anwendbare Form abhängt.

### 3. Staffel- und Indexmiete ([§ 557a BGB](https://www.gesetze-im-internet.de/bgb/__557a.html), [§ 557b BGB](https://www.gesetze-im-internet.de/bgb/__557b.html))

Vertiefung für Wohnraum: `/mietrecht:indexmiete-staffelmiete`. Die **Staffelmiete** legt die Miete für bestimmte Zeiträume betragsmäßig fest; jede Staffel muss der Höhe nach bestimmt sein. Die **Indexmiete** koppelt die Miete an den vom Statistischen Bundesamt ermittelten **Verbraucherpreisindex für Deutschland**. Die Klausel muss die Bezugsgröße, den Basiszeitpunkt, den Anpassungsmechanismus (automatisch oder auf Erklärung) und den Anpassungsrhythmus eindeutig regeln. In der Gewerberaummiete sind die Beschränkungen des Wohnraummietrechts (§ 557b Abs. 2 BGB: mindestens ein Jahr unveränderte Miete) nicht zwingend; die Grenzen ergeben sich aus dem **Preisklauselgesetz** und der AGB-Kontrolle. Einseitige Klauseln, die nur Erhöhungen und keine Senkungen zulassen, sind in AGB kritisch.

### 4. Konkurrenzschutz

Der **vertragsimmanente Konkurrenzschutz** ist eine **ungeschriebene Nebenpflicht** des Vermieters aus § 535 Abs. 1 BGB: Er darf in demselben Objekt kein Konkurrenzunternehmen ansiedeln, das dem Mieter im **vertraglich vereinbarten Hauptsortiment** Konkurrenz macht. Er gilt auch ohne ausdrückliche Vereinbarung, reicht aber nur so weit wie der **im Vertrag festgelegte Mietzweck** — daher ist eine präzise Sortimentsbeschreibung der wirksamste Schutz. Ein **erweiterter** Konkurrenzschutz bedarf der Vereinbarung; ein **Ausschluss** des Konkurrenzschutzes ist in AGB nur eingeschränkt möglich. Rechtsfolgen einer Verletzung: Unterlassungsanspruch, **Minderung** nach § 536 BGB, Schadensersatz, in schweren Fällen Kündigung nach § 543 BGB.

### 5. Betriebspflicht und Offenhaltung

Eine **Betriebspflicht** — die Pflicht, das Geschäft während der Öffnungszeiten zu betreiben — besteht **nicht kraft Gesetzes**; sie muss vereinbart werden. In Einkaufszentren ist sie üblich und im Grundsatz auch formularvertraglich zulässig, weil das Centerkonzept ein berechtigtes Interesse begründet. Kritisch in AGB sind: Betriebspflicht **kombiniert mit** Sortimentsbindung **und** Ausschluss des Konkurrenzschutzes (Kumulationswirkung), starre Öffnungszeitenvorgaben ohne Anpassungsmöglichkeit und Vertragsstrafen. Bei behördlich angeordneter Schließung wird die Betriebspflicht suspendiert.

### 6. Störung der Geschäftsgrundlage ([§ 313 BGB](https://www.gesetze-im-internet.de/bgb/__313.html), [Art. 240 § 7 EGBGB](https://www.gesetze-im-internet.de/bgbeg/art_240.html))

**Art. 240 § 7 EGBGB** (historische COVID-19-Sonderregel; heute nur noch für Altfälle und als Abwägungsmuster relevant) enthält eine **tatsächliche Vermutung**: Sind vermietete Grundstücke oder Räume infolge staatlicher Maßnahmen zur Bekämpfung der COVID-19-Pandemie für den Betrieb des Mieters nicht oder nur erheblich eingeschränkt verwendbar, wird vermutet, dass sich insoweit ein **Umstand im Sinne des § 313 Abs. 1 BGB, der zur Grundlage des Mietvertrags geworden ist, nach Vertragsschluss schwerwiegend verändert hat**. Die Vermutung betrifft nur das **reale Element**; **Zumutbarkeit** und **Anpassungsumfang** bleiben Gegenstand einer umfassenden Einzelfallabwägung.

Der BGH hat dazu geklärt: Eine coronabedingte Geschäftsschließung begründet **keinen Mangel** im Sinne des § 536 BGB und führt nicht zur Unmöglichkeit; in Betracht kommt allein eine Anpassung nach § 313 Abs. 1 BGB, und zwar **nicht pauschal hälftig**, sondern nach einer umfassenden Abwägung aller Umstände des Einzelfalls — Umsatzrückgang im konkreten Objekt, staatliche Hilfen, Versicherungsleistungen, ersparte Aufwendungen, Fortbestand der Existenz (BGH, Urt. v. 12.01.2022 – XII ZR 8/21, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2022-01-12&Aktenzeichen=XII%20ZR%208/21). Nach **§ 313 Abs. 3 BGB** kommt der **Rücktritt** — beim Dauerschuldverhältnis die **Kündigung** — nur in Betracht, wenn eine Anpassung nicht möglich oder einem Teil nicht zumutbar ist; die Anpassung hat also stets Vorrang.

### 7. Kündigung und Beendigung ([§ 580a BGB](https://www.gesetze-im-internet.de/bgb/__580a.html), [§ 543 BGB](https://www.gesetze-im-internet.de/bgb/__543.html))

Bei **unbefristeten** Verträgen über Geschäftsräume ist die ordentliche Kündigung **spätestens am dritten Werktag eines Kalendervierteljahres zum Ablauf des nächsten Kalendervierteljahres** zulässig (§ 580a Abs. 2 BGB). Abweichende Vereinbarungen sind zulässig. **Befristete** Verträge enden mit Zeitablauf; eine ordentliche Kündigung ist ausgeschlossen — es sei denn, ein Schriftformmangel nach § 550 BGB eröffnet sie. Die **außerordentliche fristlose Kündigung** nach § 543 BGB bleibt stets möglich; § 569 BGB gilt für Geschäftsräume nicht, insbesondere gibt es **keine Schonfristzahlung**. Ein **Vermieterpfandrecht** an den eingebrachten Sachen besteht nach [§ 562 BGB](https://www.gesetze-im-internet.de/bgb/__562.html). Zur Räumung: `/mietrecht:raeumungsklage`.

**Rückerhalt und Verjährung (§ 548 BGB):** Der Rückerhalt setzt voraus, dass der Vermieter die unmittelbare Sachherrschaft erlangt; er kann vor Vertragsende liegen, und nach einem gescheiterten Übergabetermin kann der Einwurf der Schlüssel in den Briefkasten genügen (BGH, Urt. v. 29.01.2025 – XII ZR 96/23, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-01-29&Aktenzeichen=XII%20ZR%2096/23). Die sechsmonatige Verjährung der Ersatzansprüche läuft ab diesem Zeitpunkt.

### 8. Anhängige Reform (BT-Drs. 21/6807)

Der Regierungsentwurf eines Gesetzes zur Änderung des Rechts der Wohn- und Geschäftsraummiete (BT-Drs. 21/6807 v. 01.07.2026; Anhörung im Rechtsausschuss 14.10.2026; **Stand 23.10.2026 nicht verabschiedet**) betrifft auch Geschäftsräume: § 566 BGB soll auf die Veräußerung an einen Miteigentümer erstreckt werden (Streichung von „an einen Dritten"), § 578 Abs. 3 BGB für Träger sozialer Wohnraumversorgung erweitert werden. Bis zur Verkündung gilt das bisherige Recht; Gestaltungen sollten auf beide Fassungen geprüft werden.

## Quellen

### Statute

- [§ 535 BGB](https://www.gesetze-im-internet.de/bgb/__535.html), [§ 536 BGB](https://www.gesetze-im-internet.de/bgb/__536.html), [§ 543 BGB](https://www.gesetze-im-internet.de/bgb/__543.html), [§ 550 BGB](https://www.gesetze-im-internet.de/bgb/__550.html), [§ 562 BGB](https://www.gesetze-im-internet.de/bgb/__562.html), [§ 580a BGB](https://www.gesetze-im-internet.de/bgb/__580a.html), [§ 578 BGB](https://www.gesetze-im-internet.de/bgb/__578.html), [§ 126b BGB](https://www.gesetze-im-internet.de/bgb/__126b.html), [§ 548 BGB](https://www.gesetze-im-internet.de/bgb/__548.html)
- [Art. 229 § 70 EGBGB](https://www.gesetze-im-internet.de/bgbeg/art_229__70.html) (Übergang zur Textform)
- [§ 557a BGB](https://www.gesetze-im-internet.de/bgb/__557a.html), [§ 557b BGB](https://www.gesetze-im-internet.de/bgb/__557b.html)
- [§ 305 BGB](https://www.gesetze-im-internet.de/bgb/__305.html), [§ 307 BGB](https://www.gesetze-im-internet.de/bgb/__307.html), [§ 310 BGB](https://www.gesetze-im-internet.de/bgb/__310.html), [§ 313 BGB](https://www.gesetze-im-internet.de/bgb/__313.html), [§ 242 BGB](https://www.gesetze-im-internet.de/bgb/__242.html)
- [Art. 240 EGBGB](https://www.gesetze-im-internet.de/bgbeg/art_240.html) (§ 7 — Störung der Geschäftsgrundlage bei Miete), [PrKG](https://www.gesetze-im-internet.de/prklg/)

### Kommentare

- Leo, in: Lindner-Figura/Oprée/Stellmann, Geschäftsraummiete, aktuelle Auflage, Kap. 6 (Schriftform)
- Bieber, in: MüKoBGB, 9. Aufl. 2023, § 550 Rn. 1 ff.; § 580a Rn. 1 ff.
- Blank/Börstinghaus, Miete, aktuelle Auflage, § 550 Rn. 1 ff.
- Weidenkaff, in: Grüneberg, BGB, 84. Aufl. 2025, § 550 Rn. 1 ff.; § 313 Rn. 1 ff.

### Rechtsprechung

- BGH, Urt. v. 27.09.2017 – XII ZR 114/16, BGHZ 216, 68 = NJW 2017, 3772 (Schriftformheilungsklauseln unwirksam; treuwidrige Berufung auf den Schriftformmangel nur ausnahmsweise) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2017-09-27&Aktenzeichen=XII%20ZR%20114/16
- BGH, Urt. v. 12.01.2022 – XII ZR 8/21 (Mietzahlungspflicht bei coronabedingter Geschäftsschließung; kein Mangel, Anpassung nach § 313 BGB nur nach Einzelfallabwägung) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2022-01-12&Aktenzeichen=XII%20ZR%208/21
- BGH, Urt. v. 29.01.2025 – XII ZR 96/23 (Rückerhalt i.S.v. § 548 BGB; Schlüsseleinwurf nach gescheitertem Übergabetermin) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-01-29&Aktenzeichen=XII%20ZR%2096/23
- Zur Reichweite des vertragsimmanenten Konkurrenzschutzes und zur AGB-Kontrolle von Betriebspflichtklauseln ist die einschlägige BGH-Rechtsprechung heranzuziehen `[unverifiziert – prüfen]`.

## Formulierungshilfe — Anpassungsverlangen nach § 313 BGB

```
Sehr geehrte Damen und Herren,

für das Mietverhältnis über die Gewerbeeinheit <Anschrift> verlange ich
namens meiner Mandantschaft die Anpassung der Miete gemäß § 313 Abs. 1 BGB
für den Zeitraum <von> bis <bis>.

1. Reales Element: Die Mieträume waren aufgrund <Bezeichnung der
   staatlichen Maßnahme> vom <Datum> bis <Datum> für den vertraglich
   vereinbarten Betrieb <nicht / nur erheblich eingeschränkt> verwendbar.
   Insoweit greift die Vermutung des Art. 240 § 7 Abs. 1 EGBGB.
2. Umsatzentwicklung: Der Umsatz der Einheit betrug im Vergleichszeitraum
   des Vorjahres <Betrag> EUR, im betroffenen Zeitraum <Betrag> EUR,
   mithin ein Rückgang von <…> %. Die Zahlen sind durch die beigefügte
   betriebswirtschaftliche Auswertung belegt.
3. Kompensation: Staatliche Hilfen wurden in Höhe von <Betrag> EUR gewährt
   bzw. <abgelehnt / beantragt>. Leistungen einer
   Betriebsschließungsversicherung wurden <nicht erbracht / in Höhe von
   <Betrag> erbracht>. Ersparte Aufwendungen betrugen <Betrag> EUR.
4. Zumutbarkeit: Unter Abwägung aller Umstände — insbesondere <…> — ist
   das Festhalten am unveränderten Vertrag unzumutbar. Eine pauschale
   hälftige Teilung wird ausdrücklich nicht zugrunde gelegt.

Ich schlage eine Reduzierung der Nettokaltmiete um <…> % für den genannten
Zeitraum vor und bitte um Rückäußerung bis zum <Datum>.

Mit freundlichen Grüßen
```

## Ausgabeformat

```
GEWERBERAUMMIETE — Prüfung — <Mandat-ID> — <Datum>

I.    Vertragstyp / anwendbares Recht    [Geschäftsraum — §§ 573 ff. BGB nicht anwendbar]
II.   Schriftform (§ 550 BGB) — AUDIT
      - Anwendbare Form                  [Textform § 578 Abs. 1 S. 2 / Schriftform Altrecht]
      - Wesentliche Bedingungen erfasst  [✅ / ❌]
      - Nachträge formwahrend            [✅ / ❌ <Nachtrag Nr. …>]
      - Anlagen in Bezug genommen        [✅ / ❌]
      - Parteiwechsel dokumentiert       [✅ / N/A / ❌]
      Schriftformheilungsklausel         [vorhanden — unwirksam / keine]
      FOLGE                              [Laufzeit gesichert /
                                          ordentlich kündbar zum <Datum> 🔴]
III.  Mietstruktur                       [Fest / Staffel § 557a / Index § 557b / Umsatz]
      Wertsicherungsklausel              [wirksam / PrKG-Risiko / AGB-Risiko]
IV.   Mietzweck / Sortiment              <Wortlaut>
      Konkurrenzschutz                   [vertragsimmanent / erweitert / ausgeschlossen]
      Verletzung                         [nein / ja → Unterlassung, § 536, § 543]
V.    Betriebspflicht                    [keine / vereinbart]  AGB-Kontrolle [✅ / ⚠️]
      Kumulation mit Sortimentsbindung   [unkritisch / ⚠️]
VI.   Störung der Geschäftsgrundlage
      - Art. 240 § 7 EGBGB Vermutung     [greift / N/A]
      - Umsatzrückgang                   <…> %
      - Staatliche Hilfen / Versicherung <Betrag>
      - Ergebnis Abwägung                [Anpassung um <…> % / keine]
      - § 313 Abs. 3 BGB Kündigung       [nachrangig / ausnahmsweise]
VII.  Beendigung                         [Zeitablauf <Datum> / § 580a Abs. 2 BGB /
                                          § 543 BGB]
      Schonfristzahlung § 569 BGB        [N/A — gilt nicht für Geschäftsraum]
VIII. Vermieterpfandrecht (§ 562 BGB)    [besteht / eingeschränkt]

Ergebnis: <…>
Risiko: [🟢 / 🟡 / 🔴]
```

## Risiken / typische Fehler

- **Schriftformmangel nach § 550 BGB** — der größte Einzelrisikoposten der Gewerberaummiete; er macht den langfristigen Vertrag ordentlich kündbar und wird typischerweise erst bei der Transaktion entdeckt.
- **Auf Schriftformheilungsklausel vertraut** — sie ist unwirksam und bindet insbesondere den Erwerber nicht; stattdessen Schriftformaudit vor jedem Nachtrag.
- **Nachträge und Anlagen nicht formwahrend** — mündliche Änderungen wesentlicher Punkte oder fehlende Bezugnahme auf Anlagen genügen auch unter der Textform für den Formmangel.
- **Alte Schriftform-Maßstäbe auf Neuverträge angewendet** — seit BEG IV genügt Textform (§ 578 Abs. 1 S. 2 BGB); Unterschrifts- und Heftungsfehler tragen für Verträge ab 01.01.2025 und für Altverträge seit 02.01.2026 keine Kündigung mehr. Umgekehrt: Für Wohnraum gilt weiter Schriftform.
- **Konkurrenzschutz mit zu weitem Mietzweck** — der vertragsimmanente Schutz reicht nur so weit wie das vereinbarte Hauptsortiment; unpräzise Zweckbestimmung entwertet ihn.
- **Betriebspflicht in AGB kumuliert** — Betriebspflicht plus Sortimentsbindung plus Ausschluss des Konkurrenzschutzes kann in der Gesamtschau unangemessen benachteiligen.
- **Coronaschließung als Mangel behandelt** — § 536 BGB greift nicht; allein § 313 BGB kommt in Betracht.
- **Hälftige Teilung als Automatismus** — Art. 240 § 7 EGBGB vermutet nur das reale Element; die Anpassungshöhe erfordert eine umfassende Einzelfallabwägung.
- **Wohnraummietrecht angewendet** — Mietpreisbremse, § 558 BGB, Kündigungsschutz und Sozialklausel gelten für Geschäftsräume nicht; ebenso wenig die Schonfristzahlung des § 569 BGB.
