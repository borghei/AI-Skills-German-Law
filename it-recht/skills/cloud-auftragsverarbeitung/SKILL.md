---
name: cloud-auftragsverarbeitung
description: "Datenschutzkonforme Gestaltung der Cloud-Nutzung: Auftragsverarbeitung nach Art. 28 DSGVO, technische und organisatorische Maßnahmen nach Art. 32 DSGVO und Drittlandtransfer nach Kapitel V DSGVO (Art. 44 ff.). Use when ein Cloud- oder SaaS-Dienst eingesetzt wird und der AVV sowie der Datentransfer geprüft oder gestaltet werden sollen."
language: de
provider_variants: [claude, gemini, openai]
test: ./test.md
---

# /it-recht:cloud-auftragsverarbeitung

## Zweck

Wer einen Cloud-Dienst nutzt, lässt regelmäßig personenbezogene Daten durch den Anbieter verarbeiten und bleibt als Verantwortlicher in der Pflicht. Dieser Skill prüft die drei kritischen Achsen einer datenschutzkonformen Cloud-Nutzung: den Auftragsverarbeitungsvertrag (**Art. 28 DSGVO**), die Sicherheit der Verarbeitung (**Art. 32 DSGVO**) und die Zulässigkeit des Datentransfers in Drittländer (**Art. 44 DSGVO** ff., Kapitel V). Er deckt Lücken auf, bevor sie zum Bußgeldfall werden, und verzahnt sich mit dem AVV-Prüfskill des Datenschutzbereichs.

## Eingaben

- Cloud-Modell (IaaS, PaaS, SaaS) und Anbieter
- Verarbeitete Datenkategorien (Standard, besondere Kategorien Art. 9, Beschäftigtendaten)
- Standort der Verarbeitung / Speicherung (EU, USA, sonstiges Drittland)
- Konzernzugehörigkeit des Anbieters (US-Mutter? Cloud Act-Zugriff?)
- Vorliegender AVV-Entwurf und Liste der Sub-Auftragsverarbeiter
- Vorhandene TOM-Dokumentation, Zertifikate (ISO 27001, C5)

## Sub-Agent-Architektur

Die Prüfung verteilt sich gedanklich auf drei Rollen. Ein **AVV-Agent** prüft den Auftragsverarbeitungsvertrag gegen den Pflichtenkatalog des Art. 28 Abs. 3 DSGVO (Gegenstand, Dauer, Weisungsbindung, Sub-Auftragsverarbeiter, Unterstützungspflichten, Löschung, Audit). Ein **TOM-Agent** bewertet die technischen und organisatorischen Maßnahmen nach Art. 32 DSGVO (Verschlüsselung, Pseudonymisierung, Verfügbarkeit, Belastbarkeit, regelmäßige Überprüfung) und gleicht sie mit dem Risiko der Datenkategorien ab. Ein **Transfer-Agent** prüft jeden Drittlandbezug nach Kapitel V (Angemessenheitsbeschluss, Standardvertragsklauseln, Transfer Impact Assessment, ergänzende Maßnahmen). Die Rollen melden ihre Befunde an eine zusammenführende Bewertung; ein Mangel auf einer Achse blockiert die Konformität insgesamt. Rechtsprechung und Aufsichtsbeschlüsse werden nur verifiziert zitiert, sonst mit `[unverifiziert – prüfen]` markiert.

## Ablauf

### 1. Rollen- und Anwendbarkeitsklärung

- Liegt Auftragsverarbeitung vor (weisungsgebundene Verarbeitung) oder gemeinsame Verantwortlichkeit (Art. 26) oder eigene Verantwortlichkeit des Anbieters?
- Nur bei Auftragsverarbeitung ist ein AVV nach Art. 28 DSGVO der richtige Vertragstyp.

### 2. AVV-Inhaltskontrolle (Art. 28 DSGVO)

Pflichtinhalte nach Art. 28 Abs. 3 DSGVO:

