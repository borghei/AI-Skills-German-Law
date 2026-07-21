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

from decimal import Decimal

from . import (
    feiertage,
    fristen,
    gkg,
    kuendigungsfristen,
    rvg,
    verjaehrung,
    verzugszinsen,
)


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


class TestKuendigungsfristen(unittest.TestCase):
    """§ 622 BGB - fixtures hand-computed from the statute."""

    def test_grundfrist_zum_monatsende(self):
        # Eintritt 2025, Zugang 05.03.2026 -> < 2 Jahre -> 4 Wochen zum 15./Monatsende.
        # 05.03. + 28 Tage = 02.04. -> naechster zulaessiger Termin ist der 15.04.
        r = kuendigungsfristen.berechne(date(2025, 1, 10), date(2026, 3, 5))
        self.assertEqual(r.beschaeftigungsjahre, 1)
        self.assertIn("Abs. 1", r.grundlage)
        self.assertEqual(r.fruehester_termin, date(2026, 4, 15))

    def test_grundfrist_rollt_auf_monatsende(self):
        # 20.03. + 28 Tage = 17.04. -> der 15.04. ist verstrichen -> 30.04.
        r = kuendigungsfristen.berechne(date(2025, 1, 10), date(2026, 3, 20))
        self.assertEqual(r.fruehester_termin, date(2026, 4, 30))

    def test_stufe_zwei_jahre_ein_monat(self):
        r = kuendigungsfristen.berechne(date(2024, 1, 10), date(2026, 3, 5))
        self.assertEqual(r.beschaeftigungsjahre, 2)
        self.assertEqual(r.frist_text, "1 Monat(e)")
        self.assertEqual(r.termin_typ, "monatsende")
        self.assertEqual(r.fruehester_termin, date(2026, 4, 30))

    def test_stufe_zwanzig_jahre_sieben_monate(self):
        r = kuendigungsfristen.berechne(date(2000, 1, 10), date(2026, 3, 5))
        self.assertGreaterEqual(r.beschaeftigungsjahre, 20)
        self.assertEqual(r.frist_text, "7 Monat(e)")
        self.assertEqual(r.fruehester_termin, date(2026, 10, 31))

    def test_alle_stufen_monoton(self):
        """Longer service must never yield a shorter period."""
        zugang = date(2026, 3, 5)
        letzte = date(1900, 1, 1)
        for jahre in (0, 1, 2, 5, 8, 10, 12, 15, 20, 30):
            eintritt = date(2026 - jahre, 1, 1)
            r = kuendigungsfristen.berechne(eintritt, zugang)
            self.assertGreaterEqual(r.fruehester_termin, letzte)
            letzte = r.fruehester_termin

    def test_arbeitnehmer_ohne_verlaengerung(self):
        """§ 622 Abs. 2 BGB applies only to employer notice."""
        ag = kuendigungsfristen.berechne(
            date(2000, 1, 10), date(2026, 3, 5), kuendigender="arbeitgeber")
        an = kuendigungsfristen.berechne(
            date(2000, 1, 10), date(2026, 3, 5), kuendigender="arbeitnehmer")
        self.assertEqual(an.frist_text, "4 Wochen")
        self.assertLess(an.fruehester_termin, ag.fruehester_termin)

    def test_probezeit_zwei_wochen_beliebiger_tag(self):
        r = kuendigungsfristen.berechne(
            date(2026, 1, 10), date(2026, 3, 5), probezeit=True)
        self.assertEqual(r.fruehester_termin, date(2026, 3, 19))
        self.assertEqual(r.termin_typ, "beliebig")

    def test_zeiten_vor_25_werden_default_mitgezaehlt(self):
        """Kücükdeveci: the Abs. 2 S. 2 carve-out must NOT be applied by default."""
        eintritt, geburt = date(2010, 1, 1), date(1992, 1, 1)
        zugang = date(2026, 3, 5)
        default = kuendigungsfristen.berechne(eintritt, zugang, geburtsdatum=geburt)
        wortlaut = kuendigungsfristen.berechne(
            eintritt, zugang, geburtsdatum=geburt,
            beruecksichtige_zeiten_vor_25=False)
        self.assertEqual(default.beschaeftigungsjahre, 16)
        self.assertEqual(wortlaut.beschaeftigungsjahre, 9)
        self.assertGreater(
            default.fruehester_termin, wortlaut.fruehester_termin,
            "Ausblenden der Zeiten vor 25 muss die Frist verkuerzen - "
            "genau deshalb ist es unionsrechtswidrig")
        self.assertTrue(any("unionsrechtswidrig" in h for h in wortlaut.hinweise))

    def test_tarifvertrag_wird_markiert(self):
        r = kuendigungsfristen.berechne(
            date(2000, 1, 10), date(2026, 3, 5), tarifvertrag=True)
        self.assertTrue(any("622 Abs. 4" in h for h in r.hinweise))

    def test_zugang_vor_eintritt_faehrt_fehler(self):
        with self.assertRaises(ValueError):
            kuendigungsfristen.berechne(date(2026, 5, 1), date(2026, 1, 1))


