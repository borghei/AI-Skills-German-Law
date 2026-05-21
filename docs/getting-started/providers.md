# Providers

The repo is **provider-agnostic at the source level**. Each skill is one canonical `SKILL.md`. Provider-specific adapter files (`providers/claude.md`, `providers/gemini.md`, `providers/openai.md`) are regenerated on demand from the canonical via `scripts/route_provider.py`.

## Why this matters

- One source of legal substance to maintain.
- Providers can be added without touching skill content.
- No drift between what Claude users see and what Gemini users see.
- Adding a new provider (Mistral, DeepSeek, Llama) is a contribution that adds one `providers/<new>.md` template, not a fork of every skill.

## Provider table

| Provider | Install path | Native format | Notes |
|---|---|---|---|
| **Claude Code** | Claude Code → Customize Plugins → Install from .zip, or `/plugin install <area>` after marketplace add | `.claude-plugin/plugin.json` + `skills/<name>/SKILL.md` | Most direct integration. Full plugin ecosystem (commands, hooks, MCP). |
| **Gemini (Gems)** | gemini.google.com → Gems → Create new gem → paste instructions | `providers/gemini.md` (instruction block) | Gem instructions field is the canonical body. Web search and code interpreter available as Gem capabilities. |
| **OpenAI (Custom GPT)** | chatgpt.com → Create a GPT → Configure → paste instructions | `providers/openai.md` (instruction block) | Custom GPT lives in your ChatGPT account. Optionally enable web browsing for verification. |
| **OpenAI (Assistants API)** | `client.beta.assistants.create(instructions=...)` | Same `providers/openai.md` text | Programmatic. Use for automated pipelines. |
| **Any chat (Claude.ai, ChatGPT.com, Gemini.com)** | Paste SKILL.md body into a new conversation | Raw markdown | Lowest-effort path. No persistence between chats. |

## Regenerating adapters

```bash
# One skill, one provider
python scripts/route_provider.py --provider claude --skill arbeitsrecht/kuendigungs-pruefung

# All skills in one area
python scripts/route_provider.py --provider gemini --area arbeitsrecht

# Everything to a bundle directory
python scripts/route_provider.py --provider openai --out dist/openai
```

## Provider parity

The conventions in [CONVENTIONS.md](https://github.com/borghei/AI-Skills-German-Law/blob/main/CONVENTIONS.md) apply identically across providers:

- Outputs in German
- Gutachtenstil / Urteilsstil per task
- BGH/Beck citation style
- No Präjudizienbindungs-Argumente (except § 31 BVerfGG)
- Verification markers on every case citation

Provider-specific tooling (Gemini web search, GPT code interpreter, MCP servers in Claude Code) may be used **only** for verification tasks. They must not surface unsourced legal claims as "research."

## § 203 routing

For real Mandatsdaten, every provider must be routed through a German § 203-compliant gateway. See [Compliance](../compliance.md) for the setup walkthrough.
