# Handelsrecht

**Production-grade Handelsrechts-Skills für Claude / Gemini / GPT.** Deutsches HGB aus Praxisperspektive: Kaufmannseigenschaft und Handelsregister, Handelsvertretervertrag inkl. Ausgleichsanspruch § 89b HGB, Besonderheiten des Handelsgeschäfts (insb. §§ 377/378 HGB). Researcher → Drafter → Reviewer.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `handelsregister-eintragungspflicht` | Prüfung Kaufmannseigenschaft, Eintragungspflicht und Publizität | §§ 1–6, 8, 15, 17 HGB |
| `handelsvertretervertrag` | Entwurf Handelsvertretervertrag inkl. Provision und Ausgleichsanspruch | §§ 84–90a HGB; RL 86/653/EWG |
| `hgb-handelsgeschaeft-besonderheiten` | Praxischeck: was ändert die Kaufmannseigenschaft am BGB-Schuldrecht? | §§ 343–378 HGB |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: HGB-Statute, BGH-Rechtsprechung, Standardkommentare (Baumbach/Hopt, MüKoHGB, Staub, EBJS)
- [`agents/drafter.md`](./agents/drafter.md) – Erstellung im Gutachten- oder Urteilsstil, Vertragsentwürfe, § 89b-Berechnung
- [`agents/reviewer.md`](./agents/reviewer.md) – Risiko-, Frist- und Berufsrechts-Check (insb. § 377 HGB Rügefrist, § 89b-Ausschlussfrist)

## Installation

### Claude Code
```bash
# Über Marketplace (empfohlen)
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install handelsrecht

# Oder als ZIP
# Claude Code → Customize Plugins → Install from .zip → handelsrecht.zip
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area handelsrecht --out dist/gemini
# Inhalt der erzeugten Dateien in neue Gemini-Gems einfügen
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area handelsrecht --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Kaufmannseigenschaft einer wachsenden GbR

```
/handelsrecht:handelsregister-eintragungspflicht
Mandant betreibt seit drei Jahren mit einem Partner einen Online-Shop
als GbR. Umsatz im laufenden Jahr ca. 2,4 Mio. EUR, 6 Beschäftigte,
Lagerlogistik extern. Bitte Kaufmannseigenschaft nach §§ 1, 2 HGB
prüfen, Folgepflichten (Eintragung, Firma, Buchführung) und § 15 HGB
Publizitätsschutz erläutern.
```

### Szenario 2 – Handelsvertretervertrag mit Ausgleichsanspruch

```
/handelsrecht:handelsvertretervertrag
Mandant (Hersteller von Industriearmaturen) will mit selbständigem
Handelsvertreter einen Vertrag für DE/AT abschließen. Provision 5 %
auf Bestands- und Neukunden, Bezirksvertretung. Bitte Vertrag entwerfen
und § 89b HGB Ausgleichsanspruch durchrechnen (Höchstgrenze, Billig-
keit, Ausschlussgründe).
```

### Szenario 3 – Mangelhafte Lieferung B2B – greift § 377 HGB?

```
/handelsrecht:hgb-handelsgeschaeft-besonderheiten
Mandantin (Maschinenbauerin) hat von Zulieferer eine Charge Lager
geliefert bekommen. Mängel sind erst nach 4 Wochen aufgefallen.
Zulieferer beruft sich auf § 377 HGB. Bitte prüfen: beidseitiges
Handelsgeschäft? Untersuchungs-/Rügepflicht eingehalten? Folgen für
Gewährleistungsansprüche.
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Standardkommentare: **Baumbach/Hopt** HGB, **MüKoHGB**, **Staub** HGB-Großkommentar, **Ebenroth/Boujong/Joost/Strohn (EBJS)** HGB, **Oetker** HGB.

Rechtsprechung: BGH, OLG, EuGH (zur Handelsvertreter-RL 86/653/EWG) im Format `BGH, Urt. v. TT.MM.JJJJ – Az., NJW JJJJ, Seite Rn. N`. Unverifizierte Zitate werden mit `[unverifiziert – prüfen in juris]` markiert.

## Hinweise

- **Abgrenzung Gesellschaftsrecht.** OHG/KG-Grundzüge (Zweites Buch HGB) gehören zu diesem Plugin, tiefer GmbH-/AG-Stoff zum bestehenden `gesellschaftsrecht`-Plugin.
- **Schnittstellen.** Frachtgeschäft (§§ 407 ff. HGB) wird hier nur skizziert; vertiefte Transport-Themen folgen einem eigenen Plugin. Bilanzrecht (Drittes Buch HGB) wird übersichtsartig behandelt; tiefe Bilanzierungs- und Konzernfragen sind nicht abgedeckt.
- **EU-Bezug Handelsvertreter.** Die §§ 84 ff. HGB setzen die RL 86/653/EWG um; nationale Auslegungsfragen sind ggf. richtlinienkonform auszulegen (Schnittstelle `europarecht`).
- **§ 377 HGB ist eine Falle.** Die Rügepflicht greift nur beim beidseitigen Handelskauf (§ 1 HGB beidseits) und nur "unverzüglich" (§ 121 BGB). Versäumung führt zum Verlust der Gewährleistungsrechte.
- **Mandatsgeheimnis (§ 43a BRAO, § 203 StGB):** Keine echten Mandatsdaten ohne § 203-konformen Gateway.
