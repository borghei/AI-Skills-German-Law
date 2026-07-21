#!/usr/bin/env python3
"""Verzugszinsen nach §§ 288, 247 BGB.

Computes default interest on a money claim: the applicable rate (5 or 9
percentage points above the Basiszinssatz), the day count, the interest amount,
and the § 288 Abs. 5 BGB flat fee of EUR 40 where applicable.

Statutory basis:
- § 288 BGB   https://www.gesetze-im-internet.de/bgb/__288.html
- § 247 BGB   https://www.gesetze-im-internet.de/bgb/__247.html (Basiszinssatz)
- § 286 BGB   https://www.gesetze-im-internet.de/bgb/__286.html (Verzugseintritt)

DESIGN DECISION - the Basiszinssatz is a REQUIRED INPUT, never hardcoded.
Under § 247 Abs. 1 BGB it changes on 1 January and 1 July of each year and is
published by the Deutsche Bundesbank. Baking a value into this module would
silently produce wrong numbers after the next reset. The caller must supply the
rate in force for the period, and where a period spans a reset the calculation
must be split into segments (see `berechne_segmente`).

Caveats:
- Verzugseintritt (§ 286 BGB) is a legal question and an INPUT here. Mahnung,
  Fälligkeit, § 286 Abs. 2 exceptions and the § 286 Abs. 3 30-day rule are not
  computed.
- Rate choice: § 288 Abs. 2 BGB (9 points) requires BOTH an Entgeltforderung AND
  no consumer being party to the transaction. Consumer involvement on either side
  drops it back to Abs. 1 (5 points).
- § 288 Abs. 5 BGB: the EUR 40 flat fee is owed where the debtor is not a
  consumer; it is set off against costs of legal pursuit (Abs. 5 S. 3).
- Day count follows actual/365 (actual/366 in a leap year segment), the practice
  for statutory interest. Pass `tageszaehlung="30E/360"` only if a contract says so.
- Drafting aid, not legal advice.
"""
from __future__ import annotations

import datetime as _dt
from dataclasses import dataclass, field
from decimal import Decimal, ROUND_HALF_UP
from typing import List, Optional, Sequence, Tuple

STAND = "2026-07-21"

PAUSCHALE_288_V = Decimal("40.00")


def _q(x: Decimal) -> Decimal:
    return x.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


@dataclass
class ZinsSegment:
    von: _dt.date
    bis: _dt.date
    tage: int
    basiszinssatz: Decimal
    zinssatz: Decimal
    tagesbasis: int
    betrag: Decimal


@dataclass
class VerzugszinsErgebnis:
    hauptforderung: Decimal
    verzugsbeginn: _dt.date
    stichtag: _dt.date
    zuschlag_punkte: Decimal
    grundlage: str
    segmente: List[ZinsSegment] = field(default_factory=list)
    zinsen: Decimal = Decimal("0.00")
    pauschale: Decimal = Decimal("0.00")
    gesamt: Decimal = Decimal("0.00")
    hinweise: List[str] = field(default_factory=list)
    stand: str = STAND

    def erklaerung(self) -> str:
        lines = [
            f"Hauptforderung:   {self.hauptforderung:,.2f} EUR",
            f"Verzug ab:        {self.verzugsbeginn:%d.%m.%Y}",
            f"Berechnet bis:    {self.stichtag:%d.%m.%Y}",
            f"Grundlage:        {self.grundlage}",
            f"Zuschlag:         {self.zuschlag_punkte} Prozentpunkte über Basiszinssatz",
            "",
            "Zinssegmente:",
        ]
        for s in self.segmente:
            lines.append(
                f"  {s.von:%d.%m.%Y} - {s.bis:%d.%m.%Y}  "
                f"{s.tage:>4} Tage  Basis {s.basiszinssatz}%  "
                f"Satz {s.zinssatz}%  ->  {s.betrag:,.2f} EUR"
            )
        lines += [
            "",
            f"Zinsen gesamt:    {self.zinsen:,.2f} EUR",
        ]
        if self.pauschale:
            lines.append(f"Pauschale § 288 V: {self.pauschale:,.2f} EUR")
        lines.append(f"Summe:            {self.gesamt:,.2f} EUR")
        if self.hinweise:
            lines += ["", "Hinweise:"] + [f"  ! {h}" for h in self.hinweise]
        lines.append(f"(Stand der Berechnungsgrundlage: {self.stand})")
        return "\n".join(lines)


def _tagesbasis(jahr: int, modus: str) -> int:
    if modus == "30E/360":
        return 360
    return 366 if _ist_schaltjahr(jahr) else 365


def _ist_schaltjahr(j: int) -> bool:
    return j % 4 == 0 and (j % 100 != 0 or j % 400 == 0)


def berechne(
    hauptforderung: Decimal | float | str,
    verzugsbeginn: _dt.date,
    stichtag: _dt.date,
    basiszinssatz: Decimal | float | str,
    entgeltforderung: bool = False,
    verbraucher_beteiligt: bool = True,
    schuldner_ist_verbraucher: bool = True,
    tageszaehlung: str = "actual/365",
) -> VerzugszinsErgebnis:
    """Single-rate computation. Use `berechne_segmente` if the Basiszinssatz changed."""
    return berechne_segmente(
        hauptforderung=hauptforderung,
        verzugsbeginn=verzugsbeginn,
        stichtag=stichtag,
        basiszinssaetze=[(verzugsbeginn, Decimal(str(basiszinssatz)))],
        entgeltforderung=entgeltforderung,
        verbraucher_beteiligt=verbraucher_beteiligt,
        schuldner_ist_verbraucher=schuldner_ist_verbraucher,
        tageszaehlung=tageszaehlung,
    )


