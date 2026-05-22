# Geldwäsche / AML / KYC

**Production-grade Geldwäschepräventions-Skills für Claude / Gemini / GPT.** Pflichten der Verpflichteten nach GwG (4. EU-GW-RL umgesetzt; 6. AMLD-Strafrecht; künftig EU-AMLR / AMLA), Schnittstelle § 261 StGB, KWG-Sondervorschriften (§§ 25h–25j) und MaRisk AT 4.4.3 / BT 5. Researcher → Drafter → Reviewer.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `gwg-risikoanalyse` | Aufbau und Aktualisierung der institutsspezifischen Risikoanalyse | § 5 GwG, § 4 GwG, § 6 GwG, supranationale + nationale Risk Assessments |
| `kyc-identifikationspflicht` | Identifizierung von Kunde und wirtschaftlich Berechtigtem, Transparenzregisterabgleich | §§ 10–17 GwG, §§ 3 ff. GwG, §§ 18–26 GwG |
| `verdachtsmeldung-fiu` | Entwurf und Versand einer Meldung an die FIU über goAML | § 43 GwG, § 46 GwG, § 47 GwG, § 48 GwG, § 261 StGB |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: GwG, KWG, ZAG, StGB, BaFin / FIU-Auslegungshinweise, EU-Recht
- [`agents/drafter.md`](./agents/drafter.md) – Erstellung in Gutachten- / Urteilsstil bzw. Meldetext für goAML
- [`agents/reviewer.md`](./agents/reviewer.md) – Pflicht-Blocker: § 47 Tippoff-Verbot, § 46 Stillhaltepflicht (3 Werktage), § 43 Unverzüglichkeit, Berufsrecht (BRAO § 43e, BNotO § 14a)

## Installation

### Claude Code
```bash
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install geldwaesche-aml-kyc
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area geldwaesche-aml-kyc --out dist/gemini
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area geldwaesche-aml-kyc --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Risikoanalyse einer Vermögensverwaltung
```
/geldwaesche-aml-kyc:gwg-risikoanalyse
Mandantin (BaFin-lizenzierte Vermögensverwaltung, 120 Mio. AuM,
internationales Privatkundengeschäft inkl. CH und VAE) hat seit
zwei Jahren keine Risikoanalyse aktualisiert. Bitte Aufbau einer
GwG-konformen Risikoanalyse nach § 5 GwG inkl. Risikofaktoren-
katalog (Kunde / Produkt / Vertriebsweg / Geografie) und
Dokumentationsraster.
```

### Szenario 2 – KYC bei komplexer Beteiligungsstruktur
```
/geldwaesche-aml-kyc:kyc-identifikationspflicht
Neukunde ist eine luxemburgische SARL, deren Anteile zu 60 % von
einer zypriotischen Holding gehalten werden, dahinter ein Trust auf
Jersey. Bitte Identifizierungsschritte nach § 11 GwG, wirtschaftlich
Berechtigter nach §§ 3, 19 GwG, Transparenzregisterabfrage und
verstärkte Sorgfaltspflichten § 15 GwG prüfen.
```

### Szenario 3 – Auffällige Bargeldzahlung beim Notar
```
/geldwaesche-aml-kyc:verdachtsmeldung-fiu
Bei einer Immobilien-Beurkundung wird eine Anzahlung in bar
(80.000 EUR) angeboten, Käufer ist über eine Briefkastenstruktur
zwischengeschaltet. Bitte prüfen, ob Meldepflicht nach § 43 GwG
besteht, Meldetext für goAML entwerfen und § 46 Stillhaltepflicht
sowie § 47 Tippoff-Verbot berücksichtigen.
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Standardkommentare: **Herzog** GwG, **Bülte** GwG, **Kreitmair** GwG, **Quedenfeld** Handbuch Bekämpfung Geldwäsche und Wirtschaftskriminalität. Strafrecht zu § 261 StGB: **MüKoStGB**, **NK-StGB**, **Fischer**. Banken-Sondervorschriften: **Boos/Fischer/Schulte-Mattler**, KWG-Kommentar.

Rechtsprechung des BGH-Strafsenats zu § 261 StGB n.F. und des BVerwG zur Auslegung von § 43 GwG ist mit `[unverifiziert – prüfen in juris]` zu kennzeichnen, solange nicht extern bestätigt.

## Hinweise

- **Tippoff-Verbot (§ 47 GwG).** Weder Kunde noch unbeteiligter Dritter darf von einer Meldung erfahren – Verstoß ist Ordnungswidrigkeit (§ 56 GwG) und kann § 258 StGB-relevant sein.
- **Stillhaltepflicht (§ 46 GwG).** Nach Meldung darf die Transaktion drei Werktage nicht durchgeführt werden; Ausnahmen nur, soweit unaufschiebbar und nachträgliche Meldung folgt.
- **Berufsrecht.** Für Anwälte, StB, Notare gilt die Sondervorschrift § 43 II GwG: Meldepflicht durchbricht Verschwiegenheit nur bei wissentlicher Beteiligung an Geldwäsche; im Übrigen § 43e BRAO, § 14a BNotO.
- **EU-Vollharmonisierung.** AMLR (VO (EU) 2024/1624) ist ab Juli 2027 unmittelbar anwendbar `[unverifiziert – Anwendungsbeginn prüfen]`; AMLA übernimmt direkte Aufsicht über große grenzüberschreitende Verpflichtete. In der Übergangsphase ist die Wechselwirkung mit dem fortgeltenden GwG zu beachten.
- **Mandatsgeheimnis (§ 43a BRAO, § 203 StGB).** Keine echten Mandatsdaten ohne § 203-konformen Gateway / AVV.
