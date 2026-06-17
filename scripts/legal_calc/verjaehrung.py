#!/usr/bin/env python3
"""Verjaehrungsberechnung nach §§ 195-199, 196, 197 BGB.

Computes when a claim becomes time-barred (verjährt). The most common case is
the Regelverjährung (§ 195: 3 Jahre) with the § 199 Abs. 1 *Ultimo-Regel*: the
period starts at the END of the year (Schluss des Jahres) in which the claim
arose AND the creditor gained (or grossly negligently failed to gain) knowledge.
On top sit the kenntnisunabhängige Höchstfristen of § 199 Abs. 2-4, which run
*taggenau* from the event, not from year-end. The governing date is the earliest
of the applicable periods (§ 199 Abs. 3 S. 2).

Statutory basis:
- § 195 BGB  https://www.gesetze-im-internet.de/bgb/__195.html
- § 199 BGB  https://www.gesetze-im-internet.de/bgb/__199.html
- § 196 BGB  https://www.gesetze-im-internet.de/bgb/__196.html
- § 197 BGB  https://www.gesetze-im-internet.de/bgb/__197.html

Caveats:
- This computes the *Ablauf* of the Frist ignoring Hemmung (§§ 203-209),
  Neubeginn (§ 212) and the Ablaufhemmung (§ 210 f.). Those shift the end and
  are case-specific - feed an adjusted start or handle separately.
- § 193 BGB is NOT applied: the herrschende Meinung holds the Verjährung ends on
  schedule even on a Sa/So/Feiertag (the creditor must act earlier, e.g. via
  Nachtbriefkasten). See `HINWEIS_193`.
- Whether the relevant period is Regel, 10 or 30 years is a legal judgment about
  the type of claim - pass it explicitly. Drafting aid, not legal advice.
"""
from __future__ import annotations

import calendar
import datetime as _dt
from dataclasses import dataclass, field
from typing import List, Optional

REGELFRIST_JAHRE = 3

HINWEIS_193 = (
    "§ 193 BGB ist auf den Ablauf der Verjährung nach h.M. nicht anwendbar: "
    "die Verjährung tritt auch dann mit Ablauf des berechneten Tages ein, wenn "
    "dieser ein Samstag, Sonntag oder Feiertag ist. Verjährungshemmende "
    "Handlungen müssen ggf. früher vorgenommen werden."
)


@dataclass
class VerjaehrungErgebnis:
    art: str
    verjaehrung_mit_ablauf: _dt.date   # claim time-barred AT END of this day
    letzter_handlungstag: _dt.date     # last day to act (== verjaehrung_mit_ablauf)
    schritte: List[str] = field(default_factory=list)

    def __str__(self) -> str:
        lines = [
            f"Verjährungsberechnung ({self.art})",
            f"  Verjährung tritt ein mit Ablauf des {self.verjaehrung_mit_ablauf:%d.%m.%Y}.",
            f"  Letzter Tag für verjährungshemmende Handlung: "
            f"{self.letzter_handlungstag:%d.%m.%Y}.",
            "  Schritte:",
        ]
        lines.extend(f"    - {s}" for s in self.schritte)
        lines.append(f"  Hinweis: {HINWEIS_193}")
        return "\n".join(lines)


def _add_years_taggenau(d: _dt.date, years: int) -> _dt.date:
    """End of an Ereignisfrist of `years` years from event `d` (§ 188 Abs. 2
    Alt. 1 BGB): the day numerically corresponding to `d`, clamped per § 188
    Abs. 3 if it does not exist (29.02. -> 28.02.)."""
    year = d.year + years
    last = calendar.monthrange(year, d.month)[1]
    return _dt.date(year, d.month, min(d.day, last))


def regelverjaehrung(
    entstehung: _dt.date,
    kenntnis: Optional[_dt.date] = None,
    *,
    frist_jahre: int = REGELFRIST_JAHRE,
) -> VerjaehrungErgebnis:
    """Regelverjährung, § 195 i.V.m. § 199 Abs. 1 BGB (Ultimo-Regel).

    Args:
        entstehung: date the claim arose (Anspruch entstanden, § 199 Abs. 1 Nr. 1).
        kenntnis: date the creditor knew / should have known (§ 199 Abs. 1 Nr. 2).
                  Defaults to `entstehung` if not given.
        frist_jahre: period length (default 3; pass another value for special
                     Regelfristen that still use the Ultimo start).
    """
    if kenntnis is None:
        kenntnis = entstehung
    massgeblich = max(entstehung, kenntnis)
    start_jahr = massgeblich.year
    ende = _dt.date(start_jahr + frist_jahre, 12, 31)
    schritte = [
        f"§ 199 Abs. 1 BGB: maßgeblich ist das spätere Ereignis aus Entstehung "
        f"({entstehung:%d.%m.%Y}) und Kenntnis ({kenntnis:%d.%m.%Y}) "
        f"= {massgeblich:%d.%m.%Y}.",
        f"Ultimo-Regel: Frist beginnt mit Schluss des Jahres {start_jahr} "
        f"(31.12.{start_jahr}).",
        f"§ 195 BGB: {frist_jahre} Jahre -> Verjährung mit Ablauf des "
        f"31.12.{start_jahr + frist_jahre}.",
    ]
    return VerjaehrungErgebnis(
        art=f"Regelverjährung {frist_jahre} Jahre (Ultimo)",
        verjaehrung_mit_ablauf=ende,
        letzter_handlungstag=ende,
        schritte=schritte,
    )


