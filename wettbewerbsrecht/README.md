# Wettbewerbsrecht (UWG)

**Production-grade Lauterkeitsrechts-Skills für Claude / Gemini / GPT.** Deutsches UWG aus Praxisperspektive: Schwarze Liste (Anhang zu § 3 III), Generalklauseln §§ 3, 3a, irreführende und vergleichende Werbung §§ 5, 5a, 5b, 6, aggressive Praktiken § 4a, unzumutbare Belästigung § 7, Ansprüche und Verfahren §§ 8 ff., einstweiliger Rechtsschutz §§ 12 ff. Researcher → Drafter → Reviewer.

Kartellrecht (GWB) ist nicht Gegenstand dieses Plugins und wird separat ausgeliefert.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `uwg-abmahnung-pruefung` | Prüfung einer UWG-Abmahnung aus Abmahner- und Abgemahnten-Perspektive | §§ 8, 8b, 8c, 13, 13a UWG; § 242 BGB |
| `irrefuehrende-werbung-pruefung` | Prüfung einer Werbeaussage auf Irreführung und vergleichende Werbung | §§ 3, 3 III iVm Anhang, 5, 5a, 5b, 6 UWG; UGP-RL 2005/29/EG |
| `einstweilige-verfuegung-uwg` | Verfügungsanspruch, Dringlichkeitsvermutung, Vollziehung, Schutzschrift | §§ 12 ff. UWG; §§ 935, 940, 929 II, 945 ZPO |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: UWG-Statute, BGH I. Zivilsenat, Kommentarliteratur (Köhler/Bornkamm/Feddersen, Harte-Bavendamm/Henning-Bodewig, Großkommentar)
- [`agents/drafter.md`](./agents/drafter.md) – Erstellung im Gutachten- oder Urteilsstil mit konkretem Antrags- und Tenor-Entwurf
- [`agents/reviewer.md`](./agents/reviewer.md) – Risiko-, Frist- und Berufsrechts-Check (inkl. 6-Monats-Verjährung § 11 UWG, Vollziehungsfrist § 929 II ZPO)

## Installation

### Claude Code
```bash
# Über Marketplace (empfohlen)
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install wettbewerbsrecht

# Oder als ZIP
# Claude Code → Customize Plugins → Install from .zip → wettbewerbsrecht.zip
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area wettbewerbsrecht --out dist/gemini
# Inhalt der erzeugten Dateien in neue Gemini-Gems einfügen
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area wettbewerbsrecht --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Eingehende UWG-Abmahnung eines Verbandes

```
/wettbewerbsrecht:uwg-abmahnung-pruefung
Mandantin (Online-Händlerin) hat von einem Verband (e. V.) eine
Abmahnung wegen fehlender Grundpreisangaben erhalten. Gefordert:
Unterlassungserklärung mit Vertragsstrafe (5.100 EUR pro Verstoß)
und Aufwendungsersatz 295 EUR. Bitte Aktivlegitimation §§ 8, 8b,
Rechtsmissbrauchsindizien § 8c und Reaktionsoptionen prüfen.
```

### Szenario 2 – Vergleichende Werbung auf Landing-Page

```
/wettbewerbsrecht:irrefuehrende-werbung-pruefung
Mandant (SaaS-Anbieter) wirbt mit "schneller als Marktführer X" und
Sternchen-Hinweis im Footer. Bitte §§ 5, 5a, 6 UWG prüfen, Maßstab
des durchschnittlich informierten Verbrauchers, Schnittstelle zur
Schwarzen Liste (Anhang § 3 III) und PAngV-Konformität.
```

### Szenario 3 – Antrag auf einstweilige Verfügung wegen Werbeaussage

```
/wettbewerbsrecht:einstweilige-verfuegung-uwg
Mandantin (Mitbewerberin) will gegen rechtswidrige Werbung der
Konkurrenz einstweilige Verfügung beantragen. Erstkenntnis vor
2 Wochen, noch keine Abmahnung ausgesprochen. Bitte Dringlichkeits-
vermutung § 12 I UWG, Schutzschriftenregister, Vollziehungsfrist
§ 929 II ZPO und Antragsentwurf.
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Standardkommentare: **Köhler/Bornkamm/Feddersen** UWG (BeckOK aktuell), **Harte-Bavendamm/Henning-Bodewig** UWG, **Ohly/Sosnitza** UWG, **Großkommentar UWG** (Jacobs/Lindacher/Teplitzky).

Rechtsprechung: BGH (I. Zivilsenat – Wettbewerbssenat), OLG, EuGH zur UGP-RL 2005/29/EG. Format: `BGH, Urt. v. TT.MM.JJJJ – I ZR NN/JJ, GRUR Jahr, Seite Rn. N`. Unverifizierte Zitate werden mit `[unverifiziert – prüfen in juris]` markiert.

## Hinweise

- **6-Monats-Verjährung § 11 UWG.** Kürzer als die regelmäßige Verjährung des BGB – nicht übersehen. Kenntnisabhängiger Beginn.
- **Dringlichkeitsvermutung § 12 I UWG.** Selbstwiderlegung durch Zuwarten — Praxis der Gerichte uneinheitlich (Faustregel 4–8 Wochen ab Kenntnis, abhängig vom OLG-Bezirk).
- **Rechtsmissbrauch § 8c UWG.** Indizien-Katalog Abs. 2 (Massenabmahnungen, überhöhter Gegenstandswert, unangemessen hohe Vertragsstrafe) seit UWG-Novelle 2021 kodifiziert.
- **Keine Präjudizienbindung deutscher Gerichte** außer § 31 BVerfGG; EuGH-Auslegung der UGP-RL ist für den BGH bindend (Art. 267 AEUV, Anwendungsvorrang).
- **Mandatsgeheimnis (§ 43a BRAO, § 203 StGB):** Keine echten Mandatsdaten ohne § 203-konformen Gateway.
