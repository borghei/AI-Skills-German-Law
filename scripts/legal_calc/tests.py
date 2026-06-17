#!/usr/bin/env python3
"""Tests for the deterministic legal calculators (stdlib unittest).

Run:
    python -m unittest scripts.legal_calc.tests
    python -m scripts.legal_calc.tests

Fixtures are hand-computed from the statutes. Fee-table *amounts* are NOT
hard-asserted (they are version-pinned data that may be updated against current
law); instead the fee tests assert the calculation *logic* against synthetic
tables plus structural invariants of the shipped tables.
"""
from __future__ import annotations

import datetime as _dt
import unittest
from datetime import date

from . import feiertage, fristen, gkg, rvg, verjaehrung


class TestFeiertage(unittest.TestCase):
    def test_ostersonntag(self):
        self.assertEqual(feiertage.ostersonntag(2024), date(2024, 3, 31))
        self.assertEqual(feiertage.ostersonntag(2025), date(2025, 4, 20))
        self.assertEqual(feiertage.ostersonntag(2026), date(2026, 4, 5))

    def test_bundeseinheitlich(self):
        f = feiertage.feiertage(2026, "BUND")
        self.assertIn(date(2026, 1, 1), f)      # Neujahr
        self.assertIn(date(2026, 4, 3), f)      # Karfreitag (Ostern - 2)
        self.assertIn(date(2026, 10, 3), f)     # Tag der Deutschen Einheit
        self.assertIn(date(2026, 12, 26), f)    # 2. Weihnachtstag

    def test_laenderspezifisch(self):
        by = feiertage.feiertage(2026, "BY")
        be = feiertage.feiertage(2026, "BE")
        # Heilige Drei Könige: BY ja, BE nein
        self.assertIn(date(2026, 1, 6), by)
        self.assertNotIn(date(2026, 1, 6), be)
        # Fronleichnam 2026 = Ostern + 60 = 04.06.2026: BY ja, BE nein
        self.assertIn(date(2026, 6, 4), by)
        self.assertNotIn(date(2026, 6, 4), be)

    def test_reformationstag_yeargate(self):
        # HH bekam Reformationstag dauerhaft erst ab 2018
        self.assertIn(date(2018, 10, 31), feiertage.feiertage(2018, "HH"))
        # NW (West) hat dauerhaft keinen Reformationstag
        self.assertNotIn(date(2018, 10, 31), feiertage.feiertage(2018, "NW"))

    def test_reformationstag_2017_bundesweit(self):
        # 500. Reformationsjubiläum: 31.10.2017 war in ALLEN Ländern Feiertag.
        for land in ("NW", "BY", "BE", "HH", "BUND"):
            self.assertIn(date(2017, 10, 31), feiertage.feiertage(2017, land),
                          f"Reformationstag 2017 fehlt in {land}")

    def test_zusammenfallende_feiertage_namen(self):
        # 2008: Ostern 23.03. -> Christi Himmelfahrt = 01.05. = Tag der Arbeit.
        # Beide Namen müssen erhalten bleiben, nicht einer verworfen werden.
        name = feiertage.feiertage(2008, "BE")[date(2008, 5, 1)]
        self.assertIn("Tag der Arbeit", name)
        self.assertIn("Christi Himmelfahrt", name)

    def test_gemeinde_konflikt_datumsabhaengig(self):
        # BY-Hinweis nur, wenn der 15.08. im Fristfenster liegt.
        self.assertIsNone(feiertage.gemeinde_konflikt("BY", date(2026, 1, 2), date(2026, 1, 5)))
        self.assertIsNotNone(feiertage.gemeinde_konflikt("BY", date(2026, 8, 1), date(2026, 8, 20)))
        self.assertIsNone(feiertage.gemeinde_konflikt("BE", date(2026, 8, 1), date(2026, 8, 20)))

    def test_unbekanntes_land(self):
        with self.assertRaises(ValueError):
            feiertage.feiertage(2026, "XX")


