#!/usr/bin/env python3
"""Unit tests for the repo's own toolchain — the checkers, not the law.

`scripts/legal_calc/tests.py` covers the calculators. Nothing covered the
scripts that decide whether a skill is valid, which is how three defects shipped
unnoticed:

- `eval.py`'s frontmatter parser stripped only *double* quotes, so a
  single-quoted list entry (the correct YAML form when the value itself contains
  a double quote) kept its delimiters and could never match a SKILL.md body.
- `verify_citations.py` mapped UWG to the slug `uwg`; gesetze-im-internet.de
  serves it as `uwg_2004`, so every UWG citation in the repo resolved to a 404
  under `--online`.
- The same map derived per-article URLs for the EGBGB, which that site does not
  publish at all — every EGBGB citation was reported as a failure.

Each test below pins one of those behaviours so a regression is loud.

Run:
    python -m unittest scripts.tests_toolchain
"""
from __future__ import annotations

import json
import unittest
from pathlib import Path

from scripts import eval as eval_mod
from scripts import verify_citations as vc

REPO_ROOT = Path(__file__).resolve().parents[1]


class TestFrontmatterQuoting(unittest.TestCase):
    """eval.py's YAML-ish parser must handle both quote styles."""

    def test_unquote_double(self):
        self.assertEqual(eval_mod._unquote('"§ 1 KSchG"'), "§ 1 KSchG")

    def test_unquote_single(self):
        self.assertEqual(eval_mod._unquote("'§ 1 KSchG'"), "§ 1 KSchG")

    def test_unquote_single_wrapping_a_double(self):
        # The case that broke: the value itself contains a double quote, so YAML
        # requires single-quote delimiters.
        self.assertEqual(
            eval_mod._unquote("""'Software als „kein Produkt" abgetan'"""),
            'Software als „kein Produkt" abgetan',
        )

    def test_unquote_leaves_bare_value_alone(self):
        self.assertEqual(eval_mod._unquote("§ 1 KSchG"), "§ 1 KSchG")

    def test_unquote_leaves_mismatched_delimiters_alone(self):
        self.assertEqual(eval_mod._unquote("\"unbalanced'"), "\"unbalanced'")

    def test_unquote_handles_short_strings(self):
        for value in ("", "'", '"', "x"):
            self.assertEqual(eval_mod._unquote(value), value)


class TestTestFileAssertionsParse(unittest.TestCase):
    """Every test.md must yield assertions the eval harness can actually use.

    A test.md whose frontmatter fails to parse does not fail loudly — the skill
    simply drops out of the eval config. This makes that silent.
    """

    def test_every_test_md_declares_parseable_assertions(self):
        empty: list[str] = []
        for test_md in sorted(REPO_ROOT.glob("*/skills/*/test.md")):
            meta = eval_mod.parse_test(test_md)
            if not (meta.get("must_cite") or meta.get("must_appear") or meta.get("must_flag")):
                empty.append(str(test_md.relative_to(REPO_ROOT)))
        self.assertEqual(empty, [], f"test.md files with no parseable assertions: {empty}")

    def test_every_assertion_is_stripped_of_its_quotes(self):
        leftover: list[str] = []
        for test_md in sorted(REPO_ROOT.glob("*/skills/*/test.md")):
            meta = eval_mod.parse_test(test_md)
            for key in ("must_cite", "must_appear", "must_flag"):
                for value in meta.get(key, []) or []:
                    if value[:1] in ('"', "'") and value[-1:] == value[:1]:
                        leftover.append(f"{test_md.relative_to(REPO_ROOT)}::{key}::{value}")
        self.assertEqual(leftover, [], f"assertions still carrying quote delimiters: {leftover}")


