#!/usr/bin/env python3
"""Generate a promptfoo eval config from the skills' test.md files.

The repo's `scripts/eval.py` does STRUCTURAL checks (does the SKILL.md text
contain the required statutes/sections/risks). This script adds the BEHAVIOURAL
layer recommended for skill libraries: it emits a `promptfoo` config that
actually sends each skill's fact pattern to a model and grades the output, using

- deterministic assertions (icontains for must_cite / must_appear / must_flag,
  not-icontains for the forbidden [generiert] marker), AND
- model-graded `llm-rubric` assertions for each `expected_behavior` line in
  test.md, graded by a JUDGE model.

This script itself calls NO LLM (matching every other script in scripts/). It
only generates the config; `promptfoo eval` does the model calls, run by the
maintainer against their own (ideally § 203-compliant) gateway. The fact
patterns in test.md are synthetic - no Mandatsdaten - so they are safe to send.

Why a separate judge family: an LLM judging its own family inflates scores
(self-enhancement bias). Default judge here is a Claude model and default
system-under-test is also Claude only as a placeholder - set --provider and
--judge to DIFFERENT families (e.g. drafter = Claude, judge = Gemini), and
avoid an OpenAI judge if the drafter is OpenAI. See evals/README.md.

Usage:
    python scripts/build_eval_config.py                       # all skills
    python scripts/build_eval_config.py --area arbeitsrecht
    python scripts/build_eval_config.py --skill arbeitsrecht/kuendigungs-pruefung
    python scripts/build_eval_config.py --provider anthropic:messages:claude-opus-4-8 \
        --judge google:gemini-2.5-pro --out evals/promptfoo.generated.yaml

Then:
    npx promptfoo@latest eval -c evals/promptfoo.generated.yaml
    npx promptfoo@latest view
"""
from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]

# Reuse skill discovery from eval.py (avoid drift). We parse the test.md
# frontmatter here with PyYAML rather than eval.py's parse_test, because the
# latter is a lightweight line parser that does not capture block-scalar
# (`fact_pattern: |`) bodies - we need the full fact pattern for the eval.
_spec = importlib.util.spec_from_file_location("_eval", Path(__file__).resolve().parent / "eval.py")
_eval = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_eval)  # type: ignore[union-attr]
find_skills = _eval.find_skills


def parse_test(test_path: Path) -> dict:
    """Parse the YAML frontmatter of a test.md (between the first two `---`).

    The delimiters are matched as full column-0 lines (`== "---"`), not as a
    substring, so a `---` appearing inside the indented `fact_pattern` block
    scalar does not prematurely terminate the frontmatter.
    """
    if not test_path.exists():
        return {}
    lines = test_path.read_text(encoding="utf-8").split("\n")
    if not lines or lines[0].rstrip() != "---":
        return {}
    end = next((i for i in range(1, len(lines)) if lines[i].rstrip() == "---"), None)
    if end is None:
        return {}
    try:
        data = yaml.safe_load("\n".join(lines[1:end]))
    except yaml.YAMLError:
        return {}
    return data if isinstance(data, dict) else {}

DEFAULT_PROVIDER = "anthropic:messages:claude-opus-4-8"
DEFAULT_JUDGE = "anthropic:messages:claude-opus-4-8"

PROMPT_TEMPLATE = (
    "{{skill_body}}\n\n"
    "---\n\n"
    "Wende den vorstehenden Skill vollständig auf folgenden Sachverhalt an. "
    "Halte dich strikt an die Zitierweise (verifizierte Statute mit Quelle, "
    "Rechtsprechung mit Verifikationsmarker) und an das Ausgabeformat.\n\n"
    "## Sachverhalt\n{{fact_pattern}}\n"
)

# German rubric wrapper for llm-rubric grading (model-graded assertions).
RUBRIC_PROMPT = """Du bewertest die juristische Ausgabe eines KI-Skills für die deutsche Rechtspraxis.

Ausgabe des zu prüfenden Modells:
{{ output }}

Bewertungskriterium (muss erfüllt sein):
{{ rubric }}

Bewerte ausschließlich, ob das Kriterium erfüllt ist. Sei streng: im Zweifel nicht bestanden.
Antworte als JSON: {"pass": true|false, "score": 0.0-1.0, "reason": "<kurze Begründung auf Deutsch>"}."""