- Gegenstand, Dauer, Art und Zweck der Verarbeitung, Datenkategorien, Betroffenenkreis
- Verarbeitung nur auf dokumentierte Weisung
- Vertraulichkeitsverpflichtung der Beschäftigten
- Maßnahmen nach **Art. 32 DSGVO**
- Genehmigung und Verträge mit Sub-Auftragsverarbeitern (Art. 28 Abs. 2, 4)
- Unterstützung bei Betroffenenrechten und bei Art. 32–36
- **Löschung** oder Rückgabe der Daten nach Vertragsende
- Nachweis- und **Audit**-Rechte des Verantwortlichen

### 3. Technische und organisatorische Maßnahmen (Art. 32 DSGVO)

- Verschlüsselung (Transport und Ruhe), Pseudonymisierung
- Sicherstellung von Vertraulichkeit, Integrität, Verfügbarkeit, Belastbarkeit
- Wiederherstellbarkeit nach Zwischenfall; regelmäßiges Testen
- Risikoangemessenheit insb. bei besonderen Datenkategorien (Art. 9)

### 4. Drittlandtransfer (Kapitel V, Art. 44 DSGVO ff.)

- **Angemessenheitsbeschluss** (Art. 45) — z. B. EU-US Data Privacy Framework für zertifizierte US-Anbieter
- **Standardvertragsklauseln** (Art. 46) + **Transfer Impact Assessment** + ggf. ergänzende Maßnahmen (Schrems II)
- Zugriffsrisiken durch Drittstaatsbehörden (Cloud Act) bewerten
- Sub-Auftragsverarbeiter in Drittländern gesondert absichern

### 5. Dokumentation und Rechenschaft

- Eintrag im Verzeichnis von Verarbeitungstätigkeiten (Art. 30)
- Datenschutz-Folgenabschätzung (Art. 35) bei hohem Risiko

## Risiken / typische Fehler

- **Fehlender AVV** — Cloud-Nutzung ohne AVV nach Art. 28 DSGVO ist ein eigenständiger Verstoß; Bußgeldrisiko nach Art. 83 DSGVO.
- **Drittlandtransfer** ohne tragfähige Grundlage — US-Anbieter ohne DPF-Zertifizierung oder ohne Standardvertragsklauseln samt TIA verletzt Kapitel V (Art. 44 DSGVO).
- **Sub-Auftragsverarbeiter** ungeprüft — fehlende Genehmigung oder Weiterreichung der Pflichten verletzt Art. 28 Abs. 4 DSGVO.
- **Bußgeld** — unzureichende Maßnahmen nach Art. 32 DSGVO oder unzulässiger Transfer können Bußgelder bis 20 Mio. EUR / 4 % auslösen (Art. 83 DSGVO).

## Ausgabeformat

```
CLOUD-AUFTRAGSVERARBEITUNG — <Dienst / Anbieter> — <Datum>

I.    Rolle:                      [Auftragsverarbeitung / gem. Verantwortl. / eigen]
II.   AVV (Art. 28 DSGVO)
      Vollständigkeit:            [✓ / 🔴 lückenhaft]   Fehlend: <…>
      Sub-Auftragsverarbeiter:    [genehmigt / ungeregelt]
      Audit / Löschung:           [✓ / 🔴]
III.  TOM (Art. 32 DSGVO)
      Verschlüsselung / Risiko:   [angemessen / ⚠️]
IV.   Drittlandtransfer (Art. 44 DSGVO)
      Standort:                   [EU / USA / Drittland]
      Grundlage:                  [Angemessenheit / SCC + TIA / 🔴 keine]
V.    Dokumentation
      VVT / DSFA:                 [✓ / offen]

Bußgeldrisiko (Art. 83 DSGVO):    <Einschätzung>
Handlungsempfehlung:              <…>
```

## Quellen

- [Art. 28 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679) (Auftragsverarbeiter)
- [Art. 32 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679) (Sicherheit der Verarbeitung)
- [Art. 44 DSGVO ff. — Kapitel V](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679) (Drittlandtransfer), Art. 45, 46
- [Art. 83 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679) (Geldbußen)
- EU-US Data Privacy Framework; EDSA-Empfehlungen 01/2020 (ergänzende Maßnahmen) `[unverifiziert – prüfen]`
