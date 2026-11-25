import unittest

from toimituskulu import toimituskulu


class TestToimituskulu(unittest.TestCase):
    def test_nollan_euron_tilaus_maksaa(self):
        summa = 0.00
        tulos = toimituskulu(summa)
        self.assertEqual(tulos, 4.90)

    def test_alle_rajan_toimitus_maksaa(self):
        summa = 49.99
        tulos = toimituskulu(summa)
        self.assertEqual(tulos, 4.90)

    def test_tasan_rajalla_toimitus_on_ilmainen(self):
        summa = 50.00
        tulos = toimituskulu(summa)
        self.assertEqual(tulos, 0.00)

    def test_yli_rajan_toimitus_on_ilmainen(self):
        summa = 50.01
        tulos = toimituskulu(summa)
        self.assertEqual(tulos, 0.00)
