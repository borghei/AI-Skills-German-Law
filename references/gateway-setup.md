# Gateway-Setup – § 203-kompatible Anbindung

Für die Verarbeitung von Mandatsdaten unter § 203 StGB / § 43e BRAO empfiehlt sich das Routing über einen deutschen Zwischenanbieter (Langdock, deepset Cloud, oder vergleichbar), der eine § 203-Verschwiegenheitserklärung unterschreibt und die API mit Anthropic/OpenAI/Google-kompatibler Base-URL bereitstellt.

> **Wichtig.** Dieses Dokument ist eine technische Anleitung. Es ersetzt nicht die anwaltliche Prüfung, ob Ihr konkreter Vertrag und Datenfluss berufs-, datenschutz- und KI-rechtlich zulässig sind. Vgl. `compliance-checklist.md`.

## Vorbereitung beim Gateway-Anbieter

1. **Anbieter wählen** mit § 203-Zusatzvereinbarung (Langdock, deepset Cloud, anymize, etc.).
2. **Verschwiegenheitsvereinbarung** unterschreiben, Original/Kopie in die Kanzleiakte.
3. **Auftragsverarbeitungsvertrag** (Art. 28 DSGVO) abschließen.
4. Im Dashboard des Anbieters einen **API-Schlüssel** erzeugen, mit sprechendem Namen (z. B. "ai-skills-german-law – Kanzlei-Workstation").
5. **Base URL** notieren (typisch `https://api.<anbieter>.de/anthropic`, `…/openai`, `…/gemini`).

## Claude Code / Claude Desktop (macOS)

```bash
# Terminal:
launchctl setenv ANTHROPIC_BASE_URL https://api.<gateway>.de/anthropic
launchctl setenv ANTHROPIC_AUTH_TOKEN <Ihr-Gateway-Schluessel>
launchctl setenv ANTHROPIC_API_KEY ""
```

Danach Claude vollständig beenden (Cmd+Q) und neu starten. Beim Login "Continue with Gateway" wählen.

## Claude Code / Claude Desktop (Windows 11)

1. Systemsteuerung → System → Erweiterte Systemeinstellungen → Umgebungsvariablen.
2. Benutzervariablen anlegen:
   - `ANTHROPIC_BASE_URL` = `https://api.<gateway>.de/anthropic`
   - `ANTHROPIC_AUTH_TOKEN` = (Ihr Schlüssel)
   - `ANTHROPIC_API_KEY` = (leer)
3. Ab- und neu anmelden, Claude starten.

## OpenAI / GPT (Custom GPT, Assistants API)

Custom GPTs konfigurieren sich nicht auf API-Ebene; für Mandatsarbeit muss die OpenAI-API direkt verwendet werden:

```bash
# macOS/Linux
export OPENAI_BASE_URL="https://api.<gateway>.de/openai/v1"
export OPENAI_API_KEY="<Ihr-Gateway-Schluessel>"
```

Mit der OpenAI-Python-SDK (≥ v1.0):

```python
from openai import OpenAI
client = OpenAI(base_url=os.environ["OPENAI_BASE_URL"],
                api_key=os.environ["OPENAI_API_KEY"])
```

## Gemini (Vertex AI über Gateway)

Gemini-Routing über deutsche Zwischenanbieter ist Stand Mai 2026 noch unüblich; sofern der Anbieter eine `https://api.<anbieter>.de/gemini`-Schnittstelle anbietet:

```bash
export GOOGLE_GENAI_BASE_URL="https://api.<gateway>.de/gemini/v1beta"
export GOOGLE_GENAI_API_KEY="<Ihr-Gateway-Schluessel>"
```

Mit `google-genai` Python-SDK:

```python
import os
from google import genai
client = genai.Client(
    api_key=os.environ["GOOGLE_GENAI_API_KEY"],
    http_options=genai.types.HttpOptions(base_url=os.environ["GOOGLE_GENAI_BASE_URL"]),
)
```

## Funktionsprüfung

Nach Setup einmal mit **Dummy-Daten** prüfen:

```bash
# Erwartete Antwort: kurze Vorstellung des Modells, KEIN Zugriff auf Web
curl -X POST "$ANTHROPIC_BASE_URL/v1/messages" \
  -H "x-api-key: $ANTHROPIC_AUTH_TOKEN" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{
    "model": "claude-sonnet-4-6",
    "max_tokens": 200,
    "messages": [{"role": "user", "content": "Wer bist du? Antworte in 2 Sätzen."}]
  }'
```

Wenn die Antwort vom Gateway durchgereicht wird: Setup steht.

## Wenn die Gateway-Antwort fehlschlägt

| Symptom | Ursache | Lösung |
|---|---|---|
| `401 Invalid API key` | x-api-key vs. Authorization-Bearer | Gateway-Doku prüfen, Auth-Schema umstellen |
| `404 Not Found` | Pfad `/v1/messages` nicht durchgeschleust | Base-URL inkl. `/anthropic`-Präfix prüfen |
| `429 Rate limited` | Tarif des Gateways | Plan upgraden oder Backoff im Code |
| Timeout | Gateway-Region | EU-Region wählen, sonst evtl. Drittlandtransfer |

## Logging und Audit

Der Gateway-Anbieter muss eine Logging-Konfiguration anbieten, die:

- **keine** Prompts und Antworten im Klartext speichert (oder nur kurze Retention mit Mandatsbezug),
- Audit-Events (Login, API-Key-Rotation) protokolliert,
- DSGVO-Auskunft Art. 15 zu den protokollierten Daten ermöglicht.

Lokal sollten Sie zusätzlich `scripts/eval.py` und `scripts/pii_redact.py` so konfigurieren, dass alle Eingaben **vor** dem Gateway durch die PII-Redaktion laufen.
