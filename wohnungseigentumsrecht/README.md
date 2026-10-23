# Wohnungseigentumsrecht (WEG)

**Production-grade WEG-Skills für Claude / Gemini / GPT.** Tested workflows, primary-source citations, Researcher → Drafter → Reviewer sub-agents. Vollständig auf dem Stand der **WEMoG-Reform (in Kraft seit 01.12.2020)** und der Änderungen vom **17.10.2024** (Steckersolargeräte, virtuelle Eigentümerversammlung). **Rechtsstand: Oktober 2026** — einschließlich der Rechtsprechung des V. Zivilsenats 2024–2026.

> **Stand des Gesetzgebungsverfahrens:** Das WEG wurde zuletzt durch G v. 10.10.2024 (BGBl. 2024 I Nr. 306) geändert. Ein Reformentwurf liegt nicht vor; das BMJV bereitet die Evaluation 2027 vor (Eigentümerbefragung bis 12.11.2026). Das Gebäudemodernisierungsgesetz (GModG, seit 29.07.2026) hat die Sonderregeln für Gemeinschaften mit Etagenheizungen (§§ 71l und 71n der früheren GEG-Fassung) gestrichen und ändert das WEG nicht.

## Skills

9 Skills. Die mit **∑** markierten Skills rechnen Fristen, Zinsen oder Verjährung deterministisch über [`scripts/legal_calc/`](../scripts/legal_calc/).

### Beschlüsse und Rechtsschutz

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `beschlussanfechtung` **∑** | Erfolgsaussicht einer Anfechtung: Klageart, Fristen, Zustellung, Nichtigkeit vs. Anfechtbarkeit, Kostenrisiko | §§ 23, 44, 45 WEG; § 49 GKG; BGH V ZR 17/24, V ZR 139/23 |
| `beschlussersetzungsklage` **∑** | Anspruch auf ordnungsmäßige Verwaltung gerichtlich durchsetzen, Vorbefassung, Negativbeschluss | §§ 18, 19, 44 Abs. 1 S. 2 WEG; BGH V ZR 86/24 |
| `eigentuemerversammlung-beschlussfassung` **∑** | Einberufung, hybride und virtuelle Versammlung, Umlaufbeschluss, Stimmrecht, Niederschrift | §§ 23–25, 29, 48 Abs. 6 WEG |

### Verwaltung und Finanzen

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `verwalter-bestellung-abberufung` | Bestellung, jederzeitige Abberufung, zertifizierter Verwalter, Haftung | §§ 9b, 19 Abs. 2 Nr. 6, 26, 26a, 27 WEG |
| `hausgeldabrechnung` **∑** | Wirtschaftsplan, Abrechnungsspitze, Anfechtungsrelevanz von Fehlern, Vermögensbericht | §§ 16, 28 WEG; BGH V ZR 102/23, V ZR 195/23, V ZR 96/24 |
| `kostenverteilung-16-weg` **∑** | Änderung des Verteilerschlüssels: Kompetenz, Ermessen, Objektprinzip, Folgebeschlüsse | § 16 Abs. 2 S. 2 WEG; BGH V ZR 81/23, V ZR 50/25 |
| `hausgeld-beitreibung-entziehung` **∑** | Zahlungsklage, Verjährung, Vorrang in der Zwangsversteigerung, Entziehung | §§ 17, 28 WEG; § 10 Abs. 1 Nr. 2 ZVG; §§ 195, 288 BGB |

### Bauliches und Vermietung

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `bauliche-veraenderung` | Beschlusszwang, privilegierte Maßnahmen (inkl. Steckersolar), Gestattungsanspruch, Kosten | §§ 15, 20, 21 WEG; BGH V ZR 29/24, V ZR 1/24 |
| `vermietete-eigentumswohnung` | Schnittstelle WEG / Mietrecht: Betriebskosten, Duldung, Mieter-Umbauten, Mängel, Umwandlung | § 15 WEG; §§ 554, 556a Abs. 3, 577a BGB |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: Statute, Kommentare, BGH-Rechtsprechung
- [`agents/drafter.md`](./agents/drafter.md) – Erstellung im Gutachten- oder Urteilsstil
- [`agents/reviewer.md`](./agents/reviewer.md) – Risiko-, Frist- und Berufsrechts-Check

## Installation

### Claude Code
```bash
# Über Marketplace (empfohlen)
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install wohnungseigentumsrecht
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area wohnungseigentumsrecht --out dist/gemini
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area wohnungseigentumsrecht --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Beschlussanfechtung mit Fristprüfung

```
/wohnungseigentumsrecht:beschlussanfechtung
Eigentümerin hält den auf der Versammlung vom 12.03. gefassten Beschluss
über die Sonderumlage für rechtswidrig. Bitte Anfechtungsfrist (§ 45 WEG),
richtigen Beklagten (§ 44 Abs. 2 WEG) und ordnungsmäßige Verwaltung
(§ 19 WEG) prüfen.
```

### Szenario 2 – Jahresabrechnung und Abrechnungsspitze

```
/wohnungseigentumsrecht:hausgeldabrechnung
Die Versammlung hat "die Jahresabrechnung 2025 genehmigt"; meine
Nachzahlung enthält eine doppelt gebuchte Versicherung. Bitte prüfen,
wie der Beschluss auszulegen ist (BGH V ZR 102/23), ob der Fehler die
Abrechnungsspitze berührt und ob eine Teilanfechtung genügt.
```

### Szenario 3 – Bauliche Veränderung (E-Mobilität)

```
/wohnungseigentumsrecht:bauliche-veraenderung
Ein Eigentümer möchte eine Wallbox in der Tiefgarage installieren. Bitte
den privilegierten Anspruch (§ 20 Abs. 2 WEG) und die Kostenverteilung
(§ 21 WEG) einordnen.
```

### Szenario 4 – Verwalter loswerden

```
/wohnungseigentumsrecht:verwalter-bestellung-abberufung
14 Einheiten, externer Verwalter ohne IHK-Zertifikat, Vertrag bis 2027,
Jahresabrechnung 2025 fehlt. Bitte Abberufung, Vertragsende und den
Anspruch auf einen zertifizierten Verwalter prüfen.
```

### Szenario 5 – Hausgeldrückstand vor Jahresende

```
/wohnungseigentumsrecht:hausgeld-beitreibung-entziehung
Eigentümer zahlt seit Februar 2026 nicht, aus 2023 ist eine Nachzahlung
offen. Bitte Verjährung zum 31.12.2026, Zinsen und den Vorrang nach
§ 10 Abs. 1 Nr. 2 ZVG berechnen.
```

## Haftungsausschluss

Diese Skills sind ein geprüftes Entwurfswerkzeug, **keine Rechtsberatung**. Jede Ausgabe ist ein Entwurf zur Prüfung durch einen zugelassenen Rechtsanwalt. Rechtsprechungszitate tragen entweder eine Quell-URL (verifiziert) oder den Marker `[unverifiziert – prüfen]`; verifizieren Sie jede Fundstelle vor mandats- oder gerichtsbezogener Verwendung in juris, Beck-Online oder openjur.
