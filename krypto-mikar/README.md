# Kryptowerteaufsicht (MiCAR / KMAG)

**Production-grade Kryptoaufsichts-Skills für Claude / Gemini / GPT.** Einordnung, Whitepaper und Angebot, Zulassung und Übergangsrecht, Marktmissbrauch. Researcher → Drafter → Reviewer.

> **Die deutsche Übergangsfrist endete am 31.12.2025 — nicht am 01.07.2026.** Art. 143 Abs. 3 der [MiCAR](https://eur-lex.europa.eu/eli/reg/2023/1114/oj) lässt Bestandsanbieter grundsätzlich bis zum **1. Juli 2026** weiterarbeiten, erlaubt den Mitgliedstaaten aber ausdrücklich, diese Übergangsregelung **nicht in Anspruch zu nehmen oder zu verkürzen**. **Deutschland hat verkürzt:** Nach [§ 50 Abs. 2 Nr. 3 KMAG](https://www.gesetze-im-internet.de/kmag/__50.html) erlischt die als fortbestehend geltende Erlaubnis **spätestens mit Ablauf des 31. Dezember 2025**. Wer mit dem Unionsdatum rechnet, liegt für Deutschland **sechs Monate daneben** — und betreibt seither unerlaubte Geschäfte mit den Folgen der §§ 9, 10 KMAG.

> **Erst die Vorrangfrage, dann MiCAR.** Tokenisierte Aktien, Schuldverschreibungen und Fondsanteile sind **Finanzinstrumente** nach MiFID II und unterfallen WpHG, WpIG und KWG — nicht der MiCAR. Einlagen und E-Geld außerhalb der EMT-Definition folgen KWG und ZAG, Investmentvermögen dem KAGB. Erst wenn all das ausscheidet, greift die MiCAR — und auch dann nicht für die nach Art. 2 Abs. 3, 4 ausgenommenen Kryptowerte, die [§ 1 Abs. 2 KMAG](https://www.gesetze-im-internet.de/kmag/__1.html) ebenfalls ausnimmt.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `micar-anwendungsbereich-token` | Vorrangprüfung, Bereichsausnahmen, Tokenklassen ART/EMT/sonstige, BaFin-Befugnisse und unerlaubte Geschäfte | Art. 1, 2, 3, 16, 48 MiCAR; §§ 1, 3, 4, 5, 9, 10, 14 KMAG; MiFID II; KWG, WpIG, KAGB, ZAG |
| `krypto-whitepaper-angebot` | Öffentliches Angebot, Whitepaper-Pflichtinhalte, Marketing, Widerrufsrecht, Whitepaper-Haftung | Art. 4–9, 12, 13, 15, 16, 19, 36, 48, 51 MiCAR; §§ 15–19, 30 KMAG |
| `casp-zulassung-uebergang` | Zulassung und Anzeigeweg, **deutsches Übergangsrecht bis 31.12.2025**, vereinfachtes Verfahren, laufende Pflichten | Art. 59, 60, 62, 63, 68, 70, 75, 143 MiCAR; §§ 5, 9, 20, 26, 45–47, 50 KMAG |
| `krypto-marktmissbrauch` | Insiderinformation, Offenlegung und Aufschub, Insidergeschäfte, Marktmanipulation, Überwachungssysteme | Art. 86–92, 111 MiCAR; §§ 31–36, 46–48 KMAG; §§ 30, 130 OWiG |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: MiCAR, KMAG, MiFID II, KWG, WpIG, KAGB, ZAG, GwG, DORA, BaFin-, EBA- und ESMA-Verlautbarungen
- [`agents/drafter.md`](./agents/drafter.md) – Entwürfe: Tokeneinordnung, Whitepaper-Prüfung, Zulassungs- und Überleitungsstrategie, Marktmissbrauchsanalyse, BaFin-Stellungnahme
- [`agents/reviewer.md`](./agents/reviewer.md) – Regime-, Übergangs-, Haftungs- und Sanktionscheck (mit eigener Sonderprüfung zum Übergangsrecht)

## Installation

### Claude Code
```bash
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install krypto-mikar
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area krypto-mikar --out dist/gemini
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area krypto-mikar --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Drei Produkte, drei Regime

```
/krypto-mikar:micar-anwendungsbereich-token
Start-up plant: (1) Euro-Stablecoin mit Rücktauschrecht, ausgegeben durch
eine GmbH ohne Lizenz; (2) Token mit Gewinnanspruch an einem
Immobilienportfolio; (3) Serie von 10.000 bildgleichen Sammel-NFTs.
Die Geschäftsführung meint, alles falle unter die MiCAR und NFTs seien
ohnehin ausgenommen. Bitte Einordnung je Produkt.
```

### Szenario 2 – Bestandsgeschäft ohne Zulassung

```
/krypto-mikar:casp-zulassung-uebergang
Frankfurter GmbH betreibt seit 2021 eine Handelsplattform und verwahrt
Kundenbestände; am 29.12.2024 bestand eine Erlaubnis nach § 32 KWG. Kein
MiCAR-Antrag gestellt, weil man von der Frist 01.07.2026 ausging. Es ist
August 2026, Kundenbestände liegen auf Sammel-Wallets. Die BaFin kündigt
eine Untersagung an. Bitte Bewertung und Sofortmaßnahmen.
```

### Szenario 3 – Insiderfall vor der Übernahme

```
/krypto-mikar:krypto-marktmissbrauch
Term Sheet über eine Übernahme am 04.05.2026 unterzeichnet; zwei Tage
später storniert der Finanzvorstand eine Verkaufsorder über eigene Token
und kauft zu. Ein Mitarbeiter erwähnt die Verhandlungen gegenüber einem
Journalisten. Auf der Plattform stützen Orders zwischen verbundenen Konten
den Kurs; eine Handelsüberwachung fehlt. Bitte Bewertung und Meldelage.
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). EU-Rechtsakte werden mit ELI-Fundstelle zitiert, deutsche Normen mit gesetze-im-internet.de.

**Rechtsprechung:** Zu MiCAR und KMAG existiert **keine** gefestigte Judikatur. Die Skills arbeiten mit Normtext, Erwägungsgründen und Verlautbarungen von BaFin, EBA und ESMA. Als **Auslegungshilfe** — und stets als solche gekennzeichnet — kommen die Rechtsprechung zu §§ 32, 37 KWG (unerlaubte Geschäfte), zur Prospekthaftung (für Art. 15 MiCAR und § 19 KMAG) und zur MAR (für Titel VI) in Betracht. Jede Entscheidung ist als `[unverifiziert – prüfen]` zu behandeln, bis sie belegt ist.

## Hinweise

- **§ 5 KMAG ordnet die sofortige Vollziehbarkeit an.** Ein Rechtsbehelf gegen Maßnahmen der BaFin hat **keine aufschiebende Wirkung** — der Eilrechtsschutz ist von Anfang an einzuplanen.
- **§ 9 KMAG adressiert Personen, nicht nur Unternehmen.** Die Anordnung der sofortigen Einstellung und unverzüglichen Abwicklung kann sich auch gegen **Gesellschafter und Organmitglieder** richten.
- **Das Whitepaper wird nicht gebilligt.** Nach Art. 8 MiCAR erfolgt bei sonstigen Kryptowerten nur eine **Übermittlung** an die zuständige Behörde. Werbung mit einer behördlichen Prüfung verstößt zugleich gegen Art. 7 und kann nach § 17 KMAG untersagt werden.
- **Haftung immer doppelt prüfen:** Art. 15 MiCAR für **fehlerhafte** Whitepaper-Informationen und § 19 KMAG für das **fehlende** Whitepaper.
- **Euro-Stablecoins sind E-Geld-Token** und dürfen nach Art. 48 MiCAR nur von **Kreditinstituten oder E-Geld-Instituten** ausgegeben werden.
- **Kundenbestände gehören getrennt.** Art. 70 und Art. 75 MiCAR und vor allem **§ 45 KMAG** (Zuordnung verwahrter Kryptowerte, Kosten der Aussonderung) entscheiden über das Schicksal der Kundenwerte in der Insolvenz.
- **Marktmissbrauch: MiCAR Titel VI, nicht MAR** — es sei denn, der Kryptowert ist ein Finanzinstrument. Die MAR-Praxis ist Auslegungshilfe, kein Ersatz; Sanktionsrahmen kommen aus §§ 46, 47 KMAG, nicht aus dem WpHG.
- **Mandantengeheimnis (§ 43a Abs. 2 BRAO, § 203 StGB):** Wallet-, Transaktions- und Kundendaten sind besonders sensibel; keine Verarbeitung ohne AVV und Pseudonymisierung (`scripts/pii_redact.py`). Geldwäscherechtliche Pflichten nach GwG und Geldtransfer-Verordnung treten eigenständig hinzu.
