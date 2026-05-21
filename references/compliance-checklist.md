# Compliance-Checkliste vor Produktivnutzung

Diese Checkliste ist **keine Rechtsberatung**. Sie listet Pflichten, die jede Kanzlei/Rechtsabteilung vor Einsatz dieses Skill-Repositorys eigenständig prüfen muss.

## I. Mandatsgeheimnis (§§ 203, 204 StGB; § 43e BRAO; § 2 BORA)

- [ ] Liegt ein schriftlicher Vertrag mit dem KI-Anbieter vor, der § 203 StGB-Verschwiegenheit zusagt (§ 203 Abs. 4 StGB)? — Anthropic, Google und OpenAI unterzeichnen diese Erklärung gegenüber deutschen Rechtsanwälten Stand 2026 **nicht direkt**. Routing über deutschen Zwischenanbieter (Langdock, deepset, etc.) ist der etablierte Workaround.
- [ ] Sind die Pflichten nach § 43e Abs. 4 BRAO (besondere Verschwiegenheitsverpflichtung der bei Dienstleister tätigen Personen) vertraglich abgedeckt?
- [ ] Sind die Mitwirkenden des Anbieters auf § 203 Abs. 3, 4 StGB hingewiesen (sonstige Stellen)?
- [ ] Liegt eine Belehrung zum Mandatsgeheimnis als Anlage zum Vertrag vor?
- [ ] Sind technische Schutzmaßnahmen (kein Training auf Mandatsdaten, kein Logging im Klartext, Verschlüsselung in Transit und at Rest) explizit vertraglich zugesichert?

## II. DSGVO / BDSG

- [ ] Auftragsverarbeitungsvertrag (Art. 28 DSGVO) liegt vor — auch mit ggf. zwischengeschaltetem Gateway-Anbieter und allen Sub-Auftragsverarbeitern.
- [ ] Rechtsgrundlage für die Verarbeitung benannt (Art. 6 DSGVO; bei besonderen Kategorien Art. 9 DSGVO).
- [ ] Bei Beschäftigtendaten: § 26 BDSG geprüft und ggf. Betriebsvereinbarung vorhanden.
- [ ] Informationspflichten Art. 13/14 DSGVO erfüllt (Datenschutzerklärung, Mandanteninformation).
- [ ] Datenschutz-Folgenabschätzung (Art. 35 DSGVO) durchgeführt — bei Legal-AI mit Mandatsdaten in der Regel erforderlich.
- [ ] Verzeichnis von Verarbeitungstätigkeiten (Art. 30 DSGVO) aktualisiert.
- [ ] Löschkonzept (Art. 17, 5 Abs. 1 lit. e DSGVO) — wie lange werden Eingaben und Ausgaben aufbewahrt?

## III. Drittlandtransfer / Schrems II

- [ ] Wird in ein Drittland (USA, UK, etc.) übermittelt? Wenn ja:
  - [ ] Angemessenheitsbeschluss (Art. 45) anwendbar? — EU-US Data Privacy Framework ist anwendbar, soweit Empfänger zertifiziert; **prüfen** unter https://www.dataprivacyframework.gov/.
  - [ ] Falls nicht: Standardvertragsklauseln (Art. 46 Abs. 2 lit. c) und Transfer Impact Assessment durchgeführt?
  - [ ] Schrems II-Risiken (US Cloud Act, FISA § 702, EO 12333) bewertet?
  - [ ] Zusätzliche Maßnahmen (Verschlüsselung, Pseudonymisierung) implementiert?

## IV. KI-VO (VO (EU) 2024/1689)