class TestFristen(unittest.TestCase):
    def test_klagefrist_kschg_3_wochen(self):
        # § 4 KSchG: Zugang Do 15.01.2026, 3 Wochen, Ereignisfrist.
        r = fristen.berechne_frist(date(2026, 1, 15), 3, "wochen")
        self.assertEqual(r.fristbeginn, date(2026, 1, 16))
        self.assertEqual(r.fristende, date(2026, 2, 5))   # Do, Werktag
        self.assertFalse(r.verschoben)

    def test_monatsfrist_overflow_und_193(self):
        # 1 Monat ab 31.01.2026 -> 28.02.2026 (§ 188 III), Sa -> 02.03 (§ 193)
        r = fristen.berechne_frist(date(2026, 1, 31), 1, "monate")
        self.assertEqual(r.fristende_roh, date(2026, 2, 28))
        self.assertEqual(r.fristende, date(2026, 3, 2))
        self.assertTrue(r.verschoben)
        # ohne Rollover bleibt es der 28.02.
        r2 = fristen.berechne_frist(date(2026, 1, 31), 1, "monate", rollover=False)
        self.assertEqual(r2.fristende, date(2026, 2, 28))

    def test_tagesfrist_ereignis_vs_beginn(self):
        # Ereignisfrist: 10 Tage ab 01.06.2026 (Mo) -> 11.06.2026
        r = fristen.berechne_frist(date(2026, 6, 1), 10, "tage", rollover=False)
        self.assertEqual(r.fristende, date(2026, 6, 11))
        # Beginnfrist: 10 Tage, Anfangstag zählt -> 10.06.2026
        rb = fristen.berechne_frist(date(2026, 6, 1), 10, "tage",
                                    art="beginn", rollover=False)
        self.assertEqual(rb.fristende, date(2026, 6, 10))

    def test_lebensalter_beginnfrist(self):
        # § 187 II / § 188 II 2: geb. 01.01.2008 wird mit Ablauf 31.12.2025 18.
        r = fristen.berechne_frist(date(2008, 1, 1), 18, "jahre",
                                   art="beginn", rollover=False)
        self.assertEqual(r.fristende, date(2025, 12, 31))

    def test_beginnfrist_schaltjahr(self):
        # § 188 II Alt. 2 i.V.m. III: geb. 29.02.2008 wird mit Ablauf 28.02.2026
        # 18 (Zieljahr hat keinen 29.02. -> letzter Tag des Monats, NICHT 27.02.).
        r = fristen.berechne_frist(date(2008, 2, 29), 18, "jahre",
                                   art="beginn", rollover=False)
        self.assertEqual(r.fristende, date(2026, 2, 28))

    def test_beginnfrist_monatsende_overflow(self):
        # Beginnfrist 1 Monat ab 31.03.2026: Zielmonat April hat keinen 31. ->
        # Ablauf mit dem letzten Tag des Monats 30.04.2026 (nicht 29.04.).
        r = fristen.berechne_frist(date(2026, 3, 31), 1, "monate",
                                   art="beginn", rollover=False)
        self.assertEqual(r.fristende, date(2026, 4, 30))

    def test_feiertag_rollover_land(self):
        # Frist endet am 06.01. (Heilige Drei Könige) -> in BY verschoben, in BE nicht
        # 06.01.2026 ist ein Dienstag.
        # Ereignisfrist 5 Tage ab 01.01.2026 -> 06.01.2026.
        r_by = fristen.berechne_frist(date(2026, 1, 1), 5, "tage", land="BY")
        r_be = fristen.berechne_frist(date(2026, 1, 1), 5, "tage", land="BE")
        self.assertEqual(r_by.fristende_roh, date(2026, 1, 6))
        self.assertTrue(r_by.verschoben)          # Feiertag in BY
        self.assertEqual(r_by.fristende, date(2026, 1, 7))
        self.assertFalse(r_be.verschoben)         # kein Feiertag in BE
        self.assertEqual(r_be.fristende, date(2026, 1, 6))

    def test_naechster_werktag(self):
        # 03.01.2026 ist ein Samstag -> nächster Werktag Montag 05.01.2026
        self.assertEqual(fristen.naechster_werktag(date(2026, 1, 3)), date(2026, 1, 5))

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            fristen.berechne_frist(date(2026, 1, 1), 0, "tage")
        with self.assertRaises(ValueError):
            fristen.berechne_frist(date(2026, 1, 1), 1, "stunden")


