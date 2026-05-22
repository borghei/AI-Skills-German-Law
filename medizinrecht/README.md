# Medizinrecht

**Production-grade Medizinrechts-Skills für Claude / Gemini / GPT.** Deutsches Medizinrecht aus Praxisperspektive: zivilrechtliche Arzthaftung nach den §§ 630a–630h BGB (Patientenrechtegesetz 2013), Deliktsrecht §§ 823 ff. BGB, ärztliches Berufsrecht (MBO-Ä, Landesberufsordnungen, Heilberufekammergesetze der Länder), Schweigepflicht § 203 StGB, Schnittstellen zu SGB V (vertragsärztliche Versorgung), BÄO (Approbation), AMG und MPDG. Researcher → Drafter → Reviewer.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `arzthaftung-aufklaerungspflicht` | Prüfung der Selbstbestimmungsaufklärung, Form, Adressat, Beweislast; Entwurf einer Stellungnahme | §§ 630a, 630c, 630e, 630h BGB; § 823 BGB; §§ 223 ff. StGB |
| `patientenrechte-akteneinsicht` | Anspruch auf Einsicht in die Behandlungsakte, parallele Ansprüche aus Art. 15 DSGVO; Erbeneinsicht | § 630g BGB; Art. 15 DSGVO; § 22 BDSG; §§ 1827 ff. BGB |
| `mbo-aerzte-pruefung` | Berufsrechtliche Prüfung der ärztlichen Pflichten (Werbung, Schweigepflicht, Dokumentation, Fernbehandlung, Fortbildung) | MBO-Ä §§ 4, 7, 8–10, 12, 27; § 203 StGB; HeilBerKG/HKaG der Länder; BÄO |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: BGB-Behandlungsvertrag, StGB-Schweigepflicht, MBO-Ä, BGH VI. Zivilsenat-Rspr., Standardkommentare
- [`agents/drafter.md`](./agents/drafter.md) – Erstellung im Gutachten- oder Urteilsstil mit ausdrücklicher Beweislastprüfung nach § 630h BGB
- [`agents/reviewer.md`](./agents/reviewer.md) – Risiko-, Frist- und Berufsrechts-Check inkl. 30-Jahre-Höchstfrist § 199 II BGB, § 203 StGB und §-630h-Beweislastregeln

## Installation

### Claude Code
```bash
# Über Marketplace (empfohlen)
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install medizinrecht

# Oder als ZIP
# Claude Code → Customize Plugins → Install from .zip → medizinrecht.zip
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area medizinrecht --out dist/gemini
# Inhalt der erzeugten Dateien in neue Gemini-Gems einfügen
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area medizinrecht --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Aufklärungspflicht vor Wirbelsäulen-OP

```
/medizinrecht:arzthaftung-aufklaerungspflicht
Patientin (62 J.) hat sich elektiv einer Bandscheiben-OP unterzogen.
Aufklärung erfolgte am Vorabend der OP durch Stationsärztin in
fünfminütigem Gespräch, Aufklärungsbogen unterschrieben. Postoperativ
Nervenschaden. Bitte prüfen: Wirksamkeit der Einwilligung,
Aufklärungstiefe, Beweislast § 630h II BGB, mögliche hypothetische
Einwilligung.
```

### Szenario 2 – Erbeneinsicht in Behandlungsakte

```
/medizinrecht:patientenrechte-akteneinsicht
Verstorbener Patient hinterlässt zwei Erben. Verdacht auf
Behandlungsfehler. Klinik verweigert Einsicht unter Hinweis auf
Schweigepflicht und "mutmaßlichen Willen" des Verstorbenen. Bitte
prüfen: Anspruch der Erben nach § 630g III BGB, Verhältnis zu
Art. 15 DSGVO, Beweisanforderungen für mutmaßliche
Geheimhaltungsinteressen.
```

### Szenario 3 – Bewertungsportal und ärztliche Werbung

```
/medizinrecht:mbo-aerzte-pruefung
Mandant (Facharzt für Plastische Chirurgie) bewirbt auf seiner Website
"100 % Erfolgsquote bei Brustvergrößerungen" und kauft Top-Platzierung
auf einem Arztbewertungsportal. Ärztekammer leitet berufsrechtliches
Verfahren ein. Bitte berufsrechtliche Prüfung MBO-Ä § 27, Verhältnis
zum HWG, mögliche Sanktionen nach HeilBerKG.
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Standardkommentare: **Laufs/Katzenmeier/Lipp**, Handbuch des Arztrechts, **Spickhoff**, Medizinrecht (Kommentar), **Ratzel/Lippert**, Kommentar zur MBO-Ä, **Pauge**, Arzthaftungsrecht, **MüKoBGB** und **BeckOK BGB** zu §§ 630a–630h.

Rechtsprechung: BGH VI. Zivilsenat (Arzthaftung), Landesberufsgerichte. Unverifizierte Zitate werden mit `[unverifiziert – prüfen in juris]` markiert.

## Hinweise

- **Schweigepflicht § 203 StGB** ist medizinrechtlich zentral und strafbewehrt; Verletzung ist zugleich Berufspflichtverletzung MBO-Ä § 9 / § 8 (je nach LBO). Übermittlung von Behandlungsdaten an Dritte (auch IT-Dienstleister) nur über § 203 III StGB-konforme Konstruktion oder gesetzliche Übermittlungsermächtigung.
- **Beweislastumkehr nach § 630h BGB** ist die Stellschraube jeder Arzthaftung: § 630h I (voll beherrschbares Risiko), II (Aufklärungs- und Einwilligungsmängel), III (Dokumentationslücke), IV (mangelnde Befähigung), V (grober Behandlungsfehler).
- **Verjährung** regelmäßig §§ 195, 199 BGB (3 Jahre ab Kenntnis), aber **Höchstfrist 30 Jahre ab Begehung** bei Verletzung des Lebens, Körpers, Gesundheit oder Freiheit (§ 199 II BGB) – im Arzthaftungsrecht regelmäßig einschlägig.
- **Keine Präjudizienbindung** deutscher Gerichte außer § 31 BVerfGG; BGH-Linie zum Arzthaftungsrecht ist faktisch leitend, aber kein Präjudiz.
- **Mandatsgeheimnis (§ 43a BRAO, § 203 StGB):** Keine echten Patienten-/Behandlungsdaten ohne § 203-konformen Gateway und AVV.
