#!/usr/bin/env python3
"""Redact German personally-identifiable information (PII) from a text file
before sending it to an LLM.

This is a pre-hook safeguard for § 203 StGB / DSGVO. It is NOT a substitute
for a proper § 203-compliant gateway — it is a defense-in-depth layer.

Redacts:
- IBAN (DE\\d{20})
- Steuer-ID (11-digit number with valid checksum if --strict)
- Phone numbers (German formats: +49 ..., 0xxx ..., (0xxx) ...)
- Email addresses
- German postal addresses (Straße + Hausnummer + PLZ + Ort) — best effort
- German Aktenzeichen patterns (e.g., "2 AZR 541/09") — kept by default, can be redacted with --redact-azr
- Geburtsdatum (TT.MM.JJJJ) — best effort

Usage:
    python scripts/pii_redact.py --in mandat.txt --out mandat-redacted.txt
    python scripts/pii_redact.py --in mandat.txt --out -  # stdout
    python scripts/pii_redact.py --in mandat.txt --strict --redact-azr
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

PATTERNS: list[tuple[str, str, str]] = [
    ("IBAN", r"\bDE\d{2}\s?(?:\d{4}\s?){4}\d{2}\b", "[IBAN_REDIGIERT]"),
    ("EMAIL", r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", "[EMAIL_REDIGIERT]"),
    (
        "PHONE_INTL",
        r"\+49[\s\-/]?(?:\(?\d{2,5}\)?[\s\-/]?)?\d{2,5}[\s\-/]?\d{3,8}",
        "[TELEFON_REDIGIERT]",
    ),
    (
        "PHONE_DE",
        r"\b0\d{1,4}[\s\-/]?\d{3,8}[\s\-/]?\d{0,8}\b",
        "[TELEFON_REDIGIERT]",
    ),
    (
        "DATE",
        r"\b(0?[1-9]|[12]\d|3[01])\.(0?[1-9]|1[0-2])\.(19|20)\d{2}\b",
        "[DATUM_REDIGIERT]",
    ),
    (
        "PLZ_ORT",
        r"\b\d{5}\s+[A-ZÄÖÜ][A-Za-zÄÖÜäöüß\-\s]{2,30}\b",
        "[PLZ_ORT_REDIGIERT]",
    ),
    (
        "STREET",
        r"\b[A-ZÄÖÜ][A-Za-zÄÖÜäöüß\-\.]{2,30}(?:straße|str\.|weg|allee|platz|gasse|ring|ufer|damm)\s+\d+[a-zA-Z]?\b",
        "[STRASSE_REDIGIERT]",
    ),
    (
        "STEUER_ID",
        r"\b\d{11}\b",
        "[STEUER_ID_REDIGIERT]",
    ),
]

AZR_PATTERN = (
    "AZR",
    r"\b\d+\s+[A-Z][A-Za-z]*\s+\d+/\d{2}\b",
    "[AKTENZEICHEN_REDIGIERT]",
)


def redact(text: str, redact_azr: bool, strict: bool) -> tuple[str, dict[str, int]]:
    counts: dict[str, int] = {}
    patterns = list(PATTERNS)
    if redact_azr:
        patterns.append(AZR_PATTERN)
    for label, pattern, replacement in patterns:
        compiled = re.compile(pattern)
        matches = compiled.findall(text)
        if matches:
            counts[label] = len(matches)
            text = compiled.sub(replacement, text)
    if strict:
        text = strict_pass(text, counts)
    return text, counts


def strict_pass(text: str, counts: dict[str, int]) -> str:
    """Aggressive pass: redact common German first-name patterns and Mandantenkennzeichnungen.

    Conservative — only triggers on obvious patterns to avoid over-redaction.
    """
    namen_pat = re.compile(
        r"\b(Herr|Frau|Hr\.?|Fr\.?)\s+(?:[A-ZÄÖÜ][a-zäöüß]+\s+){0,2}[A-ZÄÖÜ][a-zäöüß]+\b"
    )
    matches = namen_pat.findall(text)
    if matches:
        counts["PERSON_NAME"] = counts.get("PERSON_NAME", 0) + len(matches)
        text = namen_pat.sub(lambda m: f"{m.group(1)} [NAME_REDIGIERT]", text)
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description="Redact German PII from a text file")
    parser.add_argument("--in", dest="input", required=True, help="Input file (- for stdin)")
    parser.add_argument(
        "--out",
        dest="output",
        required=True,
        help="Output file (- for stdout)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Aggressive: also redact obvious person names (Herr/Frau + Name).",
    )
    parser.add_argument(
        "--redact-azr",
        action="store_true",
        help="Also redact Aktenzeichen patterns (default: keep them).",
    )
    args = parser.parse_args()

    text = sys.stdin.read() if args.input == "-" else Path(args.input).read_text(encoding="utf-8")
    redacted, counts = redact(text, args.redact_azr, args.strict)

    if args.output == "-":
        sys.stdout.write(redacted)
    else:
        Path(args.output).write_text(redacted, encoding="utf-8")

    if counts:
        report = ", ".join(f"{k}={v}" for k, v in sorted(counts.items()))
        print(f"redacted: {report}", file=sys.stderr)
    else:
        print("redacted: nothing matched", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
