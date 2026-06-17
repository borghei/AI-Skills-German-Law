#!/usr/bin/env python3
"""RVG-Gebührenberechnung (Rechtsanwaltsvergütung), § 13 RVG + Anlage 2.

Computes lawyer's fees (Wertgebühren) from the Gegenstandswert. The Gebühren-
tabelle (1,0-Gebühr per Wertstufe) is a versioned lookup loaded from
`data/rvg_tabelle.json`; the lookup is "round UP to the next Wertstufe"
(§ 13 Abs. 1: "für jeden angefangenen Betrag"). Above 500.000 EUR a fixed
increment per angefangene 50.000 EUR applies (§ 13 Abs. 1 S. 3).

A fee item is the 1,0-Gebühr times a Gebührensatz (Faktor) from the VV RVG, e.g.
Verfahrensgebühr VV 3100 = 1,3, Terminsgebühr VV 3104 = 1,2, Geschäftsgebühr
VV 2300 = 1,3 (Regelfall), Einigungsgebühr VV 1000 = 1,5. On top come the
Post-/Telekommunikationspauschale VV 7002 (20 % der Gebühren, höchstens 20 EUR)
and 19 % Umsatzsteuer VV 7008.

Statutory basis:
- § 13 RVG  https://www.gesetze-im-internet.de/rvg/__13.html
- Anlage 2  https://www.gesetze-im-internet.de/rvg/anlage_2.html
- VV RVG    https://www.gesetze-im-internet.de/rvg/anlage_1.html

CAVEAT - Versionsdrift: the amounts changed with KostRÄG 2021 and again with
KostBRÄG 2025. The shipped table carries a STAND (as-of) date - always check it
against the current Anlage 2 before relying on a figure. Drafting aid, not legal
advice.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Tuple

_DATA = Path(__file__).resolve().parent / "data" / "rvg_tabelle.json"

# Gängige Gebührensätze aus dem VV RVG (zur Bequemlichkeit; Werte prüfen).
GEBUEHRENSAETZE: Dict[str, float] = {
    "VV3100_verfahrensgebuehr": 1.3,
    "VV3104_terminsgebuehr": 1.2,
    "VV2300_geschaeftsgebuehr_regel": 1.3,
    "VV1000_einigungsgebuehr": 1.5,
    "VV1003_einigungsgebuehr_anhaengig": 1.0,
}


@dataclass
class Gebuehrenposition:
    bezeichnung: str
    faktor: float
    betrag: float


@dataclass
class RVGErgebnis:
    gegenstandswert: float
    einfachgebuehr: float
    stand: str
    positionen: List[Gebuehrenposition] = field(default_factory=list)
    zwischensumme_gebuehren: float = 0.0
    auslagenpauschale: float = 0.0
    netto: float = 0.0
    ust_satz: float = 0.19
    ust: float = 0.0
    brutto: float = 0.0

    def __str__(self) -> str:
        lines = [
            f"RVG-Berechnung (Gegenstandswert {self.gegenstandswert:,.2f} EUR, "
            f"Tabelle Stand {self.stand})",
            f"  1,0-Gebühr: {self.einfachgebuehr:,.2f} EUR",
        ]
        for p in self.positionen:
            lines.append(f"  {p.bezeichnung} ({p.faktor:g}): {p.betrag:,.2f} EUR")
        lines += [
            f"  Zwischensumme Gebühren: {self.zwischensumme_gebuehren:,.2f} EUR",
            f"  Auslagenpauschale VV 7002: {self.auslagenpauschale:,.2f} EUR",
            f"  Netto: {self.netto:,.2f} EUR",
            f"  USt VV 7008 ({self.ust_satz:.0%}): {self.ust:,.2f} EUR",
            f"  Gesamt (brutto): {self.brutto:,.2f} EUR",
        ]
        return "\n".join(lines)


def _lade_tabelle() -> dict:
    with _DATA.open(encoding="utf-8") as fh:
        return json.load(fh)


def einfachgebuehr(gegenstandswert: float, tabelle: dict | None = None) -> Tuple[float, str]:
    """Return (1,0-Gebühr, STAND) for `gegenstandswert` per Anlage 2 zu § 13 RVG.

    Rounds UP to the next Wertstufe. Above the highest tabulated Stufe, applies
    the fixed Zuschlag per angefangene 50.000 EUR (§ 13 Abs. 1 S. 3).
    """
    if gegenstandswert <= 0:
        raise ValueError("Gegenstandswert muss > 0 sein")
    tab = tabelle or _lade_tabelle()
    stufen: List[List[float]] = tab["stufen"]  # [[bis_wert, gebuehr], ...] aufsteigend
    stand: str = tab["stand"]

    for bis_wert, gebuehr in stufen:
        if gegenstandswert <= bis_wert:
            return float(gebuehr), stand

    # über der höchsten Stufe: § 13 Abs. 1 S. 3 RVG
    hoechststufe_wert, hoechststufe_gebuehr = stufen[-1]
    schritt = tab["ueber_hoechstwert"]["schritt"]        # z.B. 50000
    zuschlag = tab["ueber_hoechstwert"]["zuschlag"]      # EUR je angefangenem Schritt
    rest = gegenstandswert - hoechststufe_wert
    schritte = -(-rest // schritt)  # ceil division (angefangene Schritte)
    return float(hoechststufe_gebuehr) + schritte * zuschlag, stand


def berechne(
    gegenstandswert: float,
    faktoren: List[Tuple[str, float]],
    *,
    auslagenpauschale: bool = True,
    ust_satz: float = 0.19,
) -> RVGErgebnis:
    """Compute total fees.

    Args:
        gegenstandswert: Wert in EUR.
        faktoren: list of (Bezeichnung, Gebührensatz), z.B.
                  [("Verfahrensgebühr VV 3100", 1.3),
                   ("Terminsgebühr VV 3104", 1.2)].
        auslagenpauschale: add VV 7002 (20 % der Gebühren, max 20 EUR).
        ust_satz: USt-Satz (default 0.19); auf 0 setzen, falls nicht steuerbar.
    """
    eg, stand = einfachgebuehr(gegenstandswert)
    positionen = []
    summe = 0.0
    for bez, faktor in faktoren:
        betrag = round(eg * faktor, 2)
        positionen.append(Gebuehrenposition(bez, faktor, betrag))
        summe += betrag
    summe = round(summe, 2)

    pauschale = round(min(summe * 0.20, 20.0), 2) if auslagenpauschale else 0.0
    netto = round(summe + pauschale, 2)
    ust = round(netto * ust_satz, 2)
    brutto = round(netto + ust, 2)

    return RVGErgebnis(
        gegenstandswert=gegenstandswert,
        einfachgebuehr=eg,
        stand=stand,
        positionen=positionen,
        zwischensumme_gebuehren=summe,
        auslagenpauschale=pauschale,
        netto=netto,
        ust_satz=ust_satz,
        ust=ust,
        brutto=brutto,
    )
