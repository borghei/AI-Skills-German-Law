#!/usr/bin/env python3
"""German public holidays (gesetzliche Feiertage), stdlib-only.

Needed for Fristenberechnung: under § 193 BGB and § 222 Abs. 2 ZPO a deadline
that falls on a Sonntag, a *staatlich anerkannter allgemeiner Feiertag*, or a
Sonnabend (Samstag) rolls forward to the next Werktag. Which Feiertage count
depends on the Bundesland of the place of performance / the court's seat, so
this module is parameterised by Land.

Easter is computed with the Anonymous Gregorian algorithm (Meeus/Butcher); all
movable feasts derive from it. No third-party dependency.

Coverage and caveats:
- The nine bundeseinheitliche Feiertage are always included.
- Land-specific Feiertage follow the current statutory list, with year-gating
  for those introduced recently (Reformationstag in HB/HH/NI/SH from 2018,
  Weltkindertag in TH from 2019, Internationaler Frauentag in BE from 2019 and
  MV from 2023).
- Community-dependent holidays are deliberately NOT treated as statewide:
  Mariae Himmelfahrt (15.08) in Bayern applies only in katholisch-geprägte
  Gemeinden, and Fronleichnam in SN/TH applies only in some Gemeinden. For a
  hard deadline in those Länder, check the concrete Gemeinde. Use
  `gemeinde_hinweis()` to surface this.
- Augsburger Friedensfest (08.08, only Stadt Augsburg) is out of scope.

This is a drafting aid, not legal advice. Verify the Feiertagsgesetz of the
relevant Land for edge cases.
"""
from __future__ import annotations

import datetime as _dt
from typing import Dict

STAND = "2026-01-01"  # as-of date of the Feiertag rules encoded here

# 16 Bundesländer plus a BUND pseudo-Land (nationwide holidays only).
LAENDER = {
    "BW": "Baden-Württemberg",
    "BY": "Bayern",
    "BE": "Berlin",
    "BB": "Brandenburg",
    "HB": "Bremen",
    "HH": "Hamburg",
    "HE": "Hessen",
    "MV": "Mecklenburg-Vorpommern",
    "NI": "Niedersachsen",
    "NW": "Nordrhein-Westfalen",
    "RP": "Rheinland-Pfalz",
    "SL": "Saarland",
    "SN": "Sachsen",
    "ST": "Sachsen-Anhalt",
    "SH": "Schleswig-Holstein",
    "TH": "Thüringen",
    "BUND": "Bund (nur bundeseinheitliche Feiertage)",
}


def ostersonntag(year: int) -> _dt.date:
    """Easter Sunday (Gregorian) via the Anonymous Gregorian algorithm."""
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    el = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * el) // 451
    month = (h + el - 7 * m + 114) // 31
    day = ((h + el - 7 * m + 114) % 31) + 1
    return _dt.date(year, month, day)


def _buss_und_bettag(year: int) -> _dt.date:
    """Wednesday before 23 November (Buß- und Bettag, only Sachsen)."""
    nov23 = _dt.date(year, 11, 23)
    # The Mittwoch (weekday 2) on or before 22 Nov; always the Wed before 23rd.
    offset = (nov23.weekday() - 2) % 7
    if offset == 0:
        offset = 7
    return nov23 - _dt.timedelta(days=offset)