def hoechstfrist(
    ereignis: _dt.date,
    jahre: int,
    *,
    bezeichnung: str = "Höchstfrist",
    norm: str = "§ 199 Abs. 3/4 BGB",
) -> VerjaehrungErgebnis:
    """Kenntnisunabhängige Höchstfrist, taggenau ab `ereignis`.

    Use for § 199 Abs. 2 (30 J. ab Verletzung von Leben/Körper/Gesundheit/
    Freiheit), § 199 Abs. 3 Nr. 1 (10 J. ab Entstehung), Abs. 3 Nr. 2 / Abs. 4
    (30 bzw. 10 J. ab Begehung/Entstehung), § 196 (10 J.), § 197 (30 J.).
    """
    ende = _add_years_taggenau(ereignis, jahre)
    schritte = [
        f"{norm}: {jahre} Jahre taggenau ab {ereignis:%d.%m.%Y} "
        f"(kenntnisunabhängig).",
        f"§ 188 Abs. 2 BGB: Ablauf am entsprechenden Tag = {ende:%d.%m.%Y}.",
    ]
    return VerjaehrungErgebnis(
        art=f"{bezeichnung} ({jahre} Jahre, taggenau)",
        verjaehrung_mit_ablauf=ende,
        letzter_handlungstag=ende,
        schritte=schritte,
    )


def schadensersatz_vermoegen(
    entstehung: _dt.date,
    kenntnis: Optional[_dt.date],
    begehung: _dt.date,
) -> VerjaehrungErgebnis:
    """Reiner Vermögensschaden, § 195 i.V.m. § 199 Abs. 1, Abs. 3 BGB.

    Verjährung tritt mit Ablauf der *früher* endenden Frist ein (§ 199 Abs. 3
    S. 2):
    - Regelverjährung (3 J. ab Ultimo des Kenntnisjahres),
    - 10 J. taggenau ab Entstehung (§ 199 Abs. 3 Nr. 1),
    - 30 J. taggenau ab Begehung/Ereignis (§ 199 Abs. 3 Nr. 2).
    """
    regel = regelverjaehrung(entstehung, kenntnis)
    zehn = hoechstfrist(entstehung, 10, bezeichnung="10-Jahres-Frist ab Entstehung",
                        norm="§ 199 Abs. 3 Nr. 1 BGB")
    dreissig = hoechstfrist(begehung, 30, bezeichnung="30-Jahres-Frist ab Begehung",
                            norm="§ 199 Abs. 3 Nr. 2 BGB")
    kandidaten = [regel, zehn, dreissig]
    gewinner = min(kandidaten, key=lambda r: r.verjaehrung_mit_ablauf)
    schritte = [
        "§ 199 Abs. 3 S. 2 BGB: maßgeblich ist die früher endende Frist.",
        f"  - Regelverjährung: {regel.verjaehrung_mit_ablauf:%d.%m.%Y}",
        f"  - § 199 Abs. 3 Nr. 1 (10 J. ab Entstehung): "
        f"{zehn.verjaehrung_mit_ablauf:%d.%m.%Y}",
        f"  - § 199 Abs. 3 Nr. 2 (30 J. ab Begehung): "
        f"{dreissig.verjaehrung_mit_ablauf:%d.%m.%Y}",
        f"  => früheste: {gewinner.verjaehrung_mit_ablauf:%d.%m.%Y} "
        f"({gewinner.art}).",
    ]
    return VerjaehrungErgebnis(
        art="Schadensersatz (Vermögensschaden), früheste Frist",
        verjaehrung_mit_ablauf=gewinner.verjaehrung_mit_ablauf,
        letzter_handlungstag=gewinner.verjaehrung_mit_ablauf,
        schritte=schritte,
    )
