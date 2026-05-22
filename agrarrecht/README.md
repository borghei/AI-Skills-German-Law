# Agrarrecht

**Production-grade Agrarrechts-Skills für Claude / Gemini / GPT.** Deutsches Agrarrecht aus anwaltlicher Praxisperspektive: EU-Gemeinsame Agrarpolitik (GAP 2023–2027), nationale Förderdurchführung, Grundstücksverkehr und Landpacht, LwAnpG-Vermögensauseinandersetzung. Researcher → Drafter → Reviewer.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `gap-foerderantrag` | Direktzahlungen, Öko-Regelungen, Konditionalität, Sammelantrag InVeKoS, Widerspruch | VO (EU) 2021/2115, 2021/2116; GAP-DZG; GAPInVeKoSG; GAP-KondV; GAP-IntegrV |
| `lwanpg-pruefung` | Vermögensauseinandersetzung ehemaliger LPG und Nachfolgegesellschaften vor dem Landwirtschaftsgericht | §§ 44 ff., 51a LwAnpG; FamFG; § 65 LwVG |
| `agrar-grundstuecksverkehrsrecht` | Genehmigungspflicht Verkauf landwirtschaftlicher Flächen, Siedlungs-Vorkaufsrecht, Landpacht-Anzeige | §§ 2, 9 GrdstVG; § 4 RSG; § 2 LPachtVG; §§ 581 ff. BGB |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: EU-GAP-Verordnungen, nationales Agrar-Förderrecht, BGH-Landwirtschaftssenat
- [`agents/drafter.md`](./agents/drafter.md) – Erstellung im Gutachten- oder Urteilsstil; Antragsbegleitung, Widerspruchsbegründung, Antragsschrift LwG
- [`agents/reviewer.md`](./agents/reviewer.md) – Frist- und Berufsrechts-Check (GAP-Sammelantrag, GrdstVG-Genehmigung, LPachtVG-Anzeige, LwAnpG-Verjährung)

## Installation

### Claude Code
```bash
# Über Marketplace (empfohlen)
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install agrarrecht

# Oder als ZIP
# Claude Code → Customize Plugins → Install from .zip → agrarrecht.zip
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area agrarrecht --out dist/gemini
# Inhalt der erzeugten Dateien in neue Gemini-Gems einfügen
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area agrarrecht --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Ablehnung des Sammelantrags wegen GLÖZ-Verstoßes

```
/agrarrecht:gap-foerderantrag
Mandant (Ackerbaubetrieb 180 ha, Brandenburg) hat den Sammelantrag
2025 fristgerecht über das InVeKoS-Portal gestellt. Die Landesbehörde
hat die Basisprämie um 5 % gekürzt wegen behaupteten Verstoßes gegen
GLÖZ 8 (Mindestanteil nichtproduktive Flächen). Bitte Widerspruchs-
begründung entwerfen und Sanktionsbemessung prüfen.
```

### Szenario 2 – LwAnpG-Auseinandersetzungsanspruch 30 Jahre nach Wende

```
/agrarrecht:lwanpg-pruefung
Mandant (Erbe eines verstorbenen LPG-Mitglieds, Sachsen) macht
gegen die Nachfolgegesellschaft (eingetragene Genossenschaft i.L.)
einen Auseinandersetzungsanspruch nach § 44 LwAnpG geltend.
Erblasser ist 1998 ausgeschieden, kein Bescheid. Bitte prüfen:
Anspruchsgrundlage, Verjährung § 51a LwAnpG, Zuständigkeit
Landwirtschaftsgericht. Antragsschrift entwerfen.
```

### Szenario 3 – Versagung GrdstVG-Genehmigung wegen Nichtlandwirt-Erwerb

```
/agrarrecht:agrar-grundstuecksverkehrsrecht
Mandant (Investor, kein Landwirt) hat Kaufvertrag über 22 ha
Ackerland in Niedersachsen geschlossen. Die Genehmigungsbehörde
hat nach § 9 Abs. 1 Nr. 1 GrdstVG versagt; ein örtlicher Landwirt
hat über die Siedlungsbehörde das Vorkaufsrecht nach § 4 RSG
ausgeübt. Bitte Beschwerde nach § 22 GrdstVG/§ 9 LwVG prüfen
und Frist sichern.
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Standardkommentare: **Düsing/Martinez**, Agrarrecht (Loseblatt; früher Faßbender/Köck/Schmidt-Räntsch); **Netz**, Landpachtrecht; **Lange**, GrdstVG; **Wöhrmann**, Landwirtschaftsrecht; **Schweizer**, LwAnpG-Kommentar.

Rechtsprechung: BGH-Landwirtschaftssenat (BLw-Senat), BVerwG, EuGH zu EU-Agrarrecht im Format `BGH, Beschl. v. TT.MM.JJJJ – BLw N/JJ, AUR Jahr, Seite Rn. N`. Unverifizierte Zitate werden mit `[unverifiziert – prüfen]` markiert.

## Hinweise

- **Jährlicher Frist-Reset.** GAP-Sammelantrag, Schwellenwerte, EUR-Beträge je Hektar und Öko-Regelungen werden jährlich rechtsfortbildend angepasst — jeder konkrete Betrag im Output ist mit `[unverifiziert – aktueller Stand prüfen]` zu versehen.
- **GrdstVG-Genehmigung als Wirksamkeitserfordernis.** Ohne Genehmigung ist die Eigentumsübertragung schwebend unwirksam (§ 2 Abs. 1 GrdstVG); Reviewer-Blocker.
- **Landwirtschaftsgericht statt Zivilgericht.** Für LwAnpG- und GrdstVG-Streitigkeiten ist das Landwirtschaftsgericht beim AG (FamFG/LwVG) zuständig, nicht die ordentliche Zivilkammer.
- **Querverweise.** Düngeverordnung, BBodSchG → siehe `umweltrecht`-Plugin. TierschG-Tiefe → außerhalb dieses Plugins.
- **Mandatsgeheimnis (§ 43a BRAO, § 203 StGB):** Betriebs-, Flurstücks- und Förderdaten nur in Tools mit AVV verarbeiten.