def _rel_from_evals(skill_dir: Path, out_path: Path) -> str:
    """file:// path to SKILL.md, relative to the config file's directory."""
    skill_md = skill_dir / "SKILL.md"
    try:
        rel = skill_md.relative_to(out_path.resolve().parent)
    except ValueError:
        import os
        rel = Path(os.path.relpath(skill_md, out_path.resolve().parent))
    return f"file://{rel.as_posix()}"


def build_config(skills: list[Path], provider: str, judge: str, out_path: Path) -> dict:
    tests = []
    for skill_dir in skills:
        rel = skill_dir.relative_to(REPO_ROOT).as_posix()
        test = parse_test(skill_dir / "test.md")
        fact = (test.get("fact_pattern") or "").strip()
        if not fact:
            continue  # no fact pattern -> nothing behavioural to run

        asserts: list[dict] = []
        for anchor in (test.get("must_cite") or []):
            asserts.append({"type": "icontains", "value": anchor})
        for section in (test.get("must_appear") or []):
            asserts.append({"type": "icontains", "value": section})
        for risk in (test.get("must_flag") or []):
            asserts.append({"type": "icontains", "value": risk})
        # Forbidden marker in client-facing output.
        asserts.append({"type": "not-icontains", "value": "[generiert"})
        # Behavioural rubric assertions (graded by the judge).
        for behavior in (test.get("expected_behavior") or []):
            asserts.append({"type": "llm-rubric", "value": behavior})

        tests.append({
            "description": rel,
            "vars": {
                "skill_body": _rel_from_evals(skill_dir, out_path),
                "fact_pattern": fact,
            },
            "assert": asserts,
        })

    return {
        "description": f"Behavioural eval for {len(tests)} German-law skills",
        "providers": [provider],
        "prompts": [PROMPT_TEMPLATE],
        "defaultTest": {
            "options": {
                "provider": judge,
                "rubricPrompt": RUBRIC_PROMPT,
            }
        },
        "tests": tests,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a promptfoo eval config from test.md files")
    parser.add_argument("--area", help="restrict to one area")
    parser.add_argument("--skill", help="restrict to one skill (path relative to repo root)")
    parser.add_argument("--provider", default=DEFAULT_PROVIDER,
                        help="system-under-test provider id (promptfoo syntax)")
    parser.add_argument("--judge", default=DEFAULT_JUDGE,
                        help="judge provider id for llm-rubric (use a DIFFERENT family)")
    parser.add_argument("--out", default="evals/promptfoo.generated.yaml",
                        help="output path for the generated config")
    args = parser.parse_args(argv)

    out_path = (REPO_ROOT / args.out).resolve()
    skills = find_skills(args.area, args.skill)
    if not skills:
        print("No skills found.", file=sys.stderr)
        return 1

    config = build_config(skills, args.provider, args.judge, out_path)
    if not config["tests"]:
        print("No skills with a fact_pattern found; nothing to eval.", file=sys.stderr)
        return 1

    if args.provider.split(":")[0] == args.judge.split(":")[0]:
        print(f"WARNUNG: provider und judge sind dieselbe Familie "
              f"({args.provider.split(':')[0]}). Für unvoreingenommene Bewertung "
              f"unterschiedliche Modellfamilien wählen (self-enhancement bias).",
              file=sys.stderr)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as fh:
        fh.write("# AUTO-GENERATED by scripts/build_eval_config.py. Do not edit by hand.\n")
        fh.write("# Run: npx promptfoo@latest eval -c " + args.out + "\n")
        yaml.safe_dump(config, fh, allow_unicode=True, sort_keys=False, width=100)

    n_rubric = sum(
        1 for t in config["tests"] for a in t["assert"] if a["type"] == "llm-rubric"
    )
    try:
        shown = out_path.relative_to(REPO_ROOT)
    except ValueError:
        shown = out_path  # --out pointed outside the repo
    print(f"Wrote {shown}: {len(config['tests'])} skill(s), "
          f"{n_rubric} llm-rubric assertion(s).")
    if n_rubric == 0:
        print("Hinweis: keine 'expected_behavior'-Einträge in den test.md gefunden; "
              "nur deterministische Assertions erzeugt. Füge expected_behavior hinzu "
              "für modellbewertete Kriterien.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
