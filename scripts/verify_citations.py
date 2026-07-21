#!/usr/bin/env python3
"""Layer-A citation verifier for ai-skills-german-law.

This script is the *deterministic* citation check ("Layer A"): it scans
SKILL.md files (or an arbitrary text file) for legal citations and validates
them by **format/structure** offline, and — only with ``--online`` — by
resolving German statute URLs over HTTP. It turns the repo's manual
``[unverifiziert – prüfen]`` discipline (see references/zitierweise.md) into an
automated check.

It does NOT call any LLM and has NO third-party dependencies — vanilla
Python 3.10+ standard library only (see requirements.txt).

It detects and validates four citation kinds:

1.  German statute anchors — ``§ 1 KSchG``, ``§ 102 Abs. 1 BetrVG``,
    ``§ 626 BGB``, ``Art. 6 DSGVO``, ``Art. 12 GG``. The paragraph/article
    number plus the Gesetz abbreviation are parsed; the abbreviation is looked
    up in a map of common German law abbreviations -> gesetze-im-internet.de
    URL slug (seeded from references/primary-sources.md). Offline: an unknown
    abbreviation is flagged ("cannot verify"). Online: the consolidated
    ``__<num>.html`` page is resolved and reported as exists (200) / missing
    (404) / network-error.

2.  ECLI identifiers — ``ECLI:EU:C:1995:463``, ``ECLI:DE:BGH:2023:...``.
    The 5-part grammar ``ECLI:<country>:<court>:<year>:<ordinal>`` is checked.

3.  EU CELEX numbers — ``32016R0679`` (DSGVO), ``32024R1689`` (KI-VO).
    Sector / year / descriptor / number format is checked.

4.  Case-law citations without ECLI — ``BAG, Urt. v. 10.06.2010 - 2 AZR
    541/09`` or a bare Aktenzeichen ``2 AZR 541/09`` / EuGH ``C-311/18``.
    These cannot be resolved deterministically, so the structural plausibility
    is checked and — per the repo's own discipline — any case-law citation
    that lacks a nearby ``[unverifiziert`` / ``[generiert`` marker is reported
    as needing one (statutes with a gesetze-im-internet link need no marker).

Exit codes:
- 0  no hard failures (default, non-strict, offline → informational only,
     so CI is not broken)
- 1  hard failures: an online 404, or — with ``--strict`` — any warning
     (unknown abbreviation, malformed ECLI/CELEX, unmarked case-law citation)
- 2  usage error

Usage:
    python scripts/verify_citations.py                      # all SKILL.md, offline
    python scripts/verify_citations.py --area arbeitsrecht
    python scripts/verify_citations.py --skill arbeitsrecht/kuendigungs-pruefung
    python scripts/verify_citations.py --file some.txt      # scan an arbitrary file
    python scripts/verify_citations.py --online             # resolve statute URLs
    python scripts/verify_citations.py --strict             # warnings become failures
    python scripts/verify_citations.py --json
"""
from __future__ import annotations

import argparse
import json
import re
import ssl
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from enum import IntEnum
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

# Areas mirror eval.py / validate.py (the full plugin set).
AREAS = [
    "arbeitsrecht",
    "datenschutzrecht",
    "vertragsrecht",
    "mietrecht",
    "wohnungseigentumsrecht",
    "gesellschaftsrecht",
    "strafrecht",
    "ki-vo-compliance",
    "nis2",
    "hinweisgeberschutz",
    "lieferkettengesetz",
    "dora",
    "dsa-dma",
    "csrd",
    "insolvenzrecht",
    "prozessrecht",
    "it-recht",
    "bankrecht",
    "erbrecht",
    "familienrecht",
    "betreuungsrecht",
    "gewerblicher-rechtsschutz",
    "steuerrecht",
    "verwaltungsrecht",
    "europarecht",
    "verfassungsrecht",
    "umweltrecht",
    "sozialrecht",
    "vergaberecht",
    "wettbewerbsrecht",
    "handelsrecht",
    "medizinrecht",
    "versicherungsrecht",
    "baurecht",
    "aussenwirtschaft-zoll-sanktionen",
    "geldwaesche-aml-kyc",
    "energierecht",
    "verkehrsrecht",
    "transportrecht",
    "produktrecht",
    "ki-governance",
    "patentrecht",
    "migrationsrecht",
    "agrarrecht",
    "sportrecht",
    "urheber-medienrecht",
    "berufsrecht-anwaltschaft",
    "kapitalmarktrecht",
    "kartellrecht",
]

