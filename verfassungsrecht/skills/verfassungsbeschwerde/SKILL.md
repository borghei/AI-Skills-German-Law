---
name: verfassungsbeschwerde
description: "Zulässigkeits- und Begründetheitsprüfung einer Verfassungsbeschwerde nach Art. 93 I Nr. 4a GG, §§ 90 ff. BVerfGG inklusive Schriftsatzentwurf. Use when ein Mandant gegen einen Hoheitsakt (Gesetz, Verwaltungsakt, fachgerichtliches Urteil) eine Grundrechtsverletzung rügen möchte oder ein bereits eingegangener Beschwerdeentwurf auf Zulässigkeit geprüft werden soll."
language: de
agents:
  researcher: ../agents/researcher.md
  drafter: ../agents/drafter.md
  reviewer: ../agents/reviewer.md
provider_variants:
  - claude
  - gemini
  - openai
test: ./test.md
---

# /verfassungsrecht:verfassungsbeschwerde

## Zweck

Die Verfassungsbeschwerde nach Art. 93 Abs. 1 Nr. 4a GG, §§ 90 ff. BVerfGG ist der subsidiäre außerordentliche Rechtsbehelf zur Durchsetzung von Grundrechten und grundrechtsgleichen Rechten. Die meisten Verfassungsbeschwerden scheitern in der **Zulässigkeit** — Subsidiarität, Frist, Begründungsanforderungen. Dieser Skill prüft jede der sieben Zulässigkeitsstufen, sodann die Begründetheit (Grundrechtsprüfung) und stellt einen Schriftsatzentwurf bereit.

## Eingaben

- gerügter Hoheitsakt (Gesetz / Verwaltungsakt / Urteil) inkl. Datum und ausstellender Stelle
- gerügtes Grundrecht oder grundrechtsgleiches Recht (Art. 1–19 GG, Art. 20 Abs. 4, Art. 33, 38, 101, 103, 104 GG)
- Verfahrensstand der Fachgerichte (Instanzenzug, letzte Entscheidung, Zustelldatum)
- Beschwerdeführer (natürliche/juristische Person, Sitz/Staatsangehörigkeit)
- ggf. Eilbedürftigkeit (§ 32 BVerfGG)

## Sub-Agent-Architektur

Researcher liefert Statute und BVerfG-Rechtsprechung zu Zulässigkeit und einschlägigem Grundrecht. Drafter erstellt Zulässigkeits- und Begründetheitsprüfung im Gutachtenstil sowie den Schriftsatzentwurf im Urteilsstil mit Anträgen. Reviewer prüft Frist (§ 93 BVerfGG), Substantiierung, Subsidiarität und Annahmevoraussetzungen.

## Ablauf

### 1. Zulässigkeit (§§ 90 ff. BVerfGG)

| Stufe | Maßstab |
|---|---|
| **Beschwerdefähigkeit** | „Jedermann", Art. 19 Abs. 3 GG bei juristischen Personen des Privatrechts; juristische Personen des öffentlichen Rechts grundsätzlich nicht (Ausnahmen: Rundfunkanstalten, Universitäten, Religionsgemeinschaften — vgl. [BVerfGE 21, 362](https://www.servat.unibe.ch/dfr/bv021362.html)) |
| **Beschwerdegegenstand** | Akt der öffentlichen Gewalt (Legislative, Exekutive, Judikative) |
| **Beschwerdebefugnis** | Selbst, gegenwärtig, unmittelbar betroffen + substantiierte Möglichkeit einer Grundrechtsverletzung (§§ 23 Abs. 1, 92 BVerfGG) |
| **Rechtswegerschöpfung** | § 90 Abs. 2 S. 1 BVerfGG: fachgerichtlicher Rechtsweg vollständig durchschritten |
| **Subsidiarität (i.w.S.)** | Auch außerhalb des Rechtswegs zumutbare Abhilfen ausgeschöpft (Anhörungsrüge § 152a VwGO / § 321a ZPO, Gegenvorstellung, fachgerichtliche Tatsachenklärung) |
| **Frist** | Monatsfrist § 93 Abs. 1 BVerfGG bei Urteilen / belastenden Hoheitsakten; Jahresfrist § 93 Abs. 3 BVerfGG bei Gesetzen |
| **Form** | Schriftform, Begründung mit Bezeichnung des gerügten Rechts und des Hoheitsakts (§§ 23, 92 BVerfGG) |

Annahmeverfahren: **§ 93a Abs. 2 BVerfGG** — grundsätzliche verfassungsrechtliche Bedeutung **oder** Annahme zur Durchsetzung der in § 90 Abs. 1 BVerfGG genannten Rechte angezeigt (insbes. besonders schwerer Nachteil).

