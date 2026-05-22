# KI-Governance

**Production-grade KI-Governance-Skills für Claude / Gemini / GPT.** Querschnittsdisziplin: Aufbau- und Ablauforganisation für den KI-Einsatz im Unternehmen / in der Kanzlei, Rollen und Verantwortlichkeiten, Lieferantenmanagement, Ethik-Leitplanken, ISO/IEC 42001 (KI-Management-System), ISO/IEC 23894 (KI-Risikomanagement), NIST AI RMF 1.0, BSI AIC4. Researcher → Drafter → Reviewer.

> **Abgrenzung zu `ki-vo-compliance`.** Dieses Plugin behandelt **Governance** (Organisation, Prozesse, Standards). Die gesetzlichen Anbieter- und Betreiberpflichten der KI-VO (VO (EU) 2024/1689) – insbesondere Art. 4, 5, 6, 26, 50 ff. – sind im Plugin [`ki-vo-compliance`](../ki-vo-compliance/README.md) abgebildet. KI-VO-Pflichten werden hier nur als Bezugspunkt referenziert, nicht inhaltlich gedoppelt.

## Skills in dieser Version

| Skill | Funktion | Hauptanker |
|---|---|---|
| `ki-risikoassessment` | Strukturierte KI-Risikobewertung pro System (Identifikation, Klassifizierung, Schadensanalyse, Risk-Treatment, Wiedervorlage) | ISO/IEC 23894; NIST AI RMF; Art. 6 + Anhang III KI-VO als Trigger |
| `ki-monitoring-konzept` | Laufende Überwachung nach Inbetriebnahme (Performance, Datendrift, Concept Drift, Fairness, Robustheit, Vorfallsmanagement, Audits) | ISO/IEC 42001; Art. 12, 14, 72 KI-VO als Bezugspunkt |
| `ki-richtlinie-entwurf` | Interne KI-Richtlinie / Policy (Geltungsbereich, Grundsätze, Genehmigungsprozess, Rollen, Lieferanten, Schulung, Vorfälle) | Art. 4 KI-VO; Art. 28 DSGVO; § 43e BRAO; ISO/IEC 42001 Kap. 5–8 |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: KI-VO-Bezüge, DSGVO, Berufsrecht, Industrie-Standards
- [`agents/drafter.md`](./agents/drafter.md) – Erstellung von Risikoberichten, Monitoring-Konzepten, Richtlinien-Templates
- [`agents/reviewer.md`](./agents/reviewer.md) – Check auf saubere Abgrenzung zur KI-VO, AVV-Vollständigkeit, Schulungspflicht Art. 4 KI-VO

## Installation

### Claude Code
```bash
# Über Marketplace (empfohlen)
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install ki-governance

# Oder als ZIP
# Claude Code → Customize Plugins → Install from .zip → ki-governance.zip
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area ki-governance --out dist/gemini
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area ki-governance --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Risikoassessment eines neuen KI-Systems

```
/ki-governance:ki-risikoassessment
Mittelständische Kanzlei will einen LLM-basierten Vertragsanalyse-
Assistenten einführen (SaaS, Drittland-Anbieter). Bitte strukturiertes
Risikoassessment nach ISO/IEC 23894 / NIST AI RMF, inkl. KI-VO-
Risikoklassifizierung als Trigger, DSGVO-Bezug, Berufsrechts-Aspekte.
```

### Szenario 2 – Monitoring-Konzept für ein produktiv genutztes Modell

```
/ki-governance:ki-monitoring-konzept
Versicherer betreibt ein internes Scoring-Modell zur Tarifkalkulation
(Hochrisiko-Indiz Anhang III Nr. 5 KI-VO). Bitte Monitoring-Konzept
mit Performance-, Drift- und Fairness-Metriken, Eskalationswegen
und Audit-Intervallen.
```

### Szenario 3 – KI-Richtlinie für die Kanzlei

```
/ki-governance:ki-richtlinie-entwurf
Sozietät (35 Berufsträger) will eine verbindliche interne KI-Richtlinie
einführen. Bitte Entwurf mit Geltungsbereich, Grundsätzen, Genehmi-
gungsprozess, Rollen, Lieferantenmanagement (§ 43e BRAO, § 203 StGB),
Schulungskonzept (Art. 4 KI-VO).
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Standardkommentare: **Keller/Kapoor** KI-VO, **Hartmann/Hilgendorf** KI-Recht, **Kühling/Buchner** DSGVO/BDSG, **Paal/Pauly** DSGVO/BDSG, **Henssler/Prütting** BRAO (zu §§ 43a, 43e, 203). Industrie-Standards: ISO/IEC 42001:2023, ISO/IEC 23894:2023, ISO/IEC 22989:2022, NIST AI RMF 1.0 (Januar 2023), BSI AIC4 (Stand 2021).

Standards werden mit präzisem Veröffentlichungsstand zitiert und auf die offizielle Veröffentlichung (ISO, NIST, BSI) verlinkt – kein urheberrechtlich geschützter Volltext im Output. Rspr. wird mit `[unverifiziert – prüfen]` markiert, soweit nicht extern bestätigt.

## Hinweise

- **Keine Doppelung der KI-VO-Pflichten.** Gesetzliche Anbieter- und Betreiberpflichten gehören in `ki-vo-compliance`; hier wird nur die organisatorische Umsetzung adressiert.
- **AVV nach Art. 28 DSGVO** mit jedem Drittanbieter zwingend (LLM-as-a-Service idR Auftragsverarbeitung).
- **Berufsrecht.** Auslagerung anwaltlicher Tätigkeiten an KI-Dienstleister nur unter § 43e BRAO (Verschwiegenheits- und Sicherheitsvorgaben); § 203 StGB-konformer Gateway erforderlich.
- **Schulungspflicht Art. 4 KI-VO** seit 02.02.2025 anwendbar; in der Governance verankern.
- **Keine Präjudizienbindung** deutscher Gerichte (Ausnahme § 31 BVerfGG); BGH/EuGH-Rspr. als faktischer Maßstab.
