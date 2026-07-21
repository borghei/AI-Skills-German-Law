#!/usr/bin/env python3
"""
generate_site.py — Static site generator for AI Skills German Law.

Reads skills.json and SKILL.md files to generate a complete static website
in the site/ directory with skill pages, domain pages, getting-started guides,
how-to guides, reference pages, sitemap, robots.txt, llms.txt, and a 404 page.

Site shell (nav, structural copy, breadcrumbs, headings) is English.
Skill bodies (Zweck, Eingaben, ...) keep their original German content,
but the section H2 labels are rendered in English (Purpose, Inputs, ...).

Usage:
    python scripts/generate_site.py                          # Full site
    python scripts/generate_site.py --skill abmahnung        # One skill
    python scripts/generate_site.py --domain arbeitsrecht    # One domain
"""

import argparse
import json
import os
import re
import shutil
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from html import escape

# ---------------------------------------------------------------------------
# Paths and constants
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
SKILLS_JSON = REPO_ROOT / "skills.json"
SITE_DIR = REPO_ROOT / "site"
BASE_URL = "https://borghei.github.io/AI-Skills-German-Law"
GITHUB_URL = "https://github.com/borghei/AI-Skills-German-Law"
BRAND = "AI Skills German Law"
AUTHOR = "Borghei"

# ---------------------------------------------------------------------------
# Languages
#
# URL layout: English lives at the site root (those URLs are live and linked
# from README.md / skills.json, so they must not move). German lives under
# /de/ mirroring the same tree.
#
#   /            <-> /de/
#   /SKILLS/     <-> /de/SKILLS/
#   /guides/...  <-> /de/guides/...
#
# One sitemap.xml at the root covers both trees with hreflang alternates.
# ---------------------------------------------------------------------------

LANGS = ("en", "de")
OTHER_LANG = {"en": "de", "de": "en"}
OG_LOCALE = {"en": "en_US", "de": "de_DE"}
LANG_DIR = {"en": "", "de": "de"}


def lang_base(lang):
    """Absolute base URL for a language tree (no trailing slash)."""
    d = LANG_DIR[lang]
    return BASE_URL if not d else f"{BASE_URL}/{d}"


def url_for(lang, rel=""):
    """Absolute URL for a site-relative path (no leading slash).

    rel="" -> tree root; rel="SKILLS/" -> index; rel="SKILLS/a/b.html" -> page.
    """
    return f"{lang_base(lang)}/{rel}"


def out_path(lang, rel_file):
    """Filesystem output path for a site-relative file path."""
    d = LANG_DIR[lang]
    return SITE_DIR / rel_file if not d else SITE_DIR / d / rel_file


# ---------------------------------------------------------------------------
# STRINGS — every user-visible chrome/content string, per language.
#
# German copy targets German lawyers: Sie-form, established terminology
# (Rechtsgebiete, Erste Schritte, Anleitungen, Referenz, Schnelleinstieg).
# Skill *bodies* stay German in both trees — the legal content is German by
# nature. Only the surrounding UI, navigation and guide pages are translated.
# ---------------------------------------------------------------------------

STRINGS = {
    "en": {
        # -- chrome ---------------------------------------------------------
        "nav_skills": "Skills",
        "nav_getting_started": "Getting Started",
        "nav_guides": "Guides",
        "nav_reference": "Reference",
        "nav_github": "GitHub",
        "lang_switch_label": "Language",
        "lang_en": "EN",
        "lang_de": "DE",
        "lang_en_title": "English",
        "lang_de_title": "Deutsch",
        "footer_license": "Apache-2.0 OR MIT",
        "footer_built_by": "Built by",
        "bc_home": "Home",
        "bc_skills": "Skills",
        "bc_getting_started": "Getting Started",
        "bc_guides": "Guides",
        "bc_reference": "Reference",
        # -- shared fragments ------------------------------------------------
        "count_skills": "{n} skills",
        "count_skill_one": "1 skill",
        "count_tools": "{n} tools",
        "count_tool_one": "1 tool",
        "more_n": "+{n} more",
        "badge_references": "references",
        "search_placeholder_all": "Search {n} skills...",
        "search_placeholder_area": "Search {area} skills...",
        "german_content_note": (
            "Skill texts are written in German. That is intentional: these are drafting "
            "instructions for German legal practice, and the deliverables (Abmahnung, "
            "Schriftsatz, Memo) must be in German. The site around them is available in "
            "English and German."
        ),
        # -- landing ---------------------------------------------------------
        "landing_title": "{brand}: AI skills for German legal practice and EU compliance",
        "landing_description": (
            "{areas} areas, {total} skills, multi-provider (Claude, Gemini, GPT). "
            "Primary-source citations linked to gesetze-im-internet.de and EUR-Lex. "
            "Built for Kanzleien, in-house counsel, and EU compliance teams."
        ),
        "hero_title": "AI skills for German legal practice and EU compliance.",
        "hero_subtitle": (
            "Draft a BAG-konforme Abmahnung. Run a DSGVO Art. 15 workflow. Build a KI-VO "
            "compliance plan. Tested, sourced, multi-provider. Paste into any AI chat or "
            "install via Claude Code, Gemini, or GPT."
        ),
        "stat_areas": "Areas",
        "stat_skills": "Skills",
        "stat_providers": "Providers",
        "stat_frameworks": "Compliance Frameworks",
        "btn_browse_skills": "Browse skills",
        "btn_getting_started": "Getting started",
        "disclaimer": (
            "<strong>This project is built with the assistance of AI tools.</strong> "
            "AI-generated content may contain errors. <strong>This is not legal advice.</strong> "
            "Any output is a draft for review by a licensed Rechtsanwalt or Syndikusrechtsanwalt "
            "under &sect; 43a BRAO and &sect; 2 BORA. Verify case-law citations in Beck-Online, "
            "juris, or openjur.net before client- or court-facing use. The author accepts no "
            "liability. <strong>Use at your own risk.</strong>"
        ),
        "featured_areas": "Featured Areas",
        "featured_areas_note": (
            "{areas} areas total covering substantive German law, Fachanwaltschaften, "
            "EU compliance frameworks, and specialty domains."
        ),
        "view_all_areas": "View all {areas} areas",
        # -- skills index ----------------------------------------------------
        "skills_index_title": "All Skills - {brand}",
        "skills_index_description": "{total} German-law and EU-compliance skills across {areas} areas.",
        "skills_catalog_h1": "Skill Catalog",
        "browse_by_area": "Browse by Area",
        "all_skills_h": "All Skills",
        "filter_all_areas": "All Areas",
        # -- area page -------------------------------------------------------
        "area_description": "{n} skills in {area}. {desc}",
        "area_desc_fallback": "Skills in the {area} area",
        # -- skill page ------------------------------------------------------
        "related_skills_in": "Related Skills in {area}",
        "view_skill_md": "View SKILL.md on GitHub",
        # -- 404 -------------------------------------------------------------
        "p404_title": "404 - Page Not Found",
        "p404_text": "The page you are looking for does not exist or has moved.",
        "btn_go_home": "Go home",
        "p404_other_tree": "Deutsche Fassung",
        # -- getting started -------------------------------------------------
        "gs_title": "Getting Started",
        "gs_subtitle": "Install AI Skills German Law and run your first skill in under a minute.",
        # -- installation ----------------------------------------------------
        "install_title": "Installation",
        "install_subtitle": "Add AI Skills German Law to Claude Code, clone the repo, or copy individual skills.",
        # -- platforms -------------------------------------------------------
        "platforms_title": "Platforms",
        "platforms_subtitle": "Provider-specific setup for Claude Code, Claude.ai, Gemini, ChatGPT, Cursor, and other AI assistants.",
        # -- quick start -----------------------------------------------------
        "qs_title": "Quick Start",
        "qs_subtitle": "Run your first German-law skill in 60 seconds.",
        # -- guides ----------------------------------------------------------
        "authoring_title": "Authoring Skills",
        "authoring_subtitle": "How to write a new skill that fits the repository conventions.",
        "bundles_title": "Bundles",
        "bundles_subtitle": "Group related skills into workflows that span multiple areas.",
        "custom_title": "Customization",
        "custom_subtitle": "Fork, override, and extend skills for your Kanzlei or compliance team.",
        "orch_title": "Orchestration",
        "orch_subtitle": "How researcher, drafter, and reviewer agents work together inside every skill.",
        # -- reference -------------------------------------------------------
        "ref_title": "Reference",
        "ref_subtitle": "Binding documentation that every skill in the repository follows.",
        # -- llms.txt --------------------------------------------------------
        "llms_tagline": (
            "Provider-neutral AI skills for German legal practice and EU compliance -- "
            "{total} skills across {areas} areas. Outputs in German; statute citations "
            "linked to gesetze-im-internet.de and EUR-Lex."
        ),
        "llms_website": "Website",
        "llms_repository": "Repository",
        "llms_license": "License",
        "llms_author": "Author",
        "llms_h_what": "## What This Is",
        "llms_what": (
            "A library of provider-neutral skills (Claude, Gemini, OpenAI) for German legal practice. "
            "Each skill ships with a researcher / drafter / reviewer sub-agent architecture, linked "
            "statute citations, and case-law marked verified or [unverifiziert -- prüfen]. Outputs are "
            "drafts for review by a licensed Rechtsanwalt under § 43a BRAO and § 2 BORA."
        ),
        "llms_h_how": "## How to Use",
        "llms_h_areas": "## Areas",
        "llms_h_all": "## All Skills",
        "llms_h_lang": "## Languages",
        "llms_lang": (
            "This document describes the English site tree at {en_url}. "
            "A German tree with identical coverage is at {de_url} (llms.txt: {de_llms})."
        ),
    },
    "de": {
        # -- chrome ---------------------------------------------------------
        "nav_skills": "Skills",
        "nav_getting_started": "Erste Schritte",
        "nav_guides": "Anleitungen",
        "nav_reference": "Referenz",
        "nav_github": "GitHub",
        "lang_switch_label": "Sprache",
        "lang_en": "EN",
        "lang_de": "DE",
        "lang_en_title": "English",
        "lang_de_title": "Deutsch",
        "footer_license": "Apache-2.0 ODER MIT",
        "footer_built_by": "Erstellt von",
        "bc_home": "Startseite",
        "bc_skills": "Skills",
        "bc_getting_started": "Erste Schritte",
        "bc_guides": "Anleitungen",
        "bc_reference": "Referenz",
        # -- shared fragments ------------------------------------------------
        "count_skills": "{n} Skills",
        "count_skill_one": "1 Skill",
        "count_tools": "{n} Tools",
        "count_tool_one": "1 Tool",
        "more_n": "+{n} weitere",
        "badge_references": "Referenzen",
        "search_placeholder_all": "{n} Skills durchsuchen ...",
        "search_placeholder_area": "Skills in {area} durchsuchen ...",
        "german_content_note": (
            "Die Skill-Texte sind durchgehend deutsch. Das ist beabsichtigt: Es handelt sich um "
            "Arbeitsanweisungen für die deutsche Rechtspraxis, und die Arbeitsergebnisse "
            "(Abmahnung, Schriftsatz, Vermerk) müssen deutsch sein. Die Benutzeroberfläche steht "
            "auf Deutsch und Englisch zur Verfügung."
        ),
        # -- landing ---------------------------------------------------------
        "landing_title": "{brand}: KI-Skills für die deutsche Rechtspraxis und EU-Compliance",
        "landing_description": (
            "{areas} Rechtsgebiete, {total} Skills, anbieterübergreifend (Claude, Gemini, GPT). "
            "Normzitate verlinkt auf gesetze-im-internet.de und EUR-Lex. "
            "Für Kanzleien, Rechtsabteilungen und EU-Compliance-Teams."
        ),
        "hero_title": "KI-Skills für die deutsche Rechtspraxis und EU-Compliance.",
        "hero_subtitle": (
            "BAG-konforme Abmahnung entwerfen. Auskunftsverlangen nach Art. 15 DSGVO bearbeiten. "
            "KI-VO-Compliance-Plan aufsetzen. Getestet, mit Quellen belegt, anbieterübergreifend. "
            "In jeden KI-Chat einfügen oder über Claude Code, Gemini oder GPT installieren."
        ),
        "stat_areas": "Rechtsgebiete",
        "stat_skills": "Skills",
        "stat_providers": "Anbieter",
        "stat_frameworks": "Compliance-Rahmenwerke",
        "btn_browse_skills": "Skills durchsuchen",
        "btn_getting_started": "Erste Schritte",
        "disclaimer": (
            "<strong>Dieses Projekt wurde unter Einsatz von KI-Werkzeugen erstellt.</strong> "
            "KI-generierte Inhalte können Fehler enthalten. "
            "<strong>Dies ist keine Rechtsberatung.</strong> "
            "Jede Ausgabe ist ein Entwurf zur Prüfung durch eine zugelassene Rechtsanwältin oder "
            "einen zugelassenen Rechtsanwalt bzw. Syndikusrechtsanwalt nach &sect; 43a BRAO und "
            "&sect; 2 BORA. Prüfen Sie Rechtsprechungsnachweise vor jeder mandats- oder "
            "gerichtsbezogenen Verwendung in Beck-Online, juris oder openjur.net. Der Autor "
            "übernimmt keine Haftung. <strong>Nutzung auf eigenes Risiko.</strong>"
        ),
        "featured_areas": "Ausgewählte Rechtsgebiete",
        "featured_areas_note": (
            "Insgesamt {areas} Rechtsgebiete: materielles deutsches Recht, Fachanwaltschaften, "
            "EU-Compliance-Rahmenwerke und Spezialgebiete."
        ),
        "view_all_areas": "Alle {areas} Rechtsgebiete ansehen",
        # -- skills index ----------------------------------------------------
        "skills_index_title": "Alle Skills - {brand}",
        "skills_index_description": "{total} Skills zum deutschen Recht und zur EU-Compliance in {areas} Rechtsgebieten.",
        "skills_catalog_h1": "Skill-Katalog",
        "browse_by_area": "Nach Rechtsgebiet",
        "all_skills_h": "Alle Skills",
        "filter_all_areas": "Alle Rechtsgebiete",
        # -- area page -------------------------------------------------------
        "area_description": "{n} Skills im Rechtsgebiet {area}. {desc}",
        "area_desc_fallback": "Skills im Rechtsgebiet {area}",
        # -- skill page ------------------------------------------------------
        "related_skills_in": "Verwandte Skills in {area}",
        "view_skill_md": "SKILL.md auf GitHub ansehen",
        # -- 404 -------------------------------------------------------------
        "p404_title": "404 - Seite nicht gefunden",
        "p404_text": "Die aufgerufene Seite existiert nicht oder wurde verschoben.",
        "btn_go_home": "Zur Startseite",
        "p404_other_tree": "English version",
        # -- getting started -------------------------------------------------
        "gs_title": "Erste Schritte",
        "gs_subtitle": "AI Skills German Law installieren und den ersten Skill in unter einer Minute ausführen.",
        # -- installation ----------------------------------------------------
        "install_title": "Installation",
        "install_subtitle": "AI Skills German Law in Claude Code einbinden, das Repository klonen oder einzelne Skills kopieren.",
        # -- platforms -------------------------------------------------------
        "platforms_title": "Plattformen",
        "platforms_subtitle": "Einrichtung je Anbieter: Claude Code, Claude.ai, Gemini, ChatGPT, Cursor und weitere KI-Assistenten.",
        # -- quick start -----------------------------------------------------
        "qs_title": "Schnelleinstieg",
        "qs_subtitle": "Den ersten Skill zum deutschen Recht in 60 Sekunden ausführen.",
        # -- guides ----------------------------------------------------------
        "authoring_title": "Skills schreiben",
        "authoring_subtitle": "Wie Sie einen neuen Skill schreiben, der den Konventionen des Repositorys entspricht.",
        "bundles_title": "Bundles",
        "bundles_subtitle": "Zusammengehörige Skills zu Arbeitsabläufen über mehrere Rechtsgebiete hinweg bündeln.",
        "custom_title": "Anpassung",
        "custom_subtitle": "Skills forken, überschreiben und an Ihre Kanzlei oder Ihr Compliance-Team anpassen.",
        "orch_title": "Orchestrierung",
        "orch_subtitle": "Wie Researcher-, Drafter- und Reviewer-Agenten in jedem Skill zusammenwirken.",
        # -- reference -------------------------------------------------------
        "ref_title": "Referenz",
        "ref_subtitle": "Verbindliche Dokumentation, der jeder Skill des Repositorys folgt.",
        # -- llms.txt --------------------------------------------------------
        "llms_tagline": (
            "Anbieterneutrale KI-Skills für die deutsche Rechtspraxis und EU-Compliance -- "
            "{total} Skills in {areas} Rechtsgebieten. Ausgaben auf Deutsch; Normzitate verlinkt "
            "auf gesetze-im-internet.de und EUR-Lex."
        ),
        "llms_website": "Website",
        "llms_repository": "Repository",
        "llms_license": "Lizenz",
        "llms_author": "Autor",
        "llms_h_what": "## Worum es geht",
        "llms_what": (
            "Eine Bibliothek anbieterneutraler Skills (Claude, Gemini, OpenAI) für die deutsche "
            "Rechtspraxis. Jeder Skill bringt eine Sub-Agent-Architektur aus Researcher, Drafter und "
            "Reviewer mit, verlinkte Normzitate sowie Rechtsprechungsnachweise, die als geprüft oder "
            "als [unverifiziert -- prüfen] gekennzeichnet sind. Ausgaben sind Entwürfe zur Prüfung "
            "durch eine zugelassene Rechtsanwältin oder einen zugelassenen Rechtsanwalt nach "
            "§ 43a BRAO und § 2 BORA."
        ),
        "llms_h_how": "## Verwendung",
        "llms_h_areas": "## Rechtsgebiete",
        "llms_h_all": "## Alle Skills",
        "llms_h_lang": "## Sprachen",
        "llms_lang": (
            "Dieses Dokument beschreibt den deutschen Seitenbaum unter {de_url}. "
            "Ein englischer Baum mit identischem Umfang liegt unter {en_url} (llms.txt: {en_llms})."
        ),
    },
}