class TestVerzugszinsen(unittest.TestCase):
    """§§ 288, 247 BGB."""

    def test_fuenf_punkte_verbraucher(self):
        r = verzugszinsen.berechne(
            1000, date(2026, 1, 1), date(2027, 1, 1), basiszinssatz="2.00")
        self.assertEqual(r.zuschlag_punkte, Decimal("5"))
        self.assertIn("Abs. 1", r.grundlage)
        # 1000 EUR * 7 % * 365/365 = 70,00
        self.assertEqual(r.zinsen, Decimal("70.00"))

    def test_neun_punkte_b2b_entgeltforderung(self):
        r = verzugszinsen.berechne(
            1000, date(2026, 1, 1), date(2027, 1, 1), basiszinssatz="2.00",
            entgeltforderung=True, verbraucher_beteiligt=False,
            schuldner_ist_verbraucher=False)
        self.assertEqual(r.zuschlag_punkte, Decimal("9"))
        self.assertEqual(r.zinsen, Decimal("110.00"))
        self.assertEqual(r.pauschale, Decimal("40.00"))
        self.assertEqual(r.gesamt, Decimal("150.00"))

    def test_verbraucherbeteiligung_kippt_auf_fuenf_punkte(self):
        r = verzugszinsen.berechne(
            1000, date(2026, 1, 1), date(2027, 1, 1), basiszinssatz="2.00",
            entgeltforderung=True, verbraucher_beteiligt=True)
        self.assertEqual(r.zuschlag_punkte, Decimal("5"))
        self.assertTrue(any("greift NICHT" in h for h in r.hinweise))

    def test_pauschale_nur_gegen_nichtverbraucher(self):
        r = verzugszinsen.berechne(
            1000, date(2026, 1, 1), date(2026, 6, 1), basiszinssatz="2.00",
            entgeltforderung=True, schuldner_ist_verbraucher=True)
        self.assertEqual(r.pauschale, Decimal("0.00"))

    def test_segmentierung_bei_basiszinsaenderung(self):
        """§ 247 resets on 1.1./1.7. - the period must split."""
        r = verzugszinsen.berechne_segmente(
            10000, date(2025, 1, 1), date(2026, 1, 1),
            basiszinssaetze=[
                (date(2025, 1, 1), Decimal("1.00")),
                (date(2025, 7, 1), Decimal("3.00")),
            ])
        self.assertEqual(len(r.segmente), 2)
        self.assertEqual(r.segmente[0].zinssatz, Decimal("6.00"))
        self.assertEqual(r.segmente[1].zinssatz, Decimal("8.00"))
        self.assertEqual(sum(s.tage for s in r.segmente), 365)

    def test_schaltjahr_tagesbasis(self):
        r = verzugszinsen.berechne(
            1000, date(2024, 1, 1), date(2024, 3, 1), basiszinssatz="0.00")
        self.assertEqual(r.segmente[0].tagesbasis, 366)

    def test_stichtag_vor_verzug_faehrt_fehler(self):
        with self.assertRaises(ValueError):
            verzugszinsen.berechne(
                100, date(2026, 5, 1), date(2026, 1, 1), basiszinssatz="1.0")

    def test_negative_forderung_faehrt_fehler(self):
        with self.assertRaises(ValueError):
            verzugszinsen.berechne(
                -5, date(2026, 1, 1), date(2026, 5, 1), basiszinssatz="1.0")


if __name__ == "__main__":
    unittest.main(verbosity=2)