GII_BASE = "https://www.gesetze-im-internet.de"
EURLEX_CELEX = "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:{celex}"
ECLI_RESOLVER = "https://e-justice.europa.eu/ecli/{ecli}"

# ---------------------------------------------------------------------------
# Abbreviation -> gesetze-im-internet.de slug.
# Seeded from references/primary-sources.md and references/zitierweise.md,
# extended with the most common German statute abbreviations.
# ---------------------------------------------------------------------------
STATUTE_SLUGS: dict[str, str] = {
    # Bürgerliches Recht
    "BGB": "bgb",
    "EGBGB": "bgbeg",
    "BeurkG": "beurkg",
    "WEG": "woeigg",
    "ProdHaftG": "prodhaftg",
    # Handels- und Gesellschaftsrecht
    "HGB": "hgb",
    "GmbHG": "gmbhg",
    "AktG": "aktg",
    "UmwG": "umwg_1995",
    "GenG": "geng",
    "PartGG": "partgg",
    # Arbeitsrecht
    "KSchG": "kschg",
    "BetrVG": "betrvg",
    "AGG": "agg",
    "ArbZG": "arbzg",
    "MiLoG": "milog",
    "TzBfG": "tzbfg",
    "MuSchG": "muschg_2018",
    "BEEG": "beeg",
    "BUrlG": "burlg",
    "EFZG": "entgfg",
    "AÜG": "a_g",
    "NachwG": "nachwg",
    "PflegeZG": "pflegezg",
    "ArbGG": "arbgg",
    "ArbSchG": "arbschg",
    "SprAuG": "spraug",
    "BBiG": "bbig_2005",
    # Sozialgesetzbücher
    "SGB I": "sgb_1",
    "SGB II": "sgb_2",
    "SGB III": "sgb_3",
    "SGB IV": "sgb_4",
    "SGB V": "sgb_5",
    "SGB VI": "sgb_6",
    "SGB VII": "sgb_7",
    "SGB VIII": "sgb_8",
    "SGB IX": "sgb_9_2018",
    "SGB X": "sgb_10",
    "SGB XI": "sgb_11",
    "SGB XII": "sgb_12",
    # Mietrecht / Wohnen
    "BetrKV": "betrkv",
    "HeizkostenV": "heizkostenv",
    # Datenschutz / IT
    "BDSG": "bdsg_2018",
    "TTDSG": "ttdsg",
    "TMG": "tmg",
    "TKG": "tkg_2021",
    # Straf- und Verkehrsrecht
    "StGB": "stgb",
    "StPO": "stpo",
    "OWiG": "owig_1968",
    "StVG": "stvg",
    "StVO": "stvo_2013",
    "BKatV": "bkatv_2013",
    "JGG": "jgg",
    # Verfahrensrecht
    "ZPO": "zpo",
    "GVG": "gvg",
    "VwGO": "vwgo",
    "FamFG": "famfg",
    "FGO": "fgo",
    "SGG": "sgg",
    "BVerfGG": "bverfgg",
    "ZVG": "zvg",
    # Verwaltung / öffentliches Recht
    "VwVfG": "vwvfg",
    "GewO": "gewo",
    "AufenthG": "aufenthg",
    "AsylG": "asylvfg_1992",
    # Kosten / Berufsrecht
    "GKG": "gkg_2004",
    "RVG": "rvg",
    "BRAO": "brao",
    "RDG": "rdg",
    "BNotO": "bnoto",
    "GNotKG": "gnotkg",
    # Insolvenz / Sanierung
    "InsO": "inso",
    "StaRUG": "starug",
    # Steuerrecht
    "AO": "ao_1977",
    "EStG": "estg",
    "UStG": "ustg_1980",
    "GewStG": "gewstg",
    "KStG": "kstg",
    "ErbStG": "erbstg_1974",
    # Gewerblicher Rechtsschutz / Wettbewerb
    "UrhG": "urhg",
    "MarkenG": "markeng",
    "PatG": "patg",
    "GebrMG": "gebrmg",
    "DesignG": "geschmmg",
    "GeschGehG": "geschgehg",
    "UWG": "uwg",
    "GWB": "gwb",
    "VgV": "vgv",
    # Umwelt / Energie
    "BImSchG": "bimschg",
    "KrWG": "krwg",
    "WHG": "whg",
    "EnWG": "enwg",
    "BauGB": "bbaug",
    # Versicherung
    "VVG": "vvg_2008",
    # Finanz- / Kapitalmarktrecht
    "WpHG": "wphg",
    "WpÜG": "wp_g",
    "KWG": "kredwg",
    "VAG": "vag_2016",
    "ZAG": "zag_2018",
    "KAGB": "kagb",
    "GwG": "gwg_2017",
    # Energie / Umwelt (zusätzlich)
    "EEG": "eeg_2023",
    "EnEfG": "enefg",
    "UVPG": "uvpg",
    "UmwRG": "umwrg",
    "KSpG": "kspg",
    # Außenwirtschaft / Zoll
    "AWG": "awg_2013",
    "AWV": "awv_2013",
    # Verkehr (zusätzlich)
    "FeV": "fev",
    "FZV": "fzv_2011",
    # Agrarrecht
    "GrdstVG": "grdstvg",
    "LwAnpG": "lwanpg",
    "BauGBMaßnahmenG": "baugbma_g",
    # Lieferkette / Hinweisgeber / Prospekt
    "LkSG": "lksg",
    "HinSchG": "hinschg",
    "WpPG": "wppg",
    "EDL-G": "edl-g",
}