def T(lang, key, **kw):
    """Look up a UI string. Raises loudly on a missing language or key."""
    try:
        table = STRINGS[lang]
    except KeyError:
        raise KeyError(f"STRINGS: unknown language {lang!r}") from None
    try:
        s = table[key]
    except KeyError:
        raise KeyError(f"STRINGS[{lang!r}]: missing key {key!r}") from None
    return s.format(**kw) if kw else s


def _assert_strings_parity():
    """Both language tables must define exactly the same keys."""
    en, de = set(STRINGS["en"]), set(STRINGS["de"])
    if en != de:
        raise KeyError(
            "STRINGS key mismatch — en-only: {} | de-only: {}".format(
                sorted(en - de), sorted(de - en)
            )
        )


def n_skills(lang, n):
    """'1 skill' / '{n} skills' with correct German forms."""
    return T(lang, "count_skill_one") if n == 1 else T(lang, "count_skills", n=n)


def n_tools(lang, n):
    return T(lang, "count_tool_one") if n == 1 else T(lang, "count_tools", n=n)

# ---------------------------------------------------------------------------
# Inline SVG icons (16x16 line icons)
# ---------------------------------------------------------------------------

SVG_ICONS = {
    "arrow-right": '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>',
    "github": '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>',
    "tools": '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg>',
    "folder": '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 01-2 2H4a2 2 0 01-2-2V5a2 2 0 012-2h5l2 3h9a2 2 0 012 2z"/></svg>',
    "terminal": '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="4 17 10 11 4 5"/><line x1="12" y1="19" x2="20" y2="19"/></svg>',
    "search": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>',
    "external": '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>',
    "book": '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>',
}

# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_catalog():
    """Load skills.json catalog."""
    with open(SKILLS_JSON, "r", encoding="utf-8") as f:
        return json.load(f)


def load_skill_md(skill_path):
    """Read a SKILL.md file and return its raw text, or empty string."""
    full = REPO_ROOT / skill_path
    if full.exists():
        return full.read_text(encoding="utf-8")
    return ""


# ---------------------------------------------------------------------------
# DOMAIN_META — built from skills.json `domains` dict at script start
# ---------------------------------------------------------------------------

def build_domain_meta(catalog):
    """Build DOMAIN_META from skills.json's `domains` dict."""
    meta = {}
    for key, info in catalog.get("domains", {}).items():
        meta[key] = {
            "label": info.get("label", key.replace("-", " ").title()),
            "desc": info.get("desc", ""),
            "count": info.get("count", 0),
            "tools": info.get("tools", 0),
        }
    return meta


# DOMAIN_META gets populated in main(); accessed via the helpers below.
DOMAIN_META = {}


# ---------------------------------------------------------------------------
# Section title map — German source → English UI heading
# (Body content stays German, headings render in English.)
# ---------------------------------------------------------------------------

GERMAN_TO_ENGLISH_HEADING = {
    # H2-level section names in SKILL.md
    "zweck": "Purpose",
    "eingaben": "Inputs",
    "sub-agent-architektur": "Sub-Agent Architecture",
    "ablauf": "Process",
    "quellen": "Sources",
    "quellen und zitierweise": "Sources and Citations",
    "ausgabeformat": "Output Format",
    "risiken": "Risks",
    "risiken / typische fehler": "Risks and Common Mistakes",
    "typische fehler": "Common Mistakes",
    # Less common but seen in some skills:
    "vorgehen": "Process",
    "tools": "Tools",
    "rechtsgrundlagen": "Legal Basis",
    "abgrenzung": "Scope",
    "beispiele": "Examples",
}


def translate_heading(german_title, lang="en"):
    """Map a German H2 heading to its English UI equivalent.

    Only applies in the English tree. In the German tree the original headings
    (Zweck, Eingaben, Ablauf, Quellen, Ausgabeformat, Risiken / typische Fehler)
    are already correct German and are kept verbatim.
    """
    title = german_title.strip()
    if lang != "en":
        return title
    return GERMAN_TO_ENGLISH_HEADING.get(title.lower(), title)


# ---------------------------------------------------------------------------
# Minimal Markdown → HTML conversion (regex-based; no external deps)
# ---------------------------------------------------------------------------

def _md_inline(text):
    """Inline markdown: links, bold, italics, inline code."""
    # Inline code first (so its contents are not further parsed)
    placeholders = []

    def _stash(m):
        placeholders.append(f"<code>{escape(m.group(1))}</code>")
        return f"\x00{len(placeholders) - 1}\x00"

    text = re.sub(r"`([^`]+)`", _stash, text)
    # Now escape the rest
    text = escape(text, quote=False)
    # Bold **x** and __x__
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"__([^_]+)__", r"<strong>\1</strong>", text)
    # Italic *x* and _x_
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"(?<![A-Za-z0-9_])_([^_\n]+)_(?![A-Za-z0-9_])", r"<em>\1</em>", text)
    # Links [text](url)
    text = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>',
        text,
    )
    # Restore inline code placeholders
    for i, ph in enumerate(placeholders):
        text = text.replace(f"\x00{i}\x00", ph)
    return text


def md_to_html(md_text):
    """Convert a Markdown string to HTML.

    Supports: H2/H3 (skipped — caller already renders section headings),
    paragraphs, unordered/ordered lists, GFM tables, fenced code blocks,
    blockquotes, inline links/bold/italic/code, and horizontal rules.
    """
    lines = md_text.splitlines()
    out = []
    i = 0
    n = len(lines)

    def _is_blank(s):
        return s.strip() == ""

    while i < n:
        line = lines[i]

        # Fenced code
        m = re.match(r"^```(\w*)\s*$", line)
        if m:
            i += 1
            buf = []
            while i < n and not re.match(r"^```\s*$", lines[i]):
                buf.append(lines[i])
                i += 1
            if i < n:
                i += 1  # consume closing fence
            code_html = escape("\n".join(buf))
            out.append(f"<pre><code>{code_html}</code></pre>")
            continue

        # Horizontal rule
        if re.match(r"^---+\s*$", line) and (i + 1 >= n or _is_blank(lines[i + 1])):
            # Skip — we use section H2s as visual dividers
            i += 1
            continue

        # Headings inside body — render as H3 (the outer H2 is the section title)
        m = re.match(r"^####\s+(.+)$", line)
        if m:
            out.append(f"<h4>{_md_inline(m.group(1))}</h4>")
            i += 1
            continue
        m = re.match(r"^###\s+(.+)$", line)
        if m:
            out.append(f"<h3>{_md_inline(m.group(1))}</h3>")
            i += 1
            continue
        m = re.match(r"^##\s+(.+)$", line)
        if m:
            # Should not happen here (caller splits on H2s), but be safe.
            out.append(f"<h3>{_md_inline(m.group(1))}</h3>")
            i += 1
            continue

        # Tables (GFM)
        if "|" in line and i + 1 < n and re.match(r"^\s*\|?[\s\-:|]+\|[\s\-:|]+", lines[i + 1]):
            header_cells = [c.strip() for c in line.strip().strip("|").split("|")]
            i += 2  # skip header + separator
            rows = []
            while i < n and "|" in lines[i] and not _is_blank(lines[i]):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            thead = "<tr>" + "".join(f"<th>{_md_inline(c)}</th>" for c in header_cells) + "</tr>"
            tbody = "".join(
                "<tr>" + "".join(f"<td>{_md_inline(c)}</td>" for c in row) + "</tr>"
                for row in rows
            )
            out.append(f"<table><thead>{thead}</thead><tbody>{tbody}</tbody></table>")
            continue

        # Blockquote
        if line.startswith(">"):
            buf = []
            while i < n and lines[i].startswith(">"):
                buf.append(lines[i].lstrip(">").lstrip())
                i += 1
            out.append(f"<blockquote>{_md_inline(' '.join(buf))}</blockquote>")
            continue

        # Unordered list
        if re.match(r"^[-*]\s+", line):
            items = []
            while i < n and re.match(r"^[-*]\s+", lines[i]):
                item = re.sub(r"^[-*]\s+", "", lines[i])
                # Greedily consume continuation lines (indented or non-blank, non-list)
                i += 1
                while i < n and lines[i].startswith("  ") and not re.match(r"^\s*[-*]\s+", lines[i]):
                    item += " " + lines[i].strip()
                    i += 1
                items.append(f"<li>{_md_inline(item)}</li>")
            out.append(f"<ul>{''.join(items)}</ul>")
            continue

        # Ordered list
        if re.match(r"^\d+\.\s+", line):
            items = []
            while i < n and re.match(r"^\d+\.\s+", lines[i]):
                item = re.sub(r"^\d+\.\s+", "", lines[i])
                i += 1
                while i < n and lines[i].startswith("   ") and not re.match(r"^\s*\d+\.\s+", lines[i]):
                    item += " " + lines[i].strip()
                    i += 1
                items.append(f"<li>{_md_inline(item)}</li>")
            out.append(f"<ol>{''.join(items)}</ol>")
            continue

        # Blank line
        if _is_blank(line):
            i += 1
            continue

        # Paragraph (collect until blank/heading/list)
        buf = [line]
        i += 1
        while i < n and not _is_blank(lines[i]) and not re.match(
            r"^(#{1,4}\s+|[-*]\s+|\d+\.\s+|```|>|---+\s*$)", lines[i]
        ) and "|" not in lines[i]:
            buf.append(lines[i])
            i += 1
        out.append(f"<p>{_md_inline(' '.join(buf))}</p>")

    return "\n".join(out)


# ---------------------------------------------------------------------------
# SKILL.md parsing — split into sections by H2 headings
# ---------------------------------------------------------------------------

def parse_skill_md(md_text):
    """Strip YAML frontmatter and split the body into (german_heading, body_md) tuples.

    Also returns the intro paragraph that appears before the first H2 (if any).
    """
    # Strip frontmatter
    body = md_text
    if body.startswith("---"):
        end = body.find("\n---", 3)
        if end != -1:
            body = body[end + 4:].lstrip("\n")

    # Drop the leading H1 (skill name) if present
    body = re.sub(r"^#\s+[^\n]+\n+", "", body)

    sections = []
    intro_lines = []
    current_heading = None
    current_buf = []

    for line in body.splitlines():
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            if current_heading is None:
                # Everything before the first H2 is the intro
                intro_lines = current_buf[:]
            else:
                sections.append((current_heading, "\n".join(current_buf).strip()))
            current_heading = m.group(1).strip()
            current_buf = []
        else:
            current_buf.append(line)

    if current_heading is not None:
        sections.append((current_heading, "\n".join(current_buf).strip()))
    else:
        intro_lines = current_buf[:]

    intro = "\n".join(intro_lines).strip()
    return intro, sections


# ---------------------------------------------------------------------------
# HTML template system
# ---------------------------------------------------------------------------

