#!/usr/bin/env python3
"""GKG-Gerichtskostenberechnung, § 34 GKG + Anlage 2.

Computes court costs (Gerichtsgebühren) from the Streitwert. Structure mirrors
the RVG: a versioned 1,0-Gebühr table (loaded from `data/gkg_tabelle.json`),
"round UP to the next Wertstufe", and a fixed Zuschlag per angefangene 50.000 EUR
above the highest Stufe (§ 34 Abs. 1 S. 3 GKG). The court fee is the 1,0-Gebühr
times the Gebührensatz from the Kostenverzeichnis (KV GKG), e.g. for the
bürgerliche Rechtsstreitigkeit erster Instanz 3,0 (KV 1210), Berufung 4,0
(KV 1220), Revision 5,0 (KV 1230). Gerichtsgebühren are NOT umsatzsteuerpflichtig.

Statutory basis:
- § 34 GKG  https://www.gesetze-im-internet.de/gkg_2004/__34.html
- Anlage 2  https://www.gesetze-im-internet.de/gkg_2004/anlage_2.html
- KV GKG    https://www.gesetze-im-internet.de/gkg_2004/anlage_1.html

CAVEAT - Versionsdrift and Ermäßigung: the amounts change by Gesetz (check the
STAND). The 3,0-Verfahrensgebühr erster Instanz ermäßigt sich auf 1,0 bei früher
Verfahrensbeendigung (KV 1211, z.B. Klagerücknahme, Anerkenntnis-/Versäumnis-
urteil, Vergleich). This module computes the full Satz; pass the reduced Satz
explicitly where KV 1211 greift. Drafting aid, not legal advice.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple

_DATA = Path(__file__).resolve().parent / "data" / "gkg_tabelle.json"

# Gängige Gebührensätze aus dem KV GKG (Werte prüfen).
GEBUEHRENSAETZE = {
    "KV1210_zivil_erste_instanz": 3.0,
    "KV1211_ermaessigt": 1.0,
    "KV1220_berufung": 4.0,
    "KV1230_revision": 5.0,
}


@dataclass
class GKGErgebnis:
    streitwert: float
    einfachgebuehr: float
    faktor: float
    bezeichnung: str
    gebuehr: float
    stand: str

    def __str__(self) -> str:
        return (
            f"GKG-Berechnung (Streitwert {self.streitwert:,.2f} EUR, "
            f"Tabelle Stand {self.stand})\n"
            f"  1,0-Gebühr: {self.einfachgebuehr:,.2f} EUR\n"
            f"  {self.bezeichnung} ({self.faktor:g}): {self.gebuehr:,.2f} EUR\n"
            f"  (Gerichtsgebühren sind nicht umsatzsteuerpflichtig.)"
        )


def _lade_tabelle() -> dict:
    with _DATA.open(encoding="utf-8") as fh:
        return json.load(fh)


def einfachgebuehr(streitwert: float, tabelle: dict | None = None) -> Tuple[float, str]:
    """Return (1,0-Gebühr, STAND) for `streitwert` per Anlage 2 zu § 34 GKG."""
    if streitwert <= 0:
        raise ValueError("Streitwert muss > 0 sein")
    tab = tabelle or _lade_tabelle()
    stufen: List[List[float]] = tab["stufen"]
    stand: str = tab["stand"]

    for bis_wert, gebuehr in stufen:
        if streitwert <= bis_wert:
            return float(gebuehr), stand

    hoechststufe_wert, hoechststufe_gebuehr = stufen[-1]
    schritt = tab["ueber_hoechstwert"]["schritt"]
    zuschlag = tab["ueber_hoechstwert"]["zuschlag"]
    rest = streitwert - hoechststufe_wert
    schritte = -(-rest // schritt)
    return float(hoechststufe_gebuehr) + schritte * zuschlag, stand


def berechne(
    streitwert: float,
    faktor: float = 3.0,
    *,
    bezeichnung: str = "Verfahrensgebühr erste Instanz (KV 1210)",
) -> GKGErgebnis:
    """Compute the court fee = 1,0-Gebühr * Satz.

    Args:
        streitwert: Wert in EUR.
        faktor: Gebührensatz aus dem KV GKG (default 3,0 erste Instanz).
        bezeichnung: label for the position.
    """
    eg, stand = einfachgebuehr(streitwert)
    gebuehr = round(eg * faktor, 2)
    return GKGErgebnis(
        streitwert=streitwert,
        einfachgebuehr=eg,
        faktor=faktor,
        bezeichnung=bezeichnung,
        gebuehr=gebuehr,
        stand=stand,
    )