# Real German/EU/international norms that are NOT published on
# gesetze-im-internet.de: völkerrechtliche Übereinkommen, Kammer-/Satzungsrecht
# and Landesrecht. Reported informationally ("known, verify elsewhere") rather
# than as an unknown abbreviation, since the tool genuinely cannot resolve them
# against the Bundesrecht corpus.
KNOWN_NON_GII: dict[str, str] = {
    "CMR": "Übereinkommen über den Beförderungsvertrag im int. Straßengüterverkehr",
    "EMRK": "Europäische Menschenrechtskonvention",
    "EPÜ": "Europäisches Patentübereinkommen",
    "PCT": "Patent Cooperation Treaty",
    "EuGVVO": "Brüssel-Ia-Verordnung (EU-Recht, via EUR-Lex)",
    "FAO": "Fachanwaltsordnung (Satzungsrecht der BRAK)",
    "BORA": "Berufsordnung für Rechtsanwälte (Satzungsrecht)",
    "BORA-": "Berufsordnung für Rechtsanwälte (Satzungsrecht)",
    "MBO-Ä": "Musterberufsordnung Ärzte (Kammerrecht)",
    "MStV": "Medienstaatsvertrag (Landesrecht der Länder)",
    "RStV": "Rundfunkstaatsvertrag (Landesrecht)",
    "JuSchG": "Jugendschutz (teils Landesrecht/Staatsvertrag)",
}

# Abbreviations cited Art.-style on gesetze-im-internet.de (art_<num>.html).
GII_ART_STYLE = {"GG"}
STATUTE_SLUGS["GG"] = "gg"

