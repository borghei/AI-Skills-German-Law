# Mietrecht

**Skills für die wohnraum- und gewerberaummietrechtliche Praxis.**

**20 Skills, Rechtsstand Oktober 2026.** Geltendes Recht und anhängige Reformen (Regierungsentwurf BT-Drs. 21/6807, Bundesratsentwürfe BT-Drs. 21/1397 und 21/3509) sind in jedem Skill getrennt ausgewiesen.

Alle Skills sind zweiseitig angelegt: Dieselbe Prüfkaskade trägt den Gestaltungsentwurf des Vermieters und die Abwehrprüfung des Mieters. Mehrere Skills binden die deterministischen Rechner in [`../scripts/legal_calc/`](../scripts/legal_calc/) ein (Fristen §§ 187–193 BGB, Verzugszinsen §§ 288, 247 BGB); die Arithmetik ist maschinell, Zugang und Fristbeginn bleiben juristische Eingaben.

## Skills

| Skill | Funktion | Anker |
|---|---|---|
| `mieterhoehung-558-bgb` | Mieterhöhung auf die ortsübliche Vergleichsmiete — Vermieter-Entwurf und Mieter-Prüfung in einem Ablauf | §§ 558, 558a–558e BGB |
| `modernisierung-559-bgb` | Modernisierungsankündigung, Duldung, Härteeinwand und Modernisierungsmieterhöhung | §§ 555a–555f, 559–559c BGB |
| `heizungstausch-559e-559f` | Heizungstausch und Wärmepumpe: 10-%-Umlage, 0,50-EUR-Deckel, Jahresarbeitszahl-Nachweis | §§ 555b Nr. 1a, 559e, 559f BGB, GModG |
| `mietpreisbremse` | Zulässige Neuvertragsmiete, Auskunftspflicht, Rüge mit 30-Monats-Rückwirkung, Rückforderung, BGH 2025/2026 | §§ 556d–556g BGB |
| `indexmiete-staffelmiete` | Staffel- und Indexvereinbarung, Indexanpassung nachrechnen, Mietpreisbremse je Staffel, anhängige Indexkappung | §§ 557a, 557b BGB |
| `moeblierte-kurzzeitvermietung` | Ausnahmen § 549 Abs. 2 BGB, Möblierungszuschlag, Umgehung der Mietpreisbremse, Altrecht / Entwurf | §§ 549, 556d, 573c Abs. 3, 575 BGB |
| `mietwucher-mietpreisueberhoehung` | Mietpreisüberhöhung und Wucher, Teilnichtigkeit, Rückforderung bis zur Wesentlichkeitsgrenze | § 5 WiStG, § 291 StGB, §§ 134, 812 BGB |
| `betriebskostenabrechnung` | Abrechnungs- und Einwendungsfrist, formelle vs. materielle Fehler, Belegeinsicht, CO2-Stufenmodell | § 556 BGB, BetrKV, HeizkostenV, CO2KostAufG |
| `heizkosten-co2-fernablesung` | Heizkostenverteilung, Fernablese-Nachrüstung bis 31.12.2026, Kürzungsrechte, CO2-Aufteilung inkl. GModG ab 2028 | HeizkostenV, CO2KostAufG, BEHG |
| `mietmangel-minderung` | Mangel, Minderungsquote, Mängelanzeige, Selbstvornahme, Zurückbehaltung | §§ 536–536c BGB, § 320 BGB |
| `eigenbedarfskuendigung` | Wirksamkeit der Eigenbedarfskündigung, Sperrfrist nach Umwandlung, Schadensersatz bei Vortäuschung | §§ 573, 573c, 574, 577a BGB |
| `fristlose-kuendigung-543` | Wichtiger Grund, Zahlungsverzug, Schonfristzahlung, hilfsweise ordentliche Kündigung | §§ 543, 569, 568 BGB |
| `kuendigung-zahlungsverzug-ordentlich` | Ordentliche Kündigung wegen Rückstands, Verschulden, Schonfrist ohne Heilung (BGH 30.09.2026), § 242-Kontrolle, Entwurf § 573 Abs. 4 | §§ 573, 573c, 569, 574 BGB |
| `tod-des-mieters` | Eintritt, Fortsetzung, Sonderkündigung, Erbenhaftung | §§ 563–564, 573d, 580 BGB |
| `sozialklausel-widerspruch` | Härtegründe, Interessenabwägung, Form und Frist des Widerspruchs, Fortsetzungsverlangen | §§ 574–574c BGB |
| `raeumungsklage` | Räumungs- und Zahlungsantrag, künftige Räumung, Sicherungsanordnung, Vollstreckung | § 546 BGB, §§ 259, 283a, 721, 885a, 940a ZPO |
| `kaution-mietsicherheit` | Höchstbetrag, insolvenzfeste Anlage, Abrechnung nach Rückgabe, Verwertung | § 551 BGB, § 566a BGB, § 548 BGB |
| `schoenheitsreparaturen-rueckgabe` | AGB-Kontrolle der Renovierungsklauseln, unrenovierte Übergabe, Rückbau, Verjährung | §§ 535, 546, 548 BGB, §§ 307 ff. BGB |
| `untervermietung` | Erlaubnisvorbehalt, Gestattungsanspruch, Untermietzuschlag, Sanktionen | §§ 540, 553 BGB |
| `gewerberaummiete` | Textform seit BEG IV (§ 578 Abs. 1 S. 2 BGB), Indexmiete, Konkurrenzschutz, Betriebspflicht, § 313 BGB | §§ 550, 578, 557b, 580a BGB, Art. 229 § 70 EGBGB |

