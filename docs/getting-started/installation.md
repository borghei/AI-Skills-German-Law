# Installation

Three install paths, depending on which LLM you use.

## Claude Code (native)

```bash
# Add the marketplace once
/plugin marketplace add borghei/AI-Skills-German-Law

# Install any of the 23 areas
/plugin install arbeitsrecht
/plugin install datenschutzrecht
/plugin install ki-vo-compliance
# ...
```

After install, skills are callable as:

```
/arbeitsrecht:kuendigungs-pruefung
/datenschutzrecht:auskunftsersuchen-art-15
/ki-vo-compliance:hochrisiko-klassifizierung
```

## Gemini Gems

```bash
git clone https://github.com/borghei/AI-Skills-German-Law.git
cd AI-Skills-German-Law

# Render a Gem-ready instruction file
python scripts/route_provider.py --provider gemini --skill arbeitsrecht/kuendigungs-pruefung
```

The script writes `arbeitsrecht/skills/kuendigungs-pruefung/providers/gemini.md`. Open it, copy everything between `BEGIN GEM INSTRUCTIONS` and `END GEM INSTRUCTIONS`, then paste into a new Gem at [gemini.google.com](https://gemini.google.com).

Bulk-render all areas at once:

```bash
python scripts/route_provider.py --provider gemini --out dist/gemini
```

## OpenAI (Custom GPT or Assistants API)

```bash
python scripts/route_provider.py --provider openai --skill arbeitsrecht/kuendigungs-pruefung
```

The output is at `arbeitsrecht/skills/kuendigungs-pruefung/providers/openai.md`. For Custom GPTs, copy the instructions block into the **Configure** tab at [chatgpt.com](https://chatgpt.com/gpts/editor).

For the Assistants API:

```python
from openai import OpenAI
client = OpenAI()
with open("arbeitsrecht/skills/kuendigungs-pruefung/providers/openai.md") as f:
    instructions = f.read()
assistant = client.beta.assistants.create(
    name="Arbeitsrecht: Kündigungs-Prüfung",
    instructions=instructions,
    model="gpt-4o",
)
```

## Manual install (any AI chat)

Open any `SKILL.md`, copy the body (everything below the YAML frontmatter), paste as the first message of a new conversation in Claude.ai, ChatGPT, or Gemini, then describe your Mandat.

## Multi-skill workflows

For chained workflows (e.g., a full Kündigung pipeline), use the orchestrator:

```bash
python scripts/orchestrate.py --preset kuendigung-vollumfang --fact "Mandantin plant..."
python scripts/orchestrate.py --list-chains
```

Available presets:

- `kuendigung-vollumfang` — Kündigungs-Prüfung, Abmahnung, Aufhebungsvertrag
- `krise-360` — Liquidität, Fortbestehensprognose, Antragspflicht, GF-Haftung
- `starug-restructuring` — Liquidität then StaRUG-Plan
- `ki-deployment-compliance` — Hochrisiko, Auskunft Art. 15, IT-Vertrag
- `dsgvo-datenpanne` — Art. 15-Bearbeitung then NIS2-Meldung
- `scheidung-full` — Zugewinnausgleich