# EU instruments cited as "Art. N <Abbr>": resolved via EUR-Lex CELEX (the
# specific article cannot be deep-linked deterministically, so these are
# reported informationally with the law-level CELEX link).
EU_CELEX: dict[str, str] = {
    "DSGVO": "32016R0679",
    "GDPR": "32016R0679",
    "KI-VO": "32024R1689",
    "AI-Act": "32024R1689",
    "DSA": "32022R2065",
    "DMA": "32022R1925",
    "DORA": "32022R2554",
    "MiCAR": "32023R1114",
    "MiCA": "32023R1114",
    "NIS2": "32022L2555",
    "DSGVO-DGA": "32022R0868",
    "AEUV": "12012E/TXT",
    "EUV": "12012M/TXT",
    "MAR": "32014R0596",
    "GPSR": "32023R0988",
    "UZK": "32013R0952",
    "CSRD": "32022L2464",
    "DGA": "32022R0868",
    "Prospekt-VO": "32017R1129",
    "ProspektVO": "32017R1129",
}

# ---------------------------------------------------------------------------
# Regexes
# ---------------------------------------------------------------------------
# Statute: § / §§ / Art. + number (+ optional Abs./S./Nr. and ranges) + abbr.
# "filler" swallows subdivision markers and ranges between the number and the
# law abbreviation (e.g. "§ 102 Abs. 1 S. 3 BetrVG", "§§ 17–18 KSchG",
# "§§ 622 und 626 BGB").
_FILLER = (
    r"(?:\s*(?:Abs\.|S\.|Satz|Nr\.|Halbs\.|Halbsatz|Alt\.|lit\.|Buchst\.|"
    r"und|u\.|bis|f\.|ff\.|[IVX]{1,4}|,|;|–|-)\s*\d*\s*[a-z]?)*"
)
_ABBR = (
    r"[A-ZÄÖÜ][A-Za-z0-9ÄÖÜäöüß]*"      # leading token
    r"(?:-[A-ZÄÖÜ0-9]+\b)*"               # hyphenated ALL-CAPS tail only
    r"(?:\s[IVXL]{1,5}\b)?"               # roman book number (SGB IX)
)
# The hyphen tail is restricted to all-caps acronym segments so that German
# compounds following a cite ("DSGVO-konform", "BGB-Klausel", "AGG-Novelle")
# are not swallowed into the abbreviation - only "KI-VO", "DSGVO-DGA" etc.
STATUTE_RE = re.compile(
    r"(?P<marker>§§?|Art\.?)\s*"
    r"(?P<num>\d+[a-z]?)"
    + _FILLER
    + r"\s+(?P<abbr>" + _ABBR + r")"
)

# ECLI: 5 colon-separated parts.
ECLI_RE = re.compile(r"\bECLI:[A-Za-z0-9.]+:[A-Za-z0-9.]+:[A-Za-z0-9.]+:[A-Za-z0-9.]+\b")
ECLI_VALID_RE = re.compile(r"^ECLI:[A-Z]{2}:[A-Za-z0-9]{1,15}:\d{4}:[A-Za-z0-9.]+$")

# CELEX: sector digit + 4-digit year + descriptor letter(s) + running number.
CELEX_RE = re.compile(r"\b\d(?:19|20)\d{2}[A-Z]{1,2}\d{3,4}\b")

# Aktenzeichen (German courts): senate (roman/arabic) + registry letters +
# running-number/2-digit-year, e.g. "2 AZR 541/09", "1 BvL 15/87",
# "VIII ZR 117/22".
AZ_RE = re.compile(r"\b(?:[IVXL]{1,5}|\d{1,3})\s+[A-Za-z]{2,5}\s+\d{1,5}/\d{2,4}\b")
# EU court docket numbers, e.g. "C-311/18", "T-201/04", "C-311/2018".
EU_DOCKET_RE = re.compile(r"\b[CTF]-\d{1,4}/\d{2,4}\b")

# Verification markers used across the repo (zitierweise.md).
MARKER_RE = re.compile(r"\[(?:unverifiziert|generiert)\b")

# Markdown heading lines (used to scope a section-wide marker).
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s")

