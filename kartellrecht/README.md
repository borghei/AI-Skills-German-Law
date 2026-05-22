# Kartellrecht

**Production-grade Kartellrechts-Skills für Claude / Gemini / GPT.** Deutsches GWB und EU-Wettbewerbsrecht aus Praxisperspektive: Kartellverbot § 1 GWB / Art. 101 AEUV, Marktbeherrschung und Missbrauch §§ 18, 19, 19a, 20 GWB / Art. 102 AEUV, Fusionskontrolle §§ 35 ff. GWB und EU-FK-VO 139/2004 inkl. Transaktionswert-Schwelle § 35 Ia, Vertikal-GVO 2022/720, FuE-GVO 2023/1066, private Durchsetzung §§ 33 ff. GWB (Kartellschadensersatz). Researcher → Drafter → Reviewer.

Lauterkeitsrecht (UWG) ist Gegenstand des Plugins `wettbewerbsrecht`; die DMA-Pflichten der Gatekeeper liegen im Plugin `dsa-dma`. Schnittstellen zu `kapitalmarktrecht` (öffentliche Übernahme), `patentrecht` (FRAND, Standard-Essential Patents) und `aussenwirtschaft-zoll-sanktionen` (Investitionskontrolle AWG/AWV) werden in den jeweiligen Skills gekreuzreferenziert.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `gwb-zusammenschluss-anmeldung` | Anmeldepflicht beim BKartA, Umsatz- und Transaktionswert-Schwellen, Vollzugsverbot, Vorprüfung/Hauptprüfung | §§ 35–43 GWB; §§ 73 ff. GWB; EU-FK-VO 139/2004 (One-Stop-Shop) |
| `kartellverbot-pruefung` | Subsumtion einer Vereinbarung/abgestimmten Verhaltensweise unter § 1 GWB / Art. 101 AEUV, Vertikal-GVO-Sicherheitshafen, Einzelausnahme | § 1 GWB; § 2 GWB; Art. 101 I, III AEUV; VO (EU) 2022/720; De-minimis-Bekanntmachung |
| `marktbeherrschung-bewertung` | Marktabgrenzung, Marktanteilsvermutung, Missbrauchstatbestände inkl. § 19a strukturmarktrelevante Plattformen | §§ 18, 19, 19a, 20, 21 GWB; Art. 102 AEUV; SSNIP-Test |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: GWB, AEUV, EU-Sekundärrecht (FK-VO, Vertikal-GVO, FuE-GVO), BGH Kartellsenat / EuGH / OLG Düsseldorf-Kartellsenat / BKartA / EU-Kommission, Standardkommentare Immenga/Mestmäcker, Langen/Bunte, Loewenheim/Meessen/Riesenkampff, Bechtold/Bosch, FK-Kartellrecht
- [`agents/drafter.md`](./agents/drafter.md) – Erstellung im Gutachten- oder Urteilsstil; Anmeldeschrift-Skizzen, Subsumtions-Memos, Missbrauchsanalysen
- [`agents/reviewer.md`](./agents/reviewer.md) – Risiko-, Frist- und Berufsrechts-Check (Vollzugsverbot § 41, Hauptprüfungsfristen § 40, Verjährung § 33h GWB, Bindungswirkung § 33b, EU-Anmeldepflicht Art. 4 FK-VO)

## Installation

