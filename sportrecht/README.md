# Sportrecht

**Production-grade Sportrechts-Skills für Claude / Gemini / GPT.** Deutsches Sportrecht aus Praxisperspektive: Verbands- und Vereinsrecht (BGB §§ 21 ff.), Verbandsgerichtsbarkeit und Schiedsgerichtsbarkeit (CAS Lausanne, DIS-Sportschiedsgericht), Anti-Doping (WADC, NADC, AntiDopG), Athletenverträge und Vermarktung, Stadionverbot, Schnittstellen zu Arbeitsrecht (Spielerarbeitsvertrag), Kartellrecht (Bosman-Linie) und Sportwettenrecht (GlüStV). Researcher → Drafter → Reviewer.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `dopingverfahren-verteidigung` | Verteidigung im sportrechtlichen Dopingverfahren (Anhörung NADA → Verbandsschiedsgericht → CAS) inkl. Selbstdoping-Strafrecht | WADC Art. 2.1, 10.6; NADC; AntiDopG §§ 2, 3, 4; Art. 12 GG |
| `vereinsrechtliche-sanktion` | Anfechtung von Vereinsausschluss, Verbandssperre, Stadionverbot; Pechstein-Linie zur Schiedsklausel | BGB §§ 25, 32, 39; § 858, § 1004 BGB; Art. 9 III GG; ZPO §§ 1025 ff. |
| `athletenvertrag` | Vertragsentwurf und AGB-Kontrolle: Spielerarbeitsvertrag, Förderungs- und Sponsoringvertrag, Vermarktungs- und Persönlichkeitsklauseln | BGB §§ 305 ff., 611a, 1004; KUG §§ 22, 23; TzBfG; § 1 GWB; Art. 101 AEUV |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: Statuten, WADC/NADC, BGH/EuGH/CAS-Rechtsprechung, Sportrechtskommentare
- [`agents/drafter.md`](./agents/drafter.md) – Entwurf in Gutachten- oder Urteilsstil; Schriftsätze für Verbands-, CAS- oder Zivilgericht
- [`agents/reviewer.md`](./agents/reviewer.md) – Risiko-, Frist- und Berufsrechts-Check (Pechstein-Anhörung, WADC-Berufungsfrist 21 Tage, § 32 BGB-Anfechtungsfrist)

## Installation

### Claude Code
```bash
# Über Marketplace (empfohlen)
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install sportrecht

# Oder als ZIP
# Claude Code → Customize Plugins → Install from .zip → sportrecht.zip
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area sportrecht --out dist/gemini
# Inhalt der erzeugten Dateien in neue Gemini-Gems einfügen
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area sportrecht --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Anhörung wegen positiver Dopingprobe

```
/sportrecht:dopingverfahren-verteidigung
Profi-Triathletin, A-Probe positiv auf eine verbotene Substanz der
WADA-Liste S1. NADA hat zur Anhörung geladen. Athletin trägt vor,
die Substanz sei aus einem kontaminierten Nahrungsergänzungs-
mittel gestammt. Bitte Stellungnahme zur Anhörung vorbereiten;
Verteidigungslinie nach WADC Art. 10.5/10.6 (No Significant Fault)
prüfen; Risiken § 4 IV AntiDopG (Selbstdoping) einschätzen;
Whereabouts-Pflichten und B-Probe-Antrag adressieren.
```

### Szenario 2 – Ausschluss eines Vereinsmitglieds

```
/sportrecht:vereinsrechtliche-sanktion
Mitglied eines Schützenvereins ist vom Vorstand ausgeschlossen
worden wegen "vereinsschädigenden Verhaltens" auf Facebook.
Anhörung fand nicht statt. Satzung sieht zweistufiges Verfahren
vor. Bitte Anfechtung des Ausschlusses vorbereiten (BGB §§ 25, 32,
39; rechtliches Gehör; Inhaltskontrolle der Satzungsnorm); Frist
zur Klageerhebung prüfen.
```

### Szenario 3 – Vermarktungsvertrag einer Spitzensportlerin

```
/sportrecht:athletenvertrag
Tennisspielerin (Weltranglistenposition 80–120) soll einen Drei-
Jahres-Vermarktungs- und Förderungsvertrag mit einem Ausrüster
abschließen. Klauseln: Exklusivität weltweit, Bildrechteübertragung
"umfassend", Bonusrückzahlung bei Doping-Sperre, Ausstiegsklauseln
nur einseitig zugunsten des Sponsors. Bitte AGB-Kontrolle §§ 305 ff.
BGB und KUG-§§ 22, 23-Konformität prüfen, Klauselbausteine
entwerfen.
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Standardliteratur: **Adolphsen**, Sportrecht; **Vieweg/Steinbach**, Sportrecht (in mehreren Bänden); **Pfister/Steiner**, Sportrecht-Kommentar; **Holla**, Sportrecht-Praxishandbuch; **Haas/Martens**, Sportrecht; **Summerer**, in: Fritzweiler/Pfister/Summerer, Praxishandbuch Sportrecht.

Rechtsprechung: BGH, BVerfG, EGMR, EuGH, OLG sowie CAS und DIS-Sportschiedsgericht. Format: `BGH, Urt. v. TT.MM.JJJJ – Az., NJW Jahr, Seite, Rn. N`; `EGMR, Urt. v. TT.MM.JJJJ – Beschwerde-Nr., Pechstein und Mutu`; `CAS, Award v. TT.MM.JJJJ – CAS YYYY/A/NNNN, Athlet ./. Verband`. Unverifizierte Zitate werden mit `[unverifiziert – prüfen]` markiert; CAS-Awards in cas.tas-cas.org, BGH in bundesgerichtshof.de und juris, EGMR in hudoc.echr.coe.int zu verifizieren.

## Hinweise

- **Doppelte Rechtsordnung.** Anti-Doping ist *sportrechtlich* (WADC, NADC, Verbandsstatut, CAS) **und** parallel *staatlich* (AntiDopG, StPO). Beide Stränge laufen unabhängig — `ne bis in idem` greift zwischen ihnen *nicht* nach hM `[unverifiziert]`.
- **Pechstein-Linie.** Schiedsklauseln in Athletenvereinbarungen werden vom BGH bei "strukturellem Ungleichgewicht" geprüft; EGMR (Mutu und Pechstein/Schweiz) `[unverifiziert – prüfen]` verlangt insbesondere öffentliche Verhandlung beim CAS in Disziplinarsachen.
- **Verbandsautonomie vs. Grundrechte.** Art. 9 GG schützt Verbände — aber Sanktionen müssen Art. 12 GG (Berufsfreiheit der Athleten), Art. 5 GG (Meinungsfreiheit) und das AGG respektieren. Inhaltskontrolle der Satzung nach §§ 138, 242 BGB.
- **Keine Präjudizienbindung** deutscher Gerichte außer § 31 BVerfGG; CAS-Awards binden im konkreten Verfahren, faktisch aber als Maßstab für nachfolgende Awards.
- **Mandatsgeheimnis (§ 43a BRAO, § 203 StGB):** Keine echten Mandatsdaten — insb. Gesundheits- und Trainingsdaten der Athletinnen — ohne § 203-konformen Gateway.
