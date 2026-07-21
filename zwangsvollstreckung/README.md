# Zwangsvollstreckung

**Production-grade Vollstreckungs-Skills für Claude / Gemini / GPT.** Die allgemeinen Vollstreckungsvoraussetzungen, Forderungspfändung mit Pfändungsschutz und P-Konto, Sachpfändung und Vermögensauskunft sowie die Immobiliarvollstreckung nach dem ZVG einschließlich der Teilungsversteigerung — aus Gläubiger-, Schuldner- und Drittschuldnerperspektive. Researcher → Drafter → Reviewer.

> Abgrenzung: Die **Erlangung** des Titels liegt in [`prozessrecht`](../prozessrecht/) (Klageschrift, Mahnverfahren, Versäumnisurteil). Die materiellen Rechtsbehelfe gegen den Titel sind dort in [`prozessrecht/skills/vollstreckungsabwehrklage`](../prozessrecht/skills/vollstreckungsabwehrklage/) und der Überblick in [`prozessrecht/skills/zwangsvollstreckung-grundlagen`](../prozessrecht/skills/zwangsvollstreckung-grundlagen/) behandelt; dieses Plugin geht **in die Tiefe** für den Vollzug. Die Gesamtvollstreckung liegt in [`insolvenzrecht`](../insolvenzrecht/), die Bestellung der Grundschuld in [`immobilien-grundbuchrecht`](../immobilien-grundbuchrecht/).

## Skills

| Skill | Funktion | Anker |
|---|---|---|
| `vollstreckungsvoraussetzungen` | Prüfung der Trias Titel–Klausel–Zustellung vor Vollstreckungsbeginn und Zuordnung jedes Schuldnereinwands zum richtigen Rechtsbehelf | §§ 704, 794, 724–727, 731–733, 750, 751, 756 ZPO; §§ 732, 765a, 766, 767, 768, 771, 793, 797 ZPO |
| `forderungspfaendung` | PfÜB-Antrag, Drittschuldnererklärung und vollständige Prüfung des Pfändungsschutzes bei Lohn und Konto | §§ 828, 829, 835, 836, 840, 845 ZPO; §§ 850, 850a–850e, 850k, 850l, 899 ZPO; Pfändungsfreigrenzenbekanntmachung |
| `sachpfaendung-vermoegensauskunft` | Gerichtsvollzieherauftrag als Aufklärungsinstrument, Pfändungsverbote, Erzwingung der Auskunft und Verteidigung Dritter | §§ 803, 804, 808, 809, 811, 811a, 758a ZPO; §§ 802b–802l, 882b, 882e ZPO; § 771 ZPO; § 156 StGB |
| `immobiliarvollstreckung-zvg` | Zwangsversteigerung, Zwangsverwaltung und Teilungsversteigerung mit Rang, geringstem Gebot und Wertgrenzen | §§ 10, 15, 20, 27, 30a, 44, 52, 74a, 81, 83, 85a, 91, 96, 146, 180–182 ZVG; § 867 ZPO; §§ 749, 1365, 2042, 2044 BGB |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: ZPO 8. Buch, ZVG, flankierendes BGB, BGH VII. und V. Zivilsenat, Standardkommentare, aktuelle Pfändungsfreigrenzenbekanntmachung
- [`agents/drafter.md`](./agents/drafter.md) – Erstellung von Anträgen, Aufträgen, Erklärungen und Rechtsbehelfsschriftsätzen mit vollständiger Forderungsaufstellung
- [`agents/reviewer.md`](./agents/reviewer.md) – Frist-, Schutz- und Berufsrechts-Check (Trias, § 750 Abs. 2 ZPO, Freigrenzen, Rechtsbehelfszuordnung, Wirtschaftlichkeit)

## Installation

