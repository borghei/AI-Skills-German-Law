# Beamten- und Disziplinarrecht

**Production-grade Beamtenrechts-Skills für Claude / Gemini / GPT.** Disziplinarrecht, Konkurrentenstreit, dienstliche Beurteilung und Statusrecht aus der Perspektive der verwaltungsgerichtlichen Praxis. Researcher → Drafter → Reviewer.

> **Der Bund-Länder-Split ist das strukturelle Fehlerrisiko dieses Rechtsgebiets.** Für **Bundesbeamte** gelten **BBG** und **BDG**. Für **Landes- und Kommunalbeamte** gelten das **BeamtStG** (Rahmenrecht des Bundes), das jeweilige **Landesbeamtengesetz** und das jeweilige **Landesdisziplinargesetz**. Beide Ordnungen sind seit der Föderalismusreform I **materiell auseinandergelaufen** — insbesondere im Verfahrensrecht. Jede Skill dieses Plugins macht die Bestimmung des anwendbaren Rechts deshalb zu **Schritt 1** und bricht ab, wenn der Dienstherr nicht geklärt ist.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `disziplinarverfahren` | Behördliches Disziplinarverfahren von der Einleitung bis zur Abschlussentscheidung, Maßnahmenbemessung und Rechtsschutz | § 47 BeamtStG; § 77 BBG; §§ 5, 13, 14, 15, 17, 20, 24, 33, 34, 38, 41, 52 BDG; §§ 22, 23 BDG (Bindungswirkung); Landesdisziplinargesetze |
| `konkurrentenstreit` | Bestenauslese, Bewerbungsverfahrensanspruch, Konkurrentenmitteilung und einstweilige Anordnung vor der Ernennung | Art. 33 Abs. 2 GG; § 9 BBG; § 9 BeamtStG; § 123 VwGO; Art. 19 Abs. 4 GG; Grundsatz der Ämterstabilität |
| `dienstliche-beurteilung` | Angriff auf eine Regel- oder Anlassbeurteilung, Beurteilungsspielraum und Plausibilisierungspflicht | § 21 BBG; § 48 BLV; Beurteilungsrichtlinien; Art. 33 Abs. 2 GG; §§ 113 Abs. 5, 114 VwGO |
| `beamtenstatusrecht` | Ernennung, Umsetzung/Abordnung/Versetzung, Dienstunfähigkeit, Dienstunfall, Nebentätigkeit, Fürsorge, Remonstration | §§ 11, 12, 14, 15, 26, 33, 35, 36, 40, 45 BeamtStG; §§ 44, 60, 62, 63, 78 BBG; § 45 BeamtVG |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: BeamtStG, BBG, BDG, Landesdisziplinargesetze, BeamtVG, BLV, BVerwG 2. Senat, BVerfG 2. Senat, Standardkommentare
- [`agents/drafter.md`](./agents/drafter.md) – Entwürfe in Gutachten- oder Urteilsstil: Stellungnahme im Disziplinarverfahren, Antrag § 123 VwGO, Gegenvorstellung, Widerspruch, Klageschrift
- [`agents/reviewer.md`](./agents/reviewer.md) – Fristen-, Zuständigkeits-, Quellen- und Berufsrechts-Check (insbesondere § 15 BDG, Wartefrist im Konkurrentenstreit, § 74 VwGO)

## Installation