def feiertage(year: int, land: str = "BUND") -> Dict[_dt.date, str]:
    """Return {date: name} of gesetzliche Feiertage in `land` for `year`.

    `land` is a two-letter code from LAENDER (case-insensitive), or "BUND" for
    the nationwide set only.
    """
    land = land.upper()
    if land not in LAENDER:
        raise ValueError(f"unbekanntes Bundesland: {land!r} (erlaubt: {', '.join(LAENDER)})")

    ostern = ostersonntag(year)
    days: Dict[_dt.date, str] = {}

    def add(d: _dt.date, name: str) -> None:
        # If two Feiertage fall on the same date (e.g. Christi Himmelfahrt on
        # 01.05. in 2008), keep both names rather than silently dropping one.
        if d in days:
            if name not in days[d]:
                days[d] = f"{days[d]} / {name}"
        else:
            days[d] = name

    # --- bundeseinheitliche Feiertage (alle Länder) ---
    add(_dt.date(year, 1, 1), "Neujahr")
    add(ostern - _dt.timedelta(days=2), "Karfreitag")
    add(ostern + _dt.timedelta(days=1), "Ostermontag")
    add(_dt.date(year, 5, 1), "Tag der Arbeit")
    add(ostern + _dt.timedelta(days=39), "Christi Himmelfahrt")
    add(ostern + _dt.timedelta(days=50), "Pfingstmontag")
    add(_dt.date(year, 10, 3), "Tag der Deutschen Einheit")
    add(_dt.date(year, 12, 25), "1. Weihnachtstag")
    add(_dt.date(year, 12, 26), "2. Weihnachtstag")
    # Reformationstag 2017 war zum 500. Reformationsjubiläum einmalig in allen
    # 16 Ländern gesetzlicher Feiertag (sonst nur in einzelnen Ländern, s.u.).
    if year == 2017:
        add(_dt.date(2017, 10, 31), "Reformationstag (einmalig bundesweit 2017)")

    if land == "BUND":
        return days

    fronleichnam = ostern + _dt.timedelta(days=60)
    heilige_drei = _dt.date(year, 1, 6)
    allerheiligen = _dt.date(year, 11, 1)
    reformationstag = _dt.date(year, 10, 31)
    maria_himmelfahrt = _dt.date(year, 8, 15)
    frauentag = _dt.date(year, 3, 8)
    weltkindertag = _dt.date(year, 9, 20)

    # --- länderspezifische Feiertage ---
    if land in {"BW", "BY", "ST"}:
        add(heilige_drei, "Heilige Drei Könige")
    if land in {"BW", "BY", "HE", "NW", "RP", "SL"}:
        add(fronleichnam, "Fronleichnam")
    if land == "SL":
        add(maria_himmelfahrt, "Mariä Himmelfahrt")
    if land in {"BW", "BY", "NW", "RP", "SL"}:
        add(allerheiligen, "Allerheiligen")
    if land == "SN":
        add(_buss_und_bettag(year), "Buß- und Bettag")

    # Brandenburg counts Oster- und Pfingstsonntag as Feiertage (both Sundays).
    if land == "BB":
        add(ostern, "Ostersonntag")
        add(ostern + _dt.timedelta(days=49), "Pfingstsonntag")

    # Reformationstag: traditional in the östliche Länder; HB/HH/NI/SH from 2018.
    if land in {"BB", "MV", "SN", "ST", "TH"}:
        add(reformationstag, "Reformationstag")
    if land in {"HB", "HH", "NI", "SH"} and year >= 2018:
        add(reformationstag, "Reformationstag")

    # Internationaler Frauentag: Berlin from 2019, MV from 2023.
    if land == "BE" and year >= 2019:
        add(frauentag, "Internationaler Frauentag")
    if land == "MV" and year >= 2023:
        add(frauentag, "Internationaler Frauentag")

    # Weltkindertag: Thüringen from 2019.
    if land == "TH" and year >= 2019:
        add(weltkindertag, "Weltkindertag")

    return days


def ist_feiertag(d: _dt.date, land: str = "BUND") -> bool:
    """True if `d` is a gesetzlicher Feiertag in `land`."""
    return d in feiertage(d.year, land)


def gemeinde_hinweis(land: str) -> str | None:
    """Return a warning if `land` has community-dependent holidays not modelled.

    Bayern: Mariä Himmelfahrt (15.08) is a Feiertag only in katholisch-geprägte
    Gemeinden. Sachsen/Thüringen: Fronleichnam only in einzelnen Gemeinden.
    Such days are NOT counted as statewide here, so a deadline near them must be
    checked against the concrete Gemeinde.
    """
    land = land.upper()
    if land == "BY":
        return ("Bayern: Mariä Himmelfahrt (15.08.) ist nur in katholisch "
                "geprägten Gemeinden Feiertag und wird hier NICHT landesweit "
                "gezählt. Bei Fristen um den 15.08. die konkrete Gemeinde prüfen.")
    if land in {"SN", "TH"}:
        return (f"{LAENDER[land]}: Fronleichnam ist nur in einzelnen Gemeinden "
                "Feiertag und wird hier nicht gezählt. Bei Fristen um Fronleichnam "
                "die konkrete Gemeinde prüfen.")
    return None


def gemeinde_konflikt(land: str, start: _dt.date, ende: _dt.date) -> str | None:
    """Return `gemeinde_hinweis(land)` only if a community-dependent Feiertag
    actually falls within [start, ende] (inclusive).

    Avoids surfacing the BY/SN/TH warning for Fristen that are nowhere near the
    relevant date. Checks Mariä Himmelfahrt (15.08., Bayern) and Fronleichnam
    (Ostern + 60, Sachsen/Thüringen) across every year the period spans.
    """
    land = land.upper()
    if land not in {"BY", "SN", "TH"}:
        return None
    for year in range(start.year, ende.year + 1):
        if land == "BY":
            d = _dt.date(year, 8, 15)
        else:
            d = ostersonntag(year) + _dt.timedelta(days=60)
        if start <= d <= ende:
            return gemeinde_hinweis(land)
    return None
