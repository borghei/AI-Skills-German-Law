# Urheber- und Medienrecht

**Production-grade Urheber- und Medienrechts-Skills für Claude / Gemini / GPT.** Deutsches Urheberrecht (UrhG, UrhDaG, VGG, KUG) und Medienrecht (MStV, Landesmediengesetze, Landespressegesetze) aus anwaltlicher Praxisperspektive. Researcher → Drafter → Reviewer.

Abgegrenzt von:

- `gewerblicher-rechtsschutz` (Marken/Designs/Übersicht gewerbliche Schutzrechte)
- `patentrecht` (technische Schutzrechte)
- `wettbewerbsrecht` (UWG-irreführende Pressedarstellung als Schnittstelle)
- `datenschutzrecht` (DSGVO-Medienprivileg als Schnittstelle)

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `urheberrechtsverletzung-abmahnung` | Prüfung der Werkqualität und Verletzungshandlung, Entwurf einer § 97a-konformen Abmahnung mit dreifacher Schadensberechnung und Provider-Auskunft | §§ 2, 7, 15 ff., 31, 72, 87 ff., 97, 97a, 98, 101, 102 UrhG; UrhDaG; § 14 III TMG-Rspr.; EuGH „Cofemel"/„Brompton" |
| `lizenzvertrag-urhg` | Entwurf und Review eines Lizenzvertrags mit Nutzungsrechtseinräumung, Zweckübertragung und Angemessenheits-Check; Filmrecht- und Verlagsrecht-Schnittstelle | §§ 31–43 UrhG (insb. § 31 V Zweckübertragung), §§ 32, 32a, 32d UrhG (angemessene Vergütung, Bestseller-Klausel, Auskunft), §§ 40, 41 UrhG, §§ 88 ff. UrhG, VerlG, VGG, UrhDaG; AGB-Kontrolle §§ 305 ff. BGB |
| `mstv-medienrechtspruefung` | Pflichtenprüfung für Diensteanbieter und journalistisch-redaktionelle Telemedien: Impressum, Trennungsgebot, Sorgfaltspflichten, Gegendarstellung, Aufsicht | §§ 18, 19, 20, 22, 78 ff. MStV; Landespressegesetze; §§ 22, 23 KUG; §§ 823 I, 1004 BGB iVm Art. 1 I, 2 I GG; Art. 5 GG; DSA VO (EU) 2022/2065; DSGVO-Medienprivileg |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: UrhG/UrhDaG/MStV-Statute, BGH I. ZS / EuGH / OLG-Rspr., Standardkommentare (Dreier/Schulze, Schricker/Loewenheim, Wandtke/Bullinger, BeckOK UrhG, Fechner Medienrecht, Hamburger Kommentar Gesamtes Medienrecht).
- [`agents/drafter.md`](./agents/drafter.md) – Entwurf von Abmahnungen, Lizenzverträgen, Gegendarstellungen und medienrechtlichen Pflichtenkatalogen in Gutachten-/Urteilsstil.
- [`agents/reviewer.md`](./agents/reviewer.md) – Risiko-, Frist- und Berufsrechts-Check (insb. § 97a UrhG-Inhaltsanforderungen, dreifache Schadensberechnung, Zweckübertragung, Bestseller-Klausel, Gegendarstellungsfristen).

## Installation

