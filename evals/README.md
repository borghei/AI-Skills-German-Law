# Behavioural evals (LLM-graded)

`scripts/eval.py` checks skills **structurally** (does the SKILL.md contain the
required statutes, sections and risk flags). That runs in CI with no model and
no cost. This directory adds the **behavioural** layer: actually send each
skill's fact pattern to a model and grade the output, including model-graded
rubric criteria.

The harness is [promptfoo](https://www.promptfoo.dev). The Python generator
(`scripts/build_eval_config.py`) emits a promptfoo config from the `test.md`
files; promptfoo does the model calls. No Python script in this repo ever calls
an LLM - that boundary is intentional (see `CONVENTIONS.md`).

## What gets generated

For every skill with a `fact_pattern` in its `test.md`:

- **Deterministic assertions** - `icontains` for each `must_cite`, `must_appear`
  and `must_flag` entry, plus `not-icontains "[generiert"` (the forbidden
  fabricated-citation marker).
- **Model-graded assertions** - one `llm-rubric` per `expected_behavior` line,
  scored by a **judge** model against a strict German rubric prompt.

Add `expected_behavior:` lines to a skill's `test.md` to grow the behavioural
coverage (see `arbeitsrecht/skills/kuendigungs-pruefung/test.md` for an example).

## Running

```bash
# 1. Generate the config (all skills, or a subset)
python scripts/build_eval_config.py \
    --provider anthropic:messages:claude-opus-4-8 \
    --judge   google:gemini-2.5-pro \
    --out evals/promptfoo.generated.yaml

# 2. Run it (promptfoo reads ANTHROPIC_API_KEY / GOOGLE_API_KEY etc.)
npx promptfoo@latest eval -c evals/promptfoo.generated.yaml
npx promptfoo@latest view
```

The generated `*.generated.yaml` is git-ignored - it is a build artifact, not
source. Regenerate it whenever `test.md` files change.

## Two rules that matter

1. **Judge ≠ drafter family.** A model grading its own family inflates scores
   (self-enhancement bias). If the system-under-test is Claude, judge with
   Gemini, and vice-versa. The generator prints a warning when the families
   match. Avoid an OpenAI judge if the drafter is OpenAI.

2. **Route through your § 203-compliant gateway.** The bundled fact patterns are
   synthetic (no Mandatsdaten), so the shipped evals are safe to run against any
   endpoint. But if you adapt them to real matters, set the provider `apiBaseUrl`
   to your gateway (see `references/gateway-setup.md`) - never send Mandatsdaten
   to a raw provider endpoint.

## Roadmap

- Per-stage golden tests (researcher recall of must-cite provisions; reviewer
  fed known-flawed drafts to confirm it flags them).
- A German legal rubric on the 0-18 Punkte scale (cf. the BenGER dimensions).
- Multi-model runs (Haiku/Sonnet/Opus) to confirm a skill is model-robust.
