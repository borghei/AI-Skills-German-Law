# Steuerrecht

**Skills für die Fachanwaltschaft Steuerrecht — Schwerpunkt Verfahren mit dem Finanzamt.**

Rechtsstand aller Skills: **Oktober 2026**. Geltendes Recht und Entwurfsrecht sind in jedem Skill getrennt ausgewiesen. Der Regierungsentwurf des **Jahressteuergesetzes 2026** (BT-Drs. 21/8283; Anhörung im Finanzausschuss am 02.11.2026) ist nicht verabschiedet; die Skills markieren seine geplanten Änderungen (u. a. § 367 Abs. 2, 2c AO, § 122a AO ab 2027, § 152 Abs. 4 AO, § 238 Abs. 1a AO, elektronische Kontopfändung) ausdrücklich als „Entwurf".

## Skills

11 Skills. Die mit **∑** markierten Skills rechnen Fristen oder Gebühren deterministisch über [`scripts/legal_calc/`](../scripts/legal_calc/) — siehe [`references/rechner.md`](../references/rechner.md).

### Einspruch und Rechtsschutz

| Skill | Funktion | Anker |
|---|---|---|
| `einspruch-finanzamt` **∑** | Bekanntgabe per Post und Datenabruf (je vier Tage), Einspruchsfrist, Form, Ruhen, Präklusion, Verböserung | §§ 122, 122a, 347–367 AO |
| `aussetzung-der-vollziehung` | Ernstliche Zweifel, Begrenzung auf die Abschlusszahlung, Zugang zum FG, Aussetzungszinsen | § 361 AO, § 69 FGO, § 237 AO |
| `finanzgerichtsklage` **∑** | Klagearten, Sprung- und Untätigkeitsklage, Klagefrist, § 52d FGO, Präklusion, NZB/Revision, Kosten | §§ 40–47, 52d, 65, 68, 79b, 115 ff. FGO; § 52 GKG |
| `grundsteuer-einspruch` | Richtiger Bescheid (Wert / Messbetrag / Gemeinde), 40-%-Nachweis, Bundes- und Landesmodelle, Ruhen | §§ 182, 351 Abs. 2, 363 AO; Bewertungsgesetz §§ 219 ff. |

### Bescheid und Verfahren

| Skill | Funktion | Anker |
|---|---|---|
| `aenderung-bescheid-korrekturvorschriften` | Korrektur nach Bestandskraft, Festsetzungsfrist, grobes Verschulden, Mitberichtigung | §§ 129, 164, 165, 169–177 AO |
| `fristen-verspaetungszuschlag` | Abgabefristen VZ 2025/2026, Ende der Corona-Fristen, Fristverlängerung, Muss- und Ermessenszuschlag | §§ 108, 109, 149, 152 AO |

### Erhebung und Vollstreckung

| Skill | Funktion | Anker |
|---|---|---|
| `stundung-erlass-vollstreckungsschutz` | Stundung, Vollstreckungsaufschub, Erlass, Säumniszuschläge, Kontopfändung und P-Konto | §§ 222, 227, 234, 240, 249 ff., 258, 309 AO; § 850k ZPO |
| `haftungsbescheid` | Geschäftsführerhaftung, anteilige Tilgung, Lohnsteuer, Insolvenzlage, Ermessen, Subsidiarität | §§ 34, 69, 71, 75, 166, 191, 219 AO; § 42d EStG; § 15b InsO |

### Prüfung und Strafbefreiung

| Skill | Funktion | Anker |
|---|---|---|
| `aussenpruefung-betriebspruefung` | Reformiertes Außenprüfungsrecht seit 2025: § 200a-Mitwirkungsverlangen, Fünf-Jahres-Grenze, Datenzugriff, Schätzung, ApO | §§ 147, 162, 171 Abs. 4, 180 Abs. 1a, 193–203 AO |
| `selbstanzeige` | Vollständigkeitsgebot, Sperrgründe (Prüfungsumfang, Nachschau), Voranmeldungen, Nachzahlung, Zuschlag | §§ 371, 398a, 153, 235 AO |

### Materielle Schwerpunkte

| Skill | Funktion | Anker |
|---|---|---|
| `e-rechnung-vorsteuer` | E-Rechnungspflicht ab 2027/2028, Ausnahmen, Vorsteuerabzug und Berichtigung, Aufbewahrung, BMF 15.10.2026 | §§ 12, 14, 14b, 14c, 15, 27 Abs. 38 UStG |

## Zusammenspiel

```
Prüfungsanordnung ─► aussenpruefung-betriebspruefung ─► (Strafrisiko) selbstanzeige
        │
        ▼
Steuerbescheid ─► einspruch-finanzamt ─► aussetzung-der-vollziehung
        │                 │
        │                 ▼
        │          finanzgerichtsklage
        ▼
Frist abgelaufen ─► aenderung-bescheid-korrekturvorschriften
        │
        ▼
Zahlung ─► stundung-erlass-vollstreckungsschutz ─► (GmbH insolvent) haftungsbescheid
```

## Abgrenzung

- **Steuerstrafverteidigung** im eingeleiteten Verfahren (§§ 369 ff., 385 ff. AO): Gebiet [`wirtschafts-steuerstrafrecht`](../wirtschafts-steuerstrafrecht/). Die Selbstanzeige (§§ 371, 398a AO) bleibt hier.
- **Grundsteuer als Betriebskosten** im Mietverhältnis: [`mietrecht`](../mietrecht/) (`betriebskostenabrechnung`).

## Deterministische Fristberechnung

```bash
# Bekanntgabe (4 Tage, § 122 Abs. 2 / § 122a Abs. 4 AO) und Einspruchsfrist (1 Monat, § 355 AO)
python -m scripts.legal_calc.cli frist --ereignis 19.10.2026 --menge 4 --einheit tage --land NW
python -m scripts.legal_calc.cli frist --ereignis 23.10.2026 --menge 1 --einheit monate --land NW
# FG-Gerichtsgebühr 4,0 (KV GKG Nr. 6110)
python -m scripts.legal_calc.cli gkg --wert 20000 --faktor 4.0
```

Der Rechner macht nur die Arithmetik. Bekanntgabeweg, Bekanntgabetag und Bundesland bleiben juristische Eingaben.

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Statute sind mit gesetze-im-internet.de verlinkt; BFH-Entscheidungen ohne Fundstelle auf bundesfinanzhof.de oder dejure.org tragen `[unverifiziert – prüfen]`. Standardkommentare: **Tipke/Kruse**, **Klein**, **Gosch**, **Gräber**, **Hübschmann/Hepp/Spitaler**.

## Hinweise

- **Bekanntgabe zuerst.** Fast jede Frist im Steuerverfahren hängt am Bekanntgabetag. Den Bekanntgabeweg (Post / Datenabruf) immer erfragen.
- **Entwurfsrecht nicht als geltendes Recht ausgeben.** Ab Dezember 2026 prüfen, ob das JStG 2026 verabschiedet ist, und die Skills nachziehen.
- **Mandatsgeheimnis (§ 43a BRAO, § 203 StGB, § 57 StBerG):** Keine echten Mandatsdaten ohne § 203-konformen Gateway. Siehe [`../references/gateway-setup.md`](../references/gateway-setup.md).