### Claude Code
```bash
# Über Marketplace (empfohlen)
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install urheber-medienrecht

# Oder als ZIP
# Claude Code → Customize Plugins → Install from .zip → urheber-medienrecht.zip
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area urheber-medienrecht --out dist/gemini
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area urheber-medienrecht --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Urheberrechtsverletzung durch Bilderklau auf Online-Shop

```
/urheber-medienrecht:urheberrechtsverletzung-abmahnung
Mandantin (Berufsfotografin) entdeckt ein eigenes Lichtbildwerk
unverändert auf der Produktseite eines kommerziellen Online-Shops.
Keine Lizenzierung. Bitte Werkqualität (§ 2 I Nr. 5 / § 72 UrhG)
prüfen, Abmahnung nach § 97a UrhG entwerfen, Schadensersatz nach
Lizenzanalogie (MFM-Bildhonorartabellen) berechnen, Reaktion auf
mögliche neg. Feststellungsklage skizzieren.
```

### Szenario 2 – Total-Buy-Out-Vertrag prüfen

```
/urheber-medienrecht:lizenzvertrag-urhg
Mandant (Drehbuchautor) hat einen Buy-Out-Vertrag erhalten:
einmalige Pauschale von 8.000 EUR, alle Nutzungsrechte räumlich und
zeitlich unbeschränkt, alle bekannten und unbekannten Nutzungsarten.
Bitte prüfen: AGB-Kontrolle, Zweckübertragungsregel § 31 V UrhG,
Angemessenheit § 32 UrhG, Bestseller-Klausel § 32a UrhG,
Rückrufrecht § 41 UrhG bei Nichtausübung.
```

### Szenario 3 – Gegendarstellungsverlangen gegen Online-Magazin

```
/urheber-medienrecht:mstv-medienrechtspruefung
Mandantin (Geschäftsführerin eines KMU) wurde in einem
journalistisch-redaktionellen Online-Magazin mit der unrichtigen
Tatsachenbehauptung konfrontiert, sie habe Insolvenz angemeldet.
Bitte Gegendarstellungsantrag nach § 20 MStV / Landespressegesetz
entwerfen, Frist „unverzüglich, spätestens 3 Monate" prüfen,
Hilfsanspruch Berichtigung/Unterlassung nach §§ 823, 1004 BGB
analog skizzieren. Zusätzlich Impressumspflicht § 18 MStV beim
Magazin prüfen.
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Standardkommentare:

- **UrhG:** Dreier/Schulze, Schricker/Loewenheim, Wandtke/Bullinger, BeckOK UrhG (Ahlberg/Götting)
- **Medienrecht:** Fechner, Medienrecht; Paschke/Berlit/Meyer, Hamburger Kommentar Gesamtes Medienrecht; Spindler/Schuster, Recht der elektronischen Medien
- **EU:** Walter/von Lewinski, European Copyright Law (zu InfoSoc-RL und DSM-RL)

Rechtsprechung: BGH (I. Zivilsenat – Urheberrecht; VI. Zivilsenat – Persönlichkeitsrecht/Presserecht), EuGH, OLGe (insb. Hamburg, Köln, München für Urheberrecht; Hamburg/Berlin/Karlsruhe für Presserecht). Unverifizierte Zitate sind mit `[unverifiziert – prüfen in juris/Beck-Online]` markiert.

## Hinweise

- **EuGH-Schöpfungshöhenlinie.** „Cofemel" (C-683/17) und „Brompton" (C-833/18) `[unverifiziert]` haben die deutsche Lehre der „kleinen Münze" europarechtlich verschoben; die Anforderung der „eigenen geistigen Schöpfung" ist unionsrechtlich autonom auszulegen.
- **Plattformhaftung.** Seit UrhDaG (Umsetzung Art. 17 DSM-RL) gilt für große Online-Diensteanbieter ein eigener Pflichtenkanon; klassische Störerhaftung nach §§ 7 ff. TMG-Rspr. ist nur noch eingeschränkt anwendbar.
- **Pressefreiheit und DSGVO.** Art. 85 DSGVO iVm Landespressegesetzen / § 23 MStV (Medienprivileg) — nicht ohne Prüfung des Anwendungsbereichs.
- **Gegendarstellung ist Tatsachenkorrektur, keine Meinungsäußerung.** Eine als Gegendarstellung getarnte Werbe- oder Meinungsäußerung ist unbegründet — Risiko: § 20 V MStV / Landespressegesetz, kein Anspruch.
- **§ 97a III UrhG Deckelung** auf 1.000 EUR Gegenstandswert gilt nur bei erstmaliger Abmahnung gegenüber einem privaten Verbraucher außerhalb gewerblicher Tätigkeit. Pauschale Anwendung auf Gewerbetreibende ist Berufspflichtenverstoß.
- **Mandantengeheimnis (§ 43a BRAO, § 203 StGB):** Keine Klarnamen oder Urhebernamen ohne § 203-konformen Gateway.