class TestVerjaehrung(unittest.TestCase):
    def test_regelverjaehrung_ultimo(self):
        r = verjaehrung.regelverjaehrung(date(2023, 3, 10))
        self.assertEqual(r.verjaehrung_mit_ablauf, date(2026, 12, 31))

    def test_kenntnis_spaeter_jahr(self):
        # Entstehung 2022, Kenntnis 2023 -> maßgeblich 2023 -> Ende 31.12.2026
        r = verjaehrung.regelverjaehrung(date(2022, 11, 1), date(2023, 2, 1))
        self.assertEqual(r.verjaehrung_mit_ablauf, date(2026, 12, 31))

    def test_hoechstfrist_taggenau(self):
        r = verjaehrung.hoechstfrist(date(2020, 6, 15), 10)
        self.assertEqual(r.verjaehrung_mit_ablauf, date(2030, 6, 15))

    def test_schadensersatz_frueheste(self):
        # Entstehung 2020, Kenntnis erst 2028: Regel = 31.12.2031,
        # 10 J. ab Entstehung (10.05.2020) = 10.05.2030 -> früher.
        r = verjaehrung.schadensersatz_vermoegen(
            date(2020, 5, 10), date(2028, 1, 1), date(2020, 5, 10))
        self.assertEqual(r.verjaehrung_mit_ablauf, date(2030, 5, 10))


class TestRVGLogik(unittest.TestCase):
    SYNTH = {
        "stand": "test",
        "stufen": [[500, 49.0], [1000, 88.0], [5000, 300.0]],
        "ueber_hoechstwert": {"schritt": 1000, "zuschlag": 10.0},
    }

    def test_aufrundung_wertstufe(self):
        self.assertEqual(rvg.einfachgebuehr(1, self.SYNTH)[0], 49.0)
        self.assertEqual(rvg.einfachgebuehr(500, self.SYNTH)[0], 49.0)
        self.assertEqual(rvg.einfachgebuehr(501, self.SYNTH)[0], 88.0)
        self.assertEqual(rvg.einfachgebuehr(5000, self.SYNTH)[0], 300.0)

    def test_ueber_hoechstwert(self):
        # 5001 -> 1 angefangener 1000er-Schritt -> 300 + 10
        self.assertEqual(rvg.einfachgebuehr(5001, self.SYNTH)[0], 310.0)
        # 7000 -> 2 Schritte -> 320
        self.assertEqual(rvg.einfachgebuehr(7000, self.SYNTH)[0], 320.0)

    def test_negativ(self):
        with self.assertRaises(ValueError):
            rvg.einfachgebuehr(0, self.SYNTH)

    def test_berechnungslogik_invarianten(self):
        # gegen die echte (geshippte) Tabelle, aber nur Logik-Invarianten prüfen
        r = rvg.berechne(10000, [("Verfahrensgebühr", 1.3), ("Terminsgebühr", 1.2)])
        eg = r.einfachgebuehr
        self.assertEqual(r.positionen[0].betrag, round(eg * 1.3, 2))
        self.assertEqual(r.positionen[1].betrag, round(eg * 1.2, 2))
        self.assertEqual(r.zwischensumme_gebuehren,
                         round(round(eg * 1.3, 2) + round(eg * 1.2, 2), 2))
        # Auslagenpauschale: 20 %, höchstens 20 EUR (hier gedeckelt)
        self.assertEqual(r.auslagenpauschale, min(round(r.zwischensumme_gebuehren * 0.2, 2), 20.0))
        self.assertEqual(r.brutto, round(r.netto * 1.19, 2))


class TestGKGLogik(unittest.TestCase):
    SYNTH = {
        "stand": "test",
        "stufen": [[500, 38.0], [1000, 58.0], [5000, 161.0]],
        "ueber_hoechstwert": {"schritt": 1000, "zuschlag": 20.0},
    }

    def test_aufrundung(self):
        self.assertEqual(gkg.einfachgebuehr(700, self.SYNTH)[0], 58.0)
        self.assertEqual(gkg.einfachgebuehr(6000, self.SYNTH)[0], 161.0 + 20.0)

    def test_faktor(self):
        r = gkg.berechne(10000, 3.0)
        self.assertEqual(r.gebuehr, round(r.einfachgebuehr * 3.0, 2))


class TestGeshippteTabellen(unittest.TestCase):
    """Strukturelle Invarianten der versionierten JSON-Tabellen."""

    def _check(self, tab):
        self.assertIn("stand", tab)
        stufen = tab["stufen"]
        werte = [s[0] for s in stufen]
        gebuehren = [s[1] for s in stufen]
        self.assertEqual(werte, sorted(werte), "Wertstufen müssen aufsteigend sein")
        self.assertEqual(gebuehren, sorted(gebuehren), "Gebühren müssen monoton steigen")
        self.assertTrue(all(g > 0 for g in gebuehren))
        self.assertGreater(tab["ueber_hoechstwert"]["zuschlag"], 0)

    def test_rvg_tabelle(self):
        self._check(rvg._lade_tabelle())

    def test_gkg_tabelle(self):
        self._check(gkg._lade_tabelle())


if __name__ == "__main__":
    unittest.main(verbosity=2)