class TestStatuteSlugs(unittest.TestCase):
    """The abbreviation -> gesetze-im-internet.de slug map."""

    def test_uwg_resolves_to_the_slug_the_site_actually_serves(self):
        self.assertEqual(vc.STATUTE_SLUGS["UWG"], "uwg_2004")
        self.assertEqual(
            vc.statute_url("UWG", "3a", "§"),
            "https://www.gesetze-im-internet.de/uwg_2004/__3a.html",
        )

    def test_boersg_uses_the_underscore_umlaut_slug(self):
        # gesetze-im-internet.de writes the umlaut as an underscore.
        self.assertEqual(vc.STATUTE_SLUGS["BörsG"], "b_rsg_2007")

    def test_egbgb_has_no_derived_per_article_url(self):
        # gesetze-im-internet.de serves the EGBGB as one consolidated document,
        # so a derived art_<n>.html always 404s. It must be reported against the
        # full text instead of being resolved article-by-article.
        self.assertIn("EGBGB", vc.NO_PER_ARTICLE_PAGE)

    def test_new_area_abbreviations_are_known(self):
        for abbr, slug in (
            ("DADG", "dadg"),
            ("BFSG", "bfsg"),
            ("BFSGV", "bfsgv"),
            ("BGG", "bgg"),
            ("HwO", "hwo"),
            ("MaBV", "gewo_34cdv"),
            ("MediationsG", "mediationsg"),
        ):
            with self.subTest(abbr=abbr):
                self.assertEqual(vc.STATUTE_SLUGS.get(abbr), slug)

    def test_subdivision_markers_are_not_read_as_statutes(self):
        # "Art. 50 UAbs. 6" and "§ 18 und CE-Kennzeichnung" used to be reported
        # as citations of unknown laws named "UAbs" and "CE".
        for token in ("UAbs", "Unterabs", "CE"):
            with self.subTest(token=token):
                self.assertIn(token, vc.NON_STATUTE_TOKENS)


class TestCatalogConsistency(unittest.TestCase):
    """The generated catalog must describe the tree it was built from."""

    def test_area_lists_agree_across_the_toolchain(self):
        from scripts import validate as validate_mod
        from scripts import build_skills_json as build_mod

        on_disk = {
            p.name
            for p in REPO_ROOT.iterdir()
            if p.is_dir() and (p / ".claude-plugin" / "plugin.json").exists()
        }
        self.assertEqual(set(validate_mod.AREAS), on_disk, "validate.py AREAS drifted from disk")
        self.assertEqual(set(eval_mod.AREAS), on_disk, "eval.py AREAS drifted from disk")
        self.assertEqual(
            set(build_mod.DOMAINS_ORDER), on_disk, "build_skills_json.py DOMAINS_ORDER drifted from disk"
        )

    def test_skill_version_tracks_the_plugin_not_a_frozen_literal(self):
        from scripts import build_skills_json as build_mod

        # Was hardcoded "0.1.0" for all 275 skills, so every skill page on the
        # site showed a version chip frozen at the first release.
        for domain in build_mod.DOMAINS_ORDER:
            with self.subTest(domain=domain):
                declared = json.loads(
                    (REPO_ROOT / domain / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8")
                )["version"]
                self.assertEqual(build_mod.plugin_version(domain), declared)

    def test_all_plugin_versions_agree_with_the_catalog(self):
        catalog = json.loads((REPO_ROOT / "skills.json").read_text(encoding="utf-8"))
        versions = {
            json.loads((REPO_ROOT / d / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))["version"]
            for d in (p.name for p in REPO_ROOT.iterdir()
                      if p.is_dir() and (p / ".claude-plugin" / "plugin.json").exists())
        }
        self.assertEqual(len(versions), 1, f"plugin.json versions disagree: {sorted(versions)}")
        self.assertEqual(catalog["version"], versions.pop())

    def test_every_domain_has_display_metadata(self):
        from scripts import build_skills_json as build_mod

        missing = [d for d in build_mod.DOMAINS_ORDER if d not in build_mod.DOMAIN_META]
        self.assertEqual(missing, [], f"domains without DOMAIN_META label/description: {missing}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
