#!/usr/bin/env python3
"""Kündigungsfristen im Arbeitsverhältnis nach § 622 BGB.

Computes the applicable notice period and the earliest permissible termination
date for an employment relationship, from the start of employment, the date the
notice is received (Zugang), and who is giving notice.

The tiered employer periods of § 622 Abs. 2 BGB are a pure statutory function of
completed years of service, and the "zum Fünfzehnten oder zum Ende eines
Kalendermonats" / "zum Ende eines Kalendermonats" anchoring is exactly the kind
of date arithmetic language models get wrong. This module does it deterministically.

Statutory basis:
- § 622 BGB   https://www.gesetze-im-internet.de/bgb/__622.html
- § 187 BGB   https://www.gesetze-im-internet.de/bgb/__187.html (Fristbeginn)
- § 193 BGB   https://www.gesetze-im-internet.de/bgb/__193.html

IMPORTANT — § 622 Abs. 2 Satz 2 BGB (Zeiten vor Vollendung des 25. Lebensjahres):
The statutory text still contains the rule that periods of employment before the
employee turned 25 are not counted. The EuGH held an equivalent rule to be
unlawful age discrimination (Rs. C-555/07, Kücükdeveci), and it is consequently
NOT applied by German courts. This module therefore defaults to
`beruecksichtige_zeiten_vor_25=True` (i.e. it counts them, the correct outcome).
The opposite behaviour is available only to reproduce the literal statutory text
and must never be used for advice.

Caveats:
- § 622 Abs. 4 BGB permits deviation by Tarifvertrag - including SHORTER periods.
  Where a TV applies, this calculator does not govern. Pass `tarifvertrag=True`
  to have the result flagged accordingly.
- § 622 Abs. 3 BGB (Probezeit, max. 6 Monate) gives 2 weeks to any day.
- § 622 Abs. 5 BGB limits individual shortening; single-contract extension of the
  employee's own period beyond the employer's is unlawful (Abs. 6 - Grundsatz der
  Gleichbehandlung beider Seiten).
- Zugang (receipt) is a legal question and an INPUT here, not a computation.
- Drafting aid, not legal advice.
"""
from __future__ import annotations

import calendar
import datetime as _dt
from dataclasses import dataclass, field
from typing import List, Optional

STAND = "2026-07-21"

# § 622 Abs. 2 S. 1 BGB: (vollendete Beschäftigungsjahre, Monate, ) - zum Monatsende.
# Ordered descending so the first match wins.
STUFEN_ARBEITGEBER = (
    (20, 7),
    (15, 6),
    (12, 5),
    (10, 4),
    (8, 3),
    (5, 2),
    (2, 1),
)


@dataclass
class KuendigungsfristErgebnis:
    eintritt: _dt.date
    zugang: _dt.date
    kuendigender: str                  # "arbeitgeber" | "arbeitnehmer"
    beschaeftigungsjahre: int
    probezeit: bool
    grundlage: str                     # the applicable § 622 provision
    frist_text: str                    # human-readable period
    termin_typ: str                    # "monatsende" | "15_oder_monatsende" | "beliebig"
    fruehester_termin: _dt.date        # the answer
    schritte: List[str] = field(default_factory=list)
    hinweise: List[str] = field(default_factory=list)
    stand: str = STAND

    def erklaerung(self) -> str:
        lines = [
            f"Eintritt:            {self.eintritt:%d.%m.%Y}",
            f"Zugang Kündigung:    {self.zugang:%d.%m.%Y}",
            f"Kündigender:         {self.kuendigender}",
            f"Beschäftigungsdauer: {self.beschaeftigungsjahre} volle Jahre",
            f"Grundlage:           {self.grundlage}",
            f"Frist:               {self.frist_text}",
            f"Termin:              {self.termin_typ}",
            "",
            "Rechenweg:",
        ]
        lines += [f"  - {s}" for s in self.schritte]
        if self.hinweise:
            lines += ["", "Hinweise:"] + [f"  ! {h}" for h in self.hinweise]
        lines += ["", f"Frühestmöglicher Beendigungstermin: {self.fruehester_termin:%d.%m.%Y}"]
        lines += [f"(Stand der Berechnungsgrundlage: {self.stand})"]
        return "\n".join(lines)


def _monatsende(d: _dt.date) -> _dt.date:
    return d.replace(day=calendar.monthrange(d.year, d.month)[1])