def berechne_segmente(
    hauptforderung: Decimal | float | str,
    verzugsbeginn: _dt.date,
    stichtag: _dt.date,
    basiszinssaetze: Sequence[Tuple[_dt.date, Decimal]],
    entgeltforderung: bool = False,
    verbraucher_beteiligt: bool = True,
    schuldner_ist_verbraucher: bool = True,
    tageszaehlung: str = "actual/365",
) -> VerzugszinsErgebnis:
    """Compute default interest across one or more Basiszinssatz periods.

    `basiszinssaetze` is a sequence of (gültig_ab, satz) pairs, e.g.
        [(date(2025, 7, 1), Decimal("1.27")), (date(2026, 1, 1), Decimal("1.10"))]
    Each rate applies from its date until the next one starts. The § 247 BGB rate
    resets on 1 January and 1 July; the caller must supply the actual published
    values - this module does not know them.
    """
    haupt = Decimal(str(hauptforderung))
    if haupt <= 0:
        raise ValueError("Hauptforderung muss positiv sein")
    if stichtag < verzugsbeginn:
        raise ValueError("Stichtag liegt vor dem Verzugsbeginn")
    if not basiszinssaetze:
        raise ValueError("mindestens ein Basiszinssatz erforderlich")

    hinweise: List[str] = []

    if entgeltforderung and not verbraucher_beteiligt:
        punkte = Decimal("9")
        grundlage = "§ 288 Abs. 2 BGB (Entgeltforderung, kein Verbraucher beteiligt)"
    else:
        punkte = Decimal("5")
        grundlage = "§ 288 Abs. 1 BGB (Grundsatz)"
        if entgeltforderung and verbraucher_beteiligt:
            hinweise.append(
                "Entgeltforderung, aber Verbraucherbeteiligung: der erhöhte Satz "
                "von 9 Prozentpunkten nach § 288 Abs. 2 BGB greift NICHT."
            )

    saetze = sorted(basiszinssaetze, key=lambda t: t[0])
    segmente: List[ZinsSegment] = []
    summe = Decimal("0.00")

    # § 187 Abs. 1 BGB: der Tag des Verzugseintritts zaehlt nicht mit;
    # Zinslauf beginnt am Folgetag, der Stichtag zaehlt mit.
    lauf_von = verzugsbeginn
    grenzen: List[_dt.date] = []
    for ab, _ in saetze:
        if verzugsbeginn < ab <= stichtag:
            grenzen.append(ab)
    punkte_liste = [lauf_von] + grenzen + [stichtag]

    for i in range(len(punkte_liste) - 1):
        seg_von = punkte_liste[i]
        seg_bis = punkte_liste[i + 1]
        tage = (seg_bis - seg_von).days
        if tage <= 0:
            continue
        basis = _aktueller_satz(saetze, seg_von)
        satz = basis + punkte
        tb = _tagesbasis(seg_von.year, tageszaehlung)
        betrag = haupt * satz / Decimal("100") * Decimal(tage) / Decimal(tb)
        betrag = _q(betrag)
        segmente.append(
            ZinsSegment(
                von=seg_von, bis=seg_bis, tage=tage,
                basiszinssatz=basis, zinssatz=satz, tagesbasis=tb, betrag=betrag,
            )
        )
        summe += betrag

    pauschale = Decimal("0.00")
    if entgeltforderung and not schuldner_ist_verbraucher:
        pauschale = PAUSCHALE_288_V
        hinweise.append(
            "Pauschale nach § 288 Abs. 5 BGB angesetzt (40 EUR). Sie ist nach "
            "§ 288 Abs. 5 S. 3 BGB auf einen geschuldeten Ersatz von "
            "Rechtsverfolgungskosten anzurechnen."
        )

    hinweise.append(
        "Verzugseintritt (§ 286 BGB) ist Rechtsfrage und Eingabe - Mahnung, "
        "Fälligkeit, Ausnahmen des § 286 Abs. 2 und die 30-Tage-Regel des "
        "§ 286 Abs. 3 BGB werden hier nicht geprüft."
    )
    hinweise.append(
        "Der Basiszinssatz nach § 247 BGB ändert sich zum 1.1. und 1.7. jedes "
        "Jahres. Die verwendeten Werte sind Eingaben und gegen die "
        "Bundesbank-Veröffentlichung zu prüfen."
    )

    return VerzugszinsErgebnis(
        hauptforderung=_q(haupt),
        verzugsbeginn=verzugsbeginn,
        stichtag=stichtag,
        zuschlag_punkte=punkte,
        grundlage=grundlage,
        segmente=segmente,
        zinsen=_q(summe),
        pauschale=pauschale,
        gesamt=_q(summe + pauschale),
        hinweise=hinweise,
    )


def _aktueller_satz(
    saetze: Sequence[Tuple[_dt.date, Decimal]], tag: _dt.date
) -> Decimal:
    gewaehlt: Optional[Decimal] = None
    for ab, satz in saetze:
        if ab <= tag:
            gewaehlt = Decimal(str(satz))
    if gewaehlt is None:
        gewaehlt = Decimal(str(saetze[0][1]))
    return gewaehlt
