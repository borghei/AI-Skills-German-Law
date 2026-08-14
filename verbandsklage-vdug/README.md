# Verbandsklagerecht (VDuG)

**Production-grade Verbandsklage-Skills für Claude / Gemini / GPT.** Abhilfeklage, Musterfeststellungsklage, Anmeldung und Umsetzungsverfahren nach dem Verbraucherrechtedurchsetzungsgesetz. Researcher → Drafter → Reviewer.

> **Drei Wochen — ohne § 193 BGB.** Die Anmeldung zum Verbandsklageregister ist nach [§ 46 Abs. 1 VDuG](https://www.gesetze-im-internet.de/vdug/__46.html) nur **bis zum Ablauf von drei Wochen nach dem Schluss der mündlichen Verhandlung** möglich, und **[§ 193 BGB](https://www.gesetze-im-internet.de/bgb/__193.html) findet ausdrücklich keine Anwendung** — ein Fristende am Samstag, Sonntag oder Feiertag verschiebt sich **nicht** auf den nächsten Werktag. Dasselbe gilt für die Rücknahme der Anmeldung. Jede Skill dieses Plugins rechnet diese Frist ausdrücklich und weist den Ausschluss des § 193 BGB aus.

> **Erstinstanzlich entscheidet das Oberlandesgericht** ([§ 3 Abs. 1 VDuG](https://www.gesetze-im-internet.de/vdug/__3.html)) — ausschließlich, am allgemeinen Gerichtsstand des Unternehmers. Es gibt keine Berufung: statthaft ist die **Revision**, gegen Abhilfeendurteile sogar **ohne Zulassung** ([§ 18 Abs. 4](https://www.gesetze-im-internet.de/vdug/__18.html), [§ 42 VDuG](https://www.gesetze-im-internet.de/vdug/__42.html)).

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `verbandsklage-zulaessigkeit` | Klagearten, klageberechtigte Stellen, Quorum, Drittfinanzierungsverbot, Zuständigkeit, Sperrwirkung, Vergleich | §§ 1–13 VDuG; § 4 UKlaG; RL (EU) 2020/1828; KapMuG |
| `abhilfeklage-vdug` | Gleichartigkeit, Abhilfegrundurteil mit Berechtigungsnachweisen, Vergleichsfenster, Abhilfeendurteil, kollektiver Gesamtbetrag | §§ 14–21, 28 VDuG; §§ 287, 548 ZPO |
| `musterfeststellungsklage-vdug` | Feststellungsziele, die drei Wirkungen des § 11, Verhältnis zu KapMuG und UKlaG, Revision | §§ 1, 4, 8, 11, 41, 42 VDuG |
| `anmeldung-umsetzungsverfahren` | Anmeldung § 46, Register, Sachwalter, Umsetzungsfonds, Widerspruchsverfahren, Abschluss und Rückfluss | §§ 11, 22–40, 43–49 VDuG; § 193 BGB |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: VDuG, ZPO, UKlaG, KapMuG, RL (EU) 2020/1828, Verbandsklageregister des Bundesamts für Justiz
- [`agents/drafter.md`](./agents/drafter.md) – Entwürfe: Klageschrift, Zulässigkeits- und Individualisierungsrüge, Feststellungsziele, Urteilsformel, Anmeldung, Widerspruch
- [`agents/reviewer.md`](./agents/reviewer.md) – Zuständigkeits-, Zulässigkeits-, Fristen- und Quellencheck (insbesondere § 46 VDuG ohne § 193 BGB und die Bindungsausnahme des § 11 Abs. 3 S. 2)

## Installation

### Claude Code
```bash
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install verbandsklage-vdug
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area verbandsklage-vdug --out dist/gemini
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area verbandsklage-vdug --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Zulässigkeitsrüge gegen eine Abhilfeklage

```
/verbandsklage-vdug:verbandsklage-zulaessigkeit
Abhilfeklage gegen unsere Mandantin (Energieversorgerin, Sitz Köln) wegen
Preisanpassungsklauseln. Der klagende Verband bezieht 9 % seiner Mittel von
Branchenunternehmen; ein Prozessfinanzierer erhält 18 % des Erlöses, die
Vereinbarung wurde nicht vorgelegt. Eingereicht beim Landgericht Köln.
Bitte Zulässigkeitsrüge.
```

### Szenario 2 – Individualisierungsrüge und Urteilsformel

```
/verbandsklage-vdug:abhilfeklage-vdug
Abhilfeklage über 12 Mio. EUR kollektiven Gesamtbetrag wegen
Zustimmungsfiktionsklauseln, 210.000 Girokonten aus vier
Vertragsgenerationen. Klageschrift behauptet Gleichartigkeit pauschal und
nennt keine Berechnungsmethode. Bitte Rüge nach § 15 und Vorschlag für
praktikable Berechtigungsnachweise nach § 16 Abs. 2.
```

### Szenario 3 – Anmeldung für eine betroffene Verbraucherin

```
/verbandsklage-vdug:anmeldung-umsetzungsverfahren
Mandantin ist von einer Abhilfeklage gegen einen Stromversorger betroffen.
Schluss der mündlichen Verhandlung war der 14.03.2026; sie hat im Januar
bereits selbst geklagt und betreibt nebenbei einen Friseursalon mit drei
Angestellten. Bitte Fristberechnung, Anmeldungsentwurf und Bewertung, ob
die Anmeldung ihr nützt.
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Normen werden mit gesetze-im-internet.de zitiert, EU-Recht mit ELI-Fundstelle.

**Rechtsprechung:** Das VDuG ist am **13.10.2023** in Kraft getreten; eine gefestigte höchstrichterliche Rechtsprechung existiert **noch nicht**. Erste obergerichtliche Entscheidungen zu Zulässigkeit und Reichweite ergehen seit 2025/2026. Jede Entscheidung, die ein Modell nennt, ist als `[unverifiziert – prüfen]` zu behandeln, bis sie in juris, Beck-Online oder über das **Verbandsklageregister des Bundesamts für Justiz** belegt ist. Rechtsprechung zur alten Musterfeststellungsklage nach §§ 606 ff. ZPO a. F. ist **nicht** unbesehen übertragbar — die Bindungswirkung ist im VDuG neu geordnet.

## Hinweise

- **Kleine Unternehmen sind Verbraucher.** § 1 Abs. 2 VDuG stellt Unternehmen mit weniger als zehn Beschäftigten und höchstens 2 Mio. EUR Umsatz oder Bilanz den Verbrauchern gleich — das erweitert Quorum, Anmeldungskreis und Vergleichsmasse.
- **Die Finanzierungsrüge ist der schärfste Verteidigungsansatz.** § 4 Abs. 2 VDuG macht die Klage unzulässig, wenn dem Finanzierer mehr als **10 Prozent** der Leistung versprochen sind oder Einflussnahme auf Vergleichsentscheidungen zu erwarten ist; § 4 Abs. 3 verlangt Offenlegung auch bei nachträglicher Finanzierung.
- **Gegen Verbraucherzentralen läuft die 5-%-Rüge leer.** § 2 Abs. 3 VDuG stellt eine **unwiderlegliche** Vermutung auf.
- **Der kollektive Gesamtbetrag ist keine Haftungsobergrenze** — § 21 VDuG erlaubt die Erhöhung, und § 19 Abs. 2 eröffnet die Schätzung nach § 287 ZPO.
- **Die Bindungswirkung gilt nicht für Abhilfeendurteile** (§ 11 Abs. 3 S. 2 VDuG). Diese wirken über das Umsetzungsverfahren, nicht über eine Bindung im Folgeprozess.
- **§ 6 VDuG ist keine Discovery.** Die Offenlegung setzt konkret bezeichnete Beweismittel voraus; US-Discovery bleibt nach `CONVENTIONS.md` unzulässig.
- **Mandantengeheimnis (§ 43a Abs. 2 BRAO, § 203 StGB):** Anmeldedaten betreffen eine Vielzahl identifizierbarer Verbraucher; keine Verarbeitung ohne AVV und Pseudonymisierung (`scripts/pii_redact.py`).