### 2. Begründetheit — Grundrechtsprüfung

Die Verfassungsbeschwerde ist begründet, wenn der angegriffene Hoheitsakt den Beschwerdeführer in einem Grundrecht oder grundrechtsgleichen Recht verletzt. Prüfung nach dem 3-Stufen-Schema (siehe `/verfassungsrecht:grundrechtspruefung`): Schutzbereich → Eingriff → Verfassungsrechtliche Rechtfertigung.

Besonderheit Urteilsverfassungsbeschwerde: BVerfG prüft nicht jeden einfachgesetzlichen Fehler, sondern nur die Verletzung **spezifischen Verfassungsrechts** (sog. Heck'sche Formel — [BVerfGE 18, 85](https://www.servat.unibe.ch/dfr/bv018085.html)).

### 3. Einstweilige Anordnung (§ 32 BVerfGG)

Wenn Eilbedürftigkeit vorliegt: gesonderter Antrag. Doppelhypothetische Folgenabwägung — BVerfG wägt Nachteile bei Erlass / Nichterlass ohne Vorgriff auf die Hauptsache.

### 4. Bindungswirkung der Entscheidung

§ 31 BVerfGG ist die **gesetzliche Ausnahme** vom Grundsatz „keine Präjudizienbindung": tragende Gründe binden alle Verfassungsorgane sowie alle Gerichte und Behörden; Entscheidungen nach § 13 Nr. 6, 6a, 11, 12, 14 BVerfGG haben Gesetzeskraft.

### 5. Personalakte / interne Dokumentation

Fristenkalender mit Wiedervorlage 7 Tage vor Ablauf der Monatsfrist § 93 Abs. 1 BVerfGG. Zustellurkunde der letzten fachgerichtlichen Entscheidung im Original sichern.

## Quellen und Zitierweise

Verbindlich: [`../../references/zitierweise.md`](../../references/zitierweise.md).

### Statute

- [Art. 93 Abs. 1 Nr. 4a GG](https://www.gesetze-im-internet.de/gg/art_93.html) (Verfassungsbeschwerde)
- [Art. 5 Abs. 1 GG](https://www.gesetze-im-internet.de/gg/art_5.html) (Meinungs-/Pressefreiheit – häufig gerügtes Grundrecht bei Urteilsverfassungsbeschwerden)
- [§ 90 BVerfGG](https://www.gesetze-im-internet.de/bverfgg/__90.html) (Beschwerdebefugnis, Rechtswegerschöpfung)
- [§ 92 BVerfGG](https://www.gesetze-im-internet.de/bverfgg/__92.html) (Begründung)
- [§ 93 BVerfGG](https://www.gesetze-im-internet.de/bverfgg/__93.html) (Frist)
- [§ 93a BVerfGG](https://www.gesetze-im-internet.de/bverfgg/__93a.html) (Annahmeverfahren)
- [§ 31 BVerfGG](https://www.gesetze-im-internet.de/bverfgg/__31.html) (Bindungswirkung, Gesetzeskraft)
- [§ 32 BVerfGG](https://www.gesetze-im-internet.de/bverfgg/__32.html) (einstweilige Anordnung)
- [§ 23 BVerfGG](https://www.gesetze-im-internet.de/bverfgg/__23.html) (Schriftform)

### Kommentare

- Bethge, in: Maunz/Schmidt-Bleibtreu/Klein/Bethge, BVerfGG, Loseblatt (Stand: aktuelle Lieferung), § 90 Rn. 1 ff.
- Sperlich, in: Umbach/Clemens/Dollinger, BVerfGG, 2. Aufl. 2005, § 90 Rn. 1 ff.
- Bethge, in: Maunz/Schmidt-Bleibtreu/Klein/Bethge, BVerfGG, § 93 Rn. 1 ff. (Frist)
- Schlaich/Korioth, Das Bundesverfassungsgericht, 12. Aufl. 2021, Rn. 198 ff. (Verfassungsbeschwerde)

### Rechtsprechung

1. BVerfG, Urt. v. 15.01.1958 – 1 BvR 400/51, [BVerfGE 7, 198](https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/1958/01/rs19580115_1bvr040051.html) („Lüth", mittelbare Drittwirkung, Wechselwirkungslehre)
2. BVerfG, Beschl. v. 10.06.1964 – 1 BvR 37/63, [BVerfGE 18, 85](https://www.servat.unibe.ch/dfr/bv018085.html) („Heck'sche Formel", Prüfungsumfang Urteilsverfassungsbeschwerde)
3. BVerfG, [BVerfGE 90, 22](https://www.servat.unibe.ch/dfr/bv090022.html) (Annahmeverfahren § 93a BVerfGG) `[Datum/Aktenzeichen unverifiziert – prüfen]`
4. BVerfG, [BVerfGE 26, 246](https://www.servat.unibe.ch/dfr/bv026246.html) (Subsidiarität / Ingenieurgesetz) `[Datum/Aktenzeichen unverifiziert – prüfen]`

## Ausgabeformat

```
GUTACHTEN VERFASSUNGSBESCHWERDE
<Datum> — <Skill-Mandat-ID>

A. Sachverhalt
   <knapp, anonymisiert>

B. Frage
   Ist eine Verfassungsbeschwerde des/der … gegen <Hoheitsakt> zulässig
   und begründet?

C. Kurzantwort
   <1 Satz>

D. Zulässigkeit
   I.   Beschwerdefähigkeit (§ 90 I BVerfGG)
   II.  Beschwerdegegenstand
   III. Beschwerdebefugnis (selbst/gegenwärtig/unmittelbar; Möglichkeit
        einer Grundrechtsverletzung, §§ 23 I, 92 BVerfGG)
   IV.  Rechtswegerschöpfung (§ 90 II 1 BVerfGG)
   V.   Subsidiarität i.w.S.
   VI.  Frist (§ 93 I bzw. III BVerfGG)
   VII. Form (§§ 23 I, 92 BVerfGG)
   VIII.Annahmevoraussetzungen (§ 93a II BVerfGG)

E. Begründetheit
   I.   Schutzbereich Art. … GG
   II.  Eingriff
   III. Verfassungsrechtliche Rechtfertigung
        1. Schranken
        2. Schranken-Schranken (insb. Verhältnismäßigkeit)

F. Ergebnis
   <Zulässigkeit ✅/❌; Begründetheit ✅/❌; Annahmeprognose>

G. Risiken / offene Punkte
   - Fristanker: Zustellung am <Datum>? bestätigen
   - Subsidiarität: Anhörungsrüge erhoben?
   - Beschwerdebefugnis bei Gesetzen: unmittelbare Betroffenheit?

H. Quellenverzeichnis

— — —

SCHRIFTSATZ AN DAS BUNDESVERFASSUNGSGERICHT (Entwurf)

An das Bundesverfassungsgericht
Schlossbezirk 3
76131 Karlsruhe

In dem Verfassungsbeschwerdeverfahren des/der
   <Beschwerdeführer>

gegen
   <Hoheitsakt + Aussteller + Datum + Az.>

wegen Verletzung des/der Art. … GG

stelle ich namens und in Vollmacht des Beschwerdeführers folgende Anträge:

1. Es wird festgestellt, dass <Hoheitsakt> den Beschwerdeführer in seinem
   Grundrecht aus Art. … GG verletzt.
2. <Hoheitsakt> wird aufgehoben / das Verfahren an das <Fachgericht>
   zurückverwiesen.
3. ggf.: Es wird der Erlass einer einstweiligen Anordnung gemäß § 32
   BVerfGG beantragt.

Begründung:
A. Sachverhalt
B. Zulässigkeit
C. Begründetheit
D. Anlagen (letzte fachgerichtliche Entscheidung mit Zustellurkunde,
   Vollmacht, ggf. weitere Belege)
```

## Risiken / typische Fehler

- **Frist versäumt** (§ 93 Abs. 1 BVerfGG) — häufigster Verwerfungsgrund. Zustelldatum sichern.
- **Subsidiarität nicht beachtet** — Anhörungsrüge nach § 321a ZPO / § 152a VwGO als zumutbare Abhilfe vergessen.
- **Substantiierung unzureichend** (§§ 23, 92 BVerfGG) — gerügtes Grundrecht und Möglichkeit der Verletzung müssen aus dem Schriftsatz selbst hervorgehen.
- **Beschwerdebefugnis bei Gesetzen** — unmittelbare Betroffenheit fehlt häufig, weil noch Vollzugsakt zwischengeschaltet ist.
- **Argumentation mit „BVerfG hat entschieden, also gilt"** ohne § 31 BVerfGG — Präjudizienbindung gibt es nur dort.
- **Annahmeverfahren § 93a BVerfGG nicht angesprochen** — auch zulässige Beschwerden werden nicht zur Entscheidung angenommen, wenn keine verfassungsrechtliche Bedeutung und kein besonders schwerer Nachteil dargelegt sind.