def _add_months(d: _dt.date, months: int) -> _dt.date:
    m = d.month - 1 + months
    year = d.year + m // 12
    month = m % 12 + 1
    day = min(d.day, calendar.monthrange(year, month)[1])
    return _dt.date(year, month, day)


def volle_beschaeftigungsjahre(
    eintritt: _dt.date,
    stichtag: _dt.date,
    geburtsdatum: Optional[_dt.date] = None,
    beruecksichtige_zeiten_vor_25: bool = True,
) -> int:
    """Completed years of service as at `stichtag` (§ 622 Abs. 2 BGB).

    The reference point is the Zugang of the notice, not the intended end date -
    st. Rspr.; the period must already be reached when notice is received.
    """
    beginn = eintritt
    if not beruecksichtige_zeiten_vor_25 and geburtsdatum is not None:
        vollendung_25 = _add_months(geburtsdatum, 25 * 12)
        if vollendung_25 > beginn:
            beginn = vollendung_25
    if stichtag < beginn:
        return 0
    jahre = stichtag.year - beginn.year
    if (stichtag.month, stichtag.day) < (beginn.month, beginn.day):
        jahre -= 1
    return max(0, jahre)


def berechne(
    eintritt: _dt.date,
    zugang: _dt.date,
    kuendigender: str = "arbeitgeber",
    probezeit: bool = False,
    tarifvertrag: bool = False,
    geburtsdatum: Optional[_dt.date] = None,
    beruecksichtige_zeiten_vor_25: bool = True,
) -> KuendigungsfristErgebnis:
    """Compute the earliest permissible termination date under § 622 BGB."""
    kuendigender = kuendigender.lower()
    if kuendigender not in ("arbeitgeber", "arbeitnehmer"):
        raise ValueError("kuendigender muss 'arbeitgeber' oder 'arbeitnehmer' sein")
    if zugang < eintritt:
        raise ValueError("Zugang der Kündigung liegt vor dem Eintrittsdatum")

    schritte: List[str] = []
    hinweise: List[str] = []

    jahre = volle_beschaeftigungsjahre(
        eintritt, zugang, geburtsdatum, beruecksichtige_zeiten_vor_25
    )
    schritte.append(
        f"§ 622: maßgeblich ist der Zugang ({zugang:%d.%m.%Y}); "
        f"volle Beschäftigungsjahre = {jahre}"
    )

    if not beruecksichtige_zeiten_vor_25:
        hinweise.append(
            "Zeiten vor Vollendung des 25. Lebensjahres wurden ausgeblendet "
            "(§ 622 Abs. 2 S. 2 BGB im Wortlaut). Diese Regelung ist wegen "
            "Altersdiskriminierung unionsrechtswidrig und darf der Beratung "
            "NICHT zugrunde gelegt werden."
        )

    # --- Probezeit, § 622 Abs. 3 BGB ---
    if probezeit:
        grundlage = "§ 622 Abs. 3 BGB (Probezeit)"
        frist_text = "2 Wochen"
        termin_typ = "beliebig"
        termin = zugang + _dt.timedelta(days=14)
        schritte.append(
            "§ 622 Abs. 3 BGB: während einer vereinbarten Probezeit (längstens "
            "sechs Monate) 2 Wochen, zu jedem beliebigen Tag"
        )
        hinweise.append(
            "Probezeit ist auf längstens sechs Monate begrenzt; danach gilt "
            "wieder Abs. 1 bzw. Abs. 2."
        )
        return _finish(
            eintritt, zugang, kuendigender, jahre, probezeit, grundlage,
            frist_text, termin_typ, termin, schritte, hinweise, tarifvertrag
        )

    # --- Arbeitnehmerkündigung: immer Grundfrist, Abs. 1 ---
    if kuendigender == "arbeitnehmer":
        grundlage = "§ 622 Abs. 1 BGB (Grundkündigungsfrist)"
        frist_text = "4 Wochen"
        termin_typ = "15_oder_monatsende"
        schritte.append(
            "Arbeitnehmerkündigung: die verlängerten Fristen des § 622 Abs. 2 BGB "
            "gelten nur für die Kündigung durch den Arbeitgeber"
        )
        basis = zugang + _dt.timedelta(days=28)
        schritte.append(f"4 Wochen ab Zugang = {basis:%d.%m.%Y} (frühester Ablauf)")
        termin = _naechster_15_oder_monatsende(basis)
        schritte.append(
            f"nächstzulässiger Termin (15. oder Monatsende) ab {basis:%d.%m.%Y} "
            f"= {termin:%d.%m.%Y}"
        )
        return _finish(
            eintritt, zugang, kuendigender, jahre, probezeit, grundlage,
            frist_text, termin_typ, termin, schritte, hinweise, tarifvertrag
        )

    # --- Arbeitgeberkündigung ---
    monate = 0
    for schwelle, m in STUFEN_ARBEITGEBER:
        if jahre >= schwelle:
            monate = m
            break

    if monate == 0:
        grundlage = "§ 622 Abs. 1 BGB (Grundkündigungsfrist)"
        frist_text = "4 Wochen"
        termin_typ = "15_oder_monatsende"
        schritte.append(
            "weniger als 2 volle Beschäftigungsjahre: keine Verlängerung nach "
            "§ 622 Abs. 2 BGB, es bleibt bei der Grundfrist"
        )
        basis = zugang + _dt.timedelta(days=28)
        schritte.append(f"4 Wochen ab Zugang = {basis:%d.%m.%Y} (frühester Ablauf)")
        termin = _naechster_15_oder_monatsende(basis)
        schritte.append(
            f"nächstzulässiger Termin (15. oder Monatsende) ab {basis:%d.%m.%Y} "
            f"= {termin:%d.%m.%Y}"
        )
    else:
        grundlage = f"§ 622 Abs. 2 S. 1 Nr. {_stufen_nummer(monate)} BGB"
        frist_text = f"{monate} Monat(e)"
        termin_typ = "monatsende"
        schritte.append(
            f"{jahre} volle Beschäftigungsjahre -> Stufe: {monate} Monat(e) "
            "zum Ende eines Kalendermonats"
        )
        basis = _add_months(zugang, monate)
        schritte.append(f"{monate} Monat(e) ab Zugang = {basis:%d.%m.%Y}")
        termin = _monatsende(basis)
        if termin < basis:
            termin = _monatsende(_add_months(basis, 1))
        schritte.append(f"Aufrundung auf das Monatsende = {termin:%d.%m.%Y}")

    return _finish(
        eintritt, zugang, kuendigender, jahre, probezeit, grundlage,
        frist_text, termin_typ, termin, schritte, hinweise, tarifvertrag
    )


