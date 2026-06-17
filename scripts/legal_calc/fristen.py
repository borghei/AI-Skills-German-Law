#!/usr/bin/env python3
"""Fristenberechnung nach §§ 187-193 BGB und § 222 ZPO.

Computes the end of a legal deadline (Frist) from a starting event, the period
length, and whether it is an Ereignisfrist (§ 187 Abs. 1 BGB - the event day is
NOT counted) or a Beginnfrist (§ 187 Abs. 2 BGB - the day counts, used e.g. for
Lebensalter). Applies the § 193 BGB / § 222 Abs. 2 ZPO rollover: if the last day
is a Samstag, Sonntag or gesetzlicher Feiertag, the deadline moves to the next
Werktag.

The result is a step-by-step object so the reasoning is auditable - legal work
needs to show *why* a date came out, not just the date.

Statutory basis:
- § 187 BGB  https://www.gesetze-im-internet.de/bgb/__187.html
- § 188 BGB  https://www.gesetze-im-internet.de/bgb/__188.html
- § 193 BGB  https://www.gesetze-im-internet.de/bgb/__193.html
- § 222 ZPO  https://www.gesetze-im-internet.de/zpo/__222.html

Caveats:
- The § 193 rollover applies to a Frist for a Leistung / Erklärung or a
  prozessuale Handlung (§ 222 ZPO). It does NOT extend, e.g., the start of an
  interest period. Pass rollover=False where it must not apply.
- The relevant Feiertage are those at the Leistungs-/Erklärungsort, for court
  deadlines the seat of the court. Set `land` accordingly.
- Drafting aid, not legal advice. Verify the governing Fristvorschrift.
"""
from __future__ import annotations

import calendar
import datetime as _dt
from dataclasses import dataclass, field
from typing import List

from . import feiertage as _ft

UNITS = ("tage", "wochen", "monate", "jahre")


@dataclass
class FristErgebnis:
    start_ereignis: _dt.date
    menge: int
    einheit: str
    art: str  # "ereignis" | "beginn"
    land: str
    fristbeginn: _dt.date          # § 187: first day counted / reference
    fristende_roh: _dt.date        # before § 193 rollover
    fristende: _dt.date            # after § 193 rollover (the answer)
    verschoben: bool               # whether § 193 moved the date
    schritte: List[str] = field(default_factory=list)

    def __str__(self) -> str:
        lines = [
            f"Fristberechnung ({self.art}frist, {self.menge} {self.einheit}, Land {self.land})",
            f"  Ereignis:    {self.start_ereignis:%d.%m.%Y} ({_wochentag(self.start_ereignis)})",
            f"  Fristbeginn: {self.fristbeginn:%d.%m.%Y}",
            f"  Fristende:   {self.fristende:%d.%m.%Y} ({_wochentag(self.fristende)})",
        ]
        if self.verschoben:
            lines.append(
                f"  (§ 193 BGB: roher Ablauf {self.fristende_roh:%d.%m.%Y} "
                f"war Sa/So/Feiertag -> verschoben auf nächsten Werktag)"
            )
        lines.append("  Schritte:")
        lines.extend(f"    - {s}" for s in self.schritte)
        return "\n".join(lines)


_WOCHENTAGE = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]


def _wochentag(d: _dt.date) -> str:
    return _WOCHENTAGE[d.weekday()]


def _add_months(d: _dt.date, months: int) -> _dt.date:
    """Add `months`; if the day does not exist in the target month, clamp to the
    last day of that month (§ 188 Abs. 3 BGB)."""
    total = (d.year * 12 + (d.month - 1)) + months
    year, month = divmod(total, 12)
    month += 1
    last = calendar.monthrange(year, month)[1]
    return _dt.date(year, month, min(d.day, last))


def _ist_werktag(d: _dt.date, land: str) -> bool:
    return d.weekday() < 5 and not _ft.ist_feiertag(d, land)


def naechster_werktag(d: _dt.date, land: str = "BUND") -> _dt.date:
    """Next Werktag on or after `d` (Sa/So/Feiertag are skipped)."""
    while not _ist_werktag(d, land):
        d += _dt.timedelta(days=1)
    return d


