# Vertragsrecht

**Skills für Vertragsgestaltung und -prüfung im deutschen Recht.**

Abgedeckt sind die allgemeine Rechtsgeschäftslehre (Anfechtung), das allgemeine
Leistungsstörungsrecht (Rücktritt, Schadensersatz, Verzug), das besondere
Schuldrecht (Kauf, Werkvertrag), das Verbrauchervertragsrecht (Widerruf), die
Vertragsgestaltung (AGB, Vertragsstrafe, Sicherheiten, Preisanpassung) sowie die
Querschnittsfragen Verjährung, Abtretung und Vergleich.

## Skills

| Skill | Funktion | Anker |
|---|---|---|
| `agb-kontrolle` | Inhaltskontrolle von AGB, Einbeziehung und Klauselverbote | §§ 305c, 307–310 BGB |
| `verzug-mahnung` | Verzugseintritt, Verzugszinsen, Verzugspauschale | §§ 280, 286, 288 BGB |
| `kaufrecht-maengelhaftung` | Sachmangel, Nacherfüllung, Rücktritt, Minderung, Beweislastumkehr | §§ 434, 437–441, 477 BGB |
| `werkvertrag-maengel` | Abnahme und fiktive Abnahme, Selbstvornahme, Kündigung, Verbraucherbauvertrag | §§ 634, 637, 640, 648, 650i ff. BGB |
| `ruecktritt-schadensersatz` | Nachfristsetzung, Entbehrlichkeit, Rückabwicklung, Nutzungsersatz | §§ 280, 281, 323, 325, 346 BGB |
| `verbraucherwiderruf` | Widerrufsrecht, Muster-Belehrung, Wertersatz, digitale Produkte | §§ 312g, 355–357a, 327 ff. BGB |
| `verjaehrung-pruefung` | Fristbestimmung, Hemmung, Neubeginn, Einredeverzicht — mit Rechner | §§ 195, 199, 203, 204, 212 BGB |
| `sicherheiten-gestaltung` | Bürgschaft, Eigentumsvorbehalt, Sicherungsübereignung, Globalzession | §§ 449, 765 ff., 929, 930 BGB |
| `vertragsstrafe` | Verwirkung, AGB-Grenzen, Herabsetzung, Hamburger Brauch | §§ 339–345 BGB, § 348 HGB |
| `stoerung-geschaeftsgrundlage` | Anpassungsverlangen, Force Majeure, Kostenelementeklausel | § 313 BGB |
| `abtretung-vertragsuebernahme` | Abtretung, Abtretungsverbot, Schuld- und Vertragsübernahme, Factoring | §§ 398, 399, 407, 414 f. BGB, § 354a HGB |
| `anfechtung-willenserklaerung` | Irrtum, arglistige Täuschung, Fristen, Vertrauensschaden | §§ 119–124, 142, 143 BGB |
| `vergleich-abfindung` | Abgeltungsklausel, Widerrufsvorbehalt, Prozessvergleich | § 779 BGB, § 794 Abs. 1 Nr. 1 ZPO |
| `vorvertragliche-phase` | c.i.c., NDA, LOI/Term Sheet, Exklusivität, Break-up Fee | §§ 241 Abs. 2, 280, 311 Abs. 2 BGB |

## Sub-Agenten

Die Skills nutzen die gemeinsame Researcher → Drafter → Reviewer-Kette:

- [`agents/researcher.md`](./agents/researcher.md) — Quellenrecherche und Klassifikation
- [`agents/drafter.md`](./agents/drafter.md) — Entwurf in Gutachten- oder Urteilsstil
- [`agents/reviewer.md`](./agents/reviewer.md) — Fristen-, Quellen- und Berufsrechts-Check

## Deterministische Berechnung

`verjaehrung-pruefung`, `ruecktritt-schadensersatz` und `verbraucherwiderruf`
sind an die Rechner in [`scripts/legal_calc/`](../scripts/legal_calc/) angebunden
(siehe [`references/rechner.md`](../references/rechner.md)). Die Rechner führen
die Arithmetik nach §§ 187–193, 195–199 BGB ohne Modellaufruf aus; die
rechtliche Wertung (Anspruchsart, Kenntniszeitpunkt, Fristbeginn) bleibt
vorgelagerte Eingabe.