# Tokens that look like an abbreviation in the "§ N <token>" position but are
# really commentary pin-cites (Randnummer/Randziffer/Seite) or subdivisions —
# e.g. "§ 622 Rn. 1 ff." in "Berkowsky, in: MüKoBGB, ..., § 622 Rn. 1 ff."
NON_STATUTE_TOKENS = {
    "Rn", "Rz", "Randnummer", "Randziffer", "S", "Seite",
    "Abs", "Nr", "Halbs", "Halbsatz", "Alt", "Var", "Buchst", "lit",
}


# ---------------------------------------------------------------------------
# Findings
# ---------------------------------------------------------------------------
class Severity(IntEnum):
    INFO = 0
    WARN = 1
    FAIL = 2


@dataclass
class Finding:
    source: str
    line: int
    kind: str           # statute | ecli | celex | caselaw
    citation: str
    severity: Severity
    message: str
    url: str | None = None

    def counts_as_failure(self, strict: bool) -> bool:
        if self.severity == Severity.FAIL:
            return True
        if strict and self.severity == Severity.WARN:
            return True
        return False

    def to_dict(self) -> dict:
        return {
            "source": self.source,
            "line": self.line,
            "kind": self.kind,
            "citation": self.citation,
            "severity": self.severity.name,
            "message": self.message,
            "url": self.url,
        }


# ---------------------------------------------------------------------------
# Online resolution (only used with --online)
# ---------------------------------------------------------------------------
_SSL_CTX = ssl.create_default_context()
_UA = "ai-skills-german-law citation verifier (stdlib urllib; offline-first)"


def http_status(url: str, cache: dict[str, int], timeout: float = 6.0) -> int:
    """Return the HTTP status for *url*, or -1 on a network/transport error.

    Results are cached per-URL so repeated citations do not hammer the server.
    """
    if url in cache:
        return cache[url]
    req = urllib.request.Request(url, headers={"User-Agent": _UA}, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=_SSL_CTX) as resp:
            status = getattr(resp, "status", resp.getcode())
    except urllib.error.HTTPError as exc:
        status = exc.code
    except Exception:  # noqa: BLE001 — network errors must never crash the run
        status = -1
    cache[url] = status
    return status


# ---------------------------------------------------------------------------
# URL builders
# ---------------------------------------------------------------------------
def statute_url(abbr: str, num: str, marker: str) -> str | None:
    """Build the official source URL for a statute citation, if resolvable."""
    if abbr in EU_CELEX:
        return EURLEX_CELEX.format(celex=EU_CELEX[abbr])
    slug = STATUTE_SLUGS.get(abbr)
    if not slug:
        return None
    if abbr in GII_ART_STYLE or marker.startswith("Art"):
        return f"{GII_BASE}/{slug}/art_{num}.html"
    return f"{GII_BASE}/{slug}/__{num}.html"


