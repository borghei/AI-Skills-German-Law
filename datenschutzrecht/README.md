# Datenschutzrecht

**DSGVO-, BDSG-, TTDSG-Skills für Claude / Gemini / GPT.**

## Skills

| Skill | Funktion | Anker |
|---|---|---|
| `auskunftsersuchen-art-15` | Bearbeitung eines Auskunftsersuchens nach Art. 15 DSGVO | Art. 15 DSGVO, § 34 BDSG |
| `datenpanne-art-33` *(geplant)* | 72-Stunden-Meldung an die Aufsichtsbehörde | Art. 33, 34 DSGVO |
| `avv-review` *(geplant)* | Prüfung eines Auftragsverarbeitungsvertrags | Art. 28 DSGVO |
| `dpia` *(geplant)* | Datenschutz-Folgenabschätzung | Art. 35 DSGVO |
| `drittlandtransfer` *(geplant)* | TIA + SCC nach Schrems II | Art. 44 ff. DSGVO |
| `beschaeftigtendatenschutz` *(geplant)* | § 26 BDSG-Prüfung | § 26 BDSG |

> Skills mit *(geplant)* sind Stubs für Contributions. Siehe [`CONTRIBUTING.md`](../CONTRIBUTING.md).

## Hinweise

- **Drittlandtransfer.** Jede Verwendung von US-Cloud / EU-US-DPF dokumentieren (TIA).
- **Schrems II.** Bei Cloud-Verarbeitung Risikoabwägung gegen US Cloud Act / FISA § 702 / EO 12333.
- **DSK / EDPB-Leitlinien.** Verbindlich für Behörden, faktisch maßgeblich für Verarbeiter.

## Anwendungsbeispiel

```
/datenschutzrecht:auskunftsersuchen-art-15
Mandant ist eine eCommerce-GmbH, hat ein Auskunftsersuchen von einem
ehemaligen Kunden erhalten. Kunde verlangt Auskunft über alle gespeicherten
Daten, Empfängerkategorien und Speicherdauer. Frist?
```