def _stufen_nummer(monate: int) -> int:
    """Map the month count back to the Nr. in § 622 Abs. 2 S. 1 BGB."""
    mapping = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7}
    return mapping[monate]


def _naechster_15_oder_monatsende(ab: _dt.date) -> _dt.date:
    """Earliest 15th or end-of-month falling on or after `ab` (§ 622 Abs. 1 BGB)."""
    if ab.day <= 15:
        return ab.replace(day=15)
    me = _monatsende(ab)
    if ab <= me:
        return me
    nxt = _add_months(ab.replace(day=1), 1)
    return nxt.replace(day=15)


def _finish(
    eintritt, zugang, kuendigender, jahre, probezeit, grundlage,
    frist_text, termin_typ, termin, schritte, hinweise, tarifvertrag
) -> KuendigungsfristErgebnis:
    if tarifvertrag:
        hinweise.append(
            "Tarifvertrag angegeben: § 622 Abs. 4 BGB lässt abweichende - auch "
            "KÜRZERE - Fristen zu. Die tarifliche Regelung geht vor; dieses "
            "Ergebnis ist dann nur die gesetzliche Vergleichsgröße."
        )
    hinweise.append(
        "Zugang ist Rechtsfrage und Eingabe, keine Berechnung. Bei Zugang unter "
        "Abwesenden ist der Zeitpunkt der Möglichkeit der Kenntnisnahme maßgeblich."
    )
    hinweise.append(
        "§ 193 BGB (Verschiebung auf den nächsten Werktag) gilt für den "
        "Beendigungstermin NICHT - der Termin ist ein Endtermin, keine Frist "
        "zur Vornahme einer Handlung."
    )
    return KuendigungsfristErgebnis(
        eintritt=eintritt,
        zugang=zugang,
        kuendigender=kuendigender,
        beschaeftigungsjahre=jahre,
        probezeit=probezeit,
        grundlage=grundlage,
        frist_text=frist_text,
        termin_typ=termin_typ,
        fruehester_termin=termin,
        schritte=schritte,
        hinweise=hinweise,
    )