### Claude Code
```bash
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install beamten-disziplinarrecht
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area beamten-disziplinarrecht --out dist/gemini
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area beamten-disziplinarrecht --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Disziplinarverfahren gegen einen Bundesbeamten

```
/beamten-disziplinarrecht:disziplinarverfahren
Mandant ist Beamter auf Lebenszeit im Dienst einer Bundesoberbehörde.
Ihm wird vorgeworfen, im Zeitraum 2024 dienstliche Datenbanken ohne
dienstlichen Anlass abgefragt zu haben. Das Disziplinarverfahren wurde
am 15.01.2026 eingeleitet; parallel läuft ein Ermittlungsverfahren der
Staatsanwaltschaft. Frage: Aussetzung, Maßnahmeverbot wegen Zeitablaufs,
zu erwartende Maßnahme, Rechtsschutz.
```

### Szenario 2 – Konkurrentenstreit mit Eilantrag

```
/beamten-disziplinarrecht:konkurrentenstreit
Mandantin (Landesbeamtin, A 13) hat sich auf ein Beförderungsamt A 14
beworben und die Konkurrentenmitteilung erhalten. Die Auswahl stützt
sich auf Anlassbeurteilungen; der Auswahlvermerk ist zwei Sätze lang.
Frist bis zur Ernennung: zwei Wochen. Bitte Antrag nach § 123 VwGO.
```

### Szenario 3 – Angriff auf eine Regelbeurteilung

```
/beamten-disziplinarrecht:dienstliche-beurteilung
Mandant erhielt eine Regelbeurteilung mit einer gegenüber der Vorbeurteilung
um zwei Stufen abgesenkten Gesamtnote, ohne dass sich Aufgaben oder
Leistungen geändert hätten. Die Behörde beruft sich auf Richtwerte.
Bitte Gegenvorstellung und, falls erfolglos, Klage auf Neubeurteilung.
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Standardkommentare: **Plog/Wiedow** BBG/BeamtVG, **Battis** BBG, **von Roetteken/Rothländer** BeamtStG, **Reich** BeamtStG, **Gansen** Disziplinarrecht in Bund und Ländern, **Urban/Wittkowski** BDG, **Hummel/Köhler/Mayer/Baunack** Disziplinarrecht, **Schnellenbach/Bodanowitz** Beamtenrecht in der Praxis.

Rechtsprechung: **BVerwG 2. Senat** (Revisionsinstanz in Beamten- und Disziplinarsachen), **BVerfG 2. Senat**, OVG/VGH der Länder. Format: `BVerwG, Urt. v. TT.MM.JJJJ – 2 C NN.JJ, BVerwGE Band, Seite`. Unverifizierte Zitate werden mit `[unverifiziert - prüfen]` markiert.

## Hinweise

- **BDG-Fassung.** Das BDG gilt in der Fassung „zuletzt geändert durch Art. 6 G v. 19.7.2024 (BGBl. 2024 I Nr. 247)". Alle Disziplinarmaßnahmen des Bundes ergehen nach [§ 33 BDG](https://www.gesetze-im-internet.de/bdg/__33.html) durch **Disziplinarverfügung** — auch die Entfernung aus dem Beamtenverhältnis. Ältere Muster und Literatur, die für statusberührende Maßnahmen eine **Disziplinarklage** vorsehen, geben das Bundesrecht **nicht mehr** zutreffend wieder. In den Ländern besteht die Disziplinarklage überwiegend fort — das ist landesrechtlich zu prüfen.
- **§ 15 BDG** setzt harte Ausschlussfristen (2 Jahre Verweis, 3 Jahre Geldbuße/Kürzung, 7 Jahre Zurückstufung). Für Entfernung und Aberkennung des Ruhegehalts gilt **kein** Maßnahmeverbot wegen Zeitablaufs.
- **Konkurrentenstreit.** Nach vollzogener Ernennung greift der Grundsatz der Ämterstabilität; der unterlegene Bewerber ist praktisch auf den Eilrechtsschutz **vor** der Ernennung verwiesen. Die Wartefrist nach Konkurrentenmitteilung ist die kritischste Frist des Gebiets.
- **Mandantengeheimnis (§ 43a Abs. 2 BRAO, § 203 StGB):** Personalakten, Beurteilungen und Disziplinarvorgänge sind besonders sensibel; keine Verarbeitung ohne AVV und Pseudonymisierung (`scripts/pii_redact.py`).