def _css():
    """Inline CSS — cream/terracotta design system matching Claude-Skills."""
    return """
:root {
  --bg: #faf9f5;
  --bg-secondary: #f0eee6;
  --text: #141413;
  --text-muted: #5e5d59;
  --accent: #d97757;
  --accent-deep: #c6613f;
  --border: rgba(20,20,19,0.1);
  --border-strong: rgba(20,20,19,0.18);
  --white: #ffffff;
  --radius: 8px;
  --radius-lg: 12px;
  --font-serif: Georgia, 'Times New Roman', serif;
  --font-sans: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-mono: 'SF Mono', SFMono-Regular, ui-monospace, 'Cascadia Code', Menlo, monospace;
  --max-width: 1200px;
  --shadow-sm: 0 1px 2px rgba(20,20,19,0.04);
  --shadow: 0 1px 3px rgba(20,20,19,0.06), 0 1px 2px rgba(20,20,19,0.04);
  --shadow-md: 0 4px 12px rgba(20,20,19,0.08), 0 1px 3px rgba(20,20,19,0.06);
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; -webkit-font-smoothing: antialiased; }
body {
  font-family: var(--font-sans);
  background: var(--bg);
  color: var(--text);
  line-height: 1.6;
  overflow-x: hidden;
}
a { color: var(--accent); text-decoration: none; transition: color 0.15s; }
a:hover { color: var(--accent-deep); }
.container { max-width: var(--max-width); margin: 0 auto; padding: 0 24px; }
code { font-family: var(--font-mono); font-size: 0.875em; }

/* Navbar */
.navbar {
  position: sticky; top: 0; z-index: 100;
  background: rgba(250,249,245,0.92); backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border);
  padding: 14px 0;
}
.navbar .container { display: flex; align-items: center; justify-content: space-between; }
.nav-logo {
  font-family: var(--font-serif); font-weight: 700; font-size: 1.1rem;
  color: var(--text); letter-spacing: -0.01em;
}
.nav-logo:hover { color: var(--text); }
.nav-links { display: flex; gap: 28px; align-items: center; }
.nav-links a {
  color: var(--text-muted); font-size: 0.9rem; font-weight: 500;
  transition: color 0.15s;
}
.nav-links a:hover { color: var(--text); }
.nav-links a.active { color: var(--accent); }
.nav-links a.gh-link { display: inline-flex; align-items: center; gap: 5px; }

/* Language switcher */
.lang-switch {
  display: inline-flex; align-items: center; gap: 6px;
  padding: 3px 10px; border: 1px solid var(--border-strong);
  border-radius: 20px; background: var(--white);
  font-family: var(--font-mono); font-size: 0.75rem; line-height: 1.4;
}
.lang-switch .lang-opt { font-weight: 600; letter-spacing: 0.02em; }
.lang-switch a.lang-opt { color: var(--text-muted); }
.lang-switch a.lang-opt:hover { color: var(--accent); }
.lang-switch .lang-opt.active { color: var(--accent); cursor: default; }
.lang-switch .lang-sep { color: var(--border-strong); }

/* Breadcrumbs */
.breadcrumbs { padding: 20px 0 0; font-size: 0.85rem; color: var(--text-muted); }
.breadcrumbs a { color: var(--text-muted); }
.breadcrumbs a:hover { color: var(--accent); }
.breadcrumbs .sep { margin: 0 8px; opacity: 0.4; }

/* Page header */
.page-header { padding: 48px 0 32px; }
.page-title {
  font-family: var(--font-serif); font-size: clamp(1.75rem, 4vw, 2.75rem);
  font-weight: 700; margin-bottom: 12px; letter-spacing: -0.02em;
  color: var(--text);
}
.page-subtitle { color: var(--text-muted); max-width: 760px; font-size: 1.05rem; line-height: 1.6; }

.count-badge {
  display: inline-block; font-family: var(--font-mono); font-size: 0.8rem;
  color: var(--accent); background: rgba(217,119,87,0.08);
  padding: 2px 10px; border-radius: 20px; margin-left: 8px;
  vertical-align: middle; font-weight: 500;
}

/* Search + Filter */
.filter-bar { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 32px; }
.search-input {
  flex: 1; min-width: 200px; padding: 10px 14px 10px 38px;
  background: var(--white); border: 1px solid var(--border-strong);
  border-radius: var(--radius); color: var(--text); font-family: var(--font-sans);
  font-size: 0.9rem; outline: none; transition: border-color 0.2s, box-shadow 0.2s;
}
.search-input:focus { border-color: var(--accent); box-shadow: 0 0 0 3px rgba(217,119,87,0.1); }
.search-input::placeholder { color: var(--text-muted); }
.search-wrap { position: relative; flex: 1; min-width: 200px; }
.search-wrap svg { position: absolute; left: 12px; top: 50%; transform: translateY(-50%); color: var(--text-muted); pointer-events: none; }
.filter-select {
  padding: 10px 14px; background: var(--white); border: 1px solid var(--border-strong);
  border-radius: var(--radius); color: var(--text); font-family: var(--font-sans);
  font-size: 0.9rem; outline: none; cursor: pointer;
}
.filter-select:focus { border-color: var(--accent); box-shadow: 0 0 0 3px rgba(217,119,87,0.1); }

/* Card grid */
.skills-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; padding-bottom: 60px; }
.skill-card {
  background: var(--white); border: 1px solid var(--border);
  border-radius: var(--radius-lg); padding: 20px 22px;
  transition: border-color 0.2s, box-shadow 0.2s, transform 0.2s;
  display: flex; flex-direction: column;
}
.skill-card:hover {
  border-color: var(--border-strong);
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
}
.skill-card h3 { font-size: 0.95rem; font-weight: 600; margin-bottom: 6px; }
.skill-card h3 a { color: var(--text); }
.skill-card h3 a:hover { color: var(--accent); }
.skill-card p { font-size: 0.85rem; color: var(--text-muted); line-height: 1.55; flex: 1; }

/* Badges */
.badge-bar { display: flex; gap: 6px; flex-wrap: wrap; margin: 10px 0 6px; }
.badge {
  display: inline-flex; align-items: center; gap: 4px;
  font-family: var(--font-mono); font-size: 0.7rem; padding: 3px 9px;
  border-radius: 5px; font-weight: 500; white-space: nowrap;
}
.badge-domain { background: rgba(217,119,87,0.1); border: 1px solid rgba(217,119,87,0.2); color: var(--accent-deep); }
.badge-subdomain { background: rgba(20,20,19,0.04); border: 1px solid var(--border); color: var(--text-muted); }
.badge-version { background: rgba(20,20,19,0.03); border: 1px solid var(--border); color: var(--text-muted); }
.badge-tools { background: rgba(20,20,19,0.04); border: 1px solid var(--border); color: var(--text-muted); }
.badge-refs { background: rgba(217,119,87,0.06); border: 1px solid rgba(217,119,87,0.15); color: var(--accent); }

/* Tags */
.skill-meta { display: flex; gap: 6px; flex-wrap: wrap; margin-top: 8px; }
.tag {
  font-family: var(--font-mono); font-size: 0.65rem; padding: 2px 8px;
  background: var(--bg-secondary); border: 1px solid var(--border);
  border-radius: 4px; color: var(--text-muted);
}

.example-pills { display: flex; gap: 6px; flex-wrap: wrap; margin-top: 10px; }
.example-pill {
  font-family: var(--font-mono); font-size: 0.65rem; padding: 2px 7px;
  background: var(--bg-secondary); border: 1px solid var(--border);
  border-radius: 4px; color: var(--text-muted);
}

/* Skill detail page */
.skill-detail { padding-bottom: 80px; }
.skill-detail h2 {
  font-family: var(--font-serif); font-size: 1.4rem; font-weight: 700;
  margin: 40px 0 16px; padding-top: 16px;
  border-top: 1px solid var(--border); color: var(--text);
}
.skill-detail h3 { font-size: 1.05rem; font-weight: 600; margin: 20px 0 10px; color: var(--text); }
.skill-detail h4 { font-size: 0.95rem; font-weight: 600; margin: 16px 0 8px; color: var(--text); }
.skill-detail p, .skill-detail li { font-size: 0.95rem; color: var(--text-muted); line-height: 1.7; }
.skill-detail ul, .skill-detail ol { margin-left: 22px; margin-bottom: 16px; }
.skill-detail li { margin-bottom: 6px; }
.skill-detail blockquote {
  border-left: 3px solid var(--accent); padding: 6px 16px; margin: 12px 0;
  background: var(--bg-secondary); border-radius: 0 var(--radius) var(--radius) 0;
  color: var(--text-muted);
}
.skill-detail table {
  width: 100%; border-collapse: collapse; margin: 14px 0 22px;
  font-size: 0.9rem; background: var(--white);
  border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden;
}
.skill-detail th, .skill-detail td {
  padding: 9px 12px; text-align: left; border-bottom: 1px solid var(--border);
  vertical-align: top;
}
.skill-detail th { background: var(--bg-secondary); font-weight: 600; color: var(--text); }
.skill-detail tr:last-child td { border-bottom: none; }
.skill-detail pre {
  background: var(--bg-secondary); border: 1px solid var(--border);
  border-radius: var(--radius); padding: 16px 20px; overflow-x: auto;
  font-family: var(--font-mono); font-size: 0.85rem; line-height: 1.7;
  color: var(--text); margin: 12px 0 20px;
}
.skill-detail code {
  font-family: var(--font-mono); font-size: 0.85rem;
  background: var(--bg-secondary); padding: 2px 6px; border-radius: 4px;
}
.skill-detail pre code { background: none; padding: 0; }

/* Hero (used on landing) */
.hero { padding: 80px 0 60px; }
.hero-title {
  font-family: var(--font-serif); font-size: clamp(2rem, 5vw, 3.4rem);
  font-weight: 700; margin-bottom: 18px; letter-spacing: -0.02em;
  line-height: 1.15; color: var(--text);
}
.hero-subtitle { font-size: 1.15rem; color: var(--text-muted); max-width: 720px; line-height: 1.6; margin-bottom: 28px; }
.stat-row { display: flex; gap: 16px; flex-wrap: wrap; margin-bottom: 28px; color: var(--text-muted); font-size: 0.95rem; }
.stat-row .stat { display: inline-flex; align-items: center; gap: 6px; }
.stat-row .stat strong { color: var(--text); font-family: var(--font-mono); font-size: 1rem; }
.hero-actions { display: flex; gap: 12px; flex-wrap: wrap; }

.disclaimer {
  background: rgba(217,119,87,0.06); border: 1px solid rgba(217,119,87,0.18);
  border-left: 4px solid var(--accent); border-radius: var(--radius);
  padding: 16px 20px; font-size: 0.9rem; color: var(--text-muted);
  margin: 24px 0 40px;
}
.disclaimer strong { color: var(--text); }

/* Buttons */
.btn {
  display: inline-flex; align-items: center; gap: 6px;
  padding: 10px 18px; border-radius: var(--radius); font-size: 0.9rem;
  font-weight: 500; font-family: var(--font-sans);
  border: 1px solid transparent; cursor: pointer;
  transition: background 0.15s, color 0.15s, box-shadow 0.15s;
  text-decoration: none;
}
.btn-primary { background: var(--text); color: var(--bg); border-color: var(--text); }
.btn-primary:hover { background: #2a2a28; color: var(--bg); box-shadow: var(--shadow); }
.btn-secondary { background: transparent; color: var(--text); border-color: var(--border-strong); }
.btn-secondary:hover { background: var(--bg-secondary); color: var(--text); box-shadow: var(--shadow-sm); }

.section-heading {
  font-family: var(--font-serif); font-size: 1.4rem; font-weight: 700;
  margin: 30px 0 20px; color: var(--text);
}

/* Content pages (getting-started / guides / reference) */
.content-page { padding-bottom: 80px; max-width: 760px; }
.content-page h2 {
  font-family: var(--font-serif); font-size: 1.4rem; font-weight: 700;
  margin: 36px 0 14px; color: var(--text);
}
.content-page h3 { font-size: 1.1rem; font-weight: 600; margin: 22px 0 10px; color: var(--text); }
.content-page p, .content-page li { font-size: 0.98rem; color: var(--text-muted); line-height: 1.7; }
.content-page ul, .content-page ol { margin: 8px 0 18px 22px; }
.content-page li { margin-bottom: 6px; }
.content-page pre {
  background: var(--bg-secondary); border: 1px solid var(--border);
  border-radius: var(--radius); padding: 14px 18px; overflow-x: auto;
  font-family: var(--font-mono); font-size: 0.85rem; line-height: 1.7;
  margin: 12px 0 22px;
}
.content-page code {
  font-family: var(--font-mono); font-size: 0.88rem;
  background: var(--bg-secondary); padding: 2px 6px; border-radius: 4px;
}
.content-page pre code { background: none; padding: 0; }
.content-page table {
  width: 100%; border-collapse: collapse; margin: 16px 0;
  border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden;
}
.content-page th, .content-page td {
  padding: 9px 12px; text-align: left; border-bottom: 1px solid var(--border);
}
.content-page th { background: var(--bg-secondary); font-weight: 600; color: var(--text); }

.cards-row { display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px; margin: 16px 0 28px; }
.mini-card {
  background: var(--white); border: 1px solid var(--border);
  border-radius: var(--radius-lg); padding: 18px 20px;
  transition: border-color 0.2s, box-shadow 0.2s, transform 0.2s;
}
.mini-card:hover { border-color: var(--border-strong); box-shadow: var(--shadow-md); transform: translateY(-2px); }
.mini-card h3 { font-size: 0.95rem; font-weight: 600; margin: 0 0 6px; color: var(--text); }
.mini-card p { font-size: 0.85rem; color: var(--text-muted); line-height: 1.55; margin: 0; }
.mini-card a.view-link { display: inline-flex; align-items: center; gap: 4px; font-size: 0.8rem; margin-top: 10px; color: var(--accent); }

/* Footer */
.footer {
  padding: 36px 0; border-top: 1px solid var(--border); margin-top: 40px;
  background: var(--bg);
}
.footer-inner { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px; }
.footer-links { display: flex; align-items: center; gap: 12px; font-size: 0.85rem; color: var(--text-muted); }
.footer-links a { color: var(--text-muted); }
.footer-links a:hover { color: var(--accent); }
.footer-sep { color: var(--border-strong); }
.footer-credit { font-size: 0.85rem; color: var(--text-muted); }
.footer-credit a { color: var(--text); font-weight: 600; }

/* Related skills */
.related-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin-top: 16px; }

@media (max-width: 768px) {
  .skills-grid, .related-grid { grid-template-columns: repeat(2, 1fr); }
  .cards-row { grid-template-columns: 1fr; }
  .nav-links { gap: 14px; }
}
@media (max-width: 480px) {
  .skills-grid, .related-grid { grid-template-columns: 1fr; }
  .filter-bar { flex-direction: column; }
  .nav-links a:not(.gh-link) { font-size: 0.85rem; }
}
"""


