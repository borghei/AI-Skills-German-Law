# Vergaberecht

**Production-grade Vergaberechts-Skills für Claude / Gemini / GPT.** Tested workflows, primary-source citations, Researcher → Drafter → Reviewer sub-agents.

Abgedeckt sind der **Oberschwellenbereich** (GWB Teil 4, VgV, SektVO, KonzVgV, VSVgV) und der **Unterschwellenbereich** (UVgO, VOB/A). Bieter- und Auftraggeberseite. Nachprüfungsverfahren vor den Vergabekammern (§§ 155 ff. GWB) sowie sofortige Beschwerde zum OLG-Vergabesenat (§§ 171 ff. GWB).

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `vergabe-eu-schwellenwert-pruefung` | Geschätzter Auftragswert, EU-Schwellenwerte, Verfahrenswahl, Anwendungsbereich | § 3 VgV, §§ 99, 106 GWB; VO (EU) 2023/2497 `[unverifiziert – prüfen]` |
| `nachpruefungsverfahren-vergabekammer` | Antragsbefugnis, Rügeobliegenheit, Suspensiveffekt, Entwurf Nachprüfungsantrag | §§ 155 ff., 160, 168, 169, 182 GWB |
| `ausschreibungspruefung` | Prüfung der Vergabeunterlagen auf Vergaberechtskonformität (Eignung, Zuschlag, Lose, Diskriminierungsverbot) | §§ 97, 122–124, 127 GWB; §§ 29, 31 VgV |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: Statute, Standardkommentare, EuGH/BGH/OLG-Vergabesenate, VK-Entscheidungen
- [`agents/drafter.md`](./agents/drafter.md) – Erstellung im Gutachten- oder Urteilsstil (Memo, Rügeschreiben, Nachprüfungsantrag, Schriftsatz)
- [`agents/reviewer.md`](./agents/reviewer.md) – Frist-, Risiko- und Berufsrechts-Check; Frist-Kalender (10-Tage-Rüge § 160 Abs. 3 GWB, 15-Kalendertage-Beschwerde § 172 GWB)

## Installation

### Claude Code
```bash
# Über Marketplace (empfohlen)
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install vergaberecht

# Oder als ZIP
# Claude Code → Customize Plugins → Install from .zip → vergaberecht.zip
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area vergaberecht --out dist/gemini
# Inhalt der erzeugten Dateien in neue Gemini-Gems einfügen
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area vergaberecht --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Schwellenwert- und Verfahrensprüfung (Auftraggeber)

```
/vergaberecht:vergabe-eu-schwellenwert-pruefung
Kommunaler Auftraggeber plant Beschaffung einer Fachsoftware
(Lizenz + Wartung 4 Jahre, geschätzter Gesamtwert 280.000 EUR netto).
Bitte Auftragswert nach § 3 VgV ermitteln, Schwellenwertprüfung
nach aktueller VO (EU) und Verfahrensart empfehlen.
```

### Szenario 2 – Nachprüfungsverfahren (Bieterseite)

```
/vergaberecht:nachpruefungsverfahren-vergabekammer
Mandantin (unterlegener Bieter) hat am TT.MM.JJJJ § 134-Information
erhalten. Vermuteter Ausschluss wegen vermeintlich fehlender
Referenzen. Bitte Rügeobliegenheit § 160 Abs. 3 GWB prüfen,
Antragsbefugnis subsumieren, Nachprüfungsantrag an die zuständige
Vergabekammer entwerfen.
```

### Szenario 3 – Prüfung der Vergabeunterlagen (Bieterseite)

```
/vergaberecht:ausschreibungspruefung
Mandantin möchte sich auf eine EU-weite Ausschreibung für
IT-Dienstleistungen bewerben. Bitte Eignungsanforderungen
§§ 122–124 GWB, Zuschlagskriterien und deren Gewichtung
§ 127 GWB und Losaufteilung § 97 Abs. 4 GWB prüfen — drohen
Rügepunkte?
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Standardkommentare: **Burgi**, Vergaberecht (4. Aufl. 2022); **Ziekow/Völlink**, Vergaberecht (5. Aufl. 2024); **Beck'scher Vergaberechtskommentar** (hrsg. v. Müller-Wrede); **Pünder/Schellenberg**, Vergaberecht.

Rechtsprechung: EuGH, BGH (X. Zivilsenat), OLG-Vergabesenate (Düsseldorf, München, Karlsruhe, Frankfurt, Celle, Schleswig u. a.), VK Bund und VK der Länder. Format: `OLG …, Beschl. v. TT.MM.JJJJ – Verg X/JJ, NZBau JJJJ, Seite Rn. N`. Unverifizierte Zitate werden mit `[unverifiziert – prüfen]` markiert.

## Hinweise

- **Schwellenwerte werden alle zwei Jahre durch delegierte Verordnung der Kommission angepasst.** Stand der aktuellen VO (EU) bei jeder Anwendung des Skills prüfen `[unverifiziert]`.
- **Fristen sind im Vergaberecht harte Ausschlussfristen.** 10-Tage-Rügefrist (§ 160 Abs. 3 S. 1 Nr. 1 GWB) und 15-Kalendertage-Beschwerdefrist (§ 172 GWB) werden vom Reviewer-Agenten geprüft.
- **Suspensiveffekt § 169 GWB:** Der Zuschlag darf nach Eingang eines zulässigen Nachprüfungsantrags nicht erteilt werden. Praktisch kritischer Hebel der Bieterseite.
- **Mandatsgeheimnis (§ 43a BRAO, § 203 StGB):** Keine echten Mandatsdaten ohne § 203-konformen Gateway. Siehe [`../references/gateway-setup.md`](../references/gateway-setup.md).
