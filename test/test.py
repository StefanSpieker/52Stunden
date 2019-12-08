import unittest

from summe import summe


class TesteSumme(unittest.TestCase):
    def test_list_int(self):
        # Teste Daten
        daten = [1, 2, 3]
        result = summe(daten)
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