def _lang_switch(lang, alt_url):
    """EN/DE switcher.

    `alt_url` is the counterpart URL for the *same* page in the other language.
    If it cannot be computed (None), fall back to the other tree's root rather
    than emitting a broken link.
    """
    other = OTHER_LANG[lang]
    href = alt_url or url_for(other)
    items = []
    for code in LANGS:
        label = T(lang, f"lang_{code}")
        title = T(lang, f"lang_{code}_title")
        if code == lang:
            items.append(
                f'<span class="lang-opt active" aria-current="true" title="{escape(title)}">{escape(label)}</span>'
            )
        else:
            items.append(
                f'<a class="lang-opt" href="{href}" hreflang="{code}" lang="{code}" '
                f'title="{escape(title)}">{escape(label)}</a>'
            )
    return (
        f'<div class="lang-switch" role="group" aria-label="{escape(T(lang, "lang_switch_label"))}">'
        + '<span class="lang-sep">/</span>'.join(items)
        + "</div>"
    )


def _nav(active="", lang="en", alt_url=None):
    """Navigation bar HTML for one language tree."""
    def _cls(name):
        return ' class="active"' if active == name else ""
    gh = SVG_ICONS["github"]
    b = lang_base(lang)
    return f"""<nav class="navbar">
  <div class="container">
    <a href="{b}/" class="nav-logo">{BRAND}</a>
    <div class="nav-links">
      <a href="{b}/SKILLS/"{ _cls("skills")}>{escape(T(lang, "nav_skills"))}</a>
      <a href="{b}/getting-started/"{ _cls("getting-started")}>{escape(T(lang, "nav_getting_started"))}</a>
      <a href="{b}/guides/authoring/"{ _cls("guides")}>{escape(T(lang, "nav_guides"))}</a>
      <a href="{b}/reference/"{ _cls("reference")}>{escape(T(lang, "nav_reference"))}</a>
      <a href="{GITHUB_URL}" target="_blank" rel="noopener" class="gh-link">{gh} {escape(T(lang, "nav_github"))}</a>
      {_lang_switch(lang, alt_url)}
    </div>
  </div>
</nav>"""


def _footer(lang="en"):
    b = lang_base(lang)
    return f"""<footer class="footer">
  <div class="container footer-inner">
    <div class="footer-links">
      <a href="{GITHUB_URL}" target="_blank" rel="noopener">{escape(T(lang, "nav_github"))}</a>
      <span class="footer-sep">&middot;</span>
      <span>{escape(T(lang, "footer_license"))}</span>
      <span class="footer-sep">&middot;</span>
      <a href="{b}/llms.txt">llms.txt</a>
    </div>
    <div class="footer-credit">{escape(T(lang, "footer_built_by"))} <a href="https://github.com/borghei" target="_blank" rel="noopener">{AUTHOR}</a></div>
  </div>
</footer>"""


# Sentinel: derive the counterpart URL from `rel` automatically.
AUTO = object()


def page(title, description, rel, body, active="", breadcrumbs=None, jsonld=None,
         extra_js="", lang="en", alt_url=AUTO):
    """Wrap body content in a full HTML page.

    `rel` is the site-relative path of this page ("" / "SKILLS/" / "a/b.html").
    canonical is derived from `rel` in the current language; the counterpart in
    the other language is derived the same way unless `alt_url` overrides it
    (pass alt_url=None for pages that exist in one tree only, e.g. 404).
    """
    canonical = url_for(lang, rel)
    if alt_url is AUTO:
        alt_url = url_for(OTHER_LANG[lang], rel)
    bc_html = ""
    if breadcrumbs:
        parts = []
        for label, url in breadcrumbs:
            if url:
                parts.append(f'<a href="{url}">{escape(label)}</a>')
            else:
                parts.append(f"<span>{escape(label)}</span>")
        bc_html = f'<div class="breadcrumbs container">{"<span class=sep>/</span>".join(parts)}</div>'

    ld_tag = ""
    if jsonld:
        ld_tag = f'<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>'

    js_tag = f"<script>{extra_js}</script>" if extra_js else ""

    # hreflang alternates. Only emitted when both counterparts are known.
    alt_tags = ""
    if alt_url:
        by_lang = {lang: canonical, OTHER_LANG[lang]: alt_url}
        alt_tags = "\n  ".join(
            f'<link rel="alternate" hreflang="{code}" href="{by_lang[code]}">' for code in LANGS
        )
        # x-default always points at the English tree.
        alt_tags += f'\n  <link rel="alternate" hreflang="x-default" href="{by_lang["en"]}">'

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(description[:200])}">
  <link rel="canonical" href="{canonical}">
  {alt_tags}
  <meta property="og:title" content="{escape(title)}">
  <meta property="og:description" content="{escape(description[:200])}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="{OG_LOCALE[lang]}">
  {ld_tag}
  <style>{_css()}</style>
</head>
<body>
{_nav(active, lang, alt_url)}
{bc_html}
<main class="container">
{body}
</main>
{_footer(lang)}
{js_tag}
</body>
</html>
"""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def pretty_name(slug):
    """Convert a-slug-name to A Slug Name."""
    return " ".join(w.capitalize() for w in slug.split("-"))


def domain_label(domain):
    m = DOMAIN_META.get(domain)
    return m["label"] if m else pretty_name(domain)


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


# Every path written during a run, so stale output can be pruned afterwards.
# Without this the generator is write-only: a skill deleted from the catalog
# keeps its page served forever. That is not cosmetic - a merged or retired
# skill would go on publishing superseded legal content under a live URL.
_WRITTEN_PATHS: set[str] = set()


def write_file(path, content):
    ensure_dir(os.path.dirname(path))
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    _WRITTEN_PATHS.add(os.path.realpath(path))
    return path


def prune_stale_pages(roots=("SKILLS", "de/SKILLS")):
    """Delete generated skill/area pages that this run did not write.

    Scoped deliberately to the catalog-driven subtrees. Static content pages,
    assets, css and js are never touched, so a partial run cannot wipe the site.
    """
    removed = []
    for root in roots:
        base = SITE_DIR / root
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*.html")):
            if os.path.realpath(path) not in _WRITTEN_PATHS:
                path.unlink()
                removed.append(str(path.relative_to(SITE_DIR)))
    # Clear out any directory left empty by the pruning (e.g. a retired area).
    for root in roots:
        base = SITE_DIR / root
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*"), reverse=True):
            if path.is_dir() and not any(path.iterdir()):
                path.rmdir()
                removed.append(f"{path.relative_to(SITE_DIR)}/ (leeres Verzeichnis)")
    return removed


def truncate(text, length=160):
    text = text.replace("\n", " ").strip()
    if len(text) <= length:
        return text
    return text[:length - 3].rsplit(" ", 1)[0] + "..."


# ---------------------------------------------------------------------------
# Page generators
# ---------------------------------------------------------------------------

def gen_skill_page(skill, catalog, all_skills_by_domain, lang="en"):
    """Generate an individual skill detail page."""
    name = skill["name"]
    domain = skill["domain"]
    desc = skill.get("description", "")
    tags = skill.get("tags", [])
    tools_count = skill.get("tools", 0)
    skill_path = skill.get("path", "")
    subdomain = skill.get("subdomain", "") or ""
    version = skill.get("version", "") or ""
    has_refs = skill.get("has_references", False)

    md_text = load_skill_md(skill_path)
    intro_md, sections = parse_skill_md(md_text)

    dl = domain_label(domain)
    pn = pretty_name(name)
    b = lang_base(lang)
    title = f"{pn} - {BRAND}"
    rel = f"SKILLS/{domain}/{name}.html"
    canonical = url_for(lang, rel)
    breadcrumbs = [
        (T(lang, "bc_home"), f"{b}/"),
        (T(lang, "bc_skills"), f"{b}/SKILLS/"),
        (dl, f"{b}/SKILLS/{domain}/"),
        (pn, None),
    ]

    jsonld = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": pn,
        "description": desc,
        "applicationCategory": dl,
        "operatingSystem": "Any",
        "url": canonical,
        "author": {"@type": "Person", "name": AUTHOR},
        "inLanguage": "de",
    }

    # Badge bar
    badges = f'<span class="badge badge-domain">{escape(dl)}</span>'
    if subdomain:
        badges += f' <span class="badge badge-subdomain">{escape(pretty_name(subdomain))}</span>'
    if version:
        badges += f' <span class="badge badge-version">v{escape(version)}</span>'
    if tools_count:
        badges += f' <span class="badge badge-tools">{SVG_ICONS["tools"]} {escape(n_tools(lang, tools_count))}</span>'
    if has_refs:
        badges += f' <span class="badge badge-refs">{escape(T(lang, "badge_references"))}</span>'
    badge_bar = f'<div class="badge-bar">{badges}</div>'

    # Tag pills
    tags_html = "".join(f'<span class="tag">{escape(t)}</span>' for t in tags)
    if tags_html:
        tags_html = f'<div class="skill-meta" style="margin-bottom:24px">{tags_html}</div>'

    # Intro paragraph (description shown; intro_md skipped if just blank)
    sections_html = []

    # Render each parsed section. Body always stays German; the H2 label is
    # translated to English in the EN tree and kept German in the DE tree.
    for german_heading, body_md in sections:
        heading = translate_heading(german_heading, lang)
        body_html = md_to_html(body_md) if body_md else ""
        sections_html.append(
            f'<section><h2>{escape(heading)}</h2>{body_html}</section>'
        )

    # If no sections parsed (fallback), render the entire markdown body
    if not sections:
        body_html = md_to_html(md_text)
        sections_html.append(f'<section>{body_html}</section>')

    sections_block = "\n".join(sections_html)

    # Related skills (same domain, max 6)
    related = [s for s in all_skills_by_domain.get(domain, []) if s["name"] != name][:6]
    related_html = ""
    if related:
        cards = "".join(
            f'<a href="{b}/SKILLS/{s["domain"]}/{s["name"]}.html" class="skill-card" style="text-decoration:none">'
            f'<h3>{escape(pretty_name(s["name"]))}</h3>'
            f'<p>{escape(truncate(s.get("description", ""), 110))}</p></a>'
            for s in related
        )
        related_html = (
            f'<h2>{escape(T(lang, "related_skills_in", area=dl))}</h2>'
            f'<div class="related-grid">{cards}</div>'
        )

    # Source link
    ext = SVG_ICONS["external"]
    source_html = (
        f'<p style="margin-top:32px"><a href="{GITHUB_URL}/tree/main/{skill_path}" '
        f'target="_blank" rel="noopener" class="btn btn-secondary">'
        f'{escape(T(lang, "view_skill_md"))} {ext}</a></p>'
    )

    body = f"""
<article class="skill-detail">
  <div class="page-header">
    <h1 class="page-title">{escape(pn)}</h1>
    <p class="page-subtitle">{escape(desc)}</p>
    {badge_bar}
    {tags_html}
  </div>
  {sections_block}
  {related_html}
  {source_html}
</article>"""

    return page(title, desc, rel, body, active="skills", breadcrumbs=breadcrumbs,
                jsonld=jsonld, lang=lang)


def gen_domain_page(domain, skills, catalog, lang="en"):
    """Generate a domain (area) index page."""
    dl = domain_label(domain)
    dm = DOMAIN_META.get(domain, {})
    desc_short = dm.get("desc") or T(lang, "area_desc_fallback", area=dl)
    count = len(skills)

    b = lang_base(lang)
    title = f"{dl} - {BRAND}"
    description = T(lang, "area_description", n=count, area=dl, desc=desc_short)
    rel = f"SKILLS/{domain}/"
    breadcrumbs = [
        (T(lang, "bc_home"), f"{b}/"),
        (T(lang, "bc_skills"), f"{b}/SKILLS/"),
        (dl, None),
    ]

    search_icon = SVG_ICONS["search"]
    ph = escape(T(lang, "search_placeholder_area", area=dl))
    filter_html = f"""<div class="filter-bar">
  <div class="search-wrap">
    {search_icon}
    <input type="text" class="search-input" placeholder="{ph}" id="domain-search" onkeyup="filterCards()">
  </div>
</div>"""

    cards = []
    for s in sorted(skills, key=lambda x: x["name"]):
        tags = "".join(f'<span class="tag">{escape(t)}</span>' for t in s.get("tags", [])[:4])
        subdomain = s.get("subdomain", "")
        badges = f'<span class="badge badge-domain">{escape(dl)}</span>'
        if subdomain:
            badges += f' <span class="badge badge-subdomain">{escape(pretty_name(subdomain))}</span>'
        if s.get("has_references"):
            badges += f' <span class="badge badge-refs">{escape(T(lang, "badge_references"))}</span>'
        cards.append(
            f'<a href="{b}/SKILLS/{s["domain"]}/{s["name"]}.html" class="skill-card" '
            f'data-name="{escape(s["name"])}" data-tags="{escape(" ".join(s.get("tags", [])))}" style="text-decoration:none">'
            f'<h3>{escape(pretty_name(s["name"]))}</h3>'
            f'<p>{escape(truncate(s.get("description", ""), 130))}</p>'
            f'<div class="badge-bar">{badges}</div>'
            f'<div class="skill-meta">{tags}</div></a>'
        )

    search_js = """
function filterCards(){
  var q=document.getElementById('domain-search').value.toLowerCase();
  document.querySelectorAll('.skill-card').forEach(function(c){
    var n=c.getAttribute('data-name')||'';
    var t=c.getAttribute('data-tags')||'';
    var txt=c.textContent.toLowerCase();
    c.style.display=(n.includes(q)||t.includes(q)||txt.includes(q))?'':'none';
  });
}
"""

    body = f"""
<div class="page-header">
  <h1 class="page-title">{escape(dl)} <span class="count-badge">{escape(n_skills(lang, count))}</span></h1>
  <p class="page-subtitle">{escape(desc_short)}</p>
</div>
{filter_html}
<div class="skills-grid">
{"".join(cards)}
</div>"""

    return page(title, description, rel, body, active="skills", breadcrumbs=breadcrumbs,
                extra_js=search_js, lang=lang)


def gen_skills_index(catalog, all_skills_by_domain, lang="en"):
    """Generate the all-skills catalog page."""
    total = len(catalog["skills"])
    domain_count = len(catalog.get("domains", {}))
    b = lang_base(lang)
    title = T(lang, "skills_index_title", brand=BRAND)
    description = T(lang, "skills_index_description", total=total, areas=domain_count)
    rel = "SKILLS/"
    breadcrumbs = [(T(lang, "bc_home"), f"{b}/"), (T(lang, "bc_skills"), None)]

    domain_options = "".join(
        f'<option value="{d}">{escape(domain_label(d))}</option>'
        for d in sorted(all_skills_by_domain.keys())
    )

    search_icon = SVG_ICONS["search"]
    ph = escape(T(lang, "search_placeholder_all", n=total))
    filter_html = f"""<div class="filter-bar">
  <div class="search-wrap">
    {search_icon}
    <input type="text" class="search-input" placeholder="{ph}" id="skill-search" onkeyup="filterSkills()">
  </div>
  <select class="filter-select" id="domain-filter" onchange="filterSkills()">
    <option value="">{escape(T(lang, "filter_all_areas"))}</option>
    {domain_options}
  </select>
