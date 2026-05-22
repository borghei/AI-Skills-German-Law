# Produktrecht

**Production-grade Produktrechts-Skills für Claude / Gemini / GPT.** Deutsches Produkthaftungs-, Produktsicherheits- und Rückrufrecht aus Hersteller-, Importeur- und Marktaufsichtsperspektive. ProdHaftG (Gefährdungshaftung), § 823 BGB-Produzentenhaftung, GPSR (VO (EU) 2023/988, ab 13.12.2024) mit ProdSG-Übergang, sektorale Harmonisierung, öffentlich- und zivilrechtliches Rückrufrecht. Researcher → Drafter → Reviewer.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `prodhaftg-herstellerhaftung` | Parallele Anspruchsprüfung ProdHaftG und § 823 BGB-Produzentenhaftung, Fehlertypologie, Beweislastumkehr | §§ 1, 3, 4, 6, 10–13 ProdHaftG; § 823 BGB; BGH „Hühnerpest" BGHZ 51, 91 |
| `gpsr-sicherheitspruefung` | Pflichtenkatalog Hersteller/Importeur/Fulfillment/Online-Marktplatz nach GPSR mit Risikoanalyse und technischer Dokumentation | Art. 5, 9, 11, 12, 20, 22, 36 GPSR (VO (EU) 2023/988); ProdSG-Übergang; sektorale Harmonisierung |
| `produkt-rueckruf-anordnung` | Zivilrechtliche Rückrufpflicht aus § 823 BGB und öffentlich-rechtliche Anordnung der Marktaufsicht, Maßnahmenstufung, Safety Business Gateway | § 823 I BGB (Produktbeobachtung, BGH „Pflegebetten"); Art. 36 GPSR; § 26 ProdSG; § 28 VwVfG; VwGO |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: ProdHaftG, BGB-Deliktsrecht, GPSR, sektorale ProdSV, BGH-Produzentenhaftungs-Rspr.
- [`agents/drafter.md`](./agents/drafter.md) – Erstellung im Gutachten- oder Urteilsstil, parallel Anspruchsgrundlagen, Maßnahmen- und Rückrufkommunikation
- [`agents/reviewer.md`](./agents/reviewer.md) – Frist-, Risiko- und Berufsrechts-Check (Verjährung § 12 ProdHaftG, Erlöschen § 13, GPSR-Meldepflicht „unverzüglich")

## Installation

### Claude Code
```bash
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install produktrecht
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area produktrecht --out dist/gemini
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area produktrecht --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Personenschaden durch fehlerhaftes Verbraucherprodukt

```
/produktrecht:prodhaftg-herstellerhaftung
Verbraucherin wurde durch berstenden Akku eines Haushaltsgeräts
verletzt. Hersteller sitzt in DE. Bitte parallele Prüfung § 1
ProdHaftG und § 823 I BGB, Fehlertyp (Konstruktions- vs.
Fabrikationsfehler), Beweislastverteilung, Höchstgrenze § 10
ProdHaftG, Verjährung § 12 ProdHaftG.
```

### Szenario 2 – GPSR-Konformität eines neuen Verbraucherprodukts

```
/produktrecht:gpsr-sicherheitspruefung
Mandantin (Importeur Smart-Home-Sensor aus Drittstaat) bringt ab
01/2025 ein neues Produkt in den EU-Markt. Bitte Pflichtenkatalog
Art. 11 GPSR, Risikobewertung, technische Dokumentation, Pflichten
der Online-Marktplätze Art. 22, sowie Abgrenzung zu Funkanlagen-RL
(RED) prüfen.
```

### Szenario 3 – Rückrufanordnung der Landesmarktaufsicht

```
/produktrecht:produkt-rueckruf-anordnung
Marktaufsichtsbehörde droht Rückrufanordnung an, weil Spielzeug-
Charge eine erhöhte Phthalat-Belastung aufweist. Bitte Maßnahmen-
stufung (Warnung → Rückruf → Vernichtung), Verhältnismäßigkeit,
Anhörungsverfahren § 28 VwVfG, Sofortvollzug, Rechtsbehelf VwGO,
sowie parallele zivilrechtliche Rückrufpflicht aus § 823 BGB
(„Pflegebetten") und Safety-Business-Gateway-Meldung Art. 20 GPSR.
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Standardkommentare: **Foerste/Graf von Westphalen** Produkthaftungshandbuch, **Kullmann** ProdHaftG, **Klindt** (jetzt GPSR-Kommentar), **Lenz** ProdHaftG, **MüKoBGB** zu § 823, **Palandt/Grüneberg** zu § 823.

Rechtsprechung: BGH VI. Zivilsenat (Produzentenhaftung); EuGH zur ProdHaftRL 85/374/EWG. Format: `BGH, Urt. v. TT.MM.JJJJ – VI ZR NN/JJ, BGHZ Bd, S. Rn. N`. Unverifizierte Zitate werden mit `[unverifiziert – prüfen in juris/Beck-Online]` markiert.

## Hinweise

- **GPSR-Übergang.** Die GPSR (VO (EU) 2023/988) gilt ab 13.12.2024 und löst das ProdSG für nicht harmonisierte Verbraucherprodukte ab. Für Produkte, die vor diesem Stichtag in Verkehr gebracht wurden, gelten Übergangsregelungen — im Einzelfall prüfen.
- **Sektorale Harmonisierung verdrängt GPSR**, soweit spezielle Anforderungen bestehen (Maschinen-VO 2023/1230 ab 20.01.2027, Spielzeug-RL, NSpRG, EMV, RED, Bauprodukten-VO).
- **Parallele Anspruchsgrundlagen.** ProdHaftG schließt § 823 BGB nicht aus (§ 15 II ProdHaftG); Produzentenhaftung bleibt eigenständig wichtig wegen unbegrenztem Schadensumfang, Schmerzensgeld (§ 253 II BGB) und 10-Jahre-Erlöschen § 13 ProdHaftG.
- **Keine Präjudizienbindung** deutscher Gerichte außer § 31 BVerfGG; BGH-Linie „Hühnerpest" und „Pflegebetten" ist gefestigte, aber nicht formal bindende Rechtsprechung.
- **Mandatsgeheimnis (§ 43a BRAO, § 203 StGB):** Keine echten Hersteller-/Produktdaten ohne § 203-konformen Gateway.
