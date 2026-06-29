# Wohnungseigentumsrecht (WEG)

**Production-grade WEG-Skills für Claude / Gemini / GPT.** Tested workflows, primary-source citations, Researcher → Drafter → Reviewer sub-agents. Vollständig auf dem Stand der **WEMoG-Reform (in Kraft seit 01.12.2020)** – also nach der neuen Beklagtenrolle der Gemeinschaft der Wohnungseigentümer, der Beschlusskompetenz nur über die Abrechnungsspitze und der einfachen Mehrheit bei baulichen Veränderungen.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `beschlussanfechtung` | Erfolgsaussicht einer WEG-Beschlussanfechtung prüfen (Fristen, richtiger Beklagter, Nichtigkeit vs. Anfechtbarkeit) | §§ 23, 44, 45, 19 WEG; BGH V ZR 96/24 |
| `hausgeldabrechnung` | Plausibilität der Jahresabrechnung und Beschlusskompetenz prüfen (Abrechnungsspitze, Vermögensbericht) | § 28 WEG, §§ 16, 17 WEG; BGH V ZR 96/24 |
| `bauliche-veraenderung` | Bauliche Veränderung einordnen: Gestattungsbeschluss und privilegierter Anspruch | §§ 20, 21 WEG |

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
Die Jahresabrechnung weist eine Nachzahlung aus. Bitte prüfen, ob der
Beschluss korrekt nur die Abrechnungsspitze (§ 28 Abs. 2 WEG) erfasst und
ob der Vermögensbericht (§ 28 Abs. 4 WEG) vorliegt.
```

### Szenario 3 – Bauliche Veränderung (E-Mobilität)

```
/wohnungseigentumsrecht:bauliche-veraenderung
Ein Eigentümer möchte eine Wallbox in der Tiefgarage installieren. Bitte
den privilegierten Anspruch (§ 20 Abs. 2 WEG) und die Kostenverteilung
(§ 21 WEG) einordnen.
```

## Haftungsausschluss

Diese Skills sind ein geprüftes Entwurfswerkzeug, **keine Rechtsberatung**. Jede Ausgabe ist ein Entwurf zur Prüfung durch einen zugelassenen Rechtsanwalt. Rechtsprechungszitate sind als `[verifiziert]` oder `[unverifiziert – prüfen]` markiert; verifizieren Sie jede Fundstelle vor mandats- oder gerichtsbezogener Verwendung in juris, Beck-Online oder openjur.