</div>"""

    # Domain summary cards
    domain_summary = []
    for d in sorted(all_skills_by_domain.keys()):
        dm = DOMAIN_META.get(d, {})
        dl_name = domain_label(d)
        cnt = len(all_skills_by_domain[d])
        examples = [s["name"] for s in all_skills_by_domain[d][:4]]
        pills = "".join(f'<span class="example-pill">{escape(pretty_name(e))}</span>' for e in examples)
        if cnt > len(examples):
            pills += f'<span class="example-pill">{escape(T(lang, "more_n", n=cnt - len(examples)))}</span>'
        domain_summary.append(
            f'<a href="{b}/SKILLS/{d}/" class="skill-card" style="text-decoration:none">'
            f'<h3>{escape(dl_name)}</h3>'
            f'<div class="badge-bar"><span class="badge badge-domain">{escape(n_skills(lang, cnt))}</span></div>'
            f'<p>{escape(dm.get("desc", ""))}</p>'
            f'<div class="example-pills">{pills}</div></a>'
        )

    # All skill cards
    cards = []
    for s in sorted(catalog["skills"], key=lambda x: x["name"]):
        tags = "".join(f'<span class="tag">{escape(t)}</span>' for t in s.get("tags", [])[:3])
        subdomain = s.get("subdomain", "")
        badges = f'<span class="badge badge-domain">{escape(domain_label(s["domain"]))}</span>'
        if subdomain:
            badges += f' <span class="badge badge-subdomain">{escape(pretty_name(subdomain))}</span>'
        if s.get("has_references"):
            badges += f' <span class="badge badge-refs">{escape(T(lang, "badge_references"))}</span>'
        cards.append(
            f'<a href="{b}/SKILLS/{s["domain"]}/{s["name"]}.html" class="skill-card" '
            f'data-name="{escape(s["name"])}" data-domain="{escape(s["domain"])}" '
            f'data-tags="{escape(" ".join(s.get("tags", [])))}" style="text-decoration:none">'
            f'<h3>{escape(pretty_name(s["name"]))}</h3>'
            f'<p>{escape(truncate(s.get("description", ""), 130))}</p>'
            f'<div class="badge-bar">{badges}</div>'
            f'<div class="skill-meta">{tags}</div></a>'
        )

    search_js = """
function filterSkills(){
  var q=(document.getElementById('skill-search').value||'').toLowerCase();
  var d=document.getElementById('domain-filter').value;
  document.querySelectorAll('#all-skills .skill-card').forEach(function(c){
    var name=c.getAttribute('data-name')||'';
    var dom=c.getAttribute('data-domain')||'';
    var tags=c.getAttribute('data-tags')||'';
    var txt=c.textContent.toLowerCase();
    var matchQ=!q||name.includes(q)||tags.includes(q)||txt.includes(q);
    var matchD=!d||dom===d;
    c.style.display=(matchQ&&matchD)?'':'none';
  });
}
"""

    body = f"""
<div class="page-header">
  <h1 class="page-title">{escape(T(lang, "skills_catalog_h1"))} <span class="count-badge">{escape(n_skills(lang, total))}</span></h1>
  <p class="page-subtitle">{escape(description)}</p>
</div>

<h2 class="section-heading">{escape(T(lang, "browse_by_area"))}</h2>
<div class="skills-grid" style="margin-bottom:48px">
{"".join(domain_summary)}
</div>

<h2 class="section-heading">{escape(T(lang, "all_skills_h"))}</h2>
{filter_html}
<div class="skills-grid" id="all-skills">
{"".join(cards)}
</div>"""

    return page(title, description, rel, body, active="skills", breadcrumbs=breadcrumbs,
                extra_js=search_js, lang=lang)


# ---------------------------------------------------------------------------
# Landing page
# ---------------------------------------------------------------------------

def gen_landing(catalog, all_skills_by_domain, lang="en"):
    """Generate the landing page (site/index.html, site/de/index.html)."""
    total = catalog.get("total_skills", len(catalog["skills"]))
    domain_count = len(catalog.get("domains", {}))
    b = lang_base(lang)

    title = T(lang, "landing_title", brand=BRAND)
    description = T(lang, "landing_description", areas=domain_count, total=total)

    # Top 12 domains by skill count for the landing grid
    sorted_domains = sorted(all_skills_by_domain.items(), key=lambda x: -len(x[1]))
    featured_cards = []
    for d, sk_list in sorted_domains[:12]:
        dl = domain_label(d)
        dm = DOMAIN_META.get(d, {})
        cnt = len(sk_list)
        featured_cards.append(
            f'<a href="{b}/SKILLS/{d}/" class="skill-card" style="text-decoration:none">'
            f'<h3>{escape(dl)}</h3>'
            f'<div class="badge-bar"><span class="badge badge-domain">{escape(n_skills(lang, cnt))}</span></div>'
            f'<p>{escape(dm.get("desc", ""))}</p></a>'
        )

    body = f"""
<section class="hero">
  <h1 class="hero-title">{escape(T(lang, "hero_title"))}</h1>
  <p class="hero-subtitle">{escape(T(lang, "hero_subtitle"))}</p>
  <div class="stat-row">
    <span class="stat"><strong>{domain_count}</strong> {escape(T(lang, "stat_areas"))}</span>
    <span class="stat"><strong>{total}</strong> {escape(T(lang, "stat_skills"))}</span>
    <span class="stat"><strong>3</strong> {escape(T(lang, "stat_providers"))}</span>
    <span class="stat"><strong>8</strong> {escape(T(lang, "stat_frameworks"))}</span>
  </div>
  <div class="hero-actions">
    <a href="{b}/SKILLS/" class="btn btn-primary">{escape(T(lang, "btn_browse_skills"))}</a>
    <a href="{b}/getting-started/" class="btn btn-secondary">{escape(T(lang, "btn_getting_started"))}</a>
  </div>
</section>

<div class="disclaimer">
  <p>{T(lang, "disclaimer")}</p>
  <p style="margin-top:10px">{escape(T(lang, "german_content_note"))}</p>
</div>

<h2 class="section-heading">{escape(T(lang, "featured_areas"))}</h2>
<p style="color:var(--text-muted); max-width:720px; margin-bottom:20px;">{escape(T(lang, "featured_areas_note", areas=domain_count))}</p>
<div class="skills-grid">
{"".join(featured_cards)}
</div>

<p style="text-align:center; margin: 16px 0 60px;"><a href="{b}/SKILLS/" class="btn btn-secondary">{escape(T(lang, "view_all_areas", areas=domain_count))} {SVG_ICONS["arrow-right"]}</a></p>
"""

    return page(title, description, "", body, active="", lang=lang)


# ---------------------------------------------------------------------------
# Static content pages (getting-started / guides / reference / 404)
#
# The markdown bodies live in STRINGS so both trees go through the same
# lookup path as the chrome. Bodies that need live counts from skills.json
# carry {total} / {areas} placeholders; all other braces in these bodies are
# literal, so T() only formats when keyword arguments are supplied.
# ---------------------------------------------------------------------------

STRINGS["en"].update({
    "gs_body": """
This guide walks you through installing AI Skills German Law and running your first skill.

The skills work with three providers: **Claude** (Claude Code, claude.ai), **Gemini** (Gems, Gemini CLI), and **OpenAI** (Custom GPTs, ChatGPT). Skill outputs are in German; this site is available in English and German.

## Choose your path

- **[Installation](installation/)** — Add the marketplace to Claude Code, copy skills into your project, or use them directly from GitHub.
- **[Quick Start](quick-start/)** — Run your first skill in under 60 seconds.
- **[Platforms](platforms/)** — Provider-specific setup for Claude Code, Gemini CLI, ChatGPT Custom GPTs, Cursor, and other AI assistants.

## What you get

- {total} skills across {areas} areas of German law and EU compliance.
- Statute citations linked to `gesetze-im-internet.de` and `EUR-Lex`.
- Case-law citations labelled `[unverifiziert – prüfen]` until externally checked. `[generiert]` (hallucinated) citations are forbidden.
- Provider-neutral skill format — a single `SKILL.md` runs in Claude, Gemini, and GPT with adapters.
- Verification log (`VERIFICATION_STATUS.md`) tracking which case-law citations have been confirmed.

## Important — read first

This is not legal advice. Every skill output is a draft for review by a licensed Rechtsanwalt or Syndikusrechtsanwalt under § 43a BRAO and § 2 BORA. Always verify case-law citations in Beck-Online, juris, or openjur.net before client-facing or court-facing use.
""",
    "install_body": f"""
There are three ways to use AI Skills German Law: add it as a Claude Code plugin marketplace, clone the repo, or copy individual skills.

## Option 1 — Claude Code (recommended)

```bash
# Add the marketplace
/plugin marketplace add borghei/AI-Skills-German-Law

# Install an area
/plugin install arbeitsrecht
/plugin install datenschutzrecht
/plugin install kartellrecht

# Use a skill
/arbeitsrecht:kuendigungs-pruefung
```

## Option 2 — Clone the repository

```bash
git clone {GITHUB_URL}.git
cd AI-Skills-German-Law

# Browse a skill
cat arbeitsrecht/skills/abmahnung/SKILL.md
```

## Option 3 — Copy a single skill

Pick the area folder you need and copy it into your project.

```bash
# Example: drop the datenschutzrecht skills into your project
git clone {GITHUB_URL}.git
cp -r AI-Skills-German-Law/datenschutzrecht your-project/
```

## Verify

After install, check `VERIFICATION_STATUS.md` to see which plugins have completed an external case-law verification pass.

```bash
cat VERIFICATION_STATUS.md
```
""",
    "platforms_body": """
Every skill is provider-neutral. The same `SKILL.md` runs on Claude, Gemini, and GPT — the only difference is how you load it.

## Claude Code

The fastest setup. Install once, run with a slash command.

```bash
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install arbeitsrecht
/arbeitsrecht:abmahnung
```

## Claude.ai (Projects)

Create a Project, paste the `SKILL.md` body into Project Knowledge, then prompt as normal.

1. Open `claude.ai` → Projects → New project.
2. Name it after the skill (e.g. `Abmahnung`).
3. In Project Knowledge, add the `SKILL.md` content as text.
4. Set Custom Instructions to: *"You are an expert in the {Domain} domain. Use the project knowledge as your expertise. Output in German."*

## Gemini (Gems)

Create a Gem in `gemini.google.com`, paste the `SKILL.md` body into the system prompt.

## Gemini CLI

```bash
# Reference the SKILL.md in your Gemini settings:
.gemini/skills/abmahnung/SKILL.md
```

## ChatGPT (Custom GPTs)

1. `chatgpt.com` → Explore GPTs → Create.
2. Name the GPT after the skill.
3. Paste the `SKILL.md` body into the Instructions field.
4. Test with the sample prompt at the bottom of the `SKILL.md`.

## Cursor / Cline / Aider

Reference the `SKILL.md` from your `.cursorrules` (or equivalent) or paste its content into the system prompt.

## Notes

- Skill outputs are in German regardless of provider — that is intentional.
- Each `SKILL.md` carries provider variants in the frontmatter under `provider_variants:`.
""",
    "qs_body": """
Run your first skill in under 60 seconds.

## 1. Pick a skill

Browse the [skill catalog](../../SKILLS/) and pick one. For this walk-through we use `arbeitsrecht:abmahnung`.

## 2. Install the marketplace

```bash
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install arbeitsrecht
```

## 3. Run the skill

```
/arbeitsrecht:abmahnung
```

The skill will ask for:

- konkretes Verhalten (Datum, Ort, Zeugen)
- Art der Pflichtverletzung
- frühere Abmahnungen
- Position des AN

## 4. Review the output

Every skill output is a draft. Review the German text, verify any case-law citations marked `[unverifiziert – prüfen]` in Beck-Online or juris, then adapt to your Mandat.

## 5. Iterate

If the draft is not quite right, give the skill more context in a follow-up turn. Skills are conversational — they keep memory of the file state and earlier decisions.

## Next steps

- See [Platforms](../platforms/) for setup outside Claude Code.
- See [Authoring](../../guides/authoring/) to write your own skill.
- See [Reference](../../reference/) for the conventions every skill follows.
""",
    "authoring_body": """
This guide explains how to write a new skill that fits the repository conventions.

## Skill anatomy

Each skill lives in `<area>/skills/<skill-name>/SKILL.md` and follows this structure:

```
---
name: skill-name
description: "Eine prägnante Beschreibung..."
language: de
agents:
  researcher: ../../agents/researcher.md
  drafter: ../../agents/drafter.md
  reviewer: ../../agents/reviewer.md
provider_variants:
  - claude
  - gemini
  - openai
test: ./test.md
---

# /area:skill-name

## Zweck
...

## Eingaben
...

## Sub-Agent-Architektur
...

## Ablauf
...

## Quellen und Zitierweise
...

## Ausgabeformat
...

## Risiken / typische Fehler
...
```

## Required sections

1. **Zweck** — what the skill does and when to use it.
2. **Eingaben** — what data the user must provide.
3. **Sub-Agent-Architektur** — how researcher / drafter / reviewer collaborate.
4. **Ablauf** — the step-by-step process.
5. **Quellen und Zitierweise** — statutes, commentary, case-law (citations linked).
6. **Ausgabeformat** — the deliverable shape (letter, memo, table, etc.).
7. **Risiken / typische Fehler** — known pitfalls.

## Citation discipline

- Statutes: link to `gesetze-im-internet.de`.
- EU law: link to `EUR-Lex`.
- Case-law citations are one of three states:
  - **(no marker, with URL)** — verified against an official source.
  - **`[unverifiziert – prüfen]`** — model knowledge, not externally checked. The user must verify.
  - **`[generiert]`** — forbidden in client-facing output.

See [`references/zitierweise.md`](../../reference/) for the binding citation conventions.

## Methodology

