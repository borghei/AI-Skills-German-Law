# Quick Start

60 seconds from zero to a working drafting aid.

## Claude Code

```bash
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install arbeitsrecht
/arbeitsrecht:kuendigungs-pruefung
```

## Gemini Gem

```bash
git clone https://github.com/borghei/AI-Skills-German-Law.git
cd AI-Skills-German-Law
python scripts/route_provider.py --provider gemini --skill arbeitsrecht/kuendigungs-pruefung
```

Open `arbeitsrecht/skills/kuendigungs-pruefung/providers/gemini.md`, copy the instruction block, paste into a new Gem at [gemini.google.com](https://gemini.google.com).

## OpenAI Custom GPT

```bash
python scripts/route_provider.py --provider openai --skill arbeitsrecht/kuendigungs-pruefung
```

Open `arbeitsrecht/skills/kuendigungs-pruefung/providers/openai.md`, copy the instruction block, paste into the Configure tab at [chatgpt.com](https://chatgpt.com/gpts/editor).

## Any AI chat (no setup)

Open any `SKILL.md` in the repo. Copy the body (below the YAML frontmatter). Paste into Claude.ai, ChatGPT, or Gemini as the first message.

## Local sanity check

```bash
python scripts/validate.py    # plugin manifests + frontmatter
python scripts/eval.py        # 370+ structural assertions across 28 skills
```

Both should pass before you trust any skill.

## Sample workflow

```bash
# Chain three Arbeitsrecht skills for a full Kündigung pipeline
python scripts/orchestrate.py \
  --preset kuendigung-vollumfang \
  --fact "Mandantin (Maschinenbau, 35 EE, kein BR) plant betriebsbedingte Kündigung..."
```

The orchestrator prints a single multi-step prompt you can feed to any LLM.
