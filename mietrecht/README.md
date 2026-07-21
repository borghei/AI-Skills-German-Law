# Mietrecht

**Skills für die wohnraum- und gewerberaummietrechtliche Praxis.**

Alle Skills sind zweiseitig angelegt: Dieselbe Prüfkaskade trägt den Gestaltungsentwurf des Vermieters und die Abwehrprüfung des Mieters. Vier Skills binden die deterministischen Rechner in [`../scripts/legal_calc/`](../scripts/legal_calc/) ein (Fristen §§ 187–193 BGB, Verzugszinsen §§ 288, 247 BGB); die Arithmetik ist maschinell, Zugang und Fristbeginn bleiben juristische Eingaben.

## Skills

| Skill | Funktion | Anker |
|---|---|---|
| `mieterhoehung-558-bgb` | Mieterhöhung auf die ortsübliche Vergleichsmiete — Vermieter-Entwurf und Mieter-Prüfung in einem Ablauf | §§ 558, 558a–558e BGB |
| `modernisierung-559-bgb` | Modernisierungsankündigung, Duldung, Härteeinwand und Modernisierungsmieterhöhung | §§ 555a–555f, 559–559b BGB |
| `mietpreisbremse` | Zulässige Neuvertragsmiete, Auskunftspflicht, qualifizierte Rüge, Rückforderung | §§ 556d–556g BGB |
| `betriebskostenabrechnung` | Abrechnungs- und Einwendungsfrist, formelle vs. materielle Fehler, Belegeinsicht, CO2-Stufenmodell | § 556 BGB, BetrKV, HeizkostenV, CO2KostAufG |
| `mietmangel-minderung` | Mangel, Minderungsquote, Mängelanzeige, Selbstvornahme, Zurückbehaltung | §§ 536–536c BGB, § 320 BGB |
| `eigenbedarfskuendigung` | Wirksamkeit der Eigenbedarfskündigung und Schadensersatz bei Vortäuschung | §§ 573, 573c, 574 BGB |
| `fristlose-kuendigung-543` | Wichtiger Grund, Zahlungsverzug, Schonfristzahlung, hilfsweise ordentliche Kündigung | §§ 543, 569, 568 BGB |
| `sozialklausel-widerspruch` | Härtegründe, Interessenabwägung, Form und Frist des Widerspruchs, Fortsetzungsverlangen | §§ 574–574c BGB |
| `raeumungsklage` | Räumungs- und Zahlungsantrag, künftige Räumung, Sicherungsanordnung, Vollstreckung | § 546 BGB, §§ 259, 283a, 721, 885a, 940a ZPO |
| `kaution-mietsicherheit` | Höchstbetrag, insolvenzfeste Anlage, Abrechnung nach Rückgabe, Verwertung | § 551 BGB, § 566a BGB, § 548 BGB |
| `schoenheitsreparaturen-rueckgabe` | AGB-Kontrolle der Renovierungsklauseln, unrenovierte Übergabe, Rückbau, Verjährung | §§ 535, 546, 548 BGB, §§ 307 ff. BGB |
| `untervermietung` | Erlaubnisvorbehalt, Gestattungsanspruch, Untermietzuschlag, Sanktionen | §§ 540, 553 BGB |
| `gewerberaummiete` | Schriftform § 550 BGB, Indexmiete, Konkurrenzschutz, Betriebspflicht, § 313 BGB | §§ 550, 557b, 580a BGB, Art. 240 § 7 EGBGB |

## Deterministische Rechner

| Skill | Rechner | Wofür |
|---|---|---|
| `mieterhoehung-558-bgb` | `frist` | 15-Monats-Frist, Jahressperre, Überlegungs- und Klagefrist |
| `betriebskostenabrechnung` | `frist` | 12-Monats-Abrechnungsfrist, 12-Monats-Einwendungsfrist |
| `schoenheitsreparaturen-rueckgabe` | `frist` | Sechsmonatige Verjährung § 548 BGB ab Rückerhalt |
| `fristlose-kuendigung-543` | `verzugszinsen`, `frist` | Zahlungsrückstand, Schonfristzahlung ab Rechtshängigkeit |

## Sub-Agenten

[`agents/researcher.md`](./agents/researcher.md) → [`agents/drafter.md`](./agents/drafter.md) → [`agents/reviewer.md`](./agents/reviewer.md).

Der Researcher führt die verifizierten BGH-Leitentscheidungen dieses Plugins mit Quell-URL; unverifizierte Zitate tragen `[unverifiziert - prüfen]`. Der Marker `[generiert]` ist verboten und wird vom Validator zurückgewiesen. Zuständig sind der **VIII. Zivilsenat** (Wohnraum) und der **XII. Zivilsenat** (Gewerberaum) — das Az.-Präfix muss zum Rechtsgebiet passen.