# ---------------------------------------------------------------------------
# Per-line scanners
# ---------------------------------------------------------------------------
def _scan_statutes(line: str, lineno: int, source: str, online: bool,
                   cache: dict[str, int]) -> list[Finding]:
    findings: list[Finding] = []
    for m in STATUTE_RE.finditer(line):
        marker = m.group("marker")
        num = m.group("num")
        abbr = re.sub(r"\s+", " ", m.group("abbr").strip())
        citation = re.sub(r"\s+", " ", m.group(0).strip())

        # The roman-book tail ("SGB IX") is only meaningful for SGB. For any
        # other base, a trailing roman numeral is a stray following token
        # ("§ 5 GG I." -> abbr "GG I"); reduce to the base abbreviation.
        if " " in abbr and abbr.split(" ", 1)[0] != "SGB":
            abbr = abbr.split(" ", 1)[0]

        if abbr in NON_STATUTE_TOKENS:
            # Commentary pin-cite (e.g. "§ 622 Rn. 1") — not a statute anchor.
            continue
        # A bare Roman numeral after the number is an Absatz in German shorthand
        # ("§ 115 I", "§ 19 II") with no abbreviation following — not a citation.
        if re.fullmatch(r"[IVXLC]{1,6}", abbr):
            continue
        # Bare "VO" (generic "Verordnung") with no specific instrument is not
        # resolvable; the concrete regulation is named elsewhere in the text.
        if abbr in {"VO", "RL"}:
            continue
        # Known norms that are not on gesetze-im-internet.de (conventions,
        # Kammer-/Landesrecht) — report as info, not as an unknown abbreviation.
        if abbr in KNOWN_NON_GII:
            findings.append(Finding(
                source, lineno, "statute", citation, Severity.INFO,
                f"{abbr}: {KNOWN_NON_GII[abbr]} — nicht auf gesetze-im-internet.de, "
                "anderweitig prüfen",
            ))
            continue
        # Real statute abbreviations carry >= 2 uppercase letters (BGB, ZPO,
        # GG, KSchG, KI-VO, ...). A single-capital token after the number is a
        # sentence word ("Verstoß") or an Absatz roman numeral ("§ 115 I") —
        # not a citation, so skip it silently.
        if sum(1 for ch in abbr if ch.isupper()) < 2:
            continue

        if abbr in EU_CELEX:
            url = statute_url(abbr, num, marker)
            findings.append(Finding(
                source, lineno, "statute", citation, Severity.INFO,
                f"EU instrument ({abbr}, CELEX {EU_CELEX[abbr]}); "
                "article-level deep link not resolvable deterministically",
                url,
            ))
            continue

        if abbr not in STATUTE_SLUGS:
            findings.append(Finding(
                source, lineno, "statute", citation, Severity.WARN,
                f"unknown abbreviation '{abbr}' — not in known statute map, "
                "cannot verify",
            ))
            continue

        url = statute_url(abbr, num, marker)
        if not online:
            findings.append(Finding(
                source, lineno, "statute", citation, Severity.INFO,
                f"known abbreviation '{abbr}' (offline: format ok)", url,
            ))
            continue

        status = http_status(url, cache) if url else -1
        if status == 200:
            findings.append(Finding(
                source, lineno, "statute", citation, Severity.INFO,
                f"resolved HTTP 200 — paragraph exists", url,
            ))
        elif status == 404:
            findings.append(Finding(
                source, lineno, "statute", citation, Severity.FAIL,
                f"HTTP 404 — § {num} does not exist in consolidated {abbr}", url,
            ))
        else:
            findings.append(Finding(
                source, lineno, "statute", citation, Severity.INFO,
                f"network/transport issue (status {status}) — could not verify",
                url,
            ))
    return findings


def _scan_ecli(line: str, lineno: int, source: str, online: bool,
               has_marker: bool) -> list[Finding]:
    findings: list[Finding] = []
    for m in ECLI_RE.finditer(line):
        ecli = m.group(0)
        if not ECLI_VALID_RE.match(ecli):
            findings.append(Finding(
                source, lineno, "ecli", ecli, Severity.WARN,
                "malformed ECLI — expected ECLI:<CC>:<court>:<year>:<ordinal>",
            ))
            continue
        country = ecli.split(":")[1]
        resolver = ECLI_RESOLVER.format(ecli=ecli) if online else None
        # ECLI:DE (and EU court decisions) are case law → expect a marker.
        if not has_marker:
            findings.append(Finding(
                source, lineno, "ecli", ecli, Severity.WARN,
                f"valid ECLI ({country}) but unmarked case-law citation — "
                "add [unverifiziert] or verify",
                resolver,
            ))
        else:
            findings.append(Finding(
                source, lineno, "ecli", ecli, Severity.INFO,
                f"valid ECLI ({country}); marker present", resolver,
            ))
    return findings


def _scan_celex(line: str, lineno: int, source: str) -> list[Finding]:
    findings: list[Finding] = []
    for m in CELEX_RE.finditer(line):
        celex = m.group(0)
        findings.append(Finding(
            source, lineno, "celex", celex, Severity.INFO,
            f"valid CELEX format (sector {celex[0]}, year {celex[1:5]})",
            EURLEX_CELEX.format(celex=celex),
        ))
    return findings


