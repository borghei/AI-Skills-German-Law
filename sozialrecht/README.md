# Sozialrecht

**Production-grade Sozialrechts-Skills für Claude / Gemini / GPT.** Bürgergeld-Anspruchsprüfung, Rentenansprüche, Widerspruch gegen Leistungsbescheide. Researcher → Drafter → Reviewer-Pipeline.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `sgb-ii-leistungsanspruch` | Vollprüfung Bürgergeld-Anspruch (Erwerbsfähigkeit, Hilfebedürftigkeit, Bedarfsgemeinschaft, Regelbedarf, KdU, Mehrbedarfe, Sanktionen) | §§ 7 ff., 8, 9, 11 ff., 12, 19, 20, 21, 22, 31 ff. SGB II |
| `sgb-vi-rentenanspruch` | Prüfung Altersrente und Erwerbsminderungsrente, Wartezeit, Hinzuverdienst | §§ 33 ff., 35 ff., 43, 50, 51, 96a SGB VI |
| `widerspruch-leistungsbescheid` | Bescheidanalyse und Entwurf einer Widerspruchsschrift, Fristen, aufschiebende Wirkung, einstweiliger Rechtsschutz | §§ 78 ff., 84, 86a, 86b, 87 SGG; § 35 SGB X |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: SGB-Vorschriften, Kassler Kommentar, jurisPK-SGB, BSG-Rechtsprechung
- [`agents/drafter.md`](./agents/drafter.md) – Erstellung im Gutachten- oder Urteilsstil, Widerspruchs- und Klageentwürfe
- [`agents/reviewer.md`](./agents/reviewer.md) – Frist-, Mitwirkungs- und Berufsrechts-Check

## Installation

### Claude Code
```bash
# Über Marketplace (empfohlen)
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install sozialrecht

# Oder als ZIP
# Claude Code → Customize Plugins → Install from .zip → sozialrecht.zip
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area sozialrecht --out dist/gemini
# Inhalt der erzeugten Dateien in neue Gemini-Gems einfügen
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area sozialrecht --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Bürgergeld-Anspruchsprüfung bei Bedarfsgemeinschaft

```
/sozialrecht:sgb-ii-leistungsanspruch
Mandantin (38 J., erwerbsfähig) lebt mit Partner (45 J., monatliches
Netto-Einkommen 1.450 EUR) und zwei Kindern (10 und 14 J.) in
Mietwohnung. Kaltmiete 720 EUR, Nebenkosten 180 EUR, Heizung 110 EUR.
Vermögen: Tagesgeld 6.800 EUR, gemeinsames Auto Zeitwert 4.500 EUR.
Bitte Hilfebedürftigkeit § 9, Bedarfsgemeinschaft § 7 Abs. 3, KdU § 22
und Vermögensschonbetrag § 12 prüfen.
```

### Szenario 2 – Erwerbsminderungsrente nach 12 Jahren Beitragszahlung

```
/sozialrecht:sgb-vi-rentenanspruch
Mandant (52 J.), seit 8 Monaten arbeitsunfähig wegen chronischer
Wirbelsäulenerkrankung, Reha ohne Erfolg. Gutachten attestiert
3-Stunden-Leistungsvermögen auf dem allgemeinen Arbeitsmarkt.
12 Jahre Pflichtbeiträge, davon zuletzt 5 Jahre durchgehend. Bitte
Anspruch auf volle / teilweise EM-Rente §§ 43, 50, 51 prüfen,
Wartezeit und besondere versicherungsrechtliche Voraussetzungen.
```

### Szenario 3 – Widerspruch gegen Aufhebungs- und Erstattungsbescheid

```
/sozialrecht:widerspruch-leistungsbescheid
Mandant hat am 03.04.2026 vom Jobcenter einen Aufhebungs- und
Erstattungsbescheid über 3.840 EUR erhalten, gestützt auf nachträglich
festgestelltes anrechenbares Einkommen aus Minijob. Mandant trägt vor,
das Einkommen sei monatlich gemeldet worden. Bitte Bescheidanalyse
nach § 35 SGB X, Widerspruchsentwurf § 84 SGG, Antrag aufschiebende
Wirkung § 86b SGG erstellen.
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Standardkommentare: **Kassler Kommentar Sozialrecht**, **jurisPK-SGB** (I bis XII), **BeckOK Sozialrecht**, **Hauck/Noftz**, **LPK-SGB II**.

Rechtsprechung: BSG, LSG, BVerfG im Format `BSG, Urt. v. TT.MM.JJJJ – Az., SozR 4-… Nr. N / NZS JJJJ, Seite Rn. N`. Unverifizierte Zitate werden mit `[unverifiziert – prüfen]` markiert.

## Hinweise

- **Mitwirkungspflichten § 60 SGB I** sind zentral. Verletzung führt zur Versagung / Entziehung (§ 66 SGB I). Im Sachverhalt immer prüfen, ob Behörde zur Mitwirkung aufgefordert hat.
- **Fristen sind kurz.** Widerspruchsfrist § 84 SGG: 1 Monat ab Bekanntgabe (3 Monate bei fehlender / fehlerhafter Rechtsbehelfsbelehrung). Klagefrist § 87 SGG: 1 Monat ab Widerspruchsbescheid.
- **Aufschiebende Wirkung § 86a SGG** entfällt bei Aufhebung leistungsgewährender Bescheide. Antrag auf Anordnung § 86b Abs. 1 Nr. 2 SGG immer mitprüfen.
- **Beratungshilfe / PKH:** Mandanten häufig leistungsberechtigt. Auf §§ 73a SGG, 114 ZPO hinweisen.
- **Mandatsgeheimnis (§ 43a BRAO, § 203 StGB):** Keine echten Mandatsdaten ohne § 203-konformen Gateway. Siehe [`../references/gateway-setup.md`](../references/gateway-setup.md).