- [ ] Klassifizierung des Systems geprüft:
  - [ ] Verbotenes System nach Art. 5 KI-VO? (Social Scoring, Manipulation, etc.) — Legal-AI in den hier abgedeckten Skills regelmäßig nicht erfasst.
  - [ ] Hochrisiko-System nach Art. 6 i.V.m. Anhang III? — insb. Anhang III Nr. 8 (Justiz, demokratische Prozesse): bei Einsatz in der Rechtspflege oder von Behörden möglich. Bei rein anwaltlicher Mandatsarbeit regelmäßig nicht.
  - [ ] General-Purpose-AI-Modell nach Art. 51 ff.? — der zugrunde liegende Anbieter (Anthropic, Google, OpenAI) ist GPAI-Anbieter; Pflichten treffen primär den Anbieter, abgeleitet auch den Betreiber.
- [ ] Transparenzpflichten Art. 50 KI-VO erfüllt (Hinweis, dass mit KI interagiert wird; Kennzeichnung KI-generierter Inhalte)?
- [ ] Betreiberpflichten nach Art. 26 KI-VO bei Hochrisiko-Einsatz erfüllt (Kompetenz, Aufsicht, Datenqualität, Logging)?

## V. Berufsrecht über § 203 hinaus

- [ ] Werbung mit KI-Einsatz (§ 43b BRAO, § 6 BORA) — sachlich, nicht irreführend.
- [ ] Fortbildungspflicht § 43a Abs. 6 BRAO — KI-Kompetenz ist Fortbildungsgegenstand.
- [ ] Vermögensbetreuungspflichten bei Vertrauensanwälten (§ 43a Abs. 5 BRAO).
- [ ] Bei Steuerberatern: § 62a StBerG; bei Wirtschaftsprüfern: § 50a WPO; bei Patentanwälten: § 39c PAO; bei Notaren: § 26a BNotO.

## VI. Beschlagnahmeverbote / extraterritorialer Zugriff

- [ ] §§ 97, 160a StPO – Beschlagnahmeverbot zugunsten von Berufsgeheimnisträgern. Schutz greift nur, wenn die Daten bei dem Berufsgeheimnisträger selbst oder seiner Sphäre lagern; Cloud-Verarbeitung beim Anbieter ist umstritten.
- [ ] US Cloud Act, FISA § 702, EO 12333 — extraterritorialer Zugriff auf bei US-Anbietern lagernde Daten ist möglich.
- [ ] Vertragliche Zusicherung des Anbieters zur Ablehnung unbegründeter ausländischer Behördenanfragen (transparency report).

## VII. Technische Mindeststandards

- [ ] **PII-Redaktion vor Eingabe** (z. B. via `scripts/pii_redact.py`).
- [ ] **Audit-Log** der eingespielten Prompts und Ausgaben (lokal, verschlüsselt, mit Mandatsbezug).
- [ ] **Versionskontrolle der Skills** — welcher Stand wurde wann produktiv genutzt?
- [ ] **Nutzerkonfiguration** — keine Modellantwort wird ohne anwaltliche Prüfung an Mandanten weitergegeben.
- [ ] **Backups und Recovery** — Mandatsdaten gehören nicht ausschließlich in den AI-Anbieter.

## VIII. Organisatorisches

- [ ] KI-Richtlinie / Betriebsvereinbarung (bei Kanzleien mit ≥ 5 wahlberechtigten AN: § 87 BetrVG ggf. mitbestimmt).
- [ ] Fortbildung der Mitarbeitenden zu Grenzen der KI-Nutzung.
- [ ] Eskalationspfad bei Datenschutzvorfällen (Art. 33 DSGVO, 72-Stunden-Frist).
- [ ] Mandanteneinwilligung, falls erforderlich (insbesondere § 2 BORA, ggf. § 26 BDSG).
- [ ] Versicherung — Haftpflicht prüft KI-Nutzung explizit (Berufshaftpflicht, ggf. Cyber-Police).

## IX. Skill-spezifische Prüfungen

- [ ] Welche Skills enthalten `[unverifiziert]`-Markierungen? Workflow zur menschlichen Verifizierung definiert?
- [ ] Welche Outputs gehen direkt an Mandanten? — keine ohne anwaltliche Freigabe.
- [ ] Eval-Tests (`scripts/eval.py`) für relevante Skills mindestens einmal vor Produktivnutzung gelaufen.