- Default to **Gutachtenstil** for memos and reasoned client letters.
- **Urteilsstil** for briefs (Schriftsätze) and short internal notes.
- **Anspruchsgrundlagenprüfung** in canonical order: Vertrag → c.i.c. → GoA → dinglich → Delikt → Bereicherung.

## Test file

Every skill ships with a `test.md` that captures at least one full input/output trace. The test file is referenced from the frontmatter (`test: ./test.md`).

## Submit

Open a PR against `main`. The CI pipeline will run the smoke tests and check the frontmatter schema.
""",
    "bundles_body": """
Bundles group skills that are routinely used together. They are not a separate concept in the file tree — each plugin (area) is itself a bundle.

## Per-area bundles

Each area folder (e.g. `arbeitsrecht/`, `kartellrecht/`, `datenschutzrecht/`) is a self-contained bundle of skills, shared agents, and tests. Installing the area installs every skill in it.

## Cross-area bundles

Some scenarios cross areas. Common combinations:

- **M&A diligence**: `gesellschaftsrecht`, `kartellrecht`, `aussenwirtschaft-zoll-sanktionen`, `arbeitsrecht` (Sozialauswahl).
- **AI product launch**: `ki-vo-compliance`, `datenschutzrecht`, `dsa-dma`, `produktrecht`.
- **Compliance baseline**: `geldwaesche-aml-kyc`, `hinweisgeberschutz`, `lieferkettengesetz`, `csrd`.
- **Tech contract review**: `it-recht`, `datenschutzrecht`, `urheber-medienrecht`, `vertragsrecht`.
- **Workplace incident**: `arbeitsrecht`, `datenschutzrecht`, `strafrecht`.

## Compose bundles in Claude Code

Install multiple plugins at once:

```bash
/plugin install gesellschaftsrecht
/plugin install kartellrecht
/plugin install aussenwirtschaft-zoll-sanktionen
/plugin install arbeitsrecht
```

The skills then orchestrate together through the shared researcher/drafter/reviewer agents.
""",
    "custom_body": """
Every skill in this repo is a starting point. Customise it for your Kanzlei, your in-house style, or your Mandat.

## What to customise

- **Style**: replace the default `Sie`-form with `Du`-form if your culture allows it.
- **Templates**: every `Ausgabeformat` block (output template) can be swapped for your firm's letterhead and structure.
- **Citation density**: increase or decrease the number of Kommentar references depending on whether the output is for a partner, client, or court.
- **Risikoschwellen**: tighten or loosen the risk-flagging language in `Risiken / typische Fehler`.

## How to customise without losing updates

Fork the repo. Keep a `local/` overlay folder that mirrors the upstream area path but contains only your overrides. Your `SKILL.md` at `local/arbeitsrecht/skills/abmahnung/SKILL.md` shadows the upstream one when you load via `local/`-first.

## Add your own statutes / Kommentare

Append to `references/kommentare.md` and `references/zitierweise.md` in your fork. Cite normally from your SKILL.md.

## Provider variants

The frontmatter `provider_variants:` controls which providers a skill is exposed to. If you only use Gemini, drop `claude` and `openai`. This does not change the SKILL body; it only changes which adapter layers generate provider-specific manifests.
""",
    "orch_body": """
Skills in this repository follow a three-role sub-agent architecture: **researcher**, **drafter**, **reviewer**.

## The three agents

- **Researcher** (`agents/researcher.md`) — finds statutes, Kommentar passages, and case-law. Output is a citation pack with links.
- **Drafter** (`agents/drafter.md`) — writes the client deliverable (letter, memo, motion, output template).
- **Reviewer** (`agents/reviewer.md`) — checks for Bestimmtheit, Verhältnismäßigkeit, missing citations, and risk flags.

## How orchestration works

Each `SKILL.md` declares the three agents in its frontmatter:

```yaml
agents:
  researcher: ../../agents/researcher.md
  drafter: ../../agents/drafter.md
  reviewer: ../../agents/reviewer.md
```

The skill body then describes which agent does what under `## Sub-Agent-Architektur`. At runtime:

1. The skill is loaded.
2. The provider runs `researcher` first against the user input.
3. The `drafter` consumes the research pack and produces the deliverable.
4. The `reviewer` evaluates the deliverable, surfaces flags, and the final output is the deliverable + reviewer notes.

## Why this matters

- **Citations are produced before the deliverable**, so the drafter cannot hallucinate Fundstellen.
- **The reviewer is the last word** — it sees both the input and the deliverable and can refuse to ship.
- **Errors are localized** — if a citation is wrong, you fix it in the researcher; if tone is wrong, you fix the drafter.

## Customising the agents

Edit `agents/researcher.md`, `agents/drafter.md`, `agents/reviewer.md` in your fork. The change applies to every skill that imports them.
""",
    "ref_body": f"""
The reference section points to the binding documentation that every skill in this repository follows.

## Source documents

- **[README.md]({GITHUB_URL}/blob/main/README.md)** — project overview, install, and architecture.
- **[CONVENTIONS.md]({GITHUB_URL}/blob/main/CONVENTIONS.md)** — provider-neutral conventions every skill must follow (language, methodology, citation discipline).
- **[VERIFICATION_STATUS.md]({GITHUB_URL}/blob/main/VERIFICATION_STATUS.md)** — current snapshot of which plugins have completed an external case-law verification pass.
- **[CHANGELOG.md]({GITHUB_URL}/blob/main/CHANGELOG.md)** — notable changes per release.
- **[QUICKSTART.md]({GITHUB_URL}/blob/main/QUICKSTART.md)** — 60-second walkthrough.
- **[CONTRIBUTING.md]({GITHUB_URL}/blob/main/CONTRIBUTING.md)** — how to add or fix a skill.

## Tooling and automation

Deterministic helpers that run without a model, plus the eval and verification harness:

- **[references/rechner.md]({GITHUB_URL}/blob/main/references/rechner.md)** — deterministic legal calculators: Fristen (§§ 187-193 BGB), Verjährung (§§ 195-199 BGB), RVG and GKG fees, and Feiertage for all 16 Bundesländer.
- **[scripts/verify_citations.py]({GITHUB_URL}/blob/main/scripts/verify_citations.py)** — resolves `§`-anchors, ECLI and CELEX citations against gesetze-im-internet.de; offline-informational, `--strict` to gate.
- **[evals/]({GITHUB_URL}/blob/main/evals/README.md)** — behavioural, LLM-graded eval harness (promptfoo) generated from the per-skill `test.md` files.
- **[references/mcp-template.json]({GITHUB_URL}/blob/main/references/mcp-template.json)** — live legal-data wiring via the NeuRIS (rechtsinformationen.bund.de) MCP server.

## Repository conventions (summary)

- **Outputs in German.** English terms only when established (e.g. "Letter of Intent") and explained on first use.
- **Default to Gutachtenstil** for memos and reasoned letters; **Urteilsstil** for briefs and short internal notes.
- **Anspruchsgrundlagenprüfung** in canonical order: Vertrag → c.i.c. → GoA → dinglich → Delikt → Bereicherung.
- **Statutory interpretation** applies all four classical methods plus constitution-conforming and EU-law-conforming interpretation.

## Citation states

Every case-law citation gets one of three markers:

| State | Meaning |
|---|---|
| (no marker, with URL) | Verified against an official source |
| `[unverifiziert – prüfen]` | Model knowledge, not externally confirmed — verify before reliance |
| `[generiert]` | Forbidden in client-facing output |

## Disclaimer

This is not legal advice. Skill output is a draft for review by a licensed Rechtsanwalt or Syndikusrechtsanwalt under § 43a BRAO and § 2 BORA.
""",
})

STRINGS["de"].update({
    "gs_body": """
Diese Anleitung führt Sie durch die Installation von AI Skills German Law und die Ausführung Ihres ersten Skills.

Die Skills laufen bei drei Anbietern: **Claude** (Claude Code, claude.ai), **Gemini** (Gems, Gemini CLI) und **OpenAI** (Custom GPTs, ChatGPT). Die Skill-Ausgaben sind deutsch; diese Website steht auf Deutsch und Englisch zur Verfügung.

## Wählen Sie Ihren Einstieg

- **[Installation](installation/)** — Marketplace in Claude Code einbinden, Skills in Ihr Projekt kopieren oder direkt von GitHub nutzen.
- **[Schnelleinstieg](quick-start/)** — Den ersten Skill in unter 60 Sekunden ausführen.
- **[Plattformen](platforms/)** — Einrichtung je Anbieter: Claude Code, Gemini CLI, ChatGPT Custom GPTs, Cursor und weitere KI-Assistenten.

## Was Sie erhalten

- {total} Skills in {areas} Rechtsgebieten des deutschen Rechts und der EU-Compliance.
- Normzitate verlinkt auf `gesetze-im-internet.de` und `EUR-Lex`.
- Rechtsprechungsnachweise sind mit `[unverifiziert – prüfen]` gekennzeichnet, solange sie nicht extern geprüft wurden. `[generiert]` (halluzinierte) Fundstellen sind unzulässig.
- Anbieterneutrales Skill-Format — eine einzige `SKILL.md` läuft über Adapter in Claude, Gemini und GPT.
- Prüfprotokoll (`VERIFICATION_STATUS.md`) mit dem Stand der bestätigten Rechtsprechungsnachweise.

## Wichtig — bitte zuerst lesen

Dies ist keine Rechtsberatung. Jede Skill-Ausgabe ist ein Entwurf zur Prüfung durch eine zugelassene Rechtsanwältin oder einen zugelassenen Rechtsanwalt bzw. Syndikusrechtsanwalt nach § 43a BRAO und § 2 BORA. Prüfen Sie Rechtsprechungsnachweise stets in Beck-Online, juris oder openjur.net, bevor Sie sie gegenüber Mandantschaft oder Gericht verwenden.
""",
    "install_body": f"""
Es gibt drei Wege, AI Skills German Law zu nutzen: als Plugin-Marketplace in Claude Code einbinden, das Repository klonen oder einzelne Skills kopieren.

## Variante 1 — Claude Code (empfohlen)

```bash
# Marketplace hinzufügen
/plugin marketplace add borghei/AI-Skills-German-Law

# Ein Rechtsgebiet installieren
/plugin install arbeitsrecht
/plugin install datenschutzrecht
/plugin install kartellrecht

# Einen Skill ausführen
/arbeitsrecht:kuendigungs-pruefung
```

## Variante 2 — Repository klonen

```bash
git clone {GITHUB_URL}.git
cd AI-Skills-German-Law

# Einen Skill ansehen
cat arbeitsrecht/skills/abmahnung/SKILL.md
```

## Variante 3 — Einzelnen Skill kopieren

Wählen Sie den Ordner des gewünschten Rechtsgebiets und kopieren Sie ihn in Ihr Projekt.

```bash
# Beispiel: die Skills zum Datenschutzrecht in Ihr Projekt übernehmen
git clone {GITHUB_URL}.git
cp -r AI-Skills-German-Law/datenschutzrecht your-project/
```

## Prüfen

Sehen Sie nach der Installation in `VERIFICATION_STATUS.md` nach, für welche Plugins eine externe Prüfung der Rechtsprechungsnachweise abgeschlossen ist.

```bash
cat VERIFICATION_STATUS.md
```
""",
    "platforms_body": """
Jeder Skill ist anbieterneutral. Dieselbe `SKILL.md` läuft in Claude, Gemini und GPT — unterschiedlich ist nur, wie Sie sie laden.

## Claude Code

Die schnellste Einrichtung. Einmal installieren, per Slash-Befehl ausführen.

```bash
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install arbeitsrecht
/arbeitsrecht:abmahnung
```

## Claude.ai (Projects)

Legen Sie ein Projekt an, fügen Sie den Inhalt der `SKILL.md` in die Projektwissensbasis ein und arbeiten Sie dann wie gewohnt.

1. `claude.ai` öffnen → Projects → Neues Projekt.
2. Benennen Sie es nach dem Skill (z. B. `Abmahnung`).
3. Fügen Sie den Inhalt der `SKILL.md` als Text in die Projektwissensbasis ein.
4. Setzen Sie als Custom Instructions: *"Du bist Expertin bzw. Experte für das Rechtsgebiet {Domain}. Nutze das Projektwissen als Fachgrundlage. Antworte auf Deutsch."*

## Gemini (Gems)

Legen Sie unter `gemini.google.com` ein Gem an und fügen Sie den Inhalt der `SKILL.md` in den System-Prompt ein.

## Gemini CLI

```bash
# Die SKILL.md in den Gemini-Einstellungen referenzieren:
.gemini/skills/abmahnung/SKILL.md
```

## ChatGPT (Custom GPTs)

1. `chatgpt.com` → Explore GPTs → Create.
2. Benennen Sie den GPT nach dem Skill.
3. Fügen Sie den Inhalt der `SKILL.md` in das Feld "Instructions" ein.
4. Testen Sie mit dem Beispiel-Prompt am Ende der `SKILL.md`.

## Cursor / Cline / Aider

Referenzieren Sie die `SKILL.md` aus Ihrer `.cursorrules` (oder dem entsprechenden Pendant) oder fügen Sie den Inhalt in den System-Prompt ein.

## Hinweise

- Die Skill-Ausgaben sind unabhängig vom Anbieter deutsch — das ist beabsichtigt.
- Jede `SKILL.md` führt die Anbietervarianten im Frontmatter unter `provider_variants:`.
""",
    "qs_body": """
Führen Sie Ihren ersten Skill in unter 60 Sekunden aus.

## 1. Skill auswählen

Durchsuchen Sie den [Skill-Katalog](../../SKILLS/) und wählen Sie einen Skill. Für diese Anleitung verwenden wir `arbeitsrecht:abmahnung`.

## 2. Marketplace installieren

```bash
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install arbeitsrecht
```

## 3. Skill ausführen

```
/arbeitsrecht:abmahnung
```

Der Skill fragt ab:

- konkretes Verhalten (Datum, Ort, Zeugen)
- Art der Pflichtverletzung
- frühere Abmahnungen
- Position des AN

## 4. Ausgabe prüfen

Jede Skill-Ausgabe ist ein Entwurf. Prüfen Sie den deutschen Text, verifizieren Sie alle mit `[unverifiziert – prüfen]` gekennzeichneten Fundstellen in Beck-Online oder juris und passen Sie das Ergebnis an Ihr Mandat an.

## 5. Nachschärfen

Wenn der Entwurf noch nicht passt, geben Sie dem Skill im nächsten Schritt mehr Kontext. Skills arbeiten dialogisch — sie behalten den Stand der Datei und frühere Entscheidungen im Blick.

## Nächste Schritte

