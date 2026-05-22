# Verfassungsrecht

**Production-grade Verfassungsrechts-Skills für Claude / Gemini / GPT.** Tested workflows, primary-source citations, Researcher → Drafter → Reviewer sub-agents.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `verfassungsbeschwerde` | Zulässigkeits- und Begründetheitsprüfung einer Verfassungsbeschwerde inkl. Schriftsatzentwurf | Art. 93 I Nr. 4a GG; §§ 90 ff., 93, 93a BVerfGG |
| `grundrechtspruefung` | 3-Stufen-Schema (Schutzbereich, Eingriff, verfassungsrechtliche Rechtfertigung) inkl. Verhältnismäßigkeit | Art. 1–19 GG; Art. 20 GG; BVerfG-Rspr. |
| `organstreit-bund-laender` | Abgrenzung Organstreit / Bund-Länder-Streit / abstrakte Normenkontrolle, Antragsvoraussetzungen | Art. 93 I Nr. 1, 2, 3 GG; §§ 63 ff., 68 ff., 76 ff. BVerfGG |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: GG, BVerfGG, Standardkommentare, BVerfG-Leitentscheidungen
- [`agents/drafter.md`](./agents/drafter.md) – Erstellung im Gutachten- oder Urteilsstil
- [`agents/reviewer.md`](./agents/reviewer.md) – Zulässigkeits-, Frist- und Berufsrechts-Check

## Installation

### Claude Code
```bash
# Über Marketplace (empfohlen)
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install verfassungsrecht

# Oder als ZIP
# Claude Code → Customize Plugins → Install from .zip → verfassungsrecht.zip
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area verfassungsrecht --out dist/gemini
# Inhalt der erzeugten Dateien in neue Gemini-Gems einfügen
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area verfassungsrecht --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Verfassungsbeschwerde gegen letztinstanzliches Urteil

```
/verfassungsrecht:verfassungsbeschwerde
Mandant wurde durch BGH-Revisionsurteil rechtskräftig zur Unterlassung
einer Meinungsäußerung verurteilt. Er sieht Art. 5 Abs. 1 GG verletzt.
Bitte Zulässigkeit (Rechtswegerschöpfung, Subsidiarität, Frist § 93
BVerfGG) und Begründetheit (Schutzbereich, Eingriff, Rechtfertigung)
prüfen und Schriftsatzentwurf vorbereiten.
```

### Szenario 2 – Grundrechtsprüfung Berufsfreiheit

```
/verfassungsrecht:grundrechtspruefung
Landesgesetz beschränkt Tätigkeit freier Heilpraktiker durch neuen
Erlaubnisvorbehalt. Bitte Prüfung Art. 12 Abs. 1 GG: Schutzbereich,
Eingriffsqualität (Berufsausübungs- vs. Berufswahlregelung,
Drei-Stufen-Theorie), Schranken und Schranken-Schranken
(Verhältnismäßigkeit).
```

### Szenario 3 – Organstreit zwischen Bundestagsfraktion und Bundesregierung

```
/verfassungsrecht:organstreit-bund-laender
Eine Bundestagsfraktion sieht ihr Informationsrecht aus Art. 38 Abs. 1
S. 2 GG durch verweigerte Auskunft der Bundesregierung verletzt. Bitte
Abgrenzung zu Bund-Länder-Streit und abstrakter Normenkontrolle,
Antragsberechtigung (§ 63 BVerfGG), Antragsgegenstand und Frist
(§ 64 Abs. 3 BVerfGG) prüfen.
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Standardkommentare: **Maunz/Dürig GG**, **von Münch/Kunig GG**, **Sachs GG**, **Dreier GG**, **Jarass/Pieroth GG**; **Schlaich/Korioth**, „Das Bundesverfassungsgericht".

Rechtsprechung: BVerfG im Format `BVerfG, Urt./Beschl. v. TT.MM.JJJJ – Az., BVerfGE Bd., Seite Rn. N`. Unverifizierte Zitate werden mit `[unverifiziert – prüfen in juris/BVerfG-Datenbank]` markiert.

## Hinweise

- **§ 31 BVerfGG ist die Ausnahme** vom Grundsatz „keine Präjudizienbindung". Tragende Gründe von BVerfG-Entscheidungen binden alle Verfassungsorgane sowie alle Gerichte und Behörden; Entscheidungen nach § 13 Nr. 6, 6a, 11, 12, 14 BVerfGG haben Gesetzeskraft.
- **Verfassungsbeschwerde ist subsidiärer Rechtsbehelf.** Rechtsweg muss erschöpft sein (§ 90 Abs. 2 S. 1 BVerfGG); auch außerhalb des Rechtswegs zumutbare Abhilfen sind auszuschöpfen.
- **Monatsfrist § 93 Abs. 1 BVerfGG** bei Urteilsverfassungsbeschwerde, **Jahresfrist § 93 Abs. 3 BVerfGG** bei Rechtssatzverfassungsbeschwerde gegen Gesetze.
- **Mandatsgeheimnis (§ 43a BRAO, § 203 StGB):** Keine echten Mandatsdaten ohne § 203-konformen Gateway. Siehe [`../references/gateway-setup.md`](../references/gateway-setup.md).