def berechne_frist(
    ereignis: _dt.date,
    menge: int,
    einheit: str,
    *,
    art: str = "ereignis",
    land: str = "BUND",
    rollover: bool = True,
) -> FristErgebnis:
    """Compute the end of a Frist.

    Args:
        ereignis: the event date that triggers the Frist (z.B. Zustellung).
        menge: number of units (must be >= 1).
        einheit: one of "tage", "wochen", "monate", "jahre".
        art: "ereignis" (§ 187 Abs. 1, Ereignistag zählt nicht) or
             "beginn" (§ 187 Abs. 2, Tag zählt mit, z.B. Lebensalter).
        land: Bundesland code for the § 193 Feiertag check (see feiertage.LAENDER).
        rollover: apply § 193 BGB / § 222 Abs. 2 ZPO rollover (default True).
    """
    einheit = einheit.lower()
    if einheit not in UNITS:
        raise ValueError(f"einheit muss eine von {UNITS} sein, nicht {einheit!r}")
    if art not in ("ereignis", "beginn"):
        raise ValueError("art muss 'ereignis' oder 'beginn' sein")
    if menge < 1:
        raise ValueError("menge muss >= 1 sein")

    schritte: List[str] = []

    if art == "ereignis":
        fristbeginn = ereignis + _dt.timedelta(days=1)
        schritte.append(
            f"§ 187 Abs. 1 BGB: Ereignistag ({ereignis:%d.%m.%Y}) zählt nicht; "
            f"Frist beginnt am {fristbeginn:%d.%m.%Y}."
        )
    else:
        fristbeginn = ereignis
        schritte.append(
            f"§ 187 Abs. 2 BGB: Anfangstag ({ereignis:%d.%m.%Y}) zählt mit."
        )

    if einheit == "tage":
        if art == "ereignis":
            ende = ereignis + _dt.timedelta(days=menge)
            schritte.append(
                f"§ 188 Abs. 1 BGB: {menge} Tage ab Fristbeginn enden mit Ablauf "
                f"des {ende:%d.%m.%Y}."
            )
        else:
            ende = ereignis + _dt.timedelta(days=menge - 1)
            schritte.append(
                f"§ 188 Abs. 1 BGB: {menge} Tage (Anfangstag mitgezählt) enden "
                f"mit Ablauf des {ende:%d.%m.%Y}."
            )
    elif einheit == "wochen":
        # § 188 Abs. 2 BGB: entsprechender Wochentag (Überlauf gibt es nicht).
        korr = ereignis + _dt.timedelta(weeks=menge)
        if art == "ereignis":
            ende = korr
            schritte.append(
                f"§ 188 Abs. 2 Alt. 1 BGB: Frist endet am entsprechenden Wochentag "
                f"({_wochentag(ende)}): {ende:%d.%m.%Y}."
            )
        else:
            ende = korr - _dt.timedelta(days=1)
            schritte.append(
                f"§ 188 Abs. 2 Alt. 2 BGB: Frist endet mit Ablauf des dem "
                f"entsprechenden Tag vorhergehenden Tages: {ende:%d.%m.%Y}."
            )
    else:
        # monate / jahre: § 188 Abs. 2 BGB - der nach Zahl entsprechende Tag,
        # mit § 188 Abs. 3 BGB, wenn dieser Tag im Zielmonat fehlt.
        months = menge if einheit == "monate" else menge * 12
        total = ereignis.year * 12 + (ereignis.month - 1) + months
        ty, tm = divmod(total, 12)
        tm += 1
        last = calendar.monthrange(ty, tm)[1]
        overflow = ereignis.day > last  # entsprechender Tag existiert nicht
        if art == "ereignis":
            ende = _dt.date(ty, tm, last if overflow else ereignis.day)
            schritte.append(
                f"§ 188 Abs. 2 Alt. 1 BGB: Frist endet am entsprechenden Tag: "
                f"{ende:%d.%m.%Y}."
            )
            if overflow:
                schritte.append(
                    "§ 188 Abs. 3 BGB: entsprechender Tag fehlt im Zielmonat "
                    "-> letzter Tag des Monats."
                )
        else:
            if overflow:
                # Der dem (fehlenden) entsprechenden Tag vorhergehende Tag ist
                # der letzte existierende Tag des Zielmonats.
                ende = _dt.date(ty, tm, last)
                schritte.append(
                    "§ 188 Abs. 2 Alt. 2 i.V.m. Abs. 3 BGB: entsprechender Tag "
                    f"fehlt im Zielmonat -> Ablauf mit dem letzten Tag des Monats "
                    f"{ende:%d.%m.%Y}."
                )
            else:
                ende = _dt.date(ty, tm, ereignis.day) - _dt.timedelta(days=1)
                schritte.append(
                    f"§ 188 Abs. 2 Alt. 2 BGB: Frist endet mit Ablauf des dem "
                    f"entsprechenden Tag vorhergehenden Tages: {ende:%d.%m.%Y}."
                )

    ende_roh = ende
    verschoben = False
    if rollover and not _ist_werktag(ende, land):
        neu = naechster_werktag(ende, land)
        grund = "Samstag" if ende.weekday() == 5 else (
            "Sonntag" if ende.weekday() == 6 else
            f"Feiertag ({_ft.feiertage(ende.year, land).get(ende, 'Feiertag')})"
        )
        schritte.append(
            f"§ 193 BGB / § 222 Abs. 2 ZPO: Ablauf am {ende:%d.%m.%Y} ({grund}) "
            f"-> verschoben auf nächsten Werktag {neu:%d.%m.%Y}."
        )
        ende = neu
        verschoben = True

    return FristErgebnis(
        start_ereignis=ereignis,
        menge=menge,
        einheit=einheit,
        art=art,
        land=land.upper(),
        fristbeginn=fristbeginn,
        fristende_roh=ende_roh,
        fristende=ende,
        verschoben=verschoben,
        schritte=schritte,
    )