# Hosts that count as an authoritative decision source. Per CONVENTIONS.md the
# verified state is "no marker, WITH a source URL" - so an Aktenzeichen carrying
# one of these links is verified, not unmarked. Without this the checker would
# punish verification: removing a marker and adding a source URL would turn a
# silent INFO into a WARN, making the warning count rise as quality improves.
VERIFICATION_HOSTS = (
    "dejure.org",
    "bundesgerichtshof.de",
    "bverfg.de",
    "bverwg.de",
    "bsg.bund.de",
    "bundesarbeitsgericht.de",
    "bundesfinanzhof.de",
    "openjur.net",
    "curia.europa.eu",
    "lexetius.com",
    "rechtsprechung-im-internet.de",
)


def has_verification_source(line: str) -> bool:
    """True if the line carries a link to an authoritative decision source."""
    return any(host in line for host in VERIFICATION_HOSTS)


def _scan_caselaw(line: str, lineno: int, source: str,
                  has_marker: bool) -> list[Finding]:
    """Aktenzeichen / EU docket numbers without ECLI — manual-verify check."""
    findings: list[Finding] = []
    seen: set[str] = set()
    verified = has_verification_source(line)
    for rx in (AZ_RE, EU_DOCKET_RE):
        for m in rx.finditer(line):
            az = m.group(0)
            if az in seen:
                continue
            seen.add(az)
            if has_marker:
                findings.append(Finding(
                    source, lineno, "caselaw", az, Severity.INFO,
                    "case-law citation with verification marker (needs manual "
                    "verification, marker correctly present)",
                ))
            elif verified:
                findings.append(Finding(
                    source, lineno, "caselaw", az, Severity.INFO,
                    "case-law citation without marker but with an authoritative "
                    "source link — verified state per CONVENTIONS.md",
                ))
            else:
                findings.append(Finding(
                    source, lineno, "caselaw", az, Severity.WARN,
                    "unmarked case-law citation — add [unverifiziert] or verify",
                ))
    return findings


def scan_text(text: str, source: str, online: bool,
              cache: dict[str, int]) -> list[Finding]:
    """Scan *text* line by line and return all citation findings.

    A verification marker counts for a case-law citation if it appears on the
    same line OR in the most recent markdown heading governing the current
    section (the repo uses headings like "### Rechtsprechung (alle
    `[unverifiziert – prüfen]`)" to mark a whole list at once).
    """
    findings: list[Finding] = []
    section_marker = False
    in_fence = False
    for lineno, line in enumerate(text.splitlines(), start=1):
        # Skip fenced code blocks: citations inside ``` ... ``` are illustrative
        # examples (sample outputs, templates), not claims to be verified.
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if HEADING_RE.match(line):
            section_marker = bool(MARKER_RE.search(line))
        has_marker = section_marker or bool(MARKER_RE.search(line))
        findings.extend(_scan_statutes(line, lineno, source, online, cache))
        findings.extend(_scan_ecli(line, lineno, source, online, has_marker))
        findings.extend(_scan_celex(line, lineno, source))
        findings.extend(_scan_caselaw(line, lineno, source, has_marker))
    return findings


# ---------------------------------------------------------------------------
# Target discovery (mirrors eval.py find_skills)
# ---------------------------------------------------------------------------
@dataclass
class ScanTarget:
    name: str
    path: Path
    findings: list[Finding] = field(default_factory=list)


def find_skill_dirs(area: str | None, skill: str | None) -> list[Path]:
    if skill:
        # Accept both "arbeitsrecht/skills/<name>" and the shorthand
        # "arbeitsrecht/<name>" (with the implicit "skills/" segment).
        candidates = [REPO_ROOT / skill]
        parts = skill.split("/")
        if len(parts) == 2 and parts[1] != "skills":
            candidates.append(REPO_ROOT / parts[0] / "skills" / parts[1])
        for cand in candidates:
            if cand.is_dir() and (cand / "SKILL.md").exists():
                return [cand]
        sys.exit(f"skill directory not found (tried: "
                 f"{', '.join(str(c) for c in candidates)})")
    areas = [area] if area else AREAS
    found: list[Path] = []
    for a in areas:
        skills_dir = REPO_ROOT / a / "skills"
        if not skills_dir.is_dir():
            continue
        for p in sorted(skills_dir.iterdir()):
            if p.is_dir() and (p / "SKILL.md").exists():
                found.append(p)
    return found


