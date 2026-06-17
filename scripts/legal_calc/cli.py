#!/usr/bin/env python3
"""Command-line interface for the deterministic legal calculators.

Usage:
    python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 3 --einheit wochen --land BY
    python -m scripts.legal_calc.cli frist --ereignis 31.01.2026 --menge 1 --einheit monate
    python -m scripts.legal_calc.cli verjaehrung --entstehung 10.03.2023 --kenntnis 05.07.2023
    python -m scripts.legal_calc.cli rvg --wert 10000 --posten verfahren termin
    python -m scripts.legal_calc.cli gkg --wert 10000 --faktor 3.0
    python -m scripts.legal_calc.cli feiertage --jahr 2026 --land BY

Add --json to any subcommand for machine-readable output.
"""
from __future__ import annotations

import argparse
import dataclasses
import datetime as _dt
import json
import sys

from . import feiertage, fristen, gkg, rvg, verjaehrung


def _parse_date(s: str) -> _dt.date:
    for fmt in ("%d.%m.%Y", "%Y-%m-%d"):
        try:
            return _dt.datetime.strptime(s, fmt).date()
        except ValueError:
            continue
    raise argparse.ArgumentTypeError(f"Datum nicht erkannt: {s!r} (TT.MM.JJJJ erwartet)")


def _emit(obj, as_json: bool) -> None:
    if as_json:
        if dataclasses.is_dataclass(obj):
            payload = dataclasses.asdict(obj)
        elif isinstance(obj, dict):
            payload = obj
        else:
            payload = {"text": str(obj)}
        print(json.dumps(payload, ensure_ascii=False, indent=2, default=str))
    else:
        print(obj)


_RVG_POSTEN = {
    "verfahren": ("Verfahrensgebühr VV 3100", 1.3),
    "termin": ("Terminsgebühr VV 3104", 1.2),
    "geschaeft": ("Geschäftsgebühr VV 2300", 1.3),
    "einigung": ("Einigungsgebühr VV 1000", 1.5),
    "einigung-anhaengig": ("Einigungsgebühr VV 1003", 1.0),
}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Deterministische juristische Rechner")
    # --json is exposed on every subcommand (e.g. `frist --json`) via a shared
    # parent parser, matching the documented usage.
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--json", action="store_true", help="JSON-Ausgabe")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_frist = sub.add_parser("frist", parents=[common], help="Fristenberechnung §§ 187-193 BGB")
    p_frist.add_argument("--ereignis", type=_parse_date, required=True)
    p_frist.add_argument("--menge", type=int, required=True)
    p_frist.add_argument("--einheit", choices=fristen.UNITS, required=True)
    p_frist.add_argument("--art", choices=("ereignis", "beginn"), default="ereignis")
    p_frist.add_argument("--land", default="BUND")
    p_frist.add_argument("--kein-rollover", action="store_true",
                         help="§ 193 BGB nicht anwenden")

    p_verj = sub.add_parser("verjaehrung", parents=[common], help="Verjährung §§ 195-199 BGB")
    p_verj.add_argument("--entstehung", type=_parse_date, required=True)
    p_verj.add_argument("--kenntnis", type=_parse_date, default=None)
    p_verj.add_argument("--jahre", type=int, default=verjaehrung.REGELFRIST_JAHRE)
    p_verj.add_argument("--begehung", type=_parse_date, default=None,
                        help="für Schadensersatz-Vermögensschaden (§ 199 Abs. 3)")

    p_rvg = sub.add_parser("rvg", parents=[common], help="RVG-Gebühren § 13 RVG")
    p_rvg.add_argument("--wert", type=float, required=True)
    p_rvg.add_argument("--posten", nargs="+", choices=list(_RVG_POSTEN),
                       default=["verfahren", "termin"])
    p_rvg.add_argument("--ohne-pauschale", action="store_true")
    p_rvg.add_argument("--ust", type=float, default=0.19)

    p_gkg = sub.add_parser("gkg", parents=[common], help="GKG-Gerichtskosten § 34 GKG")
    p_gkg.add_argument("--wert", type=float, required=True)
    p_gkg.add_argument("--faktor", type=float, default=3.0)

    p_fei = sub.add_parser("feiertage", parents=[common], help="Gesetzliche Feiertage eines Jahres")
    p_fei.add_argument("--jahr", type=int, required=True)
    p_fei.add_argument("--land", default="BUND")

    args = parser.parse_args(argv)

    # Domain validation errors (bad Land, menge < 1, unknown einheit, ...) are
    # reported as a clean usage error, not an uncaught traceback.
    try:
        if args.cmd == "frist":
            res = fristen.berechne_frist(
                args.ereignis, args.menge, args.einheit,
                art=args.art, land=args.land, rollover=not args.kein_rollover,
            )
            _emit(res, args.json)
            hinweis = feiertage.gemeinde_konflikt(args.land, res.start_ereignis, res.fristende)
            if hinweis and not args.json:
                print(f"\n  ⚠ {hinweis}")

        elif args.cmd == "verjaehrung":
            if args.begehung:
                res = verjaehrung.schadensersatz_vermoegen(
                    args.entstehung, args.kenntnis, args.begehung)
            else:
                res = verjaehrung.regelverjaehrung(
                    args.entstehung, args.kenntnis, frist_jahre=args.jahre)
            _emit(res, args.json)

        elif args.cmd == "rvg":
            faktoren = [_RVG_POSTEN[p] for p in args.posten]
            res = rvg.berechne(args.wert, faktoren,
                               auslagenpauschale=not args.ohne_pauschale, ust_satz=args.ust)
            _emit(res, args.json)

        elif args.cmd == "gkg":
            res = gkg.berechne(args.wert, args.faktor)
            _emit(res, args.json)

        elif args.cmd == "feiertage":
            tage = feiertage.feiertage(args.jahr, args.land)
            if args.json:
                _emit({d.isoformat(): n for d, n in sorted(tage.items())}, True)
            else:
                print(f"Gesetzliche Feiertage {args.jahr} ({args.land}):")
                for d, n in sorted(tage.items()):
                    print(f"  {d:%d.%m.%Y} ({fristen._wochentag(d)}): {n}")
                hinweis = feiertage.gemeinde_hinweis(args.land)
                if hinweis:
                    print(f"\n  ⚠ {hinweis}")
    except ValueError as exc:
        parser.error(str(exc))

    return 0


if __name__ == "__main__":
    sys.exit(main())
