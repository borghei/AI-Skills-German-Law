"""Deterministic legal calculators for ai-skills-german-law.

These modules implement German statutory arithmetic that an LLM cannot perform
reliably: Fristenberechnung (deadline computation), Verjaehrung (limitation
periods), and statutory fee tables (RVG, GKG). They contain NO model calls -
every result is a deterministic function of structured inputs plus a versioned,
dated data table.

Design principles:
- stdlib only (vanilla Python 3.10+), matching the rest of scripts/.
- The legal *judgment* (claim classification, knowledge date, which Land applies)
  is pushed upstream into explicit inputs. The calculator only does the math.
- Every annual/amount table is version-pinned with a `STAND` (as-of) date so a
  result can be reproduced and audited. RVG/GKG amounts and holiday sets drift.
- These are drafting aids, NOT legal advice. Verify against the statute and the
  current fee table before relying on a number in client- or court-facing work.

Public API:
    from scripts.legal_calc import (
        feiertage, fristen, verjaehrung, rvg, gkg,
        kuendigungsfristen, verzugszinsen,
    )
"""
from __future__ import annotations

__all__ = [
    "feiertage",
    "fristen",
    "verjaehrung",
    "rvg",
    "gkg",
    "kuendigungsfristen",
    "verzugszinsen",
]

__version__ = "0.2.0"
