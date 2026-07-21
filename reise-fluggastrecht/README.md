# Reise- und Fluggastrecht

**Production-grade Reiserechts-Skills für Claude / Gemini / GPT.** Fluggastrechte nach VO (EG) 261/2004, Pauschalreiserecht der §§ 651a ff. BGB, Rücktritt und Insolvenzabsicherung sowie die Abgrenzung Reiseveranstalter / Reisevermittler. Researcher → Drafter → Reviewer.

> Dieses Gebiet ist der am stärksten automatisierte Massenanspruchsmarkt in Deutschland. Der Automatisierungsgrad ist zugleich das Risiko: Ausgleichsforderungen werden serienweise ohne Prüfung von Anwendungsbereich, außergewöhnlichen Umständen und Verjährung versandt. Die Skills erzwingen deshalb jeweils eine **vollständige Anspruchsprüfung vor dem Textbaustein**.

## Skills in dieser Version

| Skill | Funktion | Statutory anchors |
|---|---|---|
| `fluggastrechte-vo-261` | Ausgleichs-, Betreuungs- und Erstattungsansprüche gegen das ausführende Luftfahrtunternehmen, einschließlich Zuständigkeit und Verjährung | Art. 3, 4, 5, 6, 7, 8, 9, 12 VO (EG) 261/2004; Art. 7 Nr. 1 EuGVVO; §§ 195, 199 BGB; § 29 ZPO |
| `pauschalreise-maengel` | Mängelrechte des Reisenden nach Reiseantritt: Abhilfe, Minderung, Kündigung, Schadensersatz und entgangene Urlaubsfreude | §§ 651a, 651i, 651k, 651l, 651m, 651n, 651j BGB; Art. 250 EGBGB |
| `reiseruecktritt-insolvenzschutz` | Rücktritt vor Reisebeginn, unvermeidbare außergewöhnliche Umstände, Preiserhöhung und Insolvenzabsicherung | §§ 651f, 651g, 651h, 651r, 651s, 651t BGB; RSFG |
| `reisevermittlung-informationspflichten` | Rollenabgrenzung, vorvertragliche Information, Buchungsfehlerhaftung und das ausgeschlossene Widerrufsrecht | §§ 651a Abs. 2, 651v, 651w BGB; Art. 250, 251 EGBGB; § 312g Abs. 2 Nr. 9 BGB |

## Sub-Agenten

- [`agents/researcher.md`](./agents/researcher.md) – Quellenrecherche: VO (EG) 261/2004, §§ 651a ff. BGB, Art. 250 EGBGB, EuGH-Rechtsprechung, BGH X. Zivilsenat, Standardkommentare
- [`agents/drafter.md`](./agents/drafter.md) – Entwürfe: Ausgleichsforderung an die Airline, Mängelanzeige, Minderungsberechnung, Rücktrittserklärung, Klageschrift
- [`agents/reviewer.md`](./agents/reviewer.md) – Verjährungs-, Zuständigkeits-, Quellen- und Berufsrechts-Check (§§ 195, 199 BGB; § 651j BGB; Art. 7 Nr. 1 EuGVVO)

## Installation

### Claude Code
```bash
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install reise-fluggastrecht
```

### Gemini Gems
```bash
python ../scripts/route_provider.py --provider gemini --area reise-fluggastrecht --out dist/gemini
```

### OpenAI Custom GPTs / Assistants
```bash
python ../scripts/route_provider.py --provider openai --area reise-fluggastrecht --out dist/openai
```

## Anwendungsbeispiele

### Szenario 1 – Ausgleichszahlung nach großer Verspätung

```
/reise-fluggastrecht:fluggastrechte-vo-261
Mandantin flog Frankfurt – Singapur mit Umsteigen in Dubai, einheitliche
Buchung bei einer Nicht-EU-Airline. Der Zubringer ab Frankfurt startete
mit 100 Minuten Verspätung; der Anschluss wurde verpasst, Ankunft am
Endziel 5 Stunden 20 Minuten später. Die Airline beruft sich auf ein
Gewitter in Dubai. Frage: Anspruchshöhe, außergewöhnliche Umstände,
Gerichtsstand, Verjährung.
```

### Szenario 2 – Pauschalreise mit erheblichen Mängeln

```
/reise-fluggastrecht:pauschalreise-maengel
Mandanten buchten eine 14-tägige Pauschalreise. Vor Ort: anderes Hotel
als gebucht, Baulärm von 7 bis 18 Uhr, Pool sechs Tage gesperrt,
Klimaanlage defekt. Die Reiseleitung wurde am dritten Tag informiert,
Abhilfe erfolgte nicht. Bitte Minderungsquote, Schadensersatz und
entgangene Urlaubsfreude prüfen.
```

### Szenario 3 – Rücktritt vor Reisebeginn

```
/reise-fluggastrecht:reiseruecktritt-insolvenzschutz
Mandant hat eine Pauschalreise ins Zielgebiet gebucht. Drei Wochen vor
Abreise treten dort Unruhen auf; das Auswärtige Amt spricht eine
Reisewarnung aus. Der Veranstalter verlangt 60 % Entschädigung.
Frage: kostenfreier Rücktritt nach § 651h Abs. 3 BGB?
```

## Quellen und Zitierweise

Verbindlich: [`../references/zitierweise.md`](../references/zitierweise.md). Standardkommentare: **Führich**, Reiserecht; **Staudinger/Keiler**, Fluggastrechte-Verordnung; **Tonner**, in: MüKo-BGB, §§ 651a ff.; **Steinrötter**, in: BeckOGK BGB; **Bergmann/Blankenburg**, Fluggastrechte.

Rechtsprechung: **EuGH** (Auslegung der VO 261/2004 und der Pauschalreise-RL (EU) 2015/2302), **BGH X. Zivilsenat** (Reisesenat), Instanzgerichte. Format: `EuGH, Urt. v. TT.MM.JJJJ – C-NNN/JJ, NJW Jahr, Seite`. Unverifizierte Zitate werden mit `[unverifiziert - prüfen]` markiert.

## Hinweise

- **Die Frankfurter Tabelle ist kein Gesetz.** Sie ist eine 1985 vom LG Frankfurt am Main veröffentlichte Orientierungshilfe ohne jede Bindungswirkung. Sie darf im Mandantenschreiben genannt, aber niemals als Rechtsgrundlage der Minderung ausgewiesen werden. Rechtsgrundlage ist allein [§ 651m BGB](https://www.gesetze-im-internet.de/bgb/__651m.html).
- **Widerrufsrecht.** [§ 312g Abs. 2 Nr. 9 BGB](https://www.gesetze-im-internet.de/bgb/__312g.html) schließt das Widerrufsrecht für Beförderungs- und Beherbergungsleistungen zu bestimmten Terminen weitgehend aus. Der Rat, eine online gebuchte Reise „einfach zu widerrufen", ist der häufigste Beratungsfehler des Gebiets.
- **Verjährung.** Ausgleichsansprüche nach der VO 261/2004 verjähren nach nationalem Recht, in Deutschland nach [§§ 195, 199 BGB](https://www.gesetze-im-internet.de/bgb/__199.html) in drei Jahren ab Schluss des Entstehungsjahres. Reisevertragliche Ansprüche verjähren nach [§ 651j BGB](https://www.gesetze-im-internet.de/bgb/__651j.html) in zwei Jahren.
- **Mandantengeheimnis (§ 43a Abs. 2 BRAO, § 203 StGB):** Buchungsnummern, Bordkarten und Passdaten sind personenbezogene Daten; keine Verarbeitung ohne AVV.