- Siehe [Plattformen](../platforms/) für die Einrichtung außerhalb von Claude Code.
- Siehe [Skills schreiben](../../guides/authoring/), um einen eigenen Skill zu erstellen.
- Siehe [Referenz](../../reference/) für die Konventionen, denen jeder Skill folgt.
""",
    "authoring_body": """
Diese Anleitung erklärt, wie Sie einen neuen Skill schreiben, der den Konventionen des Repositorys entspricht.

## Aufbau eines Skills

Jeder Skill liegt unter `<rechtsgebiet>/skills/<skill-name>/SKILL.md` und folgt diesem Aufbau:

```
---
name: skill-name
description: "Eine prägnante Beschreibung..."
language: de
agents:
  researcher: ../../agents/researcher.md
  drafter: ../../agents/drafter.md
  reviewer: ../../agents/reviewer.md
provider_variants:
  - claude
  - gemini
  - openai
test: ./test.md
---

# /rechtsgebiet:skill-name

## Zweck
...

## Eingaben
...

## Sub-Agent-Architektur
...

## Ablauf
...

## Quellen und Zitierweise
...

## Ausgabeformat
...

## Risiken / typische Fehler
...
```

## Pflichtabschnitte

1. **Zweck** — was der Skill leistet und wann er einzusetzen ist.
2. **Eingaben** — welche Angaben die Nutzerin bzw. der Nutzer liefern muss.
3. **Sub-Agent-Architektur** — wie Researcher, Drafter und Reviewer zusammenwirken.
4. **Ablauf** — das schrittweise Vorgehen.
5. **Quellen und Zitierweise** — Normen, Kommentarliteratur, Rechtsprechung (Fundstellen verlinkt).
6. **Ausgabeformat** — die Form des Arbeitsergebnisses (Schreiben, Vermerk, Tabelle usw.).
7. **Risiken / typische Fehler** — bekannte Fallstricke.

## Zitierdisziplin

- Normen: Verlinkung auf `gesetze-im-internet.de`.
- Unionsrecht: Verlinkung auf `EUR-Lex`.
- Rechtsprechungsnachweise haben genau einen von drei Zuständen:
  - **(ohne Kennzeichnung, mit URL)** — gegen eine amtliche Quelle geprüft.
  - **`[unverifiziert – prüfen]`** — Modellwissen, nicht extern geprüft. Die Prüfung obliegt Ihnen.
  - **`[generiert]`** — in mandatsbezogenen Ausgaben unzulässig.

Die verbindlichen Zitierkonventionen finden Sie in [`references/zitierweise.md`](../../reference/).

## Methodik

- Für Vermerke und begründete Mandantenschreiben grundsätzlich **Gutachtenstil**.
- **Urteilsstil** für Schriftsätze und kurze interne Notizen.
- **Anspruchsgrundlagenprüfung** in der klassischen Reihenfolge: Vertrag → c.i.c. → GoA → dinglich → Delikt → Bereicherung.

## Testdatei

Zu jedem Skill gehört eine `test.md` mit mindestens einem vollständigen Durchlauf aus Eingabe und Ausgabe. Die Testdatei wird im Frontmatter referenziert (`test: ./test.md`).

## Einreichen

Öffnen Sie einen Pull Request gegen `main`. Die CI-Pipeline führt die Smoke-Tests aus und prüft das Frontmatter-Schema.
""",
    "bundles_body": """
Bundles fassen Skills zusammen, die regelmäßig gemeinsam eingesetzt werden. Sie sind kein eigenes Konzept im Dateibaum — jedes Plugin (Rechtsgebiet) ist selbst ein Bundle.

## Bundles je Rechtsgebiet

Jeder Ordner eines Rechtsgebiets (z. B. `arbeitsrecht/`, `kartellrecht/`, `datenschutzrecht/`) ist ein in sich geschlossenes Bundle aus Skills, gemeinsam genutzten Agenten und Tests. Mit dem Rechtsgebiet installieren Sie sämtliche darin enthaltenen Skills.

## Bundles über Rechtsgebiete hinweg

Manche Sachverhalte betreffen mehrere Rechtsgebiete. Häufige Kombinationen:

- **M&A-Due-Diligence**: `gesellschaftsrecht`, `kartellrecht`, `aussenwirtschaft-zoll-sanktionen`, `arbeitsrecht` (Sozialauswahl).
- **Launch eines KI-Produkts**: `ki-vo-compliance`, `datenschutzrecht`, `dsa-dma`, `produktrecht`.
- **Compliance-Grundausstattung**: `geldwaesche-aml-kyc`, `hinweisgeberschutz`, `lieferkettengesetz`, `csrd`.
- **Prüfung von IT-Verträgen**: `it-recht`, `datenschutzrecht`, `urheber-medienrecht`, `vertragsrecht`.
- **Vorfall im Betrieb**: `arbeitsrecht`, `datenschutzrecht`, `strafrecht`.

## Bundles in Claude Code zusammenstellen

Mehrere Plugins auf einmal installieren:

```bash
/plugin install gesellschaftsrecht
/plugin install kartellrecht
/plugin install aussenwirtschaft-zoll-sanktionen
/plugin install arbeitsrecht
```

Die Skills wirken dann über die gemeinsamen Researcher-, Drafter- und Reviewer-Agenten zusammen.
""",
    "custom_body": """
Jeder Skill in diesem Repository ist ein Ausgangspunkt. Passen Sie ihn an Ihre Kanzlei, Ihren internen Stil oder Ihr Mandat an.

## Was Sie anpassen können

- **Stil**: die voreingestellte Sie-Form durch die Du-Form ersetzen, wenn Ihre Unternehmenskultur das trägt.
- **Vorlagen**: jeder `Ausgabeformat`-Block lässt sich durch Ihren Briefkopf und Ihre Gliederung ersetzen.
- **Zitierdichte**: die Zahl der Kommentarnachweise erhöhen oder verringern, je nachdem, ob die Ausgabe an Partner, Mandantschaft oder Gericht geht.
- **Risikoschwellen**: die Risikohinweise unter `Risiken / typische Fehler` strenger oder großzügiger fassen.

## Anpassen, ohne Updates zu verlieren

Forken Sie das Repository. Legen Sie einen Overlay-Ordner `local/` an, der den Pfad des Ursprungs-Rechtsgebiets spiegelt, aber nur Ihre Überschreibungen enthält. Ihre `SKILL.md` unter `local/arbeitsrecht/skills/abmahnung/SKILL.md` verdrängt die stromaufwärts gelegene Fassung, wenn Sie `local/` zuerst laden.

## Eigene Normen und Kommentare ergänzen

Ergänzen Sie `references/kommentare.md` und `references/zitierweise.md` in Ihrem Fork. Zitieren Sie daraus wie gewohnt aus Ihrer SKILL.md.

## Anbietervarianten

Das Frontmatter-Feld `provider_variants:` steuert, welchen Anbietern ein Skill bereitgestellt wird. Wenn Sie ausschließlich Gemini nutzen, entfernen Sie `claude` und `openai`. Der Skill-Text selbst ändert sich dadurch nicht; es ändert sich nur, welche Adapter anbieterspezifische Manifeste erzeugen.
""",
    "orch_body": """
Die Skills dieses Repositorys folgen einer Sub-Agent-Architektur mit drei Rollen: **Researcher**, **Drafter**, **Reviewer**.

## Die drei Agenten

- **Researcher** (`agents/researcher.md`) — ermittelt Normen, Kommentarstellen und Rechtsprechung. Ergebnis ist eine Fundstellensammlung mit Links.
- **Drafter** (`agents/drafter.md`) — verfasst das Arbeitsergebnis (Schreiben, Vermerk, Schriftsatz, Ausgabevorlage).
- **Reviewer** (`agents/reviewer.md`) — prüft auf Bestimmtheit, Verhältnismäßigkeit, fehlende Nachweise und Risikohinweise.

## Wie die Orchestrierung abläuft

Jede `SKILL.md` deklariert die drei Agenten im Frontmatter:

```yaml
agents:
  researcher: ../../agents/researcher.md
  drafter: ../../agents/drafter.md
  reviewer: ../../agents/reviewer.md
```

Der Skill-Text beschreibt anschließend unter `## Sub-Agent-Architektur`, welcher Agent was übernimmt. Zur Laufzeit gilt:

1. Der Skill wird geladen.
2. Der Anbieter führt zuerst den `researcher` auf die Eingaben an.
3. Der `drafter` verarbeitet die Fundstellensammlung und erstellt das Arbeitsergebnis.
4. Der `reviewer` bewertet das Ergebnis, weist auf Risiken hin; die Endausgabe besteht aus Arbeitsergebnis und Reviewer-Hinweisen.

## Warum das wichtig ist

- **Die Fundstellen entstehen vor dem Arbeitsergebnis**, sodass der Drafter keine Fundstellen erfinden kann.
- **Der Reviewer hat das letzte Wort** — er sieht Eingabe und Ergebnis und kann die Freigabe verweigern.
- **Fehler bleiben lokal** — ist ein Nachweis falsch, korrigieren Sie den Researcher; stimmt der Ton nicht, den Drafter.

## Die Agenten anpassen

Bearbeiten Sie `agents/researcher.md`, `agents/drafter.md` und `agents/reviewer.md` in Ihrem Fork. Die Änderung wirkt für jeden Skill, der sie einbindet.
""",
    "ref_body": f"""
Die Referenz verweist auf die verbindliche Dokumentation, der jeder Skill dieses Repositorys folgt.

## Grundlagendokumente

- **[README.md]({GITHUB_URL}/blob/main/README.md)** — Projektüberblick, Installation und Architektur.
- **[CONVENTIONS.md]({GITHUB_URL}/blob/main/CONVENTIONS.md)** — anbieterneutrale Konventionen, die jeder Skill einhalten muss (Sprache, Methodik, Zitierdisziplin).
- **[VERIFICATION_STATUS.md]({GITHUB_URL}/blob/main/VERIFICATION_STATUS.md)** — aktueller Stand, für welche Plugins eine externe Prüfung der Rechtsprechungsnachweise abgeschlossen ist.
- **[CHANGELOG.md]({GITHUB_URL}/blob/main/CHANGELOG.md)** — wesentliche Änderungen je Release.
- **[QUICKSTART.md]({GITHUB_URL}/blob/main/QUICKSTART.md)** — Einstieg in 60 Sekunden.
- **[CONTRIBUTING.md]({GITHUB_URL}/blob/main/CONTRIBUTING.md)** — wie Sie einen Skill ergänzen oder korrigieren.

## Werkzeuge und Automatisierung

Deterministische Helfer, die ohne Modell laufen, sowie die Eval- und Prüfumgebung:

- **[references/rechner.md]({GITHUB_URL}/blob/main/references/rechner.md)** — deterministische Rechner: Fristen (§§ 187-193 BGB), Verjährung (§§ 195-199 BGB), RVG- und GKG-Gebühren sowie Feiertage aller 16 Bundesländer.
- **[scripts/verify_citations.py]({GITHUB_URL}/blob/main/scripts/verify_citations.py)** — löst `§`-Anker sowie ECLI- und CELEX-Fundstellen gegen gesetze-im-internet.de auf; standardmäßig nur informatorisch, mit `--strict` als Gate.
- **[evals/]({GITHUB_URL}/blob/main/evals/README.md)** — verhaltensbasierte, LLM-bewertete Eval-Umgebung (promptfoo), erzeugt aus den `test.md`-Dateien der einzelnen Skills.
- **[references/mcp-template.json]({GITHUB_URL}/blob/main/references/mcp-template.json)** — Anbindung an Live-Rechtsdaten über den MCP-Server von NeuRIS (rechtsinformationen.bund.de).

## Konventionen des Repositorys (Kurzfassung)

- **Ausgaben auf Deutsch.** Englische Begriffe nur, soweit etabliert (z. B. "Letter of Intent"), und bei erster Verwendung erläutert.
- **Grundsätzlich Gutachtenstil** für Vermerke und begründete Schreiben; **Urteilsstil** für Schriftsätze und kurze interne Notizen.
- **Anspruchsgrundlagenprüfung** in der klassischen Reihenfolge: Vertrag → c.i.c. → GoA → dinglich → Delikt → Bereicherung.
- **Auslegung** nach allen vier klassischen Methoden zuzüglich verfassungs- und unionsrechtskonformer Auslegung.

## Zustände von Rechtsprechungsnachweisen

Jeder Rechtsprechungsnachweis erhält genau eine Kennzeichnung:

| Zustand | Bedeutung |
|---|---|
| (ohne Kennzeichnung, mit URL) | gegen eine amtliche Quelle geprüft |
| `[unverifiziert – prüfen]` | Modellwissen, nicht extern bestätigt — vor Verwendung prüfen |
| `[generiert]` | in mandatsbezogenen Ausgaben unzulässig |

## Hinweis

Dies ist keine Rechtsberatung. Skill-Ausgaben sind Entwürfe zur Prüfung durch eine zugelassene Rechtsanwältin oder einen zugelassenen Rechtsanwalt bzw. Syndikusrechtsanwalt nach § 43a BRAO und § 2 BORA.
""",
})

_assert_strings_parity()


def _content_page(title, subtitle, body_md, rel, active, breadcrumbs, lang="en"):
    """Wrap markdown body inside the standard content-page shell."""
    body_html = md_to_html(body_md)
    body = f"""
<article class="content-page">
  <div class="page-header">
    <h1 class="page-title">{escape(title)}</h1>
    <p class="page-subtitle">{escape(subtitle)}</p>
  </div>
  {body_html}
