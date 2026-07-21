# Deterministische Rechner (`scripts/legal_calc/`)

Manche juristischen Aufgaben sind reine Arithmetik mit gesetzlich definierter
Formel - und genau dort halluzinieren Sprachmodelle. Diese Rechner führen die
Rechnung **deterministisch** aus, ohne Modellaufruf. Die rechtliche Wertung
(Anspruchsart, Kenntniszeitpunkt, einschlägiges Bundesland) bleibt vorgelagerte
Eingabe; der Rechner macht nur die Mathematik.

> Hilfsmittel, keine Rechtsberatung. Jedes Ergebnis vor der Verwendung gegen die
> einschlägige Norm und die **aktuelle** Gebührentabelle prüfen.

## Module

| Modul | Norm | Was es rechnet |
|---|---|---|
| `feiertage.py` | Feiertagsgesetze der Länder | Gesetzliche Feiertage je Jahr und Bundesland (Ostern via Gauß-Algorithmus, alle beweglichen Feste) |
| `fristen.py` | §§ 187-193 BGB, § 222 ZPO | Fristende mit Ereignis-/Beginnfrist, Monatsende-Überlauf (§ 188 III), §-193-Verschiebung auf den nächsten Werktag |
| `verjaehrung.py` | §§ 195-199, 196, 197 BGB | Regelverjährung (Ultimo-Regel), kenntnisunabhängige Höchstfristen, früheste Frist bei Schadensersatz |
| `rvg.py` | § 13 RVG + Anlage 2, VV RVG | Anwaltsgebühren: 1,0-Gebühr (Aufrundung auf die Wertstufe), Gebührensätze, Auslagenpauschale VV 7002, USt VV 7008 |
| `gkg.py` | § 34 GKG + Anlage 2, KV GKG | Gerichtskosten: 1,0-Gebühr, Verfahrenssatz (3,0 erste Instanz usw.) |
| `kuendigungsfristen.py` | § 622 BGB | Kündigungsfrist im Arbeitsverhältnis: Grundfrist (4 Wochen zum 15./Monatsende), Stufen des Abs. 2 nach vollendeten Beschäftigungsjahren, Probezeit Abs. 3, frühestmöglicher Beendigungstermin |
| `verzugszinsen.py` | §§ 288, 247 BGB | Verzugszinsen: 5 oder 9 Prozentpunkte über Basiszinssatz, Segmentierung bei Basiszins-Wechsel, Pauschale § 288 Abs. 5 BGB |

## CLI

```bash
# Fristen
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 3 --einheit wochen --land BY
python -m scripts.legal_calc.cli frist --ereignis 31.01.2026 --menge 1 --einheit monate

# Verjährung
python -m scripts.legal_calc.cli verjaehrung --entstehung 10.03.2023 --kenntnis 05.07.2023
python -m scripts.legal_calc.cli verjaehrung --entstehung 10.05.2020 --kenntnis 01.01.2028 --begehung 10.05.2020

# Gebühren / Kosten
python -m scripts.legal_calc.cli rvg --wert 10000 --posten verfahren termin
python -m scripts.legal_calc.cli gkg --wert 10000 --faktor 3.0

# Feiertage
python -m scripts.legal_calc.cli feiertage --jahr 2026 --land BY

# Kündigungsfrist § 622 BGB
python -m scripts.legal_calc.cli kuendigungsfrist --eintritt 01.03.2014 --zugang 20.07.2026
python -m scripts.legal_calc.cli kuendigungsfrist --eintritt 01.02.2026 --zugang 05.04.2026 --probezeit
python -m scripts.legal_calc.cli kuendigungsfrist --eintritt 01.03.2014 --zugang 20.07.2026 --kuendigender arbeitnehmer

# Verzugszinsen §§ 288, 247 BGB (Basiszinssatz ist Pflichteingabe, mehrfach angebbar)
python -m scripts.legal_calc.cli verzugszinsen --betrag 12500 \
    --verzug-ab 15.03.2025 --bis 21.07.2026 \
    --basiszins 01.01.2025:1.27 --basiszins 01.07.2025:1.30 --basiszins 01.01.2026:1.10 \
    --entgeltforderung --kein-verbraucher-beteiligt
```