### Claude Code
```bash
# Über Marketplace (empfohlen)
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install zwangsvollstreckung

# Oder als ZIP
# Claude Code → Customize Plugins → Install from .zip → zwangsvollstreckung.zip
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area zwangsvollstreckung --out dist/gemini
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area zwangsvollstreckung --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Vollstreckungsvoraussetzungen und Rechtsbehelf

```
/zwangsvollstreckung:vollstreckungsvoraussetzungen
Inkassogesellschaft vollstreckt aus einem abgetretenen Versäumnisurteil
über 8.500 EUR; die Abtretung ist nur privatschriftlich belegt, Klausel
und Urkunden wurden dem Schuldner nicht vorab zugestellt. Der Schuldner
hat nach Schluss der mündlichen Verhandlung 3.000 EUR gezahlt und ist
gesundheitlich angeschlagen. Bitte Prüfung der Trias und Zuordnung der
Rechtsbehelfe mit Fristen.
```

### Szenario 2 – Lohn- und Kontopfändung

```
/zwangsvollstreckung:forderungspfaendung
Vollstreckungsbescheid über 8.500 EUR Werklohn. Schuldner in Vollzeit
plus Minijob, zwei Kinder, Girokonto noch kein P-Konto. Bitte
PfÜB-Antrag gegen Arbeitgeberin und Bank, Zusammenrechnungsantrag
§ 850e ZPO, Behandlung der Weihnachtsvergütung und Haftung des
Arbeitgebers nach § 840 ZPO.
```

### Szenario 3 – Gerichtsvollzieherauftrag und Drittwiderspruch

```
/zwangsvollstreckung:sachpfaendung-vermoegensauskunft
Urteil über 4.200 EUR gegen einen selbstständigen Monteur. Gepfändet
wurden eine geleaste CNC-Maschine, der für Kundentermine benötigte
Firmenwagen und die Waschmaschine. Vermögensauskunft vor 14 Monaten
abgegeben, neuer Termin unentschuldigt versäumt. Bitte Auftragsmodule,
Prüfung des § 811 ZPO, Haftbefehl und Drittwiderspruch der
Leasinggeberin.
```

### Szenario 4 – Teilungsversteigerung und Abwehr

```
/zwangsvollstreckung:immobiliarvollstreckung-zvg
Getrennt lebender Ehemann beantragt die Teilungsversteigerung des
Familienheims (Verkehrswert 320.000 EUR, praktisch sein gesamtes
Vermögen, keine Zustimmung der Ehefrau). Parallel betreibt eine
nachrangige Gläubigerin die Zwangsversteigerung hinter Grundschulden
über 260.000 EUR. Die Ehefrau hat einen Kaufvertrag über 340.000 EUR.
Bitte § 1365 BGB, geringstes Gebot, Wertgrenzen und § 30a ZVG.
```

## Deterministische Rechner

Die Skills binden `scripts/legal_calc/` ein: Fristen (§§ 187–193 BGB, § 222 ZPO) für § 750 Abs. 2 ZPO, § 845 Abs. 2 ZPO, § 840 ZPO, § 882c ZPO, § 30b ZVG und § 96 ZVG sowie Verzugszinsen (§§ 288, 247 BGB) auf die zugrunde liegende Forderung und RVG/GKG für die Kostenprognose. Der Rechner macht **nur die Arithmetik**; Zugang, Zustellung und Fristbeginn bleiben juristische Eingaben. Details: [`../references/rechner.md`](../references/rechner.md).

> **Die Pfändungsfreigrenzen des § 850c ZPO werden bewusst NICHT berechnet.** Die Tabelle ist in `scripts/legal_calc/` nicht implementiert, und ihre Werte werden jährlich zum 1. Juli angepasst. Maßgeblich ist ausschließlich die aktuelle **Pfändungsfreigrenzenbekanntmachung** nebst Tabelle; der pfändbare Betrag ist dort abzulesen und mit Fassungsdatum zu dokumentieren. Dasselbe gilt für den P-Konto-Grundfreibetrag, für die Wertgrenzen des § 802l ZPO und für den Verkehrswert nach § 74a Abs. 5 ZVG.

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Standardkommentare: **Zöller** ZPO, **Musielak/Voit** ZPO, **Stein/Jonas** ZPO, **Stöber/Rellermeyer** Forderungspfändung, **Stöber** ZVG, **Dassler/Schiffhauer/Hintzen** ZVG, **Böttcher** ZVG, **Kindl/Meller-Hannich** Gesamtes Recht der Zwangsvollstreckung.

Rechtsprechung: BGH VII. Zivilsenat (Zwangsvollstreckung, P-Konto), V. Zivilsenat (ZVG), Landgerichte als Beschwerdegerichte. Format: `BGH, Beschl. v. TT.MM.JJJJ – VII ZB NN/JJ, NJW Jahr, Seite Rn. N`. Verifikation über dejure.org; unverifizierte Zitate tragen `[unverifiziert - prüfen]`.

## Hinweise

- **Titel, Klausel, Zustellung.** Fehlt eines der drei, ist die Vollstreckung angreifbar — unabhängig davon, ob der Anspruch besteht. Die Zwei-Wochen-Frist des § 750 Abs. 2 ZPO bei qualifizierter oder Rechtsnachfolgeklausel ist der am häufigsten übersehene Formfehler.
- **Der richtige Rechtsbehelf entscheidet.** Art und Weise → § 766 ZPO; Klausel formell → § 732 ZPO; materiell → § 767 ZPO; Rechtsnachfolge materiell → § 768 ZPO; Drittrecht → § 771 ZPO; Härte → § 765a ZPO. Der falsch gewählte Rechtsbehelf geht als unzulässig verloren, während die Maßnahme weiterläuft.
- **Der Wert des Gerichtsvollzieherauftrags liegt in der Aufklärung.** Vermögensauskunft § 802c ZPO und Fremdauskünfte § 802l ZPO ermöglichen die anschließende Forderungspfändung; die Sachpfändung selbst bringt selten Erlös.
- **Der Rang entscheidet in der Immobiliarvollstreckung.** Vor jedem ZVG-Antrag ist das geringste Gebot aus dem Grundbuch zu rekonstruieren; ein nachrangiger Gläubiger betreibt sonst ein Verfahren ohne Bieter.
- **Die Wertgrenzen der §§ 74a, 85a ZVG gelten nur im ersten Termin.** Sie verschaffen dem Schuldner eine zweite Chance, keinen dauerhaften Schutz.
- **Teilungsversteigerung braucht keinen Titel** — aber bei Eheleuten die Zustimmung nach § 1365 BGB, wenn das Grundstück nahezu das gesamte Vermögen ausmacht.
- **Mandantengeheimnis (§ 43a BRAO, § 203 StGB):** Keine echten Schuldnerdaten, Kontonummern oder Vermögensverzeichnisse ohne § 203-konformen Gateway.
