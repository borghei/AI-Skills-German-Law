---
name: ki-transparenzpflichten
description: "Prüfung der Transparenzpflichten nach Art. 50 KI-VO – Offenlegung der KI-Interaktion, Kennzeichnung synthetischer Inhalte und Deepfakes, Information bei Emotionserkennung und biometrischer Kategorisierung samt Bußgeldrisiko Art. 99 KI-VO. Use when ein Anbieter oder Betreiber eines KI-Systems prüfen muss, ob und wie er Nutzer über KI-Einsatz oder KI-generierte Inhalte informieren und kennzeichnen muss."
language: de
provider_variants: [claude, gemini, openai]
test: ./test.md
---

# /ki-vo-compliance:ki-transparenzpflichten

## Zweck

**Art. 50 KI-VO** ([VO (EU) 2024/1689](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1689)) auferlegt Anbietern und Betreibern bestimmter KI-Systeme **Transparenz- und Kennzeichnungspflichten**, um Täuschung, Desinformation und Manipulation im Informationsökosystem zu begrenzen. Die Pflichten gelten ab dem 2. August 2026 und treffen auch Systeme, die nicht hochrisiko-eingestuft sind. Dieser Skill ordnet einem System die einschlägige Transparenzpflicht zu und prüft die Art der Kennzeichnung.

## Eingaben

- Funktion des Systems (Interaktion mit Menschen, Inhaltserzeugung, Emotionserkennung)
- Rolle des Mandanten (Anbieter / Betreiber — Art. 3 KI-VO)
- Art der erzeugten Inhalte (Bild, Audio, Video, Text; synthetisch oder Deepfake)
- Einsatzkontext (Kundendialog, redaktioneller Inhalt, Kunst/Satire)
- Bereits vorhandene Kennzeichnung/Hinweise

## Sub-Agent-Architektur

Drei gedankliche Rollen teilen die Prüfung. Ein **Pflichten-Zuordner** ordnet die Funktion einer der vier Säulen des Art. 50 KI-VO zu (Interaktionsoffenlegung, Markierung synthetischer Inhalte, Emotionserkennung, Deepfake-Offenlegung) und bestimmt, ob Anbieter- oder Betreiberpflicht greift. Ein **Kennzeichnungs-Designer** legt fest, wie die Markierung technisch (maschinenlesbar) und gegenüber dem Menschen erfolgen muss und welche Ausnahmen gelten. Ein **Sanktions-Bewerter** beziffert das Bußgeldrisiko nach Art. 99 KI-VO. Der Pflichten-Zuordner übergibt jede bejahte Pflicht an den Kennzeichnungs-Designer.

## Ablauf

### 1. Offenlegung der KI-Interaktion (Art. 50 Abs. 1 KI-VO)

**Anbieter** müssen KI-Systeme, die für die **direkte Interaktion mit natürlichen Personen** bestimmt sind (z. B. Chatbots), so gestalten, dass die betroffene Person informiert ist, dass sie mit einem KI-System interagiert — es sei denn, dies ist aus den Umständen offensichtlich.

### 2. Kennzeichnung synthetischer Inhalte (Art. 50 Abs. 2 KI-VO)

**Anbieter** von Systemen, die synthetische **Bild-, Audio-, Video- oder Textinhalte** erzeugen oder manipulieren, müssen die Ausgabe in einem **maschinenlesbaren Format** markieren und als künstlich erzeugt/manipuliert erkennbar machen (z. B. Wasserzeichen, Metadaten).

### 3. Emotionserkennung und biometrische Kategorisierung (Art. 50 Abs. 3 KI-VO)

**Betreiber** von Emotionserkennungs- oder biometrischen Kategorisierungssystemen müssen die betroffenen Personen über den Betrieb informieren (Verzahnung mit DSGVO-Pflichten).

### 4. Deepfake-Offenlegung (Art. 50 Abs. 4 KI-VO)

**Betreiber**, die mit einem KI-System **Deepfakes** (Bild, Audio, Video) erzeugen oder manipulieren, müssen offenlegen, dass die Inhalte künstlich erzeugt/manipuliert wurden. Für offensichtlich künstlerische, kreative oder satirische Werke gilt eine **abgeschwächte** Offenlegung, die die Darstellung nicht beeinträchtigt. Auch bei KI-erzeugten/-bearbeiteten Texten zur Information der Öffentlichkeit über Angelegenheiten von öffentlichem Interesse besteht eine Offenlegungspflicht.

### 5. Form und Zeitpunkt

Informationen sind **klar und unterscheidbar spätestens zum Zeitpunkt der ersten Interaktion/Exposition** bereitzustellen, barrierefrei. Markierungen müssen wirksam, interoperabel, robust und so weit technisch möglich sein.

### 6. Sanktionen (Art. 99 KI-VO)

Verstöße gegen Transparenzpflichten nach Art. 50 KI-VO können mit Geldbußen bis **15 Mio. EUR oder 3 % des weltweiten Jahresumsatzes** geahndet werden.

## Risiken

- **Kennzeichnung vergessen** — synthetische Inhalte ohne maschinenlesbare Markierung verstoßen gegen Art. 50 Abs. 2 KI-VO.
- **Deepfake nicht offengelegt** — fehlende Offenlegung nach Art. 50 Abs. 4 KI-VO; die Kunst-/Satire-Ausnahme ist eng und befreit nicht vollständig.
- **Chatbot ohne Hinweis** — fehlende Offenlegung der KI-Interaktion nach Art. 50 Abs. 1 KI-VO.
- **Bußgeldrisiko** — bis 15 Mio. EUR / 3 % nach Art. 99 KI-VO.

## Ausgabeformat

```
KI-TRANSPARENZPFLICHTEN — PRÜFUNG — <System> — <Datum>

I.   Funktion                                   [Interaktion / Inhaltserzeugung / Emotion]
II.  Rolle (Art. 3 KI-VO)                        [Anbieter / Betreiber]
III. Einschlägige Pflicht (Art. 50 KI-VO)
     Abs. 1 KI-Interaktion                       [betroffen? <…>]
     Abs. 2 synthetische Inhalte                 [betroffen? Markierung <…>]
     Abs. 3 Emotionserkennung                    [betroffen? <…>]
     Abs. 4 Deepfake                             [betroffen? Offenlegung <…>]
IV.  Form / Zeitpunkt der Kennzeichnung          [<…>]
V.   Ausnahme (Kunst/Satire/offensichtlich)      [greift? <…>]
VI.  Bußgeldrisiko (Art. 99 KI-VO)               [bis 15 Mio. EUR / 3 %]

Empfehlung: <…>
Nächste Schritte: <…>
```

## Quellen

### Statute

- [VO (EU) 2024/1689 (KI-VO / EU AI Act)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1689) — Volltext
- Art. 50 KI-VO (Transparenzpflichten), Art. 99 KI-VO (Sanktionen)

### Leitlinien

- EU-Kommission, Leitlinien zu Transparenzpflichten nach Art. 50 KI-VO (Entwurf)

### Sekundärliteratur

- Hilgendorf/Roth-Isigkeit, KI-VO, 1. Aufl. 2024
- BeckOK KI-VO (Online)