## Zwei bewusste Konstruktionsentscheidungen

**Der Basiszinssatz wird nicht im Code vorgehalten.** Er ändert sich nach § 247
Abs. 1 BGB zum 1.1. und 1.7. jedes Jahres. Ein fest verdrahteter Wert würde nach
dem nächsten Stichtag stillschweigend falsche Ergebnisse liefern. Der Satz ist
daher **Pflichteingabe**; erstreckt sich der Zinslauf über einen Wechsel, wird
segmentweise gerechnet. Die in den Beispielen genannten Werte sind Platzhalter
und **gegen die Veröffentlichung der Deutschen Bundesbank zu prüfen**.

**§ 622 Abs. 2 S. 2 BGB wird bewusst nicht angewendet.** Der Wortlaut lässt
Beschäftigungszeiten vor Vollendung des 25. Lebensjahres außer Betracht. Der
EuGH hat eine entsprechende Regelung als Altersdiskriminierung beanstandet
(Rs. C-555/07, Kücükdeveci `[unverifiziert - prüfen]`); deutsche Gerichte wenden
sie nicht an. Der Rechner zählt diese Zeiten daher **standardmäßig mit**. Das
Gegenverhalten ist nur zur Abbildung des Gesetzeswortlauts verfügbar und trägt
im Ergebnis einen ausdrücklichen Warnhinweis.

`--json` an jedes Subkommando anhängen für maschinenlesbare Ausgabe. Jedes
Ergebnis enthält die Rechenschritte mit Normzitat, damit die Herleitung
nachvollziehbar ist (nicht nur das Datum/der Betrag).

## Versionierung der Gebührentabellen

Die RVG-/GKG-Beträge ändern sich durch Gesetz (zuletzt KostBRÄG 2025, in Kraft
seit 01.06.2025). Die 1,0-Gebühr-Tabellen liegen daher als versionierte
JSON-Dateien in `scripts/legal_calc/data/` mit den Feldern:

- `stand` - Inkrafttreten der eingetragenen Werte,
- `verifiziert` - ob gegen die amtliche Quelle geprüft,
- `_geprueft_am` / `_geprueft_gegen` - Prüfdatum und -quelle.

Die Ausgabe nennt den `stand` mit. **Vor jeder Reform die Tabellen aktualisieren**
und `stand`/`verifiziert` neu setzen. Die Tests prüfen nur die Struktur
(aufsteigende Wertstufen, monoton steigende Gebühren), nicht die konkreten
Beträge - die Beträge sind durch die amtliche Anlage 2 zu belegen.

## Grenzen / bewusst nicht automatisiert

- **Feiertage:** gemeindeabhängige Tage (Mariä Himmelfahrt in BY, Fronleichnam in
  Teilen von SN/TH) werden **nicht** landesweit gezählt; `gemeinde_hinweis()`
  warnt. Augsburger Friedensfest ist außerhalb des Umfangs.
- **§ 193 BGB bei Verjährung:** nach h.M. **nicht** anwendbar - die Verjährung
  läuft auch an einem Sa/So/Feiertag ab. Der Rechner verschiebt hier nicht.
- **Hemmung/Neubeginn** (§§ 203 ff., 212 BGB) sind fallabhängig und nicht
  eingebaut - ggf. einen angepassten Fristbeginn eingeben.
- **Streitwert nach § 3 ZPO / § 48 Abs. 2 GKG** (freies Ermessen, z.B.
  einstweilige Verfügung, Feststellungsklage) ist nicht automatisierbar; nur
  bezifferte und gesetzlich definierte Werte (§ 9 ZPO usw.) sind sichere Eingabe.
- **GKG-Ermäßigung KV 1211** (1,0 statt 3,0 bei früher Verfahrensbeendigung) ist
  über den `--faktor` explizit anzugeben.

## Tests

```bash
python -m unittest scripts.legal_calc.tests
```

Fixtures sind aus den Normen von Hand gerechnet (Klagefrist § 4 KSchG,
Monatsfrist-Überlauf, Lebensalter-Beginnfrist, Ultimo-Verjährung u.a.).