</article>"""
    return page(f"{title} - {BRAND}", subtitle, rel, body, active=active,
                breadcrumbs=breadcrumbs, lang=lang)


def _bc(lang, *trail):
    """Breadcrumb helper. `trail` is a sequence of (string-key-or-literal, rel|None)."""
    b = lang_base(lang)
    out = [(T(lang, "bc_home"), f"{b}/")]
    for key, rel in trail:
        label = T(lang, key) if key in STRINGS[lang] else key
        out.append((label, f"{b}/{rel}" if rel is not None else None))
    return out


def gen_getting_started_index(catalog, lang="en"):
    total = catalog.get("total_skills", len(catalog["skills"]))
    areas = len(catalog.get("domains", {}))
    return _content_page(
        T(lang, "gs_title"),
        T(lang, "gs_subtitle"),
        T(lang, "gs_body", total=total, areas=areas),
        "getting-started/",
        active="getting-started",
        breadcrumbs=_bc(lang, ("bc_getting_started", None)),
        lang=lang,
    )


def gen_installation(catalog=None, lang="en"):
    return _content_page(
        T(lang, "install_title"),
        T(lang, "install_subtitle"),
        T(lang, "install_body"),
        "getting-started/installation/",
        active="getting-started",
        breadcrumbs=_bc(lang, ("bc_getting_started", "getting-started/"),
                        (T(lang, "install_title"), None)),
        lang=lang,
    )


def gen_platforms(catalog=None, lang="en"):
    return _content_page(
        T(lang, "platforms_title"),
        T(lang, "platforms_subtitle"),
        T(lang, "platforms_body"),
        "getting-started/platforms/",
        active="getting-started",
        breadcrumbs=_bc(lang, ("bc_getting_started", "getting-started/"),
                        (T(lang, "platforms_title"), None)),
        lang=lang,
    )


def gen_quick_start(catalog=None, lang="en"):
    return _content_page(
        T(lang, "qs_title"),
        T(lang, "qs_subtitle"),
        T(lang, "qs_body"),
        "getting-started/quick-start/",
        active="getting-started",
        breadcrumbs=_bc(lang, ("bc_getting_started", "getting-started/"),
                        (T(lang, "qs_title"), None)),
        lang=lang,
    )


def gen_guide_authoring(catalog=None, lang="en"):
    return _content_page(
        T(lang, "authoring_title"),
        T(lang, "authoring_subtitle"),
        T(lang, "authoring_body"),
        "guides/authoring/",
        active="guides",
        breadcrumbs=_bc(lang, ("bc_guides", "guides/authoring/"),
                        (T(lang, "authoring_title"), None)),
        lang=lang,
    )


def gen_guide_bundles(catalog=None, lang="en"):
    return _content_page(
        T(lang, "bundles_title"),
        T(lang, "bundles_subtitle"),
        T(lang, "bundles_body"),
        "guides/bundles/",
        active="guides",
        breadcrumbs=_bc(lang, ("bc_guides", "guides/authoring/"),
                        (T(lang, "bundles_title"), None)),
        lang=lang,
    )


def gen_guide_customization(catalog=None, lang="en"):
    return _content_page(
        T(lang, "custom_title"),
        T(lang, "custom_subtitle"),
        T(lang, "custom_body"),
        "guides/customization/",
        active="guides",
        breadcrumbs=_bc(lang, ("bc_guides", "guides/authoring/"),
                        (T(lang, "custom_title"), None)),
        lang=lang,
    )


def gen_guide_orchestration(catalog=None, lang="en"):
    return _content_page(
        T(lang, "orch_title"),
        T(lang, "orch_subtitle"),
        T(lang, "orch_body"),
        "guides/orchestration/",
        active="guides",
        breadcrumbs=_bc(lang, ("bc_guides", "guides/authoring/"),
                        (T(lang, "orch_title"), None)),
        lang=lang,
    )


def gen_reference_index(catalog=None, lang="en"):
    return _content_page(
        T(lang, "ref_title"),
        T(lang, "ref_subtitle"),
        T(lang, "ref_body"),
        "reference/",
        active="reference",
        breadcrumbs=_bc(lang, ("bc_reference", None)),
        lang=lang,
    )


def gen_404(lang="en"):
    """GitHub Pages serves a single 404 for the whole site, so it is English
    and links into both trees."""
    b = lang_base(lang)
    other = OTHER_LANG[lang]
    body = f"""
<div class="page-header" style="text-align:center; padding:80px 0 40px;">
  <h1 class="page-title">{escape(T(lang, "p404_title"))}</h1>
  <p class="page-subtitle" style="margin: 0 auto;">{escape(T(lang, "p404_text"))}</p>
  <div style="margin-top: 28px;">
    <a href="{b}/" class="btn btn-primary">{escape(T(lang, "btn_go_home"))}</a>
    <a href="{b}/SKILLS/" class="btn btn-secondary">{escape(T(lang, "btn_browse_skills"))}</a>
    <a href="{url_for(other)}" class="btn btn-secondary" hreflang="{other}" lang="{other}">{escape(T(lang, "p404_other_tree"))}</a>
  </div>
</div>"""
    # alt_url=None: there is only one 404 page, so no counterpart exists.
    return page(T(lang, "p404_title"), T(lang, "p404_text"), "404.html", body,
                lang=lang, alt_url=None)


# ---------------------------------------------------------------------------
# Sitemap, robots.txt, llms.txt
# ---------------------------------------------------------------------------

def gen_sitemap(entries):
    """Generate one sitemap.xml covering both language trees.

    `entries` is a list of (site_relative_path, priority). Each entry produces
    one <url> per language, and every <url> carries xhtml:link alternates for
    both languages plus x-default (English).
    """
    urlset = ET.Element(
        "urlset",
        {
            "xmlns": "http://www.sitemaps.org/schemas/sitemap/0.9",
            "xmlns:xhtml": "http://www.w3.org/1999/xhtml",
        },
    )
    lastmod = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    for rel, priority in entries:
        by_lang = {code: url_for(code, rel) for code in LANGS}
        for code in LANGS:
            u = ET.SubElement(urlset, "url")
            ET.SubElement(u, "loc").text = by_lang[code]
            ET.SubElement(u, "lastmod").text = lastmod
            ET.SubElement(u, "priority").text = str(priority)
            for alt in LANGS:
                ET.SubElement(
                    u, "xhtml:link",
                    {"rel": "alternate", "hreflang": alt, "href": by_lang[alt]},
                )
            ET.SubElement(
                u, "xhtml:link",
                {"rel": "alternate", "hreflang": "x-default", "href": by_lang["en"]},
            )
    tree = ET.ElementTree(urlset)
    ET.indent(tree, space="  ")
    out = '<?xml version="1.0" encoding="UTF-8"?>\n'
    out += ET.tostring(urlset, encoding="unicode")
    return out


def gen_robots_txt():
    return f"""User-agent: *
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
"""


def gen_llms_txt(catalog, lang="en"):
    """Generate llms.txt following the llms.txt convention, per language.

    Counts always come from skills.json — never hardcoded.
    """
    total = len(catalog["skills"])
    domains = catalog.get("domains", {})
    areas = len(domains)
    b = lang_base(lang)

    lines = [
        f"# {BRAND}",
        "",
        f"> {T(lang, 'llms_tagline', total=total, areas=areas)}",
        "",
        f"{T(lang, 'llms_website')}: {b}",
        f"{T(lang, 'llms_repository')}: {GITHUB_URL}",
        f"{T(lang, 'llms_license')}: {T(lang, 'footer_license')}",
        f"{T(lang, 'llms_author')}: {AUTHOR}",
        "",
        T(lang, "llms_h_what"),
        "",
        T(lang, "llms_what"),
        "",
        T(lang, "llms_h_lang"),
        "",
        T(lang, "llms_lang",
          en_url=url_for("en"), de_url=url_for("de"),
          en_llms=f"{lang_base('en')}/llms.txt", de_llms=f"{lang_base('de')}/llms.txt"),
        "",
        T(lang, "llms_h_how"),
        "",
        "```",
        f"git clone {GITHUB_URL}.git",
        "/plugin marketplace add borghei/AI-Skills-German-Law",
        "/plugin install arbeitsrecht",
        "/arbeitsrecht:abmahnung",
        "```",
        "",
        T(lang, "llms_h_areas"),
        "",
    ]

    for d in sorted(domains.keys()):
        info = domains[d]
        cnt = info.get("count", 0)
        lines.append(f"- {info.get('label', d)}: {n_skills(lang, cnt)} — {info.get('desc', '')}")

    lines += ["", T(lang, "llms_h_all"), ""]
    for s in sorted(catalog["skills"], key=lambda x: (x["domain"], x["name"])):
        lines.append(
            f"- [{pretty_name(s['name'])}]({b}/SKILLS/{s['domain']}/{s['name']}.html): "
            f"{truncate(s.get('description', ''), 140)}"
        )

    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Static asset preservation
# ---------------------------------------------------------------------------

def preserve_static_assets():
    """Ensure existing site/assets, site/css, site/js are preserved.

    The German-law repo already ships with a small hand-coded set of static
    assets (assets/header.svg, css/style.css, js/main.js). The generator only
    rewrites HTML — it does not touch these directories. This function is a
    no-op placeholder that prints what is preserved.
    """
    for sub in ("assets", "css", "js"):
        p = SITE_DIR / sub
        if p.exists():
            print(f"  preserving {p}")


# ---------------------------------------------------------------------------
# Main orchestration
# ---------------------------------------------------------------------------

def generate_full_site():
    """Generate the complete static site."""
    global DOMAIN_META
    catalog = load_catalog()
    DOMAIN_META = build_domain_meta(catalog)
    skills = catalog["skills"]

    # Group skills by domain
    by_domain = {}
    for s in skills:
        by_domain.setdefault(s["domain"], []).append(s)

    static_pages = [
        ("getting-started/", gen_getting_started_index, "0.7"),
        ("getting-started/installation/", gen_installation, "0.6"),
        ("getting-started/platforms/", gen_platforms, "0.6"),
        ("getting-started/quick-start/", gen_quick_start, "0.6"),
        ("guides/authoring/", gen_guide_authoring, "0.6"),
        ("guides/bundles/", gen_guide_bundles, "0.6"),
        ("guides/customization/", gen_guide_customization, "0.6"),
        ("guides/orchestration/", gen_guide_orchestration, "0.6"),
        ("reference/", gen_reference_index, "0.6"),
    ]

    # Site-relative paths, shared by both trees. Collected once from the EN
    # pass so the sitemap can emit both languages with hreflang alternates.
    sitemap_entries = []
    per_lang_counts = {}
    generated = 0

    for lang in LANGS:
        n = 0

        def emit(rel_dir_or_file, html, prio=None, is_dir=True):
            """Write one page and (once) record it for the sitemap."""
            nonlocal n
            rel_file = (rel_dir_or_file + "index.html") if is_dir else rel_dir_or_file
            write_file(str(out_path(lang, rel_file)), html)
            if prio is not None and lang == LANGS[0]:
                sitemap_entries.append((rel_dir_or_file, prio))
            n += 1

        # 1. Landing
        emit("", gen_landing(catalog, by_domain, lang), "1.0")

        # 2. Skills index
        emit("SKILLS/", gen_skills_index(catalog, by_domain, lang), "0.9")

        # 3. Area index pages
        for domain, domain_skills in sorted(by_domain.items()):
            emit(f"SKILLS/{domain}/", gen_domain_page(domain, domain_skills, catalog, lang), "0.8")

        # 4. Individual skill pages
        for s in skills:
            emit(
                f"SKILLS/{s['domain']}/{s['name']}.html",
                gen_skill_page(s, catalog, by_domain, lang),
                "0.7",
                is_dir=False,
            )

        # 5. Static content pages
        for rel, fn, prio in static_pages:
            emit(rel, fn(catalog, lang), prio)

        # 6. llms.txt per tree
        emit("llms.txt", gen_llms_txt(catalog, lang), None, is_dir=False)

        per_lang_counts[lang] = n
        generated += n

    # 7. Single-instance files at the root: 404 (GitHub Pages serves one),
    #    robots.txt, and the combined sitemap.
    write_file(str(SITE_DIR / "404.html"), gen_404("en"))
    generated += 1
    write_file(str(SITE_DIR / "sitemap.xml"), gen_sitemap(sitemap_entries))
    generated += 1
    write_file(str(SITE_DIR / "robots.txt"), gen_robots_txt())
    generated += 1

    pruned = prune_stale_pages()

    preserve_static_assets()

    counts = " / ".join(f"{lang}: {c}" for lang, c in per_lang_counts.items())
    print(f"\nGenerated {generated} files in {SITE_DIR}/")
    print(f"  - {len(LANGS)} language trees ({counts} files each tree)")
    for lang in LANGS:
        root = "site/" if lang == "en" else f"site/{LANG_DIR[lang]}/"
        print(f"    [{lang}] {root} — 1 landing, 1 skills index, "
              f"{len(by_domain)} area pages, {len(skills)} skill pages, "
              f"{len(static_pages)} content pages, llms.txt")
    print(f"  - 404.html, sitemap.xml (both trees + hreflang), robots.txt")

    if pruned:
        print(f"  - pruned {len(pruned)} stale page(s) no longer in the catalog:")
        for rel in pruned:
            print(f"      {rel}")

    if len(set(per_lang_counts.values())) != 1:
        raise SystemExit(f"Tree page counts differ: {per_lang_counts}")


def generate_single_skill(skill_name):
    """Generate a single skill page."""
    global DOMAIN_META
    catalog = load_catalog()
    DOMAIN_META = build_domain_meta(catalog)
    by_domain = {}
    for s in catalog["skills"]:
        by_domain.setdefault(s["domain"], []).append(s)

    matches = [s for s in catalog["skills"] if s["name"] == skill_name]
    if not matches:
        print(f"Error: skill '{skill_name}' not found in skills.json")
        sys.exit(1)

    for s in matches:
        for lang in LANGS:
            html = gen_skill_page(s, catalog, by_domain, lang)
            rel = f"SKILLS/{s['domain']}/{s['name']}.html"
            path = write_file(str(out_path(lang, rel)), html)
            print(f"Generated [{lang}] {path}")


def generate_single_domain(domain_name):
    """Generate pages for a single domain."""
    global DOMAIN_META
    catalog = load_catalog()
    DOMAIN_META = build_domain_meta(catalog)
    by_domain = {}
    for s in catalog["skills"]:
        by_domain.setdefault(s["domain"], []).append(s)

    if domain_name not in by_domain:
        print(f"Error: domain '{domain_name}' not found. Available: {', '.join(sorted(by_domain.keys()))}")
        sys.exit(1)

    domain_skills = by_domain[domain_name]

    for lang in LANGS:
        html = gen_domain_page(domain_name, domain_skills, catalog, lang)
        path = write_file(str(out_path(lang, f"SKILLS/{domain_name}/index.html")), html)
        print(f"Generated [{lang}] {path}")

        for s in domain_skills:
            html = gen_skill_page(s, catalog, by_domain, lang)
            path = write_file(str(out_path(lang, f"SKILLS/{s['domain']}/{s['name']}.html")), html)
            print(f"Generated [{lang}] {path}")

    print(f"\n{(len(domain_skills) + 1) * len(LANGS)} pages generated for "
          f"{domain_label(domain_name)} across {len(LANGS)} language trees")


def main():
    parser = argparse.ArgumentParser(description=f"Generate {BRAND} static site")
    parser.add_argument("--skill", help="Generate page for a single skill by name")
    parser.add_argument("--domain", help="Generate pages for a single domain")
    args = parser.parse_args()

    if args.skill:
        generate_single_skill(args.skill)
    elif args.domain:
        generate_single_domain(args.domain)
    else:
        generate_full_site()


if __name__ == "__main__":
    main()