### Claude Code
```bash
# Über Marketplace (empfohlen)
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install kartellrecht

# Oder als ZIP
# Claude Code → Customize Plugins → Install from .zip → kartellrecht.zip
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area kartellrecht --out dist/gemini
# Inhalt der erzeugten Dateien in neue Gemini-Gems einfügen
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area kartellrecht --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – M&A-Anmeldung beim BKartA

```
/kartellrecht:gwb-zusammenschluss-anmeldung
Mandantin (Maschinenbau, weltw. Umsatz 800 Mio. EUR, Inland 90 Mio. EUR)
plant Erwerb von 100 % der Anteile an einer deutschen Zielgesellschaft
(Inland 20 Mio. EUR). Closing geplant in 8 Wochen. Bitte Anmeldepflicht
§ 35 GWB prüfen, Verhältnis zur EU-FK-VO klären, Vor- und Haupt-
prüfungsfristen § 40 GWB einplanen, Vollzugsverbot § 41 GWB und Gun-
Jumping-Risiko adressieren.
```

### Szenario 2 – Vertikalvereinbarung mit Preisempfehlung

```
/kartellrecht:kartellverbot-pruefung
Mandant (Hersteller von Markenprodukten, Marktanteil 20 %) plant ein
Selektivvertriebssystem mit "unverbindlicher Preisempfehlung", Verbot
des Verkaufs an nicht autorisierte Händler und Online-Beschränkungen
für autorisierte Händler (kein Verkauf über Drittplattformen). Bitte
§ 1 GWB / Art. 101 AEUV prüfen, Vertikal-GVO 2022/720-Sicherheitshafen
(Kernbeschränkungen, Marktanteilsschwelle), Einzelausnahme § 2 GWB /
Art. 101 III AEUV.
```

### Szenario 3 – Marktbeherrschungs-Missbrauch durch Plattform

```
/kartellrecht:marktbeherrschung-bewertung
Mandantschaft (kleinerer Online-Händler) wirft einer großen Plattform
(potenziell strukturmarktrelevantes Unternehmen iSv § 19a GWB) vor,
gleichartige Eigenangebote im Ranking systematisch zu bevorzugen
(Self-Preferencing). Bitte Marktabgrenzung, Marktanteilsvermutung
§ 18 IV GWB, Behinderungsmissbrauch § 19 II Nr. 1 GWB und § 19a Abs. 2
Nr. 1 GWB prüfen, ggf. parallel Art. 102 AEUV und DMA-Verhältnis
(Plugin dsa-dma) anreißen.
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Standardkommentare: **Immenga/Mestmäcker** Wettbewerbsrecht (GWB, EU), **Langen/Bunte** Kartellrecht, **Loewenheim/Meessen/Riesenkampff/Kersting/Meyer-Lindemann** Kartellrecht, **Bechtold/Bosch** GWB, **FK-Kartellrecht** (Jaeger/Kokott/Pohlmann/Schroeder).

Rechtsprechung: BGH Kartellsenat (KZR-, KVR-Verfahren), OLG Düsseldorf-Kartellsenat (VI-Kart, V-Kart), EuGH, EuG, BKartA-Beschlüsse, EU-Kommission-Entscheidungen. Format: `BGH, Beschl. v. TT.MM.JJJJ – KVR NN/JJ, NZKart Jahr, Seite Rn. N` bzw. `EuGH, Urt. v. TT.MM.JJJJ – Rs. C-NN/JJ, ECLI:EU:C:JJJJ:NNN Rn. N`. Unverifizierte Zitate werden mit `[unverifiziert – prüfen in juris/EuGH-Datenbank/BKartA-Website]` markiert.

## Hinweise

- **Vollzugsverbot § 41 GWB / Art. 7 EU-FK-VO.** Closing vor Freigabe ist Gun-Jumping und bußgeldbewehrt nach § 81 II GWB bis 10 % des weltweiten Konzernumsatzes. **🔴 BLOCKER** bei jeder M&A-Beratung.
- **Bindungswirkung Behördenentscheidung § 33b GWB.** Bestandskräftige BKartA-/Kommissions-Entscheidung wirkt im Folgeprozess auf den deutschen Zivilrichter bindend; in der privaten Durchsetzung essentiell.
- **Verjährung § 33h GWB.** Kenntnisabhängig 5 Jahre, absolut 10 Jahre; Hemmung durch behördliches Verfahren — Verjährungsfalle vermeiden.
- **Hardcore-Beschränkungen** (Preisbindung, Marktaufteilung, Mengen, absoluter Gebietsschutz) sind weder unter Vertikal-GVO noch unter De-minimis privilegiert.
- **Keine Präjudizienbindung deutscher Gerichte** außer § 31 BVerfGG; EuGH-Auslegung der Art. 101/102 AEUV ist für den deutschen Kartellrichter über Art. 267 AEUV und Anwendungsvorrang faktisch maßgeblich.
- **Mandatsgeheimnis (§ 43a BRAO, § 203 StGB):** Keine echten Mandatsdaten ohne § 203-konformen Gateway. Sensible Marktdaten und Kronzeugeninformationen besonders schützen.