## Deterministische Rechner

| Skill | Rechner | Wofür |
|---|---|---|
| `mieterhoehung-558-bgb` | `frist` | 15-Monats-Frist, Jahressperre, Überlegungs- und Klagefrist |
| `betriebskostenabrechnung` | `frist` | 12-Monats-Abrechnungsfrist, 12-Monats-Einwendungsfrist |
| `schoenheitsreparaturen-rueckgabe` | `frist` | Sechsmonatige Verjährung § 548 BGB ab Rückerhalt |
| `fristlose-kuendigung-543` | `verzugszinsen`, `frist` | Zahlungsrückstand, Schonfristzahlung ab Rechtshängigkeit |
| `kuendigung-zahlungsverzug-ordentlich` | `verzugszinsen`, `frist` | Rückstand, Schonfrist |
| `indexmiete-staffelmiete` | `frist` | Jahresfrist zwischen Anpassungen, Kündigungsverzicht |
| `heizkosten-co2-fernablesung` | `frist` | Abrechnungs- und Einwendungsfrist |
| `tod-des-mieters` | `frist` | Monatsfristen ab Kenntnis, Ausschlagungsfrist |
| `mietwucher-mietpreisueberhoehung` | `verjaehrung`, `frist` | Verjährung der Rückforderung, Verfolgungsverjährung |
| `moeblierte-kurzzeitvermietung`, `heizungstausch-559e-559f` | `frist`, `feiertage` | Planungsrechnungen |

## Sub-Agenten

[`agents/researcher.md`](./agents/researcher.md) → [`agents/drafter.md`](./agents/drafter.md) → [`agents/reviewer.md`](./agents/reviewer.md).

Der Researcher führt die verifizierten BGH-Leitentscheidungen dieses Plugins mit Quell-URL (Stand Oktober 2026, einschließlich der Entscheidungen 2025/2026); unverifizierte Zitate tragen `[unverifiziert – prüfen]`. Der Marker `[generiert]` ist verboten und wird vom Validator zurückgewiesen. Zuständig sind der **VIII. Zivilsenat** (Wohnraum) und der **XII. Zivilsenat** (Gewerberaum) — das Az.-Präfix muss zum Rechtsgebiet passen.