def collect_targets(args: argparse.Namespace) -> list[ScanTarget]:
    if args.file:
        fp = Path(args.file)
        if not fp.is_absolute():
            fp = (Path.cwd() / fp).resolve()
        if not fp.is_file():
            sys.exit(f"file not found: {fp}")
        return [ScanTarget(name=str(fp), path=fp)]
    targets: list[ScanTarget] = []
    for skill_dir in find_skill_dirs(args.area, args.skill):
        skill_md = skill_dir / "SKILL.md"
        rel = skill_md.relative_to(REPO_ROOT).as_posix()
        targets.append(ScanTarget(name=rel, path=skill_md))
    return targets


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------
_SEV_LABEL = {Severity.INFO: "info", Severity.WARN: "WARN", Severity.FAIL: "FAIL"}


def print_human(targets: list[ScanTarget], strict: bool, online: bool) -> None:
    total = {Severity.INFO: 0, Severity.WARN: 0, Severity.FAIL: 0}
    for t in targets:
        for f in t.findings:
            total[f.severity] += 1
        if not t.findings:
            continue
        # Per-file header; INFO findings are tallied but not printed (noise).
        notable = [f for f in t.findings if f.severity != Severity.INFO]
        print(f"\n{t.name}  ({len(t.findings)} citations, {len(notable)} to review)")
        for f in notable:
            loc = f"L{f.line}"
            url = f"  -> {f.url}" if f.url else ""
            print(f"    [{_SEV_LABEL[f.severity]}] {loc} {f.kind}: "
                  f"{f.citation} — {f.message}{url}")
    mode = "online" if online else "offline"
    print(
        f"\nSummary ({mode}{', strict' if strict else ''}): "
        f"{len(targets)} file(s), "
        f"{total[Severity.INFO]} ok/info, "
        f"{total[Severity.WARN]} warnings, "
        f"{total[Severity.FAIL]} failures."
    )


def print_json(targets: list[ScanTarget]) -> None:
    out = [
        {
            "source": t.name,
            "findings": [f.to_dict() for f in t.findings],
        }
        for t in targets
    ]
    print(json.dumps(out, indent=2, ensure_ascii=False))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    parser = argparse.ArgumentParser(
        description="Layer-A deterministic citation verifier for "
                    "ai-skills-german-law"
    )
    parser.add_argument("--area", help="Scan one area (e.g. arbeitsrecht)")
    parser.add_argument("--skill", help="Scan one skill path relative to repo root")
    parser.add_argument("--file", help="Scan an arbitrary text file instead of SKILL.md")
    parser.add_argument("--online", action="store_true",
                        help="Resolve German statute URLs over HTTP (polite, deduped)")
    parser.add_argument("--strict", action="store_true",
                        help="Treat warnings (unknown abbr, unmarked case law, "
                             "malformed ECLI/CELEX) as failures (exit 1)")
    parser.add_argument("--json", action="store_true", help="Emit JSON to stdout")
    args = parser.parse_args()

    if args.area and args.skill:
        parser.error("use either --area or --skill, not both")

    targets = collect_targets(args)
    if not targets:
        print("No files found to scan.")
        return 0

    cache: dict[str, int] = {}
    for t in targets:
        try:
            text = t.path.read_text(encoding="utf-8")
        except OSError as exc:
            sys.exit(f"could not read {t.path}: {exc}")
        t.findings = scan_text(text, t.name, args.online, cache)

    if args.json:
        print_json(targets)
    else:
        print_human(targets, args.strict, args.online)

    failures = sum(
        1 for t in targets for f in t.findings if f.counts_as_failure(args.strict)
    )
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
